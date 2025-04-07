#print random character of the string 10 times
import random
s=input()
for i in range(10):
	print(random.choice(s))

#Output
Hyderabad
y
a
d
d
b
r
H
d
H
b


#Generate 10 passwords each of 6 character length where 1st, 3rd, 5th characters are alphabets and 2nd, 4th, 6th characters are digits
import random
s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(10):
	res=''
	for j in range(8):
		if j%2==0:
			res+=random.choice(s)
		else:
			res+=str(random.randint(0,10))
	print(res)

#Output
M9C0P9O6
X5N4C2D0
B7G6P10O7
L8R1E6F7
I8E2Q5E1
B1Z9G5M4
A10Y10A9V4
W8X1E3R6
Z2F10D7O7
X6Z1F6S8

#print random element of the list ten times
import random
a=eval(input('Enter a list: '))
for i in range(10):
	print(random.choice(a))

#Output
Enter a list: [25,10.8,True,'Hyd',None,3+4j,(10,20)]
Hyd
(10, 20)
10.8
Hyd
25
Hyd
(3+4j)
True
(10, 20)
None

#Generate ten six-digit OTP's
import random
for i in range(10):
	res=str(random.randint(100000,999999))
	print(res)

#Output
229645
717029
851236
333534
236370
355357
481317
488317
504927
178938

#open any website from gmail, google, rediff,... with a time gap of 5 to 20 sec
import random, time
from webbrowser import open
list=['google.com','rediff.com','gmail.com','amazon.com','netflix.com']
while True:
	open(random.choice(list))
	time.sleep(8)

#Implement Rock, Paper and scissors game between user and computer
from random import choice
def game(n):
	d={0:'Rock', 1:'Paper', 2:'Scissors'}
	user=d[n]
	print('User :',d[n])
	l=list(d.values())
	comp=choice(l)
	print('Computer :',comp)
	if user==comp:
		return 'Draw'
	else:
		t=(user,comp)
		res={('Rock','Scissors'):'User wins',('Scissors','Rock'):'Computer wins',('Paper','Rock'):'User wins',('Rock','Paper'):'Computer wins',('Scissors','Paper'):'User wins',('Paper','Scissors'):'Computer wins'}
		return res[t]
n=int(input('What do you want to select (0-Rock, 1-Paper, 2-Scissors): '))
print(game(n))
while(input('Continue (y/n) ?')=='y'):
	n=int(input('What do you want to select (0-Rock, 1-Paper, 2-Scissors): '))
	print(game(n))
print('End of the game')

#Output
What do you want to select (0-Rock, 1-Paper, 2-Scissors): 0
User : Rock
Computer : Scissors
User wins
Continue (y/n) ?y
What do you want to select (0-Rock, 1-Paper, 2-Scissors): 1
User : Paper
Computer : Scissors
Computer wins
Continue (y/n) ?y
What do you want to select (0-Rock, 1-Paper, 2-Scissors): 2
User : Scissors
Computer : Rock
Computer wins
Continue (y/n) ?y
What do you want to select (0-Rock, 1-Paper, 2-Scissors): 0
User : Rock
Computer : Rock
Draw
Continue (y/n) ?n
End of the game

#Save in any file of cwd
from p1 import mod1,mod2 #How to import mod1 and mod2 of package p1 with from statement
print(mod1.x) #variable 'x' of mod1 in package p1
mod1.f1() #function f1() of mod1 in package p1
a=mod1.c1()
a.m1() #method m1() of class c1 in mod1 of package p1
print()
print()
print(mod2.x) #variable 'x' of mod2 in package p1
mod2.f1() #function f1() of mod2 in package p1
a=mod2.c1()
a.m1() #method m1() of class c1 in mod2 of package p1
print(p1.mod1.x) #Error: p1 is not imported
print(x) #Error: 'x' is not imported

#Save in any file of cwd
from p1.mod1 import * #How to import members of mod1 in package p1 with from statement
print(x)#variable 'x' of mod1 in package p1
f1() #callfunction f1() of mod1 in package p1
a=c1()
a.m1() #call method m1() of class c1 in mod1 of package p1
print()
print()
from p1.mod2 import* #import members of mod2 in package pq1 with from statement
print(x) #print variable 'x' of mod2 in package p1
f1() #call function f1() of mod2 in package p1
a=c1()
a.m1() #call method m1() of class c1 in mod2 of package p1
print(p1.mod1.x) #Error: p1.mod1 is not imported
print(mod1.x) #Error: 'mod1' is not imported
from p1 import mod1.* #Error due to '.' in import clause

#Find outputs
x=30
def f1():
	print('Function of same module')
class c1:
	def m1(self):
		print('Method of class c1 in same module')
from p1.mod1 import *
from p1.mod2 import *
print(x)  #20
f1()  #p1-->mod2-->f1
a=c1()
a.m1() #p1-->mod2-->c1-->m1

#Find outputs
x=30
def f1():
	print('Function of same module')
class c1:
	def m1(self):
		print('Method of class c1 in same module')
from p1.mod2 import *
from p1.mod1 import *
print(x)  #10
f1()  #p1-->mod1-->f1
a=c1()
a.m1() #p1-->mod1-->c1-->m1

#Find outputs
from p1.mod1 import *
from p1.mod2 import *
x=30
def f1():
	print('Function of same module')
class c1:
	def m1(self):
		print('Method of class c1 in same module')
print(x)  #30
f1()  #Function of same module
a=c1()
a.m1() #Method of class c1 in same module

#How to use members of both the modules
from p1.mod1 import x as b, f1 as c, c1 as d #import members of mod1 in package p1 with from statement
from p1.mod2 import * #import members of mod2 in package p1 with from statement
print(b) #print variable 'x' of mod1 in package p1
c() #call function f1() of mod1 in package p1
a=d()
a.m1()#call method m1 of class c1 of mod1 in package p1
print()
print()
print(x) #print variable 'x' of mod2 in package p1
f1() #call function f1() of mod2 in package p1
a=c1()
a.m1()#call method m1 of class c1 of mod2 in package p1

#Save in any file of cwd
from package1 import mod1 #How to import mod1 of package package1 with from statement
print(mod1.x) #How to print variable 'x' of  mod1 in package package1
mod1.f1() #How to call function f1() of  mod1 in package package1
a=mod1.c1()
a.m1() #How to call method m1() of class c1 in mod1 of package package1
print(package1.mod1.x) #Error: package1.mod1 is not imported
print()
print()
from package1.package2 import mod2 #How to import mod2 of sub-package package2 in package package1 with from statement
print(mod2.x) #How to print variable 'x' of  mod2 in sub-package package2 of package package1
mod2.f1() #How to call function f1() of mod2 in sub-package package2 of package package1
a=mod2.c1()
a.m1() #How to call method m1() of class c1 in mod2 of sub-package package2 in package package1
print(package1.package2.mod2.x) #package1.package2 is not imported
from package1 import package2.mod2 #Error due to '.'
from package2 import mod2 #Error due to package2

#Save in any file of cwd
from package1.mod1 import * #How to import members of mod1 in package1 with from statement
print(x) #How to print variable 'x' of  mod1 in package1
f1() #How to call function f1() of  mod1 in package1
a=c1()
a.m1() #How to call method m1() of class c1 in mod1 of package1
print()
print()
from package1.package2.mod2 import * #How to import members of mod2 of sub-package package2 in package1 with from statement
print(x) #How to print variable 'x' of  mod2 in sub-package package2 of package1
f1() #How to call function f1() of mod2 in sub-package package2 of package1
a=c1()
a.m1() #How to call method m1() of class c1 in mod2 of sub-package package2 in package1
