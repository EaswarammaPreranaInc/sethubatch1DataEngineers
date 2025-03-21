#1 #  return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin') #Begin
x =  f1() # f1 function 25 
print(x) #Type and address of x
print("End") #End


#2 # Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') #Begin 
x = f1() #Hyd Sec Cyb
print(x) #None 
print(type(x)) #<class 'NoneType'>
print('End') #End


#3 #  Gift
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1() #(10,20,30)
print(x) #(10,20,30)
print(type(x)) #<class 'tuple'>
a , b , c =  f1() 
print(a) #10 
print(b) #20
print(c) #30 
print('for  loop') #for loop
for  k   in   f1():
	print(k) #10 20 30



#4 # Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin') #Begin
x = f1()  
print(x) #10 
print('End') #End
#return   100 #error due to return outside the function


#5 #  Find  outputs
#f1() #error function can't be called before the function definition
def   f1():
        print('Hello')
print(f1()) # Hello None
print(f1) #Type and address of f1


#6 print('Hello') #Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') #Hi
print(f1()) # f1 function None
print(f1) #type and address of f1
print('Bye') #Bye


#7 #  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') #Begin
print(type(f1)) #<class 'function'>
print(id(f1)) #say some adress 1000
print('End') #End

#8 # Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) #takes Three argument function the f1 functions are ignored i.e Three argument function
f1(40 , 50) #error due to missing argument
f1(60)#error due to missing arguments
f1() #error due to missing arguments 


#9 # Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1() #No-argument  function
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10) #Single  argument  function: 10
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(10,20) #Two  argument  function: 10 20
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10,20,30) #Three  argument  function : 10 20 30  


#10 Prime number
def prime(n):
    for i in (1,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input('Enter a number: '))
if n<2:
    print('Invalid number')
elif prime(n):
    print("Prime Number")
else:
    print("composite number")


#11 # Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) #Emp Number : 25 <tab space> Emp Name: Rama Rao <tab space> Salary:100000
disp('Sita' , 20000.0 , 35) #Emp Number : Sita <tab space> Emp Name: 20000 <tab space> Salary:35


#12 # Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a: Cyb  <tab>   b:Sec   <tab> c=Cyb
f1(c = 3 + 4j , a = True , b = None) # a: True  <tab>   b:None  <tab> c=3+4j
f1(25 , c = 10.8 , b = 'Hyd') # a:25    <tab>   b:Hyd   <tab>   c:10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'


#13 # Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) # Emp Number : 25 <tab> Emp Name: Rama rao <tab> Salary: 10000
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Emp Number : 35 <tab> Emp Name: Sita <tab> Salary: 20000
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) # Emp Number : Rama Rao <tab> Emp Name: 30000 <tab> Salary: 20



#14 #  Gift
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) #23
print(f1(*[6 , 7 , 8])) #62
#print(f1([6 , 7 , 8]))  #missing args b and c 
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) #16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) #14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) #missing args b and c
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) #{'c' : 2 , 'b' :  4 , 'a' : 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))# error due to missing argument b


#15 # Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a)) #error due to pa after ka
print(sorted(a , rev = True)) #error due to rev
print(25 , 10.8 , 'Hyd' , separator = '\t')  #error due separator
print(25 , 10.8 , 'Hyd' , endofline = '\t') #error due to endofline
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') #error due to pa after ka
