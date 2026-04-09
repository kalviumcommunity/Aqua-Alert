"""Model training utilities for the Aqua-Alert ML workflow."""

from sklearn.linear_model import LogisticRegression


def train_model(X_train, y_train, random_state: int = 42) -> LogisticRegression:
    """Train a logistic regression classifier on the prepared data."""
    model = LogisticRegression(max_iter=1000, random_state=random_state)
    model.fit(X_train, y_train)
    return model
