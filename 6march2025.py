# Find outputs  (Home  work)
"""
print( 'green'   in   'Hyd  is  green  city') #true
print('day'   in   'Sankar  dayal  sarma') #true
print('Green'   in   'Hyd  is  green  city')#false
print('d  is'   in   'Hyd  is  green  city') #true
print('dis'   in   'Hyd  is  green  city') #false
print('iniv'   in   'Srinivas') #true
print('iniv'   not   in   'Srinivas')#false

"""
'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1

a = 'Rama Rao'
print(a [ : 7 : 2])#a from 0 to 7 in steps of 2 = rm a
print(a [ : 7])# a from 0 to 7 in steps of 1 =rama ra
print(a [2 : 4])# a from 2 to 4 in steps of 1 = ma
print(a [2 : ])# a from 2 to 7 in steps of 1 = ma rao
print(a [ : 4 ])# a from 0 to 4 in steps of 1 = rama
print(a [ : : 2])# a from 0 to 7 in steps of 2 = rm a
print(a [-6 : -1])# a from -6 to -1 in steps of 1 = ma ra
print(a [-6 : ])# -6 to -1 step of 1=ma rao
print(a [: -4 : -1])# -1 to -4 in steps -1 = 0ar 
print(a [-3 : -1])# -3 to -1 steps 1 = ra
print(a [-3 : ])# -3 to -1 steps 1 = ra0
print(a [ : : ])# 0 to 7 steps 1 = rama rao
print(a [ : ])# 0 to 7 steps 1 = rama rao
print(a [ : : -1])# 1 to 7 steps of -1 = oar amar
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])# -2 to 1 steps -2 = a mr
print(a [2 : 8])# 2 to 8 steps 1 = ma rao
print(a [2 : 8 : -1])# empty
print(a [ : -6 : -1])# -1 to -6 steps -1 = oar a
print(a [2 : -3]) # 2 to -3 steps 1 = ma 
print(a [1 : 6 : 2])# 1 to 5 steps 2 = aar
print(a [ : -5 : -5])# -1 to -5 steps -5 = o
print(a [2 : -5])# 2 to -5 steps 1 = m
print(a [2 : -5 : 2])# 2 to -5 steps of  2 = m
print(a [ : 0 : -1])# -1 to 1 steps -1 = oar ama
print(a [-5 : 0 : -2])# -5 to 0 steps -2 = aa
'''


#Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
'''
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice

a=(input("enter python : "))
b=(input("enter java : "))
print(a,b)
print(str(a[:2]+b[2:]))
print(str(b[:2]+a[2:]))
'''

# Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
'''
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing

a=input("enter the value : ")
if len(a)>=4:
    print(a[:2]+a[-2]+a[-1])
else:
    print("nothing")
'''

# Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice
'''
       	     				  0     1     2     3     4
Let  input  be		          V     A     M     S     I
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

a=input("enter the value of sting : ")
for i in range (0,len(a)):
    print(f"character at index {i} : {a[i]}")
print()
for j in range (-1,-len(a)-1,-1):
    print(f"character at index {j} : {a[j]}")

'''

# Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
'''
					 0      1      2      3     4       5     6      7
Let  input  be       R      a      m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop



a=input("enter the value : ")
c=b=""
for i in range(0,len(a)):
    if  i%2==0:
        c+=a[i]
        #c.append(a[i])
    else:
        b+=a[i]
        #b.append(a[i])
print("even =",c)
print("odd =",b)

'''

'''
Let  input  be    A   4   B   3   C   2   $   5
                          0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  --->  'AAAA'

2)   Iteration       i        a[i]       a[i + 1]           out
   -------------------------------------------------------------------------------------------------
                                                                 ''
            1        0        'A'           '4'             '' + 'A' * 4 = 'AAAA'
            2        2        'B'           '3'             'AAAA' + 'B' * 3  = 'AAAABBB'
            3        4        'C'           '2'             'AAAABBB' + 'C' * 2 = 'AAAABBBCC'
            4        6        '$'           '5'             'AAAABBBCC' + '$' * 5 = 'AAAABBBCC$$$$$'
----------------------------------------------------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  ---> a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string

'''
'''
try:
    a=input("enter the str and value first character  and next  integer  : ")
    c=''
    for i in range(0,len(a),2):
        c+=(a[i]*eval(a[i+1]))
    print(c)
except:
    print("Pls  enter  alternate  char  and  digit")
'''




    