'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found 3 times
'''
try:
    a=eval(input('Enter a list : '))
    s=eval(input('Enter a number to be searched in the list : '))
    count=0
    for i in range(len(a)):
        if a[i]==s:
            print(f'{s} is found at index{i}')
            count+=1
    print(f'{s} is found {count} times')
except:
    print('Input string should be in quotes')

'''  Sample output
Enter a list : [10,20,15,12,18,15,19,14,15,14]
Enter a number to be searched in the list : 15
15 is found at index2
15 is found at index5
15 is found at index8
15 is found 3 times

Enter a list : [10,20,15,12,18,15,19,14,15,14]
Enter a number to be searched in the list : 11
11 is found 0 times

Enter a list : 'HYD'
Enter a number to be searched in the list : 'D'
D is found at index2
D is found 1 times

Enter a list : hyd
Input string should be in quotes
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

6) Hint2: Use  try and except
'''

from sys import argv
try:
	a=[]
	for x in argv[1:]:
		a.append(eval(x))
	print('Largest Input : ',max(a))
except ValueError:
	print('Send atleast one input')
except NameError:
	print('Input string should be in single or triple quotes.')
except TypeError:
	print('Input should be either string inputs or  number inputs but not both')

'''  Sample output
D:\Data engineering\python\command line arguments>py largest_commandinput.py 10 20 30.8 7 40 35.6
Largest Input :  40

D:\Data engineering\python\command line arguments>py largest_commandinput.py
Send atleast one input

D:\Data engineering\python\command line arguments>py largest_commandinput.py 10 'Ten'
Input should be either string inputs or  number inputs but not both

D:\Data engineering\python\command line arguments>py largest_commandinput.py 10 Ten
Input string should be in single or triple quotes.

D:\Data engineering\python\command line arguments>py largest_commandinput.py 'Rama' 'Sita' 'Rajesh' 'Manohar' 'Vamsi' 'Amar'
Largest Input :  Vamsi
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
    What  is  the  output  ?  --->   Pls  send   an  integer input
'''
from sys import argv
try:
	x=int(argv[1])
	if x%2==0:
		print('Even number')
	else:
		print('Odd number')
except:
	print('Please send an integer input')


'''
py even_odd.py 34
Even number

py even_odd.py 35
Odd number

py even_odd.py
Please send an integer input

py even_odd.py 'Ten'
Please send an integer input

py even_odd.py 10.4
Please send an integer input
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
    What  is  the  output  ?  ---> Pls  send  number inputs
'''
from sys import argv
try:
	a=[]
	for x in argv[1:]:
		a.append(eval(x))
	print('Average : ',sum(a)/len(a))
except ZeroDivisionError:
	print('Send atleast one input')
except NameError:
	print('Input should not be a string')

'''
py sum_len.py 10.8 25 True 14.6 19 False 7.4
Average :  11.114285714285716

py sum_len.py
Send atleast one input

py sum_len.py 10.8 Ten
Input should not be a string
'''


'''
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> a . sort()
    How  to  sort  list  'a'  in  descending  order  ?  --->  a . sort(reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs together
'''
from sys import argv
try:
	a=[]
	for x in argv[1:]:
		a.append(eval(x))
	a.sort()
	print('Ascending order : ',a)
	a.sort(reverse=True)
	print('Desending order : ',a)
except NameError:
	print('Input should not be string')

'''
py asc_des.py 10 20 15.8 5 12.6
Ascending order :  [5, 10, 12.6, 15.8, 20]
Desending order :  [20, 15.8, 12.6, 10, 5]

py asc_des.py
Ascending order :  []
Desending order :  []

py asc_des.py 10 'Ten'
Input should not be string
'''


