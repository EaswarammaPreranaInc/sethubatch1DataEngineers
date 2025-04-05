
# Save  in  any  file  of  cwd
#  Save  in  any  file  of  cwd  (Homework)  
from p1 import mod1,mod2 #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x) #How  to  print  variable  'x'  of   mod1  in  package  p1
mod1.f1()#How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()
a.m1()  #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x) #How  to  print  variable  'x'  of   mod2  in  package  p1
mod2.f1() #How  to  call  function  f1()  of   mod2  in  package  p1
b=mod2.c1()
b.m1()#How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x) # error 
#print(x) # error  no x in the current module 

#  Save  in  any  file  of  cwd
from p1.mod1  import * #How  to  import  members  of  mod1  in  package  p1  with  from  statement
print(x) #How  to  print  variable  'x'  of   mod1  in  package  p1
f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()
a.m1()#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.mod2 import* #How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x) #How  to  print  variable  'x'  of   mod2  in  package  p1
f1() #How  to  call  function  f1()  of   mod2  in  package  p1
b=c1()
b.m1()#How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x) # error 
#print(mod1 . x) # error 
#from  p1   import  mod1 . * # error import clause cant have .  
'''
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x) # x=10 from mod2
f1() # mod 2 function 
a = c1()
a . m1() # method of mod2
'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs 
'''  
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   *
from  p1 . mod1    import   *
print(x) # 10
f1() # mod1 function 
a = c1()
a . m1() # od 1 methos  

''' (Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x) #30
f1() #function of same module  
a = c1()
a . m1() # method of class c1 in same module

'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from p1.mod1 import * #How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod2 import x as x2,f1 as f2,c1 as c2 #How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x)#How  to  print  variable  'x'  of   mod1  in  package  p1
f1()#How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()
a.m1()#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x2)#How  to  print  variable  'x'  of   mod2  in  package  p1
f2()#How  to  call  function  f1()  of   mod2  in  package  p1
a=c2()
a.m1()#How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
# Save  in  any  file  of  cwd
from p1 import mod1 #How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x) #How  to  print  variable  'x'  of   mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()#
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
#print(p1 . mod1 . x) # error 
print()
print()
from p1.p2 import mod2 # How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x) #How  to  print  variable  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1() #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=mod2.c1()
a.m1()#How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#print(p1 . p2 . mod2 . x) # error 
#from  p1  import   p2 . mod2 # error
#from  p2  import  mod2 # error  

# Save  in  any  file  of  cwd
from p1.mod1 import*  #How  to  import  members  of  mod1  in  p1  with  from  statement
print(x) #How  to  print  variable  'x'  of   mod1  in  package  p1
f1()#How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()
a.m1()#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2.mod2 import * #How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1  with  from  statement
print(x) #How  to  print  variable  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1()#How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=c1()
a.m1()#How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#from  p1  import  mod1 . * # error 
