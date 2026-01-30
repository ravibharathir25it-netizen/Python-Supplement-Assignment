# Problem 25: Find GCD of two numbers
# Find and fix the error

# ...existing code...
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

x, y = 48, 18
print(f"GCD of {x} and {y} is {gcd(x, y)}")
# ...existing code...
