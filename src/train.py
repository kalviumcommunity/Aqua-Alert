"""Model training helpers for the Aqua-Alert ML workflow."""

from __future__ import annotations

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from src.config import RANDOM_STATE, TARGET_COLUMN, TEST_SIZE
from src.preprocessing import build_preprocessing_pipeline

def train_model(
    dataframe,
    target_column: str = TARGET_COLUMN,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
):
    """Split the dataset, fit preprocessing on train only, and train the classifier."""
    if target_column not in dataframe.columns:
        raise ValueError(f"Target column '{target_column}' was not found.")

    X = dataframe.drop(columns=[target_column])
    y = dataframe[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    # Fit the preprocessing pipeline strictly on training features.
    preprocessor = build_preprocessing_pipeline()
    X_train_transformed = preprocessor.fit_transform(X_train)

    model = LogisticRegression(max_iter=1000, random_state=random_state)
    model.fit(X_train_transformed, y_train)

    return model, preprocessor, X_test, y_test, list(X.columns)
