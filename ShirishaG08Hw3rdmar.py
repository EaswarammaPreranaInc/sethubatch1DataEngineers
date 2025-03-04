#prgm to print each element and the corresponding index
'''
a=[25, 10.8, 'Hyd', True]
print('Indexed for loop')
for i in range(4):
	print(i, a[i])
print('For each loop') #not possible if we are using only for each loop without using slice and another varaible
for i in a:
	print(a.index(i), i)
'''

#How to print list elements in reverse order without slice
'''
try:
	a=eval(input('Enter list of elements:'))
	print('Indexed for loop')
	for i in range(-1,-len(a)-1,-1):
		print(a[i])
	print('For each loop') 
	for i in reversed(a): #  not possible if we are using only for each loop without using slice and another varaibl
		print(i)
except: 
	print('Enter string in quotes')
'''

#program to add two lists and store in 3rd list
'''
a=eval(input('Enter 1st list:'))
b=eval(input('Enter 2nd list:'))
c=[]
if len(a)==len(b):
	print('Indexed for loop')
	for i in range(len(a)):
		c.append(a[i]+b[i])
		print('3rd list:',c)
		print('for each loop')
		d=[]
		for i,j in zip(a,b):
			d.append(i+j)
			print('3rd list:',d)
else:
	print('Lists are of different lengths')
'''

#print list elements from indexed 2 to 4 without slice
'''
a=[25, 10.8, 'Hyd', True, 3+4j, None, 'sec']
print('Indexed for loop')
for i in range(2,5):
	print(a[i])
c=0
print('for each loop') # not possible if we are using only for each loop without using slice and another varaible
for i in a:
	if(c>=2 and c<=4):
		print(i)
	c+=1
'''

#Gift
'''
a=[10,20,15,18]
for i in range(len(a)):
	a[i]+=1 #Increment each element of 'a' by 1
	print('a:', a) #[11,21,16,19]
b=[10,20,15,18]
for x in b:
	x+=1    # Increment of x is done not list b
print('b:', b)  #[11,21,16,19]
'''

#print first 20 even numbers with while loop
'''
print('First 20 even numbers')
i=1
while(i<=20):
	print(2*i)
	i+=1
'''

#program to print first 20 odd numbers with while loop
'''
print('First 20 odd numbers')
i=1
while(i<=20):
	print(2*i-1)
	i+=1
'''

#print natural numbers 1 to n
'''
n=int(input('Enter value of n:'))
print('Natural numbers')
for i in range(1, n+1):
	print(i)
	i+=1
'''

#print(1-10) in reverse order
'''
print('Numbers from 10 down to 1 in steps of -1')
for i in range(10,0,-1):
	print(i)
'''

#print upper and lower case alphabets
'''
print('unicode to alphabets')
for i in range(65,91):
	print(chr(i),end=' ')
print()
for i in range(97,123):
	print(chr(i),end=' ')
print()
print('Alphabets using ord()')
for i in range(ord('A'), ord('Z')+1):
	print(chr(i),end=' ')
print()
for i in range(ord('a'),ord('z')+1):
	print(chr(i),end=' ')
'''

#program to print first n terms of fibonacci series
'''
try:
	n=int(input('Enter number of terms:'))
	print('Fibonacci series')
	a=0
	b=1
	c=a+b
	if n==0:
		print(a)
	else:
		print(a,b,sep='\n')
		for i in range(3,n+1):
			print(c)
			a=b
			b=c
			c=a+b
except:
	print('Give an integer number')
'''

#search for x in fibonacci series
'''
x=int(input('Enter the value to be searched:'))
a=0
b=1
c=a+b
if (x==a or x==b):
	print('Found')
else:
	for i in range(x):
		if (x==c):
			print('Found')
			exit()
		a=b
		b=c
		c=a+b
	print('Not Found')
'''

#Determine 1.1+2.2+3.3...n terms
'''
try:
	n=int(input('How many terms would you like to add:'))
	sum=0
	for i in range(1, n+1):
		sum+=1.1*i
	print('sum:', sum)
except:
	print('Input should be an integer')
'''

# program to print sum of first 20 even numbers
'''
sum=0
i=1
while(i<=20):
	sum+=2*i
	i+=1
print('Sum of first 20 even numbers:', sum)
'''

# program to print sum of first 20 odd numbers
'''
sum=0
i=1
while(i<=20):
	sum+=2*i-1
	i+=1
print('Sum of first 20 odd numbers:', sum)
'''

#program to determine 1+2+3+...+n without using formula n*(n+1)/2
'''
n=int(input('How many terms would you like to add:'))
sum=0
for i in range(n+1):
	sum+=i
print('Sum:', sum)
'''

#Find  outputs  (Home  work)
'''
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
'''

# Identify Error  (Home  work)
'''
if ():
	print('Hyd')
	continue # there is no keyword continue  without for loop
	print('Sec')
'''

# Find outputs (Home  work)
'''
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
'''

# Identify Error  (Home  work)
'''
if(10 , 20 , 30):
	print('Hyd')
	break # there is no keyword continue  without for loop
	print('Sec')
'''

# Find  outputs  (Home  work)
'''
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
'''


# Find  outputs  (Home  work)
'''
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
'''
