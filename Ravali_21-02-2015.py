# Assignment operator Homework
a = 25 
print(a)  # 25
b =  a  
print(b)  # 25
print(a  is  b)  # True
x = 4 
y = 5
z = x + y * 6 
print(z) # 34
25 = a # Error due to we cannot assign a value to a number
#a + b = x + y # Error due to = operator is for assigning not for comparing
print(a + b == x + y) # False

# Find outputs 
a = b = c = 25  
print(id(a)) # may be 1000 
print(id(b)) # may be 1000
print(id(c)) # may be 1000 i.e, same address for all
print(a , b , c) # 25 25 25

# Identity operators demo program
a = 25
b = 25
print(a is b) # True
print(a is not b) # False
print(a == b) # True

a = 25 
b = 25.0  
print(a is b) # False
print(a is not b) # True
print(a == b) # True

a = 'Hyd' 
b = 'Hyd' 
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True
print()
x = [1 , 2 , 3 , 4]  
y = [1 , 2 , 3 , 4]  
print(x is y) # False due to List, Dict , Set , Range are not reusable
print(x  is  not  y) # True
print(x == y) # True
print()
m = (1 , 2 , 3 , 4) 
n = (1 , 2 , 3 , 4)  
print(m  is  n) #  True 
print(m  is  not  n) # False
print(m == n) # True

# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) # True
print(19 in list) # False
print(14 not in list) # True
print(15 not in list) # False
s = 'Hyd is green city'
print( 'is' in s) # True
print('was' in s) # False
print('g' in s) # True
print('z' in s) # False
print(' ' in s) # True
print('gre' in s) # True
print('yd i' in s) # True
print('' in s) # True
print('' not in s) # False

#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a = 25
#print(a++) #  (a+)+  = a+ = 25+  throws  error
print(a++1)  # a + (+1)  =  25 + 1 = 26
print(--a) # -(-a) = a = 25
#print(a--) # Error python doesnot support post increment and post decrement
print(a--1) # a-(-1) = a+1 =26
print(-a) # -25
print(+-a) # -25
print(-+a) # -25

#  Semicolon  demo  program
print('One'); # One
print('Two'); # Two
print('Three'); # Three
print('Hyd')  ; print('Sec')  ;  print('Cyb'); # Hyd <next line> Sec <next line> Cyb <next line>

#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  Previous  integer  of  10.8  i.e.  10
print(math . ceil(10.8))  #  Next  integer  of  10.8  i.e.  11
print(math . floor(25.0)) # remains same i.e, 25
print(math . ceil(25.0)) # ""
print(math . floor(-3.5)) # -4
print(math . ceil(-3.5)) # -3
print(math . floor(-9.0)) # -9
print(math . ceil(-9.0)) # -9
print(math . floor(25.1)) # 25
print(math . ceil(25.1)) # 26
print(floor(3.5)) # Error due to no floor function in current program
print(ceil(3.5)) # Error due to no ceil function in current program

#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) # 35.8 becaz abs function always return positive number 
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import  builtins
print(builtins . abs(-25)) # 25

# max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8)) # 25
import  builtins 
print(builtins . max(10 , 20 , 30)) # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5

# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) # 1/100 = 0.01
print(pow(4 , pow(3 , 2))) # 4^9
import  builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # -1/8 = 0.125
