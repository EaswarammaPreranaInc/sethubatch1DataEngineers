#  Variable  number  of  arguments  demo  program
'''
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  Tuple  of  4  elements  is  passed  to  the  function
#(10,20,15,18)
#<class 'tuple'>
# 4
f1()
#empty
#<class 'tuple'>
#0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
#([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
#<class 'tuple'>
# 3
f1('Hyd')
# hyd
# <class 'str'>
# 1
tpl = (100 , 200 , 150)
f1(tpl)
# (100 , 200 , 150),
# <class 'tuple'>
# 1

#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka
'''

#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
'''
def  avg(*a):
    c=sum(a)/len(a)
    return c 
# Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #  Average  of  10 , 20 , 15  and  18 is 15.75
print(avg(25 , 10.8 , True)) # 12.266
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 14.26
print(avg()) # error
print(avg(25)) # 25.0
print(avg(3 + 4j , 5 + 6j)) # (4+5j)
tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) # error

'''


#Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)
'''
def  concat(*a):
    return ' '.join(a)
    #c=''
    #for i in a:
    #    c+=i+' '
    #return c
# Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))

'''


#Find  outputs (Home  work)
'''
def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)# a:10 \t b:(20,30,40)
f1(50 , 60)# a:50 \t b:(60,)
f1(70)# a:70 \t b:()
f1(a = 80)# a:80 \t b:()
f1(b = (10 , 20 , 30) , a = 40)# error
f1()# a:25 \t b:
f1(a = 10 , (20 , 30 , 40))# error
f1(25 , b = (10 , 20 , 30))# error
f1(25 , a = (10 , 20 , 30))# error
f1((10 , 20 , 30) , 10 , 20 , 30)# a:(10,20,30) \t b:(10,20,30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)# error

'''


#Find  outputs (Home  work)
'''
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)# a:(10,20,30) \t b:40
f1(50 , b = 60)# a:(50,) \t b:60
f1(b = 70)# a:() \t b:70
f1(b = 10 , a = (20 , 30 , 40))# error
f1(b = 10 , (20 , 30 , 40))# error
f1()# error
f1(10 , 20 , 30 , (10 , 20 , 30))# error
f1(10 , 20 , 30 , 40)# error
f1(25)# error
f1(10 , 20 , 30 , b = (10 , 20 , 30))# a:(10,20,30) \t b:(10,20,30)

'''


#Find  outputs (Home  work)
'''
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)# a:10 \t b:(20,30,40) \t c:50
f1(60 , 70 , c = 80)# a:60 \t b:70 \t c:80
f1(90 , c = 100)# a:90 \t b:() \t c:100
f1(a = 1 , 2 , c = 3)# error
f1(1 , 2 , 3)# error
f1(a = 1 , b = 2 , c = 3)# error
f1(a = 25 , 100 , 200 , 300 , c = 35)# error
'''

# Which  of  the  following  are  valid  ?  (Home  work)
'''
def   f1(*a , *b):# error
        pass
def  f2(*a , b):# a is positional arg and b is any
        pass
def  f3(a , *b):# a is any b is positional
        pass
def  f4(a , b):# a and b is both positional and keyword
        pass
def    f5(a , *b , c):# a is any b is positional and c is any
        pass
def   f6( * , a , *b , c):# we can't use positional arg after keyword 
       pass
def   f7(a , *b , c ,  /):# we can't use multiple things in a single one 
       pass

'''


# Find  outputs  (Home  work)
'''
def   f1(*a):
	print(a)# ([10,20],{30,40},(50,60))
	print(type(a))# <class 'tuple'>
	for  x  in  a:
		print(x)# [10,20]
				# <class 'list'>
				# {30,40}
				# <class 'set'>
				# (50,60)
				# <class 'tuple'>
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))

'''


# Variable  number  of  keyword  arguments  demo  program
'''
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  #  Dictionary  of  2  key : value  pairs  is  passed  to  the  function
											#  Results
											#  <class 'dict'>
											#  {rollno : 10 , studname : rama rao}
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0) # Results
													   # <class 'dict'>
													   # {EmpNo : 25 , EmpName : 'sita' , salary : 10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm') # results 
																		# <class 'dict'>
																		# {acno : 30 , custname : kiran , balance = 20000.0 , gender = 'm'}
disp() # results
	   # <class 'dict'>
	   # {}

'''


# Find  outputs  (Home  work)
'''
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()

# results
# empno ... 25 
# empname ... 'rama rao'
# salary ... 10000.0
# gender ... 'm'
# results

'''


# Find  outputs (Home  work)
'''
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)# (25,10.8,'hyd',true)
							# <class 'tuple'>
print()# new line 
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)# <class 'dict'>
													  # {empnum = 25 , empname = 'sita' , salary : 10000.0}

'''


