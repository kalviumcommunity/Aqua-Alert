"""Preprocessing pipeline helpers for the Aqua-Alert ML workflow."""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.config import CATEGORICAL_FEATURES, NUMERICAL_FEATURES


def build_preprocessing_pipeline() -> ColumnTransformer:
    """Create the reusable feature transformer used in training and inference."""
    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), list(NUMERICAL_FEATURES)),
            ("cat", OneHotEncoder(handle_unknown="ignore"), list(CATEGORICAL_FEATURES)),
        ]
    )


def get_fitted_scaler(preprocessor: ColumnTransformer) -> StandardScaler:
    """Return the fitted StandardScaler from a fitted ColumnTransformer."""
    if not hasattr(preprocessor, "named_transformers_"):
        raise ValueError("Preprocessor must be fitted before extracting the scaler.")

    scaler = preprocessor.named_transformers_.get("num")
    if scaler is None:
        raise ValueError("No numerical scaler named 'num' was found in the preprocessor.")
    return scaler