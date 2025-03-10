'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator
List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
Search  for  15
Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found   3  times
'''
x = eval(input('Enter the number: '))
y =  [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
for i in range(len(y)):
	if y[i] == x :
		print(f'{x} is found at {i}')
		continue
if z := y.count(x):
	print(f'{x} is Found {z} times')
else:
	print("Not Found")


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
'''

from sys import argv
try:
	a = int(argv[1])
	if a % 2 == 0:
		print("Even number")
	else:
		print('Odd number')
except ValueError:
	print('Please send an integer input')


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
from sys import argv
try:
	a=[]
	for x in argv[1:]:
		a.append(eval(x))
	a.sort()
	print('Ascending Order : ',a)
	a.sort(reverse = True)
	print('Descending Order : ',a)
except (TypeError, NameError):
	print("Please don't send number and string inputs together" )

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
from sys import argv
try:
	a = []
	for x in argv[1:]:
		a.append(eval(x))
	print('Largest input: ',max(a))
except (TypeError,ValueError):
	print('Inputs  can  not  be  number  and  string')

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
'''
from sys import argv
try:
	a = []
	for x in argv[1:]:
		a.append(eval(x))
	print('Average: ',sum(a)/len(a))
except (NameError,TypeError):
	print('Please send only integer values')
except ZeroDivisionError:
	print('Send atleast one integer.')

