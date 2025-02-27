'''
#  Assignment  operators  demo  program  (Home  work)
a = 25 
print(a) #25 
b =  a  
print(b)  #25
print(a  is  b) # True
x = 4
y = 5
z = x + y * 6  
print(z)  #34
#25 = a  
#a + b = x + y

# Find outputs (Home work)
a = b = c = 25  
print(id(a)) #140733173728936
print(id(b)) #140733173728936
print(id(c)) #140733173728936
print(a , b , c) #25 25 25


# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'  
print(x) #25
print(y) #10.8
print(z) #Hyd

# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c #a=a*(b+c)--> a=3*9
print(a) # 27


# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 #a=a%(3+2*4)---->a=20%11-->a=9
print(a) #9


# Find outputs (Home work)
a = 3
a **= 4 # a= a**4-->3^4-->81
print(a) #81


# Identity operators demo program
a = 25
b = 25
print(a is b) # True
print(a is not b) #False
print(a == b) # True
'''


'''
Identity    operators
-------------------------
1) What  are  the  two  identity  operators ? --->  is  and  is  not

2) What  does  ref1  is  ref2  do ?  --->  Compares  references
     What  does   ref1 == ref2  do ?  ---> Compares  objects  pointed  by  ref1  and  ref2

3) What  is  the  result  of  ref1  is  ref2 ?  --->
														True  when  both  the  references  point  to  same  object  and  False  otherwise
    What  is  the  result  of  ref1  ==  ref2 ?  --->
	                                                             True  when  both  the  objects  have  same  value  and  False  otherwise

4) is  and  is  not  are  quite  opposite  operators


# Find outputs (Home work)
a = 25 
b = 25.0  
print(a is b) #False
print(a is not b) #True
print(a == b) #True

# Find outputs (Home work)
a = 'Hyd' 
b = 'Hyd' 
print(a  is  b) #True
print(a  is  not  b)  #False
print(a == b) #True
print() #empty 
x = [1 , 2 , 3 , 4]  
y = [1 , 2 , 3 , 4]  
print(x is y)  # False
print(x  is  not  y)  #true
print(x == y) #True
print() #empty
m = (1 , 2 , 3 , 4) 
n = (1 , 2 , 3 , 4)  
print(m  is  n)  #True
print(m  is  not  n)  #False
print(m == n)  #True

# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) #True
print(19 in list) #False
print(14 not in list) #True
print(15 not in list) #False
s = 'Hyd is green city'
print( 'is' in s)  #True
print('was' in s) #False
print('g' in s) # True
print('z' in s)  #False
print(' ' in s)  #True(spaces in string)
print('gre' in s) #True
print('yd i' in s) #True
print('' in s)    #True (empty string  is substring of every string)
print('' not in s) #False
'''


'''
Membership    operators
------------------------------
1) What  are  the  two  membership  operators ?  --->  in  and  not  in

2) What  is  the  syntax  of  'in'  operator ?  --->  element  in  sequence

3) What  does  in  operator  do ? --->  Returns  True  when  element  is  in  the  sequence  and  False  otherwise

4) What  does  not  in  operator  do ? --->  Quite  opposite  to  in  operator
'''

'''
#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a = 25
#print(a++) #  (a+)+  = a+ = 25+  throws  error
print(a++1)  # a + (+1)  =  25 + 1 = 26
print(--a)   #-(-a) = +a = 25
#print(a--)  #(a-)-= a+= 25+ = error 
print(a--1)  #(a-)-1 = a+1 = 25+1 = 26
print(-a)   #-25
print(+-a)  #+(-a) = -a = -25
print(-+a)  #-(+a) = -a = -25

#  Semicolon  demo  program
print('One'); #One
print('Two');  #Two
print('Three'); #Three
print('Hyd')  ; print('Sec')  ;  print('Cyb'); #Hyd <nextline> Sec<next line> Cyb 

#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  Previous  integer  of  10.8  i.e.  10
print(math . ceil(10.8))  #  Next  integer  of  10.8  i.e.  11
print(math . floor(25.0)) #25
print(math . ceil(25.0))  #25
print(math . floor(-3.5)) #-4
print(math . ceil(-3.5))  #-3
print(math . floor(-9.0)) #-9
print(math . ceil(-9.0))  #-9
print(math . floor(25.1))  #25
print(math . ceil(25.1))  #26
#print(floor(3.5))  #error fun() is not defined
#print(ceil(3.5))   #error fun() is not defined
'''


'''
1) What  does  floor(x)  do ?  --->  Returns  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  next  integer  of  'x'
'''
'''
#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))   #35.8
print(abs(-27))     #27
print(abs(29.5))    #29.5  
print(abs(32))     #32
import  builtins
print(builtins . abs(-25)) #25

#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))  #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #5.9
print(max(25 , 10.8)) #25
import  builtins
print(builtins . max(10 , 20 , 30)) #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5

# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))   #0.01
print(pow(4 , pow(3 , 2))) #4^9 -->262144
import  builtins
print(builtins . pow(2 , 3)) #8
print(builtins . pow(-2 , -3)) #-0.125
'''



 