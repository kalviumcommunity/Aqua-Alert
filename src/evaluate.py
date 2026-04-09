"""Evaluation helpers for the Aqua-Alert ML workflow."""

from typing import Any, Dict

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def evaluate_model(model, preprocessor, X_test, y_test) -> Dict[str, Any]:
    """Score the fitted model on held-out data."""
    X_test_transformed = preprocessor.transform(X_test)
    predictions = model.predict(X_test_transformed)

    return {
        "accuracy": accuracy_score(y_test, predictions),
        "classification_report": classification_report(
            y_test,
            predictions,
            zero_division=0,
        ),
        "confusion_matrix": confusion_matrix(y_test, predictions),
    }
