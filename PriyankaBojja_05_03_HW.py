'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found   3  times

a=[10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
x=eval(input('Enter value to be searched: '))
ctr=0
for i in range(len(a)):
		if a[i]==x:
			print(f' {x} Found at index ',i)	
			ctr+=1
if ctr!=0:
	print(f'{x} is found {ctr} times)
else:
	print('Not found')
			
	
		

Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1 with walrus operator

try:
	sum =  ctr = 0
	x = eval(input('Enter input  (-1  to  stop)  :  '))
	while (x:=eval(input('Enter input  (-1  to  stop)  :  ')))!= -1:
		sum += x
		ctr +=1
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not  be string')

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

from sys import argv
try:
	print(argv)
	a=[]
	a.extend(argv[1:])
	a=[eval(x) for x in a]
	print(a)
	print('max element is: ',max(a))
except ValueError:
	print('please send inputs')
except TypeError:
	print('Inputs cannot be number and string')


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
	print(argv)
	a=[]
	a.extend(argv[1:])
	a=[int(x) for x in a]
	print(a)
	for n in a:
		if n%2==0:
			print(f'{n} is an Even number')
		else:
			print(f'{n} is an Odd number')
except ValueError:
	print('please send valid inputs')


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
	print(argv)
	a=[]
	a.extend(argv[1:])
	a=[eval(x) for x in a]
	print('list: ',a)
	print('sum of list elements: ',sum(a))
	print('length of list: ',len(a))
	print('Average of list elements :',sum(a)/len(a))
except ValueError:
	print('please send valid inputs')
except ZeroDivisionError:
	print('List cannot be empty')


Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> a . sort()
    How  to  sort  list  'a'  in  descending  order  ?  --->  a . sort(reverse = True)
2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together

from sys import argv
try:
	print(argv)
	a=[]
	a.extend(argv[1:])
	a=[eval(x) for x in a]
	print('Original list',a)
	a.sort()
	print('Ascending order: ',a)
	a.sort(reverse=True)
	print('Descending Order: ',a)
except (ValueError,NameError):
	print('Please enter valid input')
'''