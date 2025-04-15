# Taking input through input function
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Swapping the first two characters and concatenating with a space
result = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]


print(result)
# #Output
# ''Enter first string: Java
# Enter second string: Python
# Pyva Jathon