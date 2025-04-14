Ex-1:
'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:Use  slice
'''
a = 'java'
b =  'python'
e = b[:2]+a[2:]
f = a[:2] +b[2:]
print(e+' '+f)

Ex-2:
'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->Nothing
'''
try:
	a = eval(input("Enter a 4 characters string : "))
	if 4 <= len(a):
		b = a[:2]
		c = a[-2:]
		d = b + c
		print(d)
	else:
		print('Please enter a four characters of a String')
except NameError:
	print('Please enter a String in single quotes')
except TypeError:
	print('Please enter a String')

Ex-3 : 
'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
								                  Character  at  index  1  :  A
								                  Character  at  index  2  :  M
							                      Character  at  index  3  :  S
								                  Character  at  index  4  :  I

								                  Character  at  index  -1  :  I
								                  Character  at  index  -2  :  S
								                  Character  at  index  -3  :  M
								                  Character  at  index  -4  :  A
								                  Character  at  index  -5  :  V

Hint:  Use  two for loops
'''
try:
	a = eval(input("Enter a  string : "))
	for i in range(len(a)):
		print(F'Character  at  index  {i} : {a[i]}')

	print()
	for i in range(len(a)):
		print(F'Character  at  index  {-i} : {a[-i]}')
except TypeError:
	print('please enter a string')

Ex-4:
'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for loop
'''

try:
	a = eval(input("Enter any  string : "))
	even = odd = ''
	for i in range(len(a)):
		if i % 2 == 0:
			even += a[i]
		else:
			odd += a[i]
	print('Characters  at  even  indexes  : ',even)
	print('Characters  at  odd  indexes  : ',odd)
except TypeError:
	print('Please enter a string')

Ex-5 :
'''
Let  input  be    A   4   B   3   C   2   $   5
                          0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  --->  'AAAA'

2) Iteration    i        a[i]       a[i + 1]          out
   -------------------------------------------------------------------------------------------------
                                                                 ''
            1         0        'A'          '4'             '' + 'A' * 4 = 'AAAA'
            2        2        'B'           '3'             'AAAA' + 'B' * 3  = 'AAAABBB'
            3        4        'C'           '2'             'AAAABBB' + 'C' * 2 = 'AAAABBBCC'
            4        6        '$'           '5'             'AAAABBBCC' + '$' * 5 = 'AAAABBBCC$$$$$'
----------------------------------------------------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  ---> a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
'''
try:
	a = eval(input("Enter  any  string  with  alternate  character  and  digit :  "))
	b = ''
	for i in range(0,len(a),2):
		b = b + a[i] * eval(a[i+1])
	print(b)
except NameError:
	print('Please enter a alternate  character  and  digit')
except TypeError:
	print('Please enter a alternate  character  and  digit')
