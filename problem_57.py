# Problem 57: Find LCM of two numbers
# Find and fix the error

# ...existing code...
def remove_vowels(text):
    vowels = set("aeiouAEIOU")
    return "".join(ch for ch in text if ch not in vowels)

s = "Hello World"
print(f"Without vowels: {remove_vowels(s)}")
# ...existing code...
