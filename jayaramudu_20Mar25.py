#Ex-1
def f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  Tuple  of  4  elements  is  passed  to  the  function (10 , 20 , 15 , 18) <nl> class tuple <nl> 4
f1() # () <nl> class tuple <nl> 0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) # ([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) <nl> class tuple <nl> 3
f1('Hyd') # ('Hyd',) <nl> class tuple <nl> 1
tpl = (100 , 200 , 150)
f1(tpl) # ((100 , 200 , 150)) W<nl> class tuple <nl> 1
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka


#Ex-2
#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
def avg(*a):
    try: # Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
        return sum(a) / len(a)
    except ZeroDivisionError:
        return "Please pass values"
    except TypeError:
        return sum(*a) / len(*a)


# Test cases
print(avg(10, 20, 15, 18))  # Average of 10, 20, 15, and 18 #
print(avg(25, 10.8, True))  # True is treated as 1 # 12.27
print(avg(10.8, 20.6, 15.2, 14.9, 9.8)) # 14.26
print(avg())  # Error because No values passed
print(avg(25))  # Single value #25.0
print(avg(3 + 4j, 5 + 6j))  # Error because Complex numbers (Invalid case) # 4+5j

tpl = (10, 20, 15, 18)
print(avg(tpl))  # Unpacking tuple

# Ex-3
'''
Gift
Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)
'''
def  concat(*a):
	 return " ".join(str(item) for item in a)  #Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1,2,3))
'''
Sankar Dayal Sarma
Hyd Is Green City
Python Is A Great Language

Python
1 2 3

'''

Ex-4
#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a : 10  <tab> b : (20 , 30 , 40)
f1(50 , 60)  # a : 50  <tab> b : (60,)
f1(70) # a : 70 <tab> b : ()
f1(a = 80) # a : 80 <tab> b : ()
#f1(b = (10 , 20 , 30) , a = 40) # # Error because b is var-arg  but passed KA
f1() # a : 25 <tab> b : ()
#f1(a = 10 , (20 , 30 , 40)) #  PA after KA
#f1(25 , b = (10 , 20 , 30)) # Error because b is var-arg  but passed KA
#f1(25 , a = (10 , 20 , 30)) # # Error because b is var-arg  but passed KA
f1((10 , 20 , 30) , 10 , 20 , 30) # a : (10 , 20 , 30) <tab> b : (10, 20, 30)
#f1(a = (10 , 20 , 30),10,20,30) # Error because  KA  after PA


#Ex-5
#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a  :  (10, 20, 30) <tab> b  :  40
f1(50 , b = 60) # a  :  (50,) <tab> b  :  60
f1(b = 70) # # a  :  () <tab> b  :  (70)
#f1(b = 10 , a = (20 , 30 , 40)) # Error because where a is var-arg but pass KA
#f1(b = 10 , (20 , 30 , 40)) # Error because KA after PA ,but PA after KA
#f1() # Error because b is not pass
#f1(10 , 20 , 30 , (10 , 20 , 30)) # Error because b value is not pass
#f1(10 , 20 , 30 , 40) # # Error because b value is not pass
#f1(25) # # Error because b value is not pass
f1(10 , 20 , 30 , b =(10,20,30)) # a  :  (10, 20, 30) <tab> b  :  (10, 20, 30)

#Ex-6
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a  :  10 <tab> b  :  (20, 30, 40) <tab> c  :  50
f1(60 , 70 , c = 80) # a  :  60 <tab> b  :  (70,) <tab> c  :  80
f1(90 , c = 100) # a  :  90 <tab> b  :  () <tab> c  :  100
#f1(a = 1 , 2 , c = 3) # # Error because PA After but here KA After PA
#f1(1 , 2 , 3) # Error because c must be KA
#f1(a = 1 , b = 2 , c = 3) # Error b is var arg not KA
#f1(a = 25 , 100 , 200,300,c=35) # Error because PA After but here KA After PA


#Ex-7
# Which  of  the  following  are  valid  ?  (Home  work)
#def   f1(*a , *b): # Error multiple var arg not possible
#        pass
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
#def   f6( * , a , *b , c): # Error because * after keyword argument only
#       pass
#def   f7(a , *b , c , /): # Ambigity problem
#    pass


#Ex-8
# Find  outputs  (Home  work)
def   f1(*a):
	print(a) # tuple of nested ([10 , 20] , {30 , 40},(50,60))
	print(type(a)) # class tuple
	for  x  in  a:
		print(x) # [10,20] <nl>  {30 , 40} <nl>  (50,60)
		print(type(x)) # class list <nl> class set <nl> class tuple
# End  of  the  function
f1([10 , 20] , {30 , 40},(50,60))

#Ex-9
# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  #  Dictionary  of  2  key : value  pairs  is  passed  to  the  function # Results <nl> <class 'dict'> <nl> {'RollNo': 10, 'StudName': 'Rama  Rao'}
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0) #  Dictionary  of  3  key : value  pairs  is  passed  to  the  function # Results <nl> <class 'dict'> <nl> {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender='m') # #  Dictionary  of  4  key : value  pairs  is  passed  to  the  function # Results <nl> <class 'dict'> <nl> {'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
disp() # Results <nl> <class 'dict'> <nl> {}

#Ex-10
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender='m') #   Dictionary  of  3  key : value  pairs  is  passed  to  the  function  # Results <nl> Empno ... 25 <nl> Empname ... Rama  Rao <nl> Salary ... 10000.0 <nl> Gender ... m
f1() # Results

