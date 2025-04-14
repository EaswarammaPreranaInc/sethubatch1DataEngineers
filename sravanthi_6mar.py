# Find outputs
print( 'green'   in   'Hyd  is  green  city') 
print('day'   in   'Sankar  dayal  sarma') 
print('Green'   in   'Hyd  is  green  city')
print('d  is'   in   'Hyd  is  green  city') 
print('dis'   in   'Hyd  is  green  city') 
print('iniv'   in   'Srinivas') 
print('iniv'   not   in   'Srinivas')
output:
True
True
False
True
False
True
False
# Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon
String1="Java"
String2="Python"
String1=input("Enter 1st String:")
String2=input("Enter 2nd String:")
result=String2[:2]+String1[2:]+" "+String1[:2]+String2[2:]
print(result)
output:
Enter 1st String:Java
Enter 2nd String:Python
Pyva Jathon
# Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
S=input("Enter a String:")
if len(S)<4:
	print("Nothing")
else:
   print(S[:2]+S[-2:])
output:
Enter a String:PYTHON
PYON

Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1
What  are  the  outputs ?  --->   Character  at  index  0  :  V
								                  Character  at  index  1  :  A
								                  Character  at  index  2  :  M
							                    Character  at  index  3  :  S
								                  Character  at  index  4  :  I
                                  Character  at  index  -1  :  I 
								                  Character  at  index  -2  :  S
								                  Character  at  index  -3  :  M
								                  Character  at  index  -4  :  A
								                  Character  at  index  -5  :  V
a=input("Enter a string:")
print("String in forward:")
for i in range(len(a)):
 print(f"character at index {i}:{a[i]}")
print("String in reverse:")
for i in range(len(a)):
 print(f"character at index {(-(i+1))}:{a[-(i+1)]}")
  output:
Enter a string:VAMSI
String in forward:
character at index 0:V
character at index 1:A
character at index 2:M
character at index 3:S
character at index 4:I
String in reverse:
character at index -1:I
character at index -2:S
character at index -3:M
character at index -4:A
character at index -5:V
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object
2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object
a=input("Enter a string:")
even=""
odd=""
for i in range(len(a)):
	if i%2==0:
		even+=a[i]
	else:
		odd+=a[i]
print("Even index characters:",even)
print("Odd index characters:",odd)
output:
Enter a string:Rama Rao
Even index characters: Rm a
Odd index characters: aaRo

Let  input  be    A   4   B   3   C   2   $   5
                          0   1    2   3   4   5   6   7


2) Iteration    i        a[i]       a[i + 1]          out
   -------------------------------------------------------------------------------------------------
                                                                 ''
            1         0        'A'          '4'             '' + 'A' * 4 = 'AAAA'
            2        2        'B'           '3'             'AAAA' + 'B' * 3  = 'AAAABBB'
            3        4        'C'           '2'             'AAAABBB' + 'C' * 2 = 'AAAABBBCC'
            4        6        '$'           '5'             'AAAABBBCC' + '$' * 5 = 'AAAABBBCC$$$$$'
----------------------------------------------------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  ---> a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
Let  input  be    A   4   B   3   C   2   $   5
                          0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  --->  'AAAA'
a=input("Enter a string:")
b=""
try:
 for i in range(0,len(a),2):
   b=b+a[i]*(int(a[i+1]))
   print(b)
except Valueerror:
 print("pls enter alternate char and digit")
output:
Enter a string:A4B3C2$5
AAAA
AAAABBB
AAAABBBCC
AAAABBBCC$$$$$


