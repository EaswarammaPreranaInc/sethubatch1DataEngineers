#1
# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)#[10 , 20 , 15 , 18]
list . clear()
print(list)#[]

#2
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10 , 20 , 15 , 18]
a . reverse()
print(a)#[18,15,20,10]

#3
#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)#[10 , 20 , 15 , 18 , 5]
list . sort()
print(list)#[5,10,15,18,20]
list . sort(reverse = True)
print(list)#[20,18,15,10,5]

#4
# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)#['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a)#['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a)#['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

#5
# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort()# not support for string and floot

#6
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))#3
print(a . count(25))#0
print(len(a))#9


#7
k=list(map(int,input("enter the elements sep with ,:").split(",")))
print(k)
p=[]
for i in k:
    if k.count(i)==1:
        p.append(i)
print(p)

#8
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')

#9
try:
	a=eval(input("Enter 1st list"))
	b=eval(input("Enter 2nd list"))
	i= b.index(a[0])
	for x in a[1:]:
		i=b.index(x,i+1)
	print("True")
except:
	print("False")


#10
# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)#[10 , 20 , 15 , 18]
print(a  is  b)#False
print(a  ==  b)#True
c = a[:]
print(c)#[10 , 20 , 15 , 18]
print(a  is  c)#False
print(a  ==  c)#True
d = a
print(d)#[10 , 20 , 15 , 18]
print(a  is  d)#True
print(a  ==  d)#True

#11
'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  --->
    How  many  elements  are  in  the  list ?  --->  4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  ---> All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? ---> 3

3) Hint: Use  len()  and  count()
'''
a=list(map(eval,input("enter the list:").split()))

if len(a)== a.count(a[0]):
    print("All  the  elements  are  identical")
print(len(a))
print(a.count(a[0]))


#12
'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10,20,15,18,19,15,17,20,15,14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

Hint: Use  remove()  method
'''

k=list(map(int, input("Enter list elements separated by spaces: ").split(',')))

print(k)
p=int(input("enter the elememt to remove:"))
while p in k:
        k.remove(p)
print(k)

#13
a = eval(input("Enter list"))
b = set(a)  # 10 20 15 18 19
ctr = 0
for i in range(len(a)):  # 0 1 2 3 4
    if a.count(a[i]) > ctr:  # 4>0
        ctr = a.count(a[i])  # 4
        mode = a[i]  # 10
print(mode)

#14
#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)#[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))#3
print(a[0])
print(a[1])
print(a[2])
print(a[0][2])
print(a[1][3])
print(a[2][1])

#15
#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])
print(a[1])
print(a[2])
print(len(a[0]))
print(len(a[1]))
print(len(a[2]))

#16
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)

print('Each  inner  list   of   outer  list  without  indexes')
#How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
for x in a:
	print(x)

print('Elements  in  the  form   of  matrix   without  using  indexes')
#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
for x in a:
	for y in x:
		print(y,end=" ")
	print()

print('Elements  in  the  form   of  matrix  using  indexes')
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)
for i in range(len(a)): #0 1 2
	for j in range(len(a[i])):
		print(a[i][j] , end = '\t')
	print()



#17
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')


#18
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')

#19
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')

#20
a = [[]]
print(a[0])
print(*a)

#21
#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))#[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True))#[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)#[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]

#22
# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)\
cubes = [x**3 for x in range(2,11,2)]
print(cubes)


#23
'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  --->  ['H' , 'P' , 'C' , 'V']

Hint:  Use  upper()  method
'''

k=input("enter the elements:").split(',')
print(k)
p=[]
for i in range(len(k)):
    p.append(k[i][0].upper())
print(p)

#24
'''
(Home  work)
program  with  comprehension

Input :  [hyd,pune,chennai,vijayawada]

Output :  ['H' , 'P' , 'C' , 'V']
'''
k=input("enter the elements:").split(',')
p=[k[i][0].upper() for i in range(len(k))]
print(p)


#25
'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd is green city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

Hint:  Use  split() , upper() , len()
'''
k=input("enter the strings:").split()
print(k)
p=[]
for i in range(len(k)):
    c=[]
    c.append(k[i].upper())
    c.append(len(k[i]))
    p.append(c)
print(p)

#26
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd is green city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
k=input("enter the strings:").split()
p=[[(k[i].upper()),(len(k[i]))] for i in range(len(k))]
print(p)


