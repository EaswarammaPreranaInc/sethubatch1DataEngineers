# Take dynamic input from the user
x = float(input("Enter 1st input  : "))
y = float(input("Enter 2nd input  : "))

# Display before swapping
print(f"Before swap :  x={x}           y={y}")

# Swapping using multiplication and division
x = x * y  # Step 1: Store product of x and y in x
y = x / y  # Step 2: Extract original x into y
x = x / y  # Step 3: Extract original y into x

# Display after swapping
print(f"After swap  :  x={x}           y={y}")

