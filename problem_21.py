# Problem 21: Check if list is sorted
# Find and fix the error

# ...existing code...
# Problem 21: Check if list is sorted
# Find and fix the error

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

print(is_sorted([1, 2, 3, 4]))   # True
print(is_sorted([1, 3, 2, 4]))   # False
print(is_sorted([]))             # True
# ...existing code...
