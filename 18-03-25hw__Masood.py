#  return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')
x =  f1()
print(x)
print('End')

'''
OUTPUT:
Begin
f1  function
25
End
'''




# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
	
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')

'''
OUTPUT:
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End
'''




# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()             #(10,20,30)
print(x)             #(10,20,30)
print(type(x))       #<class 'tuple'>
a , b , c =  f1()
print(a)             #10
print(b)             #20
print(c)             #30
print('for  loop')   #for loop
for  k   in   f1():
	print(k)         #10 <nextline> 20 <nextline> 30
'''
OUTPUT:
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
        return  20
        return  30
# End  of  the  function
print('Begin')  #Begin
x = f1()
print(x)     #10
print('End') #End
#return   100
'''
OUTPUT:
Begin
10
End
'''




#  Find  outputs
f1()
def   f1():
        print('Hello')
	
print(f1())
print(f1)     
'''
OUTPUT:
Hello
None
<function f1 at 0x00000132E69C1440>
'''




# Find  outputs  (Home  work)
print('Hello') #Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')  #Hi
print(f1())  # prints f1 function and return None
print(f1)    #<function f1 at 0x00000132E69C1440>
print('Bye') #Bye

'''
OUTPUT:
Hello
Hi
f1  function
None
<function f1 at 0x000001E94A43F060>
Bye
'''



#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')
'''
OUTPUT:
Begin
<class 'function'>
2474857862208
End
'''




# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
#f1(40 , 50) # f1() missing 1 required positional argument: 'z'
#f1(60)       #f1() missing 2 required positional arguments: 'y' and 'z'
#f1()          #f1() missing 3 required positional arguments: 'x', 'y', and 'z'
'''
OUTPUT:
Three  argument  function :  10 20 30
'''



# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
x=f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
x=f1(10)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
x=f1(10,20)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
x=f1(10,20,30)
'''
OUTPUT:
End
Three  argument  function :  10 20 30
No-argument  function
Single  argument  function  :  10
Two  argument  function :  10 20
Three  argument  function :  10 20 30
'''



# Write   a  function  to  test  a  number  is  prime  (or)  not.

def   prime(n):
	if n<=1:
		return "please enter valid input"
	for i in range(2,int(n/2)+1):
		if n%i==0:
			print(i-1)
			return "composite number"
	else:
		print(i-1)
		return "prime number"
	
n=int(input("enter input:"))
print(prime(n))

'''
OUTPUT:
enter input:25
composite number
enter input:7
prime number
'''




# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)
'''
OUTPUT:
Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0
Emp  Number  :  Sita      Emp Name  :  20000.0    Salary  :  35
'''




# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') #  a :  'Cyb'   <tab>  b :  'Sec'  <tab>  c :  'Hyd'
f1(c = 3 + 4j , a = True , b = None)  #  a :  True   <tab>  b :  None  <tab>  c :  3+4j
f1(25 , c = 10.8 , b = 'Hyd')         # a  :  25   <tab>       b  :  Hyd   <tab>    c :  10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'

'''
OUTPUT:
a  :  10          b  :  20        c :  30
a  :  25          b  :  10.8      c :  Hyd
a  :  50.2        b  :  40.7      c :  60.5
a  :  Cyb         b  :  Sec       c :  Hyd
a  :  True        b  :  None      c :  (3+4j)
a  :  25          b  :  Hyd       c :  10.8
'''



# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)

'''
OUTPUT:
Emp  Number :   25        Emp  Name : Rama Rao            Salary : 10000.0
Emp  Number :   35        Emp  Name : Sita                Salary : 20000.0
Emp  Number : Rama  Rao           Emp  Name :         30000.0     Salary : 20
'''




# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))  #23
print(f1(*[6 , 7 , 8])) #62
#print(f1([6 , 7 , 8]))  #error due to  f1() missing 2 required positional arguments: 'b' and 'c'
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) #16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))  # 14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))    # f1() missing 2 required positional arguments: 'b' and 'c'
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})      #{'c': 2, 'b': 4, 'a': 6}
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))    # f1() got an unexpected keyword argument 'x'
'''
OUTPUT:
23
62
16
14
{'c': 2, 'b': 4, 'a': 6}
'''


# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a))  #positional argument follows keyword argument
#print(sorted(a , rev = True)) #error due to invalid key name  i.e rev
#print(25 , 10.8 , 'Hyd' , separator = '\t') # error due to invalid key name i.e separator
#print(25 , 10.8 , 'Hyd' , endofline = '\t')  #print() got an unexpected keyword argument 'endofline'
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') #positional argument follows keyword argument
