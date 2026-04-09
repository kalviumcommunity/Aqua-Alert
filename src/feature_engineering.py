"""Reusable feature transformations for the Aqua-Alert ML workflow."""

from sklearn.preprocessing import StandardScaler


def build_preprocessor() -> StandardScaler:
    """Create the feature transformer used during training and prediction."""
    return StandardScaler()
