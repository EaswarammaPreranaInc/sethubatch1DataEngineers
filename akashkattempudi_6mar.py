# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') 
print('day'   in   'Sankar  dayal  sarma') 
print('Green'   in   'Hyd  is  green  city')
print('d  is'   in   'Hyd  is  green  city') 
print('dis'   in   'Hyd  is  green  city') 
print('iniv'   in   'Srinivas') 
print('iniv'   not   in   'Srinivas')
'''
True
True
False
True
False
True
False
'''

'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) #String  from  indexes  0  to  6  in  steps  of  2  i.e. Rm a
print(a [ : 7]) #String  from  indexes  0  to  7  in  steps  of  1 i.e.  Rama Ra
print(a [2 : 4]) #String  from  indexes  2  to  3  in  steps  of  1  i.e.  ma
print(a [2 : ]) #String  from  indexes  2  to  7  in  steps  of  1  i.e.  ma Rao
print(a [ : 4 ]) #String  from  indexes  0  to  3  in  steps  of  1  i.e.  Rama
print(a [ : : 2])#String  from  indexes  0  to  7  in  steps  of  2  i.e.  Rm a
print(a [-6 : -1])#String  from  indexes  -6  to  -2  in  steps  of  1  i.e.  ma Ra
print(a [-6 : ]) #String  from  indexes  -6  to  7  in  steps  of  1  i.e.  ma Rao
print(a [: -4 : -1]) #String  from  indexes  2  to  7  in  steps  of  1  i.e.  ma Rao
print(a [-3 : -1])#String  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])#String  from  indexes  -3  to  7  in  steps  of  1  i.e. Rao
print(a [ : : ])#String  from  indexes  0  to  7  in  steps  of  1  i.e.  Rama Rao
print(a [ : ])#String  from  indexes  0  to  7  in  steps  of  1  i.e.  Rama Rao
print(a [ : : -1])#String  from  indexes  -1  to  -8  in  steps  of  -1  i.e.  oaR amaR
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])#String  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a mR
print(a [2 : 8])#String  from  indexes  2  to  7  in  steps  of  1  i.e. ma Rao
print(a [2 : 8 : -1]) #empty
print(a [ : -6 : -1])#String  from  indexes  -1  to  -5  in  steps  of  -1  i.e.  oaR a
print(a [2 : -3])#String  from  indexes  2  to  -4 in  steps  of  1  i.e.  ma
print(a [1 : 6 : 2])#String  from  indexes  1  to  5 in  steps  of  2  i.e.  aaR
print(a [ : -5 : -5])#String  from  indexes  -1  to  -4  in  steps  of  -5  i.e.  o
print(a [2 : -5])#String  from  indexes  2  to  -6  in  steps  of  1  i.e.  m
print(a [2 : -5 : 2])#String  from  indexes  2  to  -6  in  steps  of  2  i.e.  m
print(a [ : 0 : -1])#String  from  indexes  -1  to  1  in  steps  of  -1  i.e.  oaR ama
print(a [-5 : 0 : -2])#String  from  indexes  -1  to  -8  in  steps  of  -1  i.e.  aa


'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
try:
    a = eval(input("Enter 1st name : "))
    b = eval(input("Enter 2nd name : "))
    c = b[:2] + a[2:]
    d = a[:2] + b[2:]
    print(c,d,sep=" ")
except (ValueError,NameError):
 print("Each name should contain a minimum of two characters(or)Name must be in double quotes ")


'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
a = eval(input("Enter the name : "))
if len(a)>=4:
        print(a[:2]+a[-2:])
else:
    print("")
# Enter the name : "python"
# pyon

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
b = "AKASH"
# b = eval(input("Enter name : "))
for i in range(len(b)):
    print(F"Character at index {i} : {b[i]}")

print()
for i in range(len(b)):
    print(F"Character at index {-(i + 1)} : {b[-(i + 1)]}")

"""
Character at index 0 : A
Character at index 1 : K
Character at index 2 : A
Character at index 3 : S
Character at index 4 : H

Character at index -1 : H
Character at index -2 : S
Character at index -3 : A
Character at index -4 : K
Character at index -5 : A"""

'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  character  to  odd  object

3) Hint: Use  single  for  loop
'''
a= "Rama Rao"
even =""
odd=""
# a = eval(input("Enter name : "))
for i in range(len(a)):
    if i%2==0:
        even += a[i]
    else:
        odd+=a[i]
print("Even :",even)
print("Odd :",odd)

'''
Even : Rm a
Odd : aaRo
'''

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
a= "A4B3C2$5"
# a= eval(input("Enter any string with alternate character and digit : "))
out = ""
for i in range(0,len(a),2):
    out +=a[i]*int(a[i+1])
print(out)
'''
AAAABBBCC$$$$$
'''

