'''
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? --->  i =   2 , 3 , 4 , 5 , 6 , ..... 12

3) Let  input   be  11
    What  is   the  range  of  divisors ? --->  i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  ---> return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
'''
'''
def   prime(n):
	return  true   when  'n'  is  prime  number  and  False  otherwise
'''
'''
1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->

2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->

3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->

4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->
'''
'''
How  to  read  a  number
if   input  is  invalid:
	print('Invalid  input')
elif  input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')
'''

def prime(n):
	if n==1:
		return None
	else:
		for i in range(2,n//2+1):
			if n%i==0:
				return False
		return True

try:
	n=int(input('Enter a number : '))
	if prime(n) is None:
		print(n,'is not a prime or composite.')
	elif prime(n):
		print('Prime number')
	else:
		print('composite number ')
except:
	print('Invalid input')




'''
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

import pr
n=int(input('Enter a number : '))
c=0
for i in range(2,n+1):
	if pr.prime(i):
		print(i,"is a Prime Number")
		c+=1
print('Number of prime numbers : ',c)

'''    Sample output
Enter a number : 10
composite number
Enter a number : 10
2 is a Prime Number
3 is a Prime Number
5 is a Prime Number
7 is a Prime Number
Number of prime numbers :  4

'''



# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)  # a : 10 <tab> b : 20
f1(b = 30 , a = 40)  # a : 40 <tab> b : 30
# f1(50 , 60)  # Error : due to fl() does not take positional arguments
# f1(70 , b = 80)  # Error : fl() does not take positional arguments,But, Arg a is positional argument
# f1(a=15,25)  # Error : due to Keyword argument after positional

'''  OUTPUT
a  :  10  	  b :  20
a  :  40  	  b :  30

'''


#Find  outputs (Homework)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)  # a : 10 <tab> b : 20 <tab> c : 30
f1(a = 40 , b = 50 , c = 60)  # a : 40 <tab> b : 50 <tab> c : 60
f1(c = 100 , b = 90 , a = 80)  # a : 80 <tab> b : 90 <tab> c : 100
# f1(70 , 80 , c = 90)  # Error : f1() take 1 PA  but 2 PA were given
# f1(70 , 80 , 90)  # Error : f1() take 1 PA  but 3 PA were given
# f1(c = 15,b=25,35)  # Error : due to keyword argument after positional argument

'''   OUTPUT
a  :  10  	  b :  20  	  c  :  30 
a  :  40  	  b :  50  	  c  :  60 
a  :  80  	  b :  90  	  c  :  100 

'''



# Identify error (Homework)
# def   f1(a  , b , *):
#    pass   # Error : at least one argument should be there after * operator in function header




#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)  # a : 10 <tab> b : 20
# f1(a = 30 ,  b = 40)  # Error : fl() take 2 PA but 2 KA were given
# f1(50 , b = 60)  # Error : f1() take 2 Pa but 1 KA were given
# f1(a=70,80)  # Error : due to KA after PA

'''   OUTPUT
a  :  10  	  b  :  20

'''



# Find  outputs (Homework)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)  # a : 10 <tab> b : 20 <tab> c : 30
f1(40 , 50 , c = 60)  # a : 40 <tab> b : <tab> c : 60
# f1(a = 70 , b = 80 , c = 90)  # Error : fl() take 3 PA but 3 KA were given
# f1(a = 100 , b = 110 , 120)  # Error : due to KA after PA
# f1(a = 130 , 140 , c = 150)  # Error : due to KA after PA
# f1(160 , b = 170 , 180)  # Error : due to KA after PA
# f1(190 , b =200,c=210)  # Error : f1() take 3 PA but 2 KA were given

'''   OUTPUT
a  :  10  	  b :  20  	  c  :  30 
a  :  40  	  b :  50  	  c  :  60 

'''



# Find outputs(Homework)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)  # a : 10 <tab> b : 20 <tab> c : 30 <tab> d : 40 <atb> e : 50 <tab> f : 60
# f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)  # Error : f1() take 4 PA but 1 PA were given
# f1(1 , 2 , 3 , 4 , 5 , f = 6)  # Error : f1() take 2 KA but 1 KA were given
# f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)  # Error : due to KA after PA
f1(10 , 20 , 30 , 40 , e=50,f=60)  # a : 10 <tab> b : 20 <tab> c : 30 <tab> d : 40 <atb> e : 50 <tab> f : 60

'''   OUTPUT
a  :  10  	  b  :  20  	  c  :  30  	  d  :  40  	  e  :  50  	  f  :  60
a  :  10  	  b  :  20  	  c  :  30  	  d  :  40  	  e  :  50  	  f  :  60
'''


# Identify error (Homework)
# def  f1(/ , a , b ,  c):  # Error : at least one argument should be there before / operator in function header
#      pass
#def   f2(a , b , c , *):  # Error : at least one argument should be there after * operator in function header
#   pass


# Identify  error  (Homework)
#def  f4(* , a , b , c , /):  # Error : invalid syntax
#	 pass



# Find  outputs  (Homework)
def  f1(x):   # Discarded because another function is defined with same name
	print('1st  function : ' , x)
def  f1(y):  # Discarded because another function is defined with same name
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)  # 3rd function : 10
# f1(y =20)  # Error : y is not defined in fl()
# f1(x=30)  # Error : x is not defined in f1()

'''  OUTPUT
3rd  function :  10

'''



# Identify  Error
# def   f1(a = 10 ,  b ,  c = 20 ,  d):  # Error : due to positional arguments after keyword arguments
#	pass
def   f2(b , d , a = 10 ,c=20):
	pass



#  Find  outputs (Homework)
def   f1(a = 10):
     print(a)
# End  of  the  function
f1(20)  # 20
f1()  # 10
f1(a=30)  # 30

'''  OUTPUT
20
10
30

'''


# Find  outputs (Homework)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))  # a is 100 and b is 200 and c and d are default values --> 330
print(add(100 , 200 , 300))  # 620
print(add(100 , 200 , 300 , 400))  # 1000
print(add(b = 100 , a = 200))  # 330
print(add(100 , 200 , d = 300))  # 610
print(add(d = 100 , a = 200 , b = 300))  # 610
# print(add(c = 100 , d = 200 , 300 , 400))  # Error : due to PA after KA
# print(add(100 , 200 , c = 300 , x = 400))  # Error : Arg 'x' does not exist in add() function
# print(add())  # Error : missing positional arguments of 'a' and 'b'

'''    OUTPUT
330
620
1000
330
610
610

'''



#  Find  outputs (Homework)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))  # 10  i.e default value of 'x' is ignored
print(f1())  # 25
print(f2(20))  # 20
# print(f2())  # Error : missing positional argument of 'x'

'''   OUTPUT
10
25
20

'''


# Find  outputs (Homework)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)  # '------'
disp('$')  # '$$$$'
disp()  # '****'
disp(n = 5)  # '*****'
disp(5)  # 20
disp(n = 7 , ch = '%')  # '%%%%%%%'
disp(7 , '@')  # '@@@@@@@'
disp(7 , n = 6)  # 42
# disp(ch='!',5)  # Error : due to PA after KA

'''   OUTPUT
------
$$$$
****
*****
20
%%%%%%%
@@@@@@@
42

'''



# Find  outputs (Homework)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))  # 64
print(power(5))  # 25
print(power(b = 3 , a = 4.5))  # 91.125
print(power(3 + 4j))  # (-7+24j)
print(power(True))  # 1
#def   power(b =2,a):  # Error : due to non_default argument at the end
#   pass

'''   OUTPUT
64
25
91.125
(-7+24j)
1

'''



# Find outputs  (Homework)
def   add(a , b):  # Discarded because another function is defined with same name
	print('2-argument  function')
	return a + b
def  add(a , b , c): # Discarded because another function is defined with same name
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40))  # 4-argument function <nextline> 100
print(add(50 , 60 , 70))  # 4-argument function <nextline> 184
print(add(80 , 90))  # 4-argument function <nextline> 177
print(add(100))  # 4-argument function <nextline> 109
print(add())  # 4-argument function <nextline> 10

'''   OUTPUT
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


# Find outputs(Homework)
def   add(* , a = 10 , b = 20):
      return  a + b
# End of  the  function
print(add(a = 30 , b = 40))  # 70
print(add())  # 30
print(add(a = 50))  # 70
print(add(b = 60 , a = 70))  # 130
# print(add(80,90))  # Error : add() take 0 PA but 2 PA were given

'''    OUTPUT
70
30
70
130

'''



# Find  outputs(Home  work)
# def   add(a = 10 , b , c):  # Error : due to non default arguments at the end
#      pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))  # 120
print(add(b = 60 , c = 70))  # 140
print(add(c=80 , b=90 , a = 100))  # 270
# print(add(c = 25 , a = 43))  # Error : Arg is not passed for 'b'
# print(add(1 , 2 , 3))  # Error : add() take 0 PA but 3 PA were given
#def   add(a , b = 10 ,  c ,  * , d  , e =20,f):  # Error : due to default after non-default argument
#		pass

'''   OUTPUT
120
140
270
'''


# Find  output (Homework)
def   f1(a = []):
        pass
print(f1.__defaults__)  # ([],)

'''   OUTPUT
([],)

'''



# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)  # ([],)
f1(3)  # [3]
print('_defaults_  :  ' , f1.__defaults__)  # ([3],)
f1(4 , [1 , 2 , 3])  # [1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__)  # ([3],)
f1(9)  # [3,9]
print('_defaults_  :  ' , f1.__defaults__)  # ([3,9],)
f1(40 , [10 , 20 , 30])  # [10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__)  # ([3,9],)
f1(5)  # [3,9,5]
print('_defaults_  :  ' , f1.__defaults__)  # ([3,9,5],)
f1([6 , 7 , 8])  # [3,5,9,[6,7,8]]
print('_defaults_  :  ' , f1.__defaults__)  # ([3,9,5,[6,7,8]],)

'''   OUTPUT
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



# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__)  # ([],)
print(f1(3))  # [0,1,4]
print('_defaults  :  ' , f1.__defaults__)  # ([0,1,4],)
print(f1(4 , [10 , 20 , 15 , 18]))  # [10,20,15,18,0,1,4,9]
print('_defaults  :  ' , f1.__defaults__)  # ([0,1,4],)
print(f1(5))  # [0,1,4,0,1,4,9,16]
print('_defaults  :  ' , f1.__defaults__)  # ([0,1,4,0,1,4,9,16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))  # [100,200,300,0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__)  # ([0,1,4,0,1,4,9,16],)
print(f1(6))  # [0,1,4,0,1,4,9,16,0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__)  # ([0,1,4,0,1,4,9,16,0,1,4,9,16,25] ,)

'''   OUTPUT
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



# Find  output (Homework)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))  # [0,1,4]
print(f1(4 , [10 , 20 , 15 , 18]))  # [10,20,15,18,0,1,4,9]
print(f1(5))  # [0,1,4,9,16]
print(f1(a = [100 , 200 , 300],   x = 6))  # [100,200,300,0,1,4,9,16,25]
print(f1(6))  # [0,1,4,9,16,25]

'''   OUTPUT
[0, 1, 4]
[10, 20, 15, 18, 0, 1, 4, 9]
[0, 1, 4, 9, 16]
[100, 200, 300, 0, 1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25]

'''



# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)  # ('Hyd',[],)
f1()  #  a : 'HydSec'  <nextline> b : [1,2,3]
print('Default Values  :  ' , f1 . __defaults__)  # ('Hyd',[1,2,3])
f1()  # a : 'HydSec'  <nextline> b : [1,2,3,1,2,3]
print('Default Values  :  ' , f1 . __defaults__)  # ('Hyd',[1,2,3,1,2,3])
f1()  # a : 'HydSec'  <nextline> b : [1,2,3,1,2,3,1,2,3]

'''  OUTPUT
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
