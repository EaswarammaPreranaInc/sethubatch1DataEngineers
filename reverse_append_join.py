# Get user input
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize an empty list for reversed words
reversed_words = []

# Loop through each word and reverse it using slicing
for word in words:
    reversed_words.append(word[::-1])

# Join the reversed words into a sentence
reversed_sentence = " ".join(reversed_words)

# Print the reversed sentence
print("Reversed sentence:", reversed_sentence)