#  Find  outputs (Home work)
'''
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)# emo number : 25 , emp name : 'sita' , salary : 10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)# Error due to keyword names doesn't match
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)# emp number : {empno : 25} , emp name : {ename : sita} , salary : {sal : 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)# emp number : {eno : 25} ,emp name : {empname : sita} , salary : {salary : 10000.0}

'''



# Find  outputs   (Home  work)
'''
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)# 25
print()# new line
f1('Hyd' , 10 , 20 , 30)# hyd
						# (10,20,30)
print()					# new line
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
# 10.8
# (25,hyd,true)
# {EmpNo : 12 , EmpName : 'Rama  Rao' , Salary : 10000.0}

'''


#Find  outputs (Home  work)
'''
a = 10
def   f1():
	b = 40
	print('a : ' , a)# a : 11
	print('b : ' , b)# b : 40
	print('c : ' , c)# c : 31
	print()# new line
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)# a : 50
	print('b : ' , b)# b : 22
	print('c : ' , c)# c : 32
# End  of  f2()  function
c = 30
print('a : ' , a)#10
print('b : ' , b)#20
print('c : ' , c)#30
print()# new line
a +=  1#11
b +=  1#21
c +=  1#32
f1()
a +=  1#12
b +=  1#22
c +=  1#32
f2()
print('Bye')# bye

'''


# Find  outputs (Home  work)
'''
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)# 10
a += 1# a=11
f1()# 20
print(a)# 11

'''


# Find  outputs  (Home  work)
'''
def   f1():
	a = 20
	print(a)
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)# 10
a += 1 # 11
f1()# 20
	# 11
print(a)# 40

'''


# Find  outputs (Home  work)
'''
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()
# 10
# 10

'''


# Find  outputs (Home  work)
'''
def  f1():
	x = 20
	print(x)
	print(globals()['x'])
# End  of  the  function
f1()
# 20
# error due to global varibles are not declered

'''


# Find outputs (Home  work)
'''
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
# 40 50 60
# 10 20 30
f2()
# 100 200 300

'''


# global  keyword  demo  program (Home  work)
'''
def    f1():
	x = 20
	print(x)# 20
def   f2():
	global  x
	x = 30
	print(x)# 30
	x += 1# 31
def   f3():
	global  y
	y = 40
	print(y)# 40
	y += 1# 41
def   f4():
	x = 50
	#global  x
#  End  of  the  functions
x = 10
print(x)# 10
x += 1#11
f1()#20
print(x)#11
f2()# 30
print(x)# 31
x += 1# 32
f3()# 40
print(y)# 41
f4()# error
print(x)# 32

'''



# Find outputs (Home  work)
'''
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a)# 10
f1()# 20
	# 20
print(a)# 30

'''


# Find  outputs(Home  work)
'''
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
f1()# 10
	# 20
f2()# 30
print(a)# 30
# error due to a is not defined any where out side of the function 
'''

# Find outputs (Home  work)
'''
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
f1()# 10
f2()# 20
f3()# 30
print(a)# 40

'''

# Find outputs (Home  work)
'''
NOT UNDERSTOOD +++++++++++++++++++++++++++++++     DOUBT     +++++++++++++++++
##############################################
def  f1():
	global   a
	a = 10
	print(a)
	a = 20	
def  f2():
	print(a)------------------------------------
	a = 30
	print(a)
def  f3():
	print(a)-----------------------------------
	globals()['a'] = 40
# End  of  the  function
f1()# 10
f2()# error
f3() 
print(a)# 40

'''

#  Find  outputs (Home  work)
'''
def  f1():
        a = 10
        global  a# error becz local variable is assinged to a=10 before gobal variable is declared, we cant specify same referance to 
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()# error
print(a)# error
print(b)

'''


# Find outputs (Home  work)
'''
def  f1():
        global  a
        print(a)# 11
        a += 1# 12
def  f2():
        global  a
        print(a)# 13
        a += 1# 14
# End  of  the  function
a = 10
print(a)# 10
a += 1# 11
f1()# 11
print(a)# 12
a += 1# 13
f2()# 13
print(a)# 14

'''

# Find  outputs (Home  work)
'''
def   f1():
	a = 20
	print(a)# 20 local variable 
def  f2():
	print(a)# 11 global variable--------------------------  DOUBT  ------------
	a += 1# 12
# End of the function
a = 10
print(a)# 10
f1()# 20
a += 1# 11
f2()# 11
print(a)# 12

'''

# Find outputs (Home  work)
'''
def  f1():
	a = 20
	global   a #error
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)# 10
a += 1# 11
f1()# error we cant declare global after local declareation 
print(a)# 40

'''

#  Find   outputs
'''
def   f1():
	x = x + 5 # x = 10 + 5 => 15 
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1()# none error 
f2()# 15
print(x)# 10

'''
