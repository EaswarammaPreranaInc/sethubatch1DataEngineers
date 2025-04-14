# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5))
print(square())
'''
25
100'''

# Find  output (Home  work)
add  = lambda x=10,y=10 : x+y
# How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add))
print(add(10 , 20))
print(add(10.6 , 20.8))
print(add('Hyder' , 'abad'))
print(add(True , False))
print(add(25 , 10.8))
print(add(3 + 4j , 5 + 6j))
# print(add(10 , '20'))
print(add())
print(add)

#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))
print(add())
'''
30
3'''

#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )
print((lambda  x , y : x + y) (10.8 , 20.6))
print((lambda  x , y : x + y) ('Hyder' , 'abad'))
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))
'''
30
31.400000000000002
Hyderabad
<function <lambda> at 0x000002F1E78D1440>'''

#  Find  outputs (Home  work)
# How  to  define  lambda  to  detrmine  largest  of  two  arguments
large = lambda x,y:max(x,y)
print(large(10  ,  20))
print(large(10.7  ,  5.6))
print(large('g'  ,  's'))
print(large('Rama'  ,  'Rajesh'))
print(large(True  ,  False))
'''
20
10.7
s
Rama
True'''

#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))
print(power(4.5 , 4))
print(power())
print(power(9))
'''
8
410.0625
12.25
81'''

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
Hyd
<function <lambda> at 0x000001FCFA321440>'''

# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()
'''
Sec
Cyb
Hyd'''

# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
'''
Sec
Cyb
Hyd
None'''


# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
'''
Sec
Cyb
Hyd'''

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))
print(a)
# for  x  in  a:
# 	print(x) # error
# a() #error tuple is not callable

print(a[0]())
'''
Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x0000026626F61440>, None, None)
Hyd
None'''

#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)
'''
<function <lambda> at 0x00000194396C1440>
<function <lambda> at 0x00000194396C1440>
Hyd
None
Hyd'''

# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))
print(adder2(200))
print(adder1(300 , 400))
'''
105
210
700'''

#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))
'''
25
125
625'''

#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	    x()
# a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')] # def cannot be inside the list
# print(a)
# a = [f1() , f2()]
print(a)
'''
Hyd
Sec
[<function f1 at 0x00000241E6481440>, <function f2 at 0x00000241E6693BA0>]'''


# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])
print(a[key](5))
'''
<function <lambda> at 0x000002B814993BA0>
125'''

# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1)) #<class 'function'>
print(type(lamb)) #<class 'function'>
print(lamb(2)) #9
print(lamb(5)) #243
print(lamb) #<function f1.<locals>.<lambda> at 0x0000027B34863BA0>
print(lamb()) # no value for n


# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))
print(lam(2.5))
print(lam(4))
'''
25
33.75
69'''

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))
print(add(30)(40))
'''
30
70'''

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
print(e) #[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f) #[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) #[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1])) # error


# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) #[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a)) # error

# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))
print(max(a , key = lambda  x  :  x[1] ))
print(max(a , key = lambda  x  :  x[2] ))
print(max(a))
'''
(25, 'Kiran', 1500.0)
(15, 'Vamsi', 2000.0)
(20, 'Sita', 2800.0)
(25, 'Kiran', 1500.0)'''

# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) # False
add = lambda  x = 25 :   x == 35
print(add()) # False
# add = lambda  x  :   x = 25 # error
add = lambda  x  :   x := 25 # error

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
# f2()
'''
f1    function
f2  function
False
f1    function
True
f1    function
None'''

# Find  outputs (Home  work)
# How  to  assign  ref  'p'  to  print()  function
p = print
# How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
p("Hyderabad")
print = None
# How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
p("Hello")
'''
Hyderabad
Hello'''

# Find   outputs (Home  work)
# How  to  assign  ref  'x'  to  id()  function
x = id
# How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
print(x(25))
# How  to  assign  ref  'p'  to  len()  function
p = len
# How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
print(p("Hyd"))

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
'''
Begin
Outer  function
Hello
Inner  function
Back  to  outer  function
Hi
Other  function
Bye'''

# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) #60

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
'''
Begin
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
'''
30
10
Bye'''

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
20
10'''

# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer() #10

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
'''
10
20
15
Bye'''

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
'''
outputs:
10
15
20
25
'''

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		# print(x) # error
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
'''
10
20
25'''

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
'''
10
20
15
25'''

# Find  outputs(Home  work)
def  outer():
	def  inner():
		# nonlocal  x #error
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	# print(x) #error
# End  of  the  function
outer()
# print(x)#error
'''
20'''

# Find  outputs(Home  work)
def  outer():
	def  inner():
		# global   x # error
		x = 20
		print(x)
		x = x + 5
	# End  of  inner  function
	inner()
	# print(x)#error
# End  of  the  function
outer()
# print(x)#error
'''
20'''

#  Identify  Error
def   f1():
        # nonlocal   x#error no outer function to call

        # Find  outputs (Home  work)
        def outer():
            a = 10
            b = 20

            def inner():
                nonlocal a
                a = 100
                b = 200
                print(a, b)

            # End  of  inner  function
            print(a, b)
            inner()
            print(a, b)

        # end of outer function
outer()
'''
10 20
100 200
100 20'''

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
     x =  x +  20
     print(x)
    #end of inner function
    gun()
#end of outer function
fun()# error value for x is not defined non local can be used in this

#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x
'''
name 'x' is nonlocal and global'''


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
