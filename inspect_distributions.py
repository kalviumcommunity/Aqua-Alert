"""
Aqua-Alert: Feature Distribution Inspection
------------------------------------------
This script systematically inspects feature distributions (numerical and categorical)
to identify risks such as skewness, outliers, and rare categories before modeling.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from src.config import CATEGORICAL_FEATURES, NUMERICAL_FEATURES, TARGET_COLUMN
from src.data_loader import load_data

def inspect_numerical_distributions(df, features):
    """Analyze summary statistics, skewness, and visualize numerical features."""
    print("\n=== 1. Numerical Feature Inspection ===")
    
    # Summary Statistics
    print("\n--- Summary Statistics ---")
    print(df[list(features)].describe())
    
    # Skewness
    print("\n--- Skewness Values ---")
    skew_vals = df[list(features)].skew().sort_values(ascending=False)
    print(skew_vals)
    
    # Distribution Plots (Histograms)
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(features, 1):
        plt.subplot(3, 2, i)
        sns.histplot(df[col], kde=True, color='teal')
        plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.savefig("reports/numerical_histograms.png")
    print("\n[Saved] Histograms saved to reports/numerical_histograms.png")
    
    # Outlier Detection (Boxplots)
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(features, 1):
        plt.subplot(3, 2, i)
        sns.boxplot(x=df[col], color='orchid')
        plt.title(f"Boxplot of {col}")
    plt.tight_layout()
    plt.savefig("reports/numerical_boxplots.png")
    print("[Saved] Boxplots saved to reports/numerical_boxplots.png")

def inspect_categorical_distributions(df, features):
    """Analyze category frequencies and check for rare levels/inconsistencies."""
    print("\n=== 2. Categorical Feature Inspection ===")
    
    for col in features:
        print(f"\n--- Value Counts for '{col}' ---")
        counts = df[col].value_counts()
        print(counts)
        
        # Check for rare categories (e.g., < 5% of data)
        rare_threshold = 0.05 * len(df)
        rare_levels = counts[counts < rare_threshold].index.tolist()
        if rare_levels:
            print(f"WARNING: Rare categories detected in '{col}': {rare_levels}")
        
        # Check for potential inconsistencies (case differences, extra spaces)
        unique_vals = df[col].unique()
        normalized_vals = {str(v).strip().lower() for v in unique_vals}
        if len(unique_vals) != len(normalized_vals):
            print(f"WARNING: Potential inconsistent labeling detected in '{col}'")

def compare_features_by_target(df, num_features, target_col):
    """Visualize how numerical features differ across target classes."""
    print(f"\n=== 3. Target-Based Comparison ({target_col}) ===")
    
    # Compare top 2 most skewed or informative features
    # For demonstration, we'll use conductivity and ph_level
    plot_features = ["ph_level", "conductivity_us_cm"]
    
    plt.figure(figsize=(12, 5))
    for i, col in enumerate(plot_features, 1):
        plt.subplot(1, 2, i)
        sns.boxplot(x=target_col, y=col, data=df, palette='Set2')
        plt.title(f"{col} vs {target_col}")
    plt.tight_layout()
    plt.savefig("reports/target_comparison.png")
    print("\n[Saved] Target comparison plots saved to reports/target_comparison.png")

def main():
    # Ensure reports directory exists
    import os
    if not os.path.exists("reports"):
        os.makedirs("reports")

    # 1. Load data
    print("Loading dataset for inspection...")
    df = load_data()
    print(f"Dataset shape: {df.shape}")

    # 2. Inspect Numerical Features
    inspect_numerical_distributions(df, NUMERICAL_FEATURES)

    # 3. Inspect Categorical Features
    inspect_categorical_distributions(df, CATEGORICAL_FEATURES)

    # 4. Compare by Target
    compare_features_by_target(df, NUMERICAL_FEATURES, TARGET_COLUMN)

    print("\nInspection complete. Please review the output above and the generated plots in the 'reports' directory.")

if __name__ == "__main__":
    main()
