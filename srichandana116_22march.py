# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) #25
print(square()) #100
# Find  output (Home  work)
#How  to  define  lambda  function   to  return  sum   of  two  arguments
add=lambda x,y: x+y
print(type(add)) #<class 'function'>
print(add(10 , 20)) #30
print(add(10.6 , 20.8)) #31.4
print(add('Hyder' , 'abad')) #Hyderabad
print(add(True , False)) #1
print(add(25 , 10.8)) #35.8
print(add(3 + 4j , 5 + 6j)) #(8+10j)
#print(add(10 , '20')) #error int & str can't be added
#print(add()) #args are must
print(add) #<function <lambda> at 0x136518220>
#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) #30
print(add()) #3
#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) #30 
print((lambda  x , y : x + y) (10.8 , 20.6)) #31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) #Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) #<function <lambda> at 0x136518220>
#  Find  outputs (Home  work)
#How  to  define  lambda  to  detrmine  largest  of  two  arguments
large=lambda x,y:max(x,y)
print(large(10  ,  20)) #20
print(large(10.7  ,  5.6))#10.7
print(large('g'  ,  's'))#s
print(large('Rama'  ,  'Rajesh'))#rama
print(large(True  ,  False))#true
#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) #8
print(power(4.5 , 4)) #410.06
print(power()) #12.25
print(power(9)) #81
# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))  #<class 'tuple'>
print(x) #(17, 3, 70, 1.4285714285714286)
p , q , r , s = all(9 , 2)
print(p) #11
print(q)#7
print(r) #18
print(s) #4.5
#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) #Hyd
print(a) #<function <lambda> at 0x13651afc0>
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()
'''Sec
Cyb
Hyd'''
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
'''Sec
Cyb
Hyd
None'''
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
#a() 
print(a[0]())
'''Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x104848180>, None, None)
<function <lambda> at 0x104848180>
None
None
Hyd
None'''
#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)
'''<function <lambda> at 0x12ea9ef20>
<function <lambda> at 0x12ea9ef20>
Hyd
None
Hyd'''
# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) #105
print(adder2(200)) #210
print(adder1(300 , 400)) #700
#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))
'''25
125
625'''
#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
b = [f1 , f2]
for  x  in  b:
	     x()
a = [lambda  f11:  print('Hyd') ,  lambda f22:  print('Sec')]
print(a,b)
a = [f1() , f2()]
print(a)
'''Hyd
Sec
[<function <lambda> at 0x12ea9efc0>, <function <lambda> at 0x12eaf3600>] [<function f1 at 0x12eaf3ba0>, <function f2 at 0x12eaf3d80>]
Hyd
Sec
[None, None]'''
# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) #<function <lambda> at 0x12eaf3b00>
print(a[key](5)) #125
# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))#<class 'function'>
print(type(lamb))#<class 'function'>
print(lamb(2))#9
print(lamb(5))#243
print(lamb) #<function f1.<locals>.<lambda> at 0x162a109a0>
print(lamb(1)) #3
# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) #25
print(lam(2.5))#33.75
print(lam(4)) #69
#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) #30
print(add(30)(40)) #70
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
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g,'\n')
print(sorted(a))
'''[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)] 
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]'''
# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)
print(sorted (a, key = lambda  x  :  x['Model']))
'''[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
[{'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}, {'Make': 'Tesla', 'Model': 'X', 'Year': 1999}]'''
# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))
print(max(a , key = lambda  x  :  x[1] ))
print(max(a , key = lambda  x  :  x[2] ))
print(max(a))
'''(25, 'Kiran', 1500.0)
(15, 'Vamsi', 2000.0)
(20, 'Sita', 2800.0)
(25, 'Kiran', 1500.0)'''
# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) #False
add = lambda  x = 25 :   x == 35
print(add()) #False
#add = lambda  x  :   x = 25
#add = lambda  x  :   x := 25
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
'''f1    function
f2  function
False
f1    function
True
f1    function
None'''
# Find   outputs (Home  work)
#How  to  assign  ref  'x'  to  id()  function
x=id
s=[0,5,6]
print(x(s))
p=len
print(p('Juda'))
#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
#How  to  assign  ref  'p'  to  len()  function
#How  to  ca
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
#inner()
#other()
print('Bye')
'''Begin
Outer  function
Hello
Inner  function
Back  to  outer  function
Hi
Bye'''
# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))#60
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
'''Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye'''
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
'''30
10
Bye'''
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
'''10
20
15
Bye'''
