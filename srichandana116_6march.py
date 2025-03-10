## Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') #True
print('day'   in   'Sankar  dayal  sarma') #True
print('Green'   in   'Hyd  is  green  city') #False
print('d  is'   in   'Hyd  is  green  city') #True
print('dis'   in   'Hyd  is  green  city') #False
print('iniv'   in   'Srinivas') #True
print('iniv'   not   in   'Srinivas')  #False
'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) #Rm a
print(a [ : 7]) # Rama Ra
print(a [2 : 4]) #ma
print(a [2 : ]) #ma Rao
print(a [ : 4 ]) #Rama
print(a [ : : 2]) #Rm a
print(a [-6 : -1]) #ma Ra
print(a [-6 : ]) #ma Rao
print(a [: -4 : -1])#oaR
print(a [-3 : -1]) #Ra
print(a [-3 : ]) #Rao
print(a [ : : ])#Rama Rao
print(a [ : ]) #Rama Rao
print(a [ : : -1]) #oaR amaR
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) #a mR
print(a [2 : 8]) #ma Rao
print(a [2 : 8 : -1]) #doesnt work as 2<8 in steps of -
print(a [ : -6 : -1]) #oaR a
print(a [2 : -3])#ma 
print(a [1 : 6 : 2]) #aaR
print(a [ : -5 : -5]) #o
print(a [2 : -5]) #m
print(a [2 : -5 : 2]) #m
print(a [ : 0 : -1])#oaR ama
print(a [-5 : 0 : -2])#aa
#Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
'''Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon'''
try:
    a=input("enter 1st string:")
    b=input("enter 2nd string:")
    if len(a)>=2 and len(b)>=2:
        y=a[:2]+b[2:]
        x=b[:2]+a[2:]
        print(x,' ',y)
    else:
        print("each  string should contain  a   minimum  of  two  characters")
except:
    print("some error")
#Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
#Print  an  empty  string  if  string  contains  less  than  four  characters
try:
    a=input("enter 1st string:")
    if len(a)>=4:
        print(a[:2]+a[-2:])
    else:
        print("Nothing")
except:
    print("some error")
#Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice
try:
    a=input("enter 1st string:")
    print("str")
    for i in a:
        print(i,end="")
    print("\nrev str")
    for i in range(-1,(-len(a)-1),-1) :
        print(a[i],end="")
except:
    print("some error")
##Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
try:
    a=input("enter 1st string:")
    eve=''
    od=''
    for i in range(0,len(a),2):
        eve=eve+a[i]
        od=od+a[i+1]
    print("even",eve)
    print("odd",od)
except:
    print("some error")
#print number of character*digit for any  string  with  alternate  character  and  digit
try:
    d=""
    a=input("Enter  any  string  with  alternate  character  and  digit :")
    for i in range(0,len(a),2):
        d=d+a[i]*int(a[i+1])
    print(d)
except:
    print("some error")
