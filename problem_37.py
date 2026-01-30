# Problem 37: Check if year is leap year
# Find and fix the error
# ...existing code...
# Problem 37: Check if year is leap year
# Find and fix the error

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

print(f"Is 1900 a leap year? {is_leap_year(1900)}")
# ...existing code...
