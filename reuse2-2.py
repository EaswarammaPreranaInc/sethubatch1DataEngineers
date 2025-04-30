#Save  in  any  file  of  cwd
from p1.mod1 import* # How  to  import  members  of  mod1  in  p1  with  from  statement
print(x) # How  to  print  variable  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1() 
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1 . p2.mod2 import * # How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1  with  from  statement
print(x) # How  to  print  variable  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=c1()
a.m1()# How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#from  p1  import  mod1 . * # Error : '.' can not be used in import clause

'''
output:-
10
p1-----> mod1----> f1 function
p1--->mod1--->c1---->m1 method


20
p1----->p2----> mod2----> f1 function
p1--->p2----->mod2--->c1---->m1 method

'''