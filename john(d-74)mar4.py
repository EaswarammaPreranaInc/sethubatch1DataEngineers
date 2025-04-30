'''Write  a  program  to  determine  largest  command  line  input

from sys import argv
b=argv
a=[]

for i in range(1,len(b)):
	
	a.append(eval(b[i]))
print(f'{a}')
print(max(a))
#print(max(b))

C:\Users\johni\OneDrive\Pictures>py argv.py '1' '2' '3' '7'
['1', '2', '3', '7']
7

C:\Users\johni\OneDrive\Pictures>py argv.py 10 20 30 40
[10, 20, 30, 40]'''
#40


Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number
from sys import argv
b=argv
a=[]
for i in range(1,len(b)):
      print(b)
      a.append(eval(b[i]))
for i in a:
	if i%2==0:
		print('even number')
	else:
		print('odd number')
outputs--	
C:\Users\johni>py argv1.py 25
['argv1.py', '25']
odd number

C:\Users\johni>py argv1.py 26
['argv1.py', '26']
even number

#Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order
try:
 from sys import argv
 a=argv
 b=[]
 for i in range(1,len(a)):
	  b.append(eval(a[i]))
     
 print(c:=sorted(b))
 print(c[::-1])
except:
	print("Pls  don't  send  number  and  string  inputs  together")

outputs---

C:\Users\johni>py argv2.py 25 10 39 4 56
[4, 10, 25, 39, 56]
[56, 39, 25, 10, 4]

C:\Users\johni>py argv2.py 25 "ten"
Pls  dont  send  number  and  string  inputs  together
