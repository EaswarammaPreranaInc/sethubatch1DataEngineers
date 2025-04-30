'''
#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t)) 
	print(len(t))   
	print()   
# End  of  the  function
f1(10 , 20 , 15 , 18)     # (10,20,15,18) <nl> <class ' tuple'>  <nl>  4 #  Tuple  of  4  elements  is  passed  to  the  function
f1()   # () <nl> <class 'tuple'>  <nl> 0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})    # ([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) <nl> <class 'tuple'>  <nl> 3
f1('Hyd')   # ('Hyd') <nl> <class 'tuple'>  <nl> 1
tpl = (100 , 200 , 150)
f1(tpl)  # ((100 , 200 , 150))  <nl> <class 'tuple'>  <nl> 1
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka
'''


'''
#Find  outputs (Home  work)
def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)
f1(50 , 60)   # a : 50    b : (60,)
f1(70)        # a : 70    b : ()
f1(a = 80)    # a : 80    b : ()
#f1(b = (10 , 20 , 30) , a = 40)  #  f1() got an unexpected keyword argument 'b'
f1()   # a : 25 b:()
#f1(a = 10 , (20 , 30 , 40))    # positional argument follows keyword argument
#f1(25 , b = (10 , 20 , 30))    # f1() got an unexpected keyword argument 'b'
#f1(25 , a = (10 , 20 , 30))    # f1() got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30)   # w
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)  #  positional argument follows keyword argument
'''

'''
#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)
f1(50 , b = 60)   # a : (50,)   b : 60
f1(b = 70)      # a : ()   b : (70)
#f1(b = 10 , a = (20 , 30 , 40))  # f1() got an unexpected keyword argument 'a'
#f1(b = 10 , (20 , 30 , 40))  # positional argument follows keyword argument
#f1()   # f1() missing 1 required keyword-only argument: 'b'
#f1(10 , 20 , 30 , (10 , 20 , 30))  # f1() missing 1 required keyword-only argument: 'b'
#f1(10 , 20 , 30 , 40)   # f1() missing 1 required keyword-only argument: 'b'
#f1(25)  #  f1() missing 1 required keyword-only argument: 'b'
f1(10,20,30 , b = (10,20,30))  # a : (10,20,30)  b : (10,20,30)
'''


'''
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)  # a : 10   b : (20,30,40)  c : 50
f1(60 , 70 , c = 80)     # a : 60   b : (70,)   c : 80
f1(90 , c = 100)        # a : 90   b : ()    c : 100
#f1(a = 1 , 2 , c = 3)  # positional argument follows keyword argument
#f1(1 , 2 , 3)    # f1() missing 1 required keyword-only argument: 'c'
#f1(a = 1 , b = 2 , c = 3)  #  positional argument follows keyword argument
#f1(a = 25 , 100 , 200 , c = 35) # positional argument follows keyword argument
'''

'''
# Which  of  the  following  are  valid  ?  (Home  work)
#def   f1(*a , *b):    #  * argument may appear only once
#        pass   # unexpected indent
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
#def   f6( * , a , *b , c):   #  * argument may appear only once
#       pass   # IndentationError: unindent does not match any outer indentation level
#def f6(a, *b, c , /):   # / must be ahead of *
#	pass  # inconsistent use of tabs and spaces in indentation
'''


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

# output
([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>
'''

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
disp(AcNo = 30 , CustNmae = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

#output

Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}

Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustNmae': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}
'''

'''
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama Rao' , Salary = 10000.0 , Gender = 'm')
f1()

#output

Results
Empno ... 25
Empname ... Rama Rao
Salary ... 10000.0
Gender ... m
Results
'''

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
f2(EmpNum = 25 , EmpName = 'Sita' , Salary = 10000.0)


# output
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
'''

'''
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)   # Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # f1() got an unexpected keyword argument 'eno'
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)  # {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , Salary = 10000.0) # {'eno': 25, 'empname': 'Sita', 'Salary': 10000.0}
'''

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

#output

25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
'''

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

# output
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

'''
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

#output
10
20
11
'''

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

#output
10
20
11
40'''

'''
# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)   # 10
	print(globals()['x'])  # 10
# end of the function
f1()'''


'''
# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x) # 20
	#print(globals()['x'])
# End of the function
f1()
'''

'''
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

#output
40 50 60
10 20 30
100 200 300
'''

'''
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
	#global   x  #  name 'x' is assigned to before global declaration
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

#output
10
20
11
30
31
40
41
32'''


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

#output
10
20
20
30'''

'''
# Find  outputs(Home  work)
def  f1():
	global  a
	#print(a)   # name 'a' is not defined
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


#output
10
20
30
30'''


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
	print(a)
# End  of  the  function
f1()
f2()
f3()

#output
10
20
30
40'''


'''
# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	#print(a)  # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
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



#output

10 <nl> 20  <nl> 30 <nl> 40 <nl>'''


'''
#  Find  outputs (Home  work)
def  f1():
        a = 10
        #global  a  # name 'a' is assigned to before global declaration
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()
#print(a)  # name 'a' is not defined
print(b)

#output
10 <nl> 20
'''

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
a += 1
f1()
print(a)
a += 1
f2()
print(a)

#output
10 <nl> 12 <nl> 13 <nl> 14'''


'''
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
#def  f2():   # IndentationError: expected an indented block after function definition on line 546
	#print(a)  #  UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
	#a += 1    # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value   
# End of the function
a = 10
print(a)
f1()
a += 1
#f2()  # NameError: name 'f2' is not defined. Did you mean: 'f1'?
print(a)

#output
10 <nl> 20 <nl> 11'''


'''
# Find outputs (Home  work)
def  f1():
	a = 20
	#global   a   # SyntaxError: name 'a' is assigned to before global declaration
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)
a += 1
f1()
print(a)

#output
10 <nl> 20 <nl> 11 <nl> 40'''


'''
#  Find   outputs
#def   f1():   # IndentationError: expected an indented block after function definition 
	#x = x + 5    # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
#f1()  # NameError: name 'f1' is not defined. Did you mean: 'f2'?
f2()
print(x)


#output
15 <nl> 10 '''


'''
#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
def avg(*a):
    try: # Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
        return sum(a) / len(a)
    except ZeroDivisionError:
        return "Please pass values"
    except TypeError:
        return sum(*a) / len(*a)
		
		
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #  Average  of  10 , 20 , 15  and  18
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))

#output

Average  of  10 , 20 , 15  and  18
15.75
12.266666666666666
14.26
Please pass values
25.0
(4+5j)
15.75'''




#Gift
#Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)
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


#output
Sankar Dayal Sarma
Hyd Is Green City
Python Is A Great Language

Python
1 2 3'''
