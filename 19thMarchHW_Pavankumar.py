'''
PROGRAM_1:
Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
																		   2
																		   3
																		   5
																		   7
																		   Number  of   prime  numbers : 4
'''

from prime1 import prime
n=int(input("Enter a number"))
c=0
for i in range(2,n+1):
	if prime(i):
		print(i)
		c+=1
print("Number  of   prime  numbers : ",c)
'''
OUTPUT:
	Enter number to check prime or not : 7
Prime Number
Enter a number10
2
3
5
7
Number  of   prime  numbers :  4
'''
'''
PROGRAM_2:
'''
# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
f1(a = 10 , b = 20)
f1(b = 30 , a = 40)
#f1(50 , 60) --->f1() takes 0 positional arguments but 2 were given
#f1(70 , b = 80) --->f1() takes 0 positional arguments but only 1 positional argument is given
#f1(a=15,25) --->error due to positional argument following keyword argument
'''
OUTPUT:
a  :  10          b :  20
a  :  40          b :  30
'''
#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
f1(10 , b = 20 , c = 30)
f1(a = 40 , b = 50 , c = 60)
f1(c = 100 , b = 90 , a = 80)
#f1(70 , 80 , c = 90) --->error due two keyword arguments need be given but only given
#f1(70 , 80 , 90) --->f1() takes 1 positional argument but 3 were given
#f1(c=15,b=25,35) ---> error due to positional argument following keyword arguments
'''
OUTPUT:
a  :  10          b :  20
a  :  40          b :  30
a  :  10          b :  20         c  :  30
a  :  40          b :  50         c  :  60
a  :  80          b :  90         c  :  100
'''
# Identify error (Home  work)
#def   f1(a  , b , *) #--->there has to be atleast one argument given after *
     #pass
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
f1(10,20)
#f1(a=30,b=40) --->a,b should be positional arguments but not keyword arguments 
#f1(50,b=60) --->only positional arguments should be given before /
#f1(a=70,80) --->keyword arguments should be followed by positional arguments 
'''
OUTPUT:
a  :  10          b  :  20
'''
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
f1(10 , 20 , 30)
f1(40 , 50 , c = 60)
#f1(a = 70 , b = 80 , c = 90) ---> error due to f1() got some positional-only arguments passed as keyword arguments: 'a, b'
#f1(a = 100 , b = 110 , 120) ---> error due to positional argument follows keyword argument
#f1(a = 130 , 140 , c = 150) --->error due to positional argument follows keyword argument
#f1(160 , b = 170 , 180) --->error due to positional argument follows keyword argument
#f1(190,b=200,c=210) --->f1() got some positional-only arguments passed as keyword arguments: 'b'
'''
OUTPUT:
a  :  10          b :  20         c  :  30
a  :  40          b :  50         c  :  60
'''
# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) --->f1() got some positional-only arguments passed as keyword arguments: 'b'
#f1(1 , 2 , 3 , 4 , 5 , f = 6) --->f1() takes 4 positional arguments but 5 positional arguments (and 1 keyword-only argument) were given
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) ---> positional argument follows keyword argument
f1(10,20,30,40,e=50,f=60)
'''
OUTPUT:
a  :  10          b  :  20        c  :  30        d  :  40        e  :  50        f  :  60
a  :  10          b  :  20        c  :  30        d  :  40        e  :  50        f  :  60
'''
# Identify error (Home  work)
#def  f1(/ , a , b ,  c): --->argument should be given before /
       # pass
#def   f2(a , b , c , *):--->argument should be given after * 
#       pass
#def  f4(* , a , b , c , /):---> after * if arguments are keyword arguments then these throws error bcoz of these keyword argumets are before /
#        pass
# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z=10)
#f1(y=20) --->f1() got an unexpected keyword argument 'y'
#f1(x=30) --->f1() got an unexpected keyword argument 'x'
'''
OUTPUT:
3rd  function :  10
'''
# Identify  Error
#def   f1(a=10,b,c=20,d):--->parameter without a default follows parameter with a default
	#pass
#def   f2(b,d,a=10,c=20):--->parameter without a default follows parameter with a default
	#pass
#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
f1(20)
f1()
f1(a=30)
'''
OUTPUT:
20
10
30
'''
# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
print(add(100 , 200))
print(add(100 , 200 , 300))
print(add(100 , 200 , 300 , 400))
print(add(b = 100 , a = 200))
print(add(100 , 200 , d = 300))
print(add(d = 100 , a = 200 , b = 300))
#print(add(c = 100 , d = 200 , 300 , 400))--->positional argument follows keyword argument
#print(add(100 , 200 , c = 300 , x = 400))---> add() got an unexpected keyword argument 'x'
#print(add())--->add() missing 2 required positional arguments: 'a' and 'b'
'''
OUTPUT:
330
620
1000
330
610
610
'''
#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
print(f1(10))
print(f1())
print(f2(20))
#print(f2()) --->f2() missing 1 required positional argument: 'x'
'''
OUTPUT:
10
25
20
'''
# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
disp('-' , 6)
disp('$')
disp()
disp(n = 5)
disp(5)
disp(n = 7 , ch = '%')
disp(7 , '@')
disp(7 , n = 6)
#disp(ch='!',5)---> positional argument follows keyword argument
'''
OUTPUT:
------
$$$$
****
*****
20
%%%%%%%
@@@@@@@
42
'''
# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
print(power(2 , 6))
print(power(5))
print(power(b = 3 , a = 4.5))
print(power(3 + 4j))
print(power(True))
#def   power(b=2,a):--->parameter without a default follows parameter with a default
	#pass
