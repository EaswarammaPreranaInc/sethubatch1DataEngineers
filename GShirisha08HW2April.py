'''#How to import only variable 'x', functions add() and mul() and class c1 of cal module?
print('Begin')
from cal import x, add, mul, c1 #How to import members x, add, mul and class c1 of cal module with from statement
print(x)#How to print variable 'x' of cal module
print(y) #Error: y is not defined
print(cal.x) #Error: cal is not imported
print(add(10,7))#How to call add() function of cal module by passing 10 and 7
print(sub(10,7)) #Error: sub is not defined
print(mul(10,7))#How to call mul() function of cal module by passing 10 and 7
print(div(10,7)) #Error: div is not defined
#How to call m1() method of class c1 in cal module
a=c1()
a.m1()



#Module alias
print('Begin')
import cal as c #How to import cal module with another name using import statement
print(c.x) #How to print variable 'x' of cal module
print(c.y) #How to print variable 'y' of cal module
print(c.add(10,7)) #How to call add() function of cal module by passing 10 and 7
print(c.sub(10,7)) #How to call sub() function of cal module by passing 10 and 7
print(c.mul(10,7)) #How to call mul() function of cal module by passing 10 and 7
print(c.div(10,7)) #How to call add() function of cal module by passing 10 and 7
#How to call m1() method of class c1 in cal module
a=c.c1()
a.m1()



#Member alias
from cal import x as m, add as a, mul as b, c1 as c #How to import members x, add, mul and class c1 of cal module with another name using from statement
print(m) #How to print variable 'x' of cal module
#print(x) #Error: x is not defined
print(a(10,7)) #How to call add() function of cal module by passing 10 and 7
print(b(10,7)) #How to call mul() function of cal module by passing 10 and 7
#How to call m1() method of class c1 in cal module
a=c()
a.m1()
'''


#Find outputs
x=30
def disp():
	print('disp function of same module')
class c1:
	def m1(self):
		print('m1 method of class c1 in same module')
from mod2 import *
from mod1 import *
print(x) #'x' value of mod1 is printed
disp() #disp function of mod1 module
a=c1()
a.m1() #m1 of class c1 of mod1 is executed



#Find outputs
from mod1 import *
from mod2 import *
x=30
def disp():
	print('disp function of same module')
class c1:
	def m1(self):
		print('m1 method of class c1 in same module')
print(x) #30
disp() #disp function of same module
a=c1()
a.m1() #m1 method of class c1 in same module



#How to use members of all the 3 modules(mod1, mod2 and current module) with import statement?
import p1 #How to import mod1 and mod2 -->In __init__ of p1 import mod1 and mod2
x=30
def disp():
		print('disp function of same module')
class c1:
	def m1(self):
		print('m1 method of class c1 in same module')
print(p1.mod1.x) #How to print variable 'x' of mod1
p1.mod1.disp() #How to call disp() function of mod1
a=p1.mod1.c1()
a.m1() #How to call method m1() of class c1 in mod1
print()
print(p1.mod2.x) #How to print variable 'x' of mod2
p1.mod2.disp() #How to call disp() function of mod2
a=p1.mod2.c1()
a.m1() #How to call method m1() of class c1 in mod2
print()
print(x)How to print variable 'x' of current module)
disp() #How to call disp() function of current module
a=c1()
a.m1() #How to call method m1() of class c1 in current module



#How to use members of all the 3 modules(mod1, mod2 and current module) with from statement ?
from p1.mod1 import x as a,disp as d, c1 as g #How to import members of mod1
from p1.mod2 import x as b,disp as e, c1 as h #How to import members of mod2
x=30
def disp():
		print('disp function of same module')
class c1:
	def m1(self):
		print('m1 method of class c1 in same module')
print(a) #How to print variable 'x' of mod1
d() #How to call disp() function of mod1
z=g()
z.m1() #How to call method m1() of class c1 in mod1
print()
print()
print(b) #How to print variable 'x' of mod2
e() #How to call disp() function of mod2
z=h()
z.m1() #How to call method m1() of class c1 in mod2
print()
print()
print(x) #How to print variable 'x' of current module
disp() #How to call disp() function of current module
z=c1()
z.m1() #How to call method m1() of class c1 in current module
