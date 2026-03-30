# Environment Verification

This pull request contains proof that the local system is fully ready for Data Science work. The environment has been tested for consistency, and the following components have been verified correctly:

## 1. Python Check
Python is installed and callable from the terminal. 
- Version tested: `3.13.9`

## 2. Conda Check
Conda is correctly installed, and virtual environments function smoothly.
- Version tested: `conda 26.1.1`
- Tested creating and activating environments without issues. 

## 3. Jupyter Verification
Jupyter is functioning and can execute Python code.
- Tested launching Jupyter Notebook.
- Check the attached `env_verification.ipynb` file to see a Python cell executing successfully inside Jupyter.

## Scenario: Jupyter Notebook Uses Different Python Version
*Scenario: You can run Python from the terminal, but Jupyter notebooks are using a different Python version or fail to import libraries.*

**How to identify and fix:**
1. **Identify the issue:** Run `import sys; print(sys.executable)` inside a Jupyter Notebook cell. Compare that output with the output of `where python` (on Windows) or `which python` (on Mac/Linux) in your active Conda terminal. If they differ, Jupyter is running on a different kernel/environment than your terminal.
2. **Fixing the issue:** 
   - Ensure the Conda environment is activated (`conda activate myenv`).
   - Install `ipykernel` in that environment (`conda install ipykernel`).
   - Register that environment as a Jupyter kernel (`python -m ipykernel install --user --name=myenv --display-name="Python (myenv)"`).
   - Restart Jupyter, and specifically select `"Python (myenv)"` from the *Kernel > Change Kernel* menu to ensure the notebook runs within the correct environment.
