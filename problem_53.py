# Problem 53: Check if two strings are anagrams
# Find and fix the error

# ...existing code...
def are_anagrams(str1, str2):
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

word1 = "Listen"
word2 = "Silent"
print(f"Are anagrams: {are_anagrams(word1, word2)}")
# ...existing code...
