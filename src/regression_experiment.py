"""Linear regression baseline comparison workflow for Aqua-Alert."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.config import (
    CATEGORICAL_FEATURES,
    NUMERICAL_FEATURES,
    RANDOM_STATE,
    REGRESSION_REPORT_PATH,
    TARGET_COLUMN,
    TEST_SIZE,
)
from src.data_loader import load_data


def _build_regression_preprocessor() -> ColumnTransformer:
    """Build train-fit-only preprocessing for linear regression."""
    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), list(NUMERICAL_FEATURES)),
            ("cat", OneHotEncoder(handle_unknown="ignore"), list(CATEGORICAL_FEATURES)),
        ]
    )


def _regression_metrics(y_true, y_pred) -> dict:
    """Compute regression metric bundle used for both baseline and model."""
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    mae = float(mean_absolute_error(y_true, y_pred))
    r2 = float(r2_score(y_true, y_pred))
    return {
        "rmse": rmse,
        "mae": mae,
        "r2": r2,
    }


def _build_continuous_target(dataframe, random_state: int):
    """Build a reproducible continuous target for regression benchmarking."""
    rng = np.random.default_rng(random_state)

    sensor_effect = {
        "Industrial": 0.35,
        "Residential": 0.10,
        "Environmental": -0.05,
        "Rare_Specialized": 0.50,
    }
    location_effect = {
        "Urban": 0.20,
        "urban": 0.20,
        "Rural": -0.10,
        "RURAL ": -0.10,
        "Industrial": 0.30,
        "Remote": -0.20,
    }

    noise = rng.normal(loc=0.0, scale=0.25, size=len(dataframe))
    y = (
        0.12 * dataframe["ph_level"].to_numpy()
        + 0.03 * dataframe["temperature_c"].to_numpy()
        + 0.04 * dataframe["turbidity_ntu"].to_numpy()
        + 0.06 * dataframe["dissolved_oxygen_mg_l"].to_numpy()
        + 0.0005 * dataframe["conductivity_us_cm"].to_numpy()
        + 0.08 * dataframe["chlorine_mg_l"].to_numpy()
        + dataframe["sensor_type"].map(sensor_effect).fillna(0.0).to_numpy()
        + dataframe["location_category"].map(location_effect).fillna(0.0).to_numpy()
        + noise
    )
    return y.astype(float)


def run_linear_regression_baseline_experiment(
    target_column: str = TARGET_COLUMN,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
    report_path: Path = REGRESSION_REPORT_PATH,
) -> dict:
    """Train DummyRegressor(mean) and LinearRegression and compare on held-out test data."""
    dataframe = load_data(random_state=random_state)
    if target_column not in dataframe.columns:
        raise ValueError(f"Target column '{target_column}' was not found.")

    X = dataframe.drop(columns=[target_column])
    y = _build_continuous_target(dataframe, random_state=random_state)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
    )

    preprocessor = _build_regression_preprocessor()
    X_train_transformed = preprocessor.fit_transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)

    baseline_model = DummyRegressor(strategy="mean")
    baseline_model.fit(X_train_transformed, y_train)
    baseline_predictions = baseline_model.predict(X_test_transformed)
    baseline_metrics = _regression_metrics(y_test, baseline_predictions)

    linear_model = LinearRegression()
    linear_model.fit(X_train_transformed, y_train)
    linear_predictions = linear_model.predict(X_test_transformed)
    linear_metrics = _regression_metrics(y_test, linear_predictions)

    improvement = {
        "rmse_delta": baseline_metrics["rmse"] - linear_metrics["rmse"],
        "mae_delta": baseline_metrics["mae"] - linear_metrics["mae"],
        "mae_pct_improvement": (
            (baseline_metrics["mae"] - linear_metrics["mae"]) / baseline_metrics["mae"] * 100
            if baseline_metrics["mae"] != 0
            else 0.0
        ),
        "r2_delta": linear_metrics["r2"] - baseline_metrics["r2"],
    }

    print("Running cross-validation...")
    cv_scores = cross_val_score(
        linear_model,
        X_train_transformed,
        y_train,
        cv=5,
        scoring="neg_mean_absolute_error",
    )
    mae_cv_scores = -cv_scores

    feature_names = preprocessor.get_feature_names_out().tolist()
    coefficients = linear_model.coef_.tolist()
    coefficient_map = [
        {"feature": feature, "coefficient": float(coef)}
        for feature, coef in zip(feature_names, coefficients)
    ]
    sorted_coefficients = sorted(coefficient_map, key=lambda item: abs(item["coefficient"]), reverse=True)

    residuals = np.asarray(y_test) - linear_predictions
    residual_prediction_corr = float(np.corrcoef(linear_predictions, residuals)[0, 1])
    assumptions = {
        "residual_mean": float(np.mean(residuals)),
        "residual_std": float(np.std(residuals)),
        "residual_prediction_correlation": residual_prediction_corr,
        "notes": [
            "Residual mean near zero supports an unbiased fit on average.",
            "Residual-to-prediction correlation far from zero may indicate heteroscedasticity or nonlinearity.",
            "Outliers and synthetic data generation can violate strict linear regression assumptions.",
        ],
    }

    result = {
        "dataset_shape": list(dataframe.shape),
        "regression_target_definition": "continuous_index_from_features",
        "split": {
            "test_size": test_size,
            "random_state": random_state,
            "train_rows": int(X_train.shape[0]),
            "test_rows": int(X_test.shape[0]),
        },
        "baseline": {
            "model": "DummyRegressor(strategy='mean')",
            "metrics": baseline_metrics,
        },
        "linear_regression": {
            "model": "LinearRegression",
            "metrics": linear_metrics,
            "top_coefficients_by_absolute_value": sorted_coefficients[:10],
        },
        "comparison": improvement,
        "cross_validation": {
            "metric": "MAE",
            "scores": mae_cv_scores.tolist(),
            "mean": float(np.mean(mae_cv_scores)),
            "std": float(np.std(mae_cv_scores)),
        },
        "meaningful_improvement": bool(
            improvement["rmse_delta"] > 0 and improvement["mae_delta"] > 0 and improvement["r2_delta"] > 0
        ),
        "assumption_checks": assumptions,
    }

    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8") as report_file:
        json.dump(result, report_file, indent=2)
        report_file.write("\n")

    print("--- Linear Regression Baseline Comparison ---")
    print(f"Train/Test split: {X_train.shape[0]}/{X_test.shape[0]}")
    print("Baseline (DummyRegressor mean) metrics:")
    print(
        f"  RMSE={baseline_metrics['rmse']:.6f}, MAE={baseline_metrics['mae']:.6f}, "
        f"R2={baseline_metrics['r2']:.6f}"
    )
    print("LinearRegression metrics:")
    print(
        f"  RMSE={linear_metrics['rmse']:.6f}, MAE={linear_metrics['mae']:.6f}, "
        f"R2={linear_metrics['r2']:.6f}"
    )
    print(
        f"  RMSE delta={improvement['rmse_delta']:.6f}, "
        f"MAE delta={improvement['mae_delta']:.6f} "
        f"({improvement['mae_pct_improvement']:.2f}%), "
        f"R2 delta={improvement['r2_delta']:.6f}"
    )
    print(f"Cross-Validation MAE: {np.mean(mae_cv_scores):.6f} ± {np.std(mae_cv_scores):.6f}")
    print(f"Meaningful improvement: {result['meaningful_improvement']}")
    print(f"Regression report saved to: {report_path}")

    return result
