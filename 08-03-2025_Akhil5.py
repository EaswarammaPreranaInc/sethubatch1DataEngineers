#1 Write  a  program  to  merge  two  strings  to  form  a  new  string
a=str(input('Enter string 1 : '))
b=str(input('Enter string 2 : '))
c=''
l1,l2=len(a),len(b)
for i in range(min(l1,l2)):
	c+=a[i]+b[i]
if l1 > l2:
	c+=a[l2:]
else:
	c+=b[l1:]

print('Merged string : ',c)

#2Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
a=str(input('Enter a string : '))
b=''
for x in a:
	if x not in b:
		b+=x
print(b)

#3
try:
	s=str(input('Enter  any  string  with  alternate  character  and  digit  :  '))
	c=''
	for i in range(0,len(s),2):
		char=s[i]
		num=s[i+1]
		c+=char
		t=chr(ord(char)+int(num))
		c+=t
	print(c)

except ValueError:
	print('Enter  any  string  with  alternate  character  and  digit')
