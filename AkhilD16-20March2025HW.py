'''
#1.Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)

def  avg(*a):
	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
	print(sum(a))
	# End  of  the  function

print(avg(10,20 ,15,18)) #  Average  of  10 , 20 , 15  and  18
print(avg(25 ,10.8,True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
#print(avg(tpl))


Gift
2.Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)

def  concat(*a):
	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
	return (c:=' '.join(a))
	# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))	# Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Python Is A Great language
#print(concat())
print(concat('Python'))	# Python
#print(concat(1, 2, 3))

#3.Find  outputs (Home  work)

def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)	# a : 10	b : (20,30,40)
f1(50 , 60)		# a : 50	b : (60,)
f1(70)			# a : 70	b : ()
f1(a = 80)		# a : 80	b : ()
#f1(b = (10 , 20 , 30) , a = 40)	# Error....'*a' accepts only positional args and 'b' arg is unexpexted..
f1()			# a : 25	b : ()
#f1(a = 10 , (20 , 30 , 40))	# PA's following KA's
#f1(25 , b = (10 , 20 , 30))	# Error....'*a' accepts only positional args
#f1(25 , a = (10 , 20 , 30))	# Error....'a' got multiple args
f1((10 , 20 , 30) , 10 , 20 , 30)	# # a : (10,20,30)	b : (10,20,30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30) # PA's following KA's


#4.Find  outputs (Home  work)

def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)	# a : (10,20,30)	b : 40
f1(50 , b = 60)				# a : (50,)		b : 60
f1(b = 70)					# a : ()		b : 70
#f1(b = 10 , a = (20 , 30 , 40))	# Error....'a' is unexpected
#f1(b = 10 , (20 , 30 , 40))	# Error...PA's following KA's
#f1()			# Error... Value for 'b' is missing
#f1(10 , 20 , 30 , (10 , 20 , 30))	# Error....keyword only arg is missing for 'b'
#f1(10 , 20 , 30 , 40)			# Error....keyword only arg is missing for 'b'
#f1(25)							# Error....keyword only arg is missing for 'b'
f1(10 , 20 , 30 , b = (10 , 20 , 30))	# a : (10,20,30)	b : (10,20,30)

#5.Find  outputs (Home  work)

def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)	# a : 10	b : (20,30,40)	c : 50
f1(60 , 70 , c = 80)			# a : 60	b : (70,)	c : 80
f1(90 , c = 100)				# a : 90	b : ()	c : 100
#f1(a = 1 , 2 , c = 3)			# Error...PA's following KA's
#f1(1 , 2 , 3)					# Error..keyword only arg is missing for 'c'
#f1(a = 1 , b = 2 , c = 3)		# Error...unexpected arg 'b'
#f1(a = 25 , 100 , 200 , 300 , c = 35)	# Error...PA's following KA's

#6.Which  of  the  following  are  valid  ?  (Home  work)
#def   f1(*a , *b): # not valid
       # pass
def  f2(*a , b): # Valid
        pass
def  f3(a , *b): # Valid
        pass
def  f4(a , b): #valid
        pass
def    f5(a , *b , c):	# Valid
        pass
#def   f6( * , a , *b , c): # Not Valid
 #      pass
#def   f7(a , *b , c ,  /): # Not Valid.. '/' must be ahead of '*'
 #      pass

 

#7.Find  outputs  (Home  work)
def   f1(*a):
	print(a)		# ([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a))	# < class 'tuple'>
	for  x  in  a:
		print(x)	# [10,20]<alternateLine>{30,40}<alternateLine>(50,60)
		print(type(x))	# < class 'list'><alternateLine>< class 'set'> <alternateLine> < class 'tuple'>
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60)) # Function call...control moves to line 99

#8.Find  outputs  (Home  work)
def  f1(**a):
	print('Results')				# Results	
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')# Empno...25<nL>Empname...Rama Rao<nL>Salary...10000.0<nL>Gender...m
									# for f1()--> Results
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm') # Function call..control moves to line 109
f1()	 # Function call..control moves to line 109

#9.Find  outputs (Home  work)
def   f1(*a):
	print(type(a))	# <class 'tuple'>
	print(a)		# (25,10.8,'Hyd',True>
def   f2(**a):
	print(type(a))	# <class 'dict'>
	print(a)		# {'EmpNum' : 25,'EmpName' :'Sita','Salary ': 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True) # Function call....
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0) # Function Call....

#10.Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
				# for 1st f1()-->Emp Number : 25	 Emp Name : Sita	Salary : 10000.0
				# for 2nd f1()-->
def   f2(**a):
	print(a)	# for 1st f2()-->{'empno' : 25,'ename' : 'Sita','sal' : 10000.0}
				# for 2nd f2()-->{'eno' : 25,'empname' : 'Sita','salary' : 10000.0}
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)	# Function Call..
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0)	#Error..unexpected 'eno'
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)	# Function Call..
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) # Function Call...

#11.Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)	# for 1st f1()-->25
				# for 2nd f1()-->Hyd<nL>
				# for 3rd f1()-->10.8
	if   b:
		print(b)	#for 2nd f1()-->(10,20,30)
					#for 3rd f1()-->(25,'Hyd',True)
	if  c:
		print(c)	#for 3rd f1()-->{'EmpNo' : 12,'EmpName':'Rama Rao','Salary':10000.0}
# End  of  the  function
f1(25)						# Function Call
print()
f1('Hyd' , 10 , 20 , 30)	# Function Call
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0) # Function Call

#12.Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)	# a : 11
	print('b : ' , b)	# b : 40
	print('c : ' , c)	# c : 31
	print()
	# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)	# a : 50
	print('b : ' , b)	# b : 22
	print('c : ' , c)	# c : 32
	# End  of  f2()  function
c = 30
print('a : ' , a)	# a : 10
print('b : ' , b)	# b : 20
print('c : ' , c)	# c : 30
print()
a +=  1				# 10 + 1 = 11
b +=  1				# 20 + 1 = 21
c +=  1				# 30 + 1 = 31
f1()				# Function call...
a +=  1				# 11 + 1 = 12
b +=  1				# 21 + 1 = 22	
c +=  1				# 31 + 1 = 32
f2()				# Function Call..
print('Bye')		# Bye

#13.Find  outputs (Home  work)
def   f1():
	a = 20		
	print(a)	# 20
	a += 1		# 20 + 1 = 21
	#End  of  the  function
a = 10
print(a)	# 10
a += 1		# 10 + 1 = 11
f1()		# Function Call..
print(a)	# 11

#14.Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)			# 20 
	dict = globals()	
	print(dict['a'])	# 11
	a = 30
	dict['a'] = 40		#
#  End  of  f1()  function
a = 10
print(a)	# 10
a += 1		# 10 + 1 = 11
f1()		# Function Call..
print(a)	# 40

#15.Find  outputs (Home  work)
x = 10
def   f1():
	print(x)				# 10
	print(globals()['x'])	# 10
# end of the function
f1()	# Function Call..

#16.Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)				# 20
	#print(globals()['x'])	# 
# End  of  the  function
f1()	# Function Call..

#17.Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)	# 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])	# 10 20 30
	dict['a'] = 100		# GV 'a' is modified to 100
	dict['b'] = 200		# GV 'b' is modified to 200
	dict['c'] = 300		# GV 'c' is modified to 300
def  f2():
	print(a , b , c)	# 100 200 300
	# End  of  f2  function
a = 10
b = 20
c = 30
f1()	# Function Call..
f2()	# Function Call..

#18.global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)	# 20
def   f2():
	global  x
	x = 30
	print(x)	# 30
	x += 1		# 30 + 1 = 31
def   f3():
	global  y
	y = 40
	print(y)	# 40
	y += 1		# 40 + 1 = 41
def   f4():
	x = 50
	#global   x  # Error.....
	#  End  of  the  functions
x = 10
print(x)	# 10
x += 1		# 10 + 1 = 11
f1()		# Function Call...
print(x)	# 11
f2()		# Function Call...
print(x)	# 31
x += 1		# 31 + 1 =32
f3()		# Function Call...
print(y)	# 41
f4()		# Function Call...
print(x)	# 32

#19.Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)	# 20
	print(globals()['a']) # 20
	a = 30
# End of the function
a = 10
print(a)	# 10
f1()		# Function Call..
print(a)	# 30

#20.Find  outputs(Home  work)
def  f1():
	global  a
	#print(a) # Error...'a' is not defined
	a = 10
	print(globals()['a'])	# 10
	a = 20
	print(a)				# 20
	a = 30					# 'a' is modified to 30
def  f2():
	print(a)				# 30
	# End  of   f2   function
f1() # Function Call...
f2()# Function call
print(a)					# 30

#21.Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)		# 10
	a = 20			# GV 'a' is modified to 20
def  f2():
	global  a
	print(a)		# 20
	a = 30			# GV 'a' is modified to 30
def  f3():
	print(a)		# 30	
	globals()['a'] = 40	# GV 'a' is modified to 40
	# End  of  the  function
f1()	# Function Call..
f2()	# Function Call..
f3()	# Function Call..
print(a)			# 40

#22.Find outputs (Home  work)
def  f1():
	global   a	
	a = 10		# GV 'a' is initialized
	print(a)	# 10
	a = 20		#  GV 'a' is modified to 20
def  f2():
	#print(a)	# Error...
	a = 30		#  Lv 'a' is initilized
	print(a)	# 30
def  f3():
	print(a)	# 20
	globals()['a'] = 40	#  GV 'a' is modified to 40
	# End  of  the  function
f1()	# Function Call..
f2()	# Function Call..
f3()	# Function Call..
print(a)	# 40

#23.Find  outputs (Home  work)
def  f1():
        a = 10
       # global  a # Error....
        print(a)	# 10
        global  b
        b = 20
	# End  of  f1()  function
f1()	# Function Call...
#print(a)	# Error due to no GV
print(b)	# 20

#24.Find outputs (Home  work)
def  f1():
        global  a
        print(a)	# 11
        a += 1		# 11 + 1 =12
def  f2():
        global  a
        print(a)	# 13
        a += 1		# 13 + 1 = 14
# End  of  the  function
a = 10
print(a)	# 10
a += 1		# 10 + 1 = 11
f1()		# Function Call...
print(a)	# 12
a += 1		# 12 + 1 = 13	
f2()		# Function Call...
print(a)	# 14

#25.Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)	# 20
#def  f2():
	#print(a)	# Error..
	#a += 1		# Error..
	# End of the function
a = 10
print(a)	# 10
f1()		# Function Call...
a += 1		# 10 + 1 = 11
#f2()		# Function Call...
print(a)	# 11

#26.Find outputs (Home  work)
def  f1():
	a = 20
	#global   a		# Error..
	print(a)		# 20
	print(globals()['a'])	# 11
	a = 30			# LV 'a' is modified to 30
	globals()['a'] = 40 #  gV 'a' is modified to 40
	#  End  of  f1()   function
a = 10
print(a)	# 10
a += 1		# 10 + 1 =11
f1()		# Function Call...
print(a)	# 40
'''
#27.Find   outputs
#def   f1():
	# x = x + 5 # Error..
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)	# 15
# End of f2  function
x = 10
#f1()	# Function Call...
f2()	# function Call...
print(x)	#10
