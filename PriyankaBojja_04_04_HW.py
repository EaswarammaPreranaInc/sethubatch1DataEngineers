Q1 #Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import*
a=input('Enter any string: ')
for i in range(10):
	print(choice(a))

OP-
Enter any string: Priyanka
P
n
y
r
k
i
y
a
a
P
#------------------------------------------------------------------------------------------------------------
Q2 #Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

from random import *
for i in range(10):
	for j in range(1,7):
		if j%2==0:
			print(randint(0,9),end='')
		elif j%2!=0:
			print(chr(randint(65,90)),end='')
	print()

OP-
E0V7R4
F4L4W0
Z7P1U2
R5U2S4
A6W2U9
V0Z9V9
B5S7F2
R3M1L4
O3F5Q4
U9R0B1
#--------------------------------------------------------------------------------------------------------------
Q3 #Write  a  program  to  print  random  element  of  the  list  ten  times

from random import *
a=eval(input('Enter a List: '))
for x in range(10):
		print(choice(a))

OP-
Enter a List: [25,10.8,'Hyd',True,None,3+4j]
10.8
None
Hyd
None
(3+4j)
(3+4j)
Hyd
25
25
Hyd
#---------------------------------------------------------------------------------------------------------------------
Q4 #Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

import random
for x in range(10):
	for y in range(6):
		print(random.randint(0,9),end='')
	print()

OP-
332464
473000
862166
904905
593274
316590
693637
756454
198666
173510
#------------------------------------------------------------------------------------------------------------------------------
Q5 #Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

import time
from random import choice
from webbrowser import open
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
while True:
	open(choice(list))
	time.sleep(7)
#---------------------------------------------------------------------------------------------------------------------------
Q6 #Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  --->  Draw
2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  ---> Computer  wins  becoz  paper  dominates  rock
3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  ---> Computer  wins  becoz  scissors  dominates  paper
4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  ---> Computer  wins  becoz  rock  dominates  scissors
5) What  is  the  result  in  all  other  cases  ?  ---> User  wins

from random import choice
def game():
	a=int(input('What do you want to select(0-Rock , 1 - Paper , 2 - Scissors) : '))
	l=['Rock','Paper','Scissors']
	u=l[a]
	print(f'User : {u}')
	c=choice(l)
	print(f'Computer : {c}')
	if u==c:
		print('Draw')
	elif (u=='Rock' and c=='Paper') or (u=='Paper' and c=='Scissors') or (u=='Scissors' and c=='Rock'):
		print('Compute wins')
	else:
		print('User wins')
game()
while True:
	x=input('Continue (y/n) ? ')
	if x=='y':
		game()
	else:
		print('End of the game')
		break

OP-
What do you want to select(0-Rock , 1 - Paper , 2 - Scissors) : 0
User : Rock
Computer : Rock
Draw
Continue (y/n) ? y
What do you want to select(0-Rock , 1 - Paper , 2 - Scissors) : 1
User : Paper
Computer : Rock
User wins
Continue (y/n) ? y
What do you want to select(0-Rock , 1 - Paper , 2 - Scissors) : 2
User : Scissors
Computer : Rock
Compute wins
Continue (y/n) ? n
End of the game
#-------------------------------------------------------------------------------------------------------------------
Q7 #Save  in  any  file  of  cwd  (Homework)  
from p1 import mod1,mod2 #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x) #How  to  print  variable  'x'  of   mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1() 
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x) #How  to  print  variable  'x'  of   mod2  in  package  p1
mod2.f1() #How  to  call  function  f1()  of   mod2  in  package  p1
a=mod2.c1() 
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x) #error - p1 is not imported
#print(x)  # error- x is not there in current program

OP-
10
p1 -----> mod1 -----> f1 function
p1 -----> mod1 -----> c1 -----> m1 method


