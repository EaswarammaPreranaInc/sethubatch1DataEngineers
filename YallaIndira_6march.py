#program1:Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5      -4         -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])  #  a[0 : 7 : 2]  --->  String  from  indexes  0  to  6  in  steps  of  2  i.e. Rm a 
print(a [ : 7])      #  a[0 : 7 : 1]  --->  String  from  indexes  0  to  6  in  steps  of  1  i.e.  Rama Ra
print(a [2 : 4])     #  a[2 : 4 : 1]  --->  String  from  indexes  2  to  3  in  steps  of  1  i.e.  ma
print(a [2 : ])      #  a[2 : 8 : 1]  --->  String  from  indexes  2  to  7  in  steps  of  1  i.e.  ma Rao
print(a [ : 4 ])     #  a[0 : 4 : 1]  --->  String  from  indexes  0  to  3  in  steps  of  1 i.e.  Rama
print(a [ : : 2])    #  a[0 : 8 : 2]  --->  String  from  indexes  0  to  7  in  steps  of  2  i.e.  Rm a
print(a [-6 : -1])   #  a[-6 : -1 : 1]  --->  String  from  indexes  -6  to  -2  in  steps  of  1  i.e.  ma Ra
print(a [-6 : ])     #  a[-6 : 8 : 1]  --->  String  from  indexes  -6  to  7  in  steps  of  1  i.e.  ma Rao
print(a [: -4 : -1]) #  a[-1 : -4 : -1]  --->  String  from  indexes  -1  to  -3  in  steps  of  -1 i.e.  oaR
print(a [-3 : -1])   #  a[-3 : -1 : 1]  --->  String  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])     #  a[-3 : 8 : 1]  --->  String  from  indexes  -3  to  7  in  steps  of  1  i.e.  Rao
print(a [ : : ])     #  a[0 : 8 : 1]  --->  String  from  indexes  0  to  7  in  steps  of  1  i.e.  Rama Rao
print(a [ : ])       #  a[0 : 8 : 1]  --->  String  from  indexes  0  to  7  in  steps  of  1  i.e.  Rama Rao
print(a [ : : -1])   #  a[-1 : -9 : -1]  --->  String  from  indexes  -1  to  -8  in  steps  of  -1  i.e.  oaR amaR
print(a [ : : -2])   #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])#  a[-2 : -9 : -2]  --->  String  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a mR
print(a [2 : 8])     #  a[2 : 8 : 1]  --->  String  from  indexes  2  to  7  in  steps  of  1 i.e.  ma Rao
print(a [2 : 8 : -1]) #  a[2 : 8 : -1]  --->  String  from  indexes  2  to  7  in  steps  of  -1  i.e. empty
print(a [ : -6 : -1])  #  a[-1 : -6 : -1]  --->  String  from  indexes  -1  to  -5  in  steps  of  -1  i.e.  oaR a
print(a [2 : -3])      #  a[2 : -3 : 1]  --->  String  from  indexes  2  to  -4  in  steps  of  1  i.e.  ma
print(a [1 : 6 : 2])   #  a[1 : 6 : 2]  --->  String  from  indexes  1  to  5  in  steps  of  2  i.e.  aaR
print(a [ : -5 : -5])  #  a[-1 : -5 : -5]  --->  String  from  indexes  -1  to  -4  in  steps  of  -5  i.e. o
print(a [2 : -5])      #  a[2 : -5 : 1]  --->  String  from  indexes  2  to  -6  in  steps  of  1  i.e.  m
print(a [2 : -5 : 2])  #  a[2 : -5 : 2]  --->  String  from  indexes  2  to  -6  in  steps  of  2  i.e.  m
print(a [ -1: 0 : -1])   #  a[-1 : 0 : -1]  --->  String  from  indexes  -1  to  1  in  steps  of  -1  i.e.  oaR ama
print(a [-5 : 0 : -2]) #  a[-5 : 0 : -2]  --->  String  from  indexes  -5  to  1  in  steps  of  -2  i.e. aa

#program2:
print( 'green'   in   'Hyd  is  green  city')   #True
print('day'   in   'Sankar  dayal  sarma')      #True
print('Green'   in   'Hyd  is  green  city')    #False
print('d  is'   in   'Hyd  is  green  city')    #True
print('dis'   in   'Hyd  is  green  city')      #False
print('iniv'   in   'Srinivas')                 #True
print('iniv'   not   in   'Srinivas')           #False

#program3:Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
a=input("Enter first string : ")
b=input("Enter second string : ")
c=a[0:2]
d=a[2:]
e=b[0:2]
f=b[2:]
print('Result : ',e+d,c+f)

outputs:Enter first string : Rani
Enter second string : Indu
Result :  Inni Radu

#program4:Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing

a=input('Enter string : ')
b=a[0:2]
length=len(a)
c=a[length-2:length]
if length<4:
	print()
else:
  print("Result : ",b+c)

outputs:
Enter string : Devakarani
Result :  Deni

#program5:Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice
a=input("Enter the string : ")
print('String in forward')
for i in range(len(a)):
	print(f'Character at index {i} : {a[i]}')
print('String in reverse')
for i in range(-1,-len(a)-1,-1):
	print(f'Character at index {i} : {a[i]}')

 outputs:Enter the string : Teja
String in forward
Character at index 0 : T
Character at index 1 : e
Character at index 2 : j
Character at index 3 : a
String in reverse
Character at index -1 : a
Character at index -2 : j
Character at index -3 : e
Character at index -4 : T

#program6:Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object

a=input("Enter any String : ")
length=len(a)
even=''
odd=''
for i in range(length):
	if i%2==0:
		even=even+a[i]
	else:
		odd=odd+a[i]
print(f'Characters at even indexes : {even}')
print(f'Characters at odd indexes : {odd}')

outputs:Enter any String : devikarani
Characters at even indexes : dvkrn
Characters at odd indexes : eiaai

#program7:Let  input  be    A   4   B   3   C   2   $   5
                            0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$
try:
	a=input("Enter any string alternate character and digits : ")
	b=''
	for i in range(0,len(a),2):
		c=a[i]*int(a[i+1])
		b=b+c
	print('Result : ',b)
except:
	print("Please enter alternate char and digits")

 Enter any string alternate character and digits : A4B3C2$5
Result :  AAAABBBCC$$$$$
