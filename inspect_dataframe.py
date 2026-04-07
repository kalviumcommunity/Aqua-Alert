import os
import pandas as pd


def _classify_dtype(dtype):
    """Return a high-level type label for a pandas dtype."""
    if pd.api.types.is_numeric_dtype(dtype):
        return "numeric"
    if pd.api.types.is_datetime64_any_dtype(dtype):
        return "datetime"
    if pd.api.types.is_bool_dtype(dtype):
        return "boolean"
    return "text/categorical (object)"


def inspect_shape_and_types(file_path):
    """Inspect DataFrame shape and column dtypes without transforming data."""
    print(f"--- Loading Data from: {file_path} ---")

    if not os.path.exists(file_path):
        print(f"Error: Data file not found at {file_path}")
        return

    df = pd.read_csv(file_path)
    print("Data loaded successfully.\n")

    print("--- 1) DataFrame Shape ---")
    rows, cols = df.shape
    print(f"shape: {df.shape}")
    print(f"Interpretation: {rows} rows (observations) and {cols} columns (features).\n")

    print("--- 2) Rows vs Columns ---")
    print(f"Number of records: {rows}")
    print(f"Number of variables/features: {cols}")
    print(f"Columns: {list(df.columns)}\n")

    print("--- 3) Column Data Types ---")
    for column, dtype in df.dtypes.items():
        label = _classify_dtype(dtype)
        print(f"{column}: {dtype} ({label})")
    print()

    print("--- 4) Type-Related Risk Checks (Inspection Only) ---")
    object_columns = df.select_dtypes(include=["object", "string"]).columns.tolist()
    if object_columns:
        print("Object columns found (review whether they should be numeric):")
        for column in object_columns:
            non_null = df[column].dropna().astype(str).str.strip()
            numeric_like_ratio = pd.to_numeric(non_null, errors="coerce").notna().mean() if not non_null.empty else 0
            if numeric_like_ratio == 1.0:
                print(f"- {column}: looks fully numeric but stored as object -> potential type issue")
            elif numeric_like_ratio >= 0.6:
                print(f"- {column}: mixed content ({numeric_like_ratio:.0%} numeric-like) -> review needed")
            else:
                print(f"- {column}: likely genuine text/categorical data")
    else:
        print("No object columns detected.")

    missing_by_column = df.isna().sum()
    columns_with_missing = missing_by_column[missing_by_column > 0]
    if not columns_with_missing.empty:
        print("\nMissing values detected (these can affect inferred/usable types):")
        for column, count in columns_with_missing.items():
            print(f"- {column}: {count} missing values")
    else:
        print("\nNo missing values detected.")

    print("\nInspection complete. Next steps can be planned intentionally based on shape and dtypes.")


if __name__ == "__main__":
    data_path = os.path.join("data", "raw", "water_quality_samples.csv")
    inspect_shape_and_types(data_path)
