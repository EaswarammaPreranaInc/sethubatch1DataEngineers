# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for i in range(len(a)):
 print(i)
# How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
for i in range(len(a)):
 print(F'Index : {i} , Element : {a[i]}')
# How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

# Output:
# Indexed for loop
# 0
# 1
# 2
# 3
# For each loop
# Index : 0 , Element : 25
# Index : 1 , Element : 10.8
# Index : 2 , Element : Hyd
# Index : 3 , Element : True

#  How  to  print  list  elements  in  reverse  order   without  slice
a = eval(input('Enter  list  of  elements : '))
print('Indexed for loop')
for i in range(len(a)-1,-1,-1):
 print(str(a[i]))
print()
# How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(len(a)):
 print(str(a[i])[::-1])
print()
# How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable)
for i in a:
 print(str(i)[::-1])
# output:
# Enter  list  of  elements : ['hyd','abc',123]
# Indexed for loop
# 123
# abc
# hyd
#
# dyh
# cba
# 321
#
# dyh
# cba
# 321

'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
d= []
for i in range(len(a)):
 c.append(a[i]+b[i])
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop
for x,y in zip(a,b):
 d.append(x+y)
print(d)

#output:Enter  1st  list  :  [10 , 20 , 15 , 18]
# Enter  2nd  list  :  [30 , 40 , 35 , 12]
# [40, 60, 50, 30]
# 3rd  list :  [40, 60, 50, 30]
# [40, 60, 50, 30]

#  Gift
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1 # adds +1 to each element in the list
print('a :  ' , a) # a :   [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) #b :   [10, 20, 15, 18]

'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers  with  while  loop

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Use  while  loop
'''

i = 1
print("First 20 even numbers")
while i<=20:
 print(2*i)
 i +=1


'''
Write  a  program  to  print  first  20  odd  numbers  with  while  loop

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) In  general, print  what ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
'''
i = 1
print("First 20 Odd numbers")
while i<=20:
 print(2*i-1)
 i +=1


'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

In  general,  print  what ?  --->  Print  'i'  where  'i'  varies  from  1  to  n

Hint:  Use  for  loop
'''
n= int(input("Enter value of n : "))
print(F"First {n} Natural numbers")
for i in range(1,n+1):
 print(i)

'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

In  general, print  what ?  --->  Print  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

Hint:  Use  for  loop
'''
for i in range(10,0,-1):
 print(i)

 '''
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
 '''

 for i in range(65, 90):
  print(chr(i), end="  ")
 print()

 for i in range(97, 123):
  print(chr(i), end=" ", )
 # output:A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y
 # a b c d e f g h i j k l m n o p q r s t u v w x y z

 '''
 Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

 Let  input  be  6
 What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5

 Hint:  Use  for  loop
 '''
 n = int(input("Enter input : "))
 a,b = 0,1
 for x in range(n):
  print(a)
  a, b = b, a + b


'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? ---> Found

3) Do  not  generate  fibonacci  series
'''
x = int(input("Enter value to be searched: "))
a , b = 0, 1
while a<=x:
 if a==x:
  print("Found")
  break
 a, b = b, a + b
else:
 print("Not Found")


'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0 + 1.1 * 1 + 1.1 * 2 + 1.1* 3 +  ......

2) What  is  added  to  sum  in  general ?  ---> 1.1 * i   where  'i'  varies  from  1  to  n
'''
a = eval(input("Enter value : "))
sum = 0
for i in range(1,a+1):
 sum +=1.1*i
print(sum)

'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? ---> 2 * i   where 'i'  varies  from   1  to  20
'''
a = 20
sum = 0
for i in range(1,a+1):
 sum += 2*i
print(sum)

'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + 2 * 1 - 1 + 2 * 2 - 1 + 2 * 3 - 1 +  ... + 2 * 20 - 1

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20
'''
a = 20
sum = 0
for i in range(1,a+1):
 sum += 2*i-1
print(sum)


'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
'''
a = 10
sum = 0
for i in range(1,a+1):
 sum += i
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
#1<nextline>Sec<nextline>Hello<nextline>2<nextline>Sec<nextline>Hello<nextline>3<nextline>4<nextline>Sec<nextline>Hello<nextline>5<nextline>Sec<nextline>Hello<nextline>6<nextline>7<nextline>Sec<nextline>Hello<nextline>Outside Loop

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue #error continue is used only in for and while loops
	print('Sec')

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop') #1<nextline>Sec<nextline>Hello<nextline>2<nextline>Sec<nextline>Hello<nextline>3<nextline>Outside Loop


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break # break is used for only for and while loops
	print('Sec')

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

# output:
# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
# Hyd
# Hello
# 4
# Sec
# Hello
# 5
# Sec
# Hello
# 6
# Hyd
# Hello
# 7
# Sec
# Hello
# Outside loop


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
# #1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
