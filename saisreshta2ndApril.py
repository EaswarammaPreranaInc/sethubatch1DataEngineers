program1:
from cal import * # How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle  with  from  statement
print(x) #How  to  print  variable  'x'  of  cal   module
print(y) # error
#print(cal . x) # error 
print(add(10,7))  #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))
print(mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
a=c1() 
a.m1()  #How  to  call  m1()  method  of  class  c1  in  cal  module

program2:
# Module  alias
print('Begin')
import cal as c #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) #How  to  print  variable  'x'  of  cal   module
print(c.y) #How  to  print  variable  'y'  of  cal   module
print(c.add(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(c.sub(10,7)) #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(c.mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(c.div(10,7)) #How  to  call  div()  function  of  cal  module  by  passing  10  and  7
a=c.c1() #How  to  call  m1()  method  of  c1  class  in  cal  module
a.m1()
#print(cal . x) # error cal is not imported 
#from  math  as   m  import  * # error

program3:
# Member  alias
from cal import x as X, add as a,mul as m,c1 as C #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(X) #How  to  print  variable  'x'  of  cal   module
#print(x) # error
print(a(10,7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(m(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
i=C() #How  to  call  m1()  method  of  class  c1  in  cal  module
i.m1()
#print(add(10 , 7)) # error
#b = c1() # error

program4:
# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) # 10
disp() # disp  function  of mod1
a = c1()
a . m1() # 'm1  method of  class  c1  in mod1

program5:
# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) # 30
disp() # disp  function  of  same  module
a = c1()
a . m1() # m1  method of  class  c1  in  same  module

program6:
# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1,mod2  #How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) #How  to  print  variable  'x'  of  mod1
mod1.disp() #How  to  call  disp()  function  of  mod1
a=mod1.c1() #How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print(mod2.x) #How  to  print  variable  'x'  of  mod2
mod2.disp() #How  to  call  disp()  function  of  mod2
b=mod2.c1() #How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print(x) #How  to  print  variable  'x'  of  current  module)
disp() #How  to  call  disp()  function  of current  module
c=c1() #How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()
