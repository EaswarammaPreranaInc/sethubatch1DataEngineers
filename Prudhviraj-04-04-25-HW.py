# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
import random
n=list(input("Enter the input: "))
x=0
while x<10:
	print(random.choice(n))
	x+=1
"""
Output:
Enter the input: Hyderabad
d
H
e
y
H
a
e
a
e
H
"""

#(Home  work)
#Write  a  program to  generate  10  passwords  each  of  6 character  length  where
#1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

import random
x=0
while x<6:
	y=random.randrange(65,91)
	z=random.randrange(0,9)
	y1=random.randrange(65,91)
	z1=random.randrange(0,9)
	y2=random.randrange(65,91)
	z2=random.randrange(0,9)
	print(chr(y)+str(z)+chr(y1)+str(z1)+chr(y2)+str(z2))
	x+=1
"""
Output:
V0M7V1
E1M3R3
C5J1L6
T7O2I2
T2S1J2
W6L5L2
"""

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import random
a=[25,10.8,'Hyd',True,None,3+4j]
x=0
while x<10:
	print(random.choice(a))
	x+=1
"""
Output:
10.8
(3+4j)
Hyd
True
True
Hyd
25
True
Hyd
Hyd
"""

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import random
a=0
x=0
while x<10:
	print(random.randrange(100000,999999))
	x+=1
"""
Output:
279725
764251
522954
792801
691496
841619
590673
750872
726643
381478
"""

#Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
#1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website
#2) Where  is  open()  function  defined  ?  --->  webbrowser  module
#3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
#4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
import random
import webbrowser
import time
a=['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in a:
	if i.startswith('http://')and i.startswith('https://'):
		print(random.choice(a))
	else:
		url='http://'+i
	webbrowser.open(url)
	time.sleep(10)


#  Save  in  any  file  of  cwd  (Homework)  
import P1.mod1,P1.mod2    #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(P1.mod1.x)            #How  to  print  variable  'x'  of   mod1  in  package  p1
print(P1.mod1.f1())         #How  to  call  function  f1()  of   mod1  in  package  p1
a=P1.mod1.c1()              #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(a.m1())
print()
print()
print(P1.mod2.x)            #How  to  print  variable  'x'  of   mod2  in  package  p1
print(P1.mod2.f1())         #How  to  call  function  f1()  of   mod2  in  package  p1
b=P1.mod2.c1()
print(b.m1())               #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(P1 . mod1 . x)
#print(x)
"""
Output:
10
p1--->mod1--->f1 Function
None
p1--->mod1--->c1--->m1 Method
None


20
p1--->mod2--->f1 Function
None
p1--->mod2--->c1--->m1
None
10
"""

#  Save  in  any  file  of  cwd  (Homework)  
from P1 import mod1,mod2       #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x)                  #How  to  print  variable  'x'  of   mod1  in  package  p1
print(mod1.f1())               #How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()
print(a.m1())                  #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x)                  #How  to  print  variable  'x'  of   mod2  in  package  p1
print(mod2.f1())               #How  to  call  function  f1()  of   mod2  in  package  p1
b=mod2.c1
print(b.m1)                  #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(P1 . mod1 . x)
#print(x)
"""
Output:
10
p1--->mod1--->f1 Function
None
p1--->mod1--->c1--->m1 Method
None


20
p1--->mod2--->f1 Function
None
<function c1.m1 at 0x000001745B31C4A0>
"""

#  Save  in  any  file  of  cwd
from P1.mod1 import * #How  to  import  members  of  mod1  in  package  p1  with  from  statement
print(x) #How  to  print  variable  'x'  of   mod1  in  package  p1
print(f1()) #How  to  call  function  f1()  of   mod1  in  package  p1
print(c1.m1) #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from P1.mod2 import * #How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x) #How  to  print  variable  'x'  of   mod2  in  package  p1
print(f1()) #How  to  call  function  f1()  of   mod2  in  package  p1
print(c1.m1) #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(P1 . mod1 . x)
#print(mod1 . x)
#from  p1   import  mod1 . *
"""
Output:
10
p1--->mod1--->f1 Function
None
<function c1.m1 at 0x000001C7BE2F8220>


20
p1--->mod2--->f1 Function
None
<function c1.m1 at 0x000001C7BE2F8400>
"""
#Save  the  following  code  in    any  file  of  cwdFind  outputs
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  P1 . mod1    import    *
from  P1 . mod2    import    *
print(x)
f1()
a = c1()
a . m1()
"""
Output:
20
p1--->mod2--->f1 Function
p1--->mod2--->c1--->m1
"""

 #(Home  work)
#Save  the  following  code  in    any  file  of  cwd
#Find  outputs
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  P1 . mod2    import   *
from  P1 . mod1    import   *
print(x)
f1()
a = c1()
a . m1()
"""
Output:
10
p1--->mod1--->f1 Function
p1--->mod1--->c1--->m1 Method
"""

#(Home work)
#Save  the  following  code  in    any  file  of  cwd
#Find  outputs
from  P1 . mod1    import    *
from  P1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x)
f1()
a = c1()
a . m1()
"""
Output:
30
Function  of  same  module
Method  of  class  c1  in same  module
"""

# Save  in  any  file  of  cwd
from P1 import mod1	#How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x)	#How  to  print  variable  'x'  of   mod1  in  package  p1
print(mod1.f1())	#How  to  call  function  f1()  of   mod1  in  package  p1
print(mod1.c1.m1)	#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
#print(P1 . mod1 . x)
print()
print()
from P1 import mod2	#How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x)	#How  to  print  variable  'x'  of   mod2  in  sub-package  p2  of  package  p1
print(mod2.f1())	#How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
print(mod2.c1.m1)	#How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#print(p1 . p2 . mod2 . x)
#from  p1  import   p2 . mod2
#from  p2  import  mod2
"""
Output:
10
p1--->mod1--->f1 Function
None
<function c1.m1 at 0x000001AC82A4C2C0>


20
p1--->mod2--->f1 Function
None
<function c1.m1 at 0x000001AC82A4C4A0>
"""

# Save  in  any  file  of  cwd
from P1.mod1 import *	#How  to  import  members  of  mod1  in  p1  with  from  statement
print(x)	#How  to  print  variable  'x'  of   mod1  in  package  p1
print(f1())	#How  to  call  function  f1()  of   mod1  in  package  p1
print(c1.m1)	#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from P1.mod2 import *	#How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1  with  from  statement
print(x)	#How  to  print  variable  'x'  of   mod2  in  sub-package  p2  of  package  p1
print(f1())	#How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
print(c1.m1)	#How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#from  p1  import  mod1 . *
"""
Output:
10
p1--->mod1--->f1 Function
None
<function c1.m1 at 0x00000142BA678220>


20
p1--->mod2--->f1 Function
None
<function c1.m1 at 0x00000142BA678400>
"""
