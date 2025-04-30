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
How  to  read  a  number
How  to  print  all  prime  numbers  between  2  and  user  input
print('Number  of  prime numbers  :  ' ,  ???)
  

def prime(n):
    c=0 
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if(i%j==0):
                break    
        else:
            print(i,end=" ")
            c+=1             
    return c   
n=int(input("Enter +ve integer greater than 2: "))        
if(n<=1):
    print("Invalid Input")  
else:
    print(F'prime numbers from 2 to {n} : {prime(n)}')

'''




# Keyword  only   arguments  demo  program
'''
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)# a  :  10  \t  b :  20
f1(b = 30 , a = 40)# a  :  30  \t  b :  40
f1(50 , 60)#  error we have to pass only keyword arguments in to the function becz we used * before a and b
f1(70 , b = 80)# erroe one is positional and one is keword its ok to pass arguments like this but due to * it was not possible
f1(a = 15 , 25)#  error its was not possible to pass arguments like this we cant pass positonal arguments after keyword arguments

'''
#Find  outputs (Home  work)
'''
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)# a  :  10  \t  b :  20  \t  c  :  30
f1(a = 40 , b = 50 , c = 60)# a  :  40  \t  b :  50  \t  c  :  60
f1(c = 100 , b = 90 , a = 80)# a  :  80  \t  b :  90  \t  c  :  100
f1(70 , 80 , c = 90)# error becz b must be an keyword argument becz of *
f1(70 , 80 , 90)# error becz b and c must be keword arguments becz of *
f1(c = 15 , b = 25 , 35)# error we can specify the positonal arguments after keyword arguments 

'''

'''
# Identify error (Home  work)
def   f1(a  , b , *):
        pass
# error becz after * their must be an atleast one arugument should be specified 

'''

#  Positional  only  arguments  demo  program
'''
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)# a  :  10  \t  b  :  20
f1(a = 30 ,  b = 40)# error we have to pass only positional arguments becz we have mentioned '/' it allows only postional arguments 
f1(50 , b = 60)# error we have to pass only positional arguments becz we have mentioned '/' it allows only postional arguments 
f1(a = 70 , 80)# we cant pass positonal arguments after keyword arguments 

'''


# Find  outputs (Home  work)
'''
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)# a  :  10  \t  b :  20  \t  c  :  30
f1(40 , 50 , c = 60)# a  :  40  \t  b :  50  \t  c  :  60
f1(a = 70 , b = 80 , c = 90)# error becz we have to pass only positonal arguments to a and b becz of '/'
f1(a = 100 , b = 110 , 120)# error we cant pass positional arguments after keyword arguments
f1(a = 130 , 140 , c = 150)# error a should be an positional argument becz of '/' 
f1(160 , b = 170 , 180)# error we cant pass positional arguments after keyword arguments
f1(190 , b = 200 , c = 210)#  error b should be positional argument becz of '/'

'''
# Find outputs(Home  work)
'''
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)# a  :  10  \t  b  :  20  \t  c  :  30  \t  d  :  40  \t  e  :  50  \t  f  :  60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)# error becz b must be an postional argument becz of '/'
f1(1 , 2 , 3 , 4 , 5 , f = 6)# error e should be an keyword argument becz of '*'
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)# error c is keyword argument we can pass positonal arguments after passing keyword arguments 
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#  a  :  10  \t  b  :  20  \t  c  :  30  \t  d  :  40  \t  e  :  50  \t  f  :  60

'''


# Identify error (Home  work)
'''
def  f1(/ , a , b ,  c):# error becz their should be atlest one argument before '/'
        pass
def   f2(a , b , c , *):# error becz their should be atlest one argument after  '*'
        pass
'''


# Identify  error  (Home  work)
'''
def  f4(* , a , b , c , /):# we have to take any one ethier * at the start or / at the end or nothing , we have to mention / before * was mentioned
	        pass
                
'''


# Find  outputs  (Home  work)
'''
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)# 3rd function : 10
f1(y = 20)# error  arguments in y its not defined so we can pass only  z in to the definaion 
f1(x = 30)# error arguments in x it not defined so we can pass z in to the definaion 
# if we define the function with same names the last defined was taken

'''


 # Identify  Error
'''
def   f1(a = 10 ,  b,  c = 20 ,  d):# error we can'nt pass positional parameters to the function after passing keyword parameters 
	pass
def   f2(b , d , a = 10 , c = 20):# its possible 
	pass
'''


#  Find  outputs (Home  work)
'''
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)# 20
f1()# 10
f1(a = 30)# 30
'''


# Find  outputs (Home  work)
'''
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))# 330
print(add(100 , 200 , 300))# 620
print(add(100 , 200 , 300 , 400))# 900
print(add(b = 100 , a = 200))# 330
print(add(100 , 200 , d = 300))# 610
print(add(d = 100 , a = 200 , b = 300))# 610
print(add(c = 100 , d = 200 , 300 , 400))# error we can pass postional arg after keyword arg
print(add(100 , 200 , c = 300 , x = 400))# error x is not defiend 
print(add())#error 

'''


#  Find  outputs (Home  work)
'''
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))# 10
print(f1())# 25
print(f2(20))# 20
print(f2())# error  must have pass an argument for the defination header

