#18/3/2024 

#1.return  statement  demo  program

'''
def  f1():
	print('f1  function')
	return  25
	print('Hello')
	
# End  of  the  function
print('Begin') #1.Begin \n
x =  f1() #2.f1 function \n 
print(x)  #3. 25 \n 
print('End') #4. End

'''


#2.Find output 

'''
def   f1():
	print('Hyd') #2.Hyd
	print('Sec') #3.Sec
	print('Cyb') #4.Cyb 
	
# End  of  the  function
print('Begin') #1. Begin
x = f1()
print(x) #5.None
print(type(x)) #6.<class 'None'>
print('End') #7. End


'''



#  Gift
#3.Find  outputs

'''
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1() 
print(x) #(10,20,30)
print(type(x)) #<class 'tuple'>
a , b , c =  f1() 
print(a) #10
print(b) #20
print(c) #30
print('for  loop')
for  k   in   f1(): 
	print(k) # 10 \n 20 \n 30 \n
	
'''


#4.Find  outputs

'''
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin') #1.Begin 
x = f1()
print(x) #2. 10
print('End') #3. End 
#return   100 # error 

'''


#5.Find  outputs

'''
#f1() #Error 
def   f1():
        print('Hello') #1.Hello
print(f1()) #2.None
print(f1) # <'function' f1 at  hex(id(f1))>

'''


#6.Find  outputs

'''
print('Hello') #1. Hello
def  f1():
        print('f1  function') #3. f1 function
#End  of   function
print('Hi') #2. Hi
print(f1()) #4. None 
print(f1) #5.<function f1 at hex_address>
print('Bye') #6.Bye

'''


# 7.Find  outputs

'''
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') #1. Begin
print(type(f1)) #2. <class 'function'>
print(id(f1)) #3.address 
print('End')  #4. End


'''


#8.Find  outputs

'''
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) #1.Three  argument  function :  10 20 30
#f1(40 , 50) #error due to no z 
#f1(60) #error due to no y z
#f1() #error due to no x y z 

'''


#9.Modify  following  program  such  that  every  function  should  be  executed

'''
def  f1():
	print('No-argument  function') #1.No-argument  function
f1()

def  f1(x):
	print('Single  argument  function  : ' , x) #2. Single  argument  function  : 10
f1(10)
	
def  f1(x , y):
	print('Two  argument  function : ' , x , y) #3. Two  argument  function : 10 20
f1(10,20)

def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z) #4. Three  argument  function : 10 20 30 
	
f1(10,20,30)


'''


#10.Write   a  function  to  test  a  number  is  prime  (or)  not.

'''

from math import *
def   prime(n):
    
    L=int(sqrt(n))
    for i in range(2,L+ 1):
        if n%i==0:
            return False 
            
    return True 

n=int(input("Enter any positive number: "))

if(n<=1):
    print("Invalid  input")
    
elif(prime(n)==True):
    print("Prime number")
    
else:
    print("Composite number")
    
'''

#11.Find  outputs

'''
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) #1. Emp  Number  :  25 \t  Emp Name  :  Rama Rao \t  Salary  :  10000.0
disp('Sita' , 20000.0 , 35) #2. Emp  Number  :  Sita \t  Emp Name  :  20000.0 \t  Salary  :  35 

'''


#12.Find  outputs 

'''
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a :  Cyb   <tab>  b :  Sec  <tab>  c :  Hyd
f1(c = 3 + 4j , a = True , b = None) # a :  True   <tab>  b :  None  <tab>  c :  3+4j
f1(25 , c = 10.8 , b = 'Hyd') # a :  25   <tab>  b :  Hyd  <tab>  c :  10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'


'''

#13.Find  outputs

'''
def    disp(empno , ename , sal):
        print(F'Emp  Number:{empno:4} \t Emp  Name :{ename:15} \t Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) #1. Emp  Number : <2s>25  \t  Emp  Name : Rama Rao<7s>  \t  Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)#2. Emp  Number : <2s>35  \t  Emp  Name : Sita<11s>  \t  Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) #3. Emp  Number : <2s>20  \t  Emp  Name : Rama Rao<7s>  \t  Salary : 30000.0

'''

#  Gift
#14.Find  outputs

'''
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # 23
print(f1(*[6 , 7 , 8])) # 62
#print(f1([6 , 7 , 8])) #Error due to no b c 
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) #16 
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # 14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) #Error due ti no b  c 
print({{'c' : 2 , 'b' :  4 , 'a' : 6}}) # {'c' : 2 , 'b' :  4 , 'a' : 6}
#print(f1({'c' : 2 , 'a' : 4 , 'x' : 6})) #Error no x

'''


#15.Identify  Error 

'''
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a)) #Error no positional args after keyword args 
#print(sorted(a , rev = True)) #Error no keyword arg called rev
#print(25 , 10.8 , 'Hyd' , separator = '\t') #Error no keyword called separator
#print(25 , 10.8 , 'Hyd' , endofline = '\t') #Error no keyword called endofline 
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') #Error no positional args after keyword args 

'''