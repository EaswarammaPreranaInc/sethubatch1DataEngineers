
#1.Find outputs  (Home  work)
def   f1():
	print('Hyd')	# Hyd
	print('Sec')	# Sec
	print('Cyb')	# Cyb
	# End  of  the  function
print('Begin...')	# Begin...
x = f1()			# function() call.....control moves to line 2...	
print(x)			# None	
print(type(x))		# <class 'NoneType>'>
print('End')		# End

#Gift
#2.Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
	# End  of  the  function
x = f1()
print(x)	# (10,20,30)
print(type(x))	# <class 'tuple'>
a , b , c =  f1() # function call...
print(a)	# 10
print(b)	# 20
print(c)	# 30
print('for  loop') # for loop
for  k   in   f1():
	print(k)		# 10<nextLine>20<nextLine>30<nextLine>

#3.Find  outputs
def    f1():
        return  10
        return  20
        return  30
	# End  of  the  function
print('Begin')	# Begin
x = f1()		# function call....and function returns 10 to line 36 which is stores in 'x'
print(x)		# 10
print('End')	# End
#return   100	# Error...

#4.Find  outputs
#f1()	# Error..we cannot call a function before defining it...
def   f1():
        print('Hello')
print(f1()) # Hello
print(f1)	# <function f1 at 0x000001C5425C3D80>

#5.Find  outputs  (Home  work)
print('Hello')	# Hello
def  f1():
        print('f1  function')	# f1 funcion
	#End  of   function
print('Hi')	# Hi
print(f1())	# function call...and function returned value will be printed..i.e.None
print(f1)	# <function f1 at 0x000001C5425C3D80>
print('Bye')# Bye

#6.Find  outputs
def    f1():
        print('Hyd')	# Hyd
        print('Sec')	# Sec
        print('Cyb')	# Cyb
#End  of  the  function
print('Begin')	# Begin
print(type(f1))	# <class 'function'>
print(id(f1))	# Adress of f1 may be 1000
print('End')

#7.Find  outputs (Home  work)
def  f1():
	print('No-argument  function')	
def  f1(x):
	print('Single  argument  function  : ' , x)	
def  f1(x , y):
	print('Two  argument  function : ' , x , y)	
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z) # Three arguments: 10 20 30
f1(10 , 20 , 30)#function call... control moves to line 76 and executes the function,returns None
#f1(40 , 50)		# Error...
#f1(60)			# Error...
#f1()			# Error..


#8.Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')	#No-argument function
f1()		#function call... control moves to line 86 and executes the function,returns None
def  f1(x):
	print('Single  argument  function  : ' , x) # Single argument function : 10
f1(10)		#function call... control moves to line 89 and executes the function,returns None
def  f1(x , y):
	print('Two  argument  function : ' , x , y) # Two argument function: 20 30
f1(20,30)	#function call... control moves to line 92 and executes the function,returns None
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z) # Three argument function : 40 50 60
f1(40,50,60)#function call... control moves to line 76 and executes the function,returns None

#9.Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')#Emp Number : 25 ename : Rama Rao Salary : 10000.0
	# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)#function call... control moves to line 100 and executes the function,returns None
disp('Sita' , 20000.0 , 35) #function call... control moves to line 100
							#Executes the function,returns None but these values results in incorrect values order

#10.Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
	# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a : Cyd <tab> b : Sec <tab> c : Hyd
f1(c = 3 + 4j , a = True , b = None)# a : True <tab> b : None <tab> c : (3+4j)
f1(25 , c = 10.8 , b = 'Hyd') # a : 25 <tab> b : Hyd <tab> c : 10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'

#11.Find  outputs (Home  work)
def    disp(empno , ename , sal):	# disp() exwutes 3 times.....
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}') #Emp Number: 25<tab>Emp Name : Rama Rao<tab>Salary : 10000.0
																						#Emp Number: 35<tab>Emp Name : Sita<tab>Salary : 20000.0
																						#Emp Number: Rama Rao<tab>Emp Name :30000.0<tab>Salary : 20
	# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)	#function call... control moves to line 123 and executes the function,returns None
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)#function call... control moves to line 123 and executes the function,returns None
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)	##function call... control moves to line 123 and executes the function,returns None


#  Gift
#12.Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
	#end  of  the  function
print(f1(3 , 4 , 5))#Function call..control moves to execute f1 function..after execution value is returned and returned value is printed i.e.23
print(f1(*[6 , 7 , 8]))	# 62
#print(f1([6 , 7 , 8]))	# Error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))	# 16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))	# 14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))	#Error..
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})# 'c' : 2 'b' : 4 'a' : 6
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))	# Error..


#13.Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))	# Error.... pa..ka is allowed but not ka..pa as arguments
print(sorted(a , rev = True))		# Error due to 'rev'
print(25 , 10.8 , 'Hyd' , separator = '\t')	# Error due to 'separator'
print(25 , 10.8 , 'Hyd' , endofline = '\t')	# Error due to 'endofline'
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')	#Error.... pa..ka is allowed but not ka..pa as arguments