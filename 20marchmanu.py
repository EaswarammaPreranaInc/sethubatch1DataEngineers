'''
4)find  outputs (Home  work)

def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)# a : 10             b  :  (20, 30, 40)
f1(50 , 60) # a : 50             b  :  (60,)
f1(70) # a : 70             b  :  ()
f1(a = 80) # a : 80             b  :  ()
#f1(b = (10 , 20 , 30) , a = 40)# Error due to 'b' should be positional arguments
f1()# a : 25             b  :  ()
#f1(a = 10 , (20 , 30 , 40)) # Error due to positional argument follows keyword argument
#f1(25 , b = (10 , 20 , 30)) # Error due to 'b' should be postional arguments
#f1(25 , a = (10 , 20 , 30))# Error due to f1() got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30) #a : (10, 20, 30)           b  :  (10, 20, 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30) # Error due to  positional argument follows keyword argument

#2) Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  Tuple  of  4  elements  is  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka

outputs
--------
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

#3) Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
def  avg(*a):
	return sum(a)/len(a)  if a else 0 #Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #  Average  of  10 , 20 , 15  and  18 is 15.75
print(avg(25 , 10.8 , True))  #  Average  of  25 , 10.8   and  True is 12.266666666666666
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) #  Average  of 10.8 , 20.6 , 15.2 , 14.9 and 9.8 is 14.26
print(avg())
print(avg(25)) #  Average  of 25.0 
print(avg(3 + 4j , 5 + 6j)) #  Average  ( 3 + 4j , 5 + 6j) is (4+5j)
tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) # Error due to Tuple bcz it contains number of elements we cannot find average.

#4)Gift
Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)

def  concat(*a):
	return ' '.join(a) # Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City')) # Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Python Is A Great Language
print(concat()) # Empty space we get due to empty string.
print(concat('Python')) # python
#print(concat(1, 2, 3)) # Error due to tuple of 3 elements.

#5)#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a  :  (10, 20, 30)         b  :  40
f1(50 , b = 60) # a  :  (50,)        b  :  60
f1(b = 70) # a  :  ()           b  :  70
#f1(b = 10 , a = (20 , 30 , 40)) #Error due to 'a' should be positional arguments
#f1(b = 10 , (20 , 30 , 40)) # Error due to positional argument follows keyword argument
#f1() # #Error due to there is no value for 'b'.         
#f1(10 , 20 , 30 , (10 , 20 , 30)) #Error due to there is no value for 'b' , it takes total value for 'a'
#f1(10 , 20 , 30 , 40)  #Error due to there is no value for 'b' , it takes total value for 'a'
#f1(25)  #Error due to there is no value for 'b' , it takes total value for 'a'
f1(10 , 20 , 30 , b = (10 , 20 , 30)) # a  :  (10, 20, 30)         b  :  (10, 20, 30)

#6)Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a  :  10          b  :  (20, 30, 40)      c  :  50
f1(60 , 70 , c = 80) # a  :  60          b  :  (70,)     c  :  80
f1(90 , c = 100) # a  :  90          b  :  ()        c  :  100
#f1(a = 1 , 2 , c = 3) # Error due to positional argument follows keyword argument
#f1(1 , 2 , 3)  #Error due to there is no value for 'c' , it takes total value for 'a' and 'b'.
#f1(a = 1 , b = 2 , c = 3) # Error due to 'b' should be positional arguments.
#f1(a = 25 , 100 , 200 , 300 , c = 35)  # Error due to positional argument follows keyword argument

Note: before Star(*) argument compulsorly we have to write "postional argument" and after (*) arguments anything it should be KA (or) PA
------

#7)Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b): # invalid due to 2 * arguments
        pass
def  f2(*a , b): # Valid
        pass
def  f3(a , *b): # valid
        pass
def  f4(a , b): # valid
        pass
def    f5(a , *b , c): # Valid
        pass
def   f6( * , a , *b , c): # Invalid 
       pass
def   f7(a , *b , c ,  /): # Invalid "ambigious condition"
       pass

#8)Find  outputs  (Home  work)
def   f1(*a):
	print(a)  # ([10, 20], {40, 30}, (50, 60))
	print(type(a))  # <class 'tuple'>
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))

outputs:
--------
Iterations of 'x'

1.[10, 20]
<class 'list'>
2.{40, 30}
<class 'set'>
3.(50, 60)
<class 'tuple'>

#9)Variable  number  of  keyword  arguments  demo  program
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

output:
-------
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


#10) Find  outputs  (Home  work)
def  f1(**a):
	print('Results') # Results
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()

output:
--------
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results

#11)Find  outputs (Home  work)
def   f1(*a):
	print(type(a)) # <class 'tuple'>
	print(a) # (25, 10.8, 'Hyd', True)
def   f2(**a):
	print(type(a)) # <class 'dict'>
	print(a) # {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print() # Empty space 
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

#12) Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # Error due to f1() got an  keyword argument 'eno' instead of 'empno'
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) # {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}

#13)Find  outputs   (Home  work)
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

outputs
---------
25
empty space
empty space
Hyd
(10, 20, 30)
empty space
10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}


#14)Find  outputs (Home  work)
a = 10 # ---GV
def   f1():
	b = 40
	print('a : ' , a) # 11
	print('b : ' , b) # 40
	print('c : ' , c) # 31
	print() # empty space
# End  of  f1()  function
b = 20 # ---GV
def    f2():
	a = 50
	print('a : ' , a) # 50
	print('b : ' , b) # 22
	print('c : ' , c) #32
# End  of  f2()  function
c = 30 #---GV
print('a : ' , a) # 10
print('b : ' , b)# 20
print('c : ' , c) # 30
print()
a +=  1 # 11 , GV  incremented by '1'
b +=  1 # 21 , GV  incremented by '1'
c +=  1 # 31 , GV  incremented by '1'
f1() # f1() calling
a +=  1 # 12 , GV  incremented by '1'
b +=  1 # 22 , GV  incremented by '1'
c +=  1 # 32 , GV  incremented by '1'
f2() # f2() calling
print('Bye') # Bye


#15)Find  outputs (Home  work)
def   f1():
	a = 20 # ---LV
	print(a) # 20
	a += 1 # 21
#End  of  the  function
a = 10 # --- GV
print(a) # 10
a += 1 # 11
f1() # f1() calling
print(a) # 11 ,GV  incremented by '1'


#16)Find  outputs  (Home  work)
def   f1():
	a = 20 # --- LV
	print(a) # 20
	dict = globals() # Treat LV as GV
	print(dict['a']) # 20
	a = 30
	dict['a'] = 40 # modified LV Value '30' to 40
#  End  of  f1()  function
a = 10 # ---GV
print(a) # 10
a += 1 # 11 , GV  incremented by '1'
f1() # f1 () calling
print(a) # 40


#17)Find  outputs (Home  work)
x = 10 # ---GV
def   f1():
	print(x) # 10
	print(globals()['x']) # 10---- LV is created and reurns value of GV
# end of the function
f1()

#18) Find  outputs (Home  work)
def  f1():
	x = 20 #---- LV
	print(x) # 20
	print(globals()['x']) # Error due to we have alredy LV so no need of creating again LV
# End  of  the  function
f1()

#19)Find outputs (Home  work)
def  f1():
	a = 40 # --LV
	b = 50 # --LV
	c = 60 # --LV
	print(a , b , c) # 40 50 60
	dict = globals() # assigns the current global symbol table to the variable dict. 
	print(dict['a'] , dict['b'] , dict['c']) # 10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c) # 100 200 300 --- f2() uses modified GV's bcz f2() has no LV
# End  of  f2  function
a = 10 # --GV
b = 20 # --GV
c = 30 # --GV
f1() # f1 calling
f2() 

#20)global  keyword  demo  program (Home  work)
def    f1():
	x = 20 # ---LV
	print(x) # 20
def   f2():
	global  x # uses GV 
	x = 30 # modified GV to '30'
	print(x) # 30
	x += 1 # 31---GV incremented by '1'
def   f3():
	global  y #  uses GV
	y = 40 # modified GV to '40'
	print(y) # 40
	y += 1 # 41---GV incremented by '1'
#def   f4():
	#x = 50 # there is a LV here
	#global   x # Error due to LV is already present no need to create.
#  End  of  the  functions
x = 10 # ---GV
print(x) # 10
x += 1 # 11---- GV incremented by '1'
f1() # f1() calling
print(x) #11
f2() # f2() calling
print(x) # 31
x += 1 # 32---GV incremented by '1'
f3() # f3() calling
print(y)
#f4() # Error due to global'x'.
print(x) # 32

#21)Find outputs (Home  work)
def  f1():
	global  a # uses  GV 'a' value
	a = 20 #  modifies  GV 'a' value to 20
	print(a) # 20
	print(globals()['a']) # 20
	a = 30 #  modifies  GV 'a' value to 30
# End of the function
a = 10 # ---GV
print(a) # 10
f1() # f1() calling
print(a) # 30

#22) Find  outputs(Home  work)
def  f1():
	global  a
	#print(a) # Error bcz there is no GV
	#a = 10 # ---LV
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a) # Error bcz there is no GV
# End  of   f2   function
#f1() # f1() Calling
#f2()
#print(a) Error bcz there is no GV

#23)Find outputs (Home  work)
def  f1():
	global   a # f1() requests 'a' is treated as a GV 
	a = 10 # GV created
	print(a) # 10
	a = 20 # GV modified to value 20
def  f2():
	global  a # f2() requests 'a' is treated as a GV
	print(a) # 20
	a = 30 # GV modified to value 30
def  f3():
	print(a) # 30
	globals()['a'] = 40 # GV modified to value 40
# End  of  the  function
f1() # f1() calling
f2() # f1() calling
f3() # f1() calling
print(a) # 40

#24) Find outputs (Home  work)
def  f1():
	global   a #  f1() requests 'a' is treated as a GV
	a = 10  # GV created with a value of 10
	print(a) # 10
	a = 20 # GV modified to value 20
#def  f2():
	#print(a) # Error due to no LV
	a = 30 # GV modified to value 30
	print(a) # 30
def  f3():
	print(a) # 30
	globals()['a'] = 40 # GV modified to value 40
# End  of  the  function
f1() # f1() calling
#f2() # f2() calling
f3() # f3() calling
print(a) # 40

#24) Find  outputs (Home  work)
def  f1():
        a = 10 # ---LV
       # global  a # Error due to alredy there is a LV no need to create again LV
        #print(a) # Error due to no GV
        global  b # creating LV 'b'
        b = 20
# End  of  f1()  function
f1() # f1() calling
#print(a) # Error due to no GV
print(b) # 20

#25)Find outputs (Home  work)
def  f1():
        global  a # f1() requesting 'a' is treated as a LV
        print(a) # 11
        a += 1 # 12------ GV incremented by '1'
def  f2():
        global  a # f2() requesting 'a' is treated as a LV
        print(a) # 13
        a += 1 # 14------GV incremented by '1'
# End  of  the  function
a = 10 # ---Gv
print(a) # 10 
a += 1 # 11----- GV incremented by '1'
f1() # f1 () calling
print(a) # 12
a += 1 # 13 ----- GV incremented by '1'
f2() #f2() calling
print(a) # 14

#26) Find  outputs (Home  work)
def   f1():
	a = 20 # ----LV
	print(a) # 20
def  f2():
	print(a) # 11 ---here used f2() GV a=11
	a += 1 # 12----GV incremented by '1'
# End of the function
a = 10 #---GV
print(a) # 10
f1() # f1() calling
a += 1 # 11-----GV incremented by '1'
#f2() # f2() calling
print(a) # 11

Note:- If the GV and LV has denoted by same names LV has highest priority than GV.
--------

#27) Find outputs (Home  work)
def  f1():
	a = 20 # --- LV
	#global   a # Error bcz already have a LV no need to create again LV
	print(a) # 20
	print(globals()['a']) # 11 her prints GV  incremented by '1'.
	a = 30 # nothing happen here if we write (or) not write 
	globals()['a'] = 40 # Gv modified to 40
#  End  of  f1()   function
a = 10 #----GV
print(a) # 10
a += 1 # 11-----GV incremented by '1'
f1() # f1() calling
print(a) # 40

#28) Find   outputs
def   f1():
	x = x + 5 # Error there is no value for 'x' than how can be added 5.
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5 # here 'x' value is taken from GV than added 5 
	print(x) # 15
# End of f2  function
x = 10 #--- GV
#f1() # f1() calling
f2() # f2() calling
print(x) # 10

21- 03 -2025
------------
#1)Find  outputs  (Home  work)

def  change(b):
	b . append(25) # add '25' at the end of the list
	b[2] = 17 # index '2' is replaced with 17
	del  b[1] # delete the index '1' i.e, 20 
# End  of  the  function
a = [10 , 20 , 15 , 18] #---GV
print(a) # [10 , 20 , 15 , 18]
change(a)
print(a) # [10 , 17 , 18, 25]

#2) Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b) # [50, 60, 70, 80]
# End  of  the  function
a = [10 , 20 , 30 , 40] #----GV
print(a) # [10, 20, 30, 40]
change(a)
print(a) # [10, 20, 30, 40]

#3) Find  outputs  (Home  work)
def   f1(x):
	x = 20 #---- LV
	print(x) # 20
# End  of   the   function
x = 10 #----GV
print(x) # 10
f1(x) # f1(x) calling
print(x) # 10
'''
#4)Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25 # Error due to tuple with only one element there is index '2' here
#end  of  the  function
a = (10 , 20 , 15 , 18) #----GV
print(a) # (10, 20, 15, 18)
#f1(a) # f1(a) calling
print(a) # (10, 20, 15, 18)






































