"""Preprocessing utilities for the Aqua-Alert ML workflow."""

from typing import List, Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocess_data(
    dataframe: pd.DataFrame,
    target_column: str = "target",
    test_size: float = 0.2,
    random_state: int = 42,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, List[str]]:
    """Split the dataset and scale numeric features.

    Parameters
    ----------
    dataframe:
        Input table containing features and the target column.
    target_column:
        Name of the label column to separate from features.
    test_size:
        Proportion of the dataset reserved for evaluation.
    random_state:
        Seed used for reproducible splits.

    Returns
    -------
    tuple
        Scaled training features, scaled test features, training labels,
        test labels, and the ordered feature names.
    """
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

    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train),
        columns=features.columns,
        index=X_train.index,
    )
    X_test_scaled = pd.DataFrame(
        scaler.transform(X_test),
        columns=features.columns,
        index=X_test.index,
    )

    return X_train_scaled, X_test_scaled, y_train, y_test, list(features.columns)
