# Problem 18: Count words in a sentence
# Find and fix the error


# ...existing code...
# Problem 18: Count words in a sentence
# Find and fix the error

def count_words(sentence):
    if not sentence:
        return 0
    words = sentence.split()
    return len(words)

sentence = "This is an example sentence."
print(f"Word count: {count_words(sentence)}")
# ...existing code...