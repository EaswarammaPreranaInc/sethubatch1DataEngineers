'''def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')
x =  f1()
print(x)
print('End')

output:
Begin
f1  function
25
End'''

'''def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')

output:
Begin
Hyd
sec
cyb
none
<class 'Nonetype'>
End'''

'''def  f1():
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

output:
(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30'''

'''def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
x = f1()
print(x)
print('End')
#return   100#error

output:
Begin
10
End
'''

'''f1()#error 
def   f1():
        print('Hello')
print(f1())
print(f1)'''

'''def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

output:
Hi
f1 function
None
<function f1 at 0x000001ea375c1440>
Bye'''

'''def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')

output:
begin
<class 'function'>
may be 1000
end'''

'''def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
#f1(40 , 50)
#f1(60)
#f1()
output:
Three  argument  function :  10 20 30'''

'''def  f1_no_arg():
	print('No-argument  function')

def  f1_single_arg(x):
	print('Single  argument  function  : ' , x)

def  f1_two_arg(x , y):
	print('Two  argument  function : ' , x , y)

def  f1_three_arg(x , y , z):
	print('Three  argument  function : ' , x , y , z)

f1_no_arg()
f1_single_arg(10)
f1_two_arg(30,30)
f1_three_arg(40,50,60)
output:
No-argument  function
Single  argument  function  :  10
Two  argument  function :  30 30
Three  argument  function :  40 50 60'''

#Write   a  function  to  test  a  number  is  prime  (or)  not.
#1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself

def prime(n):
	 for i in range(2,n//2+1):
		 if n%i==0:
		  return False
	 return True
n=input('Enter an int number: ')
if(type(eval(n))!=int):
	print('Invalid input')
elif prime(int(n)):
	print('Prime number')
else:
	print('Composite number')

'''def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)

output:
Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0
Emp  Number  :  Sita      Emp Name  :  20000.0    Salary  :  35'''

'''def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#a: cyb b:sec c:hyd
f1(c = 3 + 4j , a = True , b = None)#a:true b:none c:3+4j
f1(25 , c = 10.8 , b = 'Hyd')#a:25 b:hyd c:10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'''

'''def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)

output:
Emp  Number :   25   Emp  Name : Rama Rao    Salary : 10000.0
Emp  Number :   35   Emp  Name : Sita        Salary : 20000.0
Emp  Number : Rama  Rao  Emp  Name :30000.0  Salary : 20'''

'''def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))#23
print(f1(*[6 , 7 , 8]))#62
#print(f1([6 , 7 , 8]))
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))#14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})#{'c':2,'b':4,'a':6}
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))'''

'''a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a))
#print(sorted(a , rev = True))
#print(25 , 10.8 , 'Hyd' , separator = '\t')
#print(25 , 10.8 , 'Hyd' , endofline = '\t')
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')'''
