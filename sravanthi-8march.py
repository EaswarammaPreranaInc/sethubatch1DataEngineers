Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI

             0     1    2
a  --->   H     Y    D

              0    1     2     3    4
b  --->    V    A    M    S    Ii       a[i]        b[i]          c
--------------------------------------------------------
                                    ''
0     'H'        'V'           '' + 'H' + 'V' = 'HV'
1     'Y'         'A'           'HV' + 'Y' + 'A' =  'HVYA'
2     'D'         'M'          'HVYA' + 'D' + 'M' =  'HVYADM'
--------------------------------------------------------
1) What  action  to  be  made  when  1st  string  got  exhausted ?  --->  Concatenate  remaining  chars  of  2nd    string  to  object  'c'

2) What  action  to  be  made  when  2nd  string  got  exhausted ?  --->  Concatenate  remaining  chars  of  1st  string  to  object  'c'
) Hint:  Use  while  loop  and  slice (outside)

a=input("Enter first string:")
b=input("Enter second string:")
c=""
i=0
while i<len(a) and i<len(b):
	c=c+a[i]+b[i]
	i+=1
if i<len(a):
	c=c+a[i:]
if i<len(b):
	c=c+b[i:]
print(c)
output:
Enter first string:hyd
Enter second string:vamsi
hvyadmsi
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
    What  is  the  output ? --->  RAM<space>O

2) out = '' + 'R' + 'A' + 'M' + ' ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																						Concatenate  the  character  to  out  object
4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->  Ignore  the  character

5) Hint:  Use  not  in   operator
a=input("Enter any string:")
out=""
print("String without duplicates:")
for char in a:
	if char not in out:
	 out=out+char
print(out)
output:
Enter any string:RAMA RAO
String without duplicates:
RAM O
# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) 
print(len('9247'))
print(len('+-$')) 
print(len('')) 
print(len(' ')) 
print(len('A2#')) 
print(len(3456)) 
print('Sec'. len()) 
output:
3
8
4
3
0
1
3
# chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90))
print(chr(97))
print(chr(122))
print(chr(48))
print(chr(57))
print(chr(36))
print(chr(32))
output:
A
Z
a
z
0
9
$
# ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))
print(ord('a'))
print(ord('z'))
print(ord('0'))
print(ord('9'))
print(ord('$'))
print(ord(' '))

output:
65
90
97
122
48
57
36
32


