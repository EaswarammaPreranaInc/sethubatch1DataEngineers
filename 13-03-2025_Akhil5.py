'''#1 clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)
list . clear()
print(list)

[10, 20, 15, 18]
[]

#2 reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)
a . reverse()
print(a)

[10, 20, 15, 18]
[18, 15, 20, 10]

#3 sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)
list . sort()
print(list)
list . sort(reverse = True)
print(list)

[10, 20, 15, 18, 5]
[5, 10, 15, 18, 20]
[20, 18, 15, 10, 5]

#4 Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)
a . sort()
print(a)
a . sort(reverse = True)
print(a)

['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

#5 Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort()

TypeError

#6 count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))
print(a . count(25))
print(len(a))

3
0
9

#7 Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
l=eval(input('Enter a list : '))
e=[]
for x in l:
	if l.count(x)==1:
		e.append(x)
print(e)

Enter a list : 10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19
[15, 14, 18, 19]

#8 index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')

2
5
8
15  is  found  3  times

#9 Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not. Print  True  if  it  is  a  sublist  and  False  otherwise
a=eval(input('Enter 1st list : '))
b=eval(input('Enter 2nd list : '))
s = 0 
sublist = True  
for i in a:
    try:
        s = b.index(i, s) 
    except ValueError:
        sublist = False  
        break
    s += 1  
print(sublist)

Enter 1st list : 2,3,4
Enter 2nd list : 1,2,2,3,3,4,4,5
True

#10 copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b)
c = a[:]
print(c)
print(a  is  c)
print(a  ==  c)
d = a
print(d)
print(a  is  d)
print(a  ==  d)

[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
True
True

#11 Write  a  program  to  determine  all  the  list  elements  are  identical  or  not
l=eval(input('Enter a list : '))
if l.count(l[0])== len(l):
	print('All  the  elements  are  identical')
else:
	print('All  the  elements  are  not  identical')
	print(f'No of elements in string = {len(l)}')
	print(f'No of times first element repeated = {l.count(l[0])}')

Enter a list : 5,5,5,5,8,5,58,8
All  the  elements  are  not  identical
No of elements in string = 8
No of times first element repeated = 5

#12 Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list, Hint: Use  remove()  method

try:
    l = [10, 20, 15, 18, 19, 15, 17, 20, 15, 14]
    x = int(input('Enter the number to be deleted: '))

    if x in l:
        while x in l:
            l.remove(x)
        print('Updated list:', l)
    else:
        print('Number not in the list')

except ValueError: 
    print("Invalid input! Please enter an integer.")
	
Enter the number to be deleted: 15
Updated list: [10, 20, 18, 19, 17, 20, 14]

#13 Write  a  program  to  determine  mode
l=eval(input('Enter a list : '))
a=[]
for x in l:
	f=(l.count(x))
	a.append([f,x])
print(f'[frequency,mode] = {max(a)}')

Enter a list : 10,20,15,18,10,20,15,10,20,19,10
[frequency,mode] = [4, 10]

#14 Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[0][2])
print(a[1][3])
print(a[2][1])

[[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
3
[10, 20, 30, 40]
[50, 60, 70, 80]
[90, 100, 110, 120]
30
80
100

#15 Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])
print(a[1])
print(a[2])
print(len(a[0]))
print(len(a[1]))
print(len(a[2]))

[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
2
3
4

#16 How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print(a)
for x in a:
	print(x,end=', ')
print()
for x in a:
	for y in x:
		print(y,end=', ')
print()
for x in a:
	for y in x:
		print(y,end=' ')
	print()

[[10, 20], [30, 40, 50], [60, 70, 80, 90]]
[10, 20], [30, 40, 50], [60, 70, 80, 90],
10, 20, 30, 40, 50, 60, 70, 80, 90,
10 20
30 40 50
60 70 80 90

#17 Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')

[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80

#18 Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')

[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90

#19 Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x  in  a:
	for y in x:
		print(y, end= '...')
	print()

[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
10...20...
30...40...50...
60...70...80...90...

#20 Find  outputs  (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(f'{a[0]},{a[1]},{a[2]}')
for x in a:
	print(x, end=',')

[10, 20],[30, 40, 50],[60, 70, 80, 90]
[10, 20],[30, 40, 50],[60, 70, 80, 90]

#21 Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))
print(sorted(a , reverse = True))
print(a)

[[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
[[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]

#22 Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
l=[(x*2)**3 for x in range(1,6)]
print(l)

[8, 64, 216, 512, 1000]

#23 Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
l=['hyd' , 'pune' , 'chennai' , 'vijayawada']
a=[]
for x in l:
	b=x.upper()
	a.append(b[0])
print(a)

['H', 'P', 'C', 'V']

#24 Using comprehnsion
l=['hyd' , 'pune' , 'chennai' , 'vijayawada']
a=[x.upper()[0] for x in l]
print(a)

['H', 'P', 'C', 'V']

#25 Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list (word  should  be  in  capital  letters)  without  comprehension
#Let  input  be   hyd  is  green  city, What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]], Hint:  Use  split() , upper() , len()

s='hyd  is  green  city'
a=[]
b=s.split()
for x in b:
	c=x.upper()
	a.append([c,len(x)])
print(a)

[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]

#26 Using comprehnsion
s='hyd  is  green  city'
a=[[x.upper(), len(x)] for x in s.split()]
print(a)

[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]

#27 Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension
#Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
# What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]

a=[10 , 20 , 30 , 40 , 50 , 60 , 70]
b=[100 , 200 , 300 , 400]
c=[]
for x in range(min(len(a),len(b))):
	c.append(a[x]+b[x])
print(c)

[110, 220, 330, 440]

#28 Using comprehnsion
a=[10 , 20 , 30 , 40 , 50 , 60 , 70]
b=[100 , 200 , 300 , 400]
c=[ a[x]+b[x] for x in range(min(len(a),len(b)))]
print(c)

[110, 220, 330, 440] 

#29 Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension Let inputs  be  3  and  4
# What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]] Hint:  Use  repetition  operator  *
a=int(input('How  many  lists  ?  :  '))
b=int(input('How  many  elements  in  each  list ?  :  '))
m=[[0]*b]*a
print(m)

How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

#30 Using comprehnsion
a=int(input('How  many  lists  ?  :  '))
b=int(input('How  many  elements  in  each  list ?  :  '))
c=[ [0]*b for x in range(a)]
print(c)

How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

#31 Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
#Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15] What  is  the  output ?  ---> [20 , 18 ,  32]
#Hint:  for  loop , if  cond , not  in  operator

a=[10 , 20 , 15 , 18 , 25 , 32]
b=[30 , 40 , 10 , 25 , 15]
c=[]
for x in a:
	if x not in b:
		c.append(x)
print(c)

[20, 18, 32]

#32 Using comprehnsion
a=[10 , 20 , 15 , 18 , 25 , 32]
b=[30 , 40 , 10 , 25 , 15]
c=[x for x in a if x not in b]
print(c)

[20, 18, 32]

#33  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
a=[ x for x in range(1,21) if x%2==0]
print(a)

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#34 Repeat  previous  program  with  comprehension  and  without  using  if
n=int(input('Enter a positive integer : '))
a=[x*2 for x in range(1,(n//2)+1)]
print(a)

Enter a positive integer : 20
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#35 Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
a=[ x**2 for x in range(1,21) if x%2==0]
print(a)

[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

#36  Repeat  previous  program  with  comprehension  and  without  using  if
n=int(input('Enter a positive integer : '))
a=[(x*2)**2 for x in range(1,(n//2)+1)]
print(a)

Enter a positive integer : 20
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''
#37 Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
# Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]What  is  the  result ?  --->
# [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32] , Hint : Nested  for  loops
'''
a= [10 , 20 , 15]
b= [30 , 40 , 35 , 32]
c=[]
for x in a:
	for y in b:
		c.append(x+y)
