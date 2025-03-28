
# 1. How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]

print('Indexed for loop')
#How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for i in range(len(a)):
	print(i,a[i])


print('For each loop')
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
for x in a:
	print(a.index(x),x)



# 2. How  to  print  list  elements  in  reverse  order   without  slice
a = eval(input("Enter  list  of  elements :"))
print('Indexed for loop')
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(len(a)-1,-1,-1):
	print(a[i],end=" ")

print()
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable)
#Not possible


'''
3. Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
d = []
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
for i in range(len(a)):
	sum=a[i]+b[i]
	c.append(sum)

print('3rd  list : ' , c)

#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop
#Not possible



# 4. How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2,5):
	print(a[i])

print('foreach loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop
#Not possible



'''
5.(Home  work)
Write  a  program  to  print  first  20  even  numbers  with  while  loop

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Use  while  loop
'''
print("First 20 even numbers")
i=1
while i<=20:
	print(2*i)
	i=i+1



'''
6. Write  a  program  to  print  first  20  odd  numbers  with  while  loop

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) In  general, print  what ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
'''

print("First 20 odd numbers")
i=1
while i<=20:
	print(2*i-1)
	i=i+1



'''
7. Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

In  general,  print  what ?  --->  Print  'i'  where  'i'  varies  from  1  to  n

Hint:  Use  for  loop
'''
n=int(input("Enter value of n:"))
print("Natural numbers")
for i in range(1,n+1):
	print(i)



'''
8. Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

In  general, print  what ?  --->  Print  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

Hint:  Use  for  loop
'''

for i in range(10,0,-1):
	print(i)



'''
9. Write  a  program  to  print  upper  and  lower  case  alphabets

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
'''
for i in range(65,91):
	print(chr(i),end=" ")
print()
for i in range(97,123):
	print(chr(i),end=" ")



'''
10. Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5

Hint:  Use  for  loop
'''

n=int(input("Enter number of terms :"))
print("Fibonacci series")
a=0
b=1
print(a)
print(b)
for i in range(2,n):
	c=a+b
	a=b
	b=c
	print(c)



'''                                                       
11. Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? ---> Found

3) Do  not  generate  fibonacci  series
'''

x=int(input("Enter  value  to  be  searched :"))
a=0
b=1
for i in range(2,x+1):
	c=a+b
	a=b
	b=c
	if x==c:
		print("Found")
		break
else:
	print("Not found")



'''
12. Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0 + 1.1 * 1 + 1.1 * 2 + 1.1* 3 +  ......

2) What  is  added  to  sum  in  general ?  ---> 1.1 * i   where  'i'  varies  from  1  to  n

How  many  terms  would  you  like  to  add   :  5
Sum  :   16.5
'''

n=int(input("terms  would  you  like  to  add:"))
sum=0
for i in range(1,n+1):
	sum=sum+(1.1*i)
print(sum)



'''
13. Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? ---> 2 * i   where 'i'  varies  from   1  to  20

 Sum  of  first  20  even  numbers :   420
 '''

sum=0
for i in range(21):
	sum=sum+2*i
print("Sum of  first  20  even  numbers :",sum)



'''
14. Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + 2 * 1 - 1 + 2 * 2 - 1 + 2 * 3 - 1 +  ... + 2 * 20 - 1

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

 Sum of  first  20  odd  numbers :   400
'''

sum=0
for i in range(1,21):
	sum=sum+2*i-1
print("Sum of  first  20  odd  numbers :",sum)



'''
15. Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

 How  many  terms  would  you  like  to  add   :  10
Sum :   55
'''

n=int(input("How  many  terms  would  you  like  to  add"))
sum=0
for i in range(1,n+1):
	sum=sum+i
print("Sum :",sum)