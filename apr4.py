'''#program to print random frm string
from random import *
def ran(n):
	for i in range(10):
		print(choice(n))
n=input('enter the string: ')
ran(n)
'''
''' #create password
from random import *
def pwd():
	a='ABCDEFGHIJKLMNOPQRSTUVWYZ'
	b='12345679'
	for i in range(10):
		pwd=" "
		for i in range(6):
			if i%2==0:
				pwd+=choice(a)
			else:
				pwd+=choice(b)
		print(pwd)
pwd()
'''
'''#progra for random output
from random import *
def rep(n):
	for i in range(10):
		print(choice(n))
n=[10.8,25,'hyd',True,None,3+4j]
rep(n)
'''
'''#random output
from random import *
def rep():
	i=0
	while i<=10:
		print(randrange(100000,999999))
		i+=1
rep()
'''
'''#opening of webbrowser
from time import *
from webbrowser import *
def web(n):
	for i in n:
		print(open_new_tab(i))
	sleep(5)
n=['google.com','rediif.com','gmail.com','amazon.com','netflix.com']
web(n)
'''


























