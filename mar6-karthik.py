'''
Write  a  program  to  concatenate  two  strings  separated  by  space
but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
#program
str1="Java"
str2="Python"
str3=str2[:2]+str1[2:]+" "+str1[:2]+str2[2:]
print(str3)
----------------------------------------------------------------------------------------
Write  a  program  to  print  first  two  and  
the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
#program
a=input("Enter a string:\t")
if len(a)>=4:
	b=a[:2]+a[len(a)-2]+a[len(a)-1]
	print(b)
else:
	print("Nothing")
----------------------------------------------------------------------------------------
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
#program
a=input("Enter a string\t")
print("string  in  forward")
for i in range(len(a)):
	print(f"Character at index {i} is: {a[i]}")
print("string  in  reverse")
for j in range(1,len(a)+1):
    print(f"Character at index -{j} is: {a[-j]}")
----------------------------------------------------------------------------------------
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

#program
a=input("Enter a string: ")
even=""
odd=""
for i in range(len(a)):
	if i%2==0:
		even=even+a[i]
	else:
		odd=odd+a[i]
print(f"Even={even}")
print(f"Odd={odd}")
----------------------------------------------------------------------------------------

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
#program
input_string = "A4B3C2"
output = ""

for i in range(0, len(input_string), 2):
    char = input_string[i]       
    num = int(input_string[i+1])
    output += char * num  
print(output)
