"""Model training helpers for the Aqua-Alert ML workflow."""

from __future__ import annotations

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from src.config import NUMERICAL_FEATURES, RANDOM_STATE, TARGET_COLUMN, TEST_SIZE
from src.preprocessing import build_preprocessing_pipeline, get_fitted_scaler


def verify_minmax_scaling(preprocessor, X_train) -> dict:
    """Verify MinMax scaling on training numerical features and return summary stats."""
    scaler = get_fitted_scaler(preprocessor)
    scaled_train_numerical = scaler.transform(X_train[list(NUMERICAL_FEATURES)])

    feature_min = scaled_train_numerical.min(axis=0)
    feature_max = scaled_train_numerical.max(axis=0)
    is_min_close_zero = np.isclose(feature_min, 0.0, atol=1e-9)
    is_max_close_one = np.isclose(feature_max, 1.0, atol=1e-9)

    per_feature = {
        feature: {
            "min": float(feature_min[idx]),
            "max": float(feature_max[idx]),
            "min_close_to_0": bool(is_min_close_zero[idx]),
            "max_close_to_1": bool(is_max_close_one[idx]),
        }
        for idx, feature in enumerate(NUMERICAL_FEATURES)
    }

    verification = {
        "all_mins_close_to_0": bool(np.all(is_min_close_zero)),
        "all_maxs_close_to_1": bool(np.all(is_max_close_one)),
        "per_feature": per_feature,
    }

    print("MinMax verification on training numerical features:")
    for feature, stats in per_feature.items():
        print(
            f"  {feature}: min={stats['min']:.6f}, max={stats['max']:.6f}, "
            f"min~0={stats['min_close_to_0']}, max~1={stats['max_close_to_1']}"
        )

    return verification

def train_model(
    dataframe,
    target_column: str = TARGET_COLUMN,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
):
    """Split the dataset, fit preprocessing on train only, and train the classifier."""
    if target_column not in dataframe.columns:
        raise ValueError(f"Target column '{target_column}' was not found.")

    X = dataframe.drop(columns=[target_column])
    y = dataframe[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    # Fit the preprocessing pipeline strictly on training features.
    preprocessor = build_preprocessing_pipeline()
    X_train_transformed = preprocessor.fit_transform(X_train)
    normalization_verification = verify_minmax_scaling(preprocessor, X_train)

    model = LogisticRegression(max_iter=1000, random_state=random_state)
    model.fit(X_train_transformed, y_train)

    return model, preprocessor, X_test, y_test, list(X.columns), normalization_verification
