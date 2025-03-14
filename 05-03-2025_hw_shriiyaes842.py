'''
1.Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> a . sort()
    How  to  sort  list  'a'  in  descending  order  ?  --->  a . sort(reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
'''

import sys
try:
	a=sys.argv[1:]
	c=[]
	for i in a:
		b=eval(i)
		c.append(b)
	c.sort()
	print(c)
	c.sort(reverse=True)
	print(c)
except:
	print("Pls  don't  send  number  and  string  inputs  together")


'''
2.Write  a  program  to  determine  average  of  command  line  inputs

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
import sys
if len(sys.argv)==1:
		print("Pls  send  number  inputs")
		sys.exit()
x=sys.argv[1:]
try:
	s=0
	b=[]
	
	for i in x:
		number=eval(i)
		b.append(number)
		s=s+number
	average=s/(len(b))
	print(average)
except TypeError:
	print("Please enter numbers")
except ZeroDivisionError: 
	print('division by zero')

'''
3.Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

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
import sys
try:
	
	if int((sys.argv[1]))% 2==0 :
		print("even")
	else:
		print("odd")
except (ValueError,IndexError):
	print("Pls  send   an  integer  input")


'''
4.Modify  following   program  with  walrus  operator
Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	
	while  x := eval(input('Enter input  (-1  to  stop)  :  ')):
		if x==-1:
			break
		sum += x
		ctr +=1
		
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not  be string')


'''
5.Write  a  program  to  determine  largest  command  line  input

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

import sys
try:
	a=sys.argv[1:]
	c=[]
	for i in a:
		b=eval(i)
		c.append(b)
	print(max(c))

except TypeError:
	print("Inputs  can  not  be  number  and  string")
except NameError:
	print("Inputs  can  not  be  number  and  string")
except ValueError:
	print("Enter atleast one input")


'''
6.Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found   3  times
'''

x=eval(input("Enter element to be searched:"))
a=[10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
ctr=0
if x not in a:
	print("Not found")
else:
	for i in range(len(a)):
		if x==a[i]:
			print(F"{x} Found at index: {i}")
			ctr+=1
	print(F"{x} is  found {ctr} times")
	

