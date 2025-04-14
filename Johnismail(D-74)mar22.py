# Find  outputs (Home  work)
'''square = lambda  x = 10  :   x * x
print(square(5))#25
print(square())#100

# Find  output (Home  work)
#How  to  define  lambda  function   to  return  sum   of  two  arguments
add=lambda x,y:x+y
print(type(add))#<class 'Function'>
print(add(10 , 20))#30
print(add(10.6 , 20.8))#31.4
print(add('Hyder' , 'abad'))#'Hyderabad'
print(add(True , False))#1
print(add(25 , 10.8))#35.8
print(add(3 + 4j , 5 + 6j))#8+10j
#print(add(10 , '20'))#error
#print(add())#error
print(add)#Type and adress


#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))#30
print(add())#3

#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )#30
print((lambda  x , y : x + y) (10.8 , 20.6))#31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad'))#Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))#Type and adress

#  Find  outputs (Home  work)
#How  to  define  lambda  to  detrmine  largest  of  two  arguments
large=lambda x,y:max(x,y)
print(large(10  ,  20))#20
print(large(10.7  ,  5.6))#10.7
print(large('g'  ,  's'))#s
print(large('Rama'  ,  'Rajesh'))#Rama
print(large(True  ,  False))#True

#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))#8
print(power(4.5 , 4))#410.0625
print(power())#12.25
print(power(9))#81

# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))#<class tuple>
print(x)#(17,3,70,1.4)
p , q , r , s = all(9 , 2)
print(p)#11
print(q)#7
print(r)#18
print(s)#4.5

#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())#
print(a)#Type and adress

# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()#sec cyb hyd

# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())#sec cyb Hyd None

# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())#sec cyb hyd

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')#sec cyb
print(type(a)) #<class 'Tuple'>
print(a) #(type and adress,None,None )
for  x  in  a:
	print(x)#<type and adress, None,None)
#a() #error
print(a[0]())#Hyd none

#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))#Type and adress
print(lambda  x  :  print(x) (s))#Type and adress
print((lambda  x  :  print(x)) (s))#hyd none
(lambda  x  :  print(x)) (s)#Hyd

# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))#105
print(adder2(200))#210
print(adder1(300 , 400))#700

#Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:#[lambda   x  :  x * 2] -->10
					#[lambda   x  :  x * 3]-->15
					#[lambda   x  :  x ** 4]-->625
        print(fun(5))
	
#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a)
a = [f1() , f2()]
print(a)
outputs----
Hyd
Sec
[<function f1 at 0x00000251A8183E20>, <function f2 at 0x00000251A82A2CB0>]
Hyd
Sec
[None, None]

# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])#Type and adress
print(a[key](5))#125

# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))#<class 'function'>
print(type(lamb))#<class 'function'>
print(lamb(2))#9
print(lamb(5))#243
print(lamb)#Type and adress
#print(lamb())#error

# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))#12+13=25
print(lam(2.5))#33.75
print(lam(4))#48+21=69

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))#30
print(add(30)(40))#70

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
e = sorted(a , key =  lambda   x  :  x[2])
print(e)
print()#[(15, 'Rajesh', 500.0),(10, 'Rama', 1000.0),(5, 'Amar', 1300.0),(20, 'Sita', 2000.0),(18, 'Kiran', 2800.0)]
f = sorted(a , key = lambda   x  :  x[0])
print(f)
print()#[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)#[(20, 'Sita', 2000.0),(10, 'Rama', 1000.0),(15, 'Rajesh', 500.0),(18, 'Kiran', 2800.0),(5, 'Amar', 1300.0) ]
print()
#print(sorted(a , key = x[1]))#error

# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)#[{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
#{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008},
#{'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013}]
print(sorted(a))#'<' not supported between instances of 'dict' and 'dict'

# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))#(25 , 'Kiran' , 1500.0) 
print(max(a , key = lambda  x  :  x[1] ))# (15 , 'Vamsi' , 2000.0) 
print(max(a , key = lambda  x  :  x[2] ))# (20 , 'Sita' , 2800.0)
print(max(a))##(25 , 'Kiran' , 1500.0) 

# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))#False
add = lambda  x = 25 :   x == 35
print(add())#False
add = lambda  x  :   x = 25 # cant assign value to lambda
add = lambda  x  :   x := 25 # cant assign value to lambda

#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')#'f1    function'
def    f2():
        print('f2  function')#'f2  function'
# End  of  the  function
f1()
f2()
print(f1  is  f2)#False
f2 = f1
f2()#'f1  function'
print(f1  is  f2)#True
f2 = f1()
print(f2)#'f1    function'
#f2()

# Find  outputs (Home  work)
#How  to  assign  ref  'p'  to  print()  function
p=print
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
p('Hyderabad')
print = None
p=None
print('Hello')
p('Hello')
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello

# Find   outputs (Home  work)
#How  to  assign  ref  'x'  to  id()  function
x=id(25)

#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
print(x)
#How  to  assign  ref  'p'  to  len()  function
p=len('Hyd')
#How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
print(p)

#  Find  outputs (Home  work)
def  outer():
	print('Outer  function')#'Outer  function'
	def  inner():
		print('Inner  function')#'Inner  function'
	# End  of  inner  function
	print('Hello')
	inner()
	print('Back  to  outer  function')#'Back  to  outer  function'
def  other():
	inner()
	print('Other  function')#'Other  function'
# End  of  the  function
print('Begin')#Begin
outer()
print('Hi')#hi
#inner()
#other()
print('Bye')#bye

# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))#60'''
'''
# Find  outputs (Home  work)
def  outer():
	print('Outer  function')#'Outer  function'<next line> 'Hi' '1st  inner  function' '2nd  inner  function'
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
print('Begin')#Begin
outer()#
print('Bye')

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

outputs---
30
10
Bye

# Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x)#20
		print(globals()['x'])#10
	inner()
#outer()#20

# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)#10
	inner()
outer()

# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)#20
		x +=  7 #27
	# End  of  inner  function
	print(x)#10
	x += 5 #15
	inner()
	print(x)#15
# End  of  the  function
outer()
print('Bye')

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)#10
		x = 20
		print(x)#15
		x += 5 #20
	# End  of  inner  function
	print(x)#20
	x += 5 #25
	inner()
	print(x)#15
# End  of  outer  function
outer()
#print(x)

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)#10
		nonlocal  x
		x = 20
		print(x)#10
		x += 5 #15
	# End  of  inner  function
	print(x)#20
	x += 5
	inner()
	print(x) #25
# End  of  outer  function
outer()

#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)#10
		x += 5 #15
	# End  of  inner  function
	print(x)#20
	x += 5
	inner()
	print(x)#25
# End  of  outer  function
outer()
print(x)

# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x
		x = 20
		print(x)#20
	# End  of  inner  function
	inner()
	print(x)#20
# End  of  the  function
outer()
print(x)

#  Identify  Error
def   f1():
        nonlocal   x # no binding for nonlocal 'x' found
		# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)#10 20
	# End  of  inner  function
	print(a , b)#100 200
	inner()
	print(a , b)#100 20
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
print(f1())#Hello

# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20
		print(x)
	#end of inner function
	gun()
#end of outer function
fun()#10

# Find  output(Home  work)
x = 10
def   outer():
	x = 20
	def  inner():
		#global   x
		nonlocal  x'''
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
f1()#10
