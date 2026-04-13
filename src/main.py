"""Entry point for the Aqua-Alert ML training workflow."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data_loader import load_data
from src.evaluate import evaluate_model
from src.persistence import append_experiment_log, save_artifacts, save_evaluation_report, save_scaler
from src.preprocessing import get_fitted_scaler
from src.train import train_model


def run_pipeline() -> dict:
    """Train, evaluate, and persist the model artifacts."""
    dataset = load_data()
    model, preprocessor, X_test, y_test, feature_columns = train_model(dataset)
    artifact_path = save_artifacts(model, preprocessor, feature_columns)
    scaler = get_fitted_scaler(preprocessor)
    scaler_path = save_scaler(scaler)
    metrics = evaluate_model(model, preprocessor, X_test, y_test)
    report_path = save_evaluation_report(
        {
            "dataset_shape": list(dataset.shape),
            "features": feature_columns,
            **metrics,
        }
    )
    log_path = append_experiment_log(
        {
            "dataset_rows": dataset.shape[0],
            "dataset_columns": dataset.shape[1],
            "accuracy": round(metrics["accuracy"], 6),
            "artifact_path": str(artifact_path),
            "scaler_path": str(scaler_path),
            "report_path": str(report_path),
        }
    )

    print("--- Aqua-Alert Training Workflow ---")
    print(f"Dataset shape: {dataset.shape}")
    print(f"Features used: {', '.join(feature_columns)}")
    print(f"Artifacts saved to: {artifact_path}")
    print(f"Scaler saved to: {scaler_path}")
    print(f"Evaluation report saved to: {report_path}")
    print(f"Experiment log updated at: {log_path}")
    print(f"Accuracy: {metrics['accuracy']:.3f}")
    print("Confusion Matrix:")
    print(metrics["confusion_matrix"])
    print("Classification Report:")
    print(metrics["classification_report"])

    return metrics


def main() -> None:
    """Run the training workflow."""
    run_pipeline()


if __name__ == "__main__":
    main()

