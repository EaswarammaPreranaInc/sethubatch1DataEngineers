'''from  random import *
a=input('enter string:')
for i in range(10):

	print(choice(a))
enter string:hyderabad
output-
y
h
d
h
a
r
y
h
b
d

 (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

from random import *
def digits():
		return randrange(10)
def char():
		return chr(randrange(65,91))
def f1():
		for i in range(10):
			print(char(),digits(),char(),digits(),char(),digits(),sep='')

f1()
outputs--
G2A6Z7
A1M2Z4
E0E9J6
R8U6G6
T7X9F0
D3W1H3
D8T5G4
W0K7R6
F6U9L9
P9L8A9

 Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import *
a=eval(input('enter list:'))
for i in range(1,11):
		print(choice(a))

outputs---
hyd
25
(3+4j)
hyd
True
(3+4j)
10.8
25
hyd
True

from random import *
for i in range(10):
	print(randint(100000,999999))
outputs--
444563
297885
421239
867647
528206
227351
540665
957546
523114
919448
				
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites

from webbrowser import *
from random import *
import time
list= ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in list:
	open(choice(list))
	time.sleep(5)



(Home  work)
Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  --->  Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																							Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																								Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  ---> 
																								Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  ---> User  wins

from random import choice
list=['rock','paper','sissor']
while True:
	a=int(input('enter user input(rock,paper,sissor):')	)
	if a<0 and a>2:
			print('invaid')
	else:
		user=list[a]
		comp=choice(list)
		print('user:',user)
		print('comp:',comp)
		if user==comp:
					print('Draw')
		elif user=='rock' and comp=='paper'or  user=='paper' and comp=='sissor'or  user=='sissor' and comp=='rock':
					print('comp wins')
	
		else:
				print('user wins')
		option=input('continue (y/N)')
		if option=='n' or option=='N':
				break
output--
enter user input(rock,paper,sissor):1
user: paper
comp: paper
Draw
continue (y/N)y
enter user input(rock,paper,sissor):2
user: sissor
comp: rock
comp wins
continue (y/N)y
enter user input(rock,paper,sissor):0
user: rock
comp: paper
comp wins
continue (y/N)n

'''	
