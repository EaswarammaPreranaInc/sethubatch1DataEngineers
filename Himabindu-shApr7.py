'''# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)  #How  to  print  variable  'x'  of  mod1  in  package  p1
mod1.f1()  #How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # error because p1 imported
print(p1 . init . x) # error 
print(init . x)  # error
'''

'''
# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)  #How  to  print  variable  'x'  of  mod1  in  package  p1
f1()   #How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1()  #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # error
print(p1 . init . x) # error
print(init . x) # error
from  p1  import  mod1 . * # error
'''

'''
# Save  in  any  file  of  cwd
import p1._init_  #How  to  import  init  module  of  package  p1  with  import  statement
print(p1.x)  #How  to  print  variable  'x'  of   init  module   in   package  p1
p1.f1()  #How  to  call  function  f1()  of   init  module  in  package  p1
a=p1.c1()
a.m1()  #How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
print(p1._init.x)  #How  to  print  variable  'x'  of   _init  module   in   package  p1  in  another  way
p1._init-.f1()  #How  to  call  function  f1()  of   init  module  in  package  p1  in  another  way
a=p1._init_.c1()  
a.m1()  #How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1  in  another  way
print(p1 . mod1 . x) #error
'''

'''
# Save  in  any  file  of  cwd
import   p1 # _init_ module is executed 
import  p1 . mod1 # imported mod1 of p1 and do not executed _init_ module 
from   p1   import  mod1 # imported mod1 of p1 and do not executed _init_ module 
from   p1 . mod1  import   *  
import  p1 . _init_ 
'''
