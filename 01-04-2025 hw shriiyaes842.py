
'''
1. Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  retrieve  elements
'''
def f1(a,b):
	print('Sum: ',end='')
	yield a+b
	print('Difference: ',end='')
	yield a-b
	print('Product: ',end='')
	yield a*b
	print('Division: ',end='')
	yield a/b
a=int(input("enter a number: "))
b=int(input("enter a number: "))
try:
	for x in f1(a,b):
		print(x)
except ZeroDivisionError:
	print('Divsion by 0 not permitted') 

'''
2*. Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def f2(a,b):
	while a<=b:
		yield a
		a+=1
	
a=int(input("enter start number: "))
b=int(input("enter end number: "))
for x in f2(a,b):
	print(x) 
'''
3.Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  ---> 0  and  1

4) Use  generator  function  and  for  loop
'''
def fib(i):
	a,b=0,1
	while a<=i:
		yield  a
		a,b=b,a+b
i=int(input("Fibonnaci series until some number: "))
for x in fib(i):
	print(x) 
'''
4. Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
''' 
def words(x):
	a=x.split()
	for x in a:
		yield x
x=input("Enter a String: ")
for x in words(x):
	print(x) 
# 5.  Find  outputs
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
'''
[10 , 20]
class list
{30 , 40 , 50}
class set
(60  , 70 , 80 , 90)
class tuple 
100
int '''
# 6. Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1() # Creating an empty generator object 
print('Begin') # Begin
print(*g) # memory error bcz it takes lot os space to have this numbers in generator and unpack it 
print('End')

# 7. Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g) # slow output .. console may crash 

# 8.  Find    outputs (Home  work)
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
'''
One
1
Two
2
Three
3
End
One
Two
Three
End
1
2
3
''' 
# 9. Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1() #  too many values to unpack (expected 3)
#p , q , r , s , m = f1()  # not enough values to unpack (expected 5, got 4)

# 10. Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g)) # error object of type 'generator' has no len()
# print(g * 3) # error unsupported operand type(s) for *: 'generator' and 'int'
#print(g[0]) # error 'generator' object is not subscriptable
#print(g[1 : 3]) #  error 'generator' object is not subscriptable
print(*g) # 1 2 3 
