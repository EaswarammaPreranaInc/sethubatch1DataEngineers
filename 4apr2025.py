#4/4/2025 

#1. Write  a  program  to  print  random  character  of  the  string  10  times 

'''
Enter any string : Hyderabad
H
r
d
y
a
H
H
b
d
b

'''

'''
from random import*
s=input("Enter any string : ")

for i in range(10):
    print(choice(s))
    
'''



'''  
2. Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

I6N8X7
L7V4Q8
Q8C3M9
C8O2O1
J6Q1W3
K0J1Y0
B4P7D6
U1J5L1
C6D0J6
G6C6D5

'''

'''
from random import*
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
D="1234567890"
for i in range(10):
    s=''
    for j in range(6):
        if(j%2==0):
            s+=choice(A)
            
        else:
            s+=choice(D)
            
    print(s)
            
'''

#3.Write  a  program  to  print  random  element  of  the  list  ten  times

'''
Enter a List : [25,10.8,'Hyd',True,None,3+4j]
Hyd
True
True
Hyd
Hyd
True
None
(3+4j)
(3+4j)
None
'''

'''
from random import*
l=eval(input("Enter a List : "))

for i in range(10):
    print(choice(l))

'''

#4.Write  a  program  to  generate  ten  six-digit  OTP's 

'''

758391
560191
630217
698421
711429
669098
757873
710738
504203
983112

'''

'''
from random import*
for i in range(10):
    print(randint(10**5,10**6-1))
 
'''


'''
5. Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''

'''
from webbrowser import*
from random import* 
from time import*

list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

for i in list:
    print(open('http://'+i))
    sleep(5)

'''


''' 
6.
Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  --->  Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																											Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																										Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  ---> 
																										Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  ---> User  wins
'''

'''
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  2
User  :   Scissors
Computer  :   Paper
User  wins
Continue  (  y / n)  ?  y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  0
User  :   Rock
Computer  :   Paper
Computer  wins
Continue  (  y / n)  ?  y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  1
User  :   Paper
Computer  :   Paper
Draw
Continue  (  y / n)  ?  n
End  of  the  game

'''

'''
from random import* 

while(True):
    uc=['Rock' ,'Paper' ,'Scissors']
    u= uc[int(input('What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors) :'))]
    c = choice(uc)
    
    print("User : ",u)
    print("Computer :",c)
    
    if(c==u):
        print('Draw')
        
    elif (c=='Rock' and u=='Scissors' or c=='Paper' and u=='Rock' or c=='Scissors' and u=='Paper'):
        print('Computer wins')
        
    else:
        print('User wins')
        
    bc= input('Continue  (  y / n)  ? ')
    
    if(bc=='n'):
        break
        
'''