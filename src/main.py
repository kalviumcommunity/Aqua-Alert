"""Entry point for the Aqua-Alert ML training workflow."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import FEATURE_COLUMNS
from src.data_preprocessing import load_dataset, split_dataset
from src.evaluate import evaluate_model
from src.train import save_artifacts, train_model


def run_pipeline() -> dict:
    """Train, evaluate, and persist the model artifacts."""
    dataset = load_dataset()
    X_train, X_test, y_train, y_test = split_dataset(dataset)
    model, preprocessor = train_model(X_train, y_train)
    artifact_path = save_artifacts(model, preprocessor, FEATURE_COLUMNS)
    metrics = evaluate_model(model, preprocessor, X_test, y_test)

    print("--- Aqua-Alert Training Workflow ---")
    print(f"Dataset shape: {dataset.shape}")
    print(f"Features used: {', '.join(FEATURE_COLUMNS)}")
    print(f"Artifacts saved to: {artifact_path}")
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

