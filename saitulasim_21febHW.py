#1 PROGRAM

a = 25 
print(id(a)) #random address 
b =  a  
print(id(b))   # same address 
print(a  is  b)  #True
x = 4
y = 5
z = x + y * 6  
print(z)  #34
a = 25 
print(a)  #25
a = x + y+ b  #34
print(a)

#2 PROGRAM
a = b = c = 25  
print(id(a)) #random address 
print(id(b)) # samE address
print(id(c)) # same address
print(a , b , c)  #25 25 25

#3 PROGRAM
x , y , z = 25 , 10.8 , 'Hyd'  
print(x) #25
print(y) #10.8
print(z) #'Hyd'

#4 PROGRAM
a , b , c = 3 , 4 , 5
a *= b + c
print(a) #27

#5 PROGRAM
a = 20
a %= 3 + 2 * 4 
print(a) #9

#6 PROGRAM
a = 3
a **= 4 
print(a) #81

#7 PROGRAM
a = 25
b = 25
print(a is b) #True
print(a is not b) #False
print(a == b) # True

#8 PROGRAM
a = 25 
b = 25.0  
print(a is b) #False
print(a is not b) #True
print(a == b) #True

#9 PROGRAM
a = 'Hyd' 
b = 'Hyd' 
print(a  is  b) # True
print(a  is  not  b)  #False
print(a == b) #True
print()
x = [1 , 2 , 3 , 4]  
y = [1 , 2 , 3 , 4]  
print(x is y) #False
print(x  is  not  y) #True 
print(x == y) #True
print()
j=(1,2,3,4)
u=(1,2,3,4)
print(j is u) #False
print(j is not u) #True
print(j==u) #True

#10 PROGRAM
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) #True
print(19 in list) #False
print(14 not in list) #True
print(15 not in list) #False
s = 'Hyd is green city'
print( 'is' in s) #True
print('was' in s) #False
print('g' in s) #True
print('z' in s) #False
print(' ' in s) #True
print('gre' in s) #True
print('yd i' in s) #True
print('' in s)  #True
print('' not in s) #False

#11 PROGRAM
a = 25
print(++a)  #  +(+a) = +a = 25
#print(a++) #  (a+)+  = a+ = 25+  throws  error
print(a++1)  # a + (+1)  =  25 + 1 = 26
print(--a) #-(-a) = +25
#print(a--) #(a-)- = a+ error
print(a--1) # a-(-1)= a+1= 26
print(-a) #-25
print(+-a) #+(-a)=-25
print(-+a) #-(+a)=-25

#12 PROGRAM
print('One'); #optional semicolon string as output 
print('Two'); #optional semicolon string as output 
print('Three'); # "
print('Hyd')  ;  # "
print('Sec')  ;   # "
print('Cyb'); #optional semicolon string as output 

#13 PROGRAM
import  math
print(math . floor(10.8))  #  Previous  integer i.e.  10
print(math . ceil(10.8))  #  Next  integer i.e.11
print(math . floor(25.0)) #25
print(math . ceil(25.0)) #25
print(math . floor(-3.5)) #-4
print(math . ceil(-3.5)) #-3
print(math . floor(-9.0)) #-9
print(math . ceil(-9.0)) #-9
print(math . floor(25.1)) #25
print(math . ceil(25.1)) #26
#print(floor(3.5)) #error
#print(ceil(3.5)) #error

#14 PROGRAM
from  builtins  import  abs #not required
print(abs(-35.8)) #35.8
print(abs(-27)) #27
print(abs(29.5)) #29.5
print(abs(32)) #32
import  builtins #not required
print(builtins . abs(-25)) #25

#15 PROGRAM
from  builtins  import   max , min #not required
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #5.9
print(max(25 , 10.8)) #25
import  builtins #not required
print(builtins . max(10 , 20 , 30)) #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5

#16 PROGRAM
from  builtins  import  pow  #not required
print(pow(10 , -2)) #0.01
print(pow(4 , pow(3 , 2))) #4^9
import  builtins  #not required
print(builtins . pow(2 , 3)) #8
print(builtins . pow(-2 , -3)) #error
