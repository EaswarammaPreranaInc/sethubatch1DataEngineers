#Ex-2
# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # a  :  10 <tab> b :  20
f1(b = 30 , a = 40) # a  :  40 <tab> b :  30
#f1(50 , 60) # arguments must be keyword arguments but not use positional arguments
#f1(70 , b = 80) # arguments must be keyword arguments not use positional arguments
# f1(a=15,25) # arguments must be keyword arguments not use positional arguments

#Ex-3
#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # a : 10 <tab> b : 20 <tab> c : 30
f1(a = 40 , b = 50 , c = 60)  # a : 40 <tab> b : 50 <tab> c : 60
f1(c = 100 , b = 90 , a = 80) # a : 80 <tab> b : 90 <tab> c : 100
#f1(70 , 80 , c = 90) # a must be keyword argument
#f1(70 , 80 , 90)   # a must be keyword argument
# f1(c = 15,b=25,35) # a must be keyword argument

#Ex-4
# Identify error (Home  work)
#def   f1(a  , b , *): # * comes first named parameters
#    pass

#Ex-5
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # a  :  10 <tab> b  :  20
#f1(a = 30 ,  b = 40) # only positional arguments only not keyword arguments
#f1(50 , b = 60) #  only positional arguments only not keyword arguments
#f1(a=70,80) # only positional arguments only not keyword arguments


#Ex-6
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) #  a :  10 <tab> b :  20 <tab> c  :  30
f1(40 , 50 , c = 60) #  a : 40 <tab> b :  50 <tab> c  :  30
#f1(a = 70 , b = 80 , c = 90) # first two arguments must be only positional arguments
#f1(a = 100 , b = 110 , 120) # first two arguments must be only positional arguments
#f1(a = 130 , 140 , c = 150) # first two arguments must be only positional arguments
#f1(160 , b = 170 , 180) # first two arguments must be only positional arguments
#f1(190 , b =200,c=210) # first two arguments must be only positional arguments


#Ex-7
# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # a  :  10 <tab> b  :  20  <tab> c  :  30  <tab> d  :  40  <tab> e  :  50  <tab> f  :  60
# f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) #Error because a and b must be positional arguments and e and f keyword arguments
#f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error because a and b must be positional arguments and e and f keyword arguments
# f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error Positional argument after keyword argument
f1(10 , 20 , 30 , 40 , e=50,f=60) # # a  :  10 <tab> b  :  20  <tab> c  :  30  <tab> d  :  40  <tab> e  :  50  <tab> f  :  60

#Ex-8
#Identify error (Home  work)
#def  f1(/ , a , b ,  c): # / is used after named arguments
#       pass
#def   f2(a , b , c , *): # / is used before named arguments


#Ex-9:
# Identify  error  (Home  work)
def  f4(* , a , b , c , /): # / before use positional arguments  after to use * keyword arguments
	pass

#Ex-10
# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z) # 3rd  function :  10
f1(z = 10) # f1(z) is valid remaining are  ignored
#f1(y =20) # Error keyword argument 'y' not there
#f1(x=30) # Error because keyword argument 'x' not there

#Ex-11
# Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d): # keyword arguments not use PA
#	pass
def   f2(b , d , a = 10 ,c=20):
	pass

#Ex-12
#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20) # 20
f1() #10
f1(a=30) #30

#Ex-13
# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # 330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400)) # 1000
print(add(b = 100 , a = 200)) # 330
print(add(100 , 200 , d = 300)) # 610
print(add(d = 100 , a = 200 , b = 300)) # 610
#print(add(c = 100 , d = 200 , 300 , 400)) # keyword arguments not use PA
#print(add(100 , 200 , c = 300 , x = 400)) # keyword argument x not define
#print(add()) # positional arguments 'a' and 'b' required

#Ex-14
#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))  # 10
print(f1()) # 20
print(f2(20)) # 20
#print(f2()) #missing positionsl argument

#Ex-15
# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # ------
disp('$') # $$$$
disp() # ****
disp(n = 5) # *****
disp(5) # 20
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # @@@@@@@
disp(7 , n = 6) # 42
#disp(ch='!',5) # Error because KA after not use PA

#Ex-16
# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6)) # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5)) # 91.125
print(power(3 + 4j)) # -+24j
print(power(True)) # 1
#def   power(b =2,a):  # Error because default parameter after non - default paramaeter
#	pass

