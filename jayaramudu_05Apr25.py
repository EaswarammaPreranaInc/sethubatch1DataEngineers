#Ex-1
from  p1   import  mod1
print(mod1.x) #  How  to  print  variable  'x'  of  mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1.c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
# print(p1 . x) # Error p1 not imported  p1 is a sub package
# print(p1 . _init_ . x) # Error: __init__ is not directly accessible like that
# print(__init_.x) # Error because  __init__ is not imported

#Ex-2
# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x) #  How  to  print  variable  'x'  of  mod1  in  package  p1
f1() #  How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1()# How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
#print(p1 . x) # # Error p1 not imported  p1 is a sub package
#print(p1 . _init_ . x) # p1 not imported
# print(_init_ . x) # Error: __init__ is not directly accessible
#from  p1  import  mod1 .* # Error because after import clause . is not permitted

#Ex-3
import p1 #  How  to  import  _init_  module  of  package  p1  with  import  statement
print(p1.x) # How  to  print  variable  'x'  of   _init_  module   in   package  p1
p1.f1()   # How  to  call  function  f1()  of   init  module  in  package  p1
a=c1()
a.m1()# How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
from p1 import x
print(x)   # How  to  print  variable  'x'  of   _init_  module   in   package  p1  in  another  way
from p1 import f1
f1()  # How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
from p1 import c1
a=c1()
a.m1() # How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1.mod1.x)

#Ex-4
import   p1                   # p1 imported and executed __init__
import  p1 . mod1             # import mod1 inside p1
from   p1   import  mod1     #  import mod1 inside p1 we have call members mod1.x mod1.f1() like
from   p1 . mod1  import *  # all members imported from mod1
import p1 .__init__         # when import p1 ,__init__ executed
