'''
1 Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
																		   2
																		   3
																		   5
																		   7
																		   Number  of   prime  numbers : 4

How  to  read  a  number
How  to  print  all  prime  numbers  between  2  and  user  input
print('Number  of  prime numbers  :  ' ,  ???)'''

from prime import prime 
a=int(input('Enter a number grater than 2 : '))
c=0
for i in range(2,a+1):
	if prime(i)==True:
		print(i)
		c+=1
print('Number of prime numbers : ',c)

Output:
Enter a number grater than 2 : 10
2
3
5
7
Number of prime numbers :  4

#2 Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)
f1(b = 30 , a = 40)
#f1(50 , 60)
#f1(70 , b = 80)
#f1(a = 15 , 25)

Output:
a  :  10          b :  20
a  :  40          b :  30

#3 Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)
f1(a = 40 , b = 50 , c = 60)
f1(c = 100 , b = 90 , a = 80)
#f1(70 , 80 , c = 90)
#f1(70 , 80 , 90)
#f1(c = 15 , b = 25 , 35)

Output:
a  :  10          b :  20         c  :  30
a  :  40          b :  50         c  :  60
a  :  80          b :  90         c  :  100

#4 Identify error (Home  work)
def   f1(a  , b , *):
        pass

SyntaxError: named arguments must follow bare *

#5 Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)
#f1(a = 30 ,  b = 40)
#f1(50 , b = 60)
#f1(a = 70 , 80)

Output:
a  :  10          b  :  20

#6 Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)
f1(40 , 50 , c = 60)
#f1(a = 70 , b = 80 , c = 90)
#f1(a = 100 , b = 110 , 120)
#f1(a = 130 , 140 , c = 150)
#f1(160 , b = 170 , 180)
#f1(190 , b = 200 , c = 210)

Output:
a  :  10          b :  20         c  :  30
a  :  40          b :  50         c  :  60+

#7 Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)
#f1(1 , 2 , 3 , 4 , 5 , f = 6)
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)

Output:
a  :  10          b  :  20        c  :  30        d  :  40        e  :  50        f  :  60
a  :  10          b  :  20        c  :  30        d  :  40        e  :  50        f  :  60

#8 Identify error (Home  work)
def  f1(/ , a , b ,  c):
	pass
def   f2(a , b , c , *):
        pass

Syntax Error

#8 Identify  error  (Home  work)
def  f4(* , a , b , c , /):
	        pass

Syntax Error

#9 Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)
#f1(y = 20)
#f1(x = 30)

Output:
3rd  function :  10

#10 Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):
	pass
def   f2(b , d , a = 10 , c = 20):
	pass

SyntaxError: non-default argument follows default argument

#11 Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)
f1()
f1(a = 30)

Output:
20
10
30

#12 Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))
print(add(100 , 200 , 300))
print(add(100 , 200 , 300 , 400))
print(add(b = 100 , a = 200))
print(add(100 , 200 , d = 300))
print(add(d = 100 , a = 200 , b = 300))
#print(add(c = 100 , d = 200 , 300 , 400))
#print(add(100 , 200 , c = 300 , x = 400))
#print(add())

Output:
330
620
1000
330
610
610

#13 Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))
print(f1())
print(f2(20))
#print(f2())

Output:
10
25
20

#14 Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)
disp('$')
disp()
disp(n = 5)
disp(5)
disp(n = 7 , ch = '%')
disp(7 , '@')
disp(7 , n = 6)
#disp(ch = '!' ,  5)

Output:
------
$$$$
****
*****
20
%%%%%%%
@@@@@@@
42

#15 Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))
print(power(5))
print(power(b = 3 , a = 4.5))
print(power(3 + 4j))
print(power(True))
#def   power(b = 2 , a):
 #	 pass

Output:
 64
25
91.125
(-7+24j)
1

