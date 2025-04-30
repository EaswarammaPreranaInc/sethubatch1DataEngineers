'''
#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t) #(10,20,15,18)
	print(type(t))#(<'class tuple'>)
	print(len(t))#4
	print()#0
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  Tuple  of  4  elements  is  passed  to  the  function
f1()#Empty tuple ,1,0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) # Tuple of 3 elements (which are set, list, tuple)is passed to the function	
f1('Hyd')# tuple of single string object
tpl = (100 , 200 , 150) #it is taking the single elements 
f1(tpl)# tuple of 3 elemnets which given outside the function
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka
'''

'''
(10,20,15,18)
<class  'tuple'>
4
'''

#------------------------------------------------------------------------------------------
'''
#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
def  avg(*a):
	return sum(a)/len(a)
	#return average
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #  15.75
print(avg(25 , 10.8 , True))# 12.266666666666666
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))# 14.26
#print(avg())
print(avg(25))#25.0
print(avg(3 + 4j , 5 + 6j))#(4+5j)
#tpl = (10 , 20 , 15 , 18)
#print(avg(tpl))
'''
#---------------------------------------------------------------------------------------------------
'''
Gift
Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)

def  concat(*a):
	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
	return ' '.join(a)
	#return s
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
#print(concat(1, 2, 3))
'''
#........................................................................................................
'''
#Find  outputs (Home  work)
def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)
f1(50 , 60)
f1(70)
f1(a = 80)
#f1(b = (10 , 20 , 30) , a = 40)
f1()
#f1(a = 10 , (20 , 30 , 40))# error because pa follows ka
#f1(25 , b = (10 , 20 , 30))
#f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)
# Error occurs due to positional args followed by keyword args
'''
#.....................................................----------------------------------------
'''
#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)
f1(50 , b = 60)
f1(b = 70)
#f1(b = 10 , a = (20 , 30 , 40))
#f1(b = 10 , (20 , 30 , 40))
#f1()
#f1(10 , 20 , 30 , (10 , 20 , 30))
#f1(10 , 20 , 30 , 40)
#f1(25)
f1(10 , 20 , 30 , b = (10 , 20 , 30))
'''
#------------------------------------------------------------------------------------
'''
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)
f1(60 , 70 , c = 80)
f1(90 , c = 100)
#f1(a = 1 , 2 , c = 3)
#f1(1 , 2 , 3)
#f1(a = 1 , b = 2 , c = 3)
#f1(a = 25 , 100 , 200 , 300 , c = 35)
'''
#-----------------------------------------------------------------------------------

'''
# Which  of  the  following  are  valid  ?  (Home  work)
#	def   f1(*a , *b):
 #       pass
 # * args must be only once
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
#def   f6( * , a , *b , c):
 #      pass
 # * args must be only once
#def   f7(a , *b , c ,  /):
 #.      pass
 #/ must be ahead of *
 '''
#----------------------------------------------------------------------------------
'''
# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
'''

#output-->
'''
[10 , 20] , {30 , 40} , (50 , 60)
(c<lass 'tuple'>)
[10,20]
<class 'list'>
{30,40}
<class 'set'>
(50,60)
<class 'tuple'>
'''
#--------------------------------------------------------------------------
'''
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
'''

'''
#output
Results
<class 'dict'>
'RollNo' = 10 , 'StudName' = 'Rama  Rao'

Results
<class 'dict'>
'EmpNo' = 25 , 'EmpName' = 'Sita', 'Salary' = 10000.0

Results
<class 'dict'>
'AcNo' = 30 , 'CustName' = 'Kiran' , 'Balance' = 20000.0 , 'Gender' = 'm'

Results
<class 'dict'>
{}
'''
#----------------------------------------------------------------------------------
'''
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()
'''

'''
#output---->
Results
'Empno'...25
'Empname'...'Rama Rao'
'Salary'...10000.0
'Gender'...'m'
Results
'''
#--------------------------------------------------------------------------------------
'''
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
'''
'''
#output--->
<class 'tuple'>
25,10.8,'Hyd',True

<class 'tuple'>
'EmpNum' : 25 , 'EmpName' :  'Sita' , 'Salary' : 10000.0
'''
#-----------------------------------------------------------------------------------------
'''
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0)  #Error unexpected argments occured
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
'''

