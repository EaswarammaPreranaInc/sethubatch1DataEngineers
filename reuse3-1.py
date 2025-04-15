#  Save  in  any  file  of  cwd
from p1. _init_ import * # Executes _init_ module of package p1 automatically
print( x)  # How  to  print  variable  'x'  of  _init_ module in  package  p1
f1() # How  to  call  function  f1()  of  _init_ module  in  package  p1
a = c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in  _init_ module of  package  p1
#print(p1 . _init_ . x) # Error :  _init_ module  is not imported from cwd
#print(x) # Error : No 'x' in current module
#print(p1 . mod1 . x) # Error : mod1 is not imported from package p1.

'''
output:-

_init_ module of package _name_ is executed
10
package p1----> _init_ module---> f1 function
package p1----> _init_ module---> class c1 ------> m1 method


'''
