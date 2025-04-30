#  Assignment  operators  demo  program  (Home  work)
a = 25 # a is assigned to 25
print(a)  # 25 value of a is displayed
b =  a  # id of a is copied to b
print(b)  # 25
print(a  is  b)  # references of a and b are compared which is true 
x = 4 # x is assigned 4
y = 5 # y is assigned 5
z = x + y * 6  #  z=4+5*6 --- z=34
print(z)  #34
# 25 = a   error we have varable on right hand side
# a+b=x+y # reference can’t be expression 

# Find outputs (Home work)
a = b = c = 25  # reference a,b,c points to same object 25
print(id(a)) # address of a is shown 
print(id(b)) # same address
print(id(c)) # same address
print(a,b,c)# 25 25 25

# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'  # x = 25 y=10.8 z='Hyd' 
print(x) #25
print(y) #10.8
print(z) # 'Hyd'

# Find outputs (Home work)
a , b , c = 3 , 4 , 5 # a=3 b=4 c=5
a*= b+c # a= a*(b+c) = 27
print(a) # 27

# Find outputs (Home work)
a=20 # a assigned to 20
a%=3+2*4  # a=a% (3+ (2*4)) 
print(a)# 9

# Find outputs (Home work)
a=3 # a assigns to 3
a**=4# a= a**4 
print(a)#81

a = 25
b = 25
print(a is b)
print(a is not b)
print(a == b)

a = 25 
b = 25.0  
print(a is b) # False
print(a is not b)# True
print(a==b)# True

# Find outputs (Home work)
a = 'Hyd' 
b = 'Hyd' 
print(a  is  b) # True
print(a  is  not  b) #False
print(a == b) # True
print() # Error
x = [1 , 2 , 3 , 4]  
y = [1 , 2 , 3 , 4]  
print(x is y)# False
print(x  is  not  y) # True
print(x == y) # True
print() # FAlse
m = (1 , 2 , 3 , 4) 
n = (1 , 2 , 3 , 4)  
print(m is n) # True
print(m is not n)# FAlse
print(m == n)# True

list = [10 , 20 , 15 , 12 , 18]
print(15 in list) # True
print(19 in list) # False
print(14 not in list)# True
print(15 not in list) # FALse
s = 'Hyd is green city'
print( 'is' in s) # True
print('was' in s) # False
print('g' in s) # True
print('z' in s) # False
print(' ' in s) # True
print('gre' in s)#True
print('yd i' in s)# TRue
print('' in s)# True
print('' not in s)# False

#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a = 25
#print(a++) #  (a+)+  = a+ = 25+  throws  error
print(a++1)  # a + (+1)  =  25 + 1 = 26
print(--a)# (-) - a =25
#print(a--)3 #error
print(a--1) # a - (-1) = 26
print(-a) # -25
print(+-a) # -25
print(-+a)# -25

#  Semicolon  demo  program
print('One'); # One
print('Two'); # Two
print('Three'); # Three
print('Hyd') ; print('Sec') ;  print('Cyb'); # : is mandaotry bcz multiple statements are in the same line .. we also use , (comma) instead of ;  Hyd < next line > Sec < Next Line > Cyb < next line >

#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  Previous  integer  of  10.8  i.e.  10
print(math . ceil(10.8))  #  Next  integer  of  10.8  i.e.  11
print(math . floor(25.0)) # 25
print(math . ceil(25.0))# 25
print(math . floor(-3.5))# -4
print(math . ceil(-3.5)) # -3
print(math . floor(-9.0))# -9
print(math . ceil(-9.0))# -9
print(math . floor(25.1))# 25
print(math . ceil(25.1))#26
#print(floor(3.5))# there is no floor function in the current module 
#print(ceil(3.5))# ''

#  abs()  function  demo  program
from  builtins  import  abs # optional bcz abs is automatically imported 
print(abs(-35.8))# 35.8
print(abs(-27))#27
print(abs(29.5))# 29.5
print(abs(32))# 32
import  builtins # mandatory bcz builtins is not imported 
print(builtins . abs(-25))#25

#  max()  and  min()   functions  demo  program
from  builtins  import   max , min # optional bcz  max and min are automatically imported
print(max(10.8 , 20.6)) # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))# 5.9
print(max(25 , 10.8))#25
import  builtins # mandatory
print(builtins . max(10 , 20 , 30)) # 30
print(builtins . min(10 , 20 , 15 , 5 , 12))# 5

# pow()  function  demo  program
from  builtins  import  pow # not mandatory
print(pow(10 , -2)) # 0.01
print(pow(4 , pow(3 , 2)))#262144
import  builtins # mandatory to declare 
print(builtins . pow(2 , 3)) # 8
print(builtins . pow
