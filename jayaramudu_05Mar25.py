# Ex-1: Search for an element in the list without using 'in' operator
 a = eval(input('Enter list of values: '))
try:
	count = 0
	n = int(input('Enter a search value: '))
	for i in range(len(a)):
		if a[i] == n:
			print(n, 'is found at index', i)
			count += 1
	if count == 0:
		print('Not found')
	else:
		print(n, 'is found', count, 'times')
except ValueError:
	print('Please Enter list of numbers')
except:
	print('Search input should be an integer')

# Ex-2: Modify program with walrus operator
'''
Modify  following   program  with  walrus  operator
Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	x = eval(input('Enter input  (-1  to  stop)  :  '))
	while (x := int(input('Enter input (-1 to stop): '))) != -1:
		sum += x
		ctr += 1
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not be string')


# Ex-3: Determine the largest command line input

from sys import argv
try:
	a = []
	for x in argv[1:]:
		a.append(eval(x))
	b = max(a)
	print(b)
except ValueError:
	print('Please send inputs')

# Ex-4: Determine if command line input is even or odd
from sys import argv
try:
	a = int(argv[1])
	if a % 2 == 0:
		print('Even number')
	else:
		print('Odd number')
except IndexError:
	print('Please  send   an  integer  input')

# Ex-5: Determine the average of command line inputs

from sys import argv
try:
    sum = count = 0
    for x in argv[1:]:
        sum += eval(x)
        count += 1
    print('Average :', sum / count)
except NameError:
    print('Inputs can be number and')
except TypeError:
    print('Please send integer inputs')
except ZeroDivisionError:
	print('Please send inputs')
except IndexError:  
    print('Please send inputs')

# Ex-6: Sort command line inputs in ascending and descending order
from sys import argv
try:
	a = []
	sum=0
	for i in argv[1:]:
		a.append(eval(i))
	for i in range(len(a)):
		sum +=a[i]
	c = len(a)
	print('Average' ,sum / c)
except:
	print('please send a inputs')
