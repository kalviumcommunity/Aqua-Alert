"""Raw data loading helpers for the Aqua-Alert ML workflow."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Union

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification

from src.config import (
    CATEGORICAL_FEATURES,
    NUMERICAL_FEATURES,
    RANDOM_STATE,
    SAMPLE_SIZE,
    TARGET_COLUMN,
)


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

    # Set seed for reproducibility
    np.random.seed(random_state)

    # Generate synthetic numerical data
    feature_matrix, target = make_classification(
        n_samples=n_samples,
        n_features=len(NUMERICAL_FEATURES),
        n_informative=4,
        n_redundant=1,
        n_repeated=0,
        n_clusters_per_class=1,
        class_sep=1.2,
        random_state=random_state,
    )

    dataframe = pd.DataFrame(feature_matrix, columns=list(NUMERICAL_FEATURES))
    dataframe[TARGET_COLUMN] = target

    # Inject skewness and outliers into 'conductivity_us_cm'
    # Exponential transform creates high right skew
    dataframe["conductivity_us_cm"] = np.exp(dataframe["conductivity_us_cm"]) + 500
    
    # Add some extreme outliers to conductivity
    outlier_idx_cond = np.random.choice(dataframe.index, size=5, replace=False)
    dataframe.loc[outlier_idx_cond, "conductivity_us_cm"] = dataframe["conductivity_us_cm"].max() * 3

    # Inject extreme outliers into 'ph_level' (impossible values)
    dataframe.loc[0, "ph_level"] = 14.5  
    dataframe.loc[1, "ph_level"] = -2.1  

    # Generate categorical features
    # sensor_type has rare levels
    sensor_types = ["Industrial", "Residential", "Environmental", "Rare_Specialized"]
    dataframe["sensor_type"] = np.random.choice(
        sensor_types, size=n_samples, p=[0.45, 0.45, 0.08, 0.02]
    )

    # location_category has inconsistencies
    locations = ["Urban", "Rural", "Industrial", "Remote"]
    dataframe["location_category"] = np.random.choice(locations, size=n_samples)

    # Inject inconsistent labeling
    urban_inconsistent = dataframe[dataframe["location_category"] == "Urban"].sample(5).index
    dataframe.loc[urban_inconsistent, "location_category"] = "urban"
    
    rural_inconsistent = dataframe[dataframe["location_category"] == "Rural"].sample(3).index
    dataframe.loc[rural_inconsistent, "location_category"] = "RURAL "

    return dataframe