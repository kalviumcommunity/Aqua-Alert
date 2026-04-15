"""Shared configuration for the Aqua-Alert ML workflow."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"
ARTIFACT_PATH = MODELS_DIR / "aqua_alert_artifacts.joblib"
SCALER_PATH = MODELS_DIR / "minmax_scaler.pkl"
EVALUATION_REPORT_PATH = REPORTS_DIR / "evaluation_report.json"
EXPERIMENT_LOG_PATH = LOGS_DIR / "experiment_log.csv"

RANDOM_STATE = 42
TEST_SIZE = 0.2
SAMPLE_SIZE = 500
TARGET_COLUMN = "target"

NUMERICAL_FEATURES = (
    "ph_level",
    "temperature_c",
    "turbidity_ntu",
    "dissolved_oxygen_mg_l",
    "conductivity_us_cm",
    "chlorine_mg_l",
)

CATEGORICAL_FEATURES = (
    "sensor_type",
    "location_category",
)

FEATURE_COLUMNS = NUMERICAL_FEATURES + CATEGORICAL_FEATURES
