# 1. Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # 25
print(square()) #100 
# 2.  Find  output (Home  work)
add = lambda x,y:x+y
#How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add)) #  class function 
print(add(10 , 20)) # 30 
print(add(10.6 , 20.8)) # 31.4
print(add('Hyder' , 'abad')) # Hyderabad
print(add(True , False)) # 1
print(add(25 , 10.8)) # 35.8
print(add(3 + 4j , 5 + 6j)) #8+10j
#print(add(10 , '20')) #error
#print(add()) #error 
print(add) #<function <lambda> at 0x0000012302B18180> 


#  3. Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 30
print(add()) #3 

#  4. Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) #  30
print((lambda  x , y : x + y) (10.8 , 20.6)) # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) #Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) # <function <lambda> at 0x000002B1F30F1440>

# 5. Find  outputs (Home  work) 
large=lambda x,y: x if x >y else y #lambda x,y:max(x,y)

# How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20))  
print(large(10.7  ,  5.6))
print(large('g'  ,  's'))
print(large('Rama'  ,  'Rajesh'))
print(large(True  ,  False)) 

# 6. Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) # 8
print(power(4.5 , 4)) # 410.0625
print(power()) # 12.25
print(power(9)) # 81

# 7. Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7) # 
print(type(x)) #class tuple 
print(x) # (17,3,70,1.4285)
p , q , r , s = all(9 , 2)
print(p) #11
print(q) # 7
print(r) #18
print(s) # 4.5 

# 8.  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) #   Hyd
print(a) #<function <lambda> at 0x00000265DCE81440> 

# 9. Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a() 
'''Sec
Hyd
Cyb '''

# 10. Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) 
'''Sec
Cyb
Hyd 
None '''

# 11. Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) 
'''
Sec
Cyb
hyd
 '''
 # 12. Find  outputs   (Home  work) 
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))  # class tuple 
print(a) #Sec nl Cyb nl Hyd
for  x  in  a:
	print(x) #Type and address Sec Cyb
#a() #error 
print(a[0]()) #Hyd
'''outputs:
Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x00000229F2601440>, None, None)
<function <lambda> at 0x00000229F2601440>
None
None
Hyd
None '''
#  13. Find  outputs  (Home  work)
s = 'Hyd'
'''print(lambda  s  :  print(s))  # this means printing lambda function 
print(lambda  x  :  print(x) (s)) # type and address'''
print((lambda  x  :  print(x)) (s)) # it is immediately lambda function   (s) is the argument of lambda function so the results are hyd <next line > None 
(lambda  x  :  print(x)) (s) # it is immediately lambda function so, it prints Hyd 

# 14. Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y # x stores the current value of x which is 5
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) # 105
print(adder2(200)) #210
print(adder1(300 , 400)) #700

# 15.Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a: # 
        print(fun(5)) #25 nl 125 nl 625 
#  16. Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x() #hyd Sec
# a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')] invalid syntax 
print(a) # type and address
a = [f1() , f2()] # Hyd Sec
print(a) # [None,None]

# 17.Find output  (Home  work) 
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # type and address
print(a[key](5)) #125

# 18.Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3) 
print(type(f1)) #class function 
print(type(lamb)) #class function 
print(lamb(2)) # 9
print(lamb(5)) # 3^5 --> 243 
print(lamb) #<function f1.<locals>.<lambda> at 0x000002A7AC79EFC0>
#print(lamb()) # need argument error  

# 19.Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5) 
print(lam(2)) # 25
print(lam(2.5)) # 33.75
print(lam(4)) # 69

# 20. Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add() 
print(a(20)) # 30
print(add(30)(40)) # 70  

# 21. Find  outputs
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
e = sorted(a , key =  lambda   x  :  x[2]) # sorts tuple a based on 3 rd element of inner tuple 
print(e) # [(15 ,'Rajesh' ,500.0), (10 , 'Rama' , 1000.0), (5 , 'Amar' , 1300.0), (20 , 'Sita' , 2000.0),  (18 , 'Kiran' , 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0]) #  Sorts   tuple  'a'  based  on   1st element  of  each  inner  tuple  due  to  x[0]
print(f) # [(5 , 'Amar' , 1300.0), (10 , 'Rama' , 1000.0) , (15 ,'Rajesh' , 500.0) ,(18 , 'Kiran' , 2800.0) ,(20 , 'Sita' , 2000.0)
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True) #  Sorts   tuple  'a'  based  in decending order on   2nd  element  of  each  inner  tuple  due  to  x[1]
print(g) # [(20, 'Sita', 2000.0),(10, 'Rama', 1000.0),(15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)
# print(sorted(a , key = x[1]))  error x is not defined 


