# Problem 35: Calculate percentage
# Find and fix the error


# ...existing code...
def calculate_percentage(obtained, total):
    try:
        obtained = float(obtained)
        total = float(total)
    except (TypeError, ValueError):
        raise ValueError("obtained and total must be numeric")
    if total == 0:
        return 0.0
    return (obtained / total) * 100

# examples
print(f"Percentage: {calculate_percentage(45, 50):.2f}%")   # 90.00%
print(f"Percentage: {calculate_percentage(0, 0):.2f}%")     # 0.00% (safe for zero total)
# ...existing code...