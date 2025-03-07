
# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') #T
print('Green'   in   'Hyd  is  green  city')#F
print('d  is'   in   'Hyd  is  green  city') #T
print('dis'   in   'Hyd  is  green  city') #F
print('iniv'   in   'Srinivas') #T
print('iniv'   not   in   'Srinivas')#F

'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])#a[0:7:2] --> string from indexes 0 to 6 in steps of 2 --> Rm a
print(a [ : 7])# a[0:7:1] --> string from indexes 0 to 6 in steps of 1 --> Rama Ra
print(a [2 : 4])# a[2:4:1] --. string from indexes 2 to 3 in steps of 1 --> ma
print(a [2 : ])# a[2:8:1] --> string from indexes 2 to 7 in steps of 1--> ma Rao
print(a [ : 4 ])#a[0:4:1] --> string from indexes 0 to 3 in steps of 1 --> Rama
print(a [ : : 2])# a[0:8:2] --> string from indexes 0 to 7 in stteps of 2 --> Rm Ro
print(a [-6 : -1])# a[-6:-1:1] --. string from indexes -6 to 0 in steps of 1 --> Empty string
print(a [-6 : ])# a[-6:-9:1] --> string from indexes -6 to -10 in steps of 1 --> Empty String
print(a [: -4 : -1])# a[-1:-4:-1] --> string from indexes -1 to -3 in steps of -1  --> 0aR a
print(a [-3 : -1])# a[-3:-1: 1] --> string from indexes -3 to 0 in steps of 1 --> Rao
print(a [-3 : ])# a[-3:8:1] --> string from indexes -3 to 7 in steps of 1 -->Rao
print(a [ : : ])#a[0:8:1] --> string from indexes 0 to 7   in steps of 1   -->Rama Rao
print(a [ : ])#a[0:8:1] --> string from indexes 0 to 7   in steps of  1 -->Rama Rao
print(a [ : : -1])#a[-1:-9:-1] --> string from indexes -1 to  -8   in steps of -1  --> oaR amaR
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])#a[-2:-9:-2] --> string from indexes -2 to -8   in steps of  -2 --> a aa
print(a [2 : 8])#a[2:8:1] --> string from indexes  2 to 7  in steps of 1  --> ma Rao
print(a [2 : 8 : -1])# --> string from indexes  2 to 9  in steps of   --> ma Rao
print(a [ : -6 : -1])#a[-1:-6:-1] --> string from indexes -1 to -5   in steps of -1  --> oaR a
print(a [2 : -3])#a[2:-3:1] --> string from indexes  2 to -4  in steps of 1  --> ma(space)
print(a [1 : 6 : 2])#a[1:6:2] --> string from indexes 1 to 5    in steps of 2  --> aaRo
print(a [ : -5 : -5])#a[-1:-5:-5] --> string from indexes -1 to -5    in steps of -5  -->a
print(a [2 : -5])#a[2:-5:1] --> string from indexes 2 to -6   in steps of 1  --> m
print(a [2 : -5 : 2])# --> string from indexes  2 to -6  in steps of 2  --> Empty string
print(a [ : 0 : -1])#a[-1:0:-1 --> string from indexes -1 to  1   in steps of -1  -->oaR ama
print(a [-5 : 0 : -2])#--> string from indexes -5 to 1   in steps of  -2 --> a

'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice 
'''

a=input("enter 1st string: ")
b=input("enter 2nd string: ")
if(len(a)>=2 and len(b)>=2):
	c=b[:2]+a[2:]+' '+a[:2]+b[2:]
	print(c)
else:
	print("both strings should have atleast 2 characters")

'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing '''

a= input("enter a string: ")
if len(a)>=4:
	b=a[:2]+a[-2:]
	print(b)
else:
	print("")  
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

Hint:  Use  two  for  loops
'''

a=input('Enter a String: ')
for i in range(len(a)):
	print(f'Character at index {i} : {a[i]}')
for i in range(1,len(a)+1):
	print(f'Character at index {-i} : {a[-i]}')

'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop
'''

a=input('Enter a String: ')
even=''
odd=''
for i in range(len(a)):
	if i%2 ==0:
		even+=a[i]
	
	else:
		odd+=a[i]
print(even)
print(odd)

'''
Let  input  be    A   4   B   3   C   2   $   5
                          0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  --->  'AAAA'

2) Iteration         i        a[i]       a[i + 1]          out
   -------------------------------------------------------------------------------------------------
                                                                 ''
            1         0        'A'          '4'             '' + 'A' * 4 = 'AAAA'
            2        2        'B'           '3'             'AAAA' + 'B' * 3  = 'AAAABBB'
            3        4        'C'           '2'             'AAAABBB' + 'C' * 2 = 'AAAABBBCC'
            4        6        '$'           '5'             'AAAABBBCC' + '$' * 5 = 'AAAABBBCC$$$$$'
----------------------------------------------------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  ---> a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
'''

a=input("enter alternate character and number: ")
val=0
num=0
r=''
for i in range(0,len(a),2):
	val=a[i]
	if(i+1<len(a)):
		num=int(a[i+1])
		r+=val*num
	
print(r)
