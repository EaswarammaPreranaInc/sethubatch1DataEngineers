'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found   3  times

a=[10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
search=15
count=0
for i in range(len(a)):
	if search==a[i]:
		print(f"{search} is found at index {i}")
		count=count+1
print(f"{search} is found {count} times")

'''

'''
Modify  following   program  with  walrus  operator
Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator

try:
	sum =  ctr = 0
	
	while  (x:=eval(input('Enter input  (-1  to  stop)  :  '))) != -1:
		sum += x
		ctr +=1
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not  be string')
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

from sys import argv
try:
	c=[]
	l=argv[1:]

	for i in l:
		c.append(int(i))
	print(c)
	print(max(c))
except:
	print("Enter only integers")
'''

'''


Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

1) py  prog3.py  26
    What  is  the  output ?  ---> Even  number

2) py  prog3.py  45
    What  is  the  output ?  --->  Odd  number

3) py  prog3.py
    What  is  the  output  ?  --->  Pls  send  an  integer  input

4) py  prog3.py  10.8
    What  is  the  output ?  --->  Pls  send   an  integer  input

5) py  prog3.py  Ten
    What  is  the  output  ?  --->   Pls  send   an  integer  input


from sys import argv
try:
	if int(argv[1])%2==0:
		print("Even")
	else:
		print("Odd")
except:
	print("Pls  send   an  integer  input")
'''

'''
Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->  ['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  --->	len(a)

2) py   prog4.py
    What  is  the  output ?  --->  Pls  send  number  inputs

3) py   prog4.py  25   'Ten'
    What  is  the  output  ?  ---> Pls  send  number  inputs

from sys import argv
try:
	sum=count=0

	for i in argv[1:]:
		sum=sum+int(i)
		count+=1
	print("Average is",avg:=sum/count)
except:
	print("Enter only integers")
'''

'''
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> a . sort()
    How  to  sort  list  'a'  in  descending  order  ?  --->  a . sort(reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
'''
'''
from sys import argv
try:
	c=[]
	for i in argv[1:]:
		c.append(int(i))
		c.sort()
	print(c)
except:
	print("Pls  don't  send  number  and  string  inputs  together")
'''
