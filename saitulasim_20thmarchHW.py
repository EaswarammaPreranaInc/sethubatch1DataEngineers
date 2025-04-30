# Variable  number  of  arguments  demo  program.

def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)            
f1()                              
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) 
f1('Hyd')                        
tpl = (100 , 200 , 150)
f1(tpl)                            
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  cannot be  'KA'


# Write  a  function  to  determine  average  of  arguments  passed  from  function  call 
def  avg(*a):
		return sum(a)/len(a) if a else 0

print(avg(10 , 20 , 15 , 18)) 
print(avg(25 , 10.8 , True))   
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) 
print(avg())         
print(avg(25))         
print(avg(3 + 4j , 5 + 6j)) 
tpl = (10 , 20 , 15 , 18)
#print(avg(tpl))       #error because tuple is not unpacked


#Write  a  function  to  concatenate  strings  passed  from  the  function  call
#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call

def  concat(*a):
	return ' '.join(str(i) for i in a)  
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City')) #Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) #Python Is A Great Language
print(concat())         #Empty 
print(concat('Python'))  #Python
print(concat(1, 2, 3))   # 1 2 3 


#Find  outputs

def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)  #a : 10             b  :  (20, 30, 40)
f1(50 , 60)            #a : 50             b  :  (60,)
f1(70)                 #a : 70             b  :  ()
f1(a = 80)             #a : 80             b  :  ()
#f1(b = (10 , 20 , 30) , a = 40)  #error - 'b' must be positional argument but keyword argument is given
f1()                   #a : 25             b  :  ()
#f1(a = 10 , (20 , 30 , 40))   #error - keyword arguments must be given after positional arguments
#f1(25 , b = (10 , 20 , 30))   #error - 'b' must be positional argument but keyword argument is given
#f1(25 , a = (10 , 20 , 30))    #error - a takes 25 as argument and also have keyword argument which has multiple values for a 
f1((10 , 20 , 30) , 10 , 20 , 30) #a : (10, 20, 30)           b  :  (10, 20, 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)  #error - keyword arguments must be given after positional arguments

#Find  outputs 

def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) #a  :  (10, 20, 30)         b  :  40
f1(50 , b = 60)           #a  :  (50,)        b  :  60
f1(b = 70)                #a  :  ()           b  :  70
#f1(b = 10 , a = (20 , 30 , 40)) #error - 'a' must be positional argument
#f1(b = 10 , (20 , 30 , 40))     #error - keyword arguments must be given after positional arguments
#f1()                            #error - 'b' value is not given
#f1(10 , 20 , 30 , (10 , 20 , 30)) #error - 'b' value is not given
#f1(10 , 20 , 30 , 40)              #error - 'b' value is not given
#f1(25)                             #error - 'b' value is not given
f1(10 , 20 , 30 , b = (10 , 20 , 30)) #a  :  (10, 20, 30)         b  :  (10, 20, 30) 


#Find  outputs 

def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) #a  :  10          b  :  (20, 30, 40)      c  :  50
f1(60 , 70 , c = 80) #a  :  60          b  :  (70,)     c  :  80
f1(90 , c = 100) #a  :  90          b  :  ()        c  :  100
#f1(a = 1 , 2 , c = 3)  #error - keyword arguments must be given after positional arguments
#f1(1 , 2 , 3) #error - no value is assigned to c
#f1(a = 1 , b = 2 , c = 3) #error - 'b' must be positional argument
#f1(a = 25 , 100 , 200 , 300 , c = 35) #error - keyword arguments must be given after positional arguments



# Which  of  the  following  are  valid  

#def   f1(*a , *b):  #error -  multiple * arguments
 #       pass
def  f2(*a , b): #VALID
        pass
def  f3(a , *b): #VALID
        pass
def  f4(a , b): #VALID
        pass
def    f5(a , *b , c): #VALID
        pass
#def   f6( * , a , *b , c): #error-all arguments must be keyword arguments because of * . but *b is positional argument
#      pass
#def   f7(a , *b , c ,  /): #error - 'c' must be keyword argument but before '/' argument every argument must be positional
#      pass


# Find  outputs  

def   f1(*a):
	print(a) #([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a)) #<class 'tuple'>
	for  x  in  a:  
		print(x)       # [10,20]  <class 'list'>  <\n> {30,40}  <class 'set'>   <\n>  (50,60) <class 'tuple'>
		print(type(x))  
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))



# Variable  number  of  keyword  arguments  demo  program

def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  # 
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

''' output
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
{} '''



 # Find  outputs 

def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()

 ''' output 
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results '''


# Find  outputs

def   f1(*a):
	print(type(a)) #<class 'tuple'>
	print(a)       #(25 , 10.8 , 'Hyd' , True)
def   f2(**a):
	print(type(a)) #class 'dict'>
	print(a)        #{'EmpNum' : 25 , 'EmpName' =  'Sita' , 'Salary' = 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)



#Find  outputs 

def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) #Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0) #error - due to eno keyword
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)    #{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) #{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}



# Find  outputs  

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

''' output
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0} '''



