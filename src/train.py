"""Model training and artifact persistence for Aqua-Alert."""

from pathlib import Path

from joblib import dump
from sklearn.linear_model import LogisticRegression

from src.config import ARTIFACT_PATH, MODELS_DIR, RANDOM_STATE
from src.feature_engineering import build_preprocessor


def train_model(X_train, y_train, random_state: int = RANDOM_STATE):
    """Fit the preprocessor and classifier on the training split."""
    preprocessor = build_preprocessor()
    X_train_transformed = preprocessor.fit_transform(X_train)

    model = LogisticRegression(max_iter=1000, random_state=random_state)
    model.fit(X_train_transformed, y_train)

    return model, preprocessor


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
