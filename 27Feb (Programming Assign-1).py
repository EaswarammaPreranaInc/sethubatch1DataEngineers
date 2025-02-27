-------------------------------------------------------------------------------------------------
#1. FindArea and Perimeter of rectangle.
-------------------------------------------------------------------------------------------------
try:
	L =float(input("enter length of rectangle: ")) -->4
	B =float(input("enter breath of rectangle:")) -->5
	area=L*B
	per=2*(L+B)
	print(F'Area: {area:.2f}') --->20.00
	print(F'perimeter: {per:.2f}') --->18.00
except:
	print('Input should be number')

--------------------------------------------------------------------------------------------------
#2. Find Volume of a sphere.
---------------------------------------------------------------------------------------------------
import math
try:
		r=float(input("enter radius: "))--->3.5
		volume=4/3*math.pi*r**3
		print(F'Volume of sphere : {volume:.2f}') --->179.59
except:
		print('Input should be number')
-----------------------------------------------------------------------------------------------------
#3. Find Simple interst and compound intrest
-----------------------------------------------------------------------------------------------------
try:
	P=float(input("enter principle: ")) --->10000
	T=float(input("enter Time: ")) --->3
	R=float(input("enter rate: ")) --->7.5  
	SI=(P*T*R)/100
	CI=P*(1+R/100)**T-P
	print(F'Simple intrest: {SI:.2f}')--->2250.00
	print(F'Compound intrest: {CI:.2f}') --->2422.97
except:
	print('Input should be a number')
-----------------------------------------------------------------------------------------------------
#4. Find swap values using 3rd object.
------------------------------------------------------------------------------------------------------
try:
	X=float(input("enter 1st input: ")) 
	Y=float(input("enter 2nd input: ")) 
	temp=X
	X=Y
	print(F'After swap: )
except:
	print('Input should be a number')
 
-------------------------------------------------------------------------------------------------------
#5. Swap two numbers without using 3rd object.type(1) 
----------------------------------------------------------------------------------------------------------
try:
------------------------------------------------------------------------------------------------------------
#6. Swap two numbers without using 3rd object.type(2) 
--------------------------------------------------------------------------------------------------------------
try:
-------------------------------------------------------------------------------------------------------------
#7. WAP to add,substract,multiply and divide two complex numbers. 
---------------------------------------------------------------------------------------------------------------(
try:
    A = complex(input('Enter first complex number: '))
    B = complex(input('Enter second complex number: '))  
    Sum = A + B
    Difference = A - B
    Product = A * B
    Division = A / B
    print('Sum:', Sum) --->(8+10j)
    print('Difference:', Difference) --->(-2-2j)
    print('Product:', Product) --->(-9+38j)
    print('Division:', Division) --->(0.6393442622950819+0.03278688524590165j)
except ValueError:
    print('The value entered is not a valid complex number.')
---------------------------------------------------------------------------------------------------------------------
#8.WAP to determine sum,difference,product,quotient,largest and smallest of 2 numbers.
---------------------------------------------------------------------------------------------------------------------
import math
A = int(input('Enter first integer number: ')) --->10
B = int(input('Enter second integer number: ')) --->7
add = A + B
Sub = A - B
prod = A * B
div = A / B
per = A % B
Maximum = max(A,B)
Minimum = min(A,B)
power = A ** B
Square = math . sqrt(A)
Commondivisor = math . gcd(A,B)
fact = math . factorial(A)
print(F'10+7: {add:}') --->17
print(F'10-7: {Sub:}') --->63
print(F'10*7: {prod:}') --->70
print(F'10/7: {div:}') --->1.4285714285714286
print(F'10%7: {per:}') --->3
print(F'max(10,7): {Maximum:}') --->10
print(F'max(10,7): {Minimum:}') --->3
print(F'10^7: {power:}') --->10000000
print(F'sqrt(10): {Square:}') --->3.162277660168375
print(F'gcd(10 ,7): {Commondivisor:}') --->1
print(F'fact(10): {fact:}') --->3628800

-----------------------------------------------------------------------------------------------------------------------
#9. swap values of objects without using 3rd object
-----------------------------------------------------------------------------------------------------------------------

