#Find outputs
import cal
print(cal.x) #100
print(cal.y) #200
print(cal.add(10,7)) #17
print(cal.sub(10,7)) #3
print(cal.mul(10,7)) #70
print(cal.div(10,7)) #1.428
a=cal.c1()
a.m1() #m1 method

#Print all the members of cal module without environment varaiables
import cal
d=dir(cal)
res=[]
for x in d:
	if not x.startswith('__') and not x.endswith('__'):
		res.append(x)
print(res) #['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#Find outputs
print(dir()) #[environment variables] 
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print() #<next line>
from cal import *
print() #<next line>
print(dir()) #[environment variables,'add','div','mul','sub','x','y']
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#Find outputs
print(dir()) #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print() #<next line>
from cal import add,mul,x
print()
print(dir()) #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul','x']
