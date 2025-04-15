# Get user input
string = input("Enter a string: ")

# Separate alphabets and digits
alphabets = sorted([ch for ch in string if ch.isalpha()])
digits = sorted([ch for ch in string if ch.isdigit()])

# Combine sorted alphabets and digits
sorted_string = "".join(alphabets + digits)

# Print the sorted string
print("Sorted string:", sorted_string)