'''
OUTPUT:
64
25
91.125
(-7+24j)
1
'''
# Find outputs  (Home  work)
def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
print(add(10 , 20 , 30 , 40))
print(add(50 , 60 , 70))
print(add(80 , 90))
print(add(100))
print(add())
'''
OUTPUT:
4-argument  function
100
4-argument  function
184
4-argument  function
177
4-argument  function
109
4-argument  function
10
'''
# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
disp(10 , 20 , 30)
#disp(40,50,60,70) --->disp() takes from 2 to 3 positional arguments but 4 were given
disp(80,90)
'''
OUTPUT:
3-argument  function  :   10 20 30
3-argument  function  :   80 90 25
'''
# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
print(add(a = 30 , b = 40))
print(add())
print(add(a = 50))
print(add(b = 60 , a = 70))
#print(add(80,90)) --->add() takes 0 positional arguments but 2 were given
'''
OUTPUT:
70
30
70
130
'''
# Find  outputs(Home  work)
#def   add(a = 10 , b , c): --->parameter without a default follows parameter with a default
       # pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
print(add(a = 30 , b = 40 , c = 50))
print(add(b = 60 , c = 70))
print(add(c = 80 , b = 90 , a = 100))
#print(add(c = 25 , a = 43)) --->add() missing 1 required keyword-only argument: 'b'
#print(add(1 , 2 , 3)) --->add() takes 0 positional arguments but 3 were given
#def   add(a , b = 10 ,  c ,  * , d  ,e=20,f): --->parameter without a default follows parameter with a default
	#	pass
'''
OUTPUT:
120
140
270
'''
# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1.__defaults__)
'''
OUTPUT:
([],)
'''
# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
print('_defaults_  :  ' , f1.__defaults__)
f1(3)
print('_defaults_  :  ' , f1.__defaults__)
f1(4 , [1 , 2 , 3])
print('_defaults_  :  ' , f1.__defaults__)
f1(9)
print('_defaults_  :  ' , f1.__defaults__)
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1.__defaults__)
f1(5)
print('_defaults_  :  ' , f1.__defaults__)
f1([6 , 7 , 8])
print('_defaults_  :  ' , f1.__defaults__)
'''
OUTPUT:
_defaults_  :   ([],)
List :   [3]
_defaults_  :   ([3],)
List :   [1, 2, 3, 4]
_defaults_  :   ([3],)
List :   [3, 9]
_defaults_  :   ([3, 9],)
List :   [10, 20, 30, 40]
_defaults_  :   ([3, 9],)
List :   [3, 9, 5]
_defaults_  :   ([3, 9, 5],)
List :   [3, 9, 5, [6, 7, 8]]
_defaults_  :   ([3, 9, 5, [6, 7, 8]],)
'''
#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
print('_defaults_  :  ' , f1.__defaults__)
f1(3)
print('_defaults_  :  ' , f1.__defaults__)
f1(4 , [1 , 2 , 3])
print('_defaults_  :  ' , f1.__defaults__)
f1(4)
print('_defaults_  :  ' , f1.__defaults__)
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1.__defaults__)
f1(5)
print('_defaults_  :  ' , f1.__defaults__)
f1([6 , 7 , 8])
print('_defaults_  :  ' , f1.__defaults__)
'''
OUTPUT:
_defaults_  :   ([],)
[3]
_defaults_  :   ([],)
[1, 2, 3, 4]
_defaults_  :   ([],)
[4]
_defaults_  :   ([],)
[10, 20, 30, 40]
_defaults_  :   ([],)
[5]
_defaults_  :   ([],)
[[6, 7, 8]]
_defaults_  :   ([],)
'''
# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
print('_defaults  :  ' , f1.__defaults__)
print(f1(3))
print('_defaults  :  ' , f1.__defaults__)
print(f1(4 , [10 , 20 , 15 , 18]))
print('_defaults  :  ' , f1.__defaults__)
print(f1(5))
print('_defaults  :  ' , f1.__defaults__)
print(f1(a = [100 , 200 , 300],   x = 6 ))
print('_defaults  :  ' , f1.__defaults__)
print(f1(6))
print('_defaults  :  ' , f1.__defaults__)
'''
OUTPUT:
_defaults  :   ([],)
[0, 1, 4]
_defaults  :   ([0, 1, 4],)
[10, 20, 15, 18, 0, 1, 4, 9]
_defaults  :   ([0, 1, 4],)
[0, 1, 4, 0, 1, 4, 9, 16]
_defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
[100, 200, 300, 0, 1, 4, 9, 16, 25]
_defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
[0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
_defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)
'''
# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
print(f1(3))
print(f1(4 , [10 , 20 , 15 , 18]))
print(f1(5))
print(f1(a = [100 , 200 , 300],x=6))
print(f1(6))
'''
OUTPUT:
[0,1,4]
[10,20,15,18,0,1,4,9]
[0,1,4,9,16]
[100,200,300,0,1,4,9,16,25]
[0,1,4,9,16,25]
'''
# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
print('Default Values  :  ' , f1 . __defaults__)
f1()
print('Default Values  :  ' , f1 . __defaults__)
f1()
print('Default Values  :  ' , f1 . __defaults__)
f1()
'''
OUTPUT:
Default Values  :   ('Hyd', [])
a :   HydSec
b :   [1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]
'''


