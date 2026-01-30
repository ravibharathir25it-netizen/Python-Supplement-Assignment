# Problem 20: Find common elements in two lists
# Find and fix the error

# ...existing code...
# Problem 20: Find common elements in two lists
# Find and fix the error

def common_elements(a, b):
    b_set = set(b)
    return [x for x in a if x in b_set]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 1]
print(f"Common elements: {common_elements(list1, list2)}")
# ...existing code...
# filepath: e:\PROJECT\Python-Supplement-Assignment\problem_20.py
# ...existing code...
# Problem 20: Find common elements in two lists
# Find and fix the error

def common_elements(a, b):
    b_set = set(b)
    return [x for x in a if x in b_set]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 1]
print(f"Common elements: {common_elements(list1, list2)}")
# ...existing code...
