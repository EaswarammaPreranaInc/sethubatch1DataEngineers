'''
1#) Find  outputs (Home  work)

square = lambda  x = 10  :   x * x
print(square(5)) # 25
print(square()) # 100 here default value taken 'x' value

#2)Find  output (Home  work)
add = lambda x,y, :x+y #How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add)) # <class 'function'>
print(add(10 , 20)) # 30
print(add(10.6 , 20.8)) # 31.4
print(add('Hyder' , 'abad')) # Hyderabad
print(add(True , False)) # 1
print(add(25 , 10.8)) # 35.8
print(add(3 + 4j , 5 + 6j)) # (8+10j)
#print(add(10 , '20')) # Error due to '20'
print(add()) # Error due to no arguments
print(add) # <class 'function'> <function <lambda> at 0x000001E1B4591440>

#3) Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 30
print(add())# 3 here it will takes default values

#4) Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) # 30
print((lambda  x , y : x + y) (10.8 , 20.6)) # 31.400000000000002
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) # <function <lambda> at 0x0000025004EB1440> , it treats as a type and address of lambda

#5)Find  outputs (Home  work)
large = lambda x,y :max(x,y) # lambda x,y : x if x>y else y #How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20)) # 20
print(large(10.7  ,  5.6)) # 10.7
print(large('g'  ,  's')) # s
print(large('Rama'  ,  'Rajesh')) # rama
print(large(True  ,  False)) # True

(or)
Find  outputs (Home  work)

large = lambda x,y : x if x>y else y #How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20))
print(large(10.7  ,  5.6))
print(large('g'  ,  's'))
print(large('Rama'  ,  'Rajesh'))
print(large(True  ,  False))

#6)Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) # 8
print(power(4.5 , 4)) # 410.0625
print(power()) # 12.25
print(power(9)) # 81

#7)Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x)) # <class 'tuple'>
print(x) # (17, 3, 70, 1.4285714285714286) 
p , q , r , s = all(9 , 2)
print(p) # 11
print(q) # 7 
print(r) # 18
print(s) # 4.5

#8)Find  outputs
a  =  lambda  :  'Hyd'
print(a()) # Hyd 
print(a) # <function <lambda> at 0x000001D875231440>

#9) Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a() # statement 2 and statement3 are consider as outside of the function so it will prints first and than we are calling lambda functions.

outputs:
-------
Sec
Cyb
Hyd

#10)Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # print function returns None so we get None

output:
-------
Sec
Cyb
Hyd
None 

#11) Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
output:
----------
Sec
Cyb
Hyd

#12)Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # <function <lambda> at 0x0000023B052E1440>
print(a) # None <nextline> None
for  x  in  a:
	print(x) # Sec <next line> Cyb
a() # Error due to empty Tuple
print(a[0]()) # <class 'tuple'>
               # (<function <lambda> at 0x0000023B052E1440>, None, None)

#13)Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) # <function <lambda> at 0x0000023D19211440>
print(lambda  x  :  print(x) (s)) # <function <lambda> at 0x0000023D19211440> 
print((lambda  x  :  print(x)) (s)) # Hyd <next line> None
(lambda  x  :  print(x)) (s)  # Hyd

check once
-------------
#14)Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) # 105
print(adder2(200)) # 210
print(adder1(300 , 400)) #700

#15)Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))

output:
-------
10 ---1st iteration
15 ---2nd iteration
625 ---3rd  iteration


#16) Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')] # Error due to 'def' is defined 
print(a)
a = [f1() , f2()]
print(a)

outputs:
---------
Hyd
Sec
[<function f1 at 0x000001A966841440>, <function f2 at 0x000001A966A2F060>]
Hyd
Sec
[None, None]

#17)Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # <function <lambda> at 0x00000273217AF060>
print(a[key](5)) # 125


#18)Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1)) # < class 'function'>
print(type(lamb)) # < class 'function'>
print(lamb(2)) # here x=3 and n=2 ---- 3 **2 =9
print(lamb(5)) # here x=3 and n=5 ---- 3 **5 =243
print(lamb) # <function f1.<locals>.<lambda> at 0x0000016EC715F060>
print(lamb()) # Error due to 'n' value not there


#19) Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c # (**=power), (*= multiplication) (f(x)=3x^2+4x+5)
lam  = eval(3 , 4 , 5)
print(lam(2)) # 25
print(lam(2.5)) # 33.75
print(lam(4)) # 69

#20)Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y 
a = add()
print(a(20)) # (10+20 = 30)
print(add(30)(40)) # ( 30+40 = 70)


#21) Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))   #  Nested  tuple
b = sorted(a)  # Sorts   tuple  'a'  based  on  1st  element  of  each  inner  tuple
print(b)  # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
c = sorted(a , reverse = True)  #  Sorts  tuple  'a'  in descendig  order  of   1st  element  of  inner  tuples
print(c)  #  [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])  # Sorts   tuple  'a'  based  on   2nd  element  of  each  inner  tuple  due  to  x[1]
print(d)  # [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e) # [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) # [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1])) # Error due to 'x'


#22) Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) # [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a)) # Error duen to we cannot compare dict to dict.


#23)Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) # (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] )) # (15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) # (20, 'Sita', 2800.0)
print(max(a)) # (25, 'Kiran', 1500.0)

#24)Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) # False
add = lambda  x = 25 :   x == 35
print(add()) # False
add = lambda  x  :   x = 25 # Error  due to syntax Error
add = lambda  x  :   x := 25 # Error due to syntax Error

#26)Find  outputs  (Home  work)
def    f1():
        print('f1    function') # f1    function
def    f2():
        print('f2  function') # f2    function
# End  of  the  function
f1()
f2()
print(f1  is  f2) # False-----Both are functions they are not same
f2 = f1
f2() # f1    function
print(f1  is  f2) # True
f2 = f1() # f1    function
print(f2) # None
f2() # Error due to 'NoneType' object is not callable


#27)Find  outputs (Home  work)
p = print # How  to  assign  ref  'p'  to  print()  function
p ( 'Hyderabad') # How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
p ('Hello') # How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'


#28) Find   outputs (Home  work)
x = id(25) # How  to  assign  ref  'x'  to  id()  function
print(x) # 140704876463784----- How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p = len('Hyd') # How  to  assign  ref  'p'  to  len()  function
print(p) # 3--- How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd

(or)

x = id                 
print(x(25))           
p = len                
print(p('Hyd'))   

#29)Find  outputs (Home  work)
def  outer():
	print('Outer  function') # Outer  function
	def  inner():
		print('Inner  function') # Inner  function
	# End  of  inner  function
	print('Hello') # Hello
	inner()
	print('Back  to  outer  function') # Back  to  outer  function
def  other():
	#inner()
	print('Other  function') # Other  function
# End  of  the  function
print('Begin') # Begin
outer() # calling outer function()
print('Hi') # Hi
#inner() # inner function() calling 
other() # other function () calling
print('Bye') # Bye

#30)Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a # (10 + 20 + 30 = 60)
# End  of  f1  function
print(f1(30)) # 60

#31)Find  outputs (Home  work)
def  outer():
	print('Outer  function') # Outer  function
	def  inner1():
		print( '1st  inner  function') # 1st  inner  function
	def  inner2():
		print('2nd  inner  function') # 2nd  inner  function
	print('Hi') # Hi
	inner2()
	print('Hello') # Hello
	inner1()
	print('Back  to  outer  function') # Back  to  outer  function
# End of the function
print('Begin') # Begin
outer() # outer function() calling
print('Bye') # Bye

#32)Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x) # 30
		print(globals()['x']) # 10 -------inner () requesting 'x' as a GV ie., x=10
	inner() # inner () calling
outer() # outer () calling
print('Bye') #  Bye

#33) Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x) # 20
		print(globals()['x']) # 10
	inner()
outer()

#34)Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x) # 10
	inner()
outer()

#35) Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x) # 20
		x +=  7
	# End  of  inner  function
	print(x) # 10
	x += 5 # 'x' is incremented by 5
	inner()
	print(x) #15
# End  of  the  function
outer() # outer () calling
print('Bye') # Bye
output:
-------
10
20
15
Bye

#36)Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x) # 25
		x = 20
		print(x) # 20
		x += 5
	# End  of  inner  function
	print(x) # 10
	x += 5
	inner()
	print(x) # 15
# End  of  outer  function
outer() # outer ()Calling
print(x) #10 

#37) Find  outputs  (Home  work)
def  outer():
	x = 10
	#def  inner():
		#print(x)
		#nonlocal  x # Error
		#x = 20
		#print(x)
		#x += 5
	# End  of  inner  function
	print(x) # 10
	x += 5
	#inner()
	print(x) # 15
# End  of  outer  function
outer()

outputs:-
--------
10
15

#38)Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x) # 20
		x += 5
	# End  of  inner  function
	print(x) # 10
	x += 5
	inner() 
	print(x) # 15
# End  of  outer  function
outer() # outer () calling
print(x) # 25

#39)Find  outputs(Home  work)
def  outer():
	#def  inner():
		#nonlocal  x Error 
		#x = 20
		#print(x)
	# End  of  inner  function
	#inner()
	#print(x)
# End  of  the  function
#outer()
#print(x)

#40) Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20 # 20
		print(x)
		x = x + 5 # 'x' is incremented by 5
	# End  of  inner  function
	inner()
	print(x) # 25
# End  of  the  function
outer() # outer () calling
print(x) # 25

#41)Identify  Error
def   f1():
        nonlocal   x  # Error due to nonlocal 'x'

#42)Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b) # 100 200
	# End  of  inner  function
	print(a , b) # 10 20
	inner()
	print(a , b) # 100 20
#end of outer function
outer()

#43)Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1()) # Hello

#44) Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20
		print(x) # 10
	#end of inner function
	gun()
#end of outer function
fun()

#45) Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		#global   x # Error due to global  'x'
		#nonlocal  x # Error due to nonlocal 'x'
'''
#46)Find  outputs  (Home   work)
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