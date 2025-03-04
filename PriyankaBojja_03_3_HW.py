'''
1
# How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for i in range(len(a)):
	print(a[i],i)

#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
a=[10,20,10,30]
print('For each loop')
index=0
for i in a:
	print(index,i)
	index+=1


2
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop(without slice)
a = eval(input('Enter  list  of  elements : '))
print('Indexed for loop')
for i in range(len(a)-1,-1,-1):
	print(a[i])
	
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable)
a = eval(input('Enter  list  of  elements : '))
print('for each loop')
for i in reversed(a):
	print(i)


3
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list with  indexed  based   for  loop
1st  list  --->  [10 , 20 , 15 , 18]
2nd  list  --->  [30 , 40 , 35 , 12]
3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]
Hint:  Use  append()  method

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for i in range(len(a)):
	c.append(a[i]+b[i])
print('3rd  list : ' , c)
    
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
for x,y in zip(a,b):
	c.append(x+y)
print('3rd  list : ' , c)


4
#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
for i in range(2,5):
	print(a[i])

#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('for each loop')
for index, value in enumerate(a):
	if index >=2 and index<=4:
		print(value)

5
#  Gift
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) 

a[0]= 10+1=11
a[1]= 20+1=21
a[2]= 15+1=16
a[3] = 18+1=19
OUTPUT-->  a: [11,21,16,19]

b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) 

x=10+1=11
x=20+1=21
x=15+1=16
x=18+1=19
but x value does not modify in list because we are not changing the index values like above
OUTPUT--> b: [10,20,15,18]


6
(Home  work)
Write  a  program  to  print  first  20  even  numbers  with  while  loop

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40
2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20
3) Use  while  loop


print('First 20 even numbers')
i=1
while i<=20:
	print(2*i)
	i+=1
print('Bye')

OP-
First  20  even   numbers
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
Bye

7
Write  a  program  to  print  first  20  odd  numbers  with  while  loop
1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39
2) In  general, print  what ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

print('First 20 odd numbers')
i=1
while i<=20:
	print((2*i)-1)
	i+=1


First  20  odd  numbers
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39

8
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'
In  general,  print  what ?  --->  Print  'i'  where  'i'  varies  from  1  to  n
Hint:  Use  for  loop
'''
n=int(input('Enter value of n :'))
print('Natural numbers')
for i in range(1,n+1):
	print(i)
	i+=1
'''
Enter value of n : 25
Natural  Numbers
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

9
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1
In  general, print  what ?  --->  Print  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1
Hint:  Use  for  loop

print('Numbers from 10 downto 1 in steps of -1')
for i in range(10,0,-1):
	print(i)

OP-
Numbers from 10 downto 1 in steps of -1
10
9
8
7
6
5
4
3
2
1

10
Write  a  program  to  print  upper  and  lower  case  alphabets
Hint:
1) chr(65) =  'A'
    chr(90) = 'Z'
    chr(97) =  'a'
    chr(122) = 'z'
2) What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character

3) ord('A') =  65
    ord('Z') = 90
    ord('a') =  97
    ord('z') =  122

4) What  does  ord()  function  do ?  --->  Converts  character  to  unicode  value 
5) Hint:  Use  two  for  loops

print('Uppercase letters')
for x in range(65,91):
	print(chr(x),end=' ')
print()
print('Lowercase letters')
for y in range(97,123):
	print(chr(y),end=' ')

OP
Uppercase letters
A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
lowercase letters
a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z

11
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series
Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
Hint:  Use  for  loop


x= int(input('Enter number of terms: '))
if x==0:
	print('Fibonacci series')
	print(0)
elif x<0:
	print('Input must be positive integer')
else:
		a=0
		b=1
		print('Fibonacci series')
		print(a)
		print(b)
		c=a+b
		count=2
		for i in range(x):
			if count<x:
				print(c)
				a=b
				b=c
				c=a+b
				count+=1
			
	
Enter number of terms : 10
Fibonacci series
0
1
1
2
3
5
8
13
21
34

12
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found
2) Let  input  be   21
    What  is  the  output ? ---> Found
3) Do  not  generate  fibonacci  series


x=int(input('Enter value to be searched: '))
a,b=0,1
c=a+b
while a<=x:
	if a==x:
		print('Found')
		break
	a=b
	b=c
	c=a+b
else:
	print('Not found')

OP
Enter  value  to  be  searched :  10
Not  Found
Enter  value  to  be  searched :  21
Found

13
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms
1) sum =  0 + 1.1 * 1 + 1.1 * 2 + 1.1* 3 +  ......
2) What  is  added  to  sum  in  general ?  ---> 1.1 * i   where  'i'  varies  from  1  to  n

x=int(input('Enter the number of terms to add: '))
sum=0
i=1
while i<=x:
	sum+=1.1*i
	i+=1
print(sum)
	
OP
Enter the number of terms to add: 5
sum  :   16.5

14
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20
2) What  is  added  to  sum  in  general ? ---> 2 * i   where 'i'  varies  from   1  to  20


sum=0
i=1
while i<=20:
	sum+=2*i
	i+=1
print('Sum  of  first  20  even  numbers : ',sum)

OP
Sum  of  first  20  even  numbers :   420

15
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + 2 * 1 - 1 + 2 * 2 - 1 + 2 * 3 - 1 +  ... + 2 * 20 - 1

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

sum=0
i=1
while i<=20:
	sum+=(2*i)-1
	i+=1
print('Sum  of  first  20  odd  numbers : ',sum)

OP-
Sum  of  first  20  odd  numbers :   400

16
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

x=int(input('Enter the number of terms to add: '))
sum=0
i=1
while i<=x:
	sum+=i
	i+=1
print('Sum : ',sum)

OP-
Enter the number of terms to add: 10
Sum :   55

17
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

OP-
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
Outside loop

18
# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue   #error - continue must be in for loop or while loop
	print('Sec')

19
# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break          #break statement will stop the execution at 3%3==0 because the condition is true and come out of if condition
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

OP-
1
Sec
Hello
2
Sec
Hello
3
Outside loop

20
# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break         #error- break must be used in for or while loop
	print('Sec')

21
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

OP-
Sec
Hello
2
Sec
Hello
3
Hyd
Hello
4
Sec
Hello
5
Sec
Hello
6
Hyd
Hello
7
Sec
Hello
Outside loop

22
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

OP-
1
Sec
Hello
2
Sec
Hello
3
'''