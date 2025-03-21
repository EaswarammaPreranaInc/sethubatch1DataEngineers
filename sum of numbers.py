# Function to calculate sum of numbers from 1 to n
def sum_n(n):
    total = 0  # Initialize sum to 0
    for i in range(1, n + 1):  # Loop from 1 to n
        total += i  # Add i to total
    return total  # Return the final sum

# Input from user
n = int(input("Enter a number: "))
result = sum_n(n)  # Call the function
print(f"Sum of numbers from 1 to {n} is: {result}")
# output :
# '''Enter a number: 6
# Sum of numbers from 1 to 6 is: 21'''