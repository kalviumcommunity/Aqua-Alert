"""Entry point for the Aqua-Alert ML training workflow."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data_loader import load_data
from src.evaluate import compare_model_vs_baseline, evaluate_classifier
from src.persistence import append_experiment_log, save_artifacts, save_evaluation_report, save_scaler
from src.preprocessing import get_fitted_scaler
from src.train import train_model


def run_pipeline() -> dict:
    """Train, evaluate, and persist the model artifacts."""
    dataset = load_data()
    (
        model,
        baseline_model,
        preprocessor,
        X_test,
        y_test,
        feature_columns,
        normalization_verification,
        baseline_strategy,
    ) = train_model(dataset)
    artifact_path = save_artifacts(model, preprocessor, feature_columns)
    scaler = get_fitted_scaler(preprocessor)
    scaler_path = save_scaler(scaler)
    model_metrics = evaluate_classifier(model, preprocessor, X_test, y_test)
    baseline_metrics = evaluate_classifier(baseline_model, preprocessor, X_test, y_test)
    baseline_comparison = compare_model_vs_baseline(model_metrics, baseline_metrics)
    report_path = save_evaluation_report(
        {
            "dataset_shape": list(dataset.shape),
            "features": feature_columns,
            "baseline_strategy": baseline_strategy,
            "normalization_verification": normalization_verification,
            "primary_model_metrics": model_metrics,
            "baseline_metrics": baseline_metrics,
            "model_vs_baseline": baseline_comparison,
        }
    )
    log_path = append_experiment_log(
        {
            "dataset_rows": dataset.shape[0],
            "dataset_columns": dataset.shape[1],
            "accuracy": round(model_metrics["accuracy"], 6),
            "baseline_accuracy": round(baseline_metrics["accuracy"], 6),
            "accuracy_delta": round(baseline_comparison["improvement"]["accuracy_delta"], 6),
            "artifact_path": str(artifact_path),
            "scaler_path": str(scaler_path),
            "normalization_all_mins_close_to_0": normalization_verification["all_mins_close_to_0"],
            "normalization_all_maxs_close_to_1": normalization_verification["all_maxs_close_to_1"],
            "report_path": str(report_path),
        }
    )

    print("--- Aqua-Alert Training Workflow ---")
    print(f"Dataset shape: {dataset.shape}")
    print(f"Features used: {', '.join(feature_columns)}")
    print(f"Baseline strategy: DummyClassifier(strategy='{baseline_strategy}')")
    print(f"Artifacts saved to: {artifact_path}")
    print(f"Scaler saved to: {scaler_path}")
    print(
        "Normalization verification "
        f"(all mins~0, all maxs~1): "
        f"({normalization_verification['all_mins_close_to_0']}, "
        f"{normalization_verification['all_maxs_close_to_1']})"
    )
    print(f"Evaluation report saved to: {report_path}")
    print(f"Experiment log updated at: {log_path}")
    print("--- Model vs Baseline Comparison ---")
    print(
        f"Primary accuracy: {model_metrics['accuracy']:.3f} | "
        f"Baseline accuracy: {baseline_metrics['accuracy']:.3f} | "
        f"Delta: {baseline_comparison['improvement']['accuracy_delta']:+.3f}"
    )
    print(
        f"Primary macro F1: {model_metrics['f1_macro']:.3f} | "
        f"Baseline macro F1: {baseline_metrics['f1_macro']:.3f} | "
        f"Delta: {baseline_comparison['improvement']['f1_macro_delta']:+.3f}"
    )
    print("Primary Model Confusion Matrix:")
    print(model_metrics["confusion_matrix"])
    print("Baseline Confusion Matrix:")
    print(baseline_metrics["confusion_matrix"])
    print("Primary Classification Report:")
    print(model_metrics["classification_report"])
    print("Baseline Classification Report:")
    print(baseline_metrics["classification_report"])

    return {
        "primary_model_metrics": model_metrics,
        "baseline_metrics": baseline_metrics,
        "model_vs_baseline": baseline_comparison,
    }


def main() -> None:
    """Run the training workflow."""
    run_pipeline()


if __name__ == "__main__":
    main()

