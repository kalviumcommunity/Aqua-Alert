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

---

# Conditional Logic - Milestone Walkthrough

This section covers the implementation of conditional statements and logical operators in the **Aqua-Alert** project.

## Why use Conditional Logic?
Decision-making is the core of any automated system. In Aqua-Alert, we use conditional logic to:
- **Trigger Alerts**: Send warnings when sensor values exceed safety thresholds.
- **System Monitoring**: Verify if sensors are active or in maintenance mode.
- **Categorization**: Classify environmental conditions based on multiple data points.

## 📽️ Video Walkthrough Script (~2 Minutes)

Use this structure for your third video submission:

### 1. Introduction (30 Seconds)
- "Hi, I'm [Your Name], and I'll be demonstrating the conditional logic implemented in the Aqua-Alert project."
- "Today, we're looking at `conditional_logic_demo.py`, a script that uses Python's if-elif-else structures and logical operators to make data-driven decisions."

### 2. Show the Code (60 Seconds)
- **Open `conditional_logic_demo.py`**: "As you can see, the script is organized to demonstrate four key concepts."
- **Point to Basic 'if'**: "The first part checks if the water level exceeds 80%. If true, it prints a critical alert."
- **Point to 'if-else'**: "The second part compares the sensor status string. If it's 'active', it confirms monitoring; otherwise, it warns the system is offline."
- **Point to 'if-elif-else'**: "The third part uses multiple branches to categorize rainfall rates into Critical, Heavy, Moderate, or Light rainfall."
- **Point to Logical Operators**: "Finally, we use `and`, `or`, and `not` to combine conditions. For example, we check if high humidity **and** heavy rainfall are occurring simultaneously."
- **Run the script**: "I'll now run the script from the terminal using `python conditional_logic_demo.py` to show the logic in action."

### 3. Scenario-Based Reasoning (Mandatory) (30 Seconds)
- **Scenario**: "A condition in your code always evaluates to False, even when you expect it to be True. What common mistakes could cause this, and how would you debug and fix the issue?"
- **Answer**: "This can happen for several reasons. First, **data type mismatch**—like comparing a string `'85'` to a number `80`. Second, using the wrong **comparison operator** (e.g., `>` instead of `<`). Third, **incorrect logic**—using `and` when I should have used `or`, which makes the condition too restrictive. To debug this, I'd use `print()` statements to check the actual variable values and types just before the condition, and then I'd simplify the condition to test its parts individually."

---

## Key Concepts Covered
- **Comparison Operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- **Logical Operators**: `and`, `or`, `not`.
- **Indentation**: Ensuring Python's block-based structure is correctly implemented.
- **Condition Order**: Placing more specific conditions (like `elif rainfall > 30`) before broader ones.

---

# Iteration (for and while Loops) - Milestone Walkthrough

This section covers the use of iterative control flow in the **Aqua-Alert** project through `loops_demo.py`.

## Why Iteration Matters
Loops help us avoid repetitive code and process data in a scalable, readable way.

In Aqua-Alert, loops are useful for:
- **Repeated checks** of sensor states over time
- **Processing collections** of districts or readings
- **Condition-based monitoring** where execution continues until a state changes

## Running the Script
To run the iteration milestone script from your terminal:
```bash
python loops_demo.py
```

---

## 📽️ Video Walkthrough Script (~2 Minutes)

Use this structure for your submission:

### 1. Introduction (20-30 Seconds)
- "Hi, I'm [Your Name], and I'll be demonstrating Python iteration using `for` and `while` loops in the Aqua-Alert project."
- "This script shows how to repeat logic safely and clearly when working with simple data collections."

### 2. for Loop Demonstration (30-40 Seconds)
- **Open `loops_demo.py`** and point to `for_loop_examples()`.
- Explain: "This section shows iteration over a known range and over a list of districts."
- Mention: "`for` loops are ideal when the sequence is known, like a range or list."

### 3. while Loop Demonstration (30-40 Seconds)
- Point to `while_loop_examples()`.
- Explain: "This loop continues while a condition is true and stops when the reservoir level reaches the target."
- Mention variable updates: "The loop variable changes each iteration, which guarantees termination."

