'''#  Find  outputs
import  cal
print(cal . x)
print(cal . y)
print(cal . add(10 , 7))
print(cal . sub(10 , 7))
print(cal . mul(10 , 7))
print(cal . div(10 , 7))
a = cal . c1()
a . m1()
'''

'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) Hint:  Use  startswith()  and  endswith()  methods  of  str  class

5) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables

from cal import *
#print(dir())
a=[]
for x in dir():
	a.append(x)
b=[]
for i in range(len(a)):
	if a[i].startswith('__')==False:
		b.append(a[i])
print(b)
'''



'''
#  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())
#outputs:
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''


'''
#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())

#outputs:
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']
'''
