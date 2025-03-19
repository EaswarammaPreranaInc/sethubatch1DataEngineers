import Hw
n = int(input("Enter Number : "))
c = 0
for i in range(1,n+1):
    if Hw.fun(i):
        print("prime numbers are : ",i)
        c+=1
print("Number of prime numbers are ",c)
'''
Enter Number : 49
prime numbers are :  2
prime numbers are :  3
prime numbers are :  5
prime numbers are :  7
prime numbers are :  11
prime numbers are :  13
prime numbers are :  17
prime numbers are :  19
prime numbers are :  23
prime numbers are :  29
prime numbers are :  31
prime numbers are :  37
prime numbers are :  41
prime numbers are :  43
prime numbers are :  47
Number of prime numbers are  15'''

# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) #a=10   b=20
f1(b = 30 , a = 40) # a=40  b=30
# f1(50 , 60) # error PA
# f1(70 , b = 80) # error
# f1(a = 15 , 25) # error KA before PA

#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) #a  :  10  	  b :  20  	  c  :  30
f1(a = 40 , b = 50 , c = 60) #a  :  40  	  b :  50  	  c  :  60
f1(c = 100 , b = 90 , a = 80) #a  :  80  	  b :  90  	  c  :  100
# f1(70 , 80 , c = 90) # error no KA for b
# f1(70 , 80 , 90) # error no KA for b and c
# f1(c = 15 , b = 25 , 35) # KA follows PA

# Identify error (Home  work)
def   f1(a  , b , *):
        pass # there is no arg after *

#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) #a  :  10  	  b  :  20
# f1(a = 30 ,  b = 40) #error KA where given in PA
# f1(50 , b = 60) # error
# f1(a = 70 , 80)#KA follows PA

# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)  #a  :  10  	  b :  20  	  c  :  30
f1(40 , 50 , c = 60) #a  :  40  	  b :  50  	  c  :  60
# f1(a = 70 , b = 80 , c = 90) # error
# f1(a = 100 , b = 110 , 120) # KA follows PA
# f1(a = 130 , 140 , c = 150) # error KA follows PA
# f1(160 , b = 170 , 180) # error
# f1(190 , b = 200 , c = 210) # error

# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) #a  :  10  	  b  :  20  	  c  :  30  	  d  :  40  	  e  :  50  	  f  :  60
# f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # error
# f1(1 , 2 , 3 , 4 , 5 , f = 6)#error
# f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # KA follows PA
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) #a  :  10  	  b  :  20  	  c  :  30  	  d  :  40  	  e  :  50  	  f  :  60

# Identify error (Home  work)
def  f1(/ , a , b ,  c):
        pass # PA kept at first
def   f2(a , b , c , *):
        pass # KA kept at last


# Identify  error  (Home  work)
def  f4(* , a , b , c , /):
	        pass# KA follows PA

# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) #3rd  function :  10
f1(y = 20) # expected z got y
f1(x = 30) # expected z got x

# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):
	pass # KA follows PA
def   f2(b , d , a = 10 , c = 20):
	pass # KA follows PA

#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)
f1()
f1(a = 30)
'''
20
10
30'''

# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))#330
print(add(100 , 200 , 300)) #620
print(add(100 , 200 , 300 , 400)) # 1000
print(add(b = 100 , a = 200)) # 330
print(add(100 , 200 , d = 300)) #610
print(add(d = 100 , a = 200 , b = 300)) #610
# print(add(c = 100 , d = 200 , 300 , 400)) #error positional argument follows keyword argument
# print(add(100 , 200 , c = 300 , x = 400)) # error
# print(add())#error

#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) # 10
print(f1()) #25
print(f2(20)) # 20
print(f2()) # error

# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) #------
disp('$')#$$$$
disp()#****
disp(n = 5)#*****
disp(5)#20
disp(n = 7 , ch = '%')#%%%%%%%
disp(7 , '@')#@@@@@@@
disp(7 , n = 6)#42
disp(ch = '!' ,  5)#error


# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5))#91.125
print(power(3 + 4j))#(-7+24j)
print(power(True))#1
def   power(b = 2 , a):
 	 pass # KA follows PA

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
print(add(10 , 20 , 30 , 40)) #4-argument  function<nextline>100
print(add(50 , 60 , 70))#4-argument  function<nextline>184
print(add(80 , 90))#4-argument  function<nextline>177
print(add(100))#4-argument  function<nextline>109
print(add())#4-argument  function<nextline>10

# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) #3-argument  function  :   10 20 30
# disp(40 , 50 , 60 , 70)#error
disp(80 , 90) # 3-argument  function  :   80 90 25

# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) # 70
print(add()) #30
print(add(a = 50)) #70
print(add(b = 60 , a = 70)) #130
print(add(80 , 90))#PA is given instead of KA


