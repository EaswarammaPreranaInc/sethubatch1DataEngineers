def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * (pow((1 + rate / 100), time)) - principal

# Taking user inputs
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

# Calculating interests
simple_interest = calculate_simple_interest(principal, rate, time)
compound_interest = calculate_compound_interest(principal, rate, time)

# Displaying results
print(f"Simple Interest: {simple_interest}")
print(f"Compound Interest: {compound_interest}")
