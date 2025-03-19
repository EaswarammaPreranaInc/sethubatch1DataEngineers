# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') # Begin
x = f1() 
print(x)# Hyd <nextline> Sec <nextline> Cyb
print(type(x))# <class 'function'>
print('End') # End

# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x) # (10,20,30)
print(type(x)) #<class 'function'>
a , b , c =  f1()
print(a)#10
print(b)#20
print(c)#30
print('for  loop') # for loop
for  k   in   f1():
	print(k) #10 <next line> 20 <next line> 30


# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')#Begin
x = f1()
print(x) # 10
print('End')#End
#return   100 # return always inside the function
#  Find  outputs
f1()
def   f1():
        print('Hello') # Hello
print(f1())# None
print(f1)# # function f1  and 0x008357912

# Find  outputs  (Home  work)
print('Hello')# Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')# Hi
print(f1())# f1  function
print(f1)# function f1  and 0x00835791

print('Bye') #Bye

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') #Begin
print(type(f1))# <class 'function'>
print(id(f1))# 293679032580
print('End') #End

#Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)# Three  argument  function : 10  20  30
#f1(40 , 50) # missing 1 arguments
#f1(60) #missing 2 arguments
#f1()#missing 3 arguments

# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) # Emp  Number : 25 <tab> Emp  Name : Rama Rao <tab> Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Emp  Number : 35 <tab> Emp  Name : Sita  <tab> Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) #Emp  Number : Rama Rao <tab> Emp  Name : 30000.0   <tab>  Salary : 20

# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a : Hyd  <tab>  b : Sec <tab>  c : Cyb
f1(c = 3 + 4j , a = True , b = None) # a :True <tab> b : None <tab> c : 3 + 4j
f1(25 , c = 10.8 , b = 'Hyd')# a  :  25 <tab> b  :  Hyd <tab> c :  10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  positional arguments after key arguments
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'

# Write   a  function  to  test  a  number  is  prime  (or)  not.
def prime(x):
    b=x//2
    for i in range(2,b):
        if x%i==0:
            print(i-2)
            return False   
    return True

x=int(input("Enter a number : "))
a=prime(x)
print(a)

# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # 23
print(f1(*[6 , 7 , 8])) # 62
#print(f1([6 , 7 , 8])) # error ,2 arguments are missing
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) # 14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))# error ,2 arguments are missing
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})# {'c': 2, 'b': 4, 'a': 6}
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))# error , due to x argument

# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a)) #error positional argument a  after key argument
#print(sorted(a , rev = True)) # error,there is no argument rev
#print(25 , 10.8 , 'Hyd' , separator = '\t')# error,there is no argument Separator
#print(25 , 10.8 , 'Hyd' , endofline = '\t')# error,there is no argument endofline
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')# error positional arguments 10.8 and "hyd" after key argument
