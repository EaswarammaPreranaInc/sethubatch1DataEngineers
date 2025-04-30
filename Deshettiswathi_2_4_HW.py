
Q1 # How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1  #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle  with  from  statement
print(x) #How  to  print  variable  'x'  of  cal   module  - 100
#print(y)  #error - y is not in cuurent module and also not imported from cal module
#print(cal . x) #error - cal module is not imported
print(add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)  - 17 
#print(sub(10 , 7)) #sub is not imported
print(mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7) - 70
#print(div(10 , 7)) #error - div is not imported
a=c1()
a.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module -- m1 method
#---------------------------------------------------------------------------------------------------------------------------------
Q2 # Module  alias
print('Begin') #Begin
import cal as c #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) #How  to  print  variable  'x'  of  cal   module -------- #100
print(c.y) #How  to  print  variable  'y'  of  cal   module -------- #200
print(c.add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7 ---#17 
print(c.sub(10,7)) #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7 ---#3
print(c.mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7 ---#70
print(c.div(10,7))  #How  to  call  div() function  of  cal  module  by  passing  10  and  7---#1.4285714285714286
a=c.c1()  #How  to  call  m1()  method  of  c1  class  in  cal  module
a.m1()  #m1 method
#print(cal . x) #error - cal module is not imported
#from  math as m import  *   #error- invalid syntax -cannot use 'as' when '*' is used
#-----------------------------------------------------------------------------------------------------------------------------------
Q3 #Member  alias
from cal import x as X,add as Add,mul as Mul,c1 as C1   #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(X) #How  to  print  variable  'x'  of  cal   module --------#100
#print(x) #error - x is not defined
print(Add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7 ---------#17
print(Mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7 ---------#70
a=C1()   #How  to  call  m1()  method  of  class  c1  in  cal  module
a.m1() #m1 method
#print(add(10 , 7)) #error- add is not defined
#b = c1() #error - c1 is not defined
#----------------------------------------------------------------------------------------------------------------
Q4 # Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2_02_04  import   *
from  mod1_02_04  import   *
print(x)   #10
disp()     #disp function of mod1
a = c1()
a . m1()   #m1 method of class c1 of mod1
#--------------------------------------------------------------------------------------------------------------
Q5 #Find outputs  (Home  work)
from  mod1_02_04  import  *
from  mod2_02_04  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)   #30
disp()     #disp  function  of  same  module
a = c1()
a . m1()   #m1  method of  class  c1  in  same  module
#---------------------------------------------------------------------------------------------------------------
Q6 #How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?

import mod1_02_04,mod2_02_04 #How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1_02_04.x) #How  to  print  variable  'x'  of  mod1
mod1_02_04.disp() #How  to  call  disp()  function  of  mod1
a=mod1_02_04.c1()  #How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print(mod2_02_04.x) #How  to  print  variable  'x'  of  mod2
mod2_02_04.disp() #How  to  call  disp()  function  of  mod2
b=mod2_02_04.c1() #How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print(x) #How  to  print  variable  'x'  of  current  module)
disp()   #How  to  call  disp()  function  of current  module
c=c1()   #How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()

OP-
10
disp function of mod1
m1 method of class c1 of mod1

20
disp function of mod2
m1 method of class c1 of mod2

30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
#-------------------------------------------------------------------------------------------------------------------
Q7 #How  to  use  members  of  all  the  three  modules  with  from  statement ?

from mod1_02_04 import x as x1,disp as disp1,c1 as C1 #How  to  import  members  of  mod1
from mod2_02_04 import x as x2,disp as disp2,c1 as C2 #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1) #How  to  print  variable  'x'  of  mod1)
disp1()  #How  to  call  disp()  function  of  mod1
a= C1() #How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print()
print(x2) #How  to  print  variable  'x'  of  mod2)
disp2() #How  to  call  disp()  function  of  mod2
b= C2() #How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print()
print(x) #How  to  print  variable  'x'  of  current  module)
disp() #How  to  call  disp()  function  of current  module
c= c1() #How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()

OP-
10
disp function of mod1
m1 method of class c1 of mod1


20
disp function of mod2
m1 method of class c1 of mod2


30
disp  function  of  same  module
m1   method  of  class  c1  in  same  module
