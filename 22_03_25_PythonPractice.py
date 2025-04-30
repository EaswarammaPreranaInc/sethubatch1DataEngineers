# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # 25 
print(square()) # 100 it takes default value 10 to x
# Find  output (Home  work)
add = lambda x,y : x+y #How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add)) # <class 'function'>
print(add(10 , 20)) # 30 x value 10 y value 20 
print(add(10.6 , 20.8)) # 31.4
print(add('Hyder' , 'abad')) # Hyderabad
print(add(True , False)) # 1
print(add(25 , 10.8)) # 35.8
print(add(3 + 4j , 5 + 6j)) # 8+10j
#(add(10 , '20')) # Error becoz str and int 
#print(add()) # Error: <lambda>() missing 2 required positional arguments: 'x' and 'y'
print(add) # Type and address of function
#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 30
print(add()) # 3
#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) # 30
print((lambda  x , y : x + y) (10.8 , 20.6)) # 31.400000000000002
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) # Type and address of function
#  Find  outputs (Home  work)
large = lambda x,y : x if x>y else y #How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20)) # 20
print(large(10.7  ,  5.6)) # 10.7
print(large('g'  ,  's')) # g
print(large('Rama'  ,  'Rajesh')) # Rama
print(large(True  ,  False)) # True
#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) # 8
print(power(4.5 , 4)) # 410.0625
print(power()) # 12.25
print(power(9)) # 81
# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x)) # <class 'tuple'>
print(x) # (17,3,70,1.42)
p , q , r , s = all(9 , 2)
print(p) # 11
print(q) # 9
print(r) # 18
print(s) # 4.5
#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) # Hyd
print(a) # Type and Address of function
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a() # Sec <nl> Cyb <nl> Hyd
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # Sec <nl> Cyb <nl> Hyd <nl> None
# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # Sec <nl> Cyb <nl> Hyd
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # <class 'tuple'>
print(a) # Type and Address of function None ,None
for  x  in  a:
	print(x) # Type and Address of function <nl> None <nl> None
#a() # Error: 'tuple' object is not callable
print(a[0]()) # Hyd <nl> None
#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) # Type and address of Lambda
print(lambda  x  :  print(x) (s)) # Type and address of Lambda
print((lambda  x  :  print(x)) (s)) # Hyd <nl> None
(lambda  x  :  print(x)) (s) # Hyd
# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) # 105
print(adder2(200)) # 210
print(adder1(300 , 400)) # 700
#Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5)) # 10  <next line> 15 <next line> 625
#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
#print(a)
a = [f1() , f2()]
print(a)
'''o/p: Hyd
		Sec
		Hyd
		Sec
		[None, None]'''
# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # Type and address of lambda function
print(a[key](5)) # 125
# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3) 
print(type(f1)) # <class 'function'>
print(type(lamb)) # <class 'function'>
print(lamb(2)) # 9
print(lamb(5)) # 243
print(lamb) # <function f1.<locals>.<lambda> at 0x0000014EE79482C0>
#print(lamb()) # Error: f1.<locals>.<lambda>() missing 1 required positional argument: 'n'
# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) # 25
print(lam(2.5)) # 33.75
print(lam(4)) # 69
#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) # 30
print(add(30)(40)) # 70
# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))   #  Nested  tuple
b = sorted(a)  # Sorts   tuple  'a'  based  on  1st  element  of  each  inner  tuple
print(b)  # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
c = sorted(a , reverse = True)  #  Sorts  tuple  'a'  in descendig  order  of   1st  element  of  inner  tuples
print(c)  #  [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])  # Sorts   tuple  'a'  based  on   2nd  element  of  each  inner  tuple  due  to  x[1]
print(d)  #[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) # [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
#print(sorted(a)) # Error: '<' not supported between instances of 'dict' and 'dict'
# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) # (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] )) # (15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) # (20, 'Sita', 2800.0)
print(max(a)) # (25, 'Kiran', 1500.0)
# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) # False
add = lambda  x = 25 :   x == 35
print(add()) # False
#add = lambda  x  :   x = 25 # Error: cannot assign to lambda
#add = lambda  x  :   x := 25 # Error: cannot assign to lambda
#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()
f2()
print(f1  is  f2)
f2 = f1
f2()
print(f1  is  f2)
f2 = f1()
print(f2)
#f2() # Error: 'NoneType' object is not callable
'''o/p: f1    function
		f2  function
		False
		f1    function
		True
		f1    function
		None'''
# Find  outputs (Home  work)
p = print#How  to  assign  ref  'p'  to  print()  function
p('Hyderabad')#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
#print('Hello') # Error NoneType object is not callable
p('Hello')#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
# Find   outputs (Home  work)
x = id #How  to  assign  ref  'x'  to  id()  function
#print(x(25)) #How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p = len #How  to  assign  ref  'p'  to  len()  function
#print(p('Hyd'))#How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
#print(f1(30)) #Error: 'NoneType' object is not callable
'''# Find  outputs (Home  work)
 p = print #How  to  assign  ref  'p'  to  print()  function
 p('Hyderabad') #How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
# Find   outputs (Home  work)
How  to  assign  ref  'x'  to  id()  function
How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
How  to  assign  ref  'p'  to  len()  function
How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
#  Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner():
		print('Inner  function')
	# End  of  inner  function
	print('Hello')
	inner()
	print('Back  to  outer  function')
def  other():
	inner()
	print('Other  function')
# End  of  the  function
print('Begin')
outer()
print('Hi')
inner()
other()
print('Bye')
'''# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
#print(f1(30)) # Error: 'NoneType' object is not callable
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
# End of the function
#print('Begin') # Error: 'NoneType' object is not callable
#outer() # Error: 'NoneType' object is not callable
#print('Bye') # Error: 'NoneType' object is not callable
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
'''# Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()
# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()
# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)
		x +=  7
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  the  function
outer()
print('Bye')
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
print(x)
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)
		nonlocal  x
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
print(x)
# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)
# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)
#  Identify  Error
def   f1():
        nonlocal   x
# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)
	# End  of  inner  function
	print(a , b)
	inner()
	print(a , b)
#end of outer function
outer()
# Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1())
# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x)
	#end of inner function
	gun()
#end of outer function
fun()
#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x
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
f1()'''