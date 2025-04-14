program1:
How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
#How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for i in range(len(a)):
    print(a[i]) # 0 25 <next line> 1 10.8 <next line> 2 Hyd <next line> 3 True
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
for x in a:
    print(a.index(x), x) #0 25 <next line> 1 10.8 <next line> 2 Hyd <next line> 3 True

program2:
How  to  print  list  elements  in  reverse  order   without  slice
a = eval(input('Enter  list  of  elements : '))
print('Indexed for loop :', a)
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(1,len(a)+1):
    print(a[-i])
# print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
print("we cannot print elements in reverse in a list using for each loop")

program3:
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
1st  list  --->  [10 , 20 , 15 , 18]
2nd  list  --->  [30 , 40 , 35 , 12]
3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]
Hint:  Use  append()  method'''

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
try:
        for i in range(len(a)):
            c.append(a[i]+b[i])

            print('3rd  list : ' , c)
        else:
            print("lengths of 2 lists should be same")
            print("this only works with indexed for loop not for each loop")
except:
    print("enter only lists")

program4:
How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(len(2,5)):
        print(a[i])
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop
# for each loop can iterate whole sequence  but not a part of the sequence
# 5: Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1 # increments each element of list 'a' by 1
print('a :  ' , a) #[11.21.16,19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
    x += 1 # incerement 'x' but not elements of list b
    print(x)
print('b :  ' ,  b) # [10,20,15,18]


program5:
Write  a  program  to  print  first  20  even  numbers  with  while  loop
print("first  20  even  numbers: ")
i=1
while i<21:
    print(2*i)
    i+=1
print("Bye")

program6:
 Write  a  program  to  print  first  20  odd  numbers  with  while  loop
print("first  20  odd  numbers: ")
i=1
while i<21:
    print((2*i)-1)
    i+=1
print("Bye")

prohram7:
 Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n
n=int(input("Enter value of n :"))
i=1
print("Natural  Numbers ")
while i<=n :
    print(i)
    i+=1
print("Bye")

program8:
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1
for i in range(10,0,-1):
    print(i) 
i=10
'''while i>0:
    print(i)
    i-=1 '''

program9:
# Write  a  program  to  print  upper  and  lower  case  alphabets
for i in range(65,91):
    print(chr(i), end=" ")
for j in range(97,123):
    print(chr(j), end=" ")

program10:
 Write  a  program  to  print  first  'n'  terms  of  fibonacci  series
n=int(input("Enter number of terms :"))
print("fibonacci series:")
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c

program11:
Write  a  program  to  search  for  'x'  in  fibonacci  series

x = int(input("Enter value to be searched: "))
if x == 0:
    print("Found")
else:
	a=0
	b=1
	c=a+b
	while c<= x:
		if c== x:
			print("Found")
			exit()
			a=b
			b=c
			c=a+b
			print('Not Found')

program12:
 Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms
n=int(input("Enter number of terms :"))
sum=0
for i in range(1,n+1):
    sum=sum+(1.1 * i)

print(sum)

program13:
Write  a  program  to  determine  sum  of  first  20  even  numbers
print("Sum  of  first  20  even  number: ", end=" ")
sum=0
for i in range(21):
    sum+=i*2
print(sum)

program14:
Write  a  program  to  determine  sum  of  first  20  Odd  numbers
print("Sum  of  first  20  Odd  number: ", end=" ")
sum=0
for i in range(1,21):
    sum+=2*i-1
print(sum)

program15:
 Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
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
'''if():
	print('Hyd')
	continue # error continue used in loops
	print('Sec') '''


# Find outputs (Home  work)
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
'''if(10 , 20 , 30):
	print('Hyd')
	break #break is only valid inside loops (like for or while)
	print('Sec') '''

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass # pass is an empty statement
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

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit() # stops program execution
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
3
