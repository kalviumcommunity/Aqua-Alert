# Regression Model Evaluation: Mean Absolute Error (MAE)

This milestone focuses on evaluating a regression model's performance using Mean Absolute Error (MAE), comparing it against a baseline, and understanding its implications in a real-world context.

## 1. Evaluation Results

The regression model was trained to predict a continuous water quality index. Below are the performance metrics compared against a mean-baseline.

### Metric Snapshot
| Metric | Baseline (Mean) | Linear Regression | Improvement (%) |
| :--- | :--- | :--- | :--- |
| **MAE** | 0.3887 | 0.2364 | **39.17%** |
| **RMSE** | 0.4968 | 0.3336 | 32.86% |
| **R²** | -0.0037 | 0.5475 | N/A |

### Cross-Validation
- **CV MAE (5-fold):** 0.1931 ± 0.0104
- **Interpretation:** The low standard deviation (0.010) across folds indicates that the model's performance is stable and generalizes well across different subsets of the training data.

---

## 2. Interpretation

### What does MAE mean in this context?
In the context of the Aqua-Alert index, a MAE of **0.236** means that, on average, our model's predictions differ from the actual index values by approximately 0.24 units. This provides a direct, interpretable measure of error in the same units as the target variable.

### Is the improvement meaningful?
Yes. A **39.17% reduction in average error** compared to a simple mean-guessing baseline is a significant improvement. It demonstrates that the features (pH, temperature, turbidity, etc.) contain strong predictive signals that the Linear Regression model is successfully capturing.

### Are the errors acceptable?
Given that the baseline MAE was ~0.39 and we reduced it to ~0.24, the model is significantly more useful than a naive estimate. However, whether "0.24" is acceptable depends on the specific regulatory or safety thresholds of the water quality index. If the index range is 0-10, 0.24 is excellent; if the range is 0-1, 0.24 might be too high for critical decisions.

---

## 3. Scenario-Based Analysis

### Scenario Data
- **Baseline:** MAE: 18.5, RMSE: 22.4, R²: 0.00
- **Model:** MAE: 14.2, RMSE: 24.8, R²: 0.12
- **CV MAE:** 13.9 to 21.7 (Wide range)
- **Residuals:** Occasional very large errors.

### Responses
1. **Is the model better than baseline?**
   Technically yes, because the **MAE is lower (14.2 vs 18.5)**, meaning on average the predictions are closer to reality. However, the improvement is "noisy" and potentially risky.

2. **Why is RMSE higher than baseline despite lower MAE?**
   RMSE squares errors, making it highly sensitive to outliers. The fact that RMSE increased (24.8 vs 22.4) while MAE decreased indicates that while the model handles "typical" cases better, it makes **catastrophic errors** on a few specific samples that the baseline handles more safely.

3. **What does R² = 0.12 indicate?**
   It indicates the model only explains **12% of the variance** in the data. While better than the 0% of the baseline, it is still a very weak model that fails to capture 88% of the relationship.

4. **What does the variation in CV MAE suggest?**
   A range of 13.9 to 21.7 is very high. This suggests **model instability**. The model is highly dependent on the specific data points in each fold, likely indicates it hasn't learned generalized patterns or the data is highly volatile.

5. **Would you rely only on MAE?**
   **No.** In this specific case, MAE is deceptive. It hides the catastrophic outliers (revealed by RMSE) and the instability (revealed by CV). For a system like Aqua-Alert where safety might be involved, RMSE and stability are likely more important than average error.

---

## 4. Implementation Details
The evaluation follows strict ML best practices:
1. **No Data Leakage:** Train-test split (80/20) was performed before any preprocessing or fitting.
2. **Standardized Comparison:** Both baseline and model were evaluated on the exact same held-out test set.
3. **Cross-Validation:** Used `neg_mean_absolute_error` to ensure the model's performance isn't just a fluke of the split.
