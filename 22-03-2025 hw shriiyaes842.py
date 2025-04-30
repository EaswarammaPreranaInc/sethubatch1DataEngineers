#1
# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5))#25
print(square())#100

#2
# Find  output (Home  work)
add = lambda  x ,y  :   x + y
print(type(add))#<class 'function'>
print(add(10 , 20))#30
print(add(10.6 , 20.8))#31.4
print(add('Hyder' , 'abad'))#Hyderabad
print(add(True , False))#1
print(add(25 , 10.8))#35.8
print(add(3 + 4j , 5 + 6j))#(8+10j)
#print(add(10 , '20'))
#print(add())#error,arguments are misssing
print(add)

#3
#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))#30
print(add())#3

#4
#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )#30
print((lambda  x , y : x + y) (10.8 , 20.6))#31.400000000000002
print((lambda  x , y : x + y) ('Hyder' , 'abad'))#Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))#address of the lamada

#5
#  Find  outputs (Home  work)
large = lambda  a,b :   max(a,b)
print(large(10  ,  20))#20
print(large(10.7  ,  5.6))#10.7
print(large('g'  ,  's'))#S
print(large('Rama'  ,  'Rajesh'))#Rama
print(large(True  ,  False))#True

#6#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))#8
print(power(4.5 , 4))#410.0625
print(power())#12.25
print(power(9))#81

#7
# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))#<class 'tuple'>
print(x)#(17, 3, 70, 1.4285714285714286)
p , q , r , s = all(9 , 2)
print(p)#11
print(q)#7
print(r)#18
print(s)#4.5

#8
#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())#Hyd
print(a)#address of a


#9
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()

"""
Sec
Cyb
Hyd
"""

#10
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

'''
Sec
Cyb
Hyd
None
'''


#11
# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())

"""
Sec
Cyb
Hyd
"""

#12
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))
print(a)
for  x  in  a:
	print(x)
#a()
print(a[0]())

#13
#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))#address of function
print(lambda  x  :  print(x) (s))#address of function
print((lambda  x  :  print(x)) (s))#Hyd,None
(lambda  x  :  print(x)) (s)#Hyd

#14
# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))#105
print(adder2(200))#210
print(adder1(300 , 400))#700

#15
#Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))

"""
10
15
625
"""

#16
#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()

#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]error
print(a)
a = [f1() , f2()]
print(a)

#17
# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])#address of the function
print(a[key](5))#125

#18
# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))#<class 'function'>
print(type(lamb))#<class 'function'>
print(lamb(2))
print(lamb(5))
print(lamb)#address
#print(lamb())#error

#19
# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))#25
print(lam(2.5))#33.75
print(lam(4))#69

#20
#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))#30
print(add(30)(40))#70

#21
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
e = sorted(a , key =  lambda   x  :  x[2])# Sorts   tuple  'a'  based  on   3rd  element  of  each  inner  tuple  due  to  x[2]
print(e)#[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])#
print(f)#[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)#[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1]))#error

#22
# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)#[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
#print(sorted(a))#error not supported# b/w dict

#23
# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))#(25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] ))#(15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] ))#(20, 'Sita', 2800.0)
print(max(a))#(25, 'Kiran', 1500.0)

#24
# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))
add = lambda  x = 25 :   x == 35
print(add())
#add = lambda  x  :   x = 25#error
#add = lambda  x  :   x := 25#invalid sysmtax

#25
#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()#f1    function
f2()#f2    function
print(f1  is  f2)#false
f2 = f1
f2()#f1    function
print(f1  is  f2)#true
f2 = f1()
print(f2)#f1    function,None
#f2()error

#26
'''# Find  outputs (Home  work)
How  to  assign  ref  'p'  to  print()  function
How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
'''
p=print
p("Hyderabad")
print('Hello')
p("hello")

#27
'''
# Find   outputs (Home  work)
How  to  assign  ref  'x'  to  id()  function
How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
How  to  assign  ref  'p'  to  len()  function
How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
'''

x=id
print(x(25))#address of x
p=len
print(p("hyd"))#3

#28
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
print('Begin')
outer()
print('Hi')
#inner()
other()
print('Bye')

"""
Begin
Outer  function
Hello
Inner  function
Back  to  outer  function
Hi
Other  function
Bye
"""

#29
# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))#60

#30
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
print('Begin')
outer()
print('Bye')

"""
Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye
"""

#31
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

"""
30
10
Bye
"""

#32
# Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()


"""
20
10
"""

#33
# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()

#10

#34
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

"""
10
20
15
Bye
"""


#35
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
#print(x)# is not define

"""
10
15
20
25

"""

#36
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
outer()
#error

#37
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

#38
# Find  outputs(Home  work)
def  outer():
    x=10
	def  inner():
		nonlocal  x # x not decleared
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)


#39
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

"""
20
25
25
"""

#40
#  Identify  Error
def f1():
    nonlocal x#x not found

#41
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

"""
10,20
100.200
100,20
"""

#42
# Find  outputs (Home  work)
def   f1():
	k = 'John'
	def  f2():
		nonlocal k
		k =  'Hello'
	#end of inner function
	f2()
	return  k
#  End  of  f1()  function
print(f1())


#43
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

"""
error
"""

#44
#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x


"""
x is non local and global

"""

#45
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

"""
10
"""
