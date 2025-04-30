..........1
# return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')
x =  f1()
print(x)
print('End')
output:
Begin
f1  function
25
End
.........2
# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')
output:
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End
.........3
#  Gift
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)
print(type(x))
a , b , c =  f1()
print(a)
print(b)
print(c)
print('for  loop')
for  k   in   f1():
	print(k)
output:
(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30
..........4
# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
x = f1()
print(x)
print('End')
#return   100
output:
Begin
10
End
.........5
#  Find  outputs
f1()
def   f1():
        print('Hello')
print(f1())
print(f1)
output:
Hello
None
<function f1 at 0x0000023032A91440>
............6
# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
output:
Hello
Hi
f1  function
None
<function f1 at 0x0000022C4FF41440>
Bye
..............7
#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')
output:
Begin
<class 'function'>
2445032232000
End
............8
# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
f1(40 , 50)
f1(60)
f1()
output:
Three  argument  function :  10 20 30
output:
# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)
output:
Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0
Emp  Number  :  Sita      Emp Name  :  20000.0    Salary  :  35
..............9
# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')
f1(c = 3 + 4j , a = True , b = None)
f1(25 , c = 10.8 , b = 'Hyd')
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'
output:
a  :  10          b  :  20        c :  30
a  :  25          b  :  10.8      c :  Hyd
a  :  50.2        b  :  40.7      c :  60.5
a  :  Cyb         b  :  Sec       c :  Hyd
a  :  True        b  :  None      c :  (3+4j)
a  :  25          b  :  Hyd       c :  10.8
...........10
# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)
output:
Emp  Number :   25        Emp  Name : Rama Rao            Salary : 10000.0
Emp  Number :   35        Emp  Name : Sita                Salary : 20000.0
Emp  Number : Rama  Rao           Emp  Name :         30000.0     Salary : 20
............11
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))
print(f1(*[6 , 7 , 8]))
#print(f1([6 , 7 , 8]))
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))
output:
23
62
16
14
{'c': 2, 'b': 4, 'a': 6}




