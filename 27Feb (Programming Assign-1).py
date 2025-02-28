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
#5. Swap two numbers without using 3rd object.(type1) 
----------------------------------------------------------------------------------------------------------
X=int(input("enter the 1st value: ")) --->10
Y=int(input("enter the 2nd value: ")) --->25
print(f"before swap :a : {a} \t b :{b}") --->10,25
c=X
X=Y
Y=c
print(f"after swap :a :{a}\t b :{b}") --->25.10
------------------------------------------------------------------------------------------------------------
#6. Swap two numbers without using 3rd object.(type2) 
--------------------------------------------------------------------------------------------------------------
X=int(input("enter the 1st value: ")) 
Y=int(input("enter the 2nd value: ")) 
print(f"before swap :X : {X} \t Y :{Y}")
X= X + Y
Y = X - Y
X = X - Y
print(f'after swap :X: {X} \t Y : {Y}')

-------------------------------------------------------------------------------------------------------------
#7. Swap two numbers without using 3rd object (type 3)
-------------------------------------------------------------------------------------------------------------
X=int(input("enter the 1st value: ")) --->25
Y=int(input("enter the 2nd value: ")) --->10
print(f"before swap :X : {X} \t Y :{Y}")
X= X * Y
Y = X // Y
X = X // Y
print(f'after swap :X: {X} \t Y : {Y}') --->X:10 Y:25

-------------------------------------------------------------------------------------------------------------
#8. WAP to add,substract,multiply and divide two complex numbers. 
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
#9.WAP to determine sum,difference,product,quotient,largest,smallest,sqrt,pow,GCD,factorial of 2 numbers.
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

---------------------------------------------------------------------------------------------------------------------
Gift
#10.Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
----------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
#11.Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
----------------------------------------------------------------------------------------------------------------------
A =  eval(input("Enter  1st input:")) --->enter any value int string,float,int,....... 10
B = eval(input("Enter 2nd input:")) --->enter any value int string,float,int,...........20
if A>B:
	print("Largest input:", A)
elif A<B:
    print("lagest input:", B)
else:
    print()
    			#output is displays largest of A and B o/p-->largest input is 20.
---------------------------------------------------------------------------------------------------------------------
#12.Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
----------------------------------------------------------------------------------------------------------------------
A = evla(input("enter first input:" )
B = evla(input("enter second input:" )
C = evla(input("enter third input:" )

---------------------------------------------------------------------------------------------------------------------
#13.Write  a  program  to  print   '>'  if  1st  input  >  2nd  input is '<'  if  1st  input  <  2nd  input  and
'=' inputs  are  same
---------------------------------------------------------------------------------------------------------------------
A = eval(input('Enter first integer number: ')) --->Enter any value int,float,string,list,.......
B = eval(input('Enter second integer number: ')) --->Enter any value int,float,string,list,........
if A>B:
	print('>')
elif A<B:
	print('<')
else:
 	print('=')
	
---------------------------------------------------------------------------------------------------------------------
#14.Write  a  program  to  test  input  is  even  number  or  odd  number
----------------------------------------------------------------------------------------------------------------------
A = int(input('Enter the number: ')) --->26
if A%2==0:
    print('The numbers even')
else:
    print('The number is odd')
					# output : The number is even


