'''
1. Write  a  program  to  merge  two  strings  to  form  a  new  string
1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI
             0     1    2
a  --->      H     Y    D

              0    1     2     3    4
b  --->       V    A     M     S    I

i       a[i]        b[i]          c
--------------------------------------------------------
                                    ''
0     'H'        'V'           '' + 'H' + 'V' = 'HV'
1     'Y'         'A'           'HV' + 'Y' + 'A' =  'HVYA'
2     'D'         'M'          'HVYA' + 'D' + 'M' =  'HVYADM'
--------------------------------------------------------
1) What  action  to  be  made  when  1st  string  got  exhausted ?  --->  Concatenate  remaining  chars  of  2nd    string  to  object  'c'

2) What  action  to  be  made  when  2nd  string  got  exhausted ?  --->  Concatenate  remaining  chars  of  1st  string  to  object  'c'


3) Hint:  Use  while  loop  and  slice (outside)
'''
a=input("Enter 1st string:")
b=input("Enter 2nd string:")
c=""
i=0
while i<len(a) and i<len(b):
	c=c+a[i]+b[i]
	i=i+1
	
if len(a)<len(b):
	c=c+b[i:]
	print(c)
else:
	c=c+a[i:]
	print(c)
 

'''
2.Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
    What  is  the  output ? --->  RAM<space>O

2) out = '' + 'R' + 'A' + 'M' + ' ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																						Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->  Ignore  the  character

5) Hint:  Use  not  in   operator
'''

a=input("Enter a string:")
out=""
for i in range(len(a)):
	if a[i] not in out:
		out=out+a[i]
print(out)


# 3.len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) # 8
print(len('9247'))     # 4
print(len('+-$'))      # 3
print(len(''))         # 0
print(len(' '))        # 1
print(len('A2#'))      # 3
#print(len(3456))       # Error
#print('Sec'. len())    # *** Error ***
'''
What  does  len(str)  do  ?  --->  Returns  number  of  characters  in  the  string
'''

# 4.ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))  #  Unicode  value  of  'Z'  i.e.  90
print(ord('a'))  #  Unicode  value  of  'a'  i.e.  97
print(ord('z'))  #  Unicode  value  of  'z'  i.e.  122
print(ord('0'))  #  Unicode  value  of  '0'  i.e.  48
print(ord('9'))  #  Unicode  value  of  '9'  i.e.  57
print(ord('$'))  #  Unicode  value  of  '$'  i.e.  36
print(ord(' '))  #  Unicode  value  of  ' '  i.e.  32
'''
ord()  function
------------------
1) What  does  ord()  function  do ?  --->  Converts  character  to  unicode  value

2) How  many  unicode  values  exist ?  --->  512

3) What  is  the  range  of  unicode  values ?  --->  0  to  511

4) What  are  the  unicode  values  of  'A'  -  'Z' ?  --->  65  to  90
    What  are  the  unicode  values  of  'a'  -  'z' ?  ---> 97  to  122
    What  are  the  unicode  values  of  '0'  -  '9' ?  --->  48  to  57

5) What  is  another  name  of  unicode ?  ---> Extended  Ascii

Note:  chr()  and  ord()  are  quite  opposite  functions
'''

# 5.chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90)) #  Z   becoz  90  is  unicode  value  of  'Z'
print(chr(97)) #  a   becoz  97  is  unicode  value  of  'a'
print(chr(122))#  z   becoz  122  is  unicode  value  of  'z'
print(chr(48)) #  0   becoz  48  is  unicode  value  of  '0'
print(chr(57)) #  9   becoz  57  is  unicode  value  of  '9'
print(chr(36)) #  $   becoz  36  is  unicode  value  of  '$'
print(chr(32)) #  " "  becoz  65  is  unicode value  of  ' '
'''
What  does  chr()  function  do ?  --->   Converts  unicode  value  to  character
'''

'''
6.Let  input  be  A4M3Z5D2
What  is  the  output ?  --->  AEMPZ_DF
 0     1     2     3    4    5    6     7
 A     4     M     3    Z    5    D     2
Iteration        i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                                              ''
     1               0       'A'         '4'             '' + 'A' + 'E' = 'AE'

	 2              2       'M'         '3'             'AE' + 'M' + 'P' = 'AEMP'

	 3              4       'Z'         '5'             'AEMP' + 'Z' + '' = 'AEMPZ'

	 4              6       'D'         '2'             'AEMPZ_' + 'D' +'F' = 'AEMPZ_DF'
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions
Enter  any  string  with  alternate  character  and  digit  :  M3K2$5z2
Result  :   MPKM$)z|
Enter  any  string  with  alternate  character  and  digit  :  hyd
Pls  enter  string  with  alternate  char  and  digit
'''
try:
	a=input("Enter  any  string  with  alternate  character  and  digit:")
	b=""
	for i in range(0,len(a),2):
		b=b+a[i]+chr((ord(a[i])+int(a[i+1])))
	print(b)
except:
	print("Pls  enter  string  with  alternate  char  and  digit")

