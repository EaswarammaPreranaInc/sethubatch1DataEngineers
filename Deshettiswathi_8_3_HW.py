Q1
#Write  a  program  to  merge  two  strings  to  form  a  new  string
1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI

a=input('Enter first string: ')
b=input('Enter second string: ')
c=''
i=0
while i < len(a) and i< len(b):
	c+=a[i]+b[i]
	i+=1
c+=a[i:]+b[i:]
print('Result: ',c)

OP-
Enter  first  string  :  VAMSI
Enter  second  string  :  HYD
Result  :   VHAYMDSI
---------------------------------------------------------------------------------------------------------------------------------------------
Q2
#Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

a=input('Enter any string: ')
b=''
for i in range(len(a)):
	if a[i] not in b:
		b+=a[i]
print('String without duplicates: ',b)

OP-
Enter  any  string  :  MISSISIPI
String  without  duplicates  :    MISP
----------------------------------------------------------------------------------------------------------------------
Q3
# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) #8
print(len('9247')) #4
print(len('+-$'))  #3
print(len(''))    #0
print(len(' '))   #1
print(len('A2#'))  #3
#print(len(3456))   #error because length cannot determine for int 
print('Sec'. len())  #error- format is incorrect
-----------------------------------------------------------------------------------------------------------------------
Q4
# chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90)) #  Z   becoz  90  is  unicode  value  of  'Z'
print(chr(97)) #  a   becoz  97  is  unicode  value  of  'a'
print(chr(122)) # z   becoz  122  is  unicode  value  of  'z'
print(chr(48))  # 0   becoz  48  is  unicode  value  of  '0'
print(chr(57))  # 9   becoz  57  is  unicode  value  of  '9'
print(chr(36))  # $   becoz  36  is  unicode  value  of  '$'
print(chr(32))  #' '  becoz  32  is  unicode  value  of  ' '
-----------------------------------------------------------------------------------------------------------------------
Q5
# ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))  #  Unicode  value  of  'Z'  i.e.  90
print(ord('a'))  #  Unicode  value  of  'a'  i.e.  97
print(ord('z'))  #  Unicode  value  of  'z'  i.e.  112
print(ord('0'))  #  Unicode  value  of  '0'  i.e.  48
print(ord('9'))  #  Unicode  value  of  '9'  i.e.  57
print(ord('$'))  #  Unicode  value  of  'Z'  i.e.  36 
print(ord(' '))  #  Unicode  value  of  'Z'  i.e.  32
----------------------------------------------------------------------------------------------------------------
Q6 
Character ASCII Shift Using Digits
Let  input  be  A4M3Z5D2
What  is  the  output ?  --->  AEMPZ_DF

try:
	a=input('Enter  any  string  with  alternate  character  and  digit  :')
	b=''
	for i in range(len(a)):
		if i%2==0:
			c=ord(a[i])+int(a[i+1])
			b+=a[i]+str(chr(c))
	print(b)
except ValueError:
	print('Pls  enter  string  with  alternate  char  and  digit')

OP-
Enter  any  string  with  alternate  character  and  digit  :  M3K2$5z2
Result  :   MPKM$)z|
Enter  any  string  with  alternate  character  and  digit  :  hyd
Pls  enter  string  with  al
