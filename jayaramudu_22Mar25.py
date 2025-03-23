#Ex-1
# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # x is 5 return 25
print(square()) # by default x is 10 and return 100

#Ex-2
# Find  output (Home  work)
add = lambda  x, y: x+y  #How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add)) # cass function
print(add(10 , 20)) # 30
print(add(10.6 , 20.8)) #31.4
print(add('Hyder' , 'abad')) # concat both str Hyderabad
print(add(True , False)) # 0 + 1 = 1
print(add(25 , 10.8)) # 35.8
print(add(3 + 4j , 5 + 6j))  # 3 + 4j + 5 + 6j = 8+10j
#print(add(10 , '20')) # Error because str and int can not perform sum
#print(add()) # Error because does not pass parameters
print(add) # type and address of lambda function

#Ex-3
#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 10 + 20 30
print(add()) # 1 + 2

#Ex-4
#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) # 10 + 20 = 30
print((lambda  x , y : x + y) (10.8 , 20.6))  # 10.8 + 20.6 =31.400000000000002
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # Hyderabad
print(lambda  x , y : x + y  ('Hyder','abad')) # only define function but on call type and address of lambda function

#Ex-5
#  Find  outputs (Home  work)
large = lambda  x,y :max(x,y)  # How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20)) # 20
print(large(10.7  ,  5.6)) # 10.7
print(large('g'  ,  's')) # 's'
print(large('Rama'  ,  'Rajesh')) # characters compare -'Rama'
print(large(True,False)) # 1

#Ex-6
#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))  # 2 ** 3 = 8
print(power(4.5 , 4)) # 4.5 ** 4 # 410.0625
print(power()) # 3.5 ** 2 = 12.25
print(power(9)) # 9 ** 2 = 81

#Ex-7
# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7) # (17 ,3,70,1.5)
print(type(x)) # class tuple
print(x) # type and address of lambda function
p , q , r , s = all(9 , 2) # (11,7,18,4.5)
print(p) # 11
print(q) # 7
print(r) # 18
print(s) # 4.5

#Ex-8
#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) # 'Hyd'
print(a) # type and address of lambda function

#Ex-9
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a() # 'Hyd' <nl> 'Sec' <nl> 'Cyb'

#Ex-10
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # 'Sec' <nl> 'Cyb' <nl>  'Hyd' <nl> None

#Ex-11
# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # 'Sec' <nl> 'Cyb' <nl>  'Hyd'

#Ex-12
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # class tuple
print()
print(a) # ('Sec'<nl> 'Cyb' <nl> type and address of lambda function)
for  x  in  a:
	print(x) # type and address of lambda function <nl> 'Sec' <nl> None <nl> 'Cyb' <nl>
print()
#a() # Error because tuple is object not call
print(a[0]()) # call lambda function  # 'Hyd' <nl> None

#Ex-13
#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) # type and address of lambda function because not call lambda function
print(lambda  x  :  print(x) (s)) # type and address of lambda function
print((lambda  x  :  print(x)) (s)) # Hyd <nl> None
(lambda  x  :print(x))(s) # Hyd

#Ex-14
# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y # x = 5 by default value
x = 10
adder2 = lambda  y , x = x : x + y # x = 10 by default value
x = 20
print(adder1(100)) # y = 100 ,5 + 10 = 105
print(adder2(200)) # y =200 ,10 + 200 = 210
print(adder1(300,400)) # 300 + 400


#Ex-15
#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
     print(fun(5)) # 5 ** 2 = 25 <nl> 5 ** 3 =  125 <nl> 5 ** 4 = 625

#Ex-16
#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2] # [ type and address of lambda function, type and address of lambda function]
for  x  in  a:
	     x() # Hyd <nl> Sec
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')] # Error  because syntax error
print(a)  # [ type and address of lambda function, type and address of lambda function]
a = [f1() ,f2()] # [None ,None]
print(a) # [None ,None]

#Ex-17
# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # type and address of lambda function,
print(a[key](5)) # 5 ** 3 =125

#Ex-18
# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3) # f1 return lambda function
print(type(f1)) # class function
print(type(lamb)) #  class function
print(lamb(2)) # 3 ** 2= 9
print(lamb(5)) # 3 ** 5 = 243
print(lamb) # type and address of lambda function
# print(lamb()) # missing positional argument

