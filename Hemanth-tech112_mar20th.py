#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  Tuple  of  4  elements  is  passed  to  the  function
f1()  # Empty tuple is passed to function
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})  # Tuple of 3 args is passed to the function
f1('Hyd')  # Tuple of single arg is passed to the function
tpl = (100 , 200 , 150)
f1(tpl)  # Nested tuple is passed to the function
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  parameters  can  not be  KA

'''   OUTPUTS
(10, 20, 15, 18)
<class 'tuple'>
4

()
<class 'tuple'>
0

([10, 20], (30, 40, 50), {80, 90, 60, 70})
<class 'tuple'>
3

('Hyd',)
<class 'tuple'>
1

((100, 200, 150),)
<class 'tuple'>
1
'''



#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Homework)
def  avg(*a):
   try:
      return sum(a)/len(a)# Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
   except ZeroDivisionError:
      return 0
   except TypeError:
      return sum(*a)/len(*a)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #  Average  of  10 , 20 , 15  and  18
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))

'''    Sample Output
15.75
12.266666666666666
14.26
0
25.0
(4+5j)
15.75

'''


'''
Gift
Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)
'''
def  concat(*a):
   try:
      return " ".join(a)
   except:
      return 'Pass Strings from the function call'


# Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))  # Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language'))  # Python Is A Great Language
print(concat())  # Empty tuple i.e. ()
print(concat('Python'))  # Python
print(concat(1,2,3))  # Pass Strings from the function call

'''     OUTPUT 
Sankar Dayal Sarma
Hyd Is Green City
Python Is A Great Language

Python
Pass Strings from the function call
'''


#Find  outputs (Homework)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)  # a : 10 <tab> b : (20,30,40)
f1(50 , 60)  # a : 50 <tab> b : 60
f1(70)  # a : 70 <tab> b : ()
f1(a = 80)  # a : 80 <tab> b : ()
# f1(b = (10 , 20 , 30) , a = 40)  # Error because var-arg parameter cannot be a KA
f1()  # a : 25 <tab> b : ()
# f1(a = 10 , (20 , 30 , 40))  # Error due to PA after KA
# f1(25 , b = (10 , 20 , 30))  # Error because var-arg cannot be a KA
# f1(25 , a = (10 , 20 , 30))  # Error because arg is passed for 'a' is twice
f1((10 , 20 , 30) , 10 , 20 , 30)  # a : (10,20,30) <tab> b : (10,20,30)
# f1(a = (10 , 20 , 30),10,20,30)  # Error due to PA after KA

'''    OUTPUT
a : 10  	   b  :  (20, 30, 40) 
a : 50  	   b  :  (60,) 
a : 70  	   b  :  () 
a : 80  	   b  :  () 
a : 25  	   b  :  () 
a : (10, 20, 30)  	   b  :  (10, 20, 30) 

'''



#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)  # a : (10,20,30) <tab> b : 40
f1(50 , b = 60)  # a : 50 <tab> b : 60
f1(b = 70)  # a : () <tab> b : 70
# f1(b = 10 , a = (20 , 30 , 40))  # Error because var-arg parameter cannot be a KA
# f1(b = 10 , (20 , 30 , 40))  # Error because PA after KA
# f1() # Error because argument is not passed for 'b'
# f1(10 , 20 , 30 , (10 , 20 , 30))  # Error because argument is not passed for 'b'
# f1(10 , 20 , 30 , 40)  # Error because argument is not passed for 'b'
# f1(25)  # 'a' is (25,) but Error because argument is not passed for 'b'
f1(10 , 20 , 30 , b =(10,20,30))  # a : (10,20,30) <tab> b : (10,20,30)

'''   OUTPUT
a  :  (10, 20, 30)   	   b  :  40
a  :  (50,)   	   b  :  60
a  :  ()   	   b  :  70
a  :  (10, 20, 30)   	   b  :  (10, 20, 30)

'''


