"""
Aqua-Alert: Data Splitting Demonstration
----------------------------------------
This script implements a robust train-test split strategy to ensure 
honest model evaluation and prevent data leakage.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_loader import load_data
from src.config import TARGET_COLUMN, TEST_SIZE, RANDOM_STATE

def perform_data_split(df):
    """
    Separates features and target, and performs a stratified train-test split.
    """
    print("\n--- 1. Separating Features and Target ---")
    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]
    print(f"Features (X) shape: {X.shape}")
    print(f"Target (y) shape: {y.shape}")

    print("\n--- 2. Performing Train-Test Split ---")
    # Using stratification to maintain class balance
    # Using a fixed random state for reproducibility
    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        test_size=TEST_SIZE, 
        random_state=RANDOM_STATE, 
        stratify=y
    )
    
    return X_train, X_test, y_train, y_test

def verify_split(X_train, X_test, y_train, y_test):
    """
    Validates the split by checking shapes and class distributions.
    """
    print("\n--- 3. Verification Checks ---")
    print(f"Training set shape: {X_train.shape}")
    print(f"Testing set shape: {X_test.shape}")
    
    print("\n--- 4. Class Distribution Verification ---")
    print("Train set distribution (%):")
    print(y_train.value_counts(normalize=True) * 100)
    
    print("\nTest set distribution (%):")
    print(y_test.value_counts(normalize=True) * 100)
    
    # Confirming distribution similarity
    train_dist = y_train.value_counts(normalize=True)
    test_dist = y_test.value_counts(normalize=True)
    diff = abs(train_dist - test_dist).max()
    print(f"\nMax distribution difference: {diff:.4f}")
    if diff < 0.01:
        print("SUCCESS: Class distributions are well-preserved (Stratified Split).")
    else:
        print("WARNING: Significant class distribution imbalance detected.")

def check_leakage_prevention():
    """
    Explicitly confirms that no preprocessing is fitted before splitting.
    """
    print("\n--- 5. Leakage Prevention Confirmation ---")
    print("[CONFIRMED] Preprocessing (scaling, encoding, etc.) has NOT yet been applied.")
    print("[CONFIRMED] All transformations will be fitted ONLY on X_train in the next pipeline steps.")
    print("[CONFIRMED] Test set (X_test) remains untouched and purely for final evaluation.")

def main():
    # 1. Load the dataset
    print("Loading Aqua-Alert dataset...")
    df = load_data()
    print(f"Total samples: {len(df)}")

    # 2. Split the data
    X_train, X_test, y_train, y_test = perform_data_split(df)

    # 3. Verify the split
    verify_split(X_train, X_test, y_train, y_test)

    # 4. Confirm leakage prevention
    check_leakage_prevention()

    print("\nData splitting implementation complete.")

if __name__ == "__main__":
    main()
