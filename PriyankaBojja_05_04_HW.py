Q1 # Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)     #How  to  print  variable  'x'  of  mod1  in  package  p1
mod1.f1()         #How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1()
a.m1()            #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
#print(p1 . x)     #error - p1 is not imported and p1 is package but not module to access member
#print(p1 . _init_ . x) # error - p1 is not imported
#print(_init_ . x)      #error - __init__ is not imported

OP-
__init__ module of package  p1 is executed
20
p1 -----> mod1 -----> f1 function
p1 -----> mod1 -----> c1 -----> m1 method
#-------------------------------------------------------------------------------
Q2 #Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)     #How  to  print  variable  'x'  of  mod1  in  package  p1
f1()         #How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()     
a.m1()       #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
#print(p1 . x) #error - p1 is not imported
#print(p1 . _init_ . x)  # error - p1 is not imported
#print(_init_ . x)       #error - __init__ is not imported
#from  p1  import  mod1 . *  #error - '.' cannot be used in import

OP-
__init__ module of package  p1 is executed
20
p1 -----> mod1 -----> f1 function
p1 -----> mod1 -----> c1 -----> m1 method
#-----------------------------------------------------------------------------------------------------------------
Q3 #Save  in  any  file  of  cwd
import p1.__init__   #How  to  import  _init_  module  of  package  p1  with  import  statement
print(p1.x)          #How  to  print  variable  'x'  of   _init_  module   in   package  p1
p1.f1()              #How  to  call  function  f1()  of   init  module  in  package  p1
a=p1.c1()
a.m1()                     #How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
print(p1.__init__.x)                   #How  to  print  variable  'x'  of   _init_  module   in   package  p1  in  another  way
p1.__init__.f1()                       #How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a=p1.__init__.c1() 
a.m1()                     #How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
#print(p1 . mod1 . x)       #error - mod1 is not imported

OP-
__init__ module of package  p1 is executed
__init__ module of package  p1.__init__ is executed
10
package p1 ---> __init__module ---> f1 function
package p1 ---> __init__ module ---> class c1 ---> m1 method
10
package p1 ---> __init__module ---> f1 function
package p1 ---> __init__ module ---> class c1 ---> m1 method
#------------------------------------------------------------------------------------------------------------------
# Save  in  any  file  of  cwd
import   p1                     #  __init__ module of package  p1 is executed
import  p1 . mod1               
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . __init__           #  __init__ module of package  p1.__init__ is executed
