# Milestone Summary: DataFrame Indexing and Slicing

## Overview
This milestone focused on selecting rows and columns accurately using Pandas indexing and slicing. The goal was to extract intentional subsets without performing data transformations or analysis.

## Completed Tasks
- Loaded a DataFrame from `data/raw/water_quality_samples.csv`.
- Selected a single column by name.
- Selected multiple columns using a list of names.
- Selected rows by position using `.iloc`.
- Selected rows by label using `.loc` after setting `sample_id` as index.
- Sliced row ranges and explained inclusive/exclusive behavior.
- Selected rows and columns together using both `.iloc` and `.loc`.

## Key Learning Outcomes
1. **Column selection clarity**: Understood single-column (Series) vs multi-column (DataFrame) results.
2. **Position-based selection**: Used zero-based integer indexing and positional slicing safely.
3. **Label-based selection**: Used explicit index labels and understood label slice inclusiveness with `.loc`.
4. **Combined selection confidence**: Extracted exact subsets by specifying both rows and columns together.

## Why This Matters
- Prevents selecting the wrong subset silently.
- Improves readability and predictability of data workflows.
- Reduces brittle logic caused by index confusion.
- Builds a reliable foundation for cleaning and feature engineering.

## Implementation Used
- Script: `dataframe_selection_demo.py`
- Core methods/concepts:
    - `pd.read_csv()`
    - `df['col']` and `df[['col1', 'col2']]`
    - `df.iloc[...]`
    - `df.set_index('sample_id')`
    - `df.loc[...]`
