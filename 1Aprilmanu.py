'''
#1)Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

#Hint:  Use  generator  function  and  for  loop  to  retrieve  elements

def arithmetic_operations(a, b):
    # Yield the sum
    yield a + b
    # Yield the difference
    yield a - b
    # Yield the product
    yield a * b
    # Yield the division (checking for division by zero)
    if b != 0:
        yield a / b
    else:
        yield "Division by zero is not allowed"

# Example of how to use the generator:
a = 6
b = 8

print(" arithmetic_operations(a, b):(a+b),(a-b),(a*b),(a/b))

(or)

import time
def arithmetic_operations(a, b):
    # Yield the sum
    yield a + b
    # Yield the difference
    yield a - b
    # Yield the product
    yield a * b
    # Yield the division (checking for division by zero)
    if b != 0:
        yield a / b
    else:
        yield "Division by zero is not allowed"


# Taking user input for a and b 
a = int(input("Enter the first number (a): ")) # we can use flaot (or) int here
b = int(input("Enter the second number (b): "))

# Using the generator to perform the operations
for result in arithmetic_operations(a, b):
	time.sleep(1)
	print(result)

(or)
import time
def arithmetic_operations(a, b):
    # Yield the sum
    yield a + b
    # Yield the difference
    yield a - b
    # Yield the product
    yield a * b
    # Yield the division (checking for division by zero)
    if b != 0:
        yield a / b
    else:
        yield "Division by zero is not allowed"

# Taking user input for a and b
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

# Create the generator
operations = arithmetic_operations(a, b)

# Manually retrieve each result using next()
sum_result = next(operations)
difference_result = next(operations)
product_result = next(operations)
division_result = next(operations)

# Print the results
time.sleep(1)
print("Sum:", sum_result)
time.sleep(1)
print("Difference:", difference_result)
time.sleep(1)
print("Product:", product_result)
time.sleep(1)
print("Division:", division_result)
time.sleep(1)
---------------------------------------------------------------------------------------------

#2)Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object

import time
def generate_from_x_to_y(x, y):
    while x <= y:
        yield x
        x += 1

# Input values
x = int(input("Enter the starting value (x): "))
y = int(input("Enter the ending value (y): "))

# Create the generator
gen = generate_from_x_to_y(x, y)

# Manually retrieve the values from the generator using next()

while True:
	try:
		time.sleep(1)
		print(next(gen))
	except StopIteration:
		pass


(or)


import time

def generate_from_x_to_y(x, y):
    while x <= y:
        yield x
        time.sleep(1)  # Delay of 1 second before yielding the next value
        x += 1

# Input values
x = int(input("Enter the starting value (x): "))
y = int(input("Enter the ending value (y): "))

# Create the generator
gen = generate_from_x_to_y(x, y)

# Manually retrieve the values from the generator using next()
try:
    while True:
        print(next(gen))
except StopIteration:
    pass


(or)
import time
def generate_from_x_to_y(x, y):
    while x <= y:
        yield x
        x += 1

# Input values
x = int(input("Enter the starting value (x): "))
y = int(input("Enter the ending value (y): "))

# Create the generator
gen = generate_from_x_to_y(x, y)

# Manually retrieve the values from the generator using next()

while True:
	try:
		time.sleep(1)
		print(next(gen))
	except StopIteration:
		pass
--------------------------------------------------------------------------------------------

#3)Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  ---> 0  and  1

4) Use  generator  function  and  for  loop


import time
def fibonacci_series(n):
    a, b = 0, 1  # First two terms
    for _ in range(n):
        yield a
        a, b = b, a + b  # Update to next two terms in the series

# Input: Get the number of terms from the user
n = int(input("Enter the number of Fibonacci terms to generate: "))

# Generate and print the Fibonacci series
for term in fibonacci_series(n):
	time.sleep(1)
	print(term)

(or)

import time
def fibonacci_until_max(max_value):
    a, b = 0, 1  # First two terms
    while a <= max_value:
        yield a
        a, b = b, a + b  # Update to next two terms in the series

# Input: Get the maximum value from the user
max_value = int(input("What is the last value: "))

# Generate and print the Fibonacci series up to the specified maximum value
for term in fibonacci_until_max(max_value):
	time.sleep(1)
	print(term)
-----------------------------------------------------------------------------------------

#4)Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class

Enter  any   string  :  Hyd is green city
Words  of  the  string
Hyd
is
green
city


import time
def word_generator(input_string):
    # Split the string into words using split() method
    words = input_string.split()
    
    # Yield each word one by one
    for word in words:
        yield word

# Input string
input_string = input("Enter any string: ")

# Create the generator
words = word_generator(input_string)

# Display the words
print("Words of the string:")
for word in words:
	time.sleep(1)
	print(word)
------------------------------------------------------------------------------------
#5) Find  outputs

def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	print(type(x))


outputs:-
---------

[10, 20] # for 1st iteration of for loop
<class 'list'>
{40, 50, 30} # for 2nd iteration of for loop
<class 'set'>
(60, 70, 80, 90) # for 3rd iteration of for loop
<class 'tuple'>
100 # for 4th iteration of for loop
<class 'int'>
----------------------------------------------------------------------------------------------------------

#6)Find  outputs

def   f1():
	x = 1
	while  x <=  100000000000000000000: # Memory Error
		yield  x
		x +=  1
# End of  generator
g = f1() # creating empty generator object 
print('Begin') # Begin
print(*g) # Memory Error unpack generator object,generator function fully executed from top to bottom and store the values in generators.
print('End')

(or)

def   f1():
	x = 1
	while  x <=  1000: # we get 1,2,3,4,-----------upto 1000
		yield  x
		x +=  1
# End of  generator
g = f1() # creating empty generator object 
print('Begin') # Begin
print(*g) # unpack generator object,generator function fully executed from top to bottom and store the values in generators.
print('End') # End

(or)

def f1():
    x = 1
    while x <= 10:  # A small stopping condition
        yield x
        x += 1

g = f1()
print('Begin')
print(*g)  # This will print numbers from 1 to 10
print('End')

----------------------------------------------------------------------------------------------

#7)Find  outputs
g = (x * x  for  x  in  range(500000000000000000)) # MemoryError
print(*g) # unpack generator object,generator function fully executed from top to bottom and store the values in generators.

(or)


#Find  outputs
g = (x * x  for  x  in  range(5000)) # we get the squareroot: 1,4,9,25,---------24990001(square of 5000)
print(*g) # unpack generator object,generator function fully executed from top to bottom and store the values in generators.

------------------------------------------------------------------------------------------------------------------------------------

#8)Find    outputs (Home  work)

def      f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1()
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()
print(x)
print(y)
print(z)

outputs:
---------
These are for loop iterations:

One # forloop iteration ---> 1
1   # forloop iteration ---> 1
Two # forloop iteration ---> 2
2   # forloop iteration ---> 2
Three # forloop iteration ---> 3
3     # forloop iteration ---> 3
End  # forloop iteration ---> 4
One # print (x) output bcz poits to f1()
Two # print (y) output bcz poits to f1()
Three # print (z) output bcz poits to f1()
End # bcz poits to f1()
1 # print (x) output bcz poits to f1()
2 # print (y) output bcz poits to f1()
3  # print (z) output bcz poits to f1()

---------------------------------------------------------------------------

#9)Identify  error (Home  work)

def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1() # Error due to less values to unpack the elements.
p , q , r , s , m = f1() # Error due to many values to unpack the elements.

#11)Find  outputs (Home  work)

def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g)) # length function is not there in generators 
#print(g * 3) # no Repeatation in generators.
#print(g[0]) # no Index in generators
#print(g[1 : 3]) # no Index  , so no slice methods in generators
print(*g) #  1  2  3------unpack generator object,generator function fully executed from top to bottom and store the values in generators.

--------------------------------------------------------------------------------------------------------------------

Exam patterns:-
-----------------
#1)Input : 123456789
Output  :  Twelve  crores  thirty  lakhs  fifty  six  thousand  seven  hundred  eighty  nine


def words(a):
    # Mapping of digits to words
    b = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    c = ''
    
    # Loop through each character in the input string
    for ch in a:
        # Append corresponding word for each digit
        c += b[int(ch)] + ' '
    
    # Return the final result with trailing spaces removed
    return c.strip()

# Input number as a string
a = input("Enter any number: ")

# Print the corresponding words for each digit
print('Each of words:', words(a))

# Print how many numbers (digits) were given in input
print('Number of digits:', len(a))


(or)

def words(a):
    # Mapping of digits to words
    b = {0:'zero',1:'one', 2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    
    c = ''
    
    # Loop through each character in the input string
    for ch in a:
        # Append corresponding word for each digit
        c += b[int(ch)] + ' '
    
    # Return the final result with trailing spaces removed
    return c.strip()

# Input number as a string
a = input("Enter any number: ")

# Print the corresponding words for each digit
print('Each of words:', words(a))

# Print how many numbers (digits) were given in input
print('Number of digits:', len(a))

----------------------------------------------------------------------------------------------------------------------

#2)
def roman(n):
    # List of numbers and their corresponding Roman numerals
    a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    b = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    c = ''  # Initialize the string to hold the Roman numeral
    
    # Iterate over the Roman numeral values
    for i in range(13):
        # While the number is larger than or equal to the current Roman numeral value
        while n >= a[i]:
            c += b[i]  # Append the corresponding Roman numeral to the result
            n -= a[i]  # Subtract the value from n
    
    return c  # Return the final Roman numeral string

# Input number
n = int(input("Enter any number: "))

# Output the Roman numeral equivalent of the number
print('Roman equivalent:', roman(n))

(or)



def roman(n):
    # Define the mapping of numbers to Roman numerals
    a = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    
    c = ''  # Initialize the string to hold the Roman numeral
    for value in a:
        # While the number is larger than or equal to the current Roman value
        while n >= value:
            c += a[value]  # Append the Roman numeral to the result string
            n -= value  # Subtract the value from the number
    
    return c  # Return the Roman numeral string

# Input the number from the user
d = int(input("Enter any number: "))

# Print the Roman numeral equivalent of the input number
print("Roman numeral:", roman(d))

-------------------------------------------------------------------------

#3)  output in lakhs
----------------------


def num_to_words(n):
    # Define mappings for digits and place values
    ones = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['', '', 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    thousands = ['', 'thousand','lakh','crore']

    # Function to convert numbers less than 1000 into words
    def convert_group(num):
        if num == 0:
            return ""
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
        else:
            return ones[num // 100] + " hundred" + (" " + convert_group(num % 100) if num % 100 != 0 else "")

    # Start converting the number by breaking it into groups of 1000s (lakhs, thousands, etc.)
    group_index = 0
    result = []
    while n > 0:
        if n % 1000 != 0:
            result.append(convert_group(n % 1000) + (" " + thousands[group_index] if thousands[group_index] else ""))
        n //= 1000
        group_index += 1

    # Join all parts and capitalize the first letter
    return ' '.join(reversed(result)).strip().capitalize()

# Input number
number = int(input("Enter any number: "))

# Convert the number to words
print("In words:", num_to_words(number))



