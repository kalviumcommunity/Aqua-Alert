"""Preprocessing pipeline helpers for the Aqua-Alert ML workflow."""

from sklearn.preprocessing import StandardScaler


def build_preprocessing_pipeline() -> StandardScaler:
    """Create the reusable feature transformer used in training and inference."""
    return StandardScaler()