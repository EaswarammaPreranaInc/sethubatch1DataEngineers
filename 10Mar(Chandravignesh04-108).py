'''
a = input("Enter the first string: ")
b = input("Enter the second string: ")

c = ""
i = 0

while i < min(len(a), len(b)):
    c += a[i] + b[i]
    i += 1

c += a[i:] + b[i:]
print(c)
'''
'''
a = input("enter the string: ")
b=""
i=0
while i <len(a) :
	if a[i] not in b:
		b += a[i]
	i+=1
print(F' string without duplicates: {b=}')
'''
'''
try:
	a = input("enter the string: ")
	out = ""
	for i in range(0, len(a), 2):
		char = a[i]
		digit = a[i + 1]
		out += char
		x = ord(char)
		y = x + int(digit)
		new_char = chr(y)
		out += new_char
	print(out)
except ValueError:
	print("please enter string and digit")
'''