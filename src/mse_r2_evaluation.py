"""MSE and R2 evaluation workflow for Aqua-Alert regression models."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.config import (
    CATEGORICAL_FEATURES,
    NUMERICAL_FEATURES,
    RANDOM_STATE,
    REPORTS_DIR,
    TARGET_COLUMN,
    TEST_SIZE,
)
from src.data_loader import load_data


def _build_continuous_target(dataframe, random_state: int):
    """Build a reproducible continuous target for regression benchmarking."""
    rng = np.random.default_rng(random_state)

    sensor_effect = {
        "Industrial": 15.0,
        "Residential": 5.0,
        "Environmental": -2.0,
        "Rare_Specialized": 25.0,
    }
    location_effect = {
        "Urban": 10.0,
        "urban": 10.0,
        "Rural": -5.0,
        "RURAL ": -5.0,
        "Industrial": 20.0,
        "Remote": -10.0,
    }

    # Increasing target scale to represent "lakhs" as per scenario
    noise = rng.normal(loc=0.0, scale=10.0, size=len(dataframe))
    y = (
        12.0 * dataframe["ph_level"].to_numpy()
        + 3.0 * dataframe["temperature_c"].to_numpy()
        + 4.0 * dataframe["turbidity_ntu"].to_numpy()
        + 6.0 * dataframe["dissolved_oxygen_mg_l"].to_numpy()
        + 0.05 * dataframe["conductivity_us_cm"].to_numpy()
        + 8.0 * dataframe["chlorine_mg_l"].to_numpy()
        + dataframe["sensor_type"].map(sensor_effect).fillna(0.0).to_numpy()
        + dataframe["location_category"].map(location_effect).fillna(0.0).to_numpy()
        + 100.0  # Base revenue
        + noise
    )
    return y.astype(float)


def run_evaluation_experiment():
    """Execute the full evaluation pipeline: split, baseline, model training, and metrics."""
    # 1. Load data
    dataframe = load_data(random_state=RANDOM_STATE)
    
    # 2. Create target (Continuous revenue in lakhs)
    X = dataframe.drop(columns=[TARGET_COLUMN])
    y = _build_continuous_target(dataframe, random_state=RANDOM_STATE)

    # 3. Train-Test Split (Ensures no leakage)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    # 4. Define Preprocessing & Pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), list(NUMERICAL_FEATURES)),
            ("cat", OneHotEncoder(handle_unknown="ignore"), list(CATEGORICAL_FEATURES)),
        ]
    )

    model_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression()),
        ]
    )

    # 5. Baseline Implementation (DummyRegressor)
    baseline = DummyRegressor(strategy="mean")
    baseline.fit(X_train, y_train)
    y_pred_baseline = baseline.predict(X_test)

    # 6. Model Training
    model_pipeline.fit(X_train, y_train)
    y_pred_model = model_pipeline.predict(X_test)

    # 7. Compute Metrics (The "Part 1" requirements)
    def compute_metrics(y_true, y_pred):
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_true, y_pred)
        return {"MSE": float(mse), "RMSE": float(rmse), "R2": float(r2)}

    baseline_metrics = compute_metrics(y_test, y_pred_baseline)
    model_metrics = compute_metrics(y_test, y_pred_model)

    # 8. Cross-Validation
    print("Running cross-validation...")
    cv_r2 = cross_val_score(model_pipeline, X_train, y_train, cv=5, scoring="r2")
    cv_neg_mse = cross_val_score(
        model_pipeline, X_train, y_train, cv=5, scoring="neg_mean_squared_error"
    )
    cv_rmse = np.sqrt(-cv_neg_mse)

    # 9. Results Interpretation
    results = {
        "baseline": baseline_metrics,
        "model": model_metrics,
        "cross_validation": {
            "r2_scores": cv_r2.tolist(),
            "r2_mean": float(np.mean(cv_r2)),
            "r2_std": float(np.std(cv_r2)),
            "rmse_scores": cv_rmse.tolist(),
            "rmse_mean": float(np.mean(cv_rmse)),
            "rmse_std": float(np.std(cv_rmse)),
        },
    }

    # 10. Output and Reporting
    print("\n" + "="*40)
    print(" REGRESSION EVALUATION REPORT ")
    print("="*40)
    print("\n--- Baseline vs Model Comparison ---")
    comparison_df = pd.DataFrame([baseline_metrics, model_metrics], index=["Baseline (Mean)", "Linear Regression"])
    print(comparison_df)

    print("\n--- Cross-Validation Results (5 Folds) ---")
    print(f"R2 Scores: {cv_r2}")
    print(f"R2 Mean: {np.mean(cv_r2):.4f} ± {np.std(cv_r2):.4f}")
    print(f"RMSE Mean: {np.mean(cv_rmse):.4f} ± {np.std(cv_rmse):.4f}")

    # Interpretation Questions
    improvement = model_metrics["RMSE"] < baseline_metrics["RMSE"]
    r2_val = model_metrics["R2"]
    
    print("\n--- Interpretation ---")
    print(f"1. Does the model outperform baseline? {'Yes' if improvement else 'No'}")
    print(f"2. R2 Value Indicaiton: {r2_val:.4f} of the variance in revenue is explained by the model.")
    print(f"3. RMSE Acceptability: RMSE of {model_metrics['RMSE']:.2f} relative to target mean {np.mean(y):.2f}.")
    print(f"4. Result Stability: CV R2 std is {np.std(cv_r2):.4f}. Low values suggest stability.")
    
    negative_r2 = any(score < 0 for score in cv_r2)
    if negative_r2:
        print("5. ALERT: Negative R2 detected in one or more folds! This indicates the model performs worse than the mean for that subset.")

    # Save report
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_DIR / "mse_r2_evaluation_report.json"
    with open(report_path, "w") as f:
        json.dump(results, f, indent=4)
    
    return results


if __name__ == "__main__":
    run_evaluation_experiment()
