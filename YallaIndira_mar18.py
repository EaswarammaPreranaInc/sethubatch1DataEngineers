'''#  return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')
x =  f1()
print(x)
print('End')

#output :
Begin
f1 function
25
End'''


'''# Find outputs 
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

#outputs:
Begin
Hyd
Sec
Cyd
None
<class 'NoneType'>
End '''
    

'''# Find  outputs  
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)
print(type(x))
a , b , c =  f1()
print(a)
print(b)
print(c)
print('for  loop')
for  k   in   f1():
	print(k)

#output:
(10 , 20 , 30)
<class 'tuple'>
10
20
30
for loop
10
20
30
'''

'''# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
x = f1()
print(x)
print('End')
return   100   # error return is only inside the function

#outputs:
Begin
10
End
'''

'''#  Find  outputs
f1()  # error function cal only after function defined
def   f1():
        print('Hello')
print(f1())
print(f1) # type and address of the function may be <function f1 at 0x0000027181301440>

#outputs:
Hello
None
'''

'''# Find  outputs  
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)    # type and address of the function
print('Bye')

#outputs:
Hello
Hi
f1 function
None
<function f1 at 0x00000244BE601440>
Bye
'''

'''#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')  # Begin
print(type(f1)) # <class 'function'>
print(id(f1))   # address of the f1
print('End')   # End
'''

'''# Find  outputs 
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)  #  Three  argument  function :  10  20 30
f1(40 , 50)  #  error
f1(60)   #  error
f1()     # error
'''


'''# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()  # No-argument function
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10)  # Single argument function : 10
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(10 , 20) # Two argument function : 10 20
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 ,30)  # Three argument function : 10 20 30
'''

'''Write   a  function  to  test  a  number  is  prime  (or)  not.
What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself

def prime(n):
	if n<2:
		print('Invalid number')
	else:
		for i in range(2,n//2+1):
			if n%i==0:
				print("Composite  number")
				break
		else:
			print("Prime Number")
n=int(input())
prime(n)
'''

'''# Find  outputs  
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)  # Emp  Number  :  25		Emp Name  :  Rama Rao      Salary  :  10000.0
disp('Sita' , 20000.0 , 35)    #  Emp  Number  :  Sita     Emp Name  :  20000.0     Salary  :  35
'''

'''# Find  outputs  
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')  #  a :  Cyd   <tab>  b :  Sec  <tab>  c :  Hyd
f1(c = 3 + 4j , a = True , b = None)   # a :  True   <tab>  b :  None  <tab>  c :  (3+4j)
f1(25 , c = 10.8 , b = 'Hyd')   #  a :  25   <tab>  b :  Hyd  <tab>  c :  10.8
f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'
'''

'''# Find  outputs 
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)  #  Emp  Number : 25  \t  Emp  Name : Rama Rao  \t  Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)  #  Emp  Number : 35  \t  Emp  Name : Sita  \t  Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) #  Emp  Number : Rama Rao  \t  Emp  Name : 30000.0  \t  Salary : 20
'''

'''#  Gift
# Find  outputs 
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))   # 23
print(f1(*[6 , 7 , 8])) # 62
print(f1([6 , 7 , 8])) # error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # 16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) # 14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # error
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) # {'C' : 2 , 'b' : 4 , 'a' : 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) #error
'''

'''
# Identify  Error 
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a)) # error due to keyword arguments  follows the positional arguments
print(sorted(a , rev = True)) # rev is not a formal argument of sorted function
print(25 , 10.8 , 'Hyd' , separator = '\t') # error due to separator 
print(25 , 10.8 , 'Hyd' , endofline = '\t') # error due to endofline
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') # error due keyword arguments in between the positional arguments
'''