#Find  outputs 

a = 10
def   f1():
	b = 40
	print('a : ' , a) #a :  11
	print('b : ' , b) #b :  40
	print('c : ' , c) #c :  31
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a) #a :  50
	print('b : ' , b) #b :  22
	print('c : ' , c) #c :  50
# End  of  f2()  function
c = 30
print('a : ' , a) #a :  10
print('b : ' , b) #b :  20
print('c : ' , c) #c :  32
print()            
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye') #Bye

''' output
a :  10
b :  20
c :  30

a :  11
b :  40
c :  31

a :  50
b :  22
c :  32
Bye '''



# Find  outputs 

def   f1():
	a = 20
	print(a) #20
	a += 1
#End  of  the  function
a = 10
print(a) #10
a += 1
f1()
print(a) #11

'''output
10
20
11 '''


# Find  outputs 

def   f1():
	a = 20
	print(a)           #20
	dict = globals()
	print(dict['a'])   #11
	a = 30
	dict['a'] = 40     
#  End  of  f1()  function
a = 10
print(a) #10
a += 1
f1()
print(a) #40

'''output
10
20
11
40 '''


# Find  outputs 

x = 10
def   f1():
	print(x)  #10
	print(globals()['x']) # 10
# end of the function
f1()

'''output: 10
           10 '''


# Find  outputs 

def  f1():
	x = 20
	print(x) #20
	print(globals()['x']) #error- global variable x is not there
# End  of  the  function
f1()

'''output: 20
           10 '''



# Find outputs 

def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c) # 40 50 60
	dict = globals() 
	print(dict['a'] , dict['b'] , dict['c']) #10 20 30
	dict['a'] = 100  # updates value of a to 100
	dict['b'] = 200  # updates value of b to 200
	dict['c'] = 300  # updates value of c to 300
def  f2():
	print(a , b , c) # 100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()

''' output :40 50 60
            10 20 30
            100 200 300 '''



# global  keyword  demo  program 

def    f1():
	x = 20
	print(x) #20
def   f2():
	global  x
	x = 30
	print(x) # 30
	x += 1
def   f3():
	global  y
	y = 40
	print(y) #40
	y += 1
def   f4():
	x = 50
	#global   x  #error - x value is not assigned after global declaration
#  End  of  the  functions
x = 10
print(x) #10
x += 1
f1()
print(x) #11
f2()
print(x) #31
x += 1
f3()
print(y) #41
f4()
print(x) #32

''' output
10
20
11
30
31
40
41
32 '''


# Find outputs 
def  f1():
	global  a
	a = 20
	print(a) #20
	print(globals()['a']) #20
	a = 30
# End of the function
a = 10
print(a) #10
f1()
print(a) #30

'''output
10
20
20
30 '''


# Find  outputs
def  f1():
	global  a
	#print(a)    #error - a does not have any value  
	a = 10
	print(globals()['a']) #10
	a = 20
	print(a) #20
	a = 30
def  f2():
	print(a) #30
# End  of   f2   function
f1()
f2() 
print(a) #30

'''output
10
20
30
30 '''



# Find outputs 
def  f1():
	global   a
	a = 10
	print(a)      #10
	a = 20
def  f2():
	global  a 
	print(a)     #20
	a = 30
def  f3():
	print(a)      #30
	globals()['a'] = 40 
# End  of  the  function
f1()
f2()
f3()
print(a)         #40



# Find outputs 
def  f1():
	global   a
	a = 10
	print(a) #10
	a = 20
def  f2():
	#print(a) #error - local variable a is not declared
	a = 30
	print(a) #30
def  f3():
	print(a) #20
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a) #40

''' output
10
30
20
40 '''



#Find  outputs 
def  f1():
        a = 10
        #global  a #error - already a is declared as local variable
        print(a)  #10
        global  b
        b = 20
# End  of  f1()  function
f1()
#print(a) #error - a is not defined
print(b)      #20



# Find outputs 
def  f1():
        global  a
        print(a) #11
        a += 1
def  f2():
        global  a
        print(a) #13
        a += 1
# End  of  the  function
a = 10
print(a) #10
a += 1
f1()
print(a) #12
a += 1
f2()
print(a) #14

'''output
10
11
12
13
14 '''



# Find  outputs 
def   f1():
	a = 20
	print(a) #20
def  f2():
	print(a) #11
	#a += 1   # error - local variable 'a' is not declared
# End of the function
a = 10
print(a) #10
f1()
a += 1
f2()
print(a) #11

''' output
10
20
11
11 '''



# Find outputs
def  f1():
	a = 20
	#global   a # error-local variable is already declared
	print(a)   #20
	print(globals()['a']) #11
	a = 30
	globals()['a'] = 40  #updates global value to 40
#  End  of  f1()   function
a = 10
print(a) #10
a += 1
f1()
print(a) #40

''' output
10
20
11
40 '''



#  Find   outputs
#def   f1():
#	x = x + 5 #error - local variable x is not defined
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)    #15
# End of f2  function
x = 10
#f1() error in f1()
f2()
print(x)    #10
