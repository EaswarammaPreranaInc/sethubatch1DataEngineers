'''#program to yield the arthmetic operations
try:
	import  time
	def   f1():
		yield  F' Sum : {a+b}'
		yield  F' Difference : {a-b}'
		yield  F' Multiplication : {a*b}'
		yield  F' Division: {a/b}'
	
	a=int(input("enter first number:"))
	b=int(input("enter second number:"))
	for  x  in   f1():
		print(x)
		time.sleep(2)
except ZeroDivisionError:
	print('Division  by zero  is  not  permitted')
	'''
'''
#program to print frm x to y without range in gen fun
def f1():
	global n
	global m
	while n<=m:
		yield n
		n+=1
n=int(input("Enter  start  value : "))
m=int(input("Enter  end  value : "))
for x in f1():
	print(x)
'''
'''
#program to sep string
def sep():
	l=s.split(' ')
	for i in l:
		yield i
s=input('enter any string: ')
for x in sep():
	print(x)
'''

'''
# Find  outputs
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

#outputs
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>
'''
'''
#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
print(*g)
print('End')
#output 
Begin
Memory error as *g converts genetor to seqence
'''
'''
#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)
#output
Memory error as *g converts genetor to seqence
'''
'''
#  Find    outputs (Home  work)
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
#output
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
'''
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1() # all four inputs doesnt have enough ref
#p , q , r , s , m = f1() #error due to extra ref on left side
'''
'''
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))
print(g * 3)
print(g[0])
print(g[1 : 3])
print(*g) #------>1 2 3
#outputs remaining will get error due to generator isnt had len,index,* repeatation
'''
























































