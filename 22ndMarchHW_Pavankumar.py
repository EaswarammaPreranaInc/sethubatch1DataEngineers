'''
PROGRAM_1:
'''
# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5))
print(square())
'''
OUTPUT:
25
100
'''
# Find  output (Home  work)
#How  to  define  lambda  function   to  return  sum   of  two  arguments
add= lambda x,y: x+y
print(type(add))
print(add(10 , 20))
print(add(10.6 , 20.8))
print(add('Hyder' , 'abad'))
print(add(True , False))
print(add(25 , 10.8))
print(add(3 + 4j , 5 + 6j))
#print(add(10 , '20')) --->unsupported operand type(s) for +: 'int' and 'str'
#print(add()) ---><lambda>() missing 2 required positional arguments: 'x' and 'y'
print(add)
'''
OUTPUT:
25
100
<class 'function'>
30
31.4
Hyderabad
1
35.8
(8+10j)
<function <lambda> at 0x0000019662D93F60>
'''
#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))
print(add())
'''
OUTPUT:
30
3
'''
#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )
print((lambda  x , y : x + y) (10.8 , 20.6))
print((lambda  x , y : x + y) ('Hyder','abad'))
print(lambda  x , y : x + y  ('Hyder','abad'))
'''
OUTPUT:
30
31.400000000000002
Hyderabad
<function <lambda> at 0x00000230769299E0>
'''
#  Find  outputs (Home  work)
#How  to  define  lambda  to  detrmine  largest  of  two  arguments
large= lambda a,b : a if a>b else b
print(large(10  ,  20))
print(large(10.7  ,  5.6))
print(large('g'  ,  's'))
print(large('Rama'  ,  'Rajesh'))
print(large(True,False))
'''
OUTPUT:
20
10.7
s
Rama
True
'''
#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))
print(power(4.5 , 4))
print(power())
print(power(9))
'''
OUTPUT:
8
410.0625
12.25
81
'''
# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))
print(x)
p , q , r , s = all(9 , 2)
print(p)
print(q)
print(r)
print(s)
'''
OUTPUT:
<class 'tuple'>
(17, 3, 70, 1.4285714285714286)
11
7
18
4.5
'''
#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())
print(a)
'''
OUTPUT:
Hyd
<function <lambda> at 0x00000215AD279D00>
'''
# Find  outputs
a  =  lambda  :  print('Hyd'); print('Sec') ; print('Cyb')
a()
'''
OUTPUT:
Sec
Cyb
Hyd
'''
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
'''
OUTPUT:
Sec
Cyb
Hyd
None
'''
# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
'''
OUTPUT:
Sec
Cyb
Hyd
'''
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
#a() --->there is no function name as a to call the function 
print(a[0]())
'''
OUTPUT:
Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x000002E80B739D00>, None, None)
<function <lambda> at 0x000002E80B739D00>
None
None
Hyd
None
'''
#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
#(lambda x : print(x)) (s)
'''
<function <lambda> at 0x00000199FC529DA0>
<function <lambda> at 0x00000199FC529DA0>
Hyd
None
'''
# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))
print(adder2(200))
print(adder1(300,400))
'''
OUTPUT:
105
210
700
'''
#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
	print(fun(5))
