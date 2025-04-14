#1/4/2025
'''
import time
def x(a, b):
    
    
    yield F'Sum:{a + b}'
    yield F'Difference:{a - b}'
    yield F'Product:{a * b}'
    try:
        yield F'Division:{a / b}'
    except:
        yield "Division by zero is undefined"
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

for result in x(a, b):
    print(result)
    time.sleep(2)'

#===============================================
import time
def f1(start,end):
    while start<=end:
        yield start
        start+=1
x=int(input("Enter start value:"))
y=int(input("Enter end value:"))
g=f1(x,y)
for k in g:
    print(k)
    time.sleep(2)
    
#=================================================
import time
def f1(s):
    list=s.split()
    for word in list:
        yield word
s=input("Enter any string:")
g=f1(s)
print("Words of the string")
for x in g:
    print(x)
    time.sleep(2)
    
#==============================================
import time
def f(n):
    a, b = 0, 1  # First two terms
    for _ in range(n):
        yield a  # Yield the current term
        a, b = b, a + b  # Update a and b for the next term
        
# Example usage
x = 7  # Number of terms to generate
for term in f(x):
    print(term)
    time.sleep(2)
#===========================================

# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)#[10 , 20]<class list>{30 , 40 , 50}<class set>(60  , 70 , 80 , 90)<class 'tuple'>100<class 'int'>
	print(type(x))

#============================================
#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')#Begin
print(*g)
print('End')

#============================================
#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)

#============================================
#  Find    outputs (Home  work)
def      f1():
	print('One')#one
	yield    1 #1
	print('Two')#Two
	yield    2#2
	print('Three')#Three
	yield    3#3
	print('End')#End
# End  of  generator
g = f1()
for   m   in   g:
	print(m)#one Two Three End
x ,  y ,  z  =  f1()
print(x)#1
print(y)#2
print(z)#3'

#==========================================================
# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1()#error
#p , q , r, s ,m=f1()#error

#===============================================
#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g))
#print(g * 3)
#print(g[0])
#print(g[1:3])
print(*g)#1 2 3
'''
#==================================================




