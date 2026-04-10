"""Shared configuration for the Aqua-Alert ML workflow."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"
ARTIFACT_PATH = MODELS_DIR / "aqua_alert_artifacts.joblib"
EVALUATION_REPORT_PATH = REPORTS_DIR / "evaluation_report.json"
EXPERIMENT_LOG_PATH = LOGS_DIR / "experiment_log.csv"

RANDOM_STATE = 42
TEST_SIZE = 0.2
SAMPLE_SIZE = 500
TARGET_COLUMN = "target"

FEATURE_COLUMNS = (
    "feature_1",
    "feature_2",
    "feature_3",
    "feature_4",
    "feature_5",
    "feature_6",
)
