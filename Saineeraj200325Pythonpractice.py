#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  (10, 20, 15, 18) <next line> <class 'tuple'> <next line> 4
f1() # () <next line> <class 'tuple'> <next line> 0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) # ([10, 20], (30, 40, 50), {80, 90, 60, 70}) <next line> <class 'tuple'> <next line> 3
f1('Hyd') # ('Hyd',) <next line> <class 'tuple'> <next line> 1
tpl = (100 , 200 , 150) 
f1(tpl) # ((100, 200, 150),) <next line> <class 'tuple'> <next line> 1
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka


'''
(10,20,15,18)
<class  'tuple'>
4
'''

#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
def  avg(*a):
    return sum(a)/len(a)  if a else 0   #Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #  Average  of  10 , 20 , 15  and  18 is 15.75
print(avg(25 , 10.8 , True)) # Average is 12.266666666666666
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # Average is 14.26
print(avg()) # average is 0
print(avg(25)) # average is 25.0
print(avg(3 + 4j , 5 + 6j)) # Average is 4+5j
tpl = (10 , 20 , 15 , 18)
#print(avg(tpl)) # Error: unsupported operand type(s) for +: 'int' and 'tuple'
'''
#Gift
#Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)
'''
def  concat(*a):
	return ' '.join(str(i) for i in a) if a else ''  #Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City')) # Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Python Is A Great Language
print(concat()) #    (empty string)
print(concat('Python')) # Python
print(concat(1, 2, 3)) # 1 2 3
#Find  outputs (Home  work)
def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a : 10 <tab> b : (20,30,40)
f1(50 , 60) # a : 50 <tab> b : (60,)
f1(70) # a : 70 <tab> b : ()
f1(a = 80) # a : 80 <tab> b : ()
#f1(b = (10 , 20 , 30) , a = 40) # Error: f1() got an unexpected keyword argument 'b'
f1() # a : 25  <tab>  b : ()
#f1(a = 10 , (20 , 30 , 40)) # Error: positional argument follows keyword argument
#f1(25 , b = (10 , 20 , 30)) # Error: f1() got an unexpected keyword argument 'b'
#f1(25 , a = (10 , 20 , 30)) # Error: f1() got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30) # a : (10, 20, 30)           b  :  (10, 20, 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30) Error: positional argument follows keyword argument
#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a : (10,20,30) <tab> b : 40
f1(50 , b = 60) # a : (50,) <tab> b : 60
f1(b = 70) # a : () <tab> b : 70
#f1(b = 10 , a = (20 , 30 , 40)) # Error: f1() got an unexpected keyword argument 'a'
#f1(b = 10 , (20 , 30 , 40)) # Error: positional argument follows keyword argument
#f1() # Error: f1() missing 1 required keyword-only argument: 'b'
#f1(10 , 20 , 30 , (10 , 20 , 30)) # Error: f1() missing 1 required keyword-only argument: 'b'
#f1(10 , 20 , 30 , 40) # Error: f1() missing 1 required keyword-only argument: 'b'
#f1(25) # Error: f1() missing 1 required keyword-only argument: 'b'
#f1(10 , 20 , 30 , b = (10 , 20 , 30)) # Error: f1() missing 1 required keyword-only argument: 'c'
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a  :  10          b  :  (20, 30, 40)      c  :  50
f1(60 , 70 , c = 80) # a  :  60          b  :  (70,)     c  :  80
f1(90 , c = 100) # a  :  90          b  :  ()        c  :  100
#f1(a = 1 , 2 , c = 3) # Error: positional argument follows keyword argument
#f1(1 , 2 , 3) # Error: f1() missing 1 required keyword-only argument: 'c'
#f1(a = 1 , b = 2 , c = 3) # Error: f1() got an unexpected keyword argument 'b'
#f1(a = 25 , 100 , 200 , 300 , c = 35) # Error: positional argument follows keyword argument
# Which  of  the  following  are  valid  ?  (Home  work)
#def   f1(*a , *b): # Error: * argument may appear only once
        #pass
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
#def   f6( * , a , *b , c): #Error: * argument may appear only once
       #pass
