'''
#1)Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1. x) # How  to  print  variable  'x'  of  mod1  in  package  p1
mod1 .f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1 . c1() 
a. m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
#print(p1 . x) # Error : No 'x ' in current program
#print(p1 . _init_ . x) # Error : p1 is not imported here
#print(_init_ . x) # Error : _init is not imported here



output:-
20
 p1-----> mod1---> f1 function
 p1-----> mod1---> c1-----> m1 method

 
 #2)Save  in  any  file  of  cwd

from  p1 . mod1   import  *
print(x) # How  to  print  variable  'x'  of  mod1  in  package  p1
f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = c1() 
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
#print(p1 . x) # Error there is no 'x' in current program
#print(p1 . _init_ . x) # Error : p1 is not imported here
#print(_init_ . x) # Error : _init_ is not imported here
#from  p1  import  mod1 . * # Error : due to '.'

output:-
 20
 p1-----> mod1---> f1 function
 p1-----> mod1---> c1-----> m1 method

 
 #3) Save  in  any  file  of  cwd
from p1 import _init_ # How  to  import  _init_  module  of  package  p1  with  import  statement
print(_init_ . x) # How  to  print  variable  'x'  of   _init_  module   in   package  p1
_init_ .f1() # How  to  call  function  f1()  of   init  module  in  package  p1
a = _init_. c1() # How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
a.m1()
from p1._init_ import*
print(x) # How  to  print  variable  'x'  of   _init_  module   in   package  p1  in  another  way
f1() # How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a = c1() 
a.m1() # How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
#print(p1 . mod1 . x) # Error due to '.'


output:-

init_ module of package _name_ is executed
10
package p1----> _init_ module---> f1 function
package p1----> _init_ module---> class c1 ------> m1 method
10
package p1----> _init_ module---> f1 function
package p1----> _init_ module---> class c1 ------> m1 method
'''

#4) Save  in  any  file  of  cwd
import   p1 # importing p1 package only
import  p1 . mod1 # importing mod1 module of package p1
from   p1   import  mod1 # importing  mod1 module of package p1
from   p1 . mod1  import   * # importing mod1 module of package p1
import  p1 . _init_ # importing _init_  module of package p1 ----> we get last imported module executed --->_init_ module of package _name_ is executed.
