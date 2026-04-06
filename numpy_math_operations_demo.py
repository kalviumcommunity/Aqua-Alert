"""
Milestone: Basic Mathematical Operations on NumPy Arrays
=========================================================
Demonstrates:
  - Element-wise arithmetic between arrays
  - Scalar operations on arrays
  - NumPy array math vs Python list behavior
  - Common mistakes (shape mismatch, type issues)

This script is intentionally fundamentals-only.
"""

import numpy as np


def print_header(title: str) -> None:
    print("\n" + "=" * 64)
    print(f"  {title}")
    print("=" * 64)


def section_elementwise_operations() -> None:
    print_header("1) Element-Wise Array Operations")

    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])

    print(f"Array a: {a}")
    print(f"Array b: {b}")
    print("Both arrays have shape:", a.shape)

    print("\nElement-wise results (matching positions):")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")


def section_scalar_operations() -> None:
    print_header("2) Scalar Operations on Arrays")

    values = np.array([5, 10, 15, 20])
    scalar = 3

    print(f"Base array: {values}")
    print(f"Scalar    : {scalar}")

    print("\nScalar applied to every element:")
    print(f"values + 3 = {values + scalar}")
    print(f"values - 3 = {values - scalar}")
    print(f"values * 3 = {values * scalar}")
    print(f"values / 3 = {values / scalar}")


def section_list_vs_numpy() -> None:
    print_header("3) Comparing Python Lists and NumPy Arrays")

    list_x = [1, 2, 3]
    list_y = [10, 20, 30]

    array_x = np.array([1, 2, 3])
    array_y = np.array([10, 20, 30])

    print(f"Python lists: {list_x} and {list_y}")
    print(f"NumPy arrays: {array_x} and {array_y}")

    print("\nList behavior:")
    print(f"list_x + list_y = {list_x + list_y}  (concatenation)")
    print(f"list_x * 2      = {list_x * 2}      (repetition)")

    print("\nNumPy behavior:")
    print(f"array_x + array_y = {array_x + array_y}  (element-wise addition)")
    print(f"array_x * 2       = {array_x * 2}        (element-wise scaling)")


def section_common_mistakes() -> None:
    print_header("4) Avoiding Common Mistakes")

    same_shape_left = np.array([2, 4, 6])
    same_shape_right = np.array([1, 3, 5])
    print("Compatible shapes example:")
    print(f"left shape : {same_shape_left.shape}")
    print(f"right shape: {same_shape_right.shape}")
    print(f"left + right = {same_shape_left + same_shape_right}")

    mismatch_left = np.array([10, 20, 30])
    mismatch_right = np.array([1, 2])
    print("\nIncompatible shapes example:")
    print(f"left shape : {mismatch_left.shape}")
    print(f"right shape: {mismatch_right.shape}")
    try:
        print(mismatch_left + mismatch_right)
    except ValueError as error:
        print(f"Caught ValueError: {error}")
        print("Lesson: use arrays with compatible shapes for element-wise math.")

    mixed_type_array = np.array([1, 2, "3"])
    print("\nMixed type array example:")
    print(f"mixed_type_array: {mixed_type_array}")
    print(f"dtype: {mixed_type_array.dtype}")
    print("Lesson: mixed types can coerce values to string/object, which can break numeric workflows.")


def summary() -> None:
    print_header("Summary")
    print(
        """
Key takeaways:
1. NumPy applies arithmetic element-wise for arrays of compatible shapes.
2. Scalar math applies the same operation to every array element.
3. Python lists do not perform true numeric vector math by default.
4. Shape compatibility matters for safe array operations.
5. Keeping data numeric avoids unexpected dtype issues.
"""
    )


if __name__ == "__main__":
    section_elementwise_operations()
    section_scalar_operations()
    section_list_vs_numpy()
    section_common_mistakes()
    summary()
