"""Artifact persistence helpers for the Aqua-Alert ML workflow."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

from joblib import dump, load

from src.config import (
    ARTIFACT_PATH,
    EVALUATION_REPORT_PATH,
    EXPERIMENT_LOG_PATH,
    LOGS_DIR,
    MODELS_DIR,
    REPORTS_DIR,
    SCALER_PATH,
)


def save_artifacts(model, preprocessor, feature_columns, artifact_path: Path = ARTIFACT_PATH) -> Path:
    """Persist the fitted preprocessing and model artifacts to disk."""
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    artifact_bundle = {
        "model": model,
        "preprocessor": preprocessor,
        "feature_columns": list(feature_columns),
    }
    dump(artifact_bundle, artifact_path)
    return artifact_path


def save_scaler(scaler, scaler_path: Path = SCALER_PATH) -> Path:
    """Persist the fitted MinMaxScaler for reuse during inference."""
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    dump(scaler, scaler_path)
    return scaler_path


def load_scaler(scaler_path: Path = SCALER_PATH):
    """Load the persisted MinMaxScaler without refitting."""
    if not scaler_path.exists():
        raise FileNotFoundError(f"Saved scaler was not found at {scaler_path}. Run training first.")
    return load(scaler_path)


def load_artifacts(artifact_path: Path = ARTIFACT_PATH) -> dict[str, Any]:
    """Load persisted model artifacts without refitting anything."""
    if not artifact_path.exists():
        raise FileNotFoundError(
            f"Saved artifacts were not found at {artifact_path}. Run training first."
        )
    return load(artifact_path)


def save_evaluation_report(report: Mapping[str, Any], report_path: Path = EVALUATION_REPORT_PATH) -> Path:
    """Persist evaluation metrics in a machine-readable report."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8") as report_file:
        json.dump(report, report_file, indent=2)
        report_file.write("\n")
    return report_path


def append_experiment_log(
    record: Mapping[str, Any],
    log_path: Path = EXPERIMENT_LOG_PATH,
) -> Path:
    """Append one structured experiment row to the log file."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "timestamp",
        "dataset_rows",
        "dataset_columns",
        "accuracy",
        "artifact_path",
        "scaler_path",
        "normalization_all_mins_close_to_0",
        "normalization_all_maxs_close_to_1",
        "report_path",
    ]

    log_exists = log_path.exists()
    row = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset_rows": record.get("dataset_rows", ""),
        "dataset_columns": record.get("dataset_columns", ""),
        "accuracy": record.get("accuracy", ""),
        "artifact_path": record.get("artifact_path", ""),
        "scaler_path": record.get("scaler_path", ""),
        "normalization_all_mins_close_to_0": record.get("normalization_all_mins_close_to_0", ""),
        "normalization_all_maxs_close_to_1": record.get("normalization_all_maxs_close_to_1", ""),
        "report_path": record.get("report_path", ""),
    }

    with log_path.open("a", newline="", encoding="utf-8") as log_file:
        writer = csv.DictWriter(log_file, fieldnames=fieldnames)
        if not log_exists:
            writer.writeheader()
        writer.writerow(row)

    return log_path