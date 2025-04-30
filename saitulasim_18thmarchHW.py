 #return statement demo program
def f1():
	print('f1 function')
	return 25
	print('Hello')
# End of the function
print('Begin') #Begin
x=f1()         #f1 function
print(x)       #25
print('End')   #End



#Find outputs  
def f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
#End of the function
print('Begin')  #Begin
x=f1()          #Hyd<next line>Sec<next line>Cyb
print(x)        #None
print(type(x))  #<class 'NoneType'>
print('End')    #End



#Gift
#Find outputs 
def f1():
	return 10,20,30
# End of the function
x=f1()
print(x)  #(10,20,30)
print(type(x)) #<class 'tuple'>
a,b,c=f1()
print(a) #10
print(b) #20
print(c) #30
print('for loop') #for loop
for k in f1():
	print(k)  #10<next line>20<next line>30



#Find outputs
def f1():
	return 10
	return 20
	return 30
# End of the function
print('Begin')  #Begin
x = f1() 
print(x)        #10
print('End')    #End
#return 100      #Error



#Find outputs
f1()   #Error (f1 is not defined)
def f1():
	print('Hello')
print(f1())  #Hello<next line>None
print(f1)    #<function f1 at 0x0000021A9F2D8A40>



#Find outputs
print('Hello') #Hello
def f1():
	print('f1 function')
#End of function
print('Hi') #Hi
print(f1()) #f1 function<next line>None
print(f1)   #<function f1 at 0x0000024A51708A40>
print('Bye') #Bye



#Find outputs
def f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') #Begin
print(type(f1))#<class 'function'>
print(id(f1))  #2171866548800
print('End')   #End



#Find outputs 
def f1():
	print('No-argument  function')
def f1(x):
	print('Single  argument  function  : ', x)
def f1(x,y):
	print('Two  argument  function : ', x,y)
def f1(x,y,z):
	print('Three  argument  function : ', x,y,z)
f1(10,20,30) #Three argument function : 10 20 30
#f1(40,50) #Error
#f1(60)    #Error
#f1()      #Error



#Modify following program such that every function should be executed
def f1():
	print('No-argument function')
f1()
def f1(x):
	print('Single argument  function:',x)
f1(25)
def f1(x,y):
	print('Two argument  function:',x,y)
f1(25,10.8)
def f1(x,y,z):
	print('Three argument  function:',x,y,z)
f1(25,10.8,True)

''' Output
No-argument function
Single argument  function: 25
Two argument  function: 25 10.8
Three argument  function: 25 10.8 True '''



#A function to test a number is prime or not

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

''' Output
Enter an int number: 2
Prime number
Enter an int number: 49
Composite number
Enter an int number: 'Hyd'
Invalid input '''



#Find outputs 
def disp(empno,ename,sal):
        print(F'Emp  Number : {empno} \t  Emp Name : {ename} \t  Salary : {sal}')
# End  of  the  function
disp(25,'Rama Rao',10000.0) #Emp  Number : 25          Emp Name : Rama Rao     Salary : 10000.0
disp('Sita',20000.0,35)     #Emp  Number : Sita        Emp Name : 20000.0      Salary : 35



#Find outputs 
def f1(a,b,c):
	print(F'a : {a} \t b : {b} \t c : {c}')
# End of the function
f1(a=10, b=20, c=30)  #a : 10  <tab>  b : 20 <tab>  c : 30
f1(25,10.8,'Hyd')   #a : 25   <tab>  b : 10.8  <tab>  c : Hyd
f1(b=40.7, a=50.2, c=60.5)   #a : 50.2  <tab>  b : 40.7  <tab>  c :  60.5
f1(c='Hyd',b='Sec',a='Cyb')#a : Cyb <tab> b : Sec <tab> c : Hyd
f1(c=3+4j,a=True,b=None) #a : True <tab> b : None <tab> c : (3+4j)
f1(25,c=10.8,b='Hyd')  #a : 25 <tab> b : Hyd <tab> c : 10.8
#f1(a=100,200,300)  #Error  becoz  pa's  are  after  ka
#f1(True,None,b='Hyd')  #Error  becoz arg  is  passed  for  'b'  twice
#f1(10,20,x=30) #Errorx
#f1(10,20) #Error



#Find outputs
def disp(empno,ename,sal):
	print(F'Emp Number:{empno:4} \t Emp Name:{ename:15} \t Salary:{sal}')
#End of function
disp(25,'Rama Rao',10000.0)  #Emp Number:  25 <tab> Emp Name:Rama Rao <tab> Salary:10000.0
disp(ename='Sita',sal=20000.0,empno=35) #Emp Number:  35 <tab> Emp Name:Sita <tab> Salary:20000.0
x='Rama Rao'
y=30000.0
z=20
disp(x,y,z) #Emp Number:Rama Rao <tab> Emp Name: 30000.0 <tab> Salary:20



#Gift
#Find outputs
def f1(a,b,c):
	return a+b*c
#end of the function
print(f1(3,4,5))    #23
print(f1(*[6,7,8])) #62
#print(f1([6,7,8]))  # error
#print(f1(*{1:2,3:4,5:6})) #Error
#print(f1({'c':2,'b':4,'a':6})) #Error
#print({{'c':2,'b':4,'a':6}})   #Error
#print(f1({'c':2,'a':4,'x':6})) #Error



#identify error
a=[10,20,15,5,12]
#print(sorted(reverse=True,a)) #Error (pa's after ka)
#print(sorted(a,rev=True)) #Error (due to rev)
#print(25,10.8,'Hyd',separator='\t') #Error (due to separator)
#print(25,10.8,'Hyd',endofline='\t') #Error (due to endoofline)
#print(25,sep='\t',10.8,end='\t','Hyd') #Error due to 10.8,'Hyd' coming after heyword arguments
