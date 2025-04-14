#Ex-1
'''
Write  a  program  to  print  random  character  of  the  string  10  times
'''
from random import *
from time import sleep

s = 'Hyderabad'
for i in range(10):
    print(choice(s))
    sleep(1)


#Ex-2
'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters  are digits
'''

from random import *
c=''
d=''
alpa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
for i in range(10):
    pwd = ''
    for j in range(3):
        c = choice(alpa)
        d = choice(num)
        pwd = pwd+c+d
    print(pwd)


#Ex-3
'''
# Write  a  program  to  print  random  element  of  the  list  ten  times
'''
from random import *
from time import sleep

a= eval(input('Enter a list : '))
for i in range(10):
    print(choice(a))
    sleep(1)

#Ex-4
'''
# Write  a  program  to  generate  ten  six-digit  OTP's
'''

from random import *
from time import sleep
num = '1234567890'
for i in range(10):
    pwd = ''
    for j in range(6):
        pwd +=choice(num)
    print(pwd)
    sleep(1)

#Ex-5
'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the websites
'''

from random import *
from time import sleep
from webbrowser import open_new_tab

a =['http://google.com','http://rediff.com','http://gmail.com','http://amazon.com']
for i in range(10):
    site = choice(a)
    open_new_tab(site)
    sleep(5)

#Ex-6
'''
(Home  work)
Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  --->  Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																											Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																										Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  --->
																										Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  ---> User wins

'''
from random import *
from time import sleep
a = ['Rock','Paper','Scissors']
y = True
while y:
    c = choice(a)
    n = eval(input('What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  : '))
    user_input= a[n]
    print('User : ' ,user_input)
    print('Computer :  ',c)
    if c ==  user_input:
        print('Draw')
    elif (c == 'Scissors' and user_input == 'Rock') or (c == 'Scissors' and user_input == 'Paper') or (c == 'Rock' and user_input == 'Scissors'):
        print('Computer wins')
    else:
        print('User wins')
    yes = input('Continue  (  y / n)  ?  ')
    if yes != 'y':
        y = False
print('End of the game')


#Ex-7
#  Save  in  any  file  of  cwd  (Homework)
from p1 import  mod1,mod2  # How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x)  #  How  to  print  variable  'x'  of   mod1  in  package  p1
mod1.f1()  # How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()
a.m1()  #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x) #  How  to  print  variable  'x'  of   mod2  in  package  p1
mod1.f1()   # How  to  call  function  f1()  of   mod2  in  package  p1
a = mod1.c1()
a.m1() # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1.x) # Error because p1 not imported
#print(x) # Error because x not define cwd


#Ex-8
#  Save  in  any  file  of  cwd
from p1.mod1 import  *           # How  to  import  members  of  mod1  in  package  p1  with  from  statement
print(x) # How  to  print  variable  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.mod2 import  *    #How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x) # How  to  print  variable  'x'  of   mod2  in  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  package  p1
a = c1()
a.m1()   #  How  to   call  method  m1()  of   class  c1  in  mod2  of  package  p1
# print(p1 . mod1 . x)  # Error because p1 not imported
# print(mod1 . x) # mod1 not imported .members imported
#from  p1   import  mod1.* # Error because . not permitted after the import clause from statement

#Ex-9
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    * # imported all members of mod1
from  p1 . mod2    import    * # imported all members of mod2
print(x) # member of p1.mod2
f1() # member of p1.mod2
a=c1() # creates object of p1.mod2 of class
a.m1() # call p1.mod2 class method

#Ex-10
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   * # imported all members of mod2
from  p1 . mod1    import   * # imported all members of p1.mod1
print(x)  # member of p1.mod1
f1() # member of p1.mod1
a=c1() # creates object of p1.mod1 of class
a.m1() # call p1.mod1 class method

#Ex-11
from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x) # print x cwd
f1() # f1 call cwd
a=c1() # create object cwd class
a.m1() # call m1 method of cwd class

#Ex-12
from p1.mod1 import x as x1,f1 as f1_1, c1 as c1_1  # How  to  import   members  of  mod1   in  package  p1  with  from  statement
from p1.mod2 import *  # How  to  import   members  of  mod2   in  package  p1  with  from  statement
print(x1)   # How  to  print  variable  'x'  of   mod1  in  package  p1
f1_1()       # How  to  call  function  f1()  of   mod1  in  package  p1
a =c1_1()
a.m1()     # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x)   # How  to  print  variable  'x'  of   mod2  in  package  p1
f1()       # How  to  call  function  f1()  of   mod2  in  package  p1
a = c1()
a.m1()    # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
