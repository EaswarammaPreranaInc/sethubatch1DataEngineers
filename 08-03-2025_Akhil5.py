#1 Write  a  program  to  merge  two  strings  to  form  a  new  string
a=str(input('Enter string 1 : '))
b=str(input('Enter string 2 : '))
c=''
i=0
while (i<len(a) and i<len(b)):
	c+=a[i]+b[i]
	i+=1
if len(a) > len(b):
	print(c+a[i:])
else:
	print('Merged string : ',c+b[i:])
# Output:
#Enter string 1 : abcde
#Enter string 2 : 12345
#Merged string :  a1b2c3d4e5

#2Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
a=str(input('Enter a string : '))
b=''
for x in a:
	if x not in b:
		b+=x
print('String without duplicates : ',b)
#Output:
#Enter a string : aaabbbcccddd
#String without duplicates :  abcd

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
	print('Result : ',c)

except ValueError:
	print('Enter  any  string  with  alternate  character  and  digit')
#Output:
#Enter  any  string  with  alternate  character  and  digit  :  A2B6H2C8
#Result :  ACBHHJCK
