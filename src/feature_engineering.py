"""Backward-compatible wrappers for feature preprocessing."""

from src.preprocessing import build_preprocessing_pipeline


def build_preprocessor() -> StandardScaler:
    """Create the feature transformer used during training and prediction."""
    return build_preprocessing_pipeline()
