"""Raw data loading helpers for the Aqua-Alert ML workflow."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Union

import pandas as pd
from sklearn.datasets import make_classification

from src.config import FEATURE_COLUMNS, RANDOM_STATE, SAMPLE_SIZE, TARGET_COLUMN


def load_data(
    source_path: Optional[Union[str, Path]] = None,
    n_samples: int = SAMPLE_SIZE,
    random_state: int = RANDOM_STATE,
) -> pd.DataFrame:
    """Load raw data without splitting or feature engineering."""
    if source_path is not None:
        csv_path = Path(source_path)
        if not csv_path.exists():
            raise FileNotFoundError(f"Data file not found: {csv_path}")

        dataframe = pd.read_csv(csv_path)
        if dataframe.empty:
            raise ValueError(f"Loaded dataset is empty: {csv_path}")
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