### 4. break/continue and Flow Control (20-30 Seconds)
- Point to `loop_control_examples()`.
- Explain: "`continue` skips missing values, and `break` exits early when a critical value is detected."

### 5. Infinite Loop Prevention + Scenario Reasoning (20-30 Seconds)
- Point to `infinite_loop_safety_examples()`.
- Explain: "An infinite loop happens when loop conditions never change. Here we prevent that with a clear stop condition."
- **Scenario response**: "If my loop does not stop, I first check whether the loop variable is being updated correctly and whether the condition can become false."

---

## Assignment Checklist Coverage
- ✅ `for` loop over range and list
- ✅ `while` loop with condition-based repetition
- ✅ Use of `break` and `continue`
- ✅ Infinite loop avoidance and correction strategy
- ✅ Console output for observing loop behavior

## Best Practices to Keep
- Keep loop bodies focused on one purpose.
- Update loop variables explicitly in `while` loops.
- Prefer readable loop conditions over clever shortcuts.
- Test with small examples before scaling up.

---

# Functions (Define and Call) - Milestone Walkthrough

This section covers writing reusable Python functions in **Aqua-Alert** through `functions_demo.py`.

## Why Functions Matter
Functions let you write logic once and reuse it safely.

In Aqua-Alert, functions help us:
- **Reduce repetition** by reusing alert and calculation logic
- **Improve readability** by splitting code into focused tasks
- **Debug faster** by testing behavior one function at a time

## Running the Script
To run the functions milestone script from your terminal:
```bash
python functions_demo.py
```

---

## 📽️ Video Walkthrough Script (~2 Minutes)

Use this structure for your submission:

### 1. Introduction (20-30 Seconds)
- "Hi, I'm [Your Name], and I'll be demonstrating function usage in Python using the Aqua-Alert project."
- "This milestone focuses on defining functions, calling them, passing arguments, and understanding basic scope."

### 2. Defining a Function (25-35 Seconds)
- **Open `functions_demo.py`** and point to function definitions.
- Explain: "Here I define small, single-purpose functions using the `def` keyword, such as risk scoring and alert display."
- Mention: "Each function has a clear name and focused responsibility."

### 3. Calling Functions and Passing Arguments (30-40 Seconds)
- Point to `main()` and the function calls.
- Explain: "I call functions by name and pass required arguments, for example rainfall and water-level values into the scoring function."
- Mention execution flow: "After each function completes, control returns to `main()`."

### 4. Parameters and Reusability (20-30 Seconds)
- Point to `show_alert_message(region, severity)`.
- Explain: "Because this function uses parameters, I can reuse it for different regions and severity levels without rewriting code."

### 5. Scope Basics + Scenario Reasoning (20-30 Seconds)
- Point to `scope_demo()` and global variable usage.
- Explain: "The local variable exists only inside the function, while the global variable is visible outside."
- **Scenario response**: "If I get a variable error, I check whether that variable was defined inside another function and therefore out of scope."

---

## Assignment Checklist Coverage
- ✅ Define functions with `def`
- ✅ Call functions to execute reusable logic
- ✅ Pass arguments into functions
- ✅ Demonstrate basic local vs global scope behavior
- ✅ Print outputs to observe function flow

## Best Practices to Keep
- Keep functions small and focused.
- Use descriptive function and parameter names.
- Return values when a result is needed; print only for user-facing output.
- Avoid unnecessary global variables to reduce side effects.

---

# NumPy Shape, Dimensions, and Indexing - Milestone Walkthrough

This section covers NumPy fundamentals for understanding how arrays are structured in `numpy_shape_indexing_demo.py`.

## Why This Matters
Before slicing, reshaping, or advanced operations, you must understand:
- **Shape**: how values are arranged
- **Dimensions**: how many axes exist
- **Index positions**: how to access values safely

This prevents common beginner bugs like out-of-range errors and row/column confusion.

## Running the Script
To run this milestone script from your terminal:
```bash
python numpy_shape_indexing_demo.py
```

---

## Video Walkthrough Script (~2 Minutes)

Use this structure for your submission:

### 1. Introduction (20-30 Seconds)
- "Hi, I'm [Your Name], and I'll demonstrate NumPy array structure using shape, dimensions, and indexing."
- "This milestone focuses on understanding layout before moving to slicing and reshaping."

