Ex-1:
a = 25   # reference 'a' points to Object 25
print(a)  # print Object value 25
b =  a   #  'a' reference is assign to reference 'b'
print(b)  # print same Object value 25
print(a  is  b)  # True
x = 4
y = 5
z = x + y * 6  # 4 + 5 * 6 = 34
print(z)  # 34
# 25 = a  # Error because reference 'a' can't assign to number
# a+b = x+y

Ex-2:-
a = b = c = 25 # 25 Object is assign multiple references 'a', 'b','c' at a time
print(id(a)) # print Object address of 25
print(id(b)) # print same address
print(id(c)) # print same address
print(a,b,c) # 25 25 25

Ex-3 :-
x , y , z = 25 , 10.8 , 'Hyd'  # multiple Objects assigns multiple references
print(x)  # 25
print(y) # 10.8
print(z) # 'Hyd'

Ex-4 :-
# Find outputs (Home work)
a , b , c = 3 , 4 , 5 # multiple Objects assigns multiple references
a *= b + c # a * = 4+5 => a = 3 * 9 = 27
print(a)  # 27

Ex-5 :-
a = 20             # reference 'a' points to Object 20
a %= 3 + 2 * 4     # a % = 3 + 2 * 4 => 20%9 =11
print(a)           # 11

Ex-6:-
a = 3    # reference 'a' points to Object 3
a **= 4  # a = 3 ** 4 = 3 ^ 4 =81
print(a) # 81

Ex-7:-
a = 'Hyd'   # 'Hyd' is assign to reference 'a'
b = 'Hyd'  # reference 'b' points to same Object 'Hyd'
print(a  is  b)          # True
print(a  is  not  b)     # False
print(a == b)            # True
print()
x = [1 , 2 , 3 , 4]  # list Object is assign to reference 'x'
y = [1 , 2 , 3 , 4]  # another list Object assign to reference 'y'
print(x is y)        # False
print(x  is  not  y)  # True
print(x == y)         # True
print()
m = (1 , 2 , 3 , 4)   # tuple Object is  assign to reference 'm'
n = (1 , 2 , 3 , 4)    # reference 'n' points to same tuple Object
print(m  is  n)        # True
print(m  is  not  n)   #  False
print(m==n)             # True


Ex-8 :-
from  builtins  import  abs
print(abs(-35.8))         # 35.8
print(abs(-27))           # 27
print(abs(29.5))         # 29.5
print(abs(32))          # 32
import  builtins
print(builtins.abs(-25)) # 25

Ex-9:-
from  builtins  import   max , min
print(max(10.8 , 20.6))              # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8))                # 25
import  builtins
print(builtins . max(10 , 20 , 30))  # 30
print(builtins . min(10,20,15,5,12)) # 5


Ex-10:-
from  builtins  import  pow
print(pow(10 , -2))                    # 10 ^ -2 = 0.01
print(pow(4 , pow(3 , 2)))            # pow(4 , 3 ^ 2) = pow(4,9) = 262144
import  builtins
print(builtins.pow(2 , 3))  # 2 ^ 3 =8
print(builtins.pow(-2,-3))             # -2 ^ -3 = -0.125