#Ex-19
# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5) # eval return lambda function
print(lam(2)) #  x is 2 => 3 * 2 ** 2 + 4 * 2 + 5 = 3 *  4 + 8 +5 = 25
print(lam(2.5))  #  x is 2 => 3 * 2.5 ** 2 + 4 * 2.5 + 5 = 3 * 6.25 + 10 +5 = 33.75
print(lam(4)) #  x is 2 => 3 * 4 ** 2 + 4 * 4 + 5 = 3 * 16 + 16 + 5 = 69

#Ex-20
#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add() #   a = lambda y: 10 + y
print(a(20)) # y = 20 => 10 + 20 = 30
print(add(30)(40)) # add(30) This returns lambda y: 30 + y => y is 40 then 30 + 40 = 70

#Ex-21
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
e = sorted(a , key =  lambda   x  :  x[2]) # sorts tuple 'a' based on 3rd element of each inner tuple duw to x[2]
print(e) # [(15, 'Rajesh', 500.0),(10 , 'Rama' , 1000.0) ,(5 , 'Amar' , 1300.0),(20 , 'Sita' , 2000.0),(18 , 'Kiran' , 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0]) #   Sorts  tuple  'a'  in ascending  order  of   1st  element  of  inner  tuples
print(f) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True) # #   Sorts  tuple  'a'  in descending  order  of   2nd  element  of  inner  tuples
print(g) # [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
#print(sorted(a,key=x[1])) # Error x is not define

# Ex-22
# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year']) # sort the based on year [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(b) # [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a)) # without a key does not work on lists of dictionaries.

#Ex-23
# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) # x[0] refers to the first value in each tuple. and return max value in tuple is 25 # (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] )) # x[1]  refers to the second value in each tuple. and return max value in tuple is Vamsi # (15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) # # x[1]  refers to the third value in each tuple. and return max value in tuple is 2800 # (20, 'Sita', 2800.0)
print(max(a)) # it will compare first element on each tuple # Since (25, 'Kiran', 1500.0)

#Ex-24
# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) # x is 10 pass to function and campare the 10 == 25 is  False
add = lambda  x = 25 :   x == 35 #
print(add()) # call add function and 25 == 35 is False
#add = lambda  x  :   x = 25 # Error because formal parameter can't be modified
#add = lambda x: x := 25 # # Error because formal parameter can't be modified

#Ex-25
#  Find  outputs  (Home  work)
def    f1():
        print('f1    function') # f1    function
def    f2():
        print('f2  function') # f2  function
# End  of  the  function
f1() # call f1
f2()# call f2
print(f1  is  f2) # False because both different objects
f2 = f1 # f1 function reference  is assigned to f2 reference
f2() # call f1  # f1    function
print(f1  is  f2) # True
f2 = f1() # True
print(f2) # f1 function <nl> None
#f2() # Error because NoneType object is not callable

#Ex-26
# Find  outputs (Home  work)
p = print #How  to  assign  ref  'p'  to  print()  function
p('Hyderabad') # How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
#print('Hello') # Error because NoneType object is not callable
p('Hello') # How  to  call  print()  function  thru  ref  'p'  and print 'Hello'

#Ex-27
# Find   outputs (Home  work)
x  = id # How  to  assign  ref  'x'  to  id()  function
print(x(25))  # How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p = len  # How  to  assign  ref  'p'  to  len()  function
print(p('Hyd'))    #  How  to  call  len()  function  thru  ref  'p'  and   print  length of 'Hyd


#Ex-28
#  Find  outputs (Home  work)
def  outer():
	print('Outer  function') # Outer  function
	def  inner(): # define inner function
		print('Inner  function')
	# End  of  inner  function
	print('Hello') # Hello
	inner() # call inner()  # Inner  function
	print('Back  to  outer  function') # Back  to  outer  function
def  other():
	#inner() # Error because inner() another function of inner function don't call
	print('Other  function')
# End  of  the  function
print('Begin') # Begin
outer() # call outer function
print('Hi') # Hi
# inner() # # Error because inner() another function of inner function don't call
other() # call other function # Other  function
print('Bye') # Bye

#Ex-29
# Find  output(Home  work)
def    f1(a): # a = 30
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a # call f2 and return 10 -> 10+20+30 = 60
# End  of  f1  function
print(f1(30)) # f1 call and pass 30

#Ex-30
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
outer() # Outer  function <nl> Hi <nl> 2nd  inner  function <nl> Hello <nl> 1st  inner  function <nl> Back  to  outer  function
print('Bye') # Bye