20
p1 -----> mod2 -----> f1
p1 -----> mod2 -----> c1 -----> m1
#--------------------------------------------------------------------------------------------------------------------
Q8 #Save  in  any  file  of  cwd
from p1.mod1 import *    #How  to  import  members  of  mod1  in  package  p1  with  from  statement
print(x)                 #How  to  print  variable  'x'  of   mod1  in  package  p1
f1()                     #How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()                   #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
a.m1()
print()
print()
from p1.mod2 import *    #How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x)                 #How  to  print  variable  'x'  of   mod2  in  package  p1
f1()                     #How  to  call  function  f1()  of   mod2  in  package  p1
a=c1()
a.m1()                   #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x)     #error - p1.mod1 is not imported
#print(mod1 . x)          #error - mod1 is not imported 
#from  p1   import  mod1 . *    #error- '.' cannot be used in import

OP-
10
p1 -----> mod1 -----> f1 function
p1 -----> mod1 -----> c1 -----> m1 method


20
p1 -----> mod2 -----> f1
p1 -----> mod2 -----> c1 -----> m1
Traceback (most recent call last):
#---------------------------------------------------------------------------------
Q9 #Save  the  following  code  in    any  file  of  cwd . Find  outputs

x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x) #x from p1.mod2
f1()     #f1() from p1.mod2
a = c1()
a . m1()  #m1() from p1.mod2

OP-
20
p1 -----> mod2 -----> f1
p1 -----> mod2 -----> c1 -----> m1

#------------------------------------------------------------------------------
Q10 #Save  the  following  code  in    any  file  of  cwd. Find  outputs

x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   *
from  p1 . mod1    import   *
print(x) # x from p1.mod1
f1()     #f1() from p1.mod1
a = c1()
a . m1() #m1 from p1.mod1

OP-
10
p1 -----> mod1 -----> f1 function
p1 -----> mod1 -----> c1 -----> m1 method

#----------------------------------------------------------------------
Q11 #Save  the  following  code  in    any  file  of  cwd. Find  outputs

from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x)  #x from current program
f1()       #f1() from current program
a = c1()
a . m1()   #m1() from current program

OP-
30
Function  of  same  module
Method  of  class  c1  in same  module
#_-------------------------------------------------------------------------------
Q12 #Save  the  following  code  in  any  file  of  cwd . How  to  use  members  of  both  the  modules

from p1.mod1 import x as x1,f1 as F1, c1 as C1 #How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod2 import * #How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x1)             #How  to  print  variable  'x'  of   mod1  in  package  p1
F1()                  #How  to  call  function  f1()  of   mod1  in  package  p1
a=C1()
a.m1()                #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x)              #How  to  print  variable  'x'  of   mod2  in  package  p1
f1()                  #How  to  call  function  f1()  of   mod2  in  package  p1
a=c1() 
a.m1()                #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1

OP-
10
p1 -----> mod1 -----> f1 function
p1 -----> mod1 -----> c1 -----> m1 method


20
p1 -----> mod2 -----> f1
p1 -----> mod2 -----> c1 -----> m1
#-----------------------------------------------------------------------------------------------
Q13 # Save  in  any  file  of  cwd

from p1 import mod1         #How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x)               #How  to  print  variable  'x'  of   mod1  in  package  p1
mod1.f1()                   #How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1() 
a.m1()                      #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
#print(p1 . mod1 . x)        #error - p1 is not imported
print()
print()
from p1.p2 import mod2      #How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x)               #How  to  print  variable  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1()                   #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=mod2.c1() 
a.m1()                      #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#print(p1 . p2 . mod2 . x)   #error - p1 is not imported
#from  p1  import   p2 . mod2  #error - '.' cannot be used in import 
#from  p2  import  mod2       #error - there is no module p2

OP-
10
p1 -----> mod1 -----> f1 function
p1 -----> mod1 -----> c1 -----> m1 method


20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
#----------------------------------------------------------------------------------------------------
Q14 #Save  in  any  file  of  cwd
from p1.mod1 import *    #How  to  import  members  of  mod1  in  p1  with  from  statement
print(x)                 #How  to  print  variable  'x'  of   mod1  in  package  p1
f1()                     #How  to  call  function  f1()  of   mod1  in  package  p1
a=c1() 
a.m1()                   #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2.mod2 import * #How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1  with  from  statement
print(x)                 #How  to  print  variable  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1()                     #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=c1() 
a.m1()                   #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#from  p1  import  mod1 . * #error - '.' cannot be used in import 

OP-
10
p1 -----> mod1 -----> f1 function
p1 -----> mod1 -----> c1 -----> m1 method


20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
'''