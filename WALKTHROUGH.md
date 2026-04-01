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

---

# Python Scripting - Milestone Walkthrough

This section covers the creation and execution of a standalone Python script (`basic_analysis.py`) for the **Aqua-Alert** project.

## Why use Scripts?
While Jupyter Notebooks are excellent for exploration, Python scripts are better for:
- **Automation**: They can be scheduled or triggered by other processes.
- **Reproducibility**: They ensure a linear execution path from start to finish.
- **Collaborative Workflows**: Scripts are easier to version control and integrate into production systems.

## Running the Script
To run the script from your terminal:
```bash
python basic_analysis.py
```

---

## 📽️ Video Walkthrough Script (~2 Minutes)

Use this structure for your second video submission:

### 1. Introduction (30 Seconds)
- "Hi, I'm [Your Name], and I'll be demonstrating the execution of a Python script for the Aqua-Alert project."
- "Today, we're moving from interactive notebooks to a structured, standalone script called `basic_analysis.py`."

### 2. Show the Script (60 Seconds)
- **Open `basic_analysis.py`**: "As you can see, the script is clearly structured with definitions for constants, functions for calculation, and an entry point using the `if __name__ == "__main__":` block."
- **Explain the logic**: "The script takes sample water pH readings, calculates the average, maximum, and minimum values, and prints a status check based on safe pH levels (6.5 to 8.5)."
- **Run the script**: "I'll now run the script from the terminal using `python basic_analysis.py`. As you can see, it prints the summary directly to the console."

### 3. Scenario-Based Reasoning (Mandatory) (30 Seconds)
- **Question**: "You wrote code in a notebook that works, but when moved into a Python script it fails or behaves differently. Why?"
- **Answer**: "This usually happens due to **execution order** or **persistent state**. In a notebook, I might have run cells out of order, and the kernel 'remembered' variables that aren't defined in the script's linear flow. To fix this, I ensure all variables are defined before use and follow a **linear execution path**. Additionally, notebook-specific features like **magic commands** (e.g., `%matplotlib`) must be replaced with standard Python imports and functions to work in a standalone script."

---

## Key Best Practices
- **Use functions**: Encapsulating logic in functions makes code reusable.
- **Entry points**: Use `if __name__ == "__main__":` to control script execution.
- **Print statements**: Use them to provide clear feedback during execution.
