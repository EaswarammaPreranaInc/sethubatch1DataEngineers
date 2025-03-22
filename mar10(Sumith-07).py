'''
#Program to check vowels
a = input("enter the string: ")
b=""
i=0
for i in range(len(a)):
	if a[i] in ['a','e','i','o','u','A','E','I','O','U']:
		b += a[i]
	i+=1

print(F' string with vowels: {b.upper()}')
'''
'''
#Program for find()
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . find('is')
print(index)
while ( index != -1 ):
	print(index:= a . find('is' , index+1))
print('End')
'''
'''
#Program to check index
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
	index = a . index('is')
	while  index != -1:
		print(index)
		index = a . index('is' , index + 1)
	print('End')
except ValueError:
	print("string not found at that index")
'''
'''a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' , index + 1)
print('End')
'''
'''
#Program to check rindex()
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
	index = a . rindex('is')
	while  index != -1:
		print(index)
		index = a . rindex('is' , index + 1)
	print('End')
except ValueError:
	print("string not found at that index")
'''
'''
#replace first char with *
a = input("enter the string: ")
x=a[0]
b=x
for char in a[1:]:
	if char == x:
		b+= '*'
	else:
		b+=char
print(b)
'''
'''
#program to sum the input splited by +
try:
	a = (input('enter the expression: '))
	b=(a.split('+'))
	c=[]
	sum=0
	for i in b:
		c.append(int(i))
	for x in range(len(c)):
		sum+=c[x]
	print(F' Sum: {sum}')
except ValueError:
	print("Inputs should be integers")
'''
'''
#Program to add suffiexs at end for len>3
try:
	a = input("enter the string: ")
	if len(a)>3:
		if a.endswith('ing'):
			print(a+'ly')
		else:
			print(a+'ing')
	else:
		print(a)
except ValueError:
	print("Inputs should be strings")
'''




