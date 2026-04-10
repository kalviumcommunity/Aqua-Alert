"""Model training and artifact persistence for Aqua-Alert."""

from sklearn.linear_model import LogisticRegression

from src.config import RANDOM_STATE
from src.feature_engineering import build_preprocessor


def train_model(X_train, y_train, random_state: int = RANDOM_STATE):
    """Fit the preprocessor and classifier on the training split."""
    preprocessor = build_preprocessor()
    X_train_transformed = preprocessor.fit_transform(X_train)

    model = LogisticRegression(max_iter=1000, random_state=random_state)
    model.fit(X_train_transformed, y_train)

    return model, preprocessor
