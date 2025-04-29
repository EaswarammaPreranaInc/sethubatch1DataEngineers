'''
10/3/2025 

1.Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

'''
s=input("Enter any string: ").upper()

S=''

for i in s:
    if i in "AEIOU" and i not in S:
        S+=i 
        
print(S)

'''


'''
2.Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''

'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index=-1
while  (index:=a . find('is' , index + 1))!= -1:
	print(index)
	
print('End')

'''

'''  
3.index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except
'''

'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

try:
    index=-1
    while (index:=a . index('is' , index + 1)):
        print(index)
	
except:
    print("End")
'''



'''
4.rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''

'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index=len(a)
while  (index:=a . rfind('is',0,index-1))!=-1:
    print(index)
    
print("End")
'''


'''
5.rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''

'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

try:
    index=len(a)-1
    while (index:= a .rindex('is' ,0,index-1)):
        print(index)
        
        
except:	
    print('End')
    
'''


'''
6.Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*' 
except  first  character

Enter  any  string :  babble
Result :   ba**le

'''

'''
s=input("Enter  any  string :")
S=s[1:]
print(s[0]+S.replace(s[0],'*'))

'''


'''
7.Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method


Enter the expression: 23+456+7
Sum:  486
'''

'''
s=input("Enter the expression:").split("+")

try:
    S=0
    for i in s:
        S+=int(i)
        
    print(S)
except:
    print("Enter only int  in the expression ")
    
'''


'''
8.Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

4) Hint:  Use  endswith()  method
'''
'''
s=input("Enter any string: ")

if(len(s)<3):
    print(s)
    
else:
    if(s.endswith("ing")):
        print(s+"ly")
        
    else:
        print(s+"ing")
        
'''