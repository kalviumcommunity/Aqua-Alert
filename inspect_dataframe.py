import pandas as pd
import os

def inspect_water_data():
    """
    Demonstrates basic Pandas DataFrame inspection methods:
    head(), info(), and describe().
    """
    # Define the path to the dataset
    data_path = os.path.join("data", "raw", "water_quality_samples.csv")

    # Check if the file exists
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        return

    # Load the dataset
    print("--- Loading Data ---")
    df = pd.read_csv(data_path)
    print("Data loaded successfully.\n")

    # Step 1: Preview Data with head()
    # Shows the first 5 rows by default
    print("--- Step 1: Previewing Data with head() ---")
    print(df.head())
    print("\n")

    # Step 2: Inspecting Structure with info()
    # Shows column names, non-null counts, and data types
    print("--- Step 2: Inspecting Structure with info() ---")
    df.info()
    print("\n")

    # Step 3: Summarizing Numeric Data with describe()
    # Provides statistical summary of numeric columns
    print("--- Step 3: Summarizing Data with describe() ---")
    print(df.describe())
    print("\n")

if __name__ == "__main__":
    inspect_water_data()
