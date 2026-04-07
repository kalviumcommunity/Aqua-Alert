"""
Aqua-Alert: CSV Loading and Inspection Demo
This script demonstrates how to safely load a CSV file using Pandas and
perform initial inspection to ensure data integrity.
"""

import pandas as pd
import os

def load_and_inspect_data(file_path):
    print(f"--- Loading Data from: {file_path} ---")
    
    # 1. Loading the CSV file
    # We use pd.read_csv() which is the standard method for loading tabular data.
    try:
        df = pd.read_csv(file_path)
        print("Successfully loaded the CSV into a DataFrame.\n")
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    # 2. Previewing the Data
    # Use .head() to see the first few rows and ensure headers match data.
    print("--- First 5 Rows of the Dataset ---")
    print(df.head())
    print("-" * 40 + "\n")

    # 3. Inspecting Structure (Rows and Columns)
    # .shape returns (number of rows, number of columns)
    rows, cols = df.shape
    print(f"Dataset Structure: {rows} rows and {cols} columns.")
    
    # .columns provides the names of all columns
    print(f"Column Names: {list(df.columns)}")
    print("-" * 40 + "\n")

    # 4. Verifying Data Types and Integrity
    # .info() provides a summary of the DataFrame including non-null counts and dtypes.
    print("--- DataFrame Info ---")
    df.info()
    print("-" * 40 + "\n")

    # 5. Descriptive Statistics (Optional but helpful for verification)
    # .describe() helps spot unrealistic values (e.g., pH > 14 or temp < -273)
    print("--- Descriptive Statistics ---")
    print(df.describe())
    print("-" * 40 + "\n")

    return df

def main():
    # Define the path to our sample CSV
    data_path = os.path.join('data', 'raw', 'water_quality_samples.csv')
    
    # Run the loading and inspection process
    df = load_and_inspect_data(data_path)
    
    if df is not None:
        print("Inspection complete. Data is ready for analysis.")
    else:
        print("Loading failed. Please check the file path and format.")

if __name__ == "__main__":
    main()
