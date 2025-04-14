'''
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)#{10 , 20}
print(c)#{10 , 20}
print(type(c))#class set
d = a - b
print(d)#{10 , 20}
print(type(d))#class set
print(c  is  d)#False
print(c  ==  d)#True
#----------------------------
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10,20,50,60}
print(type(c))#class set
d = a ^ b
print(d)#{10,20,50,60}
print(type(d))#class set
print(c   is   d)#False
print(c  ==   d)#True
#----------------------------
a = {x * x  for   x   in   range(10)}
print(a)#{0,1,4,9.16,25,36,49,64,81}
print(type(a))#class set
#--------------------------------
x=eval(input("Enter List:"))#[False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
print(list(set(x)))
#------------------------------------
x=eval(input("Enter 1st List:"))
y=eval(input("Enter 2nd List:"))
a=set(x)
b=set(y)
c= list(a & b)
print(c)
#--------------------------------------------'

a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a. get('Empno'))
print(a. get('Ename'))
print(a. get('Sal'))
#-------------------------------'

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)
print(id(a))
#-------------------------------------'

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.update({'Gender' : 'M'})#How  to  append  'Gender' : 'M'  to  dictionary  'a'
a.update({'Married' : True})#How  to  append  'Married' :  True  to  dictionary  'a'
print(a)
#---------------------------------------------------------------------------------------

# Find  outputs (Home  work)
a = { }
b= {10 : 'Rama',20 : 'Sita',15 : 'Rajesh',18 : 'Kiran'}
a.update(b)
#How  to  append  10 : 'Rama'  to  dictionary  'a'
#How  to  append  20 : 'Sita'  to  dictionary  'a'
#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
#How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)
#------------------------------------

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.popitem()
#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)
#--------------------------------------------------------'

def p(s):

    return s == s[::-1]

# Get input from the user
a= input("Enter a string: ")

# Check if the input string is a palindrome
if p(a):
    print("palindrome")
else:
    print("not a palindrome")
#==========================================

#1)
#  return  statement  demo  program
def  f1():
	print('f1  function')#2)f1 function
	return  25
	print('Hello')
# End  of  the  function
print('Begin')#1)Begin
x =  f1()
print(x)#3)25
print('End')#4)End
#===========================================

# Find outputs  (Home  work)
def   f1():
	print('Hyd')#Hyd
	print('Sec')#Sec
	print('Cyb')#Cyb
# End  of  the  function
print('Begin')#Begin
x = f1()
print(x)
print(type(x))#None type
print('End')#End
#==================================================

#  Gift
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)#(10,20,30)
print(type(x))#class tuple
a , b , c =  f1()
print(a)#10
print(b)#20
print(c)#30
print('for  loop')
for  k   in  f1():
      print(k)
#======================================'

# Find  outputs
def    f1():
        return  10#10
        return  20
        return  30
# End  of  the  function
print('Begin')#Begin
x = f1()
print(x)
print('End')#End
#return 100
#============================================='

f1()
def   f1():
        print('Hello')
print(f1())
print(f1) #error
#=============================================

# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
#================================================='

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
#f1(40 ,50)
#f1(60)
#f1()
#============================================================

def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(60)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(40,50)
def  f1(x , y , z):
	print('Three  argument  function :',x,y,z)
f1(10 , 20 , 30)
#============================================================'

# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)#correct results
disp('Sita',20000.0, 35)#incorrect results
#===========================================================

# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#a:Cyb <tab> b:'Sec' <tab> c:'Hyd'
f1(c = 3 + 4j , a = True , b = None)#a:True <tab> b: None <tab> c = 3 + 4j
f1(25 , c = 10.8 , b = 'Hyd')#a:25 b:'Hyd' c:10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function'
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c''
#================================================================
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x,y,z)'
#==================================================
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))
print(f1(*[6 , 7 , 8]))
#print(f1([6 , 7 , 8]))
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))
#print({{'c' : 2 , 'b' :  4 , 'a' : 6}})
#print(f1({'c' : 2 , 'a' :4,'x':6}))'
#================================================'

# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))#error
print(sorted(a , rev = True))#error
print(25 , 10.8 , 'Hyd' , separator = '\t') #error
print(25 , 10.8 , 'Hyd' , endofline = '\t')#error
print(25 ,  sep = '\t' ,10.8 , end='\t','Hyd')#error'
#==========================================================='
'''
def prime(n):
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
#End of the for loop
        return True
n = int(input('Enter any number:'))
if n<2:
    print('Invalid input')
elif prime(n):
    print('Prime number')
else:
    print('Composite number')
	
