'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI

          0     1    2
a  --->   H     Y    D
          0    1    2    3    4
b  --->   V    A    M    S    I
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
a = input('Enter 1st String: ')
b = input('Enter 2nd String: ')
c = ' '
i = 0
while i < len(a) and  i < len(b) :
		c += a[i] + b[i]
		i += 1
c += a[i:] + b[i:]
print(c)

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
x = input('Enter input to remove duplicates:')
y = ''
for i in x:
	if i not in y:
		y += i
print(y)


# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('+-$')) # 3
print(len('')) # 0
print(len(' ')) # 1
print(len('A2#')) # 3
#print(len(3456)) # Error
#print('Sec'. len()) # Error


# chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90)) # Z
print(chr(97)) # a
print(chr(122)) # z 
print(chr(48)) # 0
print(chr(57)) # 9
print(chr(36)) # $
print(chr(32)) # ' '

'''
What  does  chr()  function  do ?  --->   Converts  unicode  value  to  character
What  does  ord()  function  do ?  --->  Converts  character  to  unicode  value
'''
# ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))  # 90
print(ord('a')) # 97
print(ord('z')) # 122
print(ord('0')) # 48
print(ord('9')) # 57
print(ord('$')) # 36
print(ord(' ')) # 32

'''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0    1     2     3    4    5    6     7
 A    4     M     3    Z    5    D     2


Iteration        i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                                              ''
     1               0       'A'         '4'             '' + 'A' + 'E' = 'AE'

	 2              2       'M'         '3'             'AE' + 'M' + 'P' = 'AEMP'

	 3              4       'Z'         '5'             'AEMP' + 'Z' + '_' = 'AEMPZ_'

	 4              6       'D'         '2'             'AEMPZ_' + 'D' +'F' = 'AEMPZ_DF'
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions
'''
try:
	x = input('Enter any string with alternate one character and one integer : ')
	z = ''
	for i in range (0,len(x),2):
		y = ord(x[i]) + int(x[i+1])
		z += x[i] + chr(y)
	print(z)
except ValueError:
	print('Please enter string with alternate character and integer.')
