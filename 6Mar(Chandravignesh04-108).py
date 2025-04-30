'''
try:
	a = eval(input("enter the string1: ")) #PYTHON
	b = eval(input("enter the string2: ")) #JAVA
		print(F'{a[0:2]}{b[2:len(b)]} {b[0:2]}{a[2:len(a)]}')
except NameError:
	print(F'The input must be a string with quotes')
'''
'''
try:
	a = eval(input("enter the string: "))
	if len(a)>=4:
		print(F'{a[0:2]}{a[len(a)-2:len(a)]}')
	else:
		print(F'The string should be more than four character')
except NameError:
	print(F'The input must be a string with quotes')
except TypeError:
	print(F'The input must be a string with quotes not number')
'''
'''
try:
	a = eval(input("enter the string1: "))
	print('character in forward')
	for x in range(len(a)):
		print(F'Character  at index {x} : {a[x]}')
	print()
	print('character in reverse')
	for x in range((len(a) - 1), -1, -1):
		print(F'Character  at index {-x} : {a[x]}')
except TypeError:
	print(F'the input should be string')
except NameError:
	print(F'The input must be a string with quotes')
	
'''
'''
try:
	a = eval(input("enter the string1: "))
	even=""
	odd=""
	for x in range(len(a)):
		if x%2==0:
			even+=a[x]
				else:
			odd+=a[x]
	print(F'Characters at even object :{even}') 
	print(F'Characters at odd object :{odd}')

except TypeError:
	print(F'the input should be string')
except NameError:
	print(F'The input must be a string with quotes')
'''
'''
try:
	x = eval(input('Enter  any  string  with  alternate  character  and  digit : '))
	p =""
	y =""
	print(x)
	for i in range(len(x)):
		if i%2==0:
			y=x[i]
			print(y)
		else:
			p = p + y*eval(x[i])
		print(F'Result: {p}')
except TypeError:
	print(F'the input should be string')
except NameError:
	print(F'The input must be a string with quotes')
'''

'''
a = eval(input("enter the string1: "))
output = ""
# Iterate through the list with step of 2
for i in range(0, len(a), 2):
    x = a[i]  # Get character
    y = int(a[i + 1])  # Get repetition count
    output += x * y  # Append repeated character

# Print final output
print(output)
'''