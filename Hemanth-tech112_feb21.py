#  Assignment  operators  demo  program  (Homework)
a = 25  # Assigns reference 'a' to int object 25
print(a)  # 25
b = a  # Assigns reference 'b' to same int object where 'a' points.Both 'a' and 'b' points to same object
print(b)  # 25 
print(a is b)  # True 
x = 4  # Assigns reference 'x' to int object 4 
y = 5  # Assigns reference 'y' to int object 5  
z = x + y * 6  # Assigns reference 'z' to int object 34 
print(z)  # 34 
# 25 = a  # Error because operand1 should be only reference 
# a + b = x + y  # Error because operand1 should be reference not an expression

# Find outputs (Homework)
a = b = c = 25  # references 'a' and 'b' and 'c' points to the same int object 25 
print(id(a))  # Address of the object 25
print(id(b))  # Address of the object is same because same object 
print(id(c))  # Address of the object is same because same object  
print(a, b, c)  # 25 25 25


# Multiple  Assignment (Homework)
x, y, z = 25, 10.8, 'Hyd'  # Assigns references 'x' 'y' 'z' to 25 10.8 'Hyd' 
print(x)  # 25
print(y)  # 10.8
print(z)  #'Hyd'


# Find outputs (Homework)
a, b, c = 3, 4, 5  # Assigns references 'a' 'b' 'c' to 3 4 5 
a *= b+c  # a=a*(b+c)-->a=a*b+a*c-->a=3*4+3*5-->a=12+15-->a=27
print(a)  # 27


# Find outputs (Homework)
a = 3  # Assigns reference 'a' to int object 3
a **= 4  # a=a**(4)-->a=3**(4)-->a=81
print(a)  # 81


# Identity operators demo program
a = 25  # reference 'a' points to int object 25
b = 25  # reference 'b' points to same object where 'a' points
print(a is b)  # True
print(a is not b)  # False 
print(a == b)  # True


# Find outputs (Homework)
a = 25  # Assigns reference 'a' to int object 25
b = 25.0  # Assigns reference 'b' to float object 25.0
print(a is b)  # False
print(a is not b)  # True
print(a == b)  # True



# Find outputs (Homework)
a = 'Hyd'  # reference 'a' points to string  object 'Hyd'
b = 'Hyd'  # reference 'b' points to same object where 'a' points
print(a is b)  # True
print(a is not b)  # False
print(a == b)  # True
print()  # Empty space
x = [1, 2, 3, 4]  # reference 'x' points to list object [1, 2, 3, 4]
y = [1, 2, 3, 4]  # reference 'y' points to same object where 'x' points
print(x is y)  # True
print(x is not y)  # False
print(x == y)  # True
print()  # Empty space
m = (1, 2, 3, 4)  # reference 'm' points to tuple object (1, 2, 3, 4)
n = (1, 2, 3, 4)  # reference 'n' points to same object where 'm' points
print(m is n)  # True
print(m is not n)  # False
print(m == n)  # True


# Membership operators demo program (Homework)
list = [10, 20, 15, 12, 18]  # list is list due to []
print(15 in list)  # True
print(19 in list)  # False
print(14 not in list)  # True
print(15 not in list)  # False
s = 'Hyd is green city'  # ref 's' points to string object
print('is' in s)  # True
print('was' in s)  # False
print('g' in s)  # True
print('z' in s)  # False
print(' ' in s)  # True
print('gre' in s)  # True
print('yd i' in s)  # True
print('' in s)  # True because every string contains empty string
print('' not in s)  # False



#  ++  and  --  operators  demo  program
a = 25  # ref 'a' points to int object 25
print(++a)  # +(+a) = +a = 25
# print(a++) #  (a+)+  = a+ = 25+  throws  error
print(a++1)  # a + (+1)  =  25 + 1 = 26
print(--a)  # -(-a)= -a=-25
# print(a--)  # (a-)-= a-= 25- throws error
print(a--1)  # 26
print(-a)  # -25
print(+-a)  # -25
print(-+a)  # -25


#  Semicolon  demo  program
print('One'); # One
print('Two');  # Two
print('Three');  # Three 
print('Hyd')  ; print('Sec')  ;  print('Cyb');  # Hyd
                                                # Sec
                                                # Cyb



#  floor()  and  ceil()  functions  demo  program
import math
print(math . floor(10.8))  # Previous  integer  of  10.8  i.e.  10
print(math . ceil(10.8))  # Next  integer  of  10.8  i.e.  11
print(math . floor(25.0))  # previous integer of 25.0 i.e 25
print(math . ceil(25.0))  # Next  integer  of  25.0  i.e.  25
print(math . floor(-3.5))  # previous integer of -3.5 i.e -4
print(math . ceil(-3.5))  # Next  integer  of  -3.5  i.e.  -3
print(math . floor(-9.0))  # previous integer of -9.0 i.e -9
print(math . ceil(-9.0))  # Next  integer  of  -9.0  i.e.  -9
print(math . floor(25.1))  # previous integer of 25.1 i.e 25
print(math . ceil(25.1))   # Next  integer  of  25.1  i.e.  26
# print(floor(3.5))  # Error because there is no floor() function in current module
# print(ceil(3.5))  # Error because there is no ceil() function in current module



#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))  # 35.8
print(abs(-27))  #27
print(abs(32))  # 32
import  builtins
print(builtins.abs(-25))  # 25


#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8, 20.6))  # 20.6
print(min(10.8, 20.6, 5.9, 12.3))  # 5.9
print(max(25, 10.8))  # 25
import  builtins
print(builtins . max(10, 20, 30))  # 30
print(builtins . min(10, 20, 15, 5, 12))  # 5



# Find outputs (Homework)
a = 20  # Assigns reference 'a' to int object 20
a %= 3+2 * 4  # a=a%(3+2*4)-->a=20%(3+8)-->a=20%(11)-->a=9
print(a)  # 9


# pow()  function  demo  program
from  builtins  import  pow
print(pow(10, -2))  # 10^-2= 0.01
print(pow(4, pow(3, 2)))  # 4^(3^2)= 262144
import  builtins
print(builtins . pow(2, 3))  # 2^3=8
print(builtins . pow(-2, -3))  # -2^-3=-0.125
