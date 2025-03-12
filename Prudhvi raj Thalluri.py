a=[25 , 10.8 , 'Hyd' , True]
for x in range(len(a)):
	print(x,a[x])
print()
for i in a:
	print(a.index(i),i)

"""
Output:
0 25
1 10.8
2 Hyd
3 True

0 25
1 10.8
2 Hyd
3 True
"""

#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable)
a=eval(input('Enter  list  of  elements : '))
for x in range(1,len(a)+1):
	print(a[-x])
print()
a.reverse()
for i in a:
	print(i)
  """
  Output:
  Enter  list  of  elements : [10,20,30,40]
40
30
20
10

40
30
20
10
"""

#Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
#1st  list  --->  [10 , 20 , 15 , 18]
#2nd  list  --->  [30 , 40 , 35 , 12]
#3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c=[]
for i in range(len(a)):
	c.append(a[i]+b[i])
print(c)
for x in c:
	print(c)
	exit()
"""
Output:
Enter  1st  list  :  [10,20,30,40]
Enter  2nd  list  :  [10,20,30,40]
[20, 40, 60, 80]
[20, 40, 60, 80]
"""

#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for x in range(2,len(a)-2):
	print(a[x])
for x,y in enumerate(a) :
	if (x>=2 and x<=4):
		print(y)
"""
Output:
Hyd
True
(3+4j)

Hyd
True
(3+4j)
"""
#1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

#2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

#3) Use  while  loop
i=0
print("The First 20 Even numbers are")
while i<=20:
	print(i*2)
	i+=1
"""
Output:
The First 20 Even numbers are
0
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
"""
#Write  a  program  to  print  first  20  odd  numbers  with  while  loop
#1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39
#2) In  general, print  what ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
i=1
print("The First 20 Odd numbers are")
while i<=20:
	print(i*2-1)
	i+=1
"""
Output:
The First 20 Odd numbers are
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
"""
#Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

#In  general,  print  what ?  --->  Print  'i'  where  'i'  varies  from  1  to  n

#Hint:  Use  for  loop
n=int(input("Enter n no of natural number: "))
i=0
while i<=n:
	print(i)
	i+=1
"""
Output:
Enter n no of natural number: 25
0
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
"""

#Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

#In  general, print  what ?  --->  Print  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

#Hint:  Use  for  loop
try:
	i=int(input("Enter the input: "))
	while i>=0:
		print(i)
		i-=1
except:
	print("Enter valid number")
"""
Output:
Enter the input: 10
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
0
"""
#Write  a  program  to  print  upper  and  lower  case  alphabets
for i in range(65,90):
	print(chr(i), end=" ")
	#print()
for j in range(97,123):
	print(chr(j), end=" ")
"""
Output:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
a b c d e f g h i j k l m n o p q r s t u v w x y z
"""
#Write  a  program  to  print  first  'n'  terms  of  fibonacci  series
try:
    x=int(input("Enter  value  to  be  searched :"))
    a=0 
    b=1 
    if(x==0 or x==1):
        print("Found")
        
    else:
        for i in range(1,x+1):
            c=a+b 
            if(c==x):
                print("Found")
                break 
            a=b 
            b=c
        
        else:
            print("Not Found")
except:
    print("enter integer only")
    

"""
Output:
Enter  value  to  be  searched :5
Found
"""
#Write  a  program  to  print  fibonacci  series  upto   x
n=int(input("Enter the number"))
a,b=0,1
while a<=n:
	print(a)
	a,b=b,a+b

"""
Output:
Enter the number 4
0
1
1
2
3
"""
#Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms
try:
	i=eval(input("Enter the Input: "))
	a=0
	for i in range(1,i+1):
		t=1.1*i
		a=a+t
	print(a)
except:
	print("Invalid Input")
"""
Output:
Enter the Input: 10
60.50000000000001
"""
#Write  a  program  to  determine  sum  of  first  20  even  numbers
i=0
a=1
print("The sum of First 20 Even numbers")
while i<=20:
	a+=i*2
	i+=1
print(a)
"""
Output:
The sum of First 20 Even numbers
421
"""

#Write  a  program  to  determine  sum  of  first  20  odd  numbersi=1
a=0
print("The sum of First 20 Odd Numbers are")
while i<=20:
	a+=i*2-1
	i+=1
print(a)
"""
Output:
The sum of First 20 Odd Numbers are
400
"""
#Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
#What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
try:
	n=eval(input("Enter the nth number: "))
	a=0
	i=1
	while i<=n:
		a+=i
		i+=1
	print(a)
except:
	print("Invalid input")
"""
Output:
Enter the nth number: 10
55
"""







