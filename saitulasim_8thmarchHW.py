# 1: Write  a  program  to  merge  two  strings  to  form  a  new  string
# Hint : Use while loop and slice(outside)
a=input("Enter first string : ")
b=input("Enter second string : ")
num=min(len(a),len(b))
c=''
i=0
while i <= len(a)-1 and i<= len(b)-1:
	c+=a[i]+b[i]
	i+=1
if len(a) > len(b):
		c+=a[i:]
else:
			c+=b[i:]
			print(c)
# 2: Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

a=input("Enter any string : ")
b=''
for i in a:
	if i not in b:
		b+=i
print('string without duplicates : ',b)

# 3: len() function demo  
print(len('Hyd'))  #  3
print(len('Rama Rao')) #  8
print(len('9247'))   #  4
print(len('+-$'))  #  3
print(len(''))   #  0
print(len(' '))  #  1
print(len('A2#'))  #  3
#print(len(3456)) #error
#print('Sec'. len()) #error

# 4:chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90)) #  Z   becoz  90  is  unicode  value  of  'Z'
print(chr(97)) #  a   becoz  97  is  unicode  value  of  'a'
print(chr(122)) #  z   becoz  122  is  unicode  value  of  'a'
print(chr(48)) #  1   becoz  48 is  unicode  value  of  '1'
print(chr(57)) #  9   becoz  57 is  unicode  value  of  '9'
print(chr(36)) #  $   becoz  36  is  unicode  value  of  '$'
print(chr(32)) #     becoz  32  is  unicode  value  of  ' '

# 5: ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))  #  Unicode  value  of  'Z'  i.e.  90
print(ord('a'))  #  Unicode  value  of  'a'  i.e.  97
print(ord('z'))  #  Unicode  value  of  'z'  i.e.  122
print(ord('0'))  #  Unicode  value  of  '0'  i.e.  48
print(ord('9'))  #  Unicode  value  of  '9'  i.e.  57
print(ord('$'))  #  Unicode  value  of  '$'  i.e.  36
print(ord(' ')) #  Unicode  value  of  ' '  i.e.  32

#n6: Enter any string with alternatte charcter and digit
try:
	a=input('Enter any string with alternate character and digit : ')
	b=''
	for i in range(0,len(a),2):
		b+= a[i]+chr(ord(a[i])+int(a[i+1]))
		print(b)
except:
	print('Enter string with alternate char and digit')
