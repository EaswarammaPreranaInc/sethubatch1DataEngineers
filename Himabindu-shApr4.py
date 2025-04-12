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

1) What  is  the  result  of  'name' . startswith('')  ?  --->  True

2) What  is  the  result  of  'spec' . endswith('')  ?  --->  True

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
	if a[i].startswith('')==False:
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
['_annotations', 'builtins', 'cached', 'doc', 'file', 'loader', 'name', 'package', 'spec_']


['_annotations', 'builtins', 'cached', 'doc', 'file', 'loader', 'name', 'package', 'spec_', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''


'''
#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())

#outputs:
['_annotations', 'builtins', 'cached', 'doc', 'file', 'loader', 'name', 'package', 'spec_']


['_annotations', 'builtins', 'cached', 'doc', 'file', 'loader', 'name', 'package', 'spec_', 'add', 'mul', 'x']
'''
