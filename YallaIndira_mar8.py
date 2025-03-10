'''program1:Write  a  program  to  merge  two  strings  to  form  a  new  string
1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI'''

a=input("Enter first string : ")
b=input("Enter second string : ")
num=min(len(a),len(b))
c=''
for i in range(num):
	c=c+a[i]+b[i]
if len(a)>len(b):
	print(f"result : {c+a[num:]}")
else:
	print(f"result : {c+b[num:]}")

'''outputs:Enter first string : INDU
Enter second string : python
result : IpNyDtUhon '''

#program2:Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
a=input("Enter any string : ")
out=''
for x in a:
	if x not in out:
		out=out+x
print(f'string without duplicates : {out}')

'''outputs:Enter any string : rama rao
string without duplicates : ram o'''

#program3:len() function demo  
funcprint(len('Hyd'))  #  3
print(len('Rama Rao')) #  8
print(len('9247'))   #  4
print(len('+-$'))  #  3
print(len(''))   #  0
print(len(' '))  #  1
print(len('A2#'))  #  3
print(len(3456)) #error
print('Sec'. len()) #error

#program4:chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90)) #  Z   becoz  90  is  unicode  value  of  'Z'
print(chr(97)) #  a   becoz  97  is  unicode  value  of  'a'
print(chr(122)) #  z   becoz  122  is  unicode  value  of  'a'
print(chr(48)) #  1   becoz  48 is  unicode  value  of  '1'
print(chr(57)) #  9   becoz  57 is  unicode  value  of  '9'
print(chr(36)) #  $   becoz  36  is  unicode  value  of  '$'
print(chr(32)) #     becoz  32  is  unicode  value  of  ' '

#program5: ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))  #  Unicode  value  of  'Z'  i.e.  90
print(ord('a'))  #  Unicode  value  of  'a'  i.e.  97
print(ord('z'))  #  Unicode  value  of  'z'  i.e.  122
print(ord('0'))  #  Unicode  value  of  '0'  i.e.  48
print(ord('9'))  #  Unicode  value  of  '9'  i.e.  57
print(ord('$'))  #  Unicode  value  of  '$'  i.e.  36
print(ord(' ')  #  Unicode  value  of  ' '  i.e.  32

'''program6:Let  input  be  A4M3Z5D2
What  is  the  output ?  --->  AEMPZ_DF'''

a=input('Enter any string with alternate character and digit : ')
b=''
for i in range(0,len(a),2):
	A=ord(a[i])
	c=A+int(a[i+1])
	b=b+a[i]+chr(c)
print(f'Result : {b}')

'''outputs:Enter any string with alternate character and digit : a2b5c3
Result : acbgcf'''
