"""
Milestone: Pandas DataFrame Creation Basics
===========================================
Demonstrates:
  - Importing Pandas correctly
  - Creating a DataFrame from a Python dictionary
  - Loading a DataFrame from an external CSV file
  - Inspecting rows, columns, and basic DataFrame structure

This script intentionally avoids cleaning and analysis steps.
"""

import pandas as pd


def print_header(title: str) -> None:
    print("\n" + "=" * 66)
    print(f"  {title}")
    print("=" * 66)


def dataframe_from_dictionary() -> None:
    print_header("1) Create DataFrame from Python Dictionary")

    sensor_dict = {
        "sensor_id": ["A1", "A2", "A3"],
        "location": ["North Canal", "South Canal", "East Canal"],
        "pH": [7.0, 6.8, 7.3],
    }

    df_dict = pd.DataFrame(sensor_dict)

    print("DataFrame preview:")
    print(df_dict)
    print(f"Rows, Columns   : {df_dict.shape}")
    print(f"Column names    : {df_dict.columns.tolist()}")
    print(f"Index labels    : {df_dict.index.tolist()}")
    print("Interpretation  : Each row is one sensor reading; each column is a field.")


def dataframe_from_csv() -> None:
    print_header("2) Load DataFrame from External CSV File")

    file_path = "data/raw/sensor_data_demo.csv"
    df_file = pd.read_csv(file_path)

    print(f"Loaded file     : {file_path}")
    print("DataFrame preview (first 5 rows):")
    print(df_file.head())
    print(f"Rows, Columns   : {df_file.shape}")
    print(f"Column names    : {df_file.columns.tolist()}")
    print(f"Index labels    : {df_file.index.tolist()}")
    print("Interpretation  : Columns come directly from the CSV header row.")


def summary() -> None:
    print_header("Summary")
    print(
        """
Key takeaways:
1. pd.DataFrame(dictionary) builds a table from key-value pairs.
2. pd.read_csv(path) loads tabular data from an external file.
3. .shape shows table size as (rows, columns).
4. .columns and .index reveal DataFrame structure clearly.
"""
    )


if __name__ == "__main__":
    dataframe_from_dictionary()
    dataframe_from_csv()
    summary()