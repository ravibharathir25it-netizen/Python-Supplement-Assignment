# Problem 54: Find nth Fibonacci number
# Find and fix the error

# ...existing code...
def nth_fibonacci(n):
    """
    Return the n-th Fibonacci number (0-based):
    nth_fibonacci(0) == 0, nth_fibonacci(1) == 1
    """
    n = int(n)
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# examples
print(nth_fibonacci(0))   # 0
print(nth_fibonacci(1))   # 1
print(nth_fibonacci(10))  # 55
# ...existing code...
