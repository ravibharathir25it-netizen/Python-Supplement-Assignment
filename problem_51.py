# Problem 51: Reverse words in a sentence
# Find and fix the error

# ...existing code...
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

text = "Hello World"
print(f"Reversed words: {reverse_words(text)}")
# ...existing code...
