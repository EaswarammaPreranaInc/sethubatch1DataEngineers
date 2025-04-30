
'''Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI

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
	print('Enter a string')'''


'''Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
    What  is  the  output ? --->  RAM<space>O

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
	print('please enter a string')'''


# len()  function  demo  program  (Home  work)
'''print(len('Hyd'))  #  3
print(len('Rama Rao'))
print(len('9247'))
print(len('+-$'))
print(len(''))
print(len(' '))
print(len('A2#'))
#print(len(3456))
#print('Sec'. len())'''


# chr()  function  demo  program
'''print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90))
print(chr(97))
print(chr(122))
print(chr(48))
print(chr(57))
print(chr(36))
print(chr(32))'''


# ord()  function  demo  program
'''print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))
print(ord('a'))
print(ord('z'))
print(ord('0'))
print(ord('9'))
print(ord('$'))
print(ord(' '))'''


'''Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2


try:
	a = eval(input('Enter  any  string  with  alternate  character  and  digit: '))
	out = ''
	for i in range(0,len(a),2):
		out = out + a[i]+chr(ord(a[i])+eval(a[i+1]))
	print(out)
except (NameError,IndexError):
	print('please enter a string  with  alternate  character  and  digit: ')
except TypeError:
	print('please enter a string with in single quotes')'''