'''


# Find  outputs (Home  work)
'''
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)# ------
disp('$')# $$$$
disp()# ****
disp(n = 5)# *****
disp(5)# 20
disp(n = 7 , ch = '%')# %%%%%%%
disp(7 , '@')# @@@@@@@
disp(7 , n = 6)# 42
disp(ch = '!' ,  5)# error we can pass positional arg after ketword args 

'''


# Find  outputs (Home  work)
'''
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))# a=2 b=6 > 2**6=64
print(power(5))# a=5,b=2 > 5**2=25
print(power(b = 3 , a = 4.5))# a=4.5 b=3 > 4.5**3=91.125
print(power(3 + 4j))# a=3+4J b=2 > (3+4j)**2=(-7+24j)
print(power(True))# a=true b=2 > 1**2=1
def   power(b = 2 , a):# error we cant pass positional after keyword args
	 pass
'''


# Find outputs  (Home  work)
'''
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
print(add(10 , 20 , 30 , 40))# a=10 b=20 c=30 d=40 > a+b+c+d=100 4-argument function
print(add(50 , 60 , 70))# 50+60+70+4=184 4-argument function
print(add(80 , 90))# 80+90+3+4=177 4-argument function
print(add(100))# 100+2+3+2=109 4-argument function
print(add())# 10 4-argument function

'''


 # Find outputs  (Home  work)
'''
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)# 3-argument function : 10 20 30
disp(40 , 50 , 60 , 70)# error we have only 3 arguments in the last call here we pass 4 args 
disp(80 , 90)# 195

'''


# Find outputs(Home  work)
'''
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))# 70
print(add())# 30
print(add(a = 50))# 70
print(add(b = 60 , a = 70))# 130
print(add(80 , 90))# error we can pass only keywoed args becz of *

'''


# Find  outputs(Home  work)
'''
def   add(a = 10 , b , c):# error pos after key
       pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))# 120
print(add(b = 60 , c = 70))# 140
print(add(c = 80 , b = 90 , a = 100))# 270
print(add(c = 25 , a = 43))# error b is not passed
print(add(1 , 2 , 3))# error we can pass only key args
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):# we cant pass pos args after key args
		pass

'''


# Find  output (Home  work)
'''
def   f1(a = []):
        pass
print(f1 ._defaults_)# error becz here only one underscore of defaults we have to use double underscore( __defaults__ ([],))
'''


# Find  outputs (Home  work)
'''
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)# ([],)
f1(3)# list : [3]
print('_defaults_  :  ' , f1.__defaults__)# ([3],)
f1(4 , [1 , 2 , 3])# list : [1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__)# ([3],)
f1(9)# list : [3,9]
print('_defaults_  :  ' , f1.__defaults__)# ([3,9],)
f1(40 , [10 , 20 , 30])# list : [10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__)# ([3,9],)
f1(5)# list : [3,9,5]
print('_defaults_  :  ' , f1.__defaults__)# ([3,9,5],)
f1([6 , 7 , 8])# list : [3,9,5,[6,7,8]]
print('_defaults_  :  ' , f1.__defaults__)# ([3,9,5,[6,7,8]],)
# if list we passed directly the default canot update if the only value were passed the default were updated
'''



#  Find  outputs (Home  work)
'''
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)# ([],)
f1(3)# [3]
print('_defaults_  :  ' , f1.__defaults__)# ([],)
f1(4 , [1 , 2 , 3])# [1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__)# ([],)
f1(4)# [4]
print('_defaults_  :  ' , f1.__defaults__)# ([],)
f1(40 , [10 , 20 , 30])# [10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__)# ([],)
f1(5)# [5]
print('_defaults_  :  ' , f1.__defaults__)# ([],)
f1([6 , 7 , 8])#[[6,7,8]]
print('_defaults_  :  ' , f1.__defaults__)# ([],)
'''


# Find  outputs(Home  work)
'''
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__)# ([],)
print(f1(3))# [0,1,4]
print('_defaults  :  ' , f1.__defaults__)# ([0,1,4],)
print(f1(4 , [10 , 20 , 15 , 18]))# [10,20,15,18,0,1,4,9]
print('_defaults  :  ' , f1.__defaults__)# ([0,1,4],)
print(f1(5))# [0,1,4,0,1,4,9,16]
print('_defaults  :  ' , f1.__defaults__)# ([0,1,4,0,1,4,9,16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))# [100,200,300,0,1,4,0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__)# ([0,1,4,0,1,4,9,16],)
print(f1(6))# [0,1,4,0,1,4,9,25,0,1,4,0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__)# ([0,1,4,0,1,4,9,25,0,1,4,0,1,4,9,16,25],)

'''

# Find  output (Home  work)
'''
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))# [0,1,4]
print(f1(4 , [10 , 20 , 15 , 18]))# [10,20,15,18,0,1,4,9]
print(f1(5))# [0,1,4,9,16]
print(f1(a = [100 , 200 , 300],   x = 6 ))# [100,200,300,0,1,4,9,16,25]
print(f1(6))# [0,1,4,9,16,25]

'''


# Find  outputs
'''
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)# ('hyd',[])
f1()# a: 'Hydsec'
    # b: [1,2,3]
print('Default Values  :  ' , f1 . __defaults__)# ('hyd',[1,2,3],)
f1()# a: 'hydsec'
    # b: [1,2,3,1,2,3]
print('Default Values  :  ' , f1 . __defaults__)# ('hyd',[1,2,3,1,2,3],)
f1()# a: 'hydsec'
    # b: [1,2,3,1,2,3,1,2,3]
'''
