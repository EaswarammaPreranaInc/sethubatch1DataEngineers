#Save  in  any  file  of  cwd
import p1.mod1 ,p1.p2.mod2 #How  to  import  mod1 of package p1, mod2 of package p2 in p1 with import statement
print(p1.mod1.x) #How  to  print  variable  'x'  of   mod1  in  package  p1
p1.mod1.f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a = p1.mod1.c1()
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(p1.p2.mod2.x)#How  to  print  variable  'x'  of   mod2  in  sub-package  p2  of  package  p1
p1.p2.mod2.f1() #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a = p1. p2. mod2.c1() 
a.m1() #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1


'''
output:-
10
p1-----> mod1----> f1 function
p1--->mod1--->c1---->m1 method


20
p1----->p2----> mod2----> f1 function
p1--->p2----->mod2--->c1---->m1 method