'''Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found   3  times '''

"""
a=list(input(" enter the values to the list only give single digits : "))
b=[]
for i in range(len(a)):
    b.append(eval(a[i]))
print(b)
n=int(input(" enter the number : "))
c=0
for i in range(len(b)):
    if b[i]==n:
        print(f"{n} is found at index {i}")
        c+=1
print(f"{n} is found {c} times ")
"""


#Modify  following   program  with  walrus  operator
#Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	x = eval(input('Enter input  (-1  to  stop)  :  '))
	while  x != -1:
		sum += x
		ctr +=1
		x = eval(input('Enter input  (-1  to  stop)  :  '))
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not  be string')
'''

"""
try:
	sum,ctr=0
	while (x:= eval(input('Enter input  (-1  to  stop)  :  '))) != -1:
		sum += x
		ctr +=1
		x = eval(input('Enter input  (-1  to  stop)  :  '))
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not  be string')

"""
#my method 
'''
a=int(input("enter the number : "))
b,c=0,0
while a!=-1:
	c+=a
	b+=1
	a=int(input("enter the numbe if you want to stop give -1 "))
print("average : ",c/b)
	'''

# command line inputs 
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
try:
    print("please send inputs : ")
    from sys import argv
    a=list(argv)
    print(a)
    b=[]
    for i in range(1,len(a)):
        c=i
        print(c)
        b.append(eval(a[i]))
    print(b)
    print(max(b))
    print(max(a[1:]))
except:
    print("Inputs  can  not  be  number  and  string")
'''

#Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number
'''
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
"""
try:
    from sys import argv
    a=list(argv)
    print(a)
    b=[]
    for i in range(1,len(a)):
            b.append(eval(a[i]))
    for i in range(len(b)):
        if b[i]%2==0:
            print("even number")
        else:
            print("odd number")
except:
    print("please send an integer input")
"""

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
# Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order
"""
1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> a . sort()
    How  to  sort  list  'a'  in  descending  order  ?  --->  a . sort(reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
"""
"""
try:
    from sys import argv
    a=list(argv)
    b=[]
    for i in range(1,len(a)):
        b.append(eval(a[i]))
    print(b)
    print(c:=sorted(b))
    print(c[::-1])
    print(c.reverse())
except:
    print("Pls  don't  send  number  and  string  inputs  together")

"""