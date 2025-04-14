
Q1 #Find outputs
square=lambda x = 10: x*x
print(square(5))  #25
print(square())   #100
-----------------------------------------------------------------------------------------
Q2 #Find Outputs
add=lambda x,y: x+y #How to define lambda function to return sum of two arguments 
print(type(add)) #<class 'function'>
print(add(10,20)) #30
print(add(10.6,20.8)) # 31.4
print(add('Hyder','abad')) #Hyderabad
print(add(True,False))    #1
print(add(25,10.8))       #35.8
print(add(3+4j,5+6j))      #(8+10j)
#print(add(10,'20'))      #error  - cannot add int and str
#print(add())            #error - arguments are not given
print(add)             #<function <lambda> at 0x00000253C0B38040>
--------------------------------------------------------------------------------------------
Q3 #Find outputs
add= lambda a=1,b=2:a+b
print(add(10,20)) #30
print(add())     #3
---------------------------------------------------------------------------------------------
Q4 #Find Outputs
print((lambda x,y:x+y)(10,20)) #30
print((lambda x,y:x+y)(10.8,20.6)) #31.400000000000002
print((lambda x,y:x+y)('Hyder','abad')) #Hyderabad
print(lambda x,y:x+y('Hyder','abad')) #<function <lambda> at 0x00000214F0D61440>
-----------------------------------------------------------------------------------------------
Q5 #Find Outputs
large= lambda x,y : max(x,y) #How to define lambda to determine largest of two argumnets
print(large(10,20)) #20
print(large(10.7,5.6)) #10.7
print(large('g','s'))  #s
print(large('Rama','Rajesh')) #Rajesh
print(large(True,False))   #True
------------------------------------------------------------------------------------------------
Q6 #Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) #8
print(power(4.5 , 4)) #410.0625
print(power())  #12.25
print(power(9)) #81
-----------------------------------------------------------------------------------------------------
Q7 # Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))  #<class 'function'>
print(x)        #(17,3,70,1.4285714285714286)
p , q , r , s = all(9 , 2)
print(p)     #11
print(q)     #7
print(r)     #18
print(s)     #4.5
------------------------------------------------------------------------------------------
Q8 # Find  outputs
a  =  lambda  :  'Hyd'
print(a())  #Hyd
print(a)    #<function <lambda> at 0x00000186179B1440>
-------------------------------------------------------------------------------------
Q9 #Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()   # Sec <\n> Cyb <\n>  Hyd
-------------------------------------------------------------------------------------------
Q10	#Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())  # Sec <\n> Cyb <\n> Hyd <\n> None
-----------------------------------------------------------------------------------------
Q11 #Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())  #Sec <\n> Cyb <\n>  Hyd
-------------------------------------------------------------------------------------------
Q12 # Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))  # Sec <\n> Cyb <\n>  <class 'tuple'>
print(a)        # (<function <lambda> at 0x000001F980EB1440>, None, None)
for  x  in  a:
	print(x)    #<function <lambda> at 0x000001F980EB1440>  <\n>  None <\n> None
