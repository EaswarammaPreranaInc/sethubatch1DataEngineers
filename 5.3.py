'''
5/3/2025

1.Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found   3  times
'''

'''
a=eval(input("List:"))
e=eval(input("element:"))
c=0
for i in range(len(a)):
    if a[i]==e:
        print(F"{a[i]} is fount at index {i}")
        c+=1 
        
if(c!=0):
    print(F"{e} is found {c} times")
    
else:
    print("not found")
    
'''


'''
2.Modify  following   program  with  walrus  operator average -1 
Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator
'''


'''
try:
    sum=c=0 
    while((x:=eval(input("Enter input  (-1  to  stop)  :")))!=-1):
        sum+=x 
        c+=1 
        
    print(F"Average: {sum/c}")
    
except:
    print("Don't enter sequence or complex and 1st i/p need not be -1")
        
'''

'''
Write  a  program  to  determine  largest  command  line  input

1) py   prog2.py   10     20     30.8    7   40    35.6
    What  is  the  largest  command  line  input ?  --->	40
    What  is  argv ?  ---> ['prog2.py' , '10' , '20' , '30.8' , '7' , '40' , '35.6']
    What  is  list  'a' ?  --->  [10 , 20 , 30.8 , 7 , 40 , 35.6]
    How  to  determine  largest  element  of  list  'a' ?  ---> max(a)  i.e.  40
    What  is  the  result  of  max(argv[1:]) ?  --->  '7'
    What  is  the  issue  with  max(argv[1:])) ?  --->  Largest  string  is  obtained  but  not  largest  number

2) py  prog2.py
    What  is  the  output ?  --->	Pls  send  inputs

3) py   prog2.py   'Rama'   'Sita'   'Rajesh'   'Manohar'   'Vamsi'   'Amar'
    What  is  the  largest  command  line  input ?  --->	'Vamsi'

4) py   prog2.py   25   'Ten'
    What  is  the  output ?  ---> Inputs  can  not  be  number  and  string

5) Hint1: Use  for  loop

6) Hint2: Use  try  and  except
'''

'''

import sys 
from sys import argv

try:
	a=[]

	for i in range(1,len(argv)):
		a.append(eval(argv[i]))
		
	if(len(a)==0):
		print("enter at least 1 element to find max ")

	else:
		print(max(a))

except:
	print("enter same type of elements to find max without complex")


'''


'''
4.Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->  ['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  --->	len(a)

2) py   prog4.py
    What  is  the  output ?  --->  Pls  send  number  inputs

3) py   prog4.py  25   'Ten'
    What  is  the  output  ?  ---> Pls  send  number  inputs
'''

'''

import sys 
from sys import argv

try:
	a=[]
    
	for i in range(1,len(argv)):
		a.append(eval(argv[i]))
		
	if(len(a)==0):
		print("enter at least 1 element to find avg ")

	else:
		avg=sum(a)/len(a)
		print(F"Average :{avg}")

except:
	print("enter only int Float bool")
	
'''


'''
5.Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> a . sort()
    How  to  sort  list  'a'  in  descending  order  ?  --->  a . sort(reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
'''

'''

import sys 
from sys import argv

try:
	a=[]
    
	for i in range(1,len(argv)):
		a.append(eval(argv[i]))
		
	if(len(a)==0):
		print("enter at least 1 element to find avg ")

	else:
		a.sort()
		print("Ascending :",*a)
        
		a.sort(reverse=True)
		print("Descending :",*a)

except:
	print("enter only int Float bool or only strings or lists or tuple but don't give mixed type ")
'''