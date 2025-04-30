
Q1 # Find  outputs
import  cal
print(cal . x) #100
print(cal . y) #200
print(cal . add(10 , 7)) #17
print(cal . sub(10 , 7)) #3
print(cal . mul(10 , 7)) #70
print(cal . div(10 , 7)) #1.4285714285714286
a = cal . c1()
a . m1()                  #m1 method
#--------------------------------------------------------------------------------------------------------------------------------
Q2 #Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

from cal import *
a=[]
for x in dir():
	if not x.startswith('__') and x!='a':
		a.append(x)
print(a)
#------------------------------------------------------------------------------------------------------------------------------------
Q3 #Find  outputs
print(dir()) #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  *
print()
print(dir()) #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Q4 #Find  outputs
print(dir()) #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  add , mul , x
print()
print(dir()) #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']
