# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):  # How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
	print(i,a[i],sep=':')
print('Indexed for loop')

''' Sample output
0:25
1:10.8
2:Hyd
3:True
Indexed for loop
'''


for x in a:  # How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use 2nd variable)
    print(a.index(x),x,sep=':')
print('For each loop')

''' Sample output
0:25
1:10.8
2:Hyd
3:True
For each loop
'''


#  How  to  print  list  elements  in  reverse  order   without  slice
a = eval(input('Enter  list  of  elements : '))  # [10,20,15,18,10,18]
for i in range(1,len(a)+1):  # How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
    print(a[-i])
print('Reverse order Indexed for loop')

''' Sample output
Enter  list  of  elements : [10,20,15,18,10,18]
18
10
18
15
20
10
Reverse order Indexed for loop
'''

# How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use 2nd variable)--> Not possible

# for each loop can iterate from left to right but not reverse order(right to left)


# Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
a=eval(input('Enter 1st list : '))  # [10,20,15,18]
b=eval(input('Enter 2nd list : '))  # [30,40,35,12]
c=[]
for i in range(len(a)):
	c.append(a[i]+b[i])
print(f'Sum of 2 lists : {c}')

'''Sample output
Enter 1st list : [10,20,15,18]
Enter 2nd list : [30,40,35,12]
Sum of 2 lists : [40, 60, 50, 30]
'''
# With for each loop it is not possible


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']
for i in range(2,len(a)-2): # How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
	print(a[i])
print('Indexed for loop')

''' Sample output
Hyd
True
(3+4j)
Indexed for loop
'''

# How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with for each loop-->not possible
# for each loop can iterate whole sequence but not part of sequence


# Write  a  program  to  print  first  20  even  numbers  with  while  loop
print('First 20 even numbers')
i=1
while i<=20:
      print(i*2)
      i=i+1

''' Sample output
First 20 even numbers
2<nextline>4<nextline>6<nextline>8<nextline>10<nextline>12<nextline>14<nextline>16
18<nextline>20<nextline>22<nextline>24<nextline>26<nextline>28<nextline>30<nextline>32<nextline>34<nextline>36<nextline>38<nextline>40
'''


# Write  a  program  to  print sum first  20  even  numbers 
print('First 20 even numbers')
i=1
sum=0
while i<=20:
      sum+=2*i
      i=i+1
print(sum)


''' Sample output
First 20 even numbers
420
'''


# Write  a  program  to  print  first  20  odd  numbers  with  while  loop
print('First 25 Odd numbers')
i=1
while i<=20:
      print(i*2-1)
      i=i+1

''' Sample output
First 25 Odd numbers
1<nextline>3<nextline>5<nextline>7<nextline>9<nextline>11<nextline><nextline>13<nextline>15<nextline>17<nextline>19<nextline>21<nextline>23<nextline>25<nextline>27<nextline>29<nextline>31<nextline>33<nextline>35<nextline>37<nextline>39
'''


# Write  a  program  to  print sum of  first  20  odd  numbers
print('First 25 Odd numbers')
i=1
sum=0
while i<=20:
      sum+=i*2-1
      i=i+1
print(f'sum: {sum}')


''' Sample Output
First 25 Odd numbers
sum: 400
'''


# Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'
a=eval(input('Enter value a : '))
print('Natural Numbers')
i=1
while i<=a:
	print(f'{i}')
	i+=1


''' Sampel output
Enter value a : 10
Natural Numbers
1<nextline>2<nextline>3<nextline>4<nextline>5<nextline>6<nextline>7<nextline>8<nextline>9<nextline>10
'''




# Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1 In  general, print  what ?  --->  Print  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

n=eval(input('Enter value a : '))
print('Natural Numbers reverse order')
i=n
while i>0:
	print(f'{i}')
	i-=1


''' Sample output
Enter value a : 10
Natural Numbers reverse order
10<nextline>9<nextline>8<nextline>7<nextline>6<nextline>5<nextline>4<nextline>3<nextline>2<nextline>1
'''


# Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
a=eval(input('Enter value a : '))
print('Natural Numbers')
sum=0
for i in range(1,a+1):
    sum+=i
print(f'Sum: {sum}')


''' Sample output

Enter value a : 10
Natural Numbers
55
'''


# Write  a  program  to  print  upper  and  lower  case  alphabets
for i in range(65,91):
    print(f'{chr(i)}',end=' ')
print()
for j in range(97,122):
    print(chr(j),end=' ')

''' Sample output
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
a b c d e f g h i j k l m n o p q r s t u v w x y
'''


# Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

x=int(input('Enter number of terms : '))
print('Fibonacci series')
a=0
print(a)
if x>1:
		b=1
		print(b)
		c=a+b
		for i in range(x-2):
			print(c)
			a=b
			b=c
			c=a+b



# Write  a  program  to  search  for  'x'  in  fibonacci  series
x=int(input('Enter a number to be searched : '))
if x==0:
	print('Found')
else:
	a=0
	b=1
	c=a+b
	while c<=x:
		if c==x:
			print('Found')
			exit()
		a=b
		b=c
		c=a+b
	print('Not found')

'''Sample outputs
Enter a number to be searched : 7
Not found

Enter a number to be searched : 10
Not found

Enter a number to be searched : 23
Not found

Enter a number to be searched : 8
Found
'''


# Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms
n=int(input('No of terms to be added : '))
sum=0
for i in range(1,n+1):
	sum+=1.1*i
print('Sum : ',sum)

'''  Sample outputs
No of terms to be added : 4
Sum :  11.0

No of terms to be added : 5
Sum :  16.5
'''