'''
OUTPUT:
25
125
625
'''
#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
#a = [def f1(): print('Hyd'),def f2(): print('Sec')]
print(a)
a = [f1(),f2()]
print(a)
'''
Hyd
Sec
[<function f1 at 0x000001AD4C101440>, <function f2 at 0x000001AD4C373F60>]
Hyd
Sec
[None, None]
'''
# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])
print(a[key](5))
'''
OUTPUT:
<function <lambda> at 0x00000212BCC93F60>
125
'''
# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))
print(type(lamb))
print(lamb(2))
print(lamb(5))
print(lamb)
#print(lamb()) --->f1.<locals>.<lambda>() missing 1 required positional argument: 'n'
'''
OUTPUT:
<class 'function'>
<class 'function'>
9
243
<function f1.<locals>.<lambda> at 0x000002AB4C3F3F60>
'''
# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))
print(lam(2.5))
print(lam(4))
'''
OUTPUT:
25
33.75
69
'''
#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))
print(add(30)(40))
'''
OUTPUT:
30
70
'''
# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))  
b = sorted(a)  
print(b) 
print()
c = sorted(a , reverse = True) 
print(c) 
print()
d = sorted(a ,  key =  lambda   x  :  x[1]) 
print(d)  
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)
#print(sorted(a , key = x[1]))
'''
OUTPUT:
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]

[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]

[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
'''
# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)
#print(sorted(a))
'''
OUTPUT:
[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
'''
# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))
print(max(a , key = lambda  x  :  x[1] ))
print(max(a , key = lambda  x  :  x[2] ))
print(max(a))
'''
OUTPUT:
(25, 'Kiran', 1500.0)
(15, 'Vamsi', 2000.0)
(20, 'Sita', 2800.0)
(25, 'Kiran', 1500.0)
'''
# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))
add = lambda  x = 25 :   x == 35
print(add())
#add = lambda  x  :   x = 25 --->assignment operators are accepted as arguments for lambda
#add = lambda  x  :   x := 25
'''
OUTPUT:
False
False
'''
#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
f1()
f2()
print(f1  is  f2)
f2 = f1
f2()
print(f1  is  f2)
f2 = f1()
print(f2)
#f2()--> 'NoneType' object is not callable
'''
OUTPUT:
f1    function
f1  function
False
f2 function
True
f1   function
None
'''
# Find  outputs (Home  work)
'''
How  to  assign  ref  'p'  to  print()  function
How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
'''
p=print
p()
print(p())
p('Hyd')
p('Hello')
'''
OUTPUT:
-nothing prints
-nothing prints
None
Hyd
Hello
'''
# Find   outputs (Home  work)
'''How  to  assign  ref  'x'  to  id()  function
How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
How  to  assign  ref  'p'  to  len()  function
How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd'''
x=id
print(x(25))
p=len
print(p('Hyd'))
'''
140714682082984
3
'''
#  Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner():
		print('Inner  function')
	print('Hello')
	inner()
	print('Back  to  outer  function')
def  other():
	#inner()
	print('Other  function')
print('Begin')
outer()
print('Hi')
#inner() --->error due to name 'inner' is defined in other function 
other()
print('Bye')
'''
Begin
Outer function
Hello
Inner function
Back  to  outer  function
Hi
Other function
Bye
'''
# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	return  f2() + 20 +  a
print(f1(30))
'''
OUTPUT:
60
'''
# Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner1():
		print( '1st  inner  function')
	def  inner2():
		print('2nd  inner  function')
	print('Hi')
	inner2()
	print('Hello')
	inner1()
	print('Back  to  outer  function')
print('Begin')
outer()
print('Bye')
'''
OUTPUT:
Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye
'''
# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer()
print('Bye')
'''
OUTPUT:
30
10
Bye
'''
# Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()
'''
OUTPUT:
20
10
'''
# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()
'''
OUTPUT:
10
'''
# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)
		x +=  7
	print(x)
	x += 5
	inner()
	print(x)
outer()
print('Bye')
'''
OUTPUT:
10
20
15
bye
'''
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)
		x = 20
		print(x)
		x += 5
	print(x)
	x += 5
	inner()
	print(x)
outer()
#print(x) --->there is no global variable named as x
'''
OUTPUT:
10
15
20
25
'''
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)
		nonlocal x
		x = 20
		print(x)
		x += 5
	print(x)
	x += 5
	inner()
	print(x)
outer()
'''
OUTPUT:
10
20
25
'''
#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)
		x += 5
	print(x)
	x += 5
	inner()
	print(x)
outer()
print(x)
'''
OUTPUT:
10
20
15
25
'''
# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x --->There is no local variable x for outer function
		x = 20
		print(x)
	inner()
	#print(x) --->There is no local variable x
outer()
#print(x) --->There is no global variable x
'''
OUTPUT:
20
'''
# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)
		x = x + 5
	inner()
	print(x)
outer()
print(x)
'''
OUTPUT:
20
25
25
'''
#  Identify  Error
#def   f1():
        #nonlocal   x --->there is no inner function for f1 funtion.
# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)
	print(a , b)
	inner()
	print(a , b)
outer()
'''
OUTPUT:
10 20
100 200
100 20
'''
# Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	f2()
	return  x
print(f1())
'''
OUTPUT:
Hello
'''
# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20 --->cannot access local variable 'x' where it is not associated with a value
		print(x)
	gun()
fun()
'''
OUTPUT:
10
'''
#  Identify  Error
#x = 10
#def   outer():
	#x = 20
	#def  inner():
		#global   x --->cannot create global variable x while treating 
		#nonlocal  x
#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)
		f3()
	f2()
f1()
'''
OUTPUT:
10
'''
