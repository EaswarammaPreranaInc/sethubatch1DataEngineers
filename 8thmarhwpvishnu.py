#08mar2025
# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) 
print(len('9247'))
print(len('+-$')) 
print(len('')) 
print(len(' ')) 
print(len('A2#')) 
#print(len(3456)) 
#print('Sec'. len())


# chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90))#Z
print(chr(97))#a
print(chr(122))#z
print(chr(48))#0
print(chr(57))#9
print(chr(36))#$
print(chr(32))#space
print(chr(33))#exclamation sysmbol


# ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))#90
print(ord('a'))#97
print(ord('z'))#122
print(ord('0'))#48
print(ord('9'))#57
print(ord('$'))#36
print(ord(' '))#32

#Write  a  program  to  merge  two  strings  to  form  a  new  string
a = 'hyd'
b = 'vamsi'
c=''
i=0
length = min(len(a), len(b))
while i<=length:
	if i>=length:
		break
	else:
		c+=a[i]+b[i]
		i+=1
if len(a)>len(b):
	print(c+a[length+1:])
else:
	print(c+b[length+1:])


#Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
a = input('enter a string:')
b = ''
for x in a:
	if x not in b:
		b += x
print(b)

#
a=input('enter a string')
c = "" 
i = 0     
while i < len(s):
	char = a[i]
	if i + 1 < len(s):
		a = int(a[i + 1])  # Convert the number to an integer
		# Shift the character by the given number of positions
		b = chr(ord(char) + a)
		c += char + b  
		i += 2  
	else:
		c += char  
		i += 1  
print(c)