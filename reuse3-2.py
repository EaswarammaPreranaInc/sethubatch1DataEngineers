#  Save  in  any  file  of  cwd
import p1.mod1  # Executes _init_ module of package p1 automatically
print(p1.mod1.x) # How  to  print  variable  'x'  of  mod1  in  package  p1
p1.mod1.f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = p1.mod1. c1()
a.m1() #      How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
from p1. _init_ import*
print(x) # How to print variable 'x' of _init_ module in package p1
f1() # How to call function f1() of _init_ module in package p1
a = c1()
a.m1() # How to call  method m1 () of class c1 in the  _init_ module in package p1

'''
output:-

20
 p1-----> mod1---> f1 function
 p1-----> mod1---> c1-----> m1 method


_init_ module of package _name_ is executed
10
package p1----> _init_ module---> f1 function
package p1----> _init_ module---> class c1 ------> m1 method

'''

