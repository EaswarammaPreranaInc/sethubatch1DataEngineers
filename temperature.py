#Write  a  program  to  convert  celsius  temperature  to  farenheit  and  farenheit to celsius with if statement

# Celsius to Fahrenheit conversion formula: (Celsius * 9/5) + 32
num=int(input("Enter 1 for celsius to farenheit or enter 2 for farenheit to celsius:"))

if num==1:
    celsius=int(input("Enter the temperature in celsius:"))
    fahrenheit=(celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif num==2:
    fahrenheit=int(input("Enter the temperature in fahrenheit:"))
    celsius=(fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid input. Please enter 1 or 2.")