# Find  outputs(Home  work)
# def   add(a = 10 , b , c):
#         pass#erro KA before PA
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))#120
print(add(b = 60 , c = 70))#140
print(add(c = 80 , b = 90 , a = 100))#270
# print(add(c = 25 , a = 43))#error
# print(add(1 , 2 , 3))#PA
# def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
# 		pass#KA before PA


# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . __defaults__)#([],)


# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)
f1(3)
print('__defaults__  :  ' , f1.__defaults__)
f1(4 , [1 , 2 , 3])
print('__defaults__  :  ' , f1.__defaults__)
f1(9)
print('__defaults__  :  ' , f1.__defaults__)
f1(40 , [10 , 20 , 30])
print('__defaults__  :  ' , f1.__defaults__)
f1(5)
print('__defaults__  :  ' , f1.__defaults__)
f1([6 , 7 , 8])
print('__defaults__  :  ' , f1.__defaults__)
'''
__defaults__  :   ([],)
List :   [3]
__defaults__  :   ([3],)
List :   [1, 2, 3, 4]
__defaults__  :   ([3],)
List :   [3, 9]
__defaults__  :   ([3, 9],)
List :   [10, 20, 30, 40]
__defaults__  :   ([3, 9],)
List :   [3, 9, 5]
__defaults__  :   ([3, 9, 5],)
List :   [3, 9, 5, [6, 7, 8]]
__defaults__  :   ([3, 9, 5, [6, 7, 8]],)
'''

# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . __defaults__)#([],)


# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)
f1(3)
print('__defaults__  :  ' , f1.__defaults__)
f1(4 , [1 , 2 , 3])
print('__defaults__  :  ' , f1.__defaults__)
f1(9)
print('__defaults__  :  ' , f1.__defaults__)
f1(40 , [10 , 20 , 30])
print('__defaults__  :  ' , f1.__defaults__)
f1(5)
print('__defaults__  :  ' , f1.__defaults__)
f1([6 , 7 , 8])
print('__defaults__  :  ' , f1.__defaults__)
'''
__defaults__  :   ([],)
List :   [3]
__defaults__  :   ([3],)
List :   [1, 2, 3, 4]
__defaults__  :   ([3],)
List :   [3, 9]
__defaults__  :   ([3, 9],)
List :   [10, 20, 30, 40]
__defaults__  :   ([3, 9],)
List :   [3, 9, 5]
__defaults__  :   ([3, 9, 5],)
List :   [3, 9, 5, [6, 7, 8]]
__defaults__  :   ([3, 9, 5, [6, 7, 8]],)'''

#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)
f1(3)
print('__defaults__  :  ' , f1.__defaults__)
f1(4 , [1 , 2 , 3])
print('__defaults__  :  ' , f1.__defaults__)
f1(4)
print('__defaults__  :  ' , f1.__defaults__)
f1(40 , [10 , 20 , 30])
print('__defaults__  :  ' , f1.__defaults__)
f1(5)
print('__defaults__  :  ' , f1.__defaults__)
f1([6 , 7 , 8])
print('__defaults__  :  ' , f1.__defaults__)
'''
__defaults__  :   ([],)
[3]
__defaults__  :   ([],)
[1, 2, 3, 4]
__defaults__  :   ([],)
[4]
__defaults__  :   ([],)
[10, 20, 30, 40]
__defaults__  :   ([],)
[5]
__defaults__  :   ([],)
[[6, 7, 8]]
__defaults__  :   ([],)'''

# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('__defaults_  :  ' , f1.__defaults__)
print(f1(3))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(4 , [10 , 20 , 15 , 18]))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(5))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(a = [100 , 200 , 300],   x = 6 ))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(6))
print('__defaults_  :  ' , f1.__defaults__)
'''
__defaults_  :   ([],)
[0, 1, 4]
__defaults_  :   ([0, 1, 4],)
[10, 20, 15, 18, 0, 1, 4, 9]
__defaults_  :   ([0, 1, 4],)
[0, 1, 4, 0, 1, 4, 9, 16]
__defaults_  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
[100, 200, 300, 0, 1, 4, 9, 16, 25]
__defaults_  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
[0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
__defaults_  :   ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)'''


# Find  output (Home  work)
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
'''
[0, 1, 4]
[10, 20, 15, 18, 0, 1, 4, 9]
[0, 1, 4, 9, 16]
[100, 200, 300, 0, 1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25]'''


# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)
f1()
print('Default Values  :  ' , f1 . __defaults__)
f1()
print('Default Values  :  ' , f1 . __defaults__)
f1()
print('Default Values  :  ' , f1 . __defaults__)
'''
Default Values  :   ('Hyd', [])
a :   HydSec
b :   [1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3, 1, 2, 3])'''
