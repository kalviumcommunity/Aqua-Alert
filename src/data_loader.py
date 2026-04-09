"""Data loading utilities for the Aqua-Alert ML workflow."""

from pathlib import Path
from typing import Optional, Union

import pandas as pd
from sklearn.datasets import make_classification


def load_data(
    source_path: Optional[Union[str, Path]] = None,
    n_samples: int = 500,
    random_state: int = 42,
) -> pd.DataFrame:
    """Load tabular data from CSV or generate a synthetic dataset.

    Parameters
    ----------
    source_path:
        Optional path to a CSV file. When provided, the CSV must contain a
        target column named ``target``.
    n_samples:
        Number of synthetic rows to generate when no CSV is provided.
    random_state:
        Seed used for reproducible synthetic data generation.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing feature columns and a ``target`` column.
    """
    if source_path is not None:
        csv_path = Path(source_path)
        if not csv_path.exists():
            raise FileNotFoundError(f"Data file not found: {csv_path}")

        dataframe = pd.read_csv(csv_path)
        if "target" not in dataframe.columns:
            raise ValueError("CSV data must contain a 'target' column.")
        return dataframe

    feature_matrix, target = make_classification(
        n_samples=n_samples,
        n_features=6,
        n_informative=4,
        n_redundant=1,
        n_repeated=0,
        n_clusters_per_class=1,
        class_sep=1.4,
        random_state=random_state,
    )

    feature_columns = [
        "feature_1",
        "feature_2",
        "feature_3",
        "feature_4",
        "feature_5",
        "feature_6",
    ]

    dataframe = pd.DataFrame(feature_matrix, columns=feature_columns)
    dataframe["target"] = target
    return dataframe
