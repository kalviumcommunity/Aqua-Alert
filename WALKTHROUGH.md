# Data Organization - Milestone Walkthrough

This document outlines the organization of data in the **Aqua-Alert** repository, following the principles of data integrity, traceability, and reproducibility.

## Repository Structure

Our data is divided into three distinct stages:

1.  **`data/raw/`**: Contains the original, unmodified data collected from external sources (e.g., telemetry sensors). **Crucially, files in this directory are never edited directly.**
2.  **`data/processed/`**: Holds datasets derived from the raw data. This is where cleaning, normalization, or feature engineering results are stored.
3.  **`data/outputs/`**: Contains any final artifacts produced by the data science pipeline such as plots (`.png`, `.pdf`), trained models, or summary reports.

---

## 📽️ Video Walkthrough Script (~2 Minutes)

Feel free to use the following structure for your video submission:

### 1. Introduction (30 Seconds)
- "Hi, I'm [Your Name] and I'll be walking through the data organization for the Aqua-Alert project."
- "The goal here is to maintain a clear data lifecycle with separation of concerns."

### 2. Show the Folders (60 Seconds)
- **Point to `data/raw/`**: "Here we have the raw data folder. These are the original CSV files straight from the sensors. We never modify these to ensure we can always revert to the source of truth if needed."
- **Point to `data/processed/`**: "Next, we have the processed data. This is where cleaned datasets are stored after they've been transformed from the raw data."
- **Point to `data/outputs/`**: "Finally, there's the outputs folder. This keeps artifacts like plots and reports separate from our input data to avoid clutter and confusion."

### 3. Scenario-Based Reasoning (Mandatory) (30 Seconds)
- **Question**: "A teammate cannot reproduce your results because the raw data appears to be altered and outputs are mixed with input files. What happened and how does this fix it?"
- **Answer**: "This issue likely happened because the original raw data was overwritten during cleaning, or because input datasets and output plots were stored together, making it impossible to know which file came from which stage. By strictly separating **raw**, **processed**, and **output** folders, we protect our **source of truth (raw data)** and ensure **traceability**. This way, anyone can re-run our scripts to reproduce the exact same results with confidence."

---

## Why This Matters
- **Raw Data Integrity**: By ensuring raw data is never modified, we prevent permanent loss of information and maintain a reproducible baseline.
- **Traceability**: Decisions made during data cleaning (the transition from raw to processed) can be audited and reversed.
- **Reproducibility**: A clean environment ensures other researchers can understand the data flow without accidentally using output files as inputs.
