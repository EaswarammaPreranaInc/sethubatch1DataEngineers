#1 Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5))
print(square())

Output:
25
100

#2 Find  output (Home  work) How  to  define  lambda  function   to  return  sum   of  two  arguments
add=lambda x,y:x+y
print(type(add))
print(add(10 , 20))
print(add(10.6 , 20.8))
print(add('Hyder' , 'abad'))
print(add(True , False))
print(add(25 , 10.8))
print(add(3 + 4j , 5 + 6j))
#print(add(10 , '20'))
#print(add())
#print(add)

Output:
<class 'function'>
30
31.4
Hyderabad
1
35.8
(8+10j)

#3 Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))
print(add())

Output:
30
3

#4 Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )
print((lambda  x , y : x + y) (10.8 , 20.6))
print((lambda  x , y : x + y) ('Hyder' , 'abad'))
#print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))

Output:
30
31.400000000000002
Hyderabad

#5 Find  outputs (Home  work) How  to  define  lambda  to  detrmine  largest  of  two  arguments
large =lambda a,b: max(a,b)
print(large(10  ,  20))
print(large(10.7  ,  5.6))
print(large('g'  ,  's'))
print(large('Rama'  ,  'Rajesh'))
print(large(True  ,  False))

Output:
20
10.7
s
Rama
True

#6 Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))
print(power(4.5 , 4))
print(power())
print(power(9))

Output:
8
410.0625
12.25
81

#7 Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))
print(x)
p , q , r , s = all(9 , 2)
print(p)
print(q)
print(r)
print(s)

Output:
<class 'tuple'>
(17, 3, 70, 1.4285714285714286)
11
7
18
4.5

#8  Find  outputs
a  =  lambda  :  'Hyd'
print(a())
print(a)

Output:
Hyd
<function <lambda> at 0x0000021ECA8C3E20>

#9 Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()

Output:
Sec
Cyb
Hyd

#10 Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

Output:
Sec
Cyb
Hyd
None

#11 Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())

Output:
Sec
Cyb
Hyd

#12 Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
#a() 
print(a[0]())

Output:
Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x000001F12EAD3E20>, None, None)
<function <lambda> at 0x000001F12EAD3E20>
None
None
Hyd
None

#13 Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)
<function <lambda> at 0x00000291F07A3E20>
<function <lambda> at 0x00000291F07A3E20>

Output:
Hyd
None
Hyd

#14 Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))
print(adder2(200))
print(adder1(300 , 400))

105
210
700

#15 Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))

Output:
10
15
625

#16 Find  outputs
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

Output:
Hyd
Sec
[<function f1 at 0x00000239BBE63E20>, <function f2 at 0x00000239BBF8A290>]
Hyd
Sec
[None, None]

#17 Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])
print(a[key](5))

Output:
<function <lambda> at 0x0000016E5123A3B0>
125

#18 Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))
print(type(lamb))
print(lamb(2))
print(lamb(5))
print(lamb)
#print(lamb())

Output:
<class 'function'>
<class 'function'>
9
243
<function f1.<locals>.<lambda> at 0x000002529321A290>

#19 Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))
print(lam(2.5))
print(lam(4))

Output:
25
33.75
69

#20 Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))
print(add(30)(40))

Output:
30
70

#21 Find  outputs
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
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)
#print(sorted(a , key = x[1]))

Output:
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]

[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]

[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]

#22 Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)
#print(sorted(a))

Output:
[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]

#23 Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))
print(max(a , key = lambda  x  :  x[1] ))
print(max(a , key = lambda  x  :  x[2] ))
print(max(a))

Output:
(25, 'Kiran', 1500.0)
(15, 'Vamsi', 2000.0)
(20, 'Sita', 2800.0)
(25, 'Kiran', 1500.0)

#24 Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))
add = lambda  x = 25 :   x == 35
print(add())
#add = lambda  x  :   x = 25
#1add = lambda  x  :   x := 25

Output:
False
False

#25 Find  outputs  (Home  work)
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
#f2()

Output:
f1    function
f2  function
False
f1    function
True
f1    function
None

#26 How  to  assign  ref  'p'  to  print()  function, How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
# print = None , print('Hello'), How  to  call  print()  function  thru  ref  'p'  and   print  'Hello
p=print
p('Hyderabad')
print=None
p('Hello')

Output:
Hyderabad
Hello

#27 How  to  assign  ref  'x'  to  id()  function, # How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
# How  to  assign  ref  'p'  to  len()  function, How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
x=id
print(x(25))
p=len
print(p('Hyd'))

Output:
2482761892848
3

#28 Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner():
		print('Inner  function')
	# End  of  inner  function
	print('Hello')
	inner()
	print('Back  to  outer  function')
def  other():
#	inner()
	print('Other  function')
# End  of  the  function
print('Begin')
outer()
print('Hi')
#inner()
other()
print('Bye')

Output:
Begin
Outer  function
Hello
Inner  function
Back  to  outer  function
Hi
Other  function
Bye

#29 Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))

Output:
60

#30 Find  outputs (Home  work)
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

Output:
Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye

#31 Find  outputs  (Home  work)
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


Output:
30
10
Bye

#32 Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()

Output:
20
10

#33 Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()

Output:
10

#34 Find  outputs  (Home  work)
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

Output:
10
20
15
Bye

#35  Find  outputs  (Home  work)
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
#print(x)

Output:
10
15
20
25

#36 Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
#		print(x)
#		nonlocal  x
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

Output:
10
20
15

#37 Find   outputs(Home  work)
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

Output:
10
20
15
25

#38 Find  outputs(Home  work)
def  outer():
	def  inner():
#		nonlocal  x
		x = 20
		print(x)
	# End  of  inner  function
	inner()
#	print(x)
# End  of  the  function
outer()
#print(x)

Output:
20

#39 Find  outputs(Home  work)
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

Output:
20
25
25

#40 Identify  Error
def   f1():
	pass
#       nonlocal   x

#41 Find  outputs (Home  work)
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

Output:
10 20
100 200
100 20

#42 Find  outputs (Home  work)
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

Output:
Hello

#43 Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
#		x =  x +  20
		print(x)
	#end of inner function
	gun()
#end of outer function
fun()

10

#44 Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
#		global   x
		nonlocal  x

#45 Find  outputs  (Home   work)
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

Output:
10