# Aqua-Alert

## Problem Statement
Local governments often fail to anticipate rainfall-induced flooding because historical datasets remain unused. How might predictive modelling help districts plan early warnings?

## Project Overview
Aqua-Alert is a Data Science initiative aimed at leveraging predictive modelling to anticipate rainfall-induced flooding. By utilizing historical datasets that traditionally remain unused, this project helps local districts plan and deploy early warnings effectively.

## Modular ML Workflow

The repository now includes a structured `src/` layout that separates preprocessing, feature engineering, training, evaluation, and prediction.

### Run training and evaluation

```bash
python src/main.py
```

This trains a model on a reproducible synthetic dataset, evaluates it on a held-out split, and saves artifacts to `models/`.

### Run prediction independently

```bash
python src/predict.py
```

This loads the saved artifacts and produces a prediction without refitting the model or preprocessing step.
