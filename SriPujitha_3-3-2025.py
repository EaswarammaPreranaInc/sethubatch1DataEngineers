# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(a[i])
#How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(i, a[i])
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
for i in a:
    print(a.index(i), i)
#  How  to  print  list  elements  in  reverse  order   without  slice
a = eval(input('Enter  list  of  elements : '))
print('Indexed for loop :', a)
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(len(a)-1,-1,-1):
    print(a[i])
b = eval(input('Enter  list  of  elements : '))
print(' for each loop :', b)
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
print("we cannot print elements in reverse in a list using for each loop")
'''Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
1st  list  --->  [10 , 20 , 15 , 18]
2nd  list  --->  [30 , 40 , 35 , 12]
3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]
Hint:  Use  append()  method'''

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
try:
    if len(a)==len(b):
        for i in range(len(a)):
            k=a[i]+b[i]
            c.append(k)
        print('3rd  list : ' , c)
    else:
        print("lengths of 2 lists should be same")
    print("this only works with indexed for loop not for each loop")
except:
    print("enter only lists")
#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(len(a)):
    if 1<i<5:
        print(a[i])
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop
for i in a:
    s=a.index(i)
    if 1<s<5:
        print(i)
#  Gift
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
    x += 1
    print(x)
print('b :  ' ,  b)
'''a :   [11, 21, 16, 19]
11
21
16
19
b :   [10, 20, 15, 18]'''
#Write  a  program  to  print  first  20  even  numbers  with  while  loop
i=1
print("first  20  even  numbers: ")
while i<21:
    print(2*i, end=" ")
    i+=1
print("Bye")
#Write  a  program  to  print  first  20  odd  numbers  with  while  loop
i=1
print("first  20  odd  numbers: ")
while i<21:
    print((2*i)-1, end=" ")
    i+=1
print("Bye")
#Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n
i=1
n=int(input("Enter value of n :"))
print("Natural  Numbers ")
while i<(n+1):
    print(i, end=" ")
    i+=1
print("Bye")
#Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1
for i in range(10,0,-1):
    print(i, end=" ")
#Write  a  program  to  print  upper  and  lower  case  alphabets
for i in range(65,91):
    print(chr(i), end=" ")
for j in range(97,123):
    print(chr(j), end=" ")
#Write  a  program  to  print  first  'n'  terms  of  fibonacci  series
n=int(input("Enter number of terms :"))
print("fibonacci series:")
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
##Write  a  program  to  search  for  'x'  in  fibonacci  series
a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
x = int(input("Enter value to be searched: "))
if x in a:
    print("Found")
else:
    print("Not found")
#Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms
n=int(input("Enter number of terms :"))
print("Sum:", end=" ")
sum=0
for i in range(1,n+1):
    sum=sum+(1.1 * i)
    i+=1
print(sum)
#Write  a  program  to  determine  sum  of  first  20  even  numbers
print("Sum  of  first  20  even  number: ", end=" ")
sum=0
for i in range(21):
    sum+=i*2
print(sum)
#Write  a  program  to  determine  sum  of  first  20  Odd  numbers
print("Sum  of  first  20  Odd  number: ", end=" ")
sum=0
for i in range(1,21):
    sum+=2*i-1
print(sum)
#Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
n=int(input("Enter number of terms :"))
print("Sum:", end=" ")
sum=0
for i in range(1,n+1):
    sum=sum+(i)
    i+=1
print(sum)
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
'''1
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
Outside loop'''
#find error
if ():
	print('Hyd')
	continue
#continue is only valid inside loops (like for or while)
## Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
'''1
Sec
Hello
2
Sec
Hello
3
Outside loop
'''
# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')
#break is only valid inside loops (like for or while)
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
'''1
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
Outside loop'''
#pass does nothing just continues doing what its already doing
## Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
#1
'''Sec
Hello
2
Sec
Hello
3'''
