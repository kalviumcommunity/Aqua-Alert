# Aqua-Alert

## Problem Statement
Local governments often fail to anticipate rainfall-induced flooding because historical datasets remain unused. How might predictive modelling help districts plan early warnings?

## Project Overview
Aqua-Alert is a Data Science initiative aimed at leveraging predictive modelling to anticipate rainfall-induced flooding. By utilizing historical datasets that traditionally remain unused, this project helps local districts plan and deploy early warnings effectively.

## Project Structure

The repository follows a standard machine learning layout:

```text
Aqua-Alert/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── models/
├── reports/
├── logs/
├── main.py
├── requirements.txt
└── README.md
```

Raw data stays in `data/raw/`, generated datasets live in `data/processed/`, trained artifacts go in `models/`, evaluation outputs go in `reports/`, and experiment history is written to `logs/`.

## Project Setup Instructions

This section provides a clear, step-by-step guide to setting up the environment and running the project reliably on any machine.

### Prerequisites
- **Python Version**: Python 3.9 or higher (Tested on 3.13.12)
- **Git**: For cloning the repository

### 1. Create a Fresh Virtual Environment
To ensure project dependencies are isolated and do not conflict with your system-wide packages, create a clean virtual environment:

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment
Activate the environment before installing dependencies or running scripts.

