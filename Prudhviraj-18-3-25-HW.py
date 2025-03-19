#  return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')
x =  f1()
print(x)#'f1 function' \n 25
print('End')


# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)#'hyd'\n 'sec' \n 'cyb' \n None
print(type(x))#class nonetype
print('End')


#  Gift
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)#(10 , 20 , 30)
print(type(x))#class tuple
a , b , c =  f1()
print(a)#10 
print(b)#20
print(c)#30
print('for  loop')
for  k   in   f1():
	print(k)
#10
#20
#30


# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
x = f1()
print(x)#10
print('End')
#return   100


#  Find  outputs
#f1()
def   f1():
        print('Hello')
print(f1())#hello \n none
print(f1)#<function f1 at 0x00000178EA481440>



# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())#f1  function \n none
print(f1)#<function f1 at 0x000001BA506D1440>
print('Bye')


#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))#class function
print(id(f1))#2463160276032
print('End')


# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) #Three  argument  function :  10 20 30
#f1(40 , 50)
#f1(60)
#f1()


# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)#Emp Number:25 \t Emp Name:'Rama Rao' \t Salary:10000.0
disp('Sita' , 20000.0 , 35)#Emp Number:Sita \t Emp Name:'20000.0 Rao' \t Salary:35



# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#  a :  Cyb   <tab>  b :  Sec  <tab>  c :  Hyd
f1(c = 3 + 4j , a = True , b = None)#a :  True   <tab>  b :  None  <tab>  c :  3 + 4j
f1(25 , c = 10.8 , b = 'Hyd')#a :  25   <tab>  b :  Hyd  <tab>  c :  10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'



# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)#Emp  Number :   25   Emp  Name : Rama Rao     Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)#Emp  Number :   35  Emp  Name : Sita    Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)#Emp  Number : Rama  Rao     Emp  Name :   30000.0     Salary : 20



#  Gift
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))#23
print(f1(*[6 , 7 , 8]))#62
#print(f1([6 , 7 , 8]))#error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#16
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#error
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#error
#print({{'c' : 2 , 'b' :  4 , 'a' : 6}})#error
#print(f1({'c' : 2 , 'a' : 4 , 'x' : 6}))



# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a))#error
#print(sorted(a , rev = True))#error
#print(25 , 10.8 , 'Hyd' , separator = '\t')#error
#print(25 , 10.8 , 'Hyd' , endofline = '\t')#error
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')#error


#Write   a  function  to  test  a  number  is  prime  (or)  not.
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
