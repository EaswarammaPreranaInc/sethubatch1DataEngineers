
# 1. Variable  number  of  arguments  demo  program
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


'''
(10,20,15,18)
<class  'tuple'>
4

()
<class  'tuple'>
0

([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
class tuple 
3

((100 , 200 , 150),)
class tuple 
1



# 2. Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
def  avg(*a):
	return sum(a)/len(a) if a else 0
	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #  Average  of  10 , 20 , 15  and  18 15.75 
print(avg(25 , 10.8 , True))  # 12.266
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))#14.26
print(avg()) # 0 
print(avg(25)) #25.0
print(avg(3 + 4j , 5 + 6j)) #(4+5j)
#tpl = (10 , 20 , 15 , 18)
#print(avg(tpl))'''

'''
3. Gift
Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)
'''
def  concat(*a): 
	return ' '.join(a)
	
	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))#Hyd Is GreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))#Python Is A Great Language
print(concat())#
print(concat('Python'))#Python
#print(concat(1, 2, 3)) 

#4. *Find  outputs (Home  work)
def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) #a:10	b:(20,30,40)
f1(50 , 60) #a:50	b:(60,)
f1(70)#a:70	b:()
f1(a = 80) # a:80
#f1(b = (10 , 20 , 30) , a = 40) #error only positional arguments are permitted f1() got an unexpected keyword argument 'b'
f1() # a:25	b:()
#f1(a = 10 , (20 , 30 , 40)) #  ka before pa 
#f1(25 , b = (10 , 20 , 30)) # f1() got an unexpected keyword argument 'b'
#f1(25 , a = (10 , 20 , 30)) # f1() got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30) #a:(10,20,30) b:(10,20,30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30) # ka before pa 

# 5.Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a:(10,20,30)	b:40
f1(50 , b = 60) # a:(50,)	b:60
f1(b = 70) # a:()	b:70
# f1(b = 10 , a = (20 , 30 , 40)) #  f1() got an unexpected keyword argument 'a' only pa
#f1(b = 10 , (20 , 30 , 40)) #  positional argument follows keyword argument only pa
#f1() # missing one argument a:	b:
#f1(10 , 20 , 30 , (10 , 20 , 30)) # f1() missing 1 required keyword-only argument: 'b' 
#f1(10 , 20 , 30 , 40) #f1() missing 1 required keyword-only argument: 'b'
#f1(25)  f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , b = (10 , 20 , 30)) #  a:(10,20,30)	b:(10,20,30)  

# 6.Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a:10	b:(20,30,40)	c:50
f1(60 , 70 , c = 80) #a:60	b:70	c:80
f1(90 , c = 100) #a:90	b:()	c:100
#f1(a = 1 , 2 , c = 3)# positional argument follows keyword argument
#f1(1 , 2 , 3) #  f1() missing 1 required keyword-only argument: 'c'
#f1(a = 1 , b = 2 , c = 3) #  f1() missing 1 required keyword-only argument: 'c'
#f1(a = 25 , 100 , 200 , 300 , c = 35)# positional argument follows keyword argument

# 7. Which  of  the  following  are  valid  ?  (Home  work)
#def   f1(*a , *b): # invalid  * argument may appear only once
       # pass
def  f2(*a , b):#valid 
        pass
def  f3(a , *b): #valid
        pass
def  f4(a , b): #valid 
        pass
def    f5(a , *b , c):#valid
        pass
#def   f6( * , a , *b , c): #invalid b and a are positional arguments   * argument may appear only once
     #  pass
#def   f7(a , *b , c ,  /): # invalid  c is keyword argument / must be ahead of *
       #pass
# 8. Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60)) 
'''
([10 , 20] , {30 , 40} , (50 , 60))
class tuple
[10,20]
{30,40}
(50,60) '''

