"""Data loading, cleaning, and splitting helpers for Aqua-Alert."""

from pathlib import Path
from typing import Optional, Union

import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

from src.config import FEATURE_COLUMNS, RANDOM_STATE, SAMPLE_SIZE, TARGET_COLUMN, TEST_SIZE


def load_dataset(
    source_path: Optional[Union[str, Path]] = None,
    n_samples: int = SAMPLE_SIZE,
    random_state: int = RANDOM_STATE,
) -> pd.DataFrame:
    """Load a CSV dataset or create a reproducible synthetic dataset."""
    if source_path is not None:
        csv_path = Path(source_path)
        if not csv_path.exists():
            raise FileNotFoundError(f"Data file not found: {csv_path}")

        dataframe = pd.read_csv(csv_path)
        if TARGET_COLUMN not in dataframe.columns:
            raise ValueError(f"CSV data must contain a '{TARGET_COLUMN}' column.")
        return dataframe

    feature_matrix, target = make_classification(
        n_samples=n_samples,
        n_features=len(FEATURE_COLUMNS),
        n_informative=4,
        n_redundant=1,
        n_repeated=0,
        n_clusters_per_class=1,
        class_sep=1.4,
        random_state=random_state,
    )

    dataframe = pd.DataFrame(feature_matrix, columns=list(FEATURE_COLUMNS))
    dataframe[TARGET_COLUMN] = target
    return dataframe


def split_dataset(
    dataframe: pd.DataFrame,
    target_column: str = TARGET_COLUMN,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split features and target into train and test sets."""
    if target_column not in dataframe.columns:
        raise ValueError(f"Target column '{target_column}' was not found.")

    features = dataframe.drop(columns=[target_column])
    target = dataframe[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=test_size,
        random_state=random_state,
        stratify=target,
    )

    return X_train, X_test, y_train, y_test
