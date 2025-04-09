# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
'''print('Begin')
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle  with  from  statement
print(How  to  print  variable  'x'  of  cal   module
print(y)
print(cal . x)
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(sub(10 , 7))
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
How  to  call  m1()  method  of  class  c1  in  cal  module
'''
x=100
y=200
def add(a,b):
	return a+b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def sub(a,b):
	if a>b:
		return a-b
	else:
		return b-a
class c1:
	def m1(self):
		print("method m1 of c1 class is called")
	def m2(self):
		print("hello")
print("Begin")
from cal import div,mul,add,x,c1
print(x)
print(mul(4,5))
print(add(10,7))
print(div(10,7))
obj=c1()
obj.m1()
'''
OUTPUT:
Begin
100
20
17
1.4285714285714286
method m1 of c1 class is called
'''
# Module  alias
'''print('Begin')
How  to  import  cal  module  with   another  name  using  import  statement
print(How  to  print  variable  'x'  of  cal   module
print(How  to  print  variable  'y'  of  cal   module
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(How  to  call  div()  function  of  cal  module  by  passing  10  and  7
How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)
from  math  as   m  import  *'''
import cal as cl
print(cl.x)
print(cl.y)
print(cl.add(10,7))
print(cl.sub(10,7))
print(cl.mul(10,7))
print(cl.div(10,7))
obj1=cl.c1()
obj1.m1()
'''
OUTPUT:
Begin
100
200
17
3
70
1.4285714285714286
method m1 of c1 class is called
'''
'''# Member  alias
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(How  to  print  variable  'x'  of  cal   module
print(x)
print(How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7))
b = c1()
'''
from cal import x as y,add as a,mul as m,c1 as c
print(y)
print(a(10,7))
print(m(10,7))
obj2=c()
obj2.m1()
#print(add(10,7))-->name 'add' is not defined
#b=c1() -->name 'c1' is not defined
'''
Begin
100
17
70
method m1 of c1 class is called
'''
'''
#mod1
x = 40
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
#mod2
x = 30
def   disp():
		print('disp  function  of   module two  ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  module two')
'''
#mod3
from  mod2 import  *
from  mod1  import  *
print(x)
disp()
a=c1()
a.m1()
'''
OUTPUT:
40
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''
#mod4
# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
print(x)
disp()
a=c1()
a.m1()
'''
OUTPUT:
30
disp  function  of   module two
m1  method of  class  c1  in  module two
'''
# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
'''
How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(How  to  print  variable  'x'  of  mod2
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module
'''
import mod1,mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)
mod1.disp()
a=mod1.c1()
a.m1()
print()
print(mod2.x)
mod2.disp()
a=mod2.c1()
a.m1()
print()
print(x)
disp()
a=c1()
a.m1()
'''
OUTPUT:
40
disp  function  of  same  module
m1  method of  class  c1  in  same  module

30
disp  function  of   module two
m1  method of  class  c1  in  module two

30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''
# How  to  use  members  of  all  the  three  modules  with  from  statement ?
'''
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
print(How  to  print  variable  'x'  of  mod2)
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module
'''
from mod1 import x as x1,disp as disp1,c1 as c12
from mod2 import x as x2,disp as disp2,c1 as c21
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1)
disp1()
a=c12()
a.m1()
print()
print(x2)
disp2()
b=c21()
b.m1()
print()
print(x)
disp()
c=c1()
c.m1()
'''
OUTPUT:
40
disp  function  of  same  module
m1  method of  class  c1  in  same  module

30
disp  function  of   module two
m1  method of  class  c1  in  module two

30
disp  function  of  same  module
m1   method  of  class  c1  in  same  module
'''







