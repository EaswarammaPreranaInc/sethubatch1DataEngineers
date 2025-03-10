a = 25 
print(a)     #25
b =  a  
print(b)     #25
print(a  is  b)    #True
x = 4
y = 5
z = x + y * 6   
print(z)          #34
 

a = b = c = 25  
print(id(a))   #ramdom id
print(id(b))   #same id
print(id(c))   #same id
print(a,b,c)   #25,25,25

x , y , z = 25 , 10.8 , 'Hyd'  
print(x)    #25
print(y)    #10.8
print(z)    #Hyd

a , b , c = 3 , 4 , 5
a*= b+c
print(a)     #27


a = 25
b = 25
print(a is b)    #True
print(a is not b)#False
print(a == b)   #True

a = 25 
b = 25.0  
print(a is b)   #False
print(a is not b)#True


a = 'Hyd' 
b = 'Hyd' 
print(a  is  b)       #True
print(a  is  not  b)  #False
print(a == b)         #True
print()               #empty
x = [1 , 2 , 3 , 4]  
y = [1 , 2 , 3 , 4]  
print(x is y)          #False
print(x  is  not  y)    #True
print(x == y)          #True
print()                #empty
m = (1 , 2 , 3 , 4) 
n = (1 , 2 , 3 , 4)  
print(m  is  n)        #True
print(m==n)          #True

list = [10 , 20 , 15 , 12 , 18]
print(15 in list)        #True
print(19 in list)        #False
print(14 not in list)    #True
print(15 not in list)    #False
s = 'Hyd is green city'
print( 'is' in s)       #True
print('was' in s)       #False
print('g' in s)         #True
print('z' in s)         #False
print(' ' in s)        #True
print('gre' in s)      #True
print('yd i' in s)     #True
print('' in s)         #True
print('' not in s)     #False

a = 25
print(++a)  #  +(+a) = +a = 25
#print(a++) #  (a+)+  = a+ = 25+  throws  error
print(a++1)  # a + (+1)  =  25 + 1 = 26
print(--a)   # - (-a) = a = 26
#print(a--)    #25
print(a--1)   #26
print(-a)    # -25
print(+-a)   # -25
print(-+a)   #-25

print('One');     #One
print('Two');    #Two
print('Three');   #Three
print('Hyd');print('Sec');print('Cyb');  #all objects


import  math
print(math . floor(10.8))  #  Previous  integer  of  10.8  i.e.  10
print(math . ceil(10.8))  #  Next  integer  of  10.8  i.e.  11
print(math . floor(25.0)) #25
print(math . ceil(25.0))  #25
print(math . floor(-3.5))  #-4
print(math . ceil(-3.5))   #-3
print(math . floor(-9.0))   #-9
print(math . ceil(-9.0))    #-9
print(math . floor(25.1))   #25
print(math . ceil(25.1))    #26
#print(floor(3.5))    #Error
#print(ceil(3.5))     #Error

print(abs(-35.8))  #35.8
print(abs(-27))    #27
print(abs(29.5))   #29.5
print(abs(32))     #32
import  builtins
print(builtins.abs(-25))   #25

from  builtins  import   max , min
print(max(10.8 , 20.6))             #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))#5.9
print(max(25 , 10.8))              #25
import  builtins                  
print(builtins.max(10 , 20 , 30))  #30
print(builtins.min(10,20,30))  #10


from  builtins  import  pow
print(pow(10 , -2))          #0.01
print(pow(4 , pow(3 , 2)))  #262144
import  builtins
print(builtins.pow(2 , 3))  #8 
print(builtins.pow(-2,-3)) #-0.125








