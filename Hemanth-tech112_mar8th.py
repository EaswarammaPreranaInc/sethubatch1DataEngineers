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
try:
    a=eval(input('Enter 1st input : '))
    b=eval(input('Enter 2nd input : '))
    c=''
    i=0
    while i<len(a):
        c=c+a[i]+b[i]
        i=+i+1
    r=c+b[len(a):]
    print('Result : ',r)
except NameError:
    print('Input string should be in quotes')
except TypeError:
    print('Input should be only string not integer or float')

'''
Enter 1st input : 'HYD'
Enter 2nd input : 'VAMSI'
Result :  HVYADMSI

Enter 1st input : 1234
Enter 2nd input : 123
Input should be only string not integer or float

Enter 1st input : Hyd
Input string should be in quotes

Enter 1st input : 'RAJU'
Enter 2nd input : 'HEMANTH'
Result :  RHAEJMUANTH

'''


'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
    What  is  the  output ? --->  RAM<space>O

2) out = '' + 'R' + 'A' + 'M' + ' ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																						Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->  Ignore  the  character

5) Hint:  Use  not  in operator
'''
a=eval(input('Enter any string : '))
out=''
for x in a:
    if x not in out:
        out=out+x
print('String without duplicates : ',out)

'''
Enter any string : 'RAMA RAO'
String without duplicates :  RAM O

Enter any string : 'MISSISIPI'
String without duplicates :  MISP
'''



# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao'))  # 8
print(len('9247'))  # 4
print(len('+-$'))   # 3
print(len(''))   # 0 or Empty string
print(len(' '))   # 1
print(len('A2#'))  # 3
# print(len(3456))  # Error because int object is non-sequence it has no len() function
# print('Sec'. len())  # Error because str object has no attribute len()

''' Output
3
8
4
3
0
1
3
'''


# chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90))  # Z because 90 is unicode value of 'Z'
print(chr(97))  # a because 97 is unicode value of 'a'
print(chr(122))  # z because 122 is unicode value of 'z'
print(chr(48))  # 0 because 48 is unicode value of 0
print(chr(57))  # 9 because 57 is unicode value of 9
print(chr(36))  # 9 because 36 is unicode value of 9
print(chr(32))  # <space> because 32 is unicode value of <space bar>

'''  Output
A
Z
a
z
0
9
$
 
'''


# ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))  # Unicode  value  of  'Z'  i.e. 90
print(ord('a'))  # Unicode  value  of  'a'  i.e.  97
print(ord('z'))  # Unicode  value  of  'z'  i.e.  122
print(ord('0'))  # Unicode  value  of  '0'  i.e.  48
print(ord('9'))  # Unicode  value  of  '9'  i.e.  57
print(ord('$'))  # Unicode  value  of  '$'  i.e.  36
print(ord(' '))  # Unicode  value  of  ' '  i.e.  32

'''  Output
65
90
97
122
48
57
36
32
'''


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
Hint: Use  chr()  and  ord()  functions
'''

try:
    a=eval(input('Enter  any  string  with  alternate  character  and  digit : '))
    c=''
    for i in range(0,len(a),2):
        char=a[i]
        digit=int(a[i+1])
        c=c+char+chr(int(ord(char))+digit)
    print('Result : ',c)
except NameError:
    print('Input should be string with alternative character and digit')

'''  Sample output
Enter  any  string  with  alternate  character  and  digit : 'A4M3Z5D2'
Result :  AEMPZ_DF

Enter  any  string  with  alternate  character  and  digit : 'M3K2$5z2'
Result :  MPKM$)z|

Enter  any  string  with  alternate  character  and  digit : hyd
Input should be string with alternative character and digit

Enter  any  string  with  alternate  character  and  digit : 'A7B5C6Z8'
Result :  AHBGCIZb

'''