#Find  outputs (Homework)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)  # a : 10 <tab> b : (20,30,40) <tab> c : 50
f1(60 , 70 , c = 80)  # a : 60 <tab> b : 70 <tab> c :80
f1(90 , c = 100)  # a : 90 <tab> b : () <tab> c : 100
# f1(a = 1 , 2 , c = 3)  # Error because PA after KA
# f1(1 , 2 , 3)  # 'a' is 1 and 'b' is (2,3) Error because argument  is not passed for 'c'
# f1(a = 1 , b = 2 , c = 3)  # Error because var-arg cannot be a KA
# f1(a = 25 , 100 , 200,300,c=35)  # Error because PA after KA

'''     OUTPUT
a  :  10  	  b  :  (20, 30, 40)  	  c  :  50
a  :  60  	  b  :  (70,)  	  c  :  80
a  :  90  	  b  :  ()  	  c  :  100

'''



# Which  of  the  following  are  valid  ?  (Homework)
# def   f1(*a , *b):  # Error due to more than one var-arg parameter
#       pass
def  f2(*a , b):  # Valid due to single var-arg parameter
        pass
def  f3(a , *b):  # valid due to single var-arg parameter
        pass
def  f4(a , b):  # Valid
        pass
def    f5(a , *b , c):  # valid due to single var-arg parameter
        pass
# def   f6( * , a , *b , c):  # Error because 'a' and 'b' cannot be  KA's
#     pass
# def   f7(a , *b , c , /):   # Error because c cannot be PA
#     pass



# Find  outputs  (Homework)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40},(50,60))  # Tuple 3 elements passed to the function

'''    OUTPUT
([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>

'''



# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  #  Dictionary  of  2  key : value  pairs  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)  # Dictionary of 3 key: value pairs is passed to the function
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender='m')  # Dictionary of 4 key : value pairs is passed to the function
disp()  # Results <nextline> <class 'dict'> <nextline> {}

'''     OUTPUT
Results
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
{}

'''


# Find  outputs  (Homework)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender='m')  # Dictionary of 4 key : value pairs is passed to the function
f1()  # Results

'''    OUTPUT
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results

'''


# Find  outputs (Homework)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)  # <class 'tuple'> <nextline> (25,10.8,'Hyd',True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary=10000.0)  # Dictionary of 3 key : value pairs are passed to the function

'''
<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
'''


#  Find  outputs (Homework)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)  # Emp Number : 25 <tab> Emp Nmae : Sita <tab> Salary : 10000.0
# f1(eno = 25 , empname = 'Sita' , salary = 10000.0)  # Error due to eno is not defined
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)  # Dictionary of 3 key : value pairs are passed to the function
f2(eno = 25 , empname = 'Sita' , salary=10000.0)  # Dictionary of 3 key : value pairs are passed to the function

'''    Output
Emp  Number  :  25  	  Emp  Name  :  Sita  	  Salary  :	10000.0
{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}

'''



# Find  outputs   (Homework)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)  # a : 25
print()
f1('Hyd' , 10 , 20 , 30)  # prints a and b
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary=10000.0)  # Prints a and b and c

'''
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}

'''



#Find  outputs (Homework)
a = 10   #GV
def   f1():
	b = 40  # LV
	print('a : ' , a)  # GV a : 11
	print('b : ' , b)  # LV b : 40
	print('c : ' , c)  # GV c : 31
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50  # LV
	print('a : ' , a)  # LV a : 50
	print('b : ' , b)  # GV b : 22
	print('c : ' , c)  # GV c : 32
# End  of  f2()  function
c = 30  # GV
print('a : ' , a)  # GV i.e.  a : 10
print('b : ' , b)  # GV i.e.  b : 20
print('c : ' , c)  # GV i.e.  c :30
print()
a +=  1  # GV is incremented by 1   i.e.  11
b +=  1  # GV is incremented by 1   i.e.  21
c +=  1  # GV is incremented by 1   i.e.  31
f1()
a +=  1  # GV is incremented by 1   i.e.  12
b +=  1  # GV is incremented by 1   i.e.  22
c +=  1  # GV is incremented by 1   i.e.  32
f2()
print('Bye')  # Bye

