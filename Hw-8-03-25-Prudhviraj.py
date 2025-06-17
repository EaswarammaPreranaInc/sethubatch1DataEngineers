#Write  a  program  to  merge  two  strings  to  form  a  new  string
a=input("Enter the First String: ")
b=input("Enter the Second String: ")
m=min(len(a),len(b))
i=0
s=''
while i<m:
	s+=a[i]+b[i]
	i+1
	break
if (m==len(a)):
	s+=b[m:]
else:
	s+=a[m:]
print(F"Result={s}")

'''
Output:
Enter  first  string  :  VAMSI
Enter  second  string  :  HYD
Result  :   VHAYMDSI
'''
#Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
a=input("Enter the string: ")
b=''
for i in a:
	if i not in b:
		b+=i
print(F"String with out duplicate :{b}")
'''
Output:
Enter  any  string  :  MISSISIPI
String  without  duplicates  :    MISP
'''


#Let  input  be  A4M3Z5D2
#What  is  the  output ?  --->  AEMPZ_DF

a=input("Enter the String: ")
c=''
for i in range(0,len(a),2):
	c+=a[i]+chr(ord(a[i])+int(a[i+1]))
print(c)
'''
Output:
Enter  any  string  with  alternate  character  and  digit  :  M3K2$5z2
Result  :   MPKM$)z|
'''


# ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))  #  Unicode  value  of  'z'  i.e.  90
print(ord('a'))  #  Unicode  value  of  'a'  i.e.  97
print(ord('z'))  #  Unicode  value  of  'z'  i.e.  122
print(ord('0'))  #  Unicode  value  of  '0'  i.e.  48
print(ord('9'))  #  Unicode  value  of  '9'  i.e.  57
print(ord('$'))  #  Unicode  value  of  '$'  i.e.  36
print(ord(' '))  #  Unicode  value  of  ''   i.e.  32


# len()  function  demo  program  (Home  work)
print(len('Hyd'))     #  3
print(len('Rama Rao'))#  8
print(len('9247'))    #  4
print(len('+-$'))     #  3
print(len(''))        #  0
print(len(' '))       #  1
print(len('A2#'))     #  3
print(len(3456))      #   Nothing is returned
print('Sec'. len())   #  Nothing is returned


# chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90)) #  Z
print(chr(97)) #  a
print(chr(122))#  z
print(chr(48)) #  0
print(chr(57)) #  9
print(chr(36)) #  $
print(chr(32)) #  Nothing is returned
