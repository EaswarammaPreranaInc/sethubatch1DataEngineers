'''
print('Begin')
import cal # How to import cal module with import statement
print( cal.x ) # How to print variable 'x' of cal module--->100
print( cal.y) # How to print variable 'y' of cal module--->200
#print(x) # Error due to no 'x' in current module
print(cal. add(10,7)) # How to call add () function of cal module by passing 10 and 7----->17
print ( cal . sub(10,7) ) # How to call sub () function of cal module by passing 10 and 7----->3
print ( cal. mul(10,7)) # How to call mul () function of cal module by passing 10 and 7-----> 70
print ( cal.div(10,7)) # How to call div () function of cal module by passing 10 and 7----->1.42
#print(add(cal .x ,cal . y)) # Error due to no add ()  function in cureent module
a = cal.c1 () # creates c1 class object
a.m1() # How to call m1() method of c1 xlass in cal module -----> m1 method
#b =  c1 () # Error due to no class c1 in curent module 
#cal . c1 . m1() # Error due to method can not be called thrw classname
#m1 () # Error due to no function m1() in the current module.


#2)#How to reuse mod2 from mod 1?

print('Before import')
import mod2 # How to import mod2
#print(x) # Error due to no x in current module
print(mod2.x) # 25
#f1() # Error due to no f1() in the current module
mod2.f1() # f1() function
print('After import')
#import mod4 # Module Not Found Error  bcz mod4 is not in same folder

#3)# find outputs 

import runpy
print('Before')
runpy . run_module('mod2') # How to run mod2 without import
#print(mod2.x) # Error due to mod 2 is not imported
#mod2. f1() # Error due to mod2 is not imported 
print('After')
#run_module('mod2') # Error due to there is no run_module() function in current module

#4) mod1.py
x = 10 
def disp():
	print('disp function of mod1')
class c1:
	def m1(self):
		print( ' m1 method of class c1 in mod1')


#5)# mod2.py
x = 20
def disp():
	print('disp function of mod2')
class c1:
	def m1(self):
		print('m1 method of class c1 in mod2')

#6)Find outputs

x = 30
def disp():
	print('disp function of same module')
class c1 :
	def m1(self):
		print('m1 method of class cl in same module')
from mod1 import * # 'x' is 10 replacing 30
from mod2 import * # 'x' is 20 replacing 10
print(x) # variable 'x' of mod2  i.,e 20
disp() # Function of mod2 is executed (last function)
a = c1() # create mod2 .c1 class object
a . m1() # methos of mod2 .c1 class is executed

#7)# Find outputs 

print('Begining of mod2')
import mod1 # All the statements of mod1 are imported but if statement is not executed
print('End of mod2')

#8) Homework:-
----------------
from cal import x,y, add,sub,div, mul, c1
 #How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle  with  from  statement
print(x) #How  to  print  variable  'x'  of  cal   module
print(y)
#print(cal . x) # Error
print(add (10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))
print(mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
a = c1() #How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1()

#2)Module  alias


print('Begin')
import cal as c #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) #How  to  print  variable  'x'  of  cal   module
print(c.y) #How  to  print  variable  'y'  of  cal   module
print(c.add(10,7))#How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(c.sub(10,7)) #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(c.mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(c.div(10,7))#How  to  call  div()  function  of  cal  module  by  passing  10  and  7
a = c #How  to  call  m1()  method  of  c1  class  in  cal  module
#print(cal . x) # Error due to there is no 'x' in current program
#from  math  as   m  import  * # Error due to there is no math function here s

#3)# Member  alias

from cal import x,y,add,mul,c1
import cal as c
 #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(x) #How  to  print  variable  'x'  of  cal   module
print(y)
print(add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
a = c1() #How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1()
print(add(10 , 7))
b = c1()

#4) Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)
disp()
a = c1()
a . m1()

#5) Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)
disp()
a = c1()
a . m1()

#6)How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
How  to  import  mod1  and  mod2

import mod1
import mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) #How  to  print  variable  'x'  of  mod1
mod1.disp() #How  to  call  disp()  function  of  mod1
a = mod1 . c1 #  How  to  call  method  m1()  of  class   c1  in  mod1
a.m1() 
print()
print(mod2.x) # How  to  print  variable  'x'  of  mod2
mod2.disp() # How  to  call  disp()  function  of  mod2
b = mod2. c1() # How  to  call  method  m1()  of  class   c1  in  mod2
b. m1() 
print()
print(x) # How  to  print  variable  'x'  of  current  module)
mod.disp () #How  to  call  disp()  function  of current  module
c=mod.c1()# How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()


#)How  to  use  members  of  all  the  three  modules  with  from  statement ?
How  to  import  members  of  mod1
How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1)
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(How  to  print  variable  'x'  of  mod2)
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module


'''


from mod1 import x as x_mod1, disp as disp_mod1, c1 as c1_mod1
from mod2 import x as x_mod2, disp as disp_mod2, c1 as c1_mod2

# Current module members
x = 30

def disp():
    print('disp function of same module')

class c1:
    def m1(self):
        print('m1 method of class c1 in same module')

# Print variable 'x' of mod1
print(x_mod1)

# Call disp() function of mod1
disp_mod1()

# Call method m1() of class c1 in mod1
obj1 = c1_mod1()
obj1.m1()

print()  # Separator for clarity

# Print variable 'x' of mod2
print(x_mod2)

# Call disp() function of mod2
disp_mod2()

# Call method m1() of class c1 in mod2
obj2 = c1_mod2()
obj2.m1()

print()  # Separator for clarity

# Print variable 'x' of the current module
print(x)

# Call disp() function of the current module
disp()

# Call method m1() of class c1 in the current module
obj3 = c1()
obj3.m1()
