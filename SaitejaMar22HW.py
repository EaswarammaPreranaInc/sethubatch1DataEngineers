

#1. Find  outputs 
'''
square = lambda  x = 10  :   x * x
print(square(5)) #1. 25
print(square())  #2. 100
'''

#2.Find  output 
'''
add= lambda a,b : a+b #How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add)) #<class 'function'>
print(add(10 , 20)) #30
print(add(10.6 , 20.8)) #31.4
print(add('Hyder' , 'abad')) #Hyderabad
print(add(True , False))#1
print(add(25 , 10.8))#35.8
print(add(3 + 4j , 5 + 6j))#(8+10j)
#print(add(10 , '20'))#TypeError due to int + str 
#print(add())#Error 2 args missing 
print(add) #<function <lambda> at hex(address)>
'''

#3.Find  outputs
'''
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) #30
print(add()) #3
'''

#4.Find  outputs
'''
print((lambda  x , y : x + y) (10 , 20) ) #30
print((lambda  x , y : x + y) (10.8 , 20.6)) #31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) #Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) #<function <lambda> at 0xaddress>
'''

#5.Find  outputs
'''
large= lambda x,y : x if (x>y) else y #How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20)) #20
print(large(10.7  ,  5.6)) #10.7
print(large('g'  ,  's')) #s
print(large('Rama'  ,  'Rajesh')) #Rama 
print(large(True  ,  False)) #True
'''

#6.Find  outputs 
'''
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) #8
print(power(4.5 , 4)) # 410.0625
print(power()) #12.25
print(power(9)) #81

'''

#7.Find  outputs

'''
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x)) #<class 'tuple'>
print(x) #(17,3,70,1.4285714285714286)
p , q , r , s = all(9 , 2)
print(p) #11
print(q) #7
print(r) #18
print(s) #4.5
'''

#8.Find  outputs
'''
a  =  lambda  :  'Hyd'
print(a()) #Hyd
print(a) #<function <lambda> at 0xaddress>
'''

#9.Find  outputs
'''
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a() #Sec \n Cyb \n Hyd and returns None 
'''

#10.Find  outputs
'''
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) #Sec \n Cyb \n Hyd \n None \n 
'''

#11.Find  outputs
'''
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # Sec \n Cyb \n Hyd \n
'''

#12.Find  outputs

'''
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb') #1. Sec \n Cyb \n 
print(type(a)) #2.<class 'tuple'>
print(a) # 3.(<function <lambda> at 0xaddress ,None , None)
for  x  in  a:
	print(x) # 4.<function <lambda> at 0xaddress \n #5.None \n #6.None \n 
#a() #Error tuple is not callable
print(a[0]()) #7.Hyd \n #8.None 
'''

#13.Find  outputs 
'''
s = 'Hyd'
print(lambda  s  :  print(s)) #1.<function <lambda> at 0xaddress>
print(lambda  x  :  print(x) (s)) #2.<function <lambda> at 0xaddress>
print((lambda  x  :  print(x)) (s)) # 3.Hyd \n #4. None 
(lambda  x  :  print(x)) (s) #5. Hyd 
'''

#14.Find outputs
'''
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) #105
print(adder2(200)) #210
print(adder1(300 , 400)) #700

'''
#15.Find  outputs 
'''
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5)) #1. 10 \n #2. 15 \n #3. 625 \n
'''


# 16.Find  outputs
'''
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2] 
for  x  in  a:
	     x() #1. Hyd \n 2.Sec \n 
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')] #Error due to indentation 
print(a) #3. [<function <f1> at 0xaddress1> ,<function <f2> at 0xaddress2>]
a = [f1() , f2()] #4. Hyd [None]\n  5.Sec [None,None] \n
print(a) #6. [None,None]

'''

#17.Find output
'''
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # <function <lambda> at 0xaddress>
print(a[key](5)) #125
'''

#18.Find  outputs
'''
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1)) #<class 'function'>
print(type(lamb)) #<class 'function'>
print(lamb(2)) #9
print(lamb(5)) #243
print(lamb) #<function <lambda> at 0xaddress>
#print(lamb()) #Error req PA n 
'''


#19.Find  outputs  
'''
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) #(12 + 8 + 5) # 25
print(lam(2.5)) #(6.25) # 33.75
print(lam(4)) #(48+16+5) # 69
'''


#20.Nested  lambda  function 
'''
add  =  lambda    x = 10   :    lambda   y  :  x  + y
a = add() 
print(a(20)) #30
print(add(30)(40)) #70
'''

#21.Find  outputs
'''
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
print(e) # [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0),(5, 'Amar', 1300.0), (20, 'Sita', 2000.0),(18, 'Kiran', 2800.0),]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) # [(20, 'Sita', 2000.0),(10, 'Rama', 1000.0), (15, 'Rajesh', 500.0),(18, 'Kiran', 2800.0),(5, 'Amar', 1300.0)]
#print(sorted(a , key = x[1])) #Error no x

'''


#22.Find outputs 

'''
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) 

"""[ 
     {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
     {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008},
     {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ]
            
"""
#print(sorted(a)) #Error sort of dict not possible 
'''

#23.Find outputs 
'''
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) #(25 , 'Kiran' , 1500.0)
print(max(a , key = lambda  x  :  x[1] )) #(15 , 'Vamsi' , 2000.0)
print(max(a , key = lambda  x  :  x[2] )) #(20 , 'Sita' , 2800.0)
print(max(a)) #(25 , 'Kiran' , 1500.0)
'''

