# Aqua-Alert

## Problem Statement
Local governments often fail to anticipate rainfall-induced flooding because historical datasets remain unused. How might predictive modelling help districts plan early warnings?

## Project Overview
Aqua-Alert is a Data Science initiative aimed at leveraging predictive modelling to anticipate rainfall-induced flooding. By utilizing historical datasets that traditionally remain unused, this project helps local districts plan and deploy early warnings effectively.

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
Execute the main script to load data, perform feature engineering, train the model, and evaluate performance:

```bash
python src/main.py
```
This script evaluates the model on a test set and displays key metrics (Accuracy, Confusion Matrix, Classification Report).

### 5. Run Prediction
To demonstrate inference with saved model artifacts, run:

```bash
python src/predict.py
```

## Reproducibility Verification
This project has been tested in a clean environment to ensure all dependencies are correctly captured in `requirements.txt`. Version pinning is strictly enforced (`==`) to prevent "it works on my machine" issues caused by package updates.

## Modular ML Workflow
The repository includes a structured `src/` layout:
- `data_preprocessing.py`: Logic for data ingestion and cleaning.
- `feature_engineering.py`: Transformation and scaling logic.
- `train.py`: Model fitting and artifact persistence.
- `evaluate.py`: Performance metrics calculation.
- `predict.py`: Independent inference pipeline.
- `config.py`: Centralized configuration and constants.
