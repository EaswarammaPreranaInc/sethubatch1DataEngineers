'''
#cal . py
x = 100
y = 200
def add(a , b):
	return a + b
def sub(a,b):
    return a - b
def mul(a , b): 
    return a * b
def div(a , b):
    return a / b
class c1:
	 def m1 (self) :
		 print ('m1 method')
'''

# 1. Find  outputs
import  cal
print(cal . x) #100
print(cal . y) #200
print(cal . add(10 , 7)) #17
print(cal . sub(10 , 7)) #3
print(cal . mul(10 , 7)) #70
print(cal . div(10 , 7)) #1.4285714285714286
a = cal . c1()
a . m1()		#m1 method

'''
2. Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) Hint:  Use  startswith()  and  endswith()  methods  of  str  class

5) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables

OUTPUT: ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
 '''
import cal
a=[]
b=dir(cal)
for mem in b:
	if mem.startswith('__') or mem.endswith('__'):
		pass
	else:
		a.append(mem)
print(a)


#3.  Find  outputs
print(dir()) # [Environment variable]
print()
from  cal  import  *
print()
print(dir()) # ['add','sub','mul','div',c1,Environment variable]
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''

# 4. Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']
'''