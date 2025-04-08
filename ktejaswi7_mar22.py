program1:
# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # 25
print(square()) # 100

program2:
# Find  output (Home  work)
add=lambda x=5 , y=10 : x + y
print(type(add))   #  <class 'function'>
print(add(10 , 20))  # 30
print(add(10.6 , 20.8)) # 31.4
print(add('Hyder' , 'abad')) #  Hyderabad
print(add(True , False)) # 1
print(add(25 , 10.8))  # 35.8
print(add(3 + 4j , 5 + 6j)) # (8+10j)
#print(add(10 , '20')) # error
print(add()) # 15
print(add)  #  <function <lambda> at 0x0000021E81131440>

program3:
#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 30
print(add()) # 3

program4:
#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )  #  30
print((lambda  x , y : x + y) (10.8 , 20.6))  # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad'))  # Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) # <function <lambda> at 0x000001B1A9381440>


program5:
#  Find  outputs (Home  work)
large = lambda x , y : max(x,y)  
print(large(10  ,  20))  # 20
print(large(10.7  ,  5.6)) # 10.7
print(large('g'  ,  's')) # s
print(large('Rama'  ,  'Rajesh')) # rama
print(large(True  ,  False)) # True

program6:
#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))  #  8
print(power(4.5 , 4))  #  410.0625
print(power())  # 12.25
print(power(9)) # 81

program7:
# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)  # create the tuple with four elements i.e (17, 3, 70, 1.4285714285714286)
print(type(x))  # <class 'tuple'>
print(x)  #  (17, 3, 70, 1.4285714285714286)
p , q , r , s = all(9 , 2)  #  create the tuple with four elements i.e (11, 7, 18, 4.5)
print(p) # 11
print(q) # 7
print(r) # 18
print(s)  # 4.5

program8:
#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())  # Hyd
print(a) #  <function <lambda> at 0x000001722F321440>

program9:
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a() 

#outputs:
	Sec
	Cyb
	Hyd


program10:
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

#outputs:
	Sec
	Cyb
	Hyd
	NOne
	
program11:
# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
a()

#outputs:
	Sec
	Cyb
	Hyd

	
program12:
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))  # 
print(a) 
for  x  in  a:
	print(x)
#a()  # error 'tuple' object is not callable
print(a[0]())

outputs:
	Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x000001C389971440>, None, None)
<function <lambda> at 0x000001C389971440>
None
None
Hyd
None

program13:
#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) # <function <lambda> at 0x000001C96D488400>
print(lambda  x  :  print(x) (s)) # <function <lambda> at 0x000001C96D488400>
print((lambda  x  :  print(x)) (s)) # Hyd <nextline> none
(lambda  x  :  print(x)) (s) # Hyd

program14:
# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x   : x + y
x = 10
adder2 = lambda  y , y = y : x + y
x = 20
print(adder1(100))  # 105
print(adder2(200)) # 210
print(adder1(300 , 400)) # 700

program15:
#Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))
#outputs:
	10
	15
	625

program16:
#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]  # invalid 
print(a)
a = [f1() , f2()]
print(a)

#outputs:
Hyd
Sec
[<function f1 at 0x000001CD05031440>, <function f2 at 0x000001CD05248400>]
Hyd
Sec
[None, None]

program17:
# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) #  <function <lambda> at 0x0000023241F68400>
print(a[key](5)) # 125

program18:
# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3) 
print(type(f1)) # <class 'function'>
print(type(lamb)) # <class 'function'>
print(lamb(2)) # 9
print(lamb(5)) # 243
print(lamb) # <function f1.<locals>.<lambda> at 0x0000018A8D258400>
print(lamb()) # error

program19:
# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) # 25
print(lam(2.5)) # 33.75
print(lam(4)) # 69

program20:
#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) # 30
print(add(30)(40)) # 70

program21:
# Find  outputs
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
e = sorted(a , key =  lambda   x  :  x[2]) # Sorts   tuple  'a'  based  on   3rd  element  of  each  inner  tuple  due  to  x[2]
print(e) #   [(15 ,'Rajesh' , 500.0), (10 , 'Rama' , 1000.0), (5 , 'Amar' , 1300.0), (20 , 'Sita' , 2000.0), (18 , 'Kiran' , 2800.0)]
print()  
f = sorted(a , key = lambda   x  :  x[0])  # Sorts   tuple  'a'  based  on   1st  element  of  each  inner  tuple  due  to  x[0]
print(f) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True) # #  Sorts  tuple  'a'  in descendig  order  of   2nd  element  of  inner  tuples
print(g) #  [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1])) # error


program22:
# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year']) # sorted of list based on year
print(b) #  [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a)) # error not supported for dict

program23:
# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))  # (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] ))  # (15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] ))  # (20, 'Sita', 2800.0)
print(max(a))  # (25, 'Kiran', 1500.0)


program24:
#Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) 
add = lambda  x = 25 :   x == 35
print(add()) # 35
#add = lambda  x  :   x = 25
#add = lambda  x  :   x := 25
output:
False
False

program25:
#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1() # f1    function
f2() # f2  function
print(f1  is  f2) # False
f2 = f1 
f2() # f1    function
print(f1  is  f2) # True
f2 = f1() 
print(f2)  # f1 function
f2() #error


program26:
# Find  outputs (Home  work)
p= lambda : 'Hyderabad' #How  to  assign  ref  'p'  to  print()  function
print(p()) #How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
#print = None
p=print
p('Hello')
#print(p) #How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
output:
Hyderabad
Hello


program27:
# Find   outputs (Home  work)
x= lambda  : id(25)  #How  to  assign  ref  'x'  to  id()  function
print(x()) #How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p= lambda : len('Hyd') #How  to  assign  ref  'p'  to  len()  function
print(p()) #How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
output:
140727983736488
3


program28:
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
	#inner()
	print('Other  function')
# End  of  the  function
print('Begin') # Begin
outer() # Out function <nextline> Hello <nextline> Inner Function <nextline> Back to outer functionm
print('Hi') # Hi
#inner() # error 
other() # Other function
print('Bye') # Bye

program29:
# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) # 60

program30:
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
print('Begin') # Begin
outer() # Outer function <nextline> Hi <nextline> 2nd  inner  function <nextline>  hello <nextline> 1st  inner  function <nextline> Back to uter function
print('Bye') # Bye

program31:
# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer() # 30 <nextline> 10
print('Bye') # Bye

program32:
# Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer() # 20 <nextline> 10



program33:
# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer() # 10



program34:
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
outer() # 10 <nextline> 20 <nextline> 15
print('Bye') # Bye

program35:
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
outer() # 10 <nextline> 15 <nextline> 20 <nextline> 25
print(x) # error x is not defied 

program36:
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)
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
outer() # 10 <nextline> 20 <nextline> 25


program37:
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
outer() # 10 <nextline>  20  <nextline> 15
print(x) # 25

program38:
# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	#print(x)
# End  of  the  function
#outer() # 20 <nextline> 20
#print(x) # 20

program39:
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
outer() # 20 <nextline> 25
print(x) #25

program40:
#  Identify  Error
def   f1():
        nonlocal   x # error no nonlocal in outer function

program41:
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
outer() #  10 20 <nextline>  100 200 <nextline> 100 20

program42:
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
print(f1()) #  Hello  

program43:
# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20
		print(x)
	#end of inner function
	gun()
#end of outer function
fun() # 10

program44:
#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x  
		#nonlocal  x 

program45:
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
f1()  #  10
