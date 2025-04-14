# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) #25
print(square())  #100
'''
OUTPUT:
25
100
'''


# Find  output (Home  work)
#How  to  define  lambda  function   to  return  sum   of  two  arguments

add=lambda x,y:x+y
print(type(add))
print(add(10 , 20))
print(add(10.6 , 20.8))
print(add('Hyder' , 'abad'))
print(add(True , False))
print(add(25 , 10.8))
print(add(3 + 4j , 5 + 6j))
#print(add(10 , '20')) #Error because can't add int and str
#print(add()) #Error because <lambda>() missing 2 required positional arguments: 'x' and 'y'
print(add)
'''
OUTPUT:
<class 'function'>
30
31.4
Hyderabad
1
35.8
(8+10j)
<function <lambda> at 0x0000025D49E01440>
'''


#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) #30
print(add()) #3
'''
OUTPUT:
30
3
'''


#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )    #40 and return none
print((lambda  x , y : x + y) (10.8 , 20.6)) #31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) #Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) #<function <lambda> at 0x000001C70E6BF9C0>
'''
OUTPUT:
30
31.400000000000002
Hyderabad
<function <lambda> at 0x000001C70E6BF9C0>
'''



#  Find  outputs (Home  work)
#How  to  define  lambda  to  detrmine  largest  of  two  arguments
large=lambda x,y:max(x,y)
print(large(10  ,  20))
print(large(10.7  ,  5.6))
print(large('g'  ,  's'))
print(large('Rama'  ,  'Rajesh'))
print(large(True  ,  False))
'''
OUTPUT:
20
10.7
s
Rama
True
'''



#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) #8
print(power(4.5 , 4)) #4.5**4
print(power())        #3.5**2 
print(power(9))       #9**2
'''
OUTPUT:
8
410.0625
12.25
81
'''


# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7) #(17,3,70,1.42)
print(type(x)) # class<'tuple'>
print(x)       #(17,3,70,1.42)
p , q , r , s = all(9 , 2) 
print(p) #11
print(q) #7
print(r) #18
print(s) #4.5
'''
OUTPUT:
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
OUTPUT:
Hyd
<function <lambda> at 0x0000023BE5A082C0>
'''

# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()
'''
OUTPUT:
Sec
Cyb
Hyd
'''


# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
'''
OUTPUT:
Sec
Cyb
Hyd
None
'''



# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
'''
OUTPUT:
Sec
Cyb
Hyd
'''


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) #class<'tuple'>
print(a)       #(<function <lambda> at 0x000001EE39FB82C0>, None, None)
for  x  in  a:
	print(x)  #<function <lambda> at 0x000001EE39FB82C0> <nextline> None <nextline> None
#a()  #Error 
print(a[0]()) #Hyd <nextline> None
'''
OUTPUT:
<class 'tuple'>
(<function <lambda> at 0x000001EE39FB82C0>, None, None)
<function <lambda> at 0x000001EE39FB82C0>
None
None
Hyd
None
'''


#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) 
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)
'''
OUTPUT:
<function <lambda> at 0x000002736E9A8360>
<function <lambda> at 0x000002736E9A8360>
Hyd
None
Hyd
'''


# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))   # 105
print(adder2(200))   # 210
print(adder1(300 , 400)) #700
'''
OUTPUT:
105
210
700
'''



#Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5)) #10 <nextline> 15 <nextline> 625
'''
OUTPUT:
10
15
625
'''



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
'''
OUTPUT:
Hyd
Sec
[<function f1 at 0x000001F579B08400>, <function f2 at 0x000001F579B087C0>]
Hyd
Sec
[None, None]
'''




# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])
print(a[key](5))
'''
OUTPUT:
<function <lambda> at 0x000002813E98F060>
125
'''





# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))
print(type(lamb))
print(lamb(2)) #9
print(lamb(5)) #243
print(lamb)
#print(lamb())
'''
OUTPUT:
<class 'function'>
<class 'function'>
9
243
<function f1.<locals>.<lambda> at 0x0000021A3F10F060>
'''








# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) #25
print(lam(2.5))
print(lam(4))
'''
OUTPUT:
25
33.75
69
'''






