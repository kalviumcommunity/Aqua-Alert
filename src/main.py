"""Entry point for the Aqua-Alert ML workflow."""

import argparse
from pathlib import Path

from data_loader import load_data
from evaluate import evaluate_model
from model import train_model
from preprocessing import preprocess_data


def build_argument_parser() -> argparse.ArgumentParser:
    """Create the command-line interface for the workflow."""
    parser = argparse.ArgumentParser(description="Run the Aqua-Alert ML pipeline.")
    parser.add_argument(
        "--data-path",
        type=Path,
        default=None,
        help="Optional CSV file to load instead of the synthetic dataset.",
    )
    return parser


def run_pipeline(data_path: Path | None = None) -> dict:
    """Execute the full machine learning workflow and return metrics."""
    dataset = load_data(data_path)
    X_train, X_test, y_train, y_test, feature_names = preprocess_data(dataset)
    model = train_model(X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)

    print("--- Aqua-Alert ML Workflow ---")
    print(f"Dataset shape: {dataset.shape}")
    print(f"Features used: {', '.join(feature_names)}")
    print(f"Accuracy: {metrics['accuracy']:.3f}")
    print("Confusion Matrix:")
    print(metrics["confusion_matrix"])
    print("Classification Report:")
    print(metrics["classification_report"])

    return metrics


def main() -> None:
    """Parse arguments and run the pipeline."""
    parser = build_argument_parser()
    args = parser.parse_args()
    run_pipeline(args.data_path)


if __name__ == "__main__":
    main()