#Ex-31
# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer() # outer() call  # 30 <nl> 10
print('Bye') # Bye

#Ex-32
# Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x) # print  inside outer x value   20
		print(globals()['x']) # print global variable x 10
	inner()
outer()

#Ex-33
# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x) # there is no local variable x then print global variable x # 10
	inner()
outer() # call outer

#Ex-34
# Find  outputs  (Home  work)
def  outer():
	x = 10 # local variable of outer function
	def  inner():
		x = 20 # local variable of inner function
		print(x) # 20
		x +=  7 # modifies  x  value  local variable of inner function x = 20 + 7 = 27
	# End  of  inner  function
	print(x) #  print x value  local variable of outer function 10
	x += 5 # modifies  x  value  local variable of outer function x = 10 + 5 = 15
	inner() # call inner function
	print(x) #  print x value  local variable of outer function 15
# End  of  the  function
outer()
print('Bye') # Bye

#Ex-35
#  Find  outputs  (Home  work)
def  outer():
	x = 10 # local variable of outer function
	def  inner():
		nonlocal  x # x is local variable of outer function
		print(x) # 15
		x = 20   # modifies  x  value  nonlocal variable of outer function x = 20
		print(x) # 20
		x += 5 # x = 20 + 5 = 25
	# End  of  inner  function
	print(x) # 10
	x += 5 # x = 10 + 5 = 15
	inner()
	print(x) # 25
# End  of  outer  function
outer()
# print(x) # x not define in global variable

#Ex-36
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		# print(x) # x is not define
		nonlocal  x   # x is local variable of outer function 15
		x = 20   # modifies  x  value  nonlocal variable of outer function x = 20
		print(x) #  20
		x += 5  # x = 20 + 5 = 25
	# End  of  inner  function
	print(x) # 10
	x += 5 # x = 10 + 5 = 15
	inner()
	print(x) # 25
# End  of  outer  function
outer()

#Ex-37
#  Find   outputs(Home  work)
def  outer():
	x = 10 # local variable of outer function
	def  inner():
		global   x # declare global variable x
		x = 20  # 20 is assign x
		print(x) # 20
		x += 5 # x = 20 + 5 = 25
	# End  of  inner  function
	print(x) # 10
	x += 5 # x = 10 + 5 = 15
	inner()
	print(x) # 15
# End  of  outer  function
outer()
print(x) # 25

#Ex-38
# Find  outputs(Home  work)
def  outer():
	def  inner():
		# nonlocal  x # there is no L V of Outer function nonlocal keyword used access LV outer to modify them
		x = 20 # LV of inner function
		print(x) # 20
	# End  of  inner  function
	inner()
	#print(x) # x is not define in LV of outer
# End  of  the  function
outer()
#print(x) # x not define in globally

#Ex-39
# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x # declare G V
		x = 20 # 20 is assign x
		print(x) # 20
		x = x + 5 # x = 20 + 5 = 25
	# End  of  inner  function
	inner()
	print(x) # 25
# End  of  the  function
outer()
print(x) # 25

#Ex-40
#  Identify  Error
def   f1():
        # nonlocal x # Error because there is no x f1
    pass

# Ex-41
# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a # access LV of outer function
		a = 100 # modifies LV of outer a = 100
		b = 200 # #  LV of inner b = 200
		print(a , b) # 100 200
	# End  of  inner  function
	print(a , b) # 10 20
	inner()
	print(a , b) # 100 20
#end of outer function
outer()

#Ex-42
# Find  outputs (Home  work)
def   f1():
	x = 'John' # LV of Outer function
	def  f2():
		nonlocal  x # access LV of outer function
		x =  'Hello' # modifies LV of outer function x = 'Hello'
	#end of inner function
	f2()
	return  x # return x = 'Hello'
#  End  of  f1()  function
print(f1()) # Hello


#Ex-43
# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		# x =  x +  20 # Error because x is not define in  gun function
		print(x) # 10
	#end of inner function
	gun()
#end of outer function
fun()

#Ex-44
#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		# global  x # Error because  x is already define outer function
		nonlocal x

#Ex-45
#  Find  outputs  (Home   work)
def   f1():
	x = 10 # LV of f1
	def  f2():
		nonlocal   x # access LV OF f1
		def  f3():
			nonlocal   x #  access LV OF f1
			print(x) # print x value of f1 # 10
		f3()
	f2()
f1()
