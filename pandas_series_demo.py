"""
Milestone: Pandas Series Basics
===============================
Demonstrates:
  - Importing Pandas correctly
  - Creating Series from Python lists
  - Creating Series from NumPy arrays
  - Inspecting Series values and index

This script uses only basic Pandas fundamentals.
"""

import numpy as np
import pandas as pd


def print_header(title: str) -> None:
    print("\n" + "=" * 64)
    print(f"  {title}")
    print("=" * 64)


def section_series_from_list() -> None:
    print_header("1) Series from a Python List")

    readings = [7.2, 6.8, 7.5, 7.1]
    series = pd.Series(readings)

    print(f"Input list      : {readings}")
    print("Series values   :")
    print(series)
    print(f"Series index    : {series.index.tolist()}")
    print(f"Series values   : {series.values}")
    print(f"Series shape    : {series.shape}")
    print("Why it works   : Pandas automatically creates a default integer index starting at 0.")


def section_series_from_numpy_array() -> None:
    print_header("2) Series from a NumPy Array")

    temperatures = np.array([18, 20, 22, 24])
    series = pd.Series(temperatures)

    print(f"NumPy array     : {temperatures}")
    print("Series values   :")
    print(series)
    print(f"Series index    : {series.index.tolist()}")
    print(f"Series values   : {series.values}")
    print(f"Series shape    : {series.shape}")
    print("Why it works   : A NumPy array becomes a 1D Series with an automatic default index.")


def section_indexing_examples() -> None:
    print_header("3) Basic Indexing")

    values = pd.Series([100, 200, 300], index=["a", "b", "c"])

    print("Custom-index Series:")
    print(values)
    print(f"Index labels   : {values.index.tolist()}")
    print(f"First item     : {values['a']}")
    print(f"Second item    : {values['b']}")
    print("Why it matters : Series keeps data values and labels together.")


def summary() -> None:
    print_header("Summary")
    print(
        """
Key takeaways:
1. pd.Series can be created from both Python lists and NumPy arrays.
2. If you do not provide an index, Pandas generates one automatically: 0, 1, 2, ...
3. A Series exposes its values and index separately.
4. Custom index labels make Series easy to label and access by name.
"""
    )


if __name__ == "__main__":
    section_series_from_list()
    section_series_from_numpy_array()
    section_indexing_examples()
    summary()