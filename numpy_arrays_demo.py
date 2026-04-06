"""
Milestone 4.22 - Creating NumPy Arrays from Python Lists
=========================================================
Demonstrates:
  - Importing NumPy
  - Creating 1D and 2D NumPy arrays from Python lists
  - Inspecting array properties (shape, dtype, ndim)
  - Basic element-wise arithmetic operations
  - Key differences between Python lists and NumPy arrays
"""

import numpy as np

# ─────────────────────────────────────────────────────────
# Section 1: Python Lists vs NumPy Arrays
# ─────────────────────────────────────────────────────────
print("=" * 55)
print("  Section 1: Python Lists vs NumPy Arrays")
print("=" * 55)

python_list = [10, 20, 30, 40, 50]
numpy_array = np.array([10, 20, 30, 40, 50])

print(f"Python list  : {python_list}")
print(f"NumPy array  : {numpy_array}")
print(f"Type of list : {type(python_list)}")
print(f"Type of array: {type(numpy_array)}")

# Demonstrating difference in math behaviour
print("\n>>> Multiply by 2 :")
print(f"  Python list  (×2): {python_list * 2}  ← list is repeated, NOT multiplied!")
print(f"  NumPy array  (×2): {numpy_array * 2}  ← element-wise multiplication")

# ─────────────────────────────────────────────────────────
# Section 2: Creating a 1D NumPy Array from a Python List
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  Section 2: 1D NumPy Array")
print("=" * 55)

temperatures = [36.6, 37.1, 38.0, 36.9, 37.5]          # plain Python list
temp_array   = np.array(temperatures)                    # convert to NumPy array

print(f"Original list  : {temperatures}")
print(f"NumPy 1D array : {temp_array}")
print(f"  Shape  : {temp_array.shape}")
print(f"  Dtype  : {temp_array.dtype}")
print(f"  Ndim   : {temp_array.ndim}")

# ─────────────────────────────────────────────────────────
# Section 3: Creating a 2D NumPy Array from Nested Lists
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  Section 3: 2D NumPy Array (Matrix)")
print("=" * 55)

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = np.array(nested_list)

print("Nested Python list:")
for row in nested_list:
    print(f"  {row}")

print(f"\nNumPy 2D array:\n{matrix}")
print(f"  Shape  : {matrix.shape}   ← 3 rows, 3 columns")
print(f"  Dtype  : {matrix.dtype}")
print(f"  Ndim   : {matrix.ndim}")

# ─────────────────────────────────────────────────────────
# Section 4: Inspecting Array Properties
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  Section 4: Inspecting Array Properties")
print("=" * 55)

sample = np.array([3.14, 2.71, 1.41, 1.73])
print(f"Array         : {sample}")
print(f"  shape  : {sample.shape}   ← (4,) means 1D with 4 elements")
print(f"  dtype  : {sample.dtype}   ← 64-bit floating-point")
print(f"  ndim   : {sample.ndim}      ← 1-dimensional")
print(f"  size   : {sample.size}      ← total number of elements")

integer_arr = np.array([10, 20, 30])
print(f"\nInteger array : {integer_arr}")
print(f"  dtype  : {integer_arr.dtype}   ← 64-bit integer (inferred automatically)")

# ─────────────────────────────────────────────────────────
# Section 5: Basic Element-Wise Operations
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  Section 5: Basic Array Operations")
print("=" * 55)

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(f"Array a      : {a}")
print(f"Array b      : {b}")
print(f"  a + b      : {a + b}     ← element-wise addition")
print(f"  b - a      : {b - a}     ← element-wise subtraction")
print(f"  a * b      : {a * b}   ← element-wise multiplication")
print(f"  a ** 2     : {a ** 2}     ← squaring each element")
print(f"  b / 10     : {b / 10}   ← scalar division")

# ─────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  Summary")
print("=" * 55)
print("""
Key Takeaways
─────────────
1. np.array(list)    → converts a Python list into a NumPy array
2. Nested lists      → become multi-dimensional (2D, 3D …) arrays
3. .shape            → tuple describing dimensions  (rows, cols)
4. .dtype            → data type stored in the array
5. .ndim             → number of dimensions
6. Operations        → applied element-wise, not list-wise
7. Homogeneity       → all elements share the same data type,
                       making NumPy fast and memory-efficient
""")
