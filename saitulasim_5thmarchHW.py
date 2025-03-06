
#1:Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

a=[10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
x=eval(input('Enter value to be searched: '))
ctr=0
for i in range(len(a)):
		if a[i]==x:
			print(f' {x} is found at index ',i)	
			ctr+=1
if ctr!=0:
	print(f'{x} is found {ctr} times')
else:
	print('Not found')

'''15 is  found  at  index  2
15 is  found  at  index  5
15 is  found  at  index  8
15 is  found   3  times'''

# 2:Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1 with walrus operator

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

 
'''Enter input  (-1  to  stop)  :  3
Enter input  (-1  to  stop)  :  4.3
Enter input  (-1  to  stop)  :  2
Enter input  (-1  to  stop)  :  True
Enter input  (-1  to  stop)  :  1
Enter input  (-1  to  stop)  :  6
Enter input  (-1  to  stop)  :  -1
Average :   2.8600000000000003 '''

# 3:Write  a  program  to  determine  largest  command  line  input

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
 

''' C:\PYTHON SSSDP>py PriyankaBojja_05_03_HW.py 2 4 12 7 34 True
['PriyankaBojja_05_03_HW.py', '2', '4', '12', '7', '34', 'True']
[2, 4, 12, 7, 34, True]
max element is:  34 '''

# 4:Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

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


''' C:\PYTHON SSSDP>py PriyankaBojja_05_03_HW.py 1 2
['PriyankaBojja_05_03_HW.py', '1', '2']
[1, 2]
1 is an Odd number
2 is an Even number '''

# 5:Write  a  program  to  determine  average  of  command  line  inputs

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

 
''' C:\PYTHON SSSDP>py PriyankaBojja_05_03_HW.py True 4 2 5.6 False
['PriyankaBojja_05_03_HW.py', 'True', '4', '2', '5.6', 'False']
list:  [True, 4, 2, 5.6, False]
sum of list elements:  12.6
length of list:  5
Average of list elements : 2.52 '''

# 6:Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

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

''' C:\PYTHON SSSDP>py PriyankaBojja_05_03_HW.py 5.2 True 41 8 False
['PriyankaBojja_05_03_HW.py', '5.2', 'True', '41', '8', 'False']
Original list [5.2, True, 41, 8, False]
Ascending order:  [False, True, 5.2, 8, 41]
Descending Order:  [41, 8, 5.2, True, False] '''
