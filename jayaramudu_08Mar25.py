Ex-1:- 
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
	a = eval(input('Enter first string : '))
	b = eval(input('Enter second string : '))
	out , l = '' , 0
	while l < len(a) and l < len(b):
		out = out + a[l] + b[l]
		l += 1
	if len(a) > len(b):
		out = out + a[l:]
	elif len(a) < len(b):
		out = out + b[l:]
	print('Result : ',out)
except TypeError:
	print('Enter a string')

Ex-2 :-
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

try:
	a = eval(input('Enter any string : '))
	out = ''
	for x in a:
		if x not in out:
			out += x
	print('String without duplicates : ',out)
except NameError:
	print('Please Enter a string in quotes')
except TypeError:
	print('please enter astring')

Ex-3:-
print(len('Hyd'))  #  3
print(len('Rama Rao'))  # 8
print(len('9247')) # 4
print(len('+-$'))  # 3
print(len('')) # 0
print(len(' ')) #1
print(len('A2#'))  #3
print(len(3456))  # Error 3456 is not a sequence
print('Sec'. len()) # Error string does not have str.len() method

Ex-4 :-
# chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90)) # Z
print(chr(97)) # a
print(chr(122)) # z
print(chr(48)) # 0
print(chr(57)) #9
print(chr(36)) # $
print(chr(32)) # space

Ex-5 :-
# ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z')) # 90
print(ord('a')) # 97
print(ord('z')) # 122
print(ord('0')) # 48
print(ord('9')) # 57
print(ord('$')) # 36
print(ord(' ')) # 32

Ex-6 :-
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
Hint: Use  chr()  and  ord()functions
'''

try:
	a = eval(input('Enter  any  string  with  alternate  character  and  digit: '))
	out = ''
	for i in range(0,len(a),2):
		out = out + a[i]+chr(ord(a[i])+eval(a[i+1]))
	print(out)
except (NameError,IndexError):
	print('please enter a string  with  alternate  character  and  digit: ')
except TypeError:
	print('please enter a string with in single quotes')







