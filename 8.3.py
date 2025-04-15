"""
8/3/2025

1.Write  a  program  to  merge  two  strings  to  form  a  new  string

Enter  first  string  :  VAMSI
Enter  second  string  :  HYD
Result  :   VHAYMDSI

"""

'''
a = input("Enter  first   string  :")
b = input("Enter  second  string  :")

m=min(len(a),len(b))
i=0 
S=''

while(i<m):
    S+=a[i]+b[i]
    i+=1
    
if(m==len(a)):
    S+=b[m:]

else:
    S+=a[m:]
    
print("Result  :",S)

'''

'''
2.Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

Enter  any  string  :  MISSISIPI
String  without  duplicates  :    MISP

'''

'''
s=input("Enter  any  string  :")
S=''

for i in s:
    if i not in S:
        S+=i 
        
print("String  without  duplicates  :",S)

'''


'''
3.

Enter  any  string  with  alternate  character  and  digit  :  M3K2$5z2
Result  :   MPKM$)z|

Enter  any  string  with  alternate  character  and  digit  :  hyd
Pls  enter  string  with  alternate  char  and  digit

'''

'''
s=input("Enter  any  string  with  alternate  character  and  digit  :")
S=''

try:
    for i in range(0,len(s),2):
        S+= s[i]+chr(ord(s[i])+int(s[i+1]))
        
    print(S)
    
except:
    print("Pls  enter  string  with  alternate  char  and  digit of even number of characters")
    
'''