#27
'''
Write  a  program  to  add  two  lists  of  unequal  length  with comprehension

Let  1st  list  be  [10,20,30,40,50,60,70]  and  2nd  list  be  [100,200,300,400]
What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
k=list(map(int,input("enter the elements in list1:").split(',')))
v=list(map(int,input("enter the elements in list1:").split(',')))
c=[]
if len(k)>len(v):
       for i in range(len(v)):
              l=int(k[i]) + int(v[i])
              c.append(l)
else:
       for i in range(len(k)):
              l=int(k[i]) + int(v[i])
              c.append(l)
print(c)


#28
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10,20,30,40,50,60,70]
Input2 :  [100,200,300,400]
Output :  [110 , 220 , 330 , 440]
'''
k=list(map(int,input("enter the elements in list1:").split(',')))
v=list(map(int,input("enter the elements in list1:").split(',')))
if len(k)>len(v):
    c=[k[i]+v[i] for i in range(len(v))]
else:
    c = [k[i] + v[i] for i in range(len(v))]
print(c)

#29
'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''

k=int(input("enter no of rows:"))
m=int(input("rnter no of coloums:"))
for i in range(k+1):
    l=[[0]*m]*i
print(l)

#30
'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

k=int(input("enter no of rows:"))
m=int(input("rnter no of coloums:"))
x=[[0]*m for i in range(k)]
print(x)

#31
'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10,20,15,18,25,32]  and  2nd  list  be  [30,40,10,25,15]
What  is  the  output ?  ---> [20 , 18 ,  32]

Hint:  for  loop , if  cond , not  in  operator
'''

k=list(map(int,input("enter the elements in list1:").split(',')))
v=list(map(int,input("enter the elements in list1:").split(',')))
c=[]
for i in range(len(k)):
    if k[i] not in v:
        c.append(k[i])
print(c)

#32
'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

k=list(map(int,input("enter the elements in list1:").split(',')))
v=list(map(int,input("enter the elements in list1:").split(',')))
c=[k[i] for i in range(len(k)) if k[i] not in v]
print(c)

#33
#Write a program to print even numbers between 1 and 20 with  comprehension
k=int(input("enter the range:"))
c=[i for i in range(1,k) if i%2==0 ]
print(c)

#34
'''
Write a program to print even numbers between 1 and 20 with  comprehension without  using  if

Output: [Even  numbers  between  1  and  20]
'''

k=int(input("enter the range:"))
c=[i for i in range(2,k+1,2) ]
print(c)

#35
'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]
'''

k=int(input("enter the range:"))
c=[i**2 for i in range(1,k)if(i**2)%2==0]
print(c)

#36
#Repeat  previous  program  with  comprehension  and  without  using  if
k=int(input("enter the range:"))
c=[i**2 for i in range(2,k,2)]
print(c)

#37
'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
10,20,15
30,40,35,32
'''

k=list(map(int,input("enter the elements in list1:").split(',')))
v=list(map(int,input("enter the elements in list1:").split(',')))
c=[]
for i in range(len(k)):
    for j in range(len(v)):
        c.append(k[i]+v[j])
print(c)

#38
'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  with  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
10,20,15
30,40,35,32
'''
k=list(map(int,input("enter the elements in list1:").split(',')))
v=list(map(int,input("enter the elements in list1:").split(',')))
c=[k[i]+v[j] for i in range(len(k)) for j in range(len(v))]
print(c)

#39
'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''

k=input("enter the elements in list1:").upper()
v=input("enter the elements in list2:").upper()
c=[k[i]+v[j] for i in range(len(k)) for j in range(len(v))]
print(c)


#40
'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
c=[]
for i in a:
    for j in i:
        c.append(j)
print(c)

#41
'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  ---> [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
c=[j for i in a for j in i ]
print(c)


#42
# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)#[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

#43
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

#44

a = eval(input("Enter list"))
b = ['S', 'A', 'Z', 'K']
c = []

for x in b:  # S A Z K
    d = []
    for i in range(len(a)):

        if x == a[i][0]:
            d.append(a[i])
    c.append(d)
print(c)

#45
'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list

Eg:  List  'a'   --->  [10,20,30,40,50]   10,20,30,40,50,60,70,80
       List  'b'   --->  [5,12,20,37]   #5,12,20,37,40,45,65,80
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint :  Unsorted  lists  can  not  be  merged
'''

a=list(map(int,input("enter the elements in list1:").split(',')))
b=list(map(int,input("enter the elements in list1:").split(',')))
mergedlist = []
i,j=0,0
while i<len(a) and j<len(b) :
    if a[i]<b[j]:
        mergedlist.append(a[i])#[
        i+=1
    else:
        mergedlist.append(b[j])#[
        j+=1

mergedlist.extend(a[i:])
mergedlist.extend(b[j:])
print(mergedlist)


