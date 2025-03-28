# Find outputs  (Homework)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')  # Begin
x = f1()  # x=None
print(x)  # Hyd <nextline> Sec <nextline> Cyb <nextline> None
print(type(x))  # <class 'NoneType'>
print('End')  # End

'''    OUTPUT
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End

'''


#  Gift
# Find  outputs  (Homework)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()  # x=(10,20,30)
print(x)  # (10,20,30)
print(type(x))  # <class 'tuple'>
a , b , c =  f1()
print(a)  # 10
print(b)  # 20
print(c)  # 30
print('for  loop')  # for loop
for  k   in  f1():
	print(k)  # 10 <nextline> 20 <nextline> 30

'''   OUTPUT
(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30

'''


# Find  outputs
def    f1():
        return  10
        return  20  # it is skkiped due to return 10
        return  30  # it is skipped due to return 10
# End  of  the  function
print('Begin')  # Begin
x = f1()  # x=10
print(x)  # 10
print('End')  # End
# return 100  # Error because it is in outside the function

'''    OUTPUT
Begin
10
End

'''


#  Find  outputs
# f1()  # Error function call before function definition
def   f1():
        print('Hello')
print(f1())  # Hello <nextline> None
print(f1)  # Type and address of f1 function

'''  OUTPUT 
Hello
None
<function f1 at 0x0000019EE96B3E20>

'''


# Find  outputs  (Homework)
print('Hello')  # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')  # Hi
print(f1())  # fl function <nextline> None
print(f1)  # type and address of f1 function
print('Bye')  # Bye

'''   OUTPUT
Hello
Hi
f1  function
None
<function f1 at 0x0000025666EB3E20>
Bye
'''



#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')  # Begin
print(type(f1))  # <class 'function'>
print(id(f1))  # Address of the f1 function
print('End')  # End

'''   OUTPUT
Begin
<class 'function'>
2553711031728
End

'''


# Find  outputs (Homework)
def  f1():  # Discarded because another function is defined with same name
	print('No-argument  function')
def  f1(x):  # Discarded because another function is defined with same name
	print('Single  argument  function  : ' , x)
def  f1(x , y):  # Discarded because another function is defined with same name
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):   # It is executed because it is the last function
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)  # Three argument function :10 <space> 20 <space> 30
# f1(40 ,50)  # Error because 1 required positional argument 'z' is missing
# f1(60)   # Error because 2 required positional argument 'y','z' is missing
# f1()   # Error because 3 required positional argument 'x','y','z' is missing

'''    OUTPUT
Three  argument  function :  10 20 30

'''



# Modify  following  program  such  that  every  function  should  be  executed
def  f1():  # call the function before another function is defined with same name
	print('No-argument  function')
f1()  # No-argument function
def  f1(x):  # call the function before another function is defined with same name
	print('Single  argument  function  : ' , x)
f1(60)  # Single argument function : 60
def  f1(x , y):  # call the function before another function is defined with same name
	print('Two  argument  function : ',x , y)
f1(40,50)  # Two argument function : 40 <space> 50
def  f1(x , y , z):  # call the function before another function is defined with same name
	print('Three  argument  function :',x,y,z)
f1(10,20,30)  # Three argument function :10 <space> 20 <space> 30

'''    OUTPUT
No-argument  function
Single  argument  function  :  60
Two  argument  function :  40 50
Three  argument  function : 10 20 30

'''


# Find  outputs  (Homework)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)  # print in correct because the order is same as the order of formal parameters exsist
disp('Sita',20000.0,35)  # print but leads to incorrect results because it is not same order as the order of formal parameters exsist

'''   OUTPUT
Emp  Number  :  25 	  Emp Name  :  Rama  Rao 	  Salary  :  10000.0
Emp  Number  :  Sita 	  Emp Name  :  20000.0 	  Salary  :  35

'''


# Find  outputs  (Homework)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')  # a : 'Cyb' <tab> b : 'Sec' <tab> c : 'Hyd'
f1(c = 3 + 4j , a = True , b = None)  # a : True <tab> b : None <tab> c : 3+4j
f1(25 , c = 10.8 , b = 'Hyd')  # a : 25 <tab> b : 'Hyd' <tab> c : 10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed for 'c'




# Find  outputs (Homework)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)  # print in correct order
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)  # prints in correct order because they are keyword arguments
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x,y,z)  # x : 'Rama Rao' y : 30000.0 z : 20

'''   OUTPUT
Emp  Number :   25  	  Emp  Name : Rama Rao         	  Salary : 10000.0
Emp  Number :   35  	  Emp  Name : Sita             	  Salary : 20000.0
Emp  Number : Rama  Rao  	  Emp  Name :         30000.0  	  Salary : 20

'''


#  Gift
# Find  outputs (Homework)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))  # 23
print(f1(*[6 , 7 , 8]))  # 62
# print(f1([6 , 7 , 8]))  # Error :  Args are not passed for b and c
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))  # 16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))  # 14
# print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))  # Error : Args are not passed for 'b' and 'c'
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})  # {'c': 2, 'b': 4, 'a': 6}
# print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))  # Error : Arg 'x' does not exist

'''   OUTPUT
23
62
16
14
{'c': 2, 'b': 4, 'a': 6}

'''


# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
# print(sorted(reverse = True , a))  # Error because keyword argument is before the positional argument
# print(sorted(a , rev = True))  # Error because there is no argumrnt rec in sorted function
# print(25 , 10.8 , 'Hyd' , separator = '\t')  # Error because there is no argument seperator
# print(25 , 10.8 , 'Hyd' , endofline = '\t')  # Error because there is no argument endofline
# print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')  # Error because once keyword argument permitted then there is no permit to positional arguments