'''    OUTPUT
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


# Find  outputs (Homework)
def   f1():
	a = 20  # LV
	print(a)  # LV  is 20
	a += 1  # LV is incremented by 1  i.e. 21
#End  of  the  function
a = 10  # GV
print(a)  # 10
a +=1  # GV is incremented by 1  i.e. 11
f1()
print(a)  # 11

'''   OUTPUT
10
20
11

'''



# Find  outputs  (Homework)
def   f1():
	a = 20  # LV
	print(a)  # LV is 20
	dict = globals()  # {a : 11}
	print(dict['a'])  # GV  i.e. 11
	a = 30
	dict['a'] = 40  # Modifies GV to 40
#  End  of  f1()  function
a = 10  # GV
print(a)  # 10
a +=1  # 11
f1()
print(a)  #  40

'''   OUTPUT
10
20
11
40

'''


# Find  outputs (Homework)
x = 10  # GV
def   f1():
	print(x)  # GV  i.e. 10
	print(globals()['x'])  # 10
# end of the function
f1()

'''   OUTPUT
10
10

'''


# Find  outputs (Homework)
def  f1():
	x = 20   # LV
	print(x)  # LV  i.e. 20
	# print(globals()['x'])  # Error because GV 'x' does not exist
# End  of  the function
f1()

'''   OUTPUT
20
'''



# Find outputs (Homework)
def  f1():
	a = 40  # LV1
	b = 50  # LV2
	c = 60  # LV3
	print(a , b , c)  # 40 50 60
	dict = globals()  # {'a' : 10,'b' : 20,'c' : 30}
	print(dict['a'] , dict['b'] , dict['c'])  # i.e. 10 <space> 20 <space> 30
	dict['a'] = 100  # Modifies  GV 'a' to 100
	dict['b'] = 200  # Modifies GV 'b' to 200
	dict['c'] = 300  # Modifies GV 'c' to 300
def  f2():
	print(a , b , c)  # 100 <space> 200 <space> 300
# End  of  f2  function
a = 10  # GV1
b = 20  # GV2
c=30  # GV3
f1()
f2()

'''
40 50 60
10 20 30
100 200 300

'''


# global  keyword  demo  program (Home  work)
def    f1():
	x = 20  # LV
	print(x)  # LV   i.e. 20
def   f2():
	global  x  # Treats 'x' as GV to f2() function
	x = 30  # Modifies GV to 30
	print(x)  # GV  i.e. 30
	x += 1  # GV is incremented by 1   i.e. 31
def   f3():
	global  y   # Treats 'y' as GV to f3() function
	y = 40  # Creates a GV with value 40
	print(y)  # GV   i.e. 40
	y += 1  # GV is incremented by 1   i.e. 41
def   f4():
	x = 50
	# global   x  # Error because there is already LV with same name
#  End  of  the  functions
x = 10  # GV
print(x)  # GV   i.e 10
x += 1  # GV is incremented by 1   i.e.  11
f1()
print(x)   # LV  i.e. 20
f2()
print(x)  # GV   i.e 31
x += 1   # GV is incremented by 1   i.e. 32
f3()
print(y)   # GV   i.e.41
f4()
print(x)  # GV   i.e. 32

'''   OUTPUT
10
20
11
30
31
40
41
32

'''


# Find outputs (Homework)
def  f1():
	global  a  # Treats 'a' as GV to f1() function
	a = 20  # Modifies GV  to 20
	print(a)  # GV   i.e. 20
	print(globals()['a'])  #  GV  i.e. 20
	a = 30  # Modifies GV to 30
# End of the function
a = 10   # GV
print(a)  # GV  i.e. 10
f1()
print(a)  # GV  i.e. 30

'''   OUTPUT
10
20
20
30

'''


# Find  outputs(Home  work)
def  f1():
	global  a  # Treats 'a' as GV to f1() function
	print(a)  # Error because GV does not exist
	a = 10  # creates GV with the value 10
	print(globals()['a'])  # GV  i.e 10
	a = 20  # Modifies GV to 20
	print(a)  # GV  i.e. 20
	a = 30  # Modifies GV to 30
def  f2():
	print(a)  # GV  i.e. 30
# End  of   f2   function
f1()
f2()
print(a)  # Gv  i.e. 30

'''   OUTPUT
10
20
30
30