#24.Find  output
'''
add = lambda  x  :   x == 25
print(add(10)) #False 
add = lambda  x = 25 :   x == 35
print(add()) #False 
#add = lambda  x  :   x = 25 #Error lambda function doen't support obj modification
#add = lambda  x  :   x := 25 #Error lambda function doen't support obj modification

'''


#25.Find  outputs
'''
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1() #1. f1    function
f2() #2. f2  function

print(f1  is  f2) #3.False 
f2 = f1
f2() #4. f1    function
print(f1  is  f2) #5. True 
f2 = f1() #6. f1    function
print(f2) #7. None 
#f2() #Error f2 points to None 

'''

#26.Find  outputs 

'''
p=print #How  to  assign  ref  'p'  to  print()  function
p('Hyderabad') #How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
#print('Hello') #Error print not callable becz points to None 
p('Hello') #How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'

'''

#27.Find   outputs
'''
x=id  #How  to  assign  ref  'x'  to  id()  function
print(x(25)) #address  (How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p=len #How  to  assign  ref  'p'  to  len()  function
print(p('Hyd')) #3 How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd'

'''


#28.Find  outputs
'''
def  outer():
	print('Outer  function') #2. Outer function
	def  inner():
		print('Inner  function') #4. Inner function 
	# End  of  inner  function
	print('Hello') #3. Hello 
	inner()
	print('Back  to  outer  function') #5. Back  to  outer  function
def  other():
	#inner() #Error No inner function 
	print('Other  function') # 7. Other function 
# End  of  the  function
print('Begin') #1. Begin 
outer()
print('Hi') #6. Hi 
#inner() #Error No inner function 
other() 
print('Bye') # 8. Bye
'''

#29.Find  output
'''
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) #60
'''

#30.Find  outputs 
'''
def  outer():
	print('Outer  function') #2. Outer function
	def  inner1():
		print( '1st  inner  function') #6. 1st inner function 
	def  inner2():
		print('2nd  inner  function') #4.2nd inner function 
	print('Hi') #3. Hi 
	inner2()
	print('Hello') #5. Hello 
	inner1() 
	print('Back  to  outer  function') #7. Back to outer function 
# End of the function
print('Begin') #1. Begin 
outer()
print('Bye') #8. Bye
'''

#31.Find  outputs
'''
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x) #1. 30 
		print(globals()['x']) #2. 10
	inner()
outer()
print('Bye') #3. Bye
'''

#32.Find  outputs
'''
x = 10
def  outer():
	x = 20
	def   inner():
		print(x) #20 
		print(globals()['x']) #10
	inner()
outer()

'''

#33.Find  outputs 
'''
x = 10
def  outer():
	def   inner():
		print(x) #10 
	inner()
outer()
'''

#34.Find  outputs
'''
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x) #2. 20 
		x +=  7 #x(27)
	# End  of  inner  function
	print(x) #1. 10 
	x += 5 #x(15)
	inner()
	print(x) #3. 15
# End  of  the  function
outer()
print('Bye') #4. Bye
'''


#35.Find  outputs 
'''
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x) #2. 15 
		x = 20 #x(20)
		print(x) #3. 20 
		x += 5 #x(25)
	# End  of  inner  function
	print(x) #1. 10 
	x += 5 #x(15)
	inner()
	print(x) #4. 25 
# End  of  outer  function
outer()
#print(x) #Error x not defined 
'''

#36.Find  outputs
'''
def  outer():
	x = 10
	def  inner():
		#print(x) 
		nonlocal  x 
		x = 20 #x(20)
		print(x) #2. 20 
		x += 5 #x(25)
	# End  of  inner  function
	print(x) #1. 10
	x += 5 #x(15)
	inner()
	print(x) #3. 25
# End  of  outer  function
outer()
'''

#37.Find   outputs
'''
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20 #x(20) global 
		print(x) #2. 20 
		x += 5 #x(25) global 
	# End  of  inner  function
	print(x) #1. 10 
	x += 5 #x(15)
	inner()
	print(x) #3. 15 
# End  of  outer  function
outer()
print(x) #4. 25
'''

#38.Find  outputs
'''
def  outer():
	def  inner():
		#nonlocal  x
		x = 20
		print(x) #1. 20 
	# End  of  inner  function
	inner()
	#print(x) #Error no x 
# End  of  the  function
outer()
#print(x) #Error no global x 
'''


#39.Find  outputs
'''
def  outer():
	def  inner():
		global   x
		x = 20 
		print(x) #1. 20 
		x = x + 5 #x(25)
	# End  of  inner  function
	inner()
	print(x) #2. 25
# End  of  the  function
outer()
print(x) #3. 25 
'''

#40.Identify  Error
'''
def   f1():
        #nonlocal   x #we can't create non local object in outer function
        pass 
'''

#41.Find  outputs 
'''
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100 
		b = 200
		print(a , b) #2. 100 200 
	# End  of  inner  function
	print(a , b) #1. 10 20 
	inner()
	print(a , b) #3. 100 20
#end of outer function
outer()
'''

#42.Find  outputs 
'''
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
'''


#43.Find  output
'''
def  fun():
	x = 10
	def    gun():
		#x =  x +  20 #Error updating local x without local x
		print(x) #1. 10 
	#end of inner function
	gun()
#end of outer function
fun()
'''


#44.Identify  Error
'''
x = 10
def   outer():
	x = 20
	def  inner():
		#global   x #error because already non local x 
		nonlocal  x 
		
'''

#45.Find  outputs 
'''
def   f1():
	x = 10
	def  f2():
		nonlocal   x 
		def  f3():
			nonlocal   x
			print(x) #10
		f3()
	f2()
f1()
'''