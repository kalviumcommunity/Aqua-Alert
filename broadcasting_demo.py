"""
Milestone: NumPy Broadcasting Demonstration
===========================================
Demonstrates:
  - Inspecting shapes before applying operations
  - Scalar-to-array broadcasting
  - 1D-to-2D broadcasting
  - Verifying broadcasted results

This script uses only simple NumPy fundamentals.
"""

import numpy as np


def print_header(title: str) -> None:
    print("\n" + "=" * 64)
    print(f"  {title}")
    print("=" * 64)


def section_scalar_broadcasting() -> None:
    print_header("1) Scalar-to-Array Broadcasting")

    temperatures = np.array([18, 20, 22, 24])
    offset = np.array(3)

    print(f"Array values : {temperatures}")
    print(f"Array shape  : {temperatures.shape}")
    print(f"Scalar value  : {offset}")
    print(f"Scalar shape  : {offset.shape}")

    result = temperatures + offset
    expected = np.array([21, 23, 25, 27])

    print("\nOperation: temperatures + offset")
    print(f"Result       : {result}")
    print(f"Expected     : {expected}")
    print(f"Match        : {np.array_equal(result, expected)}")
    print(
        "Why it works: the scalar has shape (), so NumPy can apply it to every "
        "element in the 1D array without shape conflict."
    )


def section_1d_to_2d_broadcasting() -> None:
    print_header("2) 1D-to-2D Broadcasting")

    sensor_grid = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
    ])
    row_adjustments = np.array([1, 2, 3])

    print(f"2D array shape   : {sensor_grid.shape}")
    print(sensor_grid)
    print(f"1D array shape   : {row_adjustments.shape}")
    print(row_adjustments)

    result = sensor_grid + row_adjustments
    expected = np.array([
        [11, 22, 33],
        [41, 52, 63],
        [71, 82, 93],
    ])

    print("\nOperation: sensor_grid + row_adjustments")
    print(result)
    print(f"Expected result  :\n{expected}")
    print(f"Match            : {np.array_equal(result, expected)}")
    print(
        "Why it works: the 1D array matches the last axis of the 2D array, "
        "so NumPy reuses it across each row."
    )


def summary() -> None:
    print_header("Summary")
    print(
        """
Key takeaways:
1. Always inspect array shapes before relying on broadcasting.
2. A scalar broadcasts naturally to every element in an array.
3. A 1D array can broadcast across a 2D array when the trailing dimension matches.
4. Matching results confirm that the broadcasted operation behaved as intended.
"""
    )


if __name__ == "__main__":
    section_scalar_broadcasting()
    section_1d_to_2d_broadcasting()
    summary()