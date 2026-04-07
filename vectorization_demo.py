import numpy as np


def loop_based_operation(numbers: np.ndarray) -> np.ndarray:
    """Apply a simple calculation to each value with a Python loop."""
    result = np.zeros_like(numbers)
    for index in range(len(numbers)):
        result[index] = (numbers[index] * 2) + 3
    return result


def vectorized_operation(numbers: np.ndarray) -> np.ndarray:
    """Apply the same calculation using NumPy vectorization."""
    return (numbers * 2) + 3


def main() -> None:
    print("--- NumPy Vectorization Demonstration ---")

    print("\n1. Creating a NumPy array")
    numbers = np.array([1, 2, 3, 4, 5])
    print(f"Input array: {numbers}")

    print("\n2. Loop-based operation: result[i] = (numbers[i] * 2) + 3")
    loop_result = loop_based_operation(numbers)
    print(f"Loop result:       {loop_result}")

    print("\n3. Vectorized operation: result = (numbers * 2) + 3")
    vectorized_result = vectorized_operation(numbers)
    print(f"Vectorized result: {vectorized_result}")

    print("\n4. Verifying both results match")
    if np.array_equal(loop_result, vectorized_result):
        print("Both approaches produced the same values.")
    else:
        print("The results do not match.")


if __name__ == "__main__":
    main()
