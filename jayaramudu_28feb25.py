# Ex-1: Check Even or Odd
try:
    num = int(input('Enter any number: '))
    if num % 2 == 0:
        print('Even Number')
    else:
        print('Odd Number')
except:
    print('Input should be an integer')

# Ex-2: Print Month Name by Number
try:
    m = int(input("Enter month number (1-12): "))
    if m == 1:
        print("January")
    elif m == 2:
        print("February")
    elif m == 3:
        print("March")
    elif m == 4:
        print("April")
    elif m == 5:
        print("May")
    elif m == 6:
        print("June")
    elif m == 7:
        print("July")
    elif m == 8:
        print("August")
    elif m == 9:
        print("September")
    elif m == 10:
        print("October")
    elif m == 11:
        print("November")
    elif m == 12:
        print("December")
    else:
        print("Input should be between 1 and 12.")
except:
    print("Input should be an integer")

# Ex-3: Check Leap Year
try:
    l = int(input('Enter a 4-digit year: '))
    if l % 4 == 0 and l % 100 != 0 or l % 400 == 0:
        print('Leap year')
    else:
        print('Not a leap year')
except:
    print('Input should be an integer')

# Ex-4: Find Largest of Three Numbers
try:
    a = int(input('Enter 1st input: '))
    b = int(input('Enter 2nd input: '))
    c = int(input('Enter 3rd input: '))
    if a > b and a > c:
        print(f'Largest number: {a}')
    elif b > c:
        print(f'Largest number: {b}')
    else:
        print(f'Largest number: {c}')
except:
    print('Input should be an Integer')

# Ex-5: Convert Celsius to Fahrenheit and Vice-Versa
try:
    a = int(input('Enter 1 for Celsius to Fahrenheit and 2 for Fahrenheit to Celsius: '))
    if a == 1:
        c = float(input('Enter Celsius temperature: '))
        print(f'Fahrenheit equivalent: {1.8 * c + 32:.2f}')
    elif a == 2:
        f = float(input('Enter Fahrenheit temperature: '))
        print(f'Celsius equivalent: {(f - 32) / 1.8:.2f}')
    else:
        print("Invalid input")
except:
    print('Input should be an integer')

# Ex-6: Determine Quadrant of a Point
try:
    x = int(input('Enter x-coordinate: '))
    y = int(input('Enter y-coordinate: '))
    if x > 0 and y > 0:
        print('1st quadrant')
    elif x < 0 and y > 0:
        print('2nd quadrant')
    elif x < 0 and y < 0:
        print('3rd quadrant')
    elif x > 0 and y < 0:
        print('4th quadrant')
    elif x != 0 and y == 0:
        print("x-axis")
    elif x == 0 and y != 0:
        print("y-axis")
    else:
        print('Origin')
except:
    print('Input should be an integer')

# Ex-7: Find Largest, Smallest, and Middle of Three Numbers
try:
    a, b, c = map(float, input('Enter three numbers: ').split())
    max_val = max(a, b, c)
    min_val = min(a, b, c)
    mid_val = (a + b + c) - (max_val + min_val)
    print(f'Largest: {max_val}, Smallest: {min_val}, Middle: {mid_val}')
except:
    print("Invalid input")

# Ex-8: Check Triangle Type
import math
try:
    a, b, c = map(int, input('Enter three sides: ').split())
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            print(f'Equilateral Triangle, Area: {math.sqrt(3) / 4 * (a ** 2):.2f}')
        elif a == b or b == c or a == c:
            print(f'Isosceles Triangle, Perimeter: {a + b + c:.2f}')
        else:
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print(f'Scalene Triangle, Area: {area:.2f}, Perimeter: {a + b + c:.2f}')
    else:
        print('Not a Triangle')
except:
    print("Invalid Input")

# Ex-9 : Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

import math

try:
    a = float(input('Enter value of a: '))
    if a != 0:
        b = float(input('Enter value of b: '))
        c = float(input('Enter value of c: '))
        disc = b ** 2 - 4 * a * c  # Discriminant
        print(disc)
        if disc > 0:
            root1 = (-b + math.sqrt(disc)) / (2 * a)
            root2 = (-b - math.sqrt(disc)) / (2 * a)
            print(f'Roots are real and distinct:\nRoot 1: {'%.2f' %root1}\nRoot 2: {'%.2f' %root2}')

        elif disc == 0:
            root1 = -b / (2 * a)
            print(f'Roots are real and equal:\n Root: {root1}')

        else:
            real = -b / (2 * a)
            img = math.sqrt(-disc) / (2 * a)
            print(f'Roots are imaginary (complex):\nRoot 1: {real} + {img}j\nRoot 2: {real} - {img}j')

    else:
        print('Value of a cannot be 0')

except ValueError:
    print('Invalid input! Please enter numeric values.')


# Ex-10: Check if a Point Lies Inside, Outside, or On a Circle
import math
try:
    x, y = map(float, input('Enter x and y coordinates: ').split())
    r = float(input('Enter radius of circle: '))
    distance = math.sqrt(x ** 2 + y ** 2)
    if distance > r:
        print('Outside the circle')
    elif distance < r:
        print('Inside the circle')
    else:
        print('Point is on the circle')
except:
    print('Invalid Input')

#Ex-11: Print Day of the Week using match-case

try:
    day = int(input('Enter a number between 1-7: '))
    match day:
        case 1:
            print('Monday')
        case 2:
            print('Tuesday')
        case 3:
            print('Wednesday')
        case 4:
            print('Thursday')
        case 5:
            print('Friday')
        case 6:
            print('Saturday')
        case 7:
            print('Sunday')
        case _:
            print('Invalid Day')
except:
    print('Input should be an integer')
# Ex-12: Print Digit in Words using match-case
try:
    digit = int(input('Enter a digit: '))
    match digit:
        case 0:
            print('Zero')
        case 1:
            print('One')
        case 2:
            print('Two')
        case 3:
            print('Three')
        case 4:
            print('Four')
        case 5:
            print('Five')
        case 6:
            print('Six')
        case 7:
            print('Seven')
        case 8:
            print('Eight')
        case 9:
            print('Nine')
        case _:
            print('Not a digit')
except:
    print('Input should be an integer')
# Ex-13: Calculate Electricity Bill using match-case
try:
    units = int(input('Enter units: '))
    match units // 100:
        case 0:
            cost = units * 3.00
        case 1:
            cost = 100 * 3.00 + (units - 100) * 3.50
        case 2 | 3:
            cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
        case 4 | 5 | 6:
            cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
        case _:
            cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00
    print(f"Bill amount: Rs. {cost:.2f}")
except ValueError:
    print("Invalid Input! Please enter an integer.")

# Ex-14: Fibonacci Series up to x
try:
    x = int(input('Enter value of x: '))
    a, b = 0, 1
    print(a)
    print(b)
    c = a + b
    while c < x:
        print(c)
        a, b = b, c
        c = a + b
except:
    print('Input should be an integer')
