# Problem 79: Calculate compound interest
# Find and fix the error
def compound_interest(principal, rate, time, n):
    # Calculate total amount after interest
    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    # Return only the interest earned
    return amount - principal

p = 1000  # Principal
r = 5     # Annual interest rate in %
t = 2     # Time in years
n = 4     # Number of times interest applied per year (quarterly)
print(f"Compound Interest: {compound_interest(p, r, t, n)}")


