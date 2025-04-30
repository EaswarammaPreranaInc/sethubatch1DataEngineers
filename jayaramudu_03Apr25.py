#Ex-1
#  Find  outputs
import  cal # import only module
print(cal . x) # 100
print(cal . y) # 200
print(cal . add(10 , 7)) # 17
print(cal . sub(10 , 7)) # 3
print(cal . mul(10 , 7)) # 70
print(cal . div(10 , 7)) # 1.42
a = cal.c1() # create object class c1
a.m1() # call c1 object method # m1 method

#Ex-2

'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) Hint:  Use  startswith()  and  endswith()  methods  of  str  class

5) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment variables
'''
from cal import  *
a = dir()
b = []
for x in a:
    if not x.startswith('__') and not x.endswith('__'):
        b.append(x)
print(b)

print()
print()

#Ex-3
#  Find  outputs
print(dir()) # Environment variables of current module
print()
from  cal  import  *  # Environment variables  ,__all_ members of cal module
print()
print(dir()) # Environment variables ,__all__ members

#Ex-4
#  Find  outputs
print(dir()) #  Environment variables of current module
print()
from  cal  import  add , mul , x
print()
print(dir()) # Environment variables of current module , add , mul , x