#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) #30
print(add(30)(40))#70
'''
OUTPUT:
30
70
'''



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
e = sorted(a , key =  lambda   x  :  x[2])  #Sorts   tuple  'a'  based  on   3rd  element  of  each  inner  tuple  due  to  x[2]
print(e)    #[(15, 'Rajesh', 500.0),(10, 'Rama', 1000.0),(5, 'Amar', 1300.0),(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])##Sorts   tuple  'a'  based  on   1st  element  of  each  inner  tuple  due  to  x[0]
print(f) #[(5, 'Amar', 1300.0),(10, 'Rama', 1000.0),(15, 'Rajesh', 500.0),(18, 'Kiran', 2800.0),(20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True) # # Sorts   tuple  'a' in descending order based  on   2nd  element  of  each  inner  tuple  due  to  x[1]
print(g) #[(20, 'Sita', 2000.0),(10, 'Rama', 1000.0),(15, 'Rajesh', 500.0),(18, 'Kiran', 2800.0),(5, 'Amar', 1300.0)]
#print(sorted(a , key = x[1]))
'''
OUTPUT:
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]

[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]

[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
'''




# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year']) # #  Sorts  list  'a'  in ascending order   of   year  element  of  inner  dictionary
print(b)   #[{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999},{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008},{'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013}]
#print(sorted(a))  #Error
'''
OUTPUT:
[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
'''



# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) #(25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] )) #(15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) #(20, 'Sita', 2800.0)
print(max(a))#(25, 'Kiran', 1500.0)
'''OUTPUT:
(25, 'Kiran', 1500.0)
(15, 'Vamsi', 2000.0)
(20, 'Sita', 2800.0)
(25, 'Kiran', 1500.0)
'''



# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) #False
add = lambda  x = 25 :   x == 35
print(add()) #False
#add = lambda  x  :   x = 25 #can't assign for lambda
#add = lambda  x  :   x := 25
'''
OUTPUT:
False
False
'''




'''#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()
f2()
print(f1  is  f2) #False
f2 = f1
#f2()
print(f1  is  f2)#True
f2 = f1()
print(f2) #f1 function
#f2()

f1    function
f2  function
False
True
f1    function
None




# Find  outputs (Home  work)
#How  to  assign  ref  'p'  to  print()  function
p=print
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
p('hyderabad')
p=print
print=None
p('Hello')
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'

OUTPUT:
hyderabad
Hello





# Find   outputs (Home  work)
#How  to  assign  ref  'x'  to  id()  function
x=id
#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p=print
p=x
p(25)
print(p(25))#140721753491112
#How  to  assign  ref  'p'  to  len()  function
p=len
#How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
print(p('hyd')) #3'''




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
'''
OUTPUT:
Begin
Outer  function
Hello
Inner  function
Back  to  outer  function
Hi
Other  function
Bye
'''




# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a #10+20+30
# End  of  f1  function
print(f1(30)) #60





# Find  outputs (Home  work)
def  outer():
	print('Outer  function') #Outer function
	def  inner1():
		print( '1st  inner  function')
	def  inner2():
		print('2nd  inner  function')
	print('Hi') #Hi
	inner2()    #2nd inner function
	print('Hello') #Hello
	inner1()    #1st inner function
	print('Back  to  outer  function') #Back to outer function
# End of the function
print('Begin') #Begin
outer()
print('Bye') #Bye
'''
OUTPUT:
Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye
'''




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
OUTPUT:
30
10
Bye
'''





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
OUTPUT:
20
10
'''



# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()
'''
OUTPUT:
10
'''


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
OUTPUT:
10
20
15
Bye
'''



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
print(x)
'''
OUTPUT:
15
20
25
10
'''
print()

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)
		#nonlocal  x
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
OUTPUT:
10
20
15
'''




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
OUTPUT:
10
20
15
25
'''
print()




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
outer()
#print(x)
'''
OUTPUT:
20
'''




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
'''
OUTPUT:
20
25
25
'''



#  Identify  Error
'''def   f1():
        #nonlocal   x
		pass'''





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
'''
OUTPUT:
10 20
100 200
100 20
'''




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
print(f1())
'''
Hello
'''



# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20
		print(x)
	#end of inner function
	gun()
#end of outer function
fun()
'''
OUTPUT:
10
'''

#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		#nonlocal x


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
'''
OUTPUT:
10
'''
















