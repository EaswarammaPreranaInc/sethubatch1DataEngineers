#1st PROGRAM
'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
CODE:
a=input("enter first input:")
b=input("enter second input:")
print(a[0:2]+b[2:6])
print(b[0:2]+a[2:4])

OUTPUT:
enter first input:Java
enter second input:Python
Jathon
Pyva


#2nd PROGRAM
'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
CODE:
str=input("enter first input:")
if len(str)<4:
		print("Nothing")
else:
		print(str[:2]+str[-2:])

OUTPUT:
enter first input:PYTHON
PYON
enter first input:hyd
Nothing


#3rd PROGRAM
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
CODE:
a = input("Enter string: ")
for i in range(len(a)):  
    print(f"Character at index {i} : {a[i]}")
print()
for i in range(-1, -len(a) - 1, -1):  
    print(f"Character at index {i} : {a[i]}")

OUTPUT:
Enter string: VAMSI
Character at index 0 : V
Character at index 1 : A
Character at index 2 : M
Character at index 3 : S
Character at index 4 : I

Character at index -1 : I
Character at index -2 : S
Character at index -3 : M
Character at index -4 : A
Character at index -5 : V


#4th PROGRAM
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
CODE:
a = input("Enter string: ")
even = ""  
odd = ""  
for i in range(len(a)):  
    if i % 2 == 0:  
        even += a[i]
    else:  
        odd += a[i]
print("Even index characters:", even)
print("Odd index characters:", odd)

OUTPUT:
Enter string: Rama Rao
Even index characters: Rm a
Odd index characters: aaRo


#5th PROGRAM
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
CODE:
try:
   a=input("enter string:")
   for i in range(0,len(a),2):
	      print(a[i]*int(a[i+1]),end='')
   print()
except:
	print("Pls  enter  alternate  char  and  digit")

OUTPUT:
enter string:A4B3C2$5
AAAABBBCC$$$$$

#6th PROGRAM
# Find outputs  
print( 'green'   in   'Hyd  is  green  city') 
print('day'   in   'Sankar  dayal  sarma') 
print('Green'   in   'Hyd  is  green  city')
print('d  is'   in   'Hyd  is  green  city') 
print('dis'   in   'Hyd  is  green  city') 
print('iniv'   in   'Srinivas') 
print('iniv'   not   in   'Srinivas')

OUTPUTS:
True
True
False
True
False
True
False

#7th PROGRAM
'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1
'''
CODE:
a = 'Rama Rao'
print(a [ : 7 : 2])
print(a [ : 7])
print(a [2 : 4])
print(a [2 : ])
print(a [ : 4 ])
print(a [ : : 2])
print(a [-6 : -1])
print(a [-6 : ])
print(a [: -4 : -1])
print(a [-3 : -1])
print(a [-3 : ])
print(a [ : : ])
print(a [ : ])
print(a [ : : -1])
print(a [ : : -2]) 
print(a [ -2 : : -2])
print(a [2 : 8])
print(a [2 : 8 : -1])
print(a [ : -6 : -1])
print(a [2 : -3])
print(a [1 : 6 : 2])
print(a [ : -5 : -5])
print(a [2 : -5])
print(a [2 : -5 : 2])
print(a [ : 0 : -1])
print(a [-5 : 0 : -2])

OUTPUTS:
Rm a
Rama Ra
ma
ma Rao
Rama
Rm a
ma Ra
ma Rao
oaR
Ra
Rao
Rama Rao
Rama Rao
oaR amaR
oRaa
a mR
ma Rao

oaR a
ma
aaR
o
m
m
oaR ama
aa
