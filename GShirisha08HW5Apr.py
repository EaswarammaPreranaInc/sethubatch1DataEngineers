#Repeat previous program such that OTP can be between 000000 and 999999 (may be 000156)
from random import randint
for i in range(10):
    s=''
    for i in range(6):
        s+=str(randint(0,9))
    print(s)

#Output
923814
733395
410475
017358
919343
645794
085069
031034
023836
125870

#Save in any file of cwd
from p1 import mod1
print(mod1.x) #How to print variable 'x' of mod1 in package p1
mod1.f1() #How to call function f1() of mod1 in package p1
a=mod1.c1()
a.m1() #How to call method m1() of class c1 in mod1 of package p1
print(p1.x) #Error: p1 is not imported
print(p1.__init__.x) #Error: p1.__init__ is not imported
print(__init__.x) #Error: 'x' is as good as member of p1

#Save in any file of cwd
from p1.mod1 import *
print(x) #How to print variable 'x' of mod1 in package p1
f1() #How to call function f1() of mod1 in package p1
a=c1()
a.m1() #How to call method m1() of class c1 in mod1 of package p1
print(p1.x) #Error: p1 is not imported
print(p1.__init__.x) #Error: p1.__init__ is not imported
print(__init__.x) #Error: 'x' is as good as member of p1
from p1 import mod1.* #Error: due to '.' in import clause of from stmt

#Save in any file of cwd
import p1.__init__ #How to import__init__ module of package p1 with import statement
print(p1.x) #How to print variable 'x' of __init__ module in package p1
p1.f1() #How to call function f1() of init module in package p1
a=p1.c1()
a.m1() #How to call method m1() of class c1 in init module of package p1
from p1.__init__ import *
print(x) #How to print variable 'x' of __init__ module in package p1 in another way
f1() #How to call function f1() of init module in package p1 in another way
a=c1()
a.m1() #How to call method m1() of class c1 in init module of package p1 in another way
print(p1.mod1.x) #Error: p1.mod1 is not imported

#Save in any file of cwd
import p1
import p1.mod1 #ifnored due to next line
from p1 import mod1 
from p1.mod1 import *
import p1._init_ #__init__ is executed 2 times
