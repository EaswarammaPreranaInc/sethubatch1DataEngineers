#1
s1=str(input('Enter string 1 :'))
s2=str(input('Enter string 2 :'))
s3=s2[0:1]+s1[1:]+' ' +s1[0:1]+s2[1:]
print(s3)

#2
s=str(input('Enter a string : '))
if len(s)< 4 :
	print('String should have minimum 4 letters')
else:
	print(s[0:2] + s[len(s)-2:])

#3
s=str(input('Enter a string : '))
print('Characters of the string in forward direction :')
for x in s:
	print(f'Character at index {s.index(x)}: {x}')
print('Characters of the string in reverse direction :')
for x in reversed(s):
	print(f'Character at index  {s.index(x)}: {x}')

#4
s=str(input('Enter a string : '))
print('Characters in even index : ',end='')
for x in s:
	if s.index(x)%2==0 :
		print(x,end='')
print()
print('Characters in odd index : ',end='')
for x in s:
	if s.index(x)%2 !=0:
		print(x,end='')
print()

#5
a=input("enter string:")
for i in range(0,len(a),2):
	print(a[i]*int(a[i+1]),end='')
print()