# 9. Variable  number  of  keyword  arguments  demo  program
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
Results
class dict
{RollNo:10,StudName:'Rama Rao'}

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
# 10. Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()
'''
Results
Empno ... 25
Empname...'Rama Rao'
Salary ... 10000.0
Gender ... 'm'
Results
'''  
# 11.Find  outputs (Home  work)
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
class tuple
(25 , 10.8 , 'Hyd' , True)

class dict
{'EmpNum':25 , 'EmpName': 'Sita' , 'Salary':10000.0} '''

# 12. Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) #Emp  Number  :  25   Emp  Name  : Sita  Salary  : 10000.0
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0) #error f1() got an unexpected keyword argument 'eno'
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # {'empno':25,'ename':'Sita','Sal'=10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) #{'eno':25 , 'empname': 'Sita' , 'salary': 10000.0}

# 13. Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25) #25
print() #
f1('Hyd' , 10 , 20 , 30) # 'Hyd' next line (10,20,30)
print() #
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0) # 10.8 next line (25,'Hyd',true) next line {'EmpNo':12,'EmpName:'Rama Rao',Salary:10000.0}

# 14.Find  outputs (Home  work)
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
print('a : ' , a) #a:10
print('b : ' , b) #b:20
print('c : ' , c) #c:30
print()
a +=  1 #11
b +=  1 #21
c +=  1 #31
f1() # a:11 nl b:40 nl c:31
a +=  1 #12
b +=  1 #22
c +=  1 #32
f2() # a:50 nl b:22 c:32
print('Bye') #bye 

# 15.Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a) #10
a += 1 #11
f1() #20
print(a) #11

# 16. Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a) #10
a += 1 #11
f1() #20 nl 11
print(a) #40 
# 17. Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1() #10 nl 10
# 18. Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	#print(globals()['x']) #error 
# End  of  the  function
f1() # 20 
#19. Find outputs (Home  work)
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
f1() # 40 50 60 nl 10 20 30
f2() # 100  200  300 
# 20. global  keyword  demo  program (Home  work)
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
print(x) #10
x += 1 #11
f1() # 20
print(x) #11
f2() # 30 
print(x) #31
x += 1 #32
f3() #40
print(y)#41
f4() 
print(x) #32

# 21. Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10 
print(a) #10
f1() #20 nl 20 
print(a) #30
# 22. Find  outputs(Home  work)
def  f1():
	global  a
	#print(a) #error printed before declaration 
	a = 10
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1() # 10  20
f2() #30
print(a) #30 

# 23.Find  outputs (Home  work)
def  f1():
        a = 10
        #global  a # already local variable is defined we cant treat it as local 
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1() # 10
# print(a) #error name 'a' is not defined  
print(b) #20  

# 24 Find outputs (Home  work)
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
print(a) #10
a += 1 #11
f1() #11
print(a) # 12
a += 1 #13
f2() # 13
print(a) #14

# 25 Find  outputs (Home  work)
def  f1():
        a = 10
        #global  a #error
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1() #10
#print(a) #error!
print(b) #20

# 26.Find outputs (Home  work)
def  f1():
        global  a
        print(a)
        a += 1 #12
def  f2():
        global  a
        print(a)
        a += 1
# End  of  the  function
a = 10 
print(a) #10
a += 1 #11
f1() #11
print(a) #12
a += 1 #13
f2() #13
print(a) #14 

# 27.Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
def  f2():
	#print(a) # error cant print before declaration of local variable 
	#a += 1 # a is not defined 
	pass
# End of the function
a = 10
print(a) #10
f1() #20
a += 1 #11
f2() #
print(a) #11 

# 28..Find outputs (Home  work)
def  f1():
	a = 20
	#global   a #error 
	print(a) #20
	print(globals()['a']) #10
	a = 30 
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a) #10
a += 1 #11
f1() # 20 11  
print(a) #40 

#  29. Find   outputs
def   f1():
	# x = x + 5 x is local variable not defined 
	pass
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1() 
f2() #15
print(x) #10
