# Define the list
numbers = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]

# Define the target element to search
search_element = 15

# Initialize a counter for occurrences
count = 0

# Iterate through the list using index
for index in range(len(numbers)):
    if numbers[index] == search_element:
        print(f"{search_element} is found at index {index}")
        count += 1

# Print the total occurrences
print(f"{search_element} is found {count} times")
