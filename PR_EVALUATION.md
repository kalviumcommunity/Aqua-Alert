# Pull Request: Regression Model Evaluation (MSE & R²)

## Description
This PR implements a comprehensive evaluation pipeline for the Aqua-Alert regression model, comparing it against a mean-baseline. We assess performance using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² (Coefficient of Determination) to ensure the model provides meaningful predictive value.

## Metrics Calculation Summary
- **MSE (Mean Squared Error)**: Measures the average squared difference between estimated values and actual value.
- **RMSE (Root Mean Squared Error)**: Standard deviation of residuals; interpreted in the same units as the target (lakhs).
- **R² (Coefficient of Determination)**: Proportion of variance explained by the model.

## Evaluation Results

### Model vs Baseline Comparison (Test Set)
| Metric | Baseline (Mean) | Linear Regression | Improvement |
| :--- | :--- | :--- | :--- |
| **MSE** | 1439.04 | 178.06 | 87.63% reduction |
| **RMSE** | 37.93 | 13.34 | 64.83% reduction |
| **R²** | -0.0019 | 0.8760 | Significant increase |

### Cross-Validation Results (5 Folds)
- **R² Scores**: [0.7860, 0.8146, 0.8817, 0.7878, 0.8566]
- **R² Mean**: 0.8253 ± 0.0380
- **RMSE Mean**: 9.8589 ± 0.3945

---

## Written Interpretation

### 1. Does the model meaningfully outperform the baseline?
**Yes.** The model reduces the Mean Squared Error (MSE) by approximately 87%. The RMSE dropped from 37.93 to 13.34, indicating a substantial reduction in typical prediction error.

### 2. What does the R² value indicate?
The R² value of **0.876** indicates that our model explains approximately **87.6% of the variance** in the target variable (Aqua-Alert Revenue). This is a strong result, suggesting the features provided have high predictive power.

### 3. Is the RMSE acceptable relative to the target scale?
Yes. The average target value is approximately 111 (lakhs). An RMSE of **13.34** represents an error of about 12% relative to the mean, which is acceptable for an initial predictive model in this domain.

### 4. Are results stable across folds?
**Yes.** The standard deviation of R² across folds is low (0.0380), and the mean (0.8253) is consistent with the test set performance. This suggests the model generalizes well and is not overly sensitive to specific data subsets.

### 5. Did any fold produce negative R²?
No. In our experimental run, all R² scores were positive, indicating that the model consistently outperformed the mean predictor in every data slice.

---
## Files Modified
- `src/mse_r2_evaluation.py`: Core evaluation script and pipeline.
