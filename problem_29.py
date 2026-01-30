# Problem 29: Function with default argument
# Find and fix the error

# ...existing code...
# Problem 29: Function with default argument
# Find and fix the error

def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

# examples
print(append_to_list(1))          # [1]
print(append_to_list(2))          # [2]  (not [1, 2])
print(append_to_list(3, [10]))    # [10, 3]
# ...existing code...
