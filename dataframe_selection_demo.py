import os
import pandas as pd


def run_selection_demo(file_path):
    """Demonstrate DataFrame column and row selection with clear, safe examples."""
    print(f"--- Loading Data from: {file_path} ---")

    if not os.path.exists(file_path):
        print(f"Error: Data file not found at {file_path}")
        return

    df = pd.read_csv(file_path)
    print("Data loaded successfully.")
    print(f"Initial shape: {df.shape}\n")

    print("--- 1) Selecting Columns by Name ---")
    single_column = df["ph_level"]
    print("Single column selection: df['ph_level']")
    print(f"Result type: {type(single_column).__name__}")
    print(single_column.head(), "\n")

    multi_columns = df[["location", "ph_level", "temperature_c"]]
    print("Multiple column selection: df[['location', 'ph_level', 'temperature_c']]")
    print(f"Result type: {type(multi_columns).__name__}")
    print(multi_columns.head(), "\n")

    print("--- 2) Selecting Rows by Position (iloc) ---")
    print("Single row by position: df.iloc[2]")
    print(df.iloc[2], "\n")

    print("Row slice by position: df.iloc[1:4] (start inclusive, stop exclusive)")
    print(df.iloc[1:4], "\n")

    print("--- 3) Selecting Rows by Label (loc) ---")
    labeled_df = df.set_index("sample_id")
    print("Using sample_id as index for label-based selection.")
    print("Single row by label: labeled_df.loc['WQS-003']")
    print(labeled_df.loc["WQS-003"], "\n")

    print("Row slice by label: labeled_df.loc['WQS-002':'WQS-004'] (both labels included)")
    print(labeled_df.loc["WQS-002":"WQS-004"], "\n")

    print("--- 4) Selecting Rows and Columns Together ---")
    print("By position: df.iloc[1:4, [2, 3, 4]]")
    print(df.iloc[1:4, [2, 3, 4]], "\n")

    print("By label: labeled_df.loc['WQS-002':'WQS-004', ['location', 'ph_level']]")
    print(labeled_df.loc["WQS-002":"WQS-004", ["location", "ph_level"]], "\n")

    print("Selection demo complete. Always verify slices to ensure you selected the intended subset.")


if __name__ == "__main__":
    dataset_path = os.path.join("data", "raw", "water_quality_samples.csv")
    run_selection_demo(dataset_path)