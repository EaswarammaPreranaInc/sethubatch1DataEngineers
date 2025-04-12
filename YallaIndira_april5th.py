'''# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)  #How  to  print  variable  'x'  of  mod1  in  package  p1
mod1.f1()  #How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # error because p1 imported
print(p1 . _init_ . x) # error 
print(_init_ . x)  # error
'''

'''
# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)  #How  to  print  variable  'x'  of  mod1  in  package  p1
f1()   #How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1()  #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # error
print(p1 . _init_ . x) # error
print(_init_ . x) # error
from  p1  import  mod1 . * # error
'''

'''
# Save  in  any  file  of  cwd
import p1.__init__  #How  to  import  _init_  module  of  package  p1  with  import  statement
print(p1.x)  #How  to  print  variable  'x'  of   _init_  module   in   package  p1
p1.f1()  #How  to  call  function  f1()  of   init  module  in  package  p1
a=p1.c1()
a.m1()  #How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
print(p1.__init__.x)  #How  to  print  variable  'x'  of   _init_  module   in   package  p1  in  another  way
p1.__init_-.f1()  #How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a=p1.__init__.c1()  
a.m1()  #How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1 . mod1 . x) #error
'''

'''
# Save  in  any  file  of  cwd
import   p1 # __init__ module is executed 
import  p1 . mod1 # imported mod1 of p1 and do not executed __init__ module 
from   p1   import  mod1 # imported mod1 of p1 and do not executed __init__ module 
from   p1 . mod1  import   *  
import  p1 . __init__ 
'''
