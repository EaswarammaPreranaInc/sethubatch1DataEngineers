'''
#1) Save  in  any  file  of  cwd
from p1. mod1 import*  #How  to  import  members  of  mod1  in  package  p1  with  from  statement
print(x) # How  to  print  variable  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1. mod2 import* # How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x) # How  to  print  variable  'x'  of   mod2  in  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  package  p1
a = c1() #
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x) # Error due to mod1 is not there in current module 
#print(mod1 . x) # Error due to mod1 is not there in current module
#from  p1   import  mod1 . * # Error due to '.'.



#2)Save  the  following  code  in    any  file  of  cwd
Find  outputs

x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    * # first we are imported mod1 from package p1
from  p1 . mod2    import    * # second we are imported mod2 from package p1
print(x) # 30 ---here it will prints last imported module(mod2) value of 'x'
f1() #  p1-----> mod2----> f1 function  --->here it will prints last imported module(mod2)  function f1()
a = c1() # ----> creating object for class c1()  here it will calls last imported module (mod2) class c1()
a . m1() #  p1--->mod2--->c1---->m1 method ---> here it will prints last imported module(mod2) method m1()

#3)(Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs

x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   * # first we are imported mod2 from package p1
from  p1 . mod1    import   * # second we are imported mod1 from package p1
print(x) # 10---here it will prints last imported module(mod1) value of 'x'
f1() # p1-----> mod1----> f1 function -----here it will prints last imported module(mod1) value of 'x'
a = c1() # ----> creating object for class c1()  here it will calls last imported module (mod1) class c1()
a . m1() # p1--->mod1--->c1---->m1 method ---> here it will prints last imported module(mod2) method m1()

#4)(Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs

from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x) # 30
f1() # Function  of  same  module----> current module executed
a = c1()
a . m1() # Method  of  class  c1  in same  module-----> current module executed

#5)(Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from p1 import mod1, mod2 # How  to  import   members  of  mod1   in  package  p1  with  from  statement
# How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(mod1.x) # How  to  print  variable  'x'  of   mod1  in  package  p1
mod1. f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1. c1() 
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x) # How  to  print  variable  'x'  of   mod2  in  package  p1
mod2. f1() # How  to  call  function  f1()  of   mod2  in  package  p1
a = mod2.c1() 
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1

output:-
--------
10
p1-----> mod1----> f1 function
p1--->mod1--->c1---->m1 method


30
p1-----> mod2----> f1 function
p1--->mod2--->c1---->m1 method