### 2. 1D and 2D Shape Demonstration (30-40 Seconds)
- Open `numpy_shape_indexing_demo.py` and point to `section_shape_basics()`.
- Explain: "For a 1D array, shape like `(5,)` means five elements on one axis."
- Explain: "For a 2D array, shape like `(3, 4)` means 3 rows and 4 columns."

### 3. Dimensions (`ndim`) Explanation (20-30 Seconds)
- Point to `section_dimensions()`.
- Explain: "`ndim` tells how many dimensions an array has: 1D, 2D, or 3D."
- Mention: "In 2D arrays, axis 0 corresponds to rows and axis 1 to columns."

### 4. Indexing Logic Demo (30-40 Seconds)
- Point to `section_indexing()`.
- Explain: "Indexing is zero-based, so the first position is index 0."
- Show examples: 1D indexing (`arr[index]`) and 2D indexing (`array[row, column]`).
- Emphasize: "Rows come before columns in 2D indexing."

### 5. Layout Visualization + Common Mistake (20-30 Seconds)
- Point to `section_visualize_layout()` and `section_common_mistakes()`.
- Explain: "The index map helps connect positions like `[row, col]` to actual values."
- Scenario response: "If I hit an index error, I first check the array shape and verify the index is within bounds."

---

## Assignment Checklist Coverage
- ✅ 1D array and its shape
- ✅ 2D array and its shape
- ✅ Dimension checks using `ndim`
- ✅ Element access using index positions
- ✅ Clear indexing explanation for rows and columns
- ✅ Basic safe-access mindset to avoid index bugs

## Best Practices to Keep
- Always inspect `shape` before indexing.
- Remember indexing starts at zero.
- In 2D arrays, access values as `[row, column]`.
- Use small arrays first to build indexing intuition.

---

# NumPy Basic Math Operations - Milestone Walkthrough

This section covers basic arithmetic operations in NumPy using `numpy_math_operations_demo.py`.

## Why This Matters
NumPy lets you apply formulas to entire arrays at once.
This makes numerical code:
- concise
- easier to read
- more reliable than manual loops for simple array math

## Running the Script
To run this milestone script from your terminal:
```bash
python numpy_math_operations_demo.py
```

---

## Video Walkthrough Script (~2 Minutes)

Use this structure for your submission:

### 1. Introduction (20-30 Seconds)
- "Hi, I'm [Your Name], and I'll demonstrate basic mathematical operations on NumPy arrays."
- "This milestone focuses on element-wise behavior, scalar math, and common beginner mistakes."

### 2. Create Arrays and Show Element-Wise Operations (35-45 Seconds)
- Open `numpy_math_operations_demo.py` and point to `section_elementwise_operations()`.
- Explain: "I create two arrays with the same shape and apply addition, subtraction, multiplication, and division."
- Mention: "NumPy applies each operation to corresponding positions in both arrays."

### 3. Demonstrate Scalar Operations (25-35 Seconds)
- Point to `section_scalar_operations()`.
- Explain: "When I add or multiply by a scalar, NumPy applies that operation to every element in the array."
- Show at least one example such as `values * 3`.

### 4. Compare Python Lists vs NumPy Arrays (25-35 Seconds)
- Point to `section_list_vs_numpy()`.
- Explain: "List addition concatenates, but array addition performs element-wise math."
- Explain: "List multiplication repeats elements, while array multiplication scales numerically."

### 5. Common Mistakes + Shape Awareness (20-30 Seconds)
- Point to `section_common_mistakes()`.
- Explain: "Array math requires compatible shapes for element-wise operations."
- Scenario response: "If I see a shape-related error, I check each array's shape and make sure they are compatible."

---

## Assignment Checklist Coverage
- ✅ Creating NumPy arrays
- ✅ Performing basic arithmetic operations
- ✅ Demonstrating scalar operations
- ✅ Explaining element-wise behavior
- ✅ Showing list vs array math differences
- ✅ Highlighting common shape and dtype pitfalls

## Best Practices to Keep
- Prefer NumPy operations over loops for simple array math.
- Verify shapes before combining arrays.
- Keep demonstration arrays small and numeric for clarity.
- Print outputs clearly to confirm behavior.
