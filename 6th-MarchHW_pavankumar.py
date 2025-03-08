#_PROGRAM_1
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters
Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon
Hint:  Use  slice

CODE:
a=input("Enter the first input : ")
b=input("Enter the second input : ")
print(b[0:2]+a[2:],a[0:2]+b[2:])

OUTPUT:
Enter the first input : Python
Enter the second input : Java
Jathon Pyva

#_PROGRAM_2
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters
1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON
2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
    
CODE:
a=input("enter the input : ")
if len(a)<4:
    print("nothing")
else:
    print(a[0:2]+a[len(a)-2:len(a)])

OUTPUT:
enter the input : PYTHON
PYON
enter the input : PYT
nothing

#_PROGRAM_3
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

Hint:  Use  two  for  loops

CODE:
a=input("enter the string:")
for i in range(0,len(a)):
	print(F'Character at index {i} : {a[i]}')
for i in range(-1,-len(a)-1,-1):
	print(F'Character at index {i} : {a[i]}')

OUTPUT:
enter the string:vamsi
Character at index 0 : v
Character at index 1 : a
Character at index 2 : m
Character at index 3 : s
Character at index 4 : i
Character at index -1 : i
Character at index -2 : s
Character at index -3 : m
Character at index -4 : a
Character at index -5 : v

#_PRPGRAM_4
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop

CODE:
a=input("Enter the input : ")
even=""
odd=""
for i in range(0,len(a)):
	if(i%2==0):
		even=even+a[i]
	else:
		odd=odd+a[i]
print("Characters at even index : ",even)
print("Characters at odd index : ",odd)

OUTPUT:
Enter the input : Rama Rao
Characters at even index :  Rm a
Characters at odd index :  aaRo

#PROGRAM_5
Let  input  be    A   4   B   3   C   2   $   5
                          0   1    2   3   4   5   6   7

What  is  the  output ?  --->   $5P2K3Z4

CODE:
a=input("Enter  any  string  with  alternate  character  and  digit : ")
try:
	for i in range(0,len(a),2):
		print(a[i]*int(a[i+1]),end="")
except:
	print("Pls enter alternate char and digit")

OUTPUT:
Enter  any  string  with  alternate  character  and  digit : $5P2K3Z4
$$$$$PPKKKZZZZPress any key to continue . . .

#PROGRAM_6
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1
'''
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
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
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
print(a [-5 : 0 : -2])

CODE:
a='Rama Rao'
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
print(a[-5:0:-2])
OUTPUT:
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





