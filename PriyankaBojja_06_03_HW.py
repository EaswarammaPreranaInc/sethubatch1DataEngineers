'''
# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')  #True
print('day'   in   'Sankar  dayal  sarma')     #True
print('Green'   in   'Hyd  is  green  city')   #False
print('d  is'   in   'Hyd  is  green  city')   #True
print('dis'   in   'Hyd  is  green  city')     #False
print('iniv'   in   'Srinivas')                #True
print('iniv'   not   in   'Srinivas')          #False
  

(Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1

a = 'Rama Rao'
print(a [ : 7 : 2])  #  a[0 : 7 : 2]  --->  String  from  indexes  0  to  6  in  steps  of  2  i.e.  Rm a
print(a [ : 7])      #  a[0 : 7 : 1]  --->  String  from  indexes  0  to  6  in  steps  of  1  i.e.  Rama Ra
print(a [2 : 4])     #  a[2 : 4 : 1]  --->  String  from  indexes  2  to  3  in  steps  of  1  i.e.  ma
print(a [2 : ])      #  a[2 : 8 : 1]  --->  String  from  indexes  2  to  7  in  steps  of  1  i.e.  ma Rao
print(a [ : 4 ])     #  a[0 : 4 : 1]  --->  String  from  indexes  0  to  3  in  steps  of  1  i.e.  Rama
print(a [ : : 2])    #  a[0 : 8 : 2]  --->  String  from  indexes  0  to  7  in  steps  of  2  i.e.  Rm a
print(a [-6 : -1])   #  a[-6 : -1 : 1]  --->  String  from  indexes  -6  to  -2  in  steps  of  1  i.e.  ma Ra
print(a [-6 : ])     #  a[-6 : 8 : 1]  --->  String  from  indexes  -6  to  7  in  steps  of  1  i.e.  ma Rao
print(a [: -4 : -1]) #  a[-1 : -4 : -1]  --->  String  from  indexes  -1  to  -3  in  steps  of  -1  i.e.  oaR
print(a [-3 : -1])   #  a[-3 : -1 : 1]  --->  String  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])     #  a[-3 : 8 : 1]  --->  String  from  indexes  -3  to  7  in  steps  of  1  i.e.  Rao
print(a [ : : ])     #  a[0 : 8 : 1]  --->  String  from  indexes  0  to  7  in  steps  of  1  i.e.  Rama Rao
print(a [ : ])       #  a[0 : 8 : 1]  --->  String  from  indexes  0  to  7  in  steps  of  1  i.e.  Rama Rao
print(a [ : : -1])   #  a[-1 : -9 : -1]  --->  String  from  indexes  -1  to  -8  in  steps  of  -1  i.e.  oaR amaR
print(a [ : : -2])   #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])#  a[-2 : -9 : -2]  --->  String  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a mR
print(a [2 : 8])     #  a[2 : 8 : 1]  --->  String  from  indexes  2  to  7  in  steps  of  1  i.e.  ma Rao
print(a [2 : 8 : -1])#  a[2 : 8 : -1]  --->  empty string
print(a [ : -6 : -1])#  a[-1 : -6 : -1]  --->  String  from  indexes  -1  to  -5  in  steps  of  -1  i.e.  oaR a
print(a [2 : -3])    #  a[2 : -3 : 1]  --->  String  from  indexes  2  to  -4  in  steps  of  1  i.e.  ma 
print(a [1 : 6 : 2]) #  a[1 : 6 : 2]  --->  String  from  indexes  1  to  5  in  steps  of  2  i.e.  aa R
print(a [ : -5 : -5])#  a[-1 : -5 : -5]  --->  String  from  indexes  1  to  -4  in  steps  of  -5  i.e.  o
print(a [2 : -5])    #  a[2 : -5 : 1]  --->  String  from  indexes  2  to  -6  in  steps  of  1  i.e.  m
print(a [2 : -5 : 2])#  a[2 : -5 : 2]  --->  String  from  indexes  2  to  -6  in  steps  of  2  i.e.  m
print(a [ : 0 : -1]) #  a[-1 : 0 : -1]  --->  String  from  indexes  -1  to  1  in  steps  of  -1  i.e.  oaR ama
print(a [-5 : 0 : -2])#  a[-5 : 0 : -2]  --->  String  from  indexes  -5  to  1  in  steps  of  -2  i.e. aa

Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice

a=input('Enter 1st string: ')
b=input('Enter 2nd string: ')
c=b[0:2]+a[2:]
d=a[0:2]+b[2:]
print('Result: ',c+ ' ' +d)

OP-Enter 1st string: HERO
Enter 2nd string: VILLAN
Result:  VIRO  HELLAN

Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing


a=input('Enter any string: ')
b=a[0:2]
c=a[len(a)-2:]
if len(a)<4:
	print('')
else:
	print('Result :',b+c)

OP-
Enter  any  string : PYTHON
Result :  PYON



Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     		 0      1     2     3     4
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

Hint:  Use  two  for  loops

a=input('Enter any string: ')
print('String in forward')
for i in range(len(a)):
	print(f'Character at index {i} : {a[i]}')
print('String in reverse')
for i in range(len(a)):
	print(f'Character at index {-(i+1)} : {a[-(i+1)]}')

OP-
Enter any string: HELLO
String in forward
Character at index 0 : H
Character at index 1 : E
Character at index 2 : L
Character at index 3 : L
Character at index 4 : O
String in reverse
Character at index -1 : O
Character at index -2 : L
Character at index -3 : L
Character at index -4 : E
Character at index -5 : H



Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop


Enter  any  string  :  Rama Rao
Characters  at  even  indexes  :   Rm a
Characters  at  odd  indexes  :   aaRo



a=input('Enter any string: ')
odd=""
even=""
for x in range(len(a)):
	if x%2==0:
		even=even+a[x]
	else:
		odd=odd+a[x]
print('Characters at even indexes : ',even)
print('Characters at odd indexes : ',odd)

OP-Enter any string: PRIYANKA
Characters at even indexes :  PIAK
Characters at odd indexes :  RYNA



Let  input  be    A   4   B   3   C   2   $   5
                          0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  --->  'AAAA'

2) Iteration    i        a[i]       a[i + 1]          out
   -------------------------------------------------------------------------------------------------
                                                                 ''
		1        0        'A'          '4'             '' + 'A' * 4 = 'AAAA'
		2        2        'B'           '3'             'AAAA' + 'B' * 3  = 'AAAABBB'
		3        4        'C'           '2'             'AAAABBB' + 'C' * 2 = 'AAAABBBCC'
		4        6        '$'           '5'             'AAAABBBCC' + '$' * 5 = 'AAAABBBCC$$$$$'
----------------------------------------------------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  ---> a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
Enter  any  string  with  alternate  character  and  digit :  $5P2K3Z4
Result :   $$$$$PPKKKZZZZ

Enter  any  string  with  alternate  character  and  digit :  hyd
Pls  enter  alternate  char  and  digit

try:
	a=input('Enter  any  string  with  alternate  character  and  digit : ')
	y=""
	for i in range(len(a)):
		if i%2==0:
			y=y+(a[i]*int(a[i+1]))
	print('Result : ',y)
except (ValueError,IndexError):
	print('Please enter alternate Char and digit')

OP-
Enter  any  string  with  alternate  character  and  digit : P2C4$5
Result :  PPCCCC$$$$$

Enter  any  string  with  alternate  character  and  digit : 2s5f
Please enter alternate Char and digit
'''