**On Windows:**
```bash
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
Install all required libraries with pinned versions using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Run the Training Pipeline
Execute the main script to load data, perform feature engineering, train the model, save artifacts, and generate reports:

```bash
python main.py
```
This script evaluates the model on a test set and writes the trained artifact bundle to `models/`, the evaluation report to `reports/`, and the run log to `logs/`.

### 5. Run Prediction
To demonstrate inference with saved model artifacts, run:

```bash
python src/predict.py
```

## Reproducibility Verification
This project has been tested in a clean environment to ensure all dependencies are correctly captured in `requirements.txt`. Version pinning is strictly enforced (`==`) to prevent "it works on my machine" issues caused by package updates.

## Modular ML Workflow
The repository includes a structured `src/` layout:
- `config.py`: Centralized configuration and filesystem paths.
- `data_loader.py`: Raw data loading only, with no splitting or transformation.
- `preprocessing.py`: Reusable preprocessing pipeline construction.
- `train.py`: Train/test splitting, preprocessing fit, and model fitting.
- `evaluate.py`: Performance metrics calculation.
- `persistence.py`: Saving and loading artifacts, reports, and logs.
- `predict.py`: Independent inference pipeline.

## Feature Distribution Analysis

Before training any model, we systematically inspected the distributions of each feature to identify risks and determine necessary preprocessing.

### Numerical Features

- `ph_level`: Approximately normal but contains extreme outliers (e.g., 14.5 and -2.1) that violate physical constraints.
- `conductivity_us_cm`: Highly right-skewed (exponential distributed). Mean is significantly higher than the median.
- `turbidity_ntu`, `dissolved_oxygen_mg_l`, `temperature_c`, `chlorine_mg_l`: Show approximately symmetric, bell-shaped distributions.

### Categorical Features

- `sensor_type`: Highly imbalanced. `Industrial` and `Residential` levels dominate, while `Rare_Specialized` is a rare class (< 2% of samples).
- `location_category`: Contains inconsistent labels like "urban" (lowercase) and "RURAL " (extra whitespace).

### Target Comparison Insights

- `conductivity_us_cm` shows different median values across target classes, suggesting a potentially predictive signal.
- `ph_level` distribution overlaps heavily across classes, requiring normalization and outlier handling.

### Preprocessing Decisions

1. **Log Transformation**: Required for `conductivity_us_cm` to stabilize variance.
2. **Outlier Clipping**: extreme values in `ph_level` must be capped.
3. **Categorical Normalization**: `location_category` requires case normalization and whitespace stripping.
4. **Rare Category Handling**: `Rare_Specialized` in `sensor_type` may need grouping.

## Data Splitting Strategy

To ensure honest evaluation and measure the model's ability to generalize to unseen data, we implement a strict data splitting boundary.

### Split Methodology
- **Split Ratio**: 80% Training / 20% Testing.
- **Stratification**: Enabled (`stratify=y`). This ensures that the class proportions in both the training and testing sets match the original dataset, which is critical for maintaining evaluation stability in classification tasks.
- **Reproducibility**: `random_state=42` is fixed to ensure that the exact same split is generated every time the script is run.

### Leakage Prevention
- **Split Before Fitting**: The data is split into $X_{train}, X_{test}, y_{train}, y_{test}$ *before* any preprocessing (scaling, encoding, or imputation) is fitted.
- **Training Integrity**: All transformations are fitted strictly on the training set ($X_{train}$) and then applied to the test set ($X_{test}$). This prevents "future information" from leaking into the training process.
- **Sacred Test Set**: The test set is held out entirely and is not used for hyperparameter tuning or feature selection.

### Validation
Each split is verified by checking:
1. **Set Shapes**: Confirming the 80/20 ratio is correctly applied.
2. **Class Proportions**: Confirming that the target distribution remains consistent across both sets (verified < 1% difference).

---

## Numerical Feature Normalization

This project applies feature normalization with `MinMaxScaler` for numeric variables only.

### Which Features Were Scaled
- `ph_level`
- `temperature_c`
- `turbidity_ntu`
- `dissolved_oxygen_mg_l`
- `conductivity_us_cm`
- `chlorine_mg_l`

### Model Used
- `LogisticRegression` (scikit-learn)

### Why MinMaxScaler Was Chosen Instead of StandardScaler
`LogisticRegression` is scale-sensitive and benefits from consistent feature ranges. `MinMaxScaler` was selected to bound each numerical feature to $[0, 1]$, which provides stable optimization and comparable magnitudes across inputs while preserving relative ordering. This project uses normalization primarily to enforce bounded inputs end-to-end.

`StandardScaler` is still valid in many settings, but it produces unbounded transformed values and is more sensitive to outlier magnitude in terms of resulting standardized values. Since this workflow benefits from fixed-range inputs, `MinMaxScaler` is the preferred choice.

### Leakage Prevention During Scaling
- The project explicitly separates `X` and `y`.
- Train/test split is performed before any preprocessing fit.
- A `ColumnTransformer` with `MinMaxScaler` (numerical) and `OneHotEncoder` (categorical) is fitted only on `X_train`.
- The fitted transformer is reused to transform `X_test` with `transform()` only.
- The target variable is never scaled.

### Why Categorical Features Were Not Scaled
Categorical columns are non-numeric labels and do not have meaningful distance on a continuous scale. They are encoded with `OneHotEncoder(handle_unknown="ignore")` and are not passed through `MinMaxScaler`.

### Verification of MinMax Range
After fitting on `X_train`, the project verifies normalization by checking that each training numerical feature has minimum approximately $0$ and maximum approximately $1$ (within floating-point tolerance). Verification results are printed in training logs and saved in `reports/evaluation_report.json`.

### Outlier Consideration
- `ph_level` includes impossible/extreme injected values.
- `conductivity_us_cm` is strongly right-skewed with injected extreme outliers.

For this assignment, outliers were left unchanged to preserve raw signal behavior and to demonstrate true MinMax behavior under realistic skewed data. This is acceptable because the chosen model still benefits from bounded numeric inputs in $[0, 1]$. In a production setting, optional clipping or log transforms can be evaluated before normalization if outlier compression is required.

### Scaler Persistence for Inference
- The fitted scaler from the numerical preprocessing branch is saved as `models/minmax_scaler.pkl` using `joblib.dump`.
- The full preprocessing + model bundle is also saved in `models/aqua_alert_artifacts.joblib`.
- Inference loads saved preprocessing artifacts and saved scaler with `joblib.load` and does not refit the scaler.

---

## Outputs

- `models/aqua_alert_artifacts.joblib`: Saved model bundle.
- `models/minmax_scaler.pkl`: Saved fitted `MinMaxScaler` for numerical features.
- `reports/evaluation_report.json`: Evaluation summary.
- `logs/experiment_log.csv`: Append-only experiment log.

---

## Baseline Model Comparison

To establish a minimum benchmark for this classification task, the workflow trains and evaluates a baseline model alongside the primary model.

### Baseline Choice
- Baseline model: `DummyClassifier(strategy="most_frequent")`
- Why this baseline: it predicts the majority class only, representing a trivial classifier that uses class frequency without learning feature-target relationships.

### Train/Test Integrity and Leakage Control
- Dataset is split before any model fitting.
- Both baseline and primary models are fit only on the training data.
- Both are evaluated on the same held-out test set.
- Both use the same evaluation metrics for fair comparison.

### Metrics Used (Same for Both Models)
- Accuracy
- Macro Precision
- Macro Recall
- Macro F1
- Confusion Matrix
- Full per-class classification report

### Comparison Output
`src/main.py` computes and saves:
- `primary_model_metrics`
- `baseline_metrics`
- `model_vs_baseline` with metric deltas

These are written to `reports/evaluation_report.json` and summarized in console output for side-by-side inspection.

### Is Improvement Meaningful?
Improvement is considered meaningful when the primary model exceeds the baseline on multiple shared metrics (especially macro F1 and per-class recall), indicating it learns predictive patterns beyond majority-class guessing.