#Ex-11
# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True) # tuple of 3 elements pass to function <class tuple> <nl> (25,10.8,'Hyd',True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary=10000.0) # Dictionary  of  3  key : value  pairs  is  passed  to  the  function  <class 'dict'> <nl> {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

#Ex-12
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # tuple 3 values  Emp  Number  :  25  <tab> Emp  Name  :  Sita  <tap> Salary  :	10000.0
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # eno  ,empname, salary are  not declare
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # dict of 3 key value pairs {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary=10000.0) # dict of 3 key value pairs {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}

#Ex-13
# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25) # 25
print()
f1('Hyd' , 10 , 20 , 30) #  a = 'Hyd' b = (10,20,30) # 'Hyd' <nl> (10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary=10000.0) # a = 10.8 b = 25,'Hyd',True c ={'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0} # 10.8 <nl> (25,'Hyd', True) <nl> {'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}

#Ex-14
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

'''
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
'''

#Ex-15
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)
a +=1
f1()
print(a)

'''
10 <nl> 20 <nl>
'''

#Ex-16
# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a) # 20
	dict = globals() # get all global variables
	print(dict['a']) # 11
	a = 30
	dict['a'] = 40 # global variable modify a = 40
#  End  of  f1()  function
a = 10
print(a) # 10
a +=1 # a = 10+1 = 11
f1() # 20 11 40
print(a)
'''
10 <nl> 20 <nl> 11 <nl> 40
'''

#Ex-17
# Find  outputs (Home  work)
x = 10 # 1  start
def   f1():
	print(x) # 10
	print(globals()['x']) # 10
# end of the function
f1() # 2  10 <nl> 10

#Ex-18
# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	#print(globals()['x']) # Error because there is no key x in global
# End  of  the function
f1()

#Ex-19
# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c) # 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c']) # 10 20 30
	dict['a'] = 100 # modify global variable a = 100
	dict['b'] = 200 # modify global variable a = 200
	dict['c'] = 300 # modify global variable a = 300
def  f2():
	print(a , b , c) # 100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()

#Ex-20
# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x) # 20
def   f2():
	global  x # access global variable x
	x = 30 # x is modified
	print(x) # 30
	x += 1 # x = 30 +1 = 31
def   f3():
	global  y # declare y in globally
	y = 40 # 40 is assign to y
	print(y)# 40
	y += 1 # y = 40 +1 =41
def   f4():
	x = 50
#	global   x # Error because x is already intialized
#  End  of  the  functions
x = 10 # start
print(x) # 10
x += 1 # x = 10+1 = 11
f1() # f1 call
print(x) # 11
f2() # x is  modified 31
print(x) # 31
x += 1 # x = 31 + 1 = 32
f3() #  y = 41
print(y) # 41
f4()
print(x) # 32

#Ex-21
# Find outputs (Home  work)
def  f1():
	global  a # access global variable a
	a = 20 # g v a is modified 20
	print(a) # 20
	print(globals()['a']) # 20
	a = 30 # a is modified 30
# End of the function
a = 10 # start
print(a) # 10
f1() # call f1  a = 30 # 20 20
print(a) # 30

#Ex-22
# Find  outputs(Home  work)
def  f1():
	global  a  #  declare a in globally
	#print(a) # a is  not defined
	a = 10
	print(globals()['a']) # 10
	a = 20 # g v modified a = 20
	print(a) # 20
	a = 30 # # g v modified a = 30
def  f2():
    print(a) # 30
#End  of   f2   function
f1()
f2()
print(a) # 30

#Ex-23
# Find outputs (Home  work)
def  f1():
	global   a # declare global variable a
	a = 10 # a = 10
	print(a) # 10
	a = 20 # modified global variable a
def  f2():
	global  a #
	print(a) # 20
	a = 30 # modified global variable a is 30
def  f3():
	print(a) # 30
	globals()['a'] = 40 # modified global variable is 40
# End  of  the  function
f1()
f2()
f3()
print(a) # 40

#Ex-24
# Find outputs (Home  work)
def  f1():
	global   a # declare global variable a
	a = 10
	print(a) # 10
	a = 20 # G V is modified a is 20
def  f2():
	#print(a) # not defined
	a = 30
	print(a) # 30
def  f3():
	print(a) # 20
	globals()['a'] = 40 # G V a is modified 40
# End  of  the  function
f1()
f2()
f3()
print(a) # 40


#Ex-25
#  Find  outputs (Home  work)
def  f1():
        a = 10
        # global  a # Error because after a initialization after declare global a
        print(a) # 10
        global  b # declare g v as b
        b = 20 # 20 is assigned b
# End  of  f1()  function
f1()
# print(a) # not defined
print(b) # 20

#Ex-26
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a) # 20
#def  f2():
	#print(a) # Error becoz a not defined
	#a += 1  #  Error becoz a not defined
# End of the function
a = 10
print(a) # 10
f1()
a +=1 # a = 10 +1 = 11
#f2()
print(a) # 11


#Ex-27
# Find outputs (Home  work)
def  f1():
	a = 20
	#global   a # # Error because after a initialization after declare global a
	print(a) # 20
	print(globals()['a']) # 11
	a = 30
	globals()['a'] = 40 # GV modified a = 40
#  End  of  f1()   function
a = 10 # start
print(a) # 10
a +=1 # a = 10 + 1 = 11
f1() # f1 call
print(a) # 40

#Ex-28
#  Find   outputs
#def   f1():
	# x = x + 5 # x is not define local variable
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5 # x is L V  x = 10 + 5 =15
	print(x) # 15
# End of f2  function
x = 10 # start
#f1() # f1 call
f2()
print(x) # 10