'''
#output--->
'Emp  Number'  :  25  'Emp  Name'  :  'Sita'    'Salary'  :	10000.0

'empno' : 25 , 'ename' :'Sita' , 'sal' : 10000.0
'eno' : 25 , 'empname' : 'Sita' , 'salary' : 10000.0
'''
#-----------------------------------------------------------------------------------------
'''
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
'''
'''
#output--->
25

'Hyd'
(10,20,30)

10.8 
(25,'Hyd',True)
'EmpNo' : 12 , 'EmpName' : 'Rama  Rao' , 'Salary' : 10000.0
'''
#------------------------------------------------------------------------------------------------
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
a +=  1 #11
b +=  1 #21
c +=  1 #31
f1()
a +=  1 #12
b +=  1 #22
c +=  1 #32
f2()
print('Bye')

#output--->
a:10
b:20
c:30

a:11
b:40
c:31

a:50
b:22
c:32
Bye
'''
#---------------------------------------------------------------------------------
'''
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1 #21
#End  of  the  function
a = 10
print(a)
a += 1 #11
f1()
print(a)

output--->
10
20
11
'''
#------------------------------------------------------------------------------
'''
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

output--->
10
20
11
40
'''
#---------------------------------------------------------------------------------
'''
# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()


#output--->
10
10
'''
#-----------------------------------------------------------------------------------
'''
# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	#print(globals()['x'])
# End  of  the  function
f1()
'''
'''
output--->
20
error because after local varaiable u cant write global varaiables
'''
#---------------------------------------------------------------------------------
'''
# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)
	dict = globals() #here it takes values from global values mention in lines from 412 to 414
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
'''
'''
output-->
40,50,60
10,20,30
100,200,300
'''
#-----------------------------------------------------------------------------------------
'''
# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)
def   f2():
	global  x
	x = 30
	print(x)
	x += 1 #31
def   f3():
	global  y
	y = 40
	print(y)
	y += 1 #41
def   f4():
	x = 50
	#global   x
#  End  of  the  functions
x = 10
print(x)
x+= 1 #11
f1()
print(x)
f2()
print(x)
x += 1 #32
f3()
print(y)
f4()
print(x)

#output
10
20
11
30
31
40
41
32
'''
#---------------------------------------------------------------------
'''
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

#output==>
10
20
20
30
'''
#----------------------------------------------------------------------
'''
# Find  outputs(Home  work)
def  f1():
	
	global  a
	#print(a)
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

#output--->
10
20
30
30
'''
#-------------------------------------------------------------------
'''
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

#output--->
10
20
30
40
'''
#------------------------------------------------------------------------
'''
# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	#print(a) #Error because  need to creation before the print statement
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)

#output--->
10
20
30
40
'''
#--------------------------------------------------------------------------
'''
#  Find  outputs (Home  work)
def  f1():
        a = 10
       # global  a #error because after creating local var we cant write global var 
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()
#print(a) error because 'a' is not defined outside the function
print(b)

#output--->
10
20
'''
#-------------------------------------------------------------------------------
'''
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
print(a)
a += 1 #11
f1()
print(a)
a += 1
f2()
print(a)

#output--->
10
11
12
13
14
'''
#------------------------------------------------------------------------------
'''
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
def  f2():
	#print(a) error coz a is not created in the function
	#a += 1
	pass
# End of the function
a = 10
print(a)
f1()
a += 1 #11
f2()
print(a)

#output--->
10
20
11
'''
#----------------------------------------------------------------------------------
'''
# Find outputs (Home  work)
def  f1():
	a = 20
	#global   a
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)
a += 1 #11
f1()
print(a)

#output--->
10
20
11
40
'''
#---------------------------------------------------------------------------------
'''
#  Find   outputs
def   f1():
	#x = x + 5 error because x is not defined in function
	pass
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1()
f2()
print(x)

#output--->
15
10
'''
