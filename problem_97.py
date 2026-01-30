# Problem 97: Remove element from list
# Find and fix the error
def remove_element(nums, val):
    i = 0                     # Pointer for the position of the next valid element
    for j in range(len(nums)): # j scans through all elements
        if nums[j] != val:    # If current element is not the one to remove
            nums[i] = nums[j] # Place it at the 'i'-th position
            i += 1             # Move the position pointer forward
    return i                  # Return the new length of the array


