# Workspace & Jupyter Organization Proof

This PR provides evidence of understanding the Jupyter Home interface, workspace organization, and notebook management within the `Aqua-Alert` project. 

## Requirements Displayed:
- **Jupyter Notebook launched from intended directory:** Launched specifically from the root `Aqua-Alert/` repository directory, ensuring relative paths remain clean and project-scoped.
- **Notebook Created Inside the Correct Folder:** Designed intentionally inside a `notebooks/` directory rather than placed arbitrarily at the root or user home directory.
- **Proper Naming & Python Execution:** The notebook `01_workspace_setup.ipynb` is correctly named and successfully running a python cell confirming its present working directory.

## Scenario Response: File Not Found
**Scenario:** *You open a notebook and realize it cannot find a dataset file that exists on your machine. How would you use your understanding of the Jupyter Home interface and folder structure to diagnose and fix this issue?*

**Diagnosis Strategy & Fix:**
1. **Launch Directory:** When Jupyter is launched, the root of the Home interface is tied to the terminal's directory when the command was run. Launching from the specific project directory (`Aqua-Alert/`) guarantees all file operations in notebooks are contained and scoped locally.
2. **Folder Navigation:** By going back to the Jupyter Home tab (the file tree), I can visually check where my notebook lives (e.g., inside `/notebooks`) and where my dataset file actually lives (e.g., inside `/data`).  
3. **Relative Paths:** If my notebook is in `notebooks/` and data is in `data/`, the cell code looking for `data.csv` in the current folder won't work. By navigating the file tree visually, I know to fix my code string to use a relative path back up one folder: `pd.read_csv('../data/data.csv')`.
4. **Workspace Awareness:** Being aware of the folder structure means I never hardcode paths like `C:/Users/.../data.csv`. Using relative paths ensures it stays valid inside the project workspace regardless of which machine runs the notebook.
