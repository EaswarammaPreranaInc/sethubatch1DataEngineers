from p1 import mod1 # How to import mod1 of package p1 with from statement
print(mod1.x) # How to print variable 'x' of mod1 in package p1
mod1.f1() # How to call function f1 in mod1 in package p1
a = mod1.c1()
a.m1() # How to call method m1() of class c1 in mod1 in package p1
#print(p1.mod1.x) # Error: package p1 is not imported
print()
print()
from p1.p2 import mod2  # How to import mod2 of sub-package p2 in package p1 with from statement
print(mod2.x) #How to print variable 'x' of mod2 in sub-package p2 in package p1
mod2.f1() # How to call a function f1() of mod2 of sub-package p2 in package p1
a = mod2.c1()
a.m1() # How to call method m1() of class c1 in mod2 of sub-package p2 in package p1
#print(p1.p2.mod2.x) # Error : package p1 is not imported
#from p1 import p2.mod2 # Error : '.' can not be used in import clause
#from p2 import mod2 # Error : No package p2 in cwd

'''
output:-
-------
10
p1-----> mod1----> f1 function
p1--->mod1--->c1---->m1 method


20
p1----->p2----> mod2----> f1 function
p1--->p2----->mod2--->c1---->m1 method
'''
