'''6/3/2025 
#1.
a = 'Rama Rao'
print(a [ : 7 : 2]) #[0:7:2] Rm a
print(a [ : 7]) #[0:7:1] Rama Ra
print(a [2 : 4]) #[2:4:1] ma
print(a [2 : ]) #[2:len(a):1] ma Rao 
print(a [ : 4 ]) #[0:4:1] Rama 
print(a [ : : 2]) #[0:len(a):2] Rm a 
print(a [-6 : -1]) #[-6:-1:1] ma Ra
print(a [-6 : ]) # [-6:len(a):1] ma Rao 
print(a [: -4 : -1]) #[-1:-4:-1] oaR
print(a [-3 : -1]) # [-3:-1:1] Ra
print(a [-3 : ]) # [-3: len(a) :1] Rao 
print(a [ : : ]) #[0:len(a):1] Rama Rao
print(a [ : ]) #[0:len(a):1] Rama Rao
print(a [ : : -1]) #[-1:-len(a)-1:-1] oaR amaR
print(a [ : : -2]) #  a[-1 : -len(a)-1 : -2] oRaa
print(a [ -2 : : -2]) #[-2: -len(a)-1:-2] a m R
print(a [2 : 8]) #[2:8:1] ma Rao
print(a [2 : 8 : -1]) #[2:8:-1] # empty string 
print(a [ : -6 : -1]) #[-1:-6:-1] oaR a
print(a [2 : -3]) #[2:-3:1] ma<s>
print(a [1 : 6 : 2]) #[1:6:2] aaR
print(a [ : -5 : -5]) #[-1:-5:-5] o
print(a [2 : -5]) #[2:-5:1] #m
print(a [2 : -5 : 2]) #[2:-5:2] #m
print(a [ : 0 : -1]) #[-1:0:-1] #oaR ama
print(a [-5 : 0 : -2]) #[-5:0:-2] #aa

'''


'''
2.Write  a  program  to  concatenate  two  strings  separated  by  space  
but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Enter first string: JAVA
Enter second string: PYTHON
Result  :   PYVA JATHON
'''

'''
a=input("Enter first string:")
b=input("Enter second string:")


if(len(a)<2 or len(b)<2):
    print("Not possible")
    
else:
    print(F"Result: {b[0:2]+a[2:]+" "+a[0:2]+b[2:]}")
    
'''

'''
3.Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''

'''
s=input("Enter any string:")
if(len(s)<4):
    print("Nothing")
    
else:
    print(s[0:2]+s[-2::1])
    
'''

'''
4.Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

Enter the string: VAMSI
String in forward:
Character at index 0: V
Character at index 1: A
Character at index 2: M
Character at index 3: S
Character at index 4: I
String in reverse:
Character at index -1: I
Character at index -2: S
Character at index -3: M
Character at index -4: A
Character at index -5: V

'''

'''
s=input("Enter the string:")

print("String in forward:")
for i in range(len(s)):
    print(F"Character at index {i}: {s[i]}")
    
print("String in reverse:")
for i in range(-1,-len(s)-1,-1):
    print(F"Character at index {i}: {s[i]}")
    
'''

'''
5.Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

Enter  any  string  :  Rama Rao
Characters  at  even  indexes  :   Rm a
Characters  at  odd  indexes  :   aaRo
'''

'''
s=input("Enter  any  string  :")
o=e=''
for i in range(len(s)):
    if(i%2==0):
        e+=s[i]
        
    else:
        o+=s[i]
        
print("Characters  at  even  indexes  :",e)
print("Characters  at  odd   indexes  :",o)

'''
    
    
'''
6.

Enter  any  string  with  alternate  character  and  digit :  $5P2K3Z4
Result :   $$$$$PPKKKZZZZ
    
Enter  any  string  with  alternate  character  and  digit :  hyd
Pls  enter  alternate  char  and  digit

'''

'''
s=input("Enter  any  string  with  alternate  character  and  digit :") 
S=''
if(len(s)%2==0):
    for i in range(1,len(s),2):
        if(type(s[i])!=type(1)):
            print("Pls  enter  alternate  char  and  digit")
            break 
        
        S+=(int(s[i])*s[i-1])
    else:
        print("Result :",S)
        
else:
    print("enter even number of charcters alternate  char  and  digit")
 
'''