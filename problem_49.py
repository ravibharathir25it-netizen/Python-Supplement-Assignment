# Problem 49: Find all divisors of a number
# Find and fix the error

# ...existing code...
def find_divisors(n):
    n = abs(int(n))
    if n == 0:
        return []
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    return sorted(divisors)

num = 36
print(f"Divisors of {num}: {find_divisors(num)}")
# ...existing code...
