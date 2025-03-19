

#1.Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found   3  times

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


"""
Output:
15 is  found  at  index  2
15 is  found  at  index  5
15 is  found  at  index  8
15 is  found   3  times
"""


#2.Modify  following   program  with  walrus  operator average -1 
#Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator
try:
    sum=c=0 
    while((x:=eval(input("Enter input  (-1  to  stop)  :")))!=-1):
        sum+=x 
        c+=1 
        
    print(F"Average: {sum/c}")
    
except:
    print("Don't enter sequence or complex and 1st i/p need not be -1")
        

"""
Output:
Enter input  (-1  to  stop)  :  25
Enter input  (-1  to  stop)  :  10.8
Enter input  (-1  to  stop)  :  True
Enter input  (-1  to  stop)  :  46.2
Enter input  (-1  to  stop)  :  False
Enter input  (-1  to  stop)  :  92
Enter input  (-1  to  stop)  :  -1
Average :   29.166666666666668
"""
#Write  a  program  to  determine  largest  command  line  input

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
OutPut:
40
'''
#4.Write  a  program  to  determine  average  of  command  line  inputs
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
Output:
 Even  number
Odd  number

'''
#5.Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order
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
Output:

'''
