"""
Milestone: NumPy Shape, Dimensions, and Index Positions
=======================================================
Demonstrates:
  - Understanding array shape and dimensions
  - Distinguishing 1D vs 2D arrays
  - Accessing values with correct index positions
  - Visualizing row/column layout
  - Avoiding common indexing mistakes

This script intentionally uses only NumPy fundamentals.
"""

import numpy as np


def print_header(title: str) -> None:
    print("\n" + "=" * 62)
    print(f"  {title}")
    print("=" * 62)


def section_shape_basics() -> None:
    print_header("1) Understanding Array Shape")

    arr_1d = np.array([12, 18, 21, 30, 42])
    print(f"1D array: {arr_1d}")
    print(f"Shape   : {arr_1d.shape}  -> 5 elements in one axis")

    arr_2d = np.array([
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
    ])
    print("\n2D array:")
    print(arr_2d)
    print(f"Shape   : {arr_2d.shape}  -> 3 rows, 4 columns")
    print("Interpretation:")
    print("  - First number = rows")
    print("  - Second number = columns")


def section_dimensions() -> None:
    print_header("2) Understanding Dimensions (ndim)")

    arr_1d = np.array([5, 10, 15])
    arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
    arr_3d = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ])

    print(f"1D array ndim: {arr_1d.ndim}, shape: {arr_1d.shape}")
    print(f"2D array ndim: {arr_2d.ndim}, shape: {arr_2d.shape}")
    print(f"3D array ndim: {arr_3d.ndim}, shape: {arr_3d.shape}")
    print("\nAxis idea (basic):")
    print("  - axis 0: outer direction (rows in 2D)")
    print("  - axis 1: inner direction (columns in 2D)")


def section_indexing() -> None:
    print_header("3) Accessing Elements Using Index Positions")

    arr_1d = np.array([100, 200, 300, 400, 500])
    print(f"1D array: {arr_1d}")
    print("Zero-based positions: 0, 1, 2, 3, 4")
    print(f"arr_1d[0] = {arr_1d[0]}")
    print(f"arr_1d[2] = {arr_1d[2]}")
    print(f"arr_1d[4] = {arr_1d[4]}")

    grid = np.array([
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33],
    ])
    print("\n2D array:")
    print(grid)
    print("2D indexing format: array[row, column]")
    print(f"grid[0, 0] = {grid[0, 0]}  (first row, first column)")
    print(f"grid[1, 2] = {grid[1, 2]}  (second row, third column)")
    print(f"grid[2, 1] = {grid[2, 1]}  (third row, second column)")


def section_visualize_layout() -> None:
    print_header("4) Visualizing Array Layout")

    table = np.array([
        [101, 102, 103, 104],
        [201, 202, 203, 204],
        [301, 302, 303, 304],
    ])

    print("Array as a grid:")
    print(table)
    print("\nIndex map -> value")
    for row_index in range(table.shape[0]):
        for col_index in range(table.shape[1]):
            value = table[row_index, col_index]
            print(f"  [{row_index}, {col_index}] -> {value}")

    print("\nMemory-order intuition (row-major display):")
    print("  NumPy stores data so row positions are grouped in sequence.")
    print("  For this table, values are laid out row by row: 101..104, 201..204, 301..304")


def section_common_mistakes() -> None:
    print_header("5) Common Indexing Mistakes and Safe Checks")

    arr = np.array([7, 14, 21])
    print(f"Array: {arr}, shape: {arr.shape}")
    print("Safe rule: valid index range is 0 to len(array)-1")

    candidate_index = 3
    if 0 <= candidate_index < arr.shape[0]:
        print(f"arr[{candidate_index}] = {arr[candidate_index]}")
    else:
        print(f"arr[{candidate_index}] is out of range. Skipping access safely.")

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\n2D matrix shape: {matrix.shape}  -> rows=2, cols=3")
    print("Common confusion: matrix[1, 2] means row 1 first, then column 2.")

    try:
        print(f"matrix[1, 2] = {matrix[1, 2]}")
        print("Attempting matrix[2, 1] (invalid row index) ...")
        print(matrix[2, 1])
    except IndexError as error:
        print(f"Caught IndexError: {error}")
        print("Lesson: always check shape before indexing.")


def summary() -> None:
    print_header("Summary")
    print(
        """
Key takeaways:
1. shape tells how data is organized across axes.
2. ndim tells how many dimensions an array has.
3. 2D indexing is always [row, column].
4. Indexing is zero-based.
5. Checking shape before access prevents index bugs.
"""
    )


if __name__ == "__main__":
    section_shape_basics()
    section_dimensions()
    section_indexing()
    section_visualize_layout()
    section_common_mistakes()
    summary()
