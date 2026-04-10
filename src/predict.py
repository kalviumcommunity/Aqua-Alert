"""Prediction helpers for the Aqua-Alert ML workflow."""

from pathlib import Path
import sys
from typing import Any, Mapping

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd

from src.data_loader import load_data
from src.persistence import load_artifacts


def predict(model_artifacts: Mapping[str, Any], input_frame: pd.DataFrame) -> pd.Series:
    """Transform the input features and return predictions."""
    feature_columns = model_artifacts["feature_columns"]
    preprocessor = model_artifacts["preprocessor"]
    model = model_artifacts["model"]

    missing_columns = [column for column in feature_columns if column not in input_frame.columns]
    if missing_columns:
        raise ValueError(f"Input data is missing required columns: {', '.join(missing_columns)}")

    feature_frame = input_frame.loc[:, feature_columns]
    transformed_features = preprocessor.transform(feature_frame)
    predictions = model.predict(transformed_features)
    return pd.Series(predictions, name="prediction")


def main() -> None:
    """Run a simple prediction example using the saved artifact bundle."""
    artifacts = load_artifacts()
    sample_input = load_data(n_samples=5, random_state=1).drop(columns=["target"]).iloc[[0]]
    prediction = predict(artifacts, sample_input)

    print("--- Aqua-Alert Prediction ---")
    print(sample_input)
    print("Prediction:")
    print(prediction.to_string(index=False))


if __name__ == "__main__":
    main()