#def   f7(a , *b , c ,  /): # Error: / must be ahead of *
       #pass
# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60)) 
'''o/p: ([10, 20], {40, 30}, (50, 60))
		<class 'tuple'>
		[10, 20]
		<class 'list'>
		{40, 30}
		<class 'set'>
		(50, 60)
		<class 'tuple'>'''
# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  #  Dictionary  of  2  key : value  pairs  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()
'''o/p: Results
		<class 'dict'>
		{'RollNo': 10, 'StudName': 'Rama  Rao'}

		Results
		<class 'dict'>
		{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

		Results
		<class 'dict'>
		{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

		Results
		<class 'dict'>
		{}'''
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()
'''o/p: Results
		Empno ... 25
		Empname ... Rama  Rao
		Salary ... 10000.0
		Gender ... m
		Results'''
# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
'''o/p: <class 'tuple'>
		(25, 10.8, 'Hyd', True)

		<class 'dict'>
		{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}'''
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # Error: f1() got an unexpected keyword argument 'eno'
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) # {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}
# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)
print()
f1('Hyd' , 10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
'''o/p: 25

		Hyd
		(10, 20, 30)

		10.8
		(25, 'Hyd', True)
		'''
#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)
a += 1
f1()
print(a)
'''o/p: {'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
		a :  10
		b :  20
		c :  30

		a :  11
		b :  40
		c :  31

		a :  50
		b :  22
		c :  32
		Bye
		10
		20
		11'''
# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)
a += 1
f1()
print(a)
# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()
# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	print(globals()['x'])
# End  of  the  function
f1()
# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()
'''o/p: 10
		20
		11
		40
		10
		10
		20
		10
		40 50 60
		10 20 30
		100 200 300'''
# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)
def   f2():
	global  x
	x = 30
	print(x)
	x += 1
def   f3():
	global  y
	y = 40
	print(y)
	y += 1
def   f4():
	x = 50
	#global   x #Error: name 'x' is assigned to before global declaration
#  End  of  the  functions
x = 10
print(x)
x += 1
f1()
print(x)
f2()
print(x)
x += 1
f3()
print(y)
f4()
print(x)
'''o/p: 10
		20
		11
		30
		31
		40
		41
		32'''
# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a)
f1()
print(a)
'''o/p: 10
		20
		20
		30'''
# Find  outputs(Home  work)
def  f1():
	global  a
	print(a)
	a = 10
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1()
f2()
print(a)
'''o/p: 30
		10
		20
		30
		30'''
# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	global  a
	print(a)
	a = 30
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)
'''o/p: 10
		20
		30
		40'''
# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	print(a)
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1() # 10
#f2() # Error: cannot access local variable 'a' where it is not associated with a value
f3() # 20
print(a) # 40
#  Find  outputs (Home  work)
def  f1():
        a = 10
        #global  a # Error: name 'a' is assigned to before global declaration
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1() # 10
print(a) # 40
print(b) # 20

# Find outputs (Home  work)
def  f1():
        global  a
        print(a)
        a += 1
def  f2():
        global  a
        print(a)
        a += 1
# End  of  the  function
a = 10
print(a) # 10
a += 1
f1() # 11
print(a) # 12
a += 1
f2() # 13
print(a) # 14
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
def  f2():
	print(a)
	a += 1
# End of the function
a = 10
print(a) # 10
f1() # 20
a += 1
#f2() # Error: cannot access local variable 'a' where it is not associated with a value
print(a) # 11
# Find outputs (Home  work)
def  f1():
	a = 20
	#global   a # Error: name 'a' is assigned to before global declaration
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a) # 10
a += 1
f1() # 20
print(a) # 11 <nl> 40
#  Find   outputs
def   f1():
	x = x + 5
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
#f1() # Error: cannot access local variable 'x' where it is not associated with a value
f2() # 15
print(x) # 10