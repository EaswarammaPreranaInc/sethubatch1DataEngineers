#1ST PROGRAM
'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI

             0     1    2
a  --->   H     Y    D

              0    1     2     3    4
b  --->    V    A    M    S    I


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
CODE:
a=input("enter string1:")
b=input("enter string2:")
c=""
i=0
j=0
while i<len(a) and j<len(b):
	c+=a[i]+b[j]
	i+=1
	j+=1

c+=a[i:]+b[j:]
print(c)

OUTPUT:
enter string1:HYD
enter string2:VAMSI
HVYADMSI



2ND PROGRAM
'''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2


Iteration        i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                                              ''
     1               0       'A'         '4'             '' + 'A' + 'E' = 'AE'

	 2              2       'M'         '3'             'AE' + 'M' + 'P' = 'AEMP'

	 3              4       'Z'         '5'             'AEMP' + 'Z' + '' = 'AEMPZ'

	 4              6       'D'         '2'             'AEMPZ_' + 'D' +'F' = 'AEMPZ_DF'
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions
'''
CODE:
try:
  a=input("enter string with alternate character and string:")
  c=''
  for i in range(0,len(a),2):
	  char=a[i]
	  num=a[i+1]
	  c+=char
	  new_char=chr(ord(char)+int(num))
    
	  c+=new_char
  print(c)
except ValueError:
	print("enter string with alternate char and int")

OUTPUT:
enter string with alternate character and string:A4M3Z5D2
AEMPZ_DF
enter string with alternate character and string:hyd
enter string with alternate char and int



3RD PROGRAM
'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
    What  is  the  output ? --->  RAM<space>O

2) out = '' + 'R' + 'A' + 'M' + ' ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																						Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->  Ignore  the  character

5) Hint:  Use  not  in   operator
'''
CODE:
a=input("enter a string:")
out=''
for i in range(len(a)):
	if a[i] not in out:
		out+=a[i]
print(out)

OUTPUT:
enter a string:RAMA  RAO
RAM O


