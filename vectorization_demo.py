import numpy as np

def loop_based_operation(a, b):
    """Performs element-wise operation using a Python loop."""
    result = np.zeros_like(a)
    for i in range(len(a)):
        result[i] = a[i] * b[i] + 5
    return result

def vectorized_operation(a, b):
    """Performs the exact same operation using NumPy vectorization."""
    # This is not only more readable but also significantly faster
    # as NumPy delegates the iteration to optimized C code.
    return a * b + 5

def main():
    print("--- NumPy Vectorization Demonstration ---")
    
    # 1. Create NumPy arrays
    print("\n1. Creating NumPy Arrays...")
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([10, 20, 30, 40, 50])
    print(f"Array a: {a}")
    print(f"Array b: {b}")
    
    # 2. Write a loop-based numerical operation
    print("\n2. Executing loop-based operation: c[i] = a[i] * b[i] + 5")
    loop_result = loop_based_operation(a, b)
    print(f"Loop result: {loop_result}")
    
    # 3. Rewrite the same logic using vectorized operations
    print("\n3. Executing vectorized operation: c = a * b + 5")
    vectorized_result = vectorized_operation(a, b)
    print(f"Vectorized result: {vectorized_result}")
    
    # 4. Verify that both approaches produce the same result
    print("\n4. Verifying outputs match...")
    is_matching = np.array_equal(loop_result, vectorized_result)
    
    if is_matching:
        print("✅ SUCCESS: Both approaches produced the exact same result!")
    else:
        print("❌ ERROR: Results do not match.")

if __name__ == "__main__":
    main()
