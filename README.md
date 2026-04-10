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
- `data_preprocessing.py`: Data ingestion, cleaning, and splitting.
- `feature_engineering.py`: Transformation and scaling logic.
- `train.py`: Model fitting.
- `evaluate.py`: Performance metrics calculation.
- `persistence.py`: Saving and loading artifacts, reports, and logs.
- `predict.py`: Independent inference pipeline.

## Outputs

- `models/aqua_alert_artifacts.joblib`: Saved model bundle.
- `reports/evaluation_report.json`: Evaluation summary.
- `logs/experiment_log.csv`: Append-only experiment log.
