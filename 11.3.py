'''
11/3/2025

#1.isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) #False due to A
print('\n  \t' . isspace()) #True 
print('\n  7\t' . isspace()) #False due to 7
print('\n' . isspace()) #True
print('\n  $\t' . isspace()) #False due to $
print('\t' . isspace()) #True
print('' . isspace()) #False due to no space 
print(' ' . isspace()) #True

'''

'''
#2.Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) #25,10.8,Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) #25,10.8,Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) #Hyd,10.8,25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) #Hyd,Hyd,Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) #25,10.8,Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #Hyd,10.8,25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #25,25,25

'''


'''
#3.Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

Enter  any  character  :  A
Alpha  Numeric  Character
Alphabet  Character
Upper  case  Alphabet

'''

'''

s=input("Enter any Character: ")

if(s.isalnum()):
    print("Alpha  Numeric  Character")
    
    if(s.isalpha()):
        print("Alphabet  Character")
        
        if(s.isupper()):
            print("Upper  case  Alphabet")
            
        else:
            print("Lower  case  Alphabet")
            
    else:
        print("Digit Character")
    
elif(s.isspace( ) or s=="\\t" or s=='\\n'):
    print("White space")
    
else:
    print("Special character")
    
'''

'''
#4.Write  a  program  to  reverse  a  string  without  slice


Enter  any  string : Rama Rao
Reverse  String :   oaR amaR

'''


'''
s=input("Enter  any  string :")
S=''
for i in range(1,len(s)+1):
    S+=s[-i]
    
print(S)

'''


'''
#5.Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice


Enter  any  sententce : students are getting  bored
Reverse  order  of  words :  bored getting are students

'''

'''
s=input("Enter  any  sententce :").split()

S=''

for i in range(1,len(s)+1):
    
    if(i==len(s)):
        S+=s[-i]
        
    else:
        S+=s[-i]+" "
        
print(S)
    
'''


'''
#6.Write  a  program  to  reverse  each  word  of  the  sentence

Enter  any  sentence  :  hyd is green city
dyh si neerg ytic

'''

'''
s=input("Enter  any  sentence  :").split()
S=''
for i in range(len(s)):
    
    if(i<len(s)-1):
        S+=s[i][::-1]+" "
        
        
    else:
        S+=s[i][::-1]
        
print(S)

'''


'''
#7.Write  a  program  to  sort  string  in  alphabetical  order

Enter  any  string  :  RAJESH
Sorted  string  :    AEHJRS

'''

'''
s=input("Enter  any  string  :")
l=sorted(s)
print(''.join(l))

'''


'''
#8.Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579

1) Hint:  sorted()  function , isalpha() , isdigit()  and   join()  method

'''

'''

s=input("Enter  any  string  :")
l=sorted(s)

d=''
a=''

for i in l:
    if i.isdigit():
        d+=i 
        
    else:
        a+=i 
        
print(a+d)


'''