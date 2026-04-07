# PR Submission Guide: CSV Loading Milestone

This guide will walk you through the process of submitting your Pull Request for this milestone.

## Step 1: Push Your Changes
Since we are on the `feat/csv-loading` branch, you need to push this branch to your remote repository (e.g., GitHub).

```bash
git push origin feat/csv-loading
```

## Step 2: Create the Pull Request
1. Go to your repository on GitHub.
2. You should see a prompt saying "feat/csv-loading has recent pushes... Compare & pull request". Click that button.
3. If you don't see the prompt, go to the **Pull Requests** tab and click **New pull request**.
4. Set the **base** branch to `main` (or your default branch) and the **compare** branch to `feat/csv-loading`.

## Step 3: Fill Out the PR Template
Use the following as your PR description:

---
### Milestone: CSV Loading and Inspection

#### Description
This PR implements a robust CSV loading and inspection script using Pandas. It focuses on safe data ingestion and immediate verification of dataset structure.

#### Key Changes
- Added `data/raw/water_quality_samples.csv` for demonstration.
- Added `csv_loading_demo.py` showcasing:
    - `pd.read_csv()` for loading.
    - Data preview with `.head()`.
    - Structural checks with `.shape` and `.columns`.
    - Data integrity checks with `.info()` and `.describe()`.

#### Verification
- Ran the script successfully in the terminal.
- Verified that all columns were correctly mapped and data types inferred appropriately.
---

## Step 4: Submit and Link
1. Click **Create pull request**.
2. Copy the URL of the Pull Request you just created.
3. Submit this link as per your assignment instructions.
