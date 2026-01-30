# Problem 47: Check if string starts with a specific character
# Find and fix the error

# ...existing code...
def starts_with(text, char):
    return text.startswith(char)

word = "Python"
print(f"Starts with 'P': {starts_with(word, 'P')}")
print(f"Starts with 'J': {starts_with('', 'J')}")
# ...existing code...
