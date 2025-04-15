# Get user input
string = input("Enter a string: ")

# Initialize an empty string for the reversed result
reversed_string = ""

# Loop through the string in reverse order using a negative index
for i in range(1, len(string) + 1):
    reversed_string += string[-i]

# Print the reversed string
print("Reversed string:", reversed_string)
