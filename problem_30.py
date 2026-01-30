# Problem 30: Calculate area of circle
# Find and fix the error

# ...existing code...
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

r = 5  # was "5" (string); use numeric
print(f"Area: {area_of_circle(r)}")
# ...existing code...