'''


# Find outputs (Homework)
def  f1():
	global   a  # Treats 'a' as GV to f1() function
	a = 10  # Creates GV with the value 10
	print(a)  # GV  i.e. 10
	a = 20  # Modifies GV to 20
def  f2():
	global  a  # Treats 'a' as GV to f2() function
	print(a)  # GV   i.e. 20
	a = 30  # Modifies GV to 30
def  f3():
	print(a)  # GV  i.e. 30
	globals()['a'] = 40  # Creates a new GV 40
# End  of  the  function
f1()
f2()
f3()
print(a)  # GV  i.e. 40

'''   OUTPUT
10
20
30
40

'''


# Find outputs (Homework)
def  f1():
	global   a  # Treats 'a' as GV to f1() function
	a = 10  # Creates GV with the value 10
	print(a)  # GV  i.e. 10
	a = 20  # Modifies GV to 20
def  f2():
	# print(a)  # Error because 'a' does not exist
	a = 30  # LV
	print(a)  # LV   i.e. 30
def  f3():
	print(a)  # GV  i.e 20
	globals()['a'] = 40  # Create new GV 40
# End  of  the  function
f1()
f2()
f3()
print(a)  # GV  i.e. 40

'''
10
30
20
40

'''



#  Find  outputs (Homework)
def  f1():
        a = 10
        # global  a  # Error because LV 'a' already exists
        print(a)  # LV  i.e. 10
        global  b  # Treats 'b' as Gv to f2() function
        b = 20  # Creates Gv with the value 20
# End  of  f1()  function
f1()
# print(a)  # Error because there is no GV 'a'
print(b)  # GV  i.e. 20

'''
10
20
'''


# Find outputs (Homework)
def  f1():
        global  a  # Treats 'a' as GV to f1() function
        print(a)  # GV  i.e. 11
        a += 1  # GV is incremented by 1  i.e. 12
def  f2():
        global  a  # Treats 'a' as GV to f2() function
        print(a)  # GV   i.e. 13
        a += 1  # GV is incremented by 1   i.e. 14
# End  of  the  function
a = 10  # GV
print(a)  # GV  i.e 10
a += 1  # GV is incremented by 1   i.e.  11
f1()
print(a)  # GV  i.e  12
a +=1  # GV is incremented by 1  i.e.  13
f2()
print(a)  # GV  i.e. 14

'''   OUTPUT
10
11
12
13
14

'''



# Find  outputs (Homework)
def   f1():
	a = 20  # LV
	print(a)  # LV    i.e 20
def  f2():
	#print(a)  # Error because LV 'a' is not initialised
	#a += 1  # Error because LV 'a' on the rhs is not yet intialized
    pass
# End of the function
a = 10  # GV
print(a)  # GV   i.e. 10
f1()
a +=1  # GV is incremented by 1   i.e. 11
f2()
print(a)  # GV  i.e.  11

'''   OUTPUT
10
20
11

'''


# Find outputs (Homework)
def  f1():
	a = 20
	# global   a  # Error because LV 'a' already exists
	print(a)  # 20
	print(globals()['a'])  # GV  i.e. 11
	a = 30  # Modifies GV to 30
	globals()['a'] = 40  # creates a new GV 40
#  End  of  f1()   function
a = 10  # GV
print(a)  # GV  i.e. 10
a +=1  # GV is incremented by 1  i.e. 11
f1()
print(a)  # GV   i.e. 40

'''   OUTPUT
10
20
11
40

'''



#  Find   outputs
def   f1():
	# x = x + 5  # Error because LV 'x' is not initialized
    pass
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5  # creates LV with 10+5=15
	print(x)  # LV  i.e. 15
# End of f2  function
x = 10
f1()
f2()
print(x)  # GV   i.e. 10

'''   Output
15
10

'''


