
#Ex-1
# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from  cal import *  #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle  with  from  statement
print(x)      # How  to  print  variable  'x'  of  cal   module
print(y)
#print(cal . x) # Error because cal not imported
print(add(10,7))  # How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))
print(mul(10,7))  # How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
a = c1()  # How  to  call  m1()  method  of  class  c1 in cal module
a.m1()

#Ex-2
# Module  alias
print('Begin')
import cal as m # How  to  import  cal  module  with   another  name  using  import  statement
print(m.x)  # How  to  print  variable  'x'  of  cal   module
print(m.y) #  How  to  print  variable  'y'  of  cal   module
print(m.add(10,7))  # How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(m.sub(10,7))  #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(m.mul(10,7))#How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(m.div(10,7))    # How  to  call  div()  function  of  cal  module  by  passing  10  and  7
a = m.c1()
a.m1()# How  to  call  m1()  method  of  c1  class  in  cal  module
#print(cal . x) # Error because cal module given alternate name
# from  math  as m  import  *  # Error because invalid syntax

#Ex-3
# Member  alias
from cal import x as var_x,add as add_f ,sub as sub_f,mul as mul_f,div as div_f, c1 as c1_cl# How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(var_x) # How  to  print  variable  'x'  of  cal   module
# print(x) # error x is given another name
print(add_f(10,7)) #   How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(mul_f(10,7))  #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
a=c1_cl()
a.m1()         # How  to  call  m1()  method  of  class  c1  in  cal  module
# print(add(10,7)) # Error beacuse add method not define in current program
#b= c1() # Error becoz c1 class imported and given alternative name

#Ex-4
# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   * # x value is 20 of mo2
from  mod1  import   * # x value is 10 of mod1
print(x)  # x value is 10 of mod1
disp() # disp() mod1
a =c1() # class c1 of mod1
a.m1() # class c1 of method in mod1


#Ex-5
# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) # print  variable  'x'  of  current  module
disp() # call disp current  module
a=c1() # create object current  module
a.m1() # call current  module class c1 method

#Ex-6
# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1 ,mod2, mod3 #How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) # How  to  print  variable  'x'  of  mod1
mod1.disp() #How  to  call  disp()  function  of  mod1
a = mod1.c1()
a.m1()# How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x) #How  to  print  variable  'x'  of  mod2
mod2.disp()  # How  to  call  disp()  function  of  mod2
a = mod2.c1()
a.m1()# How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(x) # How  to  print  variable  'x'  of  current  module)
disp()# How  to  call  disp()  function  of current  module
a= c1()
a.m1()#How  to  call  method  m1()  of  class   c1  in  current module

#Ex-7
# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import x as x1, disp as disp1, c1 as c1_mod1
from mod2 import x as x2, disp as disp2, c1 as c1_mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1)  # How  to  print  variable  'x'  of  mod1)
disp1()# How  to  call  disp()  function  of  mod1
a=c1_mod1()
a.m1()# How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(x2) # How  to  print  variable  'x'  of  mod2)
disp2()# How  to  call  disp()  function  of  mod2
a=c1_mod2()
a.m1()# How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x)  # How  to  print  variable  'x'  of  current  module)
disp() # How  to  call  disp()  function  of current  module
a = c1() # How  to  call  method  m1()  of  class   c1  in  current  module
a.m1()