# 22.Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) #[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
#print(sorted(a)) <  not supported b/w dict and dict 

# 23. Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) # (25 , 'Kiran' , 1500.0) 
print(max(a , key = lambda  x  :  x[1] )) #(20 , 'Sita' , 2800.0)
print(max(a , key = lambda  x  :  x[2] )) # (20 , 'Sita' , 2800.0)
print(max(a)) # (25 , 'Kiran' , 1500.0)

# 24. Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))  # False
add = lambda  x = 25 :   x == 35
print(add()) # False
#add = lambda  x  :   x = 25 #cannot assign to lambda  here 25 is assigned to x which is not possible bcz lambda raises error 
#add = lambda  x  :   x := 25 # error 2 nd : invalid syntax 

# 25. Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1() #f1    function
f2() #f2    function
print(f1  is  f2) # False 
f2 = f1 # alias 
f2() # f1 Function 
print(f1  is  f2) # True 
f2 = f1() 
print(f2) #f1 function next line None 
#f2() # 'NoneType' object is not callable 

# 26. Find  outputs (Home  work)
'''How  to  assign  ref  'p'  to  print()  function
How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')
How  to  call  print()  function  thru  ref  'p'  and   print  'Hello' '''
p=print
p('Hyderabad')
print = None
#print('Hello') # error none is not a function to call 
print=p
p('Hello')

# 27. Find   outputs (Home  work)
'''How  to  assign  ref  'x'  to  id()  function
How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
How  to  assign  ref  'p'  to  len()  function
How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd'
'''
x=id
print(x(25))
p=len
print(p('Hyd'))

# 28. Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner():
		print('Inner  function')
	# End  of  inner  function
	print('Hello')
	inner() 
	print('Back  to  outer  function')
def  other():
	inner() # here inner is called but not defined we need to define inner like def inner: 
	print('Other  function')
# End  of  the  function
print('Begin') # Begin 
outer() # 'Outer  function' next line Hello  next line  'Inner function next line Back to outer function 
print('Hi') # Hi 
#inner() # error 
#other()  # NameError: name 'inner' is not defined. Did you mean: 'iter'?
print('Bye') # bye 
# 29.Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) #60

# 30. Find  outputs (Home  work) 
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
outer() 
''' Outer Function
Hi
2nd inner function 
Hello 
!st inner function 
Back to outer function 
'''
print('Bye')  # Bye 

# 31. Find  outputs  (Home  work) 
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer() # 30 next line 10
print('Bye') # bye 

# 32.  Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer() # 20 10 
# 33.Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer() # 10
# 34. Find  outputs  (Home  work)
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
outer() # 10 20 15
print('Bye') #bye 

# *35. Find  outputs  (Home  work) 
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x) # no error 
		x = 20
		print(x) 
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer() # 10  15 20 25
#print(x)  # error 

# 36*. Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)
		#nonlocal  x # name 'x' is used prior to nonlocal declaration
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
15 '''

# 37*  Find   outputs(Home  work)
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
outer() #10 15 20
print(x) #20

# 38. Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x # to have a nonlocal x we need to have a local x  no binding for nonlocal 'x' found
		x = 20 
		print(x)
	# End  of  inner  function
	inner() 
	#print(x)
# End  of  the  function
outer() #20 
#print(x)  # error 

# 39. Find  outputs(Home  work)
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
outer() #20 25
print(x) #25 

#  40. Identify  Error
def   f1():
	pass
       # nonlocal   x # cant use non local here it can be local 
# 41. Find  outputs (Home  work)
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
'''
#10 20  
100 200
100 20'''

# 42. Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1()) #Hello

# 43*. Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20 UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
		print(x)
	#end of inner function
	gun()
#end of outer function
fun() # 10
# 44. Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		#global   x #name 'x' is nonlocal and global
		nonlocal  x
# 45. Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)
		f3()
	f2()
f1() #10
