# Get user input
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize an empty list for the reversed words
reversed_words = []

# Loop through the words in reverse order using a negative index
for i in range(1, len(words) + 1):
    reversed_words.append(words[-i])

# Join the reversed words into a sentence
reversed_sentence = " ".join(reversed_words)

# Print the reversed sentence
print("Reversed sentence:", reversed_sentence)