#Ex-17
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
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40)) # 4-argument  function <nl> 100
print(add(50 , 60 , 70)) # 4-argument  function <nl> 184
print(add(80 , 90)) # 4-argument  function <nl> 177
print(add(100)) # 4-argument  function <nl> 109
print(add()) # 4-argument  function <nl> 10

# Ex-18
# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :  10 <space> 20 <space> 30
#disp(40 , 50 , 60 , 70) # Error because only taking 2 or 3 PA  but given 4
disp(80,90) # # 3-argument  function  :  80 <space> 90 <space> 25

#Ex-19
# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) #70
print(add()) #30
print(add(a = 50)) #70
print(add(b = 60 , a = 70)) # 130
#print(add(80,90)) # Error because only take KA but given PA

#Ex-20
# Find  outputs(Home  work)
#def   add(a = 10 , b , c): # # Error because default parameters after non-default parameter
#        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) #120
print(add(b = 60 , c = 70)) # 140
print(add(c = 80 , b = 90 , a = 100)) # 270
#print(add(c = 25 , a = 43)) # Error because  b is not KA  ,b is missing
#print(add(1 , 2 , 3))  # Error because only take KA but given PA
#def   add(a , b = 10 ,  c ,  * , d  , e =20,f): # Error because default parameters after non-default parameter
#		pass

#Ex-21
# Find  output (Home  work)
def   f1(a = []):
        pass
#print(f1._defaults_) # Error because _defaults_, but __defaults__

#Ex-22
# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([],)
f1(3) # List :   [3]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([3],)
f1(4 , [1 , 2 , 3]) # List :   [1, 2, 3, 4]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([3],)
f1(9) # List :   [3, 9]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([3, 9],)
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([3, 9],)
f1(5) # List :   [3, 9, 5]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([3, 9, 5],)
f1([6 , 7 , 8]) # List :   [3, 9, 5, [6, 7, 8]]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([3, 9, 5, [6, 7, 8]],)


# Ex-23
#Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_  :   ([],)
f1(3) # [3]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([],)
f1(4 , [1 , 2 , 3]) # [1, 2, 3, 4]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([],)
f1(4) # [4]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([],)
f1(40 , [10 , 20 , 30]) # [10, 20, 30, 40]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([],)
f1(5) # [5]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_  :   ([],)
f1([6 , 7 , 8]) # [[6, 7, 8]]
print('_defaults_  :  ' , f1.__defaults__) #_defaults_  :   ([],)

#Ex-24
# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__) # _defaults  :   ([],)
print(f1(3)) # [0, 1, 4]
print('_defaults  :  ' , f1.__defaults__) # _defaults  :   ([0, 1, 4],)
print(f1(4 , [10 , 20 , 15 , 18])) # [10, 20, 15, 18, 0, 1, 4, 9]
print('_defaults  :  ' , f1.__defaults__) # _defaults  :   ([0, 1, 4],)
print(f1(5)) # [0, 1, 4, 0, 1, 4, 9, 16]
print('_defaults  :  ' , f1.__defaults__) # _defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a = [100 , 200 , 300],   x = 6 )) # [100, 200, 300, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1.__defaults__) # _defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(6)) # [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1.__defaults__) # _defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)

#Ex-25
# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3)) # [0, 1, 4]
print(f1(4 , [10 , 20 , 15 , 18])) # [10, 20, 15, 18, 0, 1, 4, 9]
print(f1(5)) # [0, 1, 4, 9, 16]
print(f1(a = [100 , 200 , 300],   x = 6)) # [100, 200, 300, 0, 1, 4, 9, 16, 25]
print(f1(6)) # [0, 1, 4, 9, 16, 25]

#Ex-26
# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__) # Default Values  :   ('Hyd', [])
f1() # a :   HydSec <nl> b :   [1, 2, 3]
print('Default Values  :  ' , f1 . __defaults__) # Default Values  :   ('Hyd', [1, 2, 3])
f1() # a :   HydSec <nl> b :   [1, 2, 3, 1, 2, 3]
print('Default Values  :  ' , f1 .__defaults__) # Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3])
f1() # a :   HydSec <nl> b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]

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
# D:\python\Programs\18_03_25_HW\Prime.py

from Prime import prime
n = int(input('Enter a number : '))
ctr = 0
for i in range(2,n+1):
    if prime(i):
        print(i)
        ctr +=1
print('Number  of   prime  numbers : ',ctr)