#a()            #error  - 'a' is tuple not function
print(a[0]())  #Hyd <\n> None
-----------------------------------------------------------------------------------------------
Q13	# Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) #<function <lambda> at 0x0000020D4CF11440> 
print(lambda  x  :  print(x) (s)) #<function <lambda> at 0x0000020D4CF11440>
print((lambda  x  :  print(x)) (s)) #Hyd <\n> None
(lambda  x  :  print(x)) (s)       #Hyd
------------------------------------------------------------------------------------------------
Q14 # Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) #105
print(adder2(200)) #210
print(adder1(300 , 400)) #700
---------------------------------------------------------------------------------------------------------------
Q15 #Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5)) #10 <\n> 15 <\n> 625
---------------------------------------------------------------------------------------------------------------------
Q16 #Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()    #Hyd <\n>  Sec
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]  #error - function should not be defined in list
print(a)        #[<function f1 at 0x000001F721DC1440>, <function f2 at 0x000001F721FD3D80>]
a = [f1() , f2()]  #Hyd <\n> Sec
print(a)     #[None,None]
--------------------------------------------------------------------------------------------------------------------------
Q17 # Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])  # <function <lambda> at 0x000001AAA3543D80>
print(a[key](5)) #125
----------------------------------------------------------------------------------------------------------------------
Q18 # Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))  #<class 'function'>
print(type(lamb)) #<class 'function'>
print(lamb(2))   #9
print(lamb(5))    #243
print(lamb)        #<function f1.<locals>.<lambda> at 0x0000017FCDD03D80>
#print(lamb())    # error - 'n' value is missing
------------------------------------------------------------------------------------------------------------
Q19 # Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) # 12+8+5 = 25
print(lam(2.5)) #33.75
print(lam(4))   #48+16+5 = 69
----------------------------------------------------------------------------------------------------------------
Q20 #Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()    
print(a(20))  #30
print(add(30)(40)) #70
--------------------------------------------------------------------------------------------------------------------------------------------------------
Q21 # Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))   #  Nested  tuple
b = sorted(a)    # Sorts   tuple  'a'  based  on  1st  element  of  each  inner  tuple
print(b)          # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
c = sorted(a , reverse = True)  #  Sorts  tuple  'a'  in descendig  order  of   1st  element  of  inner  tuples
print(c)  #  [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])  # Sorts   tuple  'a'  based  on   2nd  element  of  each  inner  tuple  due  to  x[1]
print(d)  # [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)  #[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)  #[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)  #[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
#print(sorted(a , key = x[1]))  #error - there is no variable x
------------------------------------------------------------------------------------------------------------------------------------------------------------
Q22 # Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)         #[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a)) #  #error - dict should be sorted based on keys or values
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Q23 # Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))  #(25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] ))  #(15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] ))  #(20, 'Sita', 2800.0)
print(max(a))                              #(25, 'Kiran', 1500.0)
---------------------------------------------------------------------------------------------------------------------------------------------
Q24 # Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) #False
add = lambda  x = 25 :   x == 35
print(add())   #False
#add = lambda  x  :   x = 25  #assignment is not allowed inside lambda
#add = lambda  x  :   x := 25 #assignment is not allowed inside lambda
------------------------------------------------------------------------------------------------------------------------
Q25 # Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()  #f1 function
f2()  #f2 function
print(f1  is  f2) #False
f2 = f1 
f2()  #f1 function
print(f1  is  f2) #True
f2 = f1()  #f1 function
print(f2) # None
f2()  #error - f2 is Nonetype object but not not function
---------------------------------------------------------------------------------------------------------------------------------
Q26 # Find  outputs (Home  work)
p=print #How  to  assign  ref  'p'  to  print()  function
p('Hyd') #How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
#print('Hello') #error- None  is assigned to print. Nonetype object is not callable
p('Hello') #How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'
-------------------------------------------------------------------------------------------------------------------------------
Q27 # Find   outputs (Home  work)
x=id #How  to  assign  ref  'x'  to  id()  function
print(x(25))  #140713345877672   #How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p=len  #How  to  assign  ref  'p'  to  len()  function
print(p('Hyd')) #3  #How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
------------------------------------------------------------------------------------------------------------------------------
Q28 # Find  outputs (Home  work)
def  outer():
	print('Outer  function')       
	def  inner():
		print('Inner  function')
	# End  of  inner  function
	print('Hello')
	inner()
	print('Back  to  outer  function')
def  other():
	#inner() #error - inner() function is not defined in other()
	print('Other  function')
--------------------------------------------------------------------------------------------------------------------------------
Q29 # End  of  the  function
print('Begin')  
outer()
print('Hi')
#inner() #error - inner() function is only for outer()
other()
print('Bye')

OP-
Begin
Outer function
Hello
Inner function
Back to outer function
Hi
other function 
Bye
----------------------------------------------------------------------------------------------------------------
Q30 # Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) # 60
-----------------------------------------------------------
Q31 # Find  outputs (Home  work)
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

OP-
Begin
Outer function
Hi
2nd inner function
Hello
1st inner function
Back to outer function
Bye
------------------------------------------------------------------------
Q32 # Find  outputs  (Home  work)
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

OP-
30
10
Bye
------------------------------------------------------------------------
Q33 # Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()

OP-
20
10
--------------------------------------------------------------------------
Q34 # Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)     #10
	inner()
outer()
-------------------------------------------------------------------------
Q35 # Find  outputs  (Home  work)
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

OP-
10
20
15
Bye
--------------------------------------------------------------------
Q36 # Find  outputs  (Home  work)
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
#print(x) # error - no  variable x outside the function

OP-
10
15
20
25
------------------------------------------------------------------------------------
Q37 # Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x) #error - x does not have value in inner()
		#nonlocal  x   #error - declaring x as nonlocal after using it
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

OP-
10
20
15
---------------------------------------------------------------------------------
Q38 # Find   outputs(Home  work)
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

OP-
10
20
15
25
------------------------------------------------------------------------------------
Q39 # Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x  #error- x is not defined in outer()
		x = 20
		print(x)   #20
	# End  of  inner  function
	inner()
	#print(x)  #error- x is not defined in outer
# End  of  the  function
outer()
#print(x)  #error - x is not defined globally
-------------------------------------------------------------------------------
Q40 # Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)   #20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)  #25
# End  of  the  function
outer()
print(x)  #25
-----------------------------------------------------------------------------------------------
Q41 # Identify  Error
def   f1():
        nonlocal   x  # error - x is not defined and nonlocal must be in nested function 
---------------------------------------------------------------------------------------------
Q42 # Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)  #100 200
	# End  of  inner  function
	print(a , b)  #10 20
	inner()
	print(a , b)  #10 20
#end of outer function
outer()
------------------------------------------------------------------------------
Q43 # Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1())    #Hello
----------------------------------------------------------------------------------------------
Q44 # Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20   #error- x has no value in nested function
		print(x)      
	#end of inner function
	gun()
#end of outer function
fun()
-------------------------------------------------------------------------------------------
Q45 # Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		#global   x   #error - x cannot be global and nonlocal in the same function
		nonlocal  x  
--------------------------------------------------------------------------------------------
Q46 # Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)       #10
		f3()
	f2()
f1()
