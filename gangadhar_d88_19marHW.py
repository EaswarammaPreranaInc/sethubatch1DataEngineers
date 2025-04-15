# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)# a:10   b: 20
f1(b = 30 , a = 40)# a:40   b: 30
#f1(50 , 60)#error due to positional are not allowed  
#f1(70 , b = 80)# error due to 70 positional are not allowed 
#f1(a = 15 , 25)# error due to positional argument after kerword argument 

 #Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)# a:10   b: 20  c:30
f1(a = 40 , b = 50 , c = 60)# a:40   b: 50  c:60
f1(c = 100 , b = 90 , a = 80)# a:80   b: 90  c:100
#f1(70 , 80 , c = 90)#error,after * keyword argument only allowed
#f1(70 , 80 , 90)#error,after * keyword argument only allowed
#f1(c = 15 , b = 25 , 35)# error due to positional argument after kerword argument 

 # Identify error (Home  work)
#def   f1(a  , b , *):# after * atleast one argument is required
        
        #pass

 #  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)# a:10   b: 20
#f1(a = 30 ,  b = 40)#error,before / always positional arguments allowed
#f1(50 , b = 60)#error,before / always positional arguments are allowed
#f1(a = 70 , 80)# error due to positional argument after kerword argument 

 # Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)# a:10   b: 20  c:30
f1(40 , 50 , c = 60)# a:40   b: 50  c:60
#f1(a = 70 , b = 80 , c = 90)#error: due to a and b aarguments,before / always positional only  arguments
#f1(a = 100 , b = 110 , 120)# error due to positional argument after kerword argument 
#f1(a = 130 , 140 , c = 150)# error due to positional argument after kerword argument 
#f1(160 , b = 170 , 180)# error due to positional argument after kerword argument 
#f1(190 , b = 200 , c = 210)#error: due to b argument ,before / always positional only arguments

 # Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)# a:10   b:20    c:30    d:40    e:50    f:60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) #error: due to b argument ,before / always positional only  arguments
#f1(1 , 2 , 3 , 4 , 5 , f = 6)#error: due to e argument ,after * only keyword  arguments allowed
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)# error due to positional argument after kerword argument 
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)# a:10   b:20    c:30    d:40    e:50    f:60

# Identify error (Home  work)
"""
def  f1(/ , a , b ,  c): # error due to / ,should be end of arguments,not at  start 
        pass
def   f2(a , b , c , *):# error due to  * ,should be start of arguments,not at  end
        pass
 # Identify  error  (Home  work)# error due to / 
def  f4(* , a , b , c , /):
                
	        pass
"""

 # Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)# 3rd  function : 10
#f1(y = 20) # error : y is not suuported keyowrd
#f1(x = 30)#error : x is not supported keyword

'''
'''
 # Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d):# errror : due to positional argument after keyword argument
#	pass
def   f2(b , d , a = 10 , c = 20):
	pass
#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)# 20
f1()# 10,because of default argument value is 10
f1(a = 30)# 30 
 # Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) #330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400))# 1000
print(add(b = 100 , a = 200)) # 330
print(add(100 , 200 , d = 300)) #610
print(add(d = 100 , a = 200 , b = 300)) #610
#print(add(c = 100 , d = 200 , 300 , 400)) # errror : due to positional argument after keyword argument
#print(add(100 , 200 , c = 300 , x = 400)) # error : due to x 
#print(add())# error : 2 arguments are missed 

#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))#10
print(f1())#25
print(f2(20))#20
#print(f2())#error : 1 arg missed


 # Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)# ------

disp('$')# $$$$
disp()# ****
disp(n = 5)# *****
disp(5)#error
disp(n = 7 , ch = '%')# %%%%%%%
disp(7 , '@')
disp(7 , n = 6)#42
#disp(ch = '!' ,  5) # error : positional argument after keyword argument
 # Find  outputs (Home  work)

def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5))
print(power(3 + 4j))
print(power(True))
#def   power(b = 2 , a):# error : positional argument after keyword argument
 	 #pass

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
print(add(10 , 20 , 30 , 40))#100
print(add(50 , 60 , 70))#  184
print(add(80 , 90))#77
print(add(100))#109
print(add())#10
# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)# 3-argument  function  :10 20 30
#disp(40 , 50 , 60 , 70) # error : d argument
disp(80 , 90)# 3-argument  function  :80 90 25

 # Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))# 70
print(add())# 30
print(add(a = 50))#60
print(add(b = 60 , a = 70))# 130
#print(add(80 , 90))# error : due * allows keyword only arguments
# Find  outputs(Home  work)
#def   add(a = 10 , b , c):#error : positional argument after keyword argument
      # pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))#120
print(add(b = 60 , c = 70))#140
print(add(c = 80 , b = 90 , a = 100))#270
#print(add(c = 25 , a = 43))# error due b arguments is missed
#print(add(1 , 2 , 3))#error , * allows keyword ony argument
#def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):#error : positional argument after keyword argument
	#pass

# Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and also  print  how  many  prime  numbers  are  existing

from gangadhar_d88_18marHW.py import prime # import function prime 
n=int(input("enter a number : "))# 10
def nPrime(n):
    for i in range(2,n+1): # iterate from 2 to 11
        if prime(i):# checks if i is prime or not
            print(i)# 2  3  5  7 
           
            

nPrime(n) # calling function by passing 10
