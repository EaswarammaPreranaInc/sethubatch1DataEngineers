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
		print(X,Y)
except:
		print('Input should be a number')


				

