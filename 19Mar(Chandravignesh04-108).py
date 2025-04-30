'''
def f1(a="hyd" ,b=[]):
	a+='sec'
	b+=[1,2,3]
	print('a:', a)
	print('b:', b)
print('default values:',f1._defaults_)
f1()
print('default values:',f1._defaults_)
f1()
print('default values:',f1._defaults_)
f1()
'''

'''
def   f1(x, a=[]):
	if a==[]:
		a=[]
	for i in range(x):
		a.append(i*i)
		return a
print(f1(3))
print(f1(4,[10,20,15,18]))
print(f1(5))
print(f1(a=[100,200,300],x=6))
print(f1(6))
'''

'''program to print all numbers
from prime import *
def num(n):
	count=0
	for z in range(2,n+1):
		if  prime(z):
			print(z)
			count+=1
	print(F'number of primes are: {count}')
n=int(input("enter the number"))
num(n)
'''