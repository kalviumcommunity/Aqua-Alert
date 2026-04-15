"""Evaluation helpers for the Aqua-Alert ML workflow."""

from typing import Any, Dict

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def evaluate_classifier(model, preprocessor, X_test, y_test) -> Dict[str, Any]:
    """Score a fitted classifier on held-out data using a common metric bundle."""
    X_test_transformed = preprocessor.transform(X_test)
    predictions = model.predict(X_test_transformed)
    report_dict = classification_report(
        y_test,
        predictions,
        zero_division=0,
        output_dict=True,
    )

    return {
        "accuracy": accuracy_score(y_test, predictions),
        "f1_macro": report_dict["macro avg"]["f1-score"],
        "precision_macro": report_dict["macro avg"]["precision"],
        "recall_macro": report_dict["macro avg"]["recall"],
        "per_class": {
            label: value
            for label, value in report_dict.items()
            if label not in {"accuracy", "macro avg", "weighted avg"}
        },
        "classification_report": classification_report(
            y_test,
            predictions,
            zero_division=0,
        ),
        "confusion_matrix": confusion_matrix(y_test, predictions).tolist(),
    }


def compare_model_vs_baseline(model_metrics: Dict[str, Any], baseline_metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Return side-by-side comparison and deltas for model vs baseline."""
    return {
        "model": {
            "accuracy": model_metrics["accuracy"],
            "f1_macro": model_metrics["f1_macro"],
            "precision_macro": model_metrics["precision_macro"],
            "recall_macro": model_metrics["recall_macro"],
        },
        "baseline": {
            "accuracy": baseline_metrics["accuracy"],
            "f1_macro": baseline_metrics["f1_macro"],
            "precision_macro": baseline_metrics["precision_macro"],
            "recall_macro": baseline_metrics["recall_macro"],
        },
        "improvement": {
            "accuracy_delta": model_metrics["accuracy"] - baseline_metrics["accuracy"],
            "f1_macro_delta": model_metrics["f1_macro"] - baseline_metrics["f1_macro"],
            "precision_macro_delta": model_metrics["precision_macro"] - baseline_metrics["precision_macro"],
            "recall_macro_delta": model_metrics["recall_macro"] - baseline_metrics["recall_macro"],
        },
    }


def evaluate_model(model, preprocessor, X_test, y_test) -> Dict[str, Any]:
    """Backward-compatible wrapper around evaluate_classifier."""
    return evaluate_classifier(model, preprocessor, X_test, y_test)
