#  Variable  number  of  arguments  demo  program
'''def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  Tuple  of  4  elements  is  passed  to  the  function
f1()# ()
    #<class  'tuple'>
	#0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})#([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
													#<class 'tuple'>
													#3
													
f1('Hyd')#('Hyd')
		#<class  'tuple'>
		#1
tpl = (100 , 200 , 150)
f1(tpl)#((100 , 200 , 150),)
       #<class  'tuple'>
	   #1
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka




 #  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
def  avg(*a):
	Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function

try:
	def  avg(*a):		
			return sum(a)/len(a)
			 
		
				
										
	print(avg(10 , 20 , 15 , 18)) #15.75
	print(avg(25 , 10.8 , True))#12.266666666666666
	print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))#14.26
	print(avg())
	print(avg(25))#25.0
	print(avg(3 + 4j , 5 + 6j))#(4+5j)
	tpl = (10 , 20 , 15 , 18)
	print(avg(tpl))
except :
	print('zero is not divisible it gives error')
#error not support for int and tuple

Gift
Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)
try:
	def  concat(*a):
		 return ' '.join(a)		
	
# End   of  the   function
	print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
	print(concat('Hyd', 'Is', 'Green', 'City'))
	print(concat('Python', 'Is', 'A', 'Great', 'Language'))
	print(concat(''))
	print(concat('Python'))
	print(concat(1, 2, 3))
except:
	print('elements of tuple must be strings not integers')

#Find  outputs (Home  work)
def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a:10 b:20,30,40
f1(50 , 60)#a:50 b:60
f1(70)#a:25 b:70
f1(a = 80)#error
#f1(b = (10 , 20 , 30) , a = 40)##error becoz 'b' must be positional argument
f1()#a:25 b:()
f1(a = 10 , (20 , 30 , 40))#error becoz positional argument after keyword argument
f1(25 , b = (10 , 20 , 30))#error becoz 'b' must be positional argument
f1(25 , a = (10 , 20 , 30))#error becoz keyword argument 'a' got to many values
f1((10 , 20 , 30) , 10 , 20 , 30)#a:(10 , 20 , 30) b:(10 , 20 , 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)#error becoz positional argument after keyword argument

#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)#a:(10 , 20 , 30) b:40
f1(50 , b = 60)#a:50 b:60
f1(b = 70)#a:() b:70
f1(b = 10 , a = (20 , 30 , 40))#error
f1(b = 10 , (20 , 30 , 40))#error becoz positional argument after keyword argument
f1()#error
f1(10 , 20 , 30 , (10 , 20 , 30))#error
f1(10 , 20 , 30 , 40)#error
f1(25)#error
f1(10 , 20 , 30 , b = (10 , 20 , 30))#a: (10, 20, 30)   b: (10, 20, 30)  

#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#a:10 b:(20 , 30 , 40 ) c:50
f1(60 , 70 , c = 80)#a:60 b:(70,) c:80
f1(90 , c = 100)#a:90 b:() c:100
#f1(a = 1 , 2 , c = 3)#error becoz positional argument after keyword argument
#f1(1 , 2 , 3)#error
#f1(a = 1 , b = 2 , c = 3)#error
#f1(a = 25 , 100 , 200 , 300 , c = 35)#error


# Which  of  the  following  are  valid  ?  (Home  work)
#def   f1(*a , *b):#invalid
       # pass
def  f2(*a , b):#valid
        pass
def  f3(a , *b):#valid
        pass
def  f4(a , b):#valid
        pass
def    f5(a , *b , c):#invalid
        pass
#def   f6( * , a , *b , c):#invalid
       #pass
#def   f7(a , *b , c ,  /):#invalid
      # pass
	  
	# Find  outputs  (Home  work)
def   f1(*a):
	print(a)#([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a))#<class 'tuple'>
	for  x  in  a:
		print(x)#[10,20] 
		print(type(x))#<class 'set'> 
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))

# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  #  {RollNo : 10 StudName :'Rama  Rao'}
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)#{EmpNo = 25 EmpName = 'Sita' Salary = 10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')#(AcNo : 30 , CustName : 'Kiran' , Balance : 20000.0 Gender : 'm')
disp()#{}

# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')#{Empno ... 25  Empname ...'Rama  Rao' Salary ... 10000.0  Gender... 'm'}
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()

# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))#<class 'tuple'> 
	print(a)#(25 , 10.8 , 'Hyd' , True)
def   f2(**a):
	print(type(a))#<class 'dict'>
	print(a)#{EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)#
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')#empno = 25 , ename = 'Sita' , sal = 10000.0
def   f2(**a):
	print(a)#{empno : 25 , ename : 'Sita' , sal : 10000.0}
	       #f2{eno = 25 , empname = 'Sita' , salary = 10000.0}
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0)#error
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)

# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)#a:25
print()
f1('Hyd' , 10 , 20 , 30)#a:'Hyd' b:(10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)#a:10.8 b:( 25 , 'Hyd' , True )

#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)#11
	print('b : ' , b)#40
	print('c : ' , c)#31
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)#50
	print('b : ' , b)#22
	print('c : ' , c)#32
# End  of  f2()  function
c = 30
print('a : ' , a)#10
print('b : ' , b)#20
print('c : ' , c)#30
print()
a +=  1#11
b +=  1#21
c +=  1#31
f1()
a +=  1
b +=  1#22
c +=  1#32
f2()
print('Bye')

# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)#20
	a += 1
#End  of  the  function
a = 10
print(a)#10
a += 1#11
f1()
print(a)#11

# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)#20
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)#10
a += 1#11
f1()
print(a)#40

# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()#10 10

# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	print(globals()['x'])
# End  of  the  function
f1()#20 

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

outputs--
40 50 60
10 20 30
100 200 300

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
	#global   x
#  End  of  the  functions
x = 10
print(x)
x += 1#11
f1()                    
print(x)
f2()
print(x)
x += 1#32
f3()
print(y)
f4()
print(x)

#outputs--
# 10 20 11 30 31 40 41  32
# Find outputs (Home  work)

def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a)#10 20 20 30
f1()
print(a)

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
f1()#10 20 30
f2()#
print(a)#30

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
outputs---
10 20 30 40

# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	#print(a)
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()#10 30 20 40
f2()
f3()
print(a)

#  Find  outputs (Home  work)
def  f1():
        a = 10
        #global  a
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()#10 10 20
#print(a)
print(b)

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
print(a)#
a += 1 #13
f1()
print(a)
a += 1
f2()
print(a)
outputs---
10 11 12 13 14

# Find  outputs (Home  work)
def   f1():
	a = 20 #20
	print(a)
def  f2():
	print(a)#11
	#a += 1
# End of the function
a = 10
print(a)#10
f1()
a += 1 #11
f2()
print(a)#11

otputs--
10 20 11 11

# Find outputs (Home  work)
def  f1():
	a = 20 #20
	#global   a
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)#10 40
a += 1 #11
f1()
print(a)
outputs--
10 20 11 40

#  Find   outputs
def   f1():
	x = x + 5 #15
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
#f1()
f2()
print(x)

outputs--15 10'''
