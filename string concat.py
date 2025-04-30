def swap_and_concatenate(str1, str2):
    # Swapping the first two characters of each string
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    
    # Concatenating with space
    result = new_str1 + " " + new_str2
    return result

# Example input
str1 = "Java"
str2 = "Python"

# Output
output = swap_and_concatenate(str1, str2)
print(output)
