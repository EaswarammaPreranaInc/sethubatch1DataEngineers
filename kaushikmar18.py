'''def  f1():
	print('f1  function')
	return  25
	print('Hello')
print('Begin')
x=f1()
print(x)
print('End')'''

'''def  f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')


def f1():
	return (10,20,30)
print('begin')
f1()
print(f1())
a,b,c=f1()
print(a)
print(b)
print(c)
for i in f1():
	print(i)'''

'''def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
f1()
print(f1())
print('End')
#return 100'''

#f1()
'''def   f1():
        print('Hello')
print(f1())
print(f1)'''

''' line 46 error because function is called before def
f1()=none 
f1= id and type'''


'''print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')'''

'''def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')'''

'''def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
#f1(40,50)
#f1(60)
#f1()'''

'''def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(25)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(25,30)
def  f1(x , y , z):
	print('Three argument function:',x,y,z)
f1(25,30,40)'''



'''def prime(n):
	for i in range(2,(n//2)+1):
		if n % i==0:
			return False

	return True

n=int(input('enter the number'))

if n<=1:
	print('invalid')
elif prime(n):
	print('prime')
else:
	print('composite')'''

'''def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita',20000.0,35)'''

'''def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')
f1(c = 3 + 4j , a = True , b = None)
f1(25 , c = 10.8 , b = 'Hyd')
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function'''

'''def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))
print(f1(*[6 , 7 , 8]))
print(f1([6 , 7 , 8]))
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))
print({{'c' : 2 , 'b' :  4 , 'a' : 6}})
print(f1({'c': 2,'a':4,'x':6}))

a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))
print(sorted(a , rev = True))
print(25 , 10.8 , 'Hyd' , separator = '\t')
print(25 , 10.8 , 'Hyd' , endofline = '\t')'''
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')'''
