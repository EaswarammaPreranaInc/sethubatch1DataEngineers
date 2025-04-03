'''
#1Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) Hint:  Use  startswith()  and  endswith()  methods  of  str  class

5) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables


#) 
import cal
a = []
for items in dir(cal):
	if not items. startswith('_') and not items.endswith('_'):
		a.append(items)
print(a)

#2) Find  outputs

print(dir()) # we get the members of current module ,here we dont have any members so we get Environmental variables.
print()
from  cal  import  * # import cal module all  members.
print()
print(dir()) # we get total imported cal module members.


outputs:-
-----------
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#3) Find  outputs

print(dir()) # we get the members of current module ,here we dont have any members so we get Environmental variables.
print()
from  cal  import  add , mul , x    # import cal module members, not all members we are calling specific members that are add, mul, x
print()
print(dir())  # we get  imported cal module specific members like add, mul, x .

outputs:-
----------
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']

'''
#4) Find  outputs
import  cal # imported cal module and statements of cal modules
print(cal . x) # 100
print(cal . y) # 200
print(cal . add(10 , 7)) # 17
print(cal . sub(10 , 7)) # 3
print(cal . mul(10 , 7)) # 70
print(cal . div(10 , 7)) # 1.4285714286
a = cal . c1()  # creating class object here
a . m1() # mi method ----> calling class method

outputs:-
---------
100
200
17
3
70
1.4285714285714286
m1 method
