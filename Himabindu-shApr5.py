'''# Write  a  program  to  print  random  character  of  the  string  10  times
import random
s=input("Enter the string : ")
for i in range(10):
	print(random.choice(s))
	'''
'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

import random
S='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(10):
	s=''
	for j in range(3):
		s=s+random.choice(S)
		s=s+str(random.randint(1,10))
	print(s)
'''

'''
# Write  a  program  to  print  random  element  of  the  list  ten  times  

import random
list=eval(input("enter the list : "))
for i in range(10):
	print(random.choice(list))
'''

'''
# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import random
for i in range(10):
	d=''
	for j in range(6):
		d=d+str(random.randint(1,9))
	print(d)
'''

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites

import random,time,webbrowser
list= ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in range(len(list)):
	webbrowser.open(list[i])
	time.sleep(20)
'''

'''Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  --->  Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																											Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																										Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  ---> 
																										Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  ---> User  wins


import random
list=['Rock','Paper','Scissors']
while True:
	n=int(input('What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors  : '))
	if n<0 or n>2:
		print("Invalid Input")
	else:
		user_input=list[n]
		computer=random.choice(list)
		print(user_input)
		print(computer)
		if user_input==computer:
			print("Draw")
		elif (computer=='Rock' and user_input=='Scissors') or (computer=='Paper' and user_input=='Rock') or (computer=='Scissors' and user_input=='Paper'):
			print('Computer win')
		else:
			print('You win')
		option=input('continue y/n ?')
		if option=='n' or option=='N':
			break
print('end of the game')
'''

'''
#  Save  in  any  file  of  cwd  (Homework)  
from p1 import mod1  #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
from p1 import mod2
print(mod1.x)  #How  to  print  variable  'x'  of   mod1  in  package  p1
mod1.f1()   #How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()  
a.m1()  #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x)  #How  to  print  variable  'x'  of   mod2  in  package  p1
mod2.f1()  #How  to  call  function  f1()  of   mod2  in  package  p1
a=mod2.c1() 
a.m2()  #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x) # error
print(x) # error
'''