#16 Find outputs  (Home  work)
def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40))
print(add(50 , 60 , 70))
print(add(80 , 90))
print(add(100))
print(add())

Output:
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

#17 Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)
#disp(40 , 50 , 60 , 70)
disp(80 , 90)

Output:
3-argument  function  :   10 20 30
3-argument  function  :   80 90 25

#18 Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))
print(add())
print(add(a = 50))
print(add(b = 60 , a = 70))
#print(add(80 , 90))

Output:
70
30
70
130

#19 Find  outputs(Home  work)
#def   add(a = 10 , b , c):
#        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))
print(add(b = 60 , c = 70))
print(add(c = 80 , b = 90 , a = 100))
#print(add(c = 25 , a = 43))
#print(add(1 , 2 , 3))
#def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
#		pass

Output:
120
140
270

#20  Find  output (Home  work)
def   f1(a = []):
        pass
#print(f1 . _defaults_)

#21 Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
#print('_defaults_  :  ' , f1._defaults_)
f1(3)
#print('_defaults_  :  ' , f1._defaults_)
f1(4 , [1 , 2 , 3])
#print('_defaults_  :  ' , f1._defaults_)
f1(9)
#print('_defaults_  :  ' , f1._defaults_)
f1(40 , [10 , 20 , 30])
#print('_defaults_  :  ' , f1._defaults_)
f1(5)
#print('_defaults_  :  ' , f1._defaults_)
f1([6 , 7 , 8])
#print('_defaults_  :  ' , f1._defaults_)

Output:
List :   [3]
List :   [1, 2, 3, 4]
List :   [3, 9]
List :   [10, 20, 30, 40]
List :   [3, 9, 5]
List :   [3, 9, 5, [6, 7, 8]]

#22 Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
#print('_defaults_  :  ' , f1._defaults_)
f1(3)
#print('_defaults_  :  ' , f1._defaults_)
f1(4 , [1 , 2 , 3])
#print('_defaults_  :  ' , f1._defaults_)
f1(4)
#1print('_defaults_  :  ' , f1._defaults_)
f1(40 , [10 , 20 , 30])
#print('_defaults_  :  ' , f1._defaults_)
f1(5)
#print('_defaults_  :  ' , f1._defaults_)
f1([6 , 7 , 8])
#print('_defaults_  :  ' , f1._defaults_)

Output:
[3]
[1, 2, 3, 4]
[4]
[10, 20, 30, 40]
[5]
[[6, 7, 8]]

#23 Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
#print('_defaults  :  ' , f1._defaults_)
print(f1(3))
#print('_defaults  :  ' , f1._defaults_)
print(f1(4 , [10 , 20 , 15 , 18]))
#print('_defaults  :  ' , f1._defaults_)
print(f1(5))
#print('_defaults  :  ' , f1._defaults_)
print(f1(a = [100 , 200 , 300],   x = 6 ))
#print('_defaults  :  ' , f1._defaults_)
print(f1(6))
#print('_defaults  :  ' , f1._defaults_)

Output:
[0, 1, 4]
[10, 20, 15, 18, 0, 1, 4, 9]
[0, 1, 4, 0, 1, 4, 9, 16]
[100, 200, 300, 0, 1, 4, 9, 16, 25]
[0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]

#24 Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))
print(f1(4 , [10 , 20 , 15 , 18]))
print(f1(5))
print(f1(a = [100 , 200 , 300],   x = 6 ))
print(f1(6))

Output:
[0, 1, 4]
[10, 20, 15, 18, 0, 1, 4, 9]
[0, 1, 4, 9, 16]
[100, 200, 300, 0, 1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25]

#25 Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
#print('Default Values  :  ' , f1 . _defaults_)
f1()
#print('Default Values  :  ' , f1 . _defaults_)
f1()
#print('Default Values  :  ' , f1 . _defaults_)
f1()

Output:
a :   HydSec
b :   [1, 2, 3]
a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]