print(c)

[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]

#38 Using comprehension
a= [10 , 20 , 15]
b= [30 , 40 , 35 , 32]
c=[x+y for x in a for y in b]
print(c)
[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]

#39 Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
# Let  1st string  be  HYD  and   2nd string  be   PUNE, What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']
a= 'HYD'
b= 'PUNE'
c=[x+y for x in a for y in b]
print(c)

['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']

#40 Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
# Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]], What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
l=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
a=[]
for x in l:
	for y in x:
		a.append(y)
print(a)

[10, 20, 30, 40, 50, 60, 70, 80, 90]

#41 Using comprehension
l=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
a=[y for x in l for y in x]
print(a)

[10, 20, 30, 40, 50, 60, 70, 80, 90]

#42 Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)

[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

#43 Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)

[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

#44 

Normal  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

1) b = ['S', 'A' , 'Z' , 'K']

2) c = []

3) Iteartion  1 :  d  =  ['Swathi' , 'Srinivas']
                           c =  [['Swathi' , 'Srinivas']]

4) Iteartion  2 :  d  =  ['Anand' , 'Amar']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]

5) Iteartion  3 :  d  =  ['Zebra']
                            c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]

6) Iteartion  4 :  d  =  ['King']
                            c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

a=eval(input('Enter the list of strings : '))
b=['S', 'A' , 'Z' , 'K']
c=[]
for ch in b:
	d=[]
	for n in a:
		if n.startswith(ch):
			d.append(n)
	if d:
		c.append(d)
print(c)

[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]'''

#45
'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint :  Unsorted  lists  can  not  be  merged
'''
a=eval(input('Enter 1st list : '))
b=eval(input('Enter 2nd list : '))
i,j=0,0
c=[]
while (i<len(a) and j<len(b)):
	if a[i]<b[j]:
		c.append(a[i])
		i+=1
	else:
		c.append(b[j])
		j+=1
c+=a[i:]
c+=b[j:]
print(c)



