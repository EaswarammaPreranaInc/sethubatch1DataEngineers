Q1 # clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . clear()
print(list)  #[]
--------------------------------------------------------------------------------------------
Q2 # reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
a . reverse() 
print(a) #[18,15,20,10]
--------------------------------------------------------------------------------------------
Q3 # sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) #[10 , 20 , 15 , 18 , 5]
list . sort() 
print(list) #[5,10,15,18,20]
list . sort(reverse = True) 
print(list) #[20,18,15,10,5]
------------------------------------------------------------------------------------------------------
Q4 #Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)   #['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a)    #['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a)   #['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
-----------------------------------------------------------------------------------------------------
Q5 #Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort()  #error- cannot sort because of 'Hyd'
------------------------------------------------------------------------------------------------------
Q6 #count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3
print(a . count(25)) #0
print(len(a)) # 9
-----------------------------------------------------------------------------------------------------------
Q7 Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)

a=eval(input('Enter list: '))
b=[]
for x in a:
	if a.count(x)==1:
		b.append(x)
print('List without duplicates: ',b)

OP-Enter list: [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
List without duplicates:  [15, 14, 18, 19]
---------------------------------------------------------------------------------------------------------------
Q8 #index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#    0    1    2     3    4    5    6    7    8    9   10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ') # 2 5 8 , 15 is found 3 times
---------------------------------------------------------------------------------------------------------------------
Q9 Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.

try:
	a=eval(input('Enter 1st list: '))
	b=eval(input('Enter 2nd list: '))
	i=-1
	for x in a:
			i=b.index(x,i+1)
	print('True')
except:
		print('False')

OP-
Enter 1st list: [2,4,3]
Enter 2nd list: [2,2,3,4,5]
False

OP-
Enter 1st list: [2,3,4]
Enter 2nd list: [2,2,3,4,5]
True
---------------------------------------------------------------------------------------------------
Q10 # copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)     #[10 , 20 , 15 , 18]
print(a  is  b) # False
print(a  ==  b) #True
c = a[:]
print(c)        # [10 , 20 , 15 , 18]
print(a  is  c) #False
print(a  ==  c) #True
d = a
print(d)        # [10 , 20 , 15 , 18]
print(a  is  d) #True
print(a  ==  d) #True
---------------------------------------------------------------------------------------------------------
Q11 #Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

a=eval(input('Enter any list : '))
for x in range(len(a)):
	if a.count(a[x])==len(a):
		print('All the list elements are identical')
		break
else:
	print('List elements are not identical')

OP-
Enter  any  list  :  [10,10,20,10]
List   elements  are  not  identical

Enter  any  list  :  [25,25,25.0,25]
All  the  list  elements  are  identical
----------------------------------------------------------------------------------------------------------------
Q12 #Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
Hint: Use  remove()  method

a=eval(input('Enter list : '))
b=int(input('Enter element to be deleted : '))
while b in a:
	a.remove(b)
print(f'List without {b} : {a}')

OP-
Enter List  :  [15,15,15]
Enter  element  to  be  deleted : 15
List  without   15's :  []
-------------------------------------------------------------------------------------------
Q13 #Write  a  program  to  determine  mode

a=eval(input('Enter any list: '))
ctr=0
b=set(a)
for x in b:
	freq=a.count(x)
	if freq>ctr:
		ctr=freq
		mode=x
print('Mode :',mode)

OP-
Enter any list: [10,20,15,18,10,20,15,10,20,19,10]
Mode : 10
----------------------------------------------------------------------------------------------------
Q14 # Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)       #[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))  #3
print(a[0])    #How  to  print  1st  inner  list
print(a[1])    #How  to  print  2nd  inner  list
print(a[2])    #How  to  print  3rd  inner  list
print(a[0][2]) #How  to  print  30
print(a[1][3]) #How  to  print  80
print(a[2][1]) #How  to  print  100
----------------------------------------------------------------------------------------------------------
Q15 #Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print('1st inner list: ',a[0]) #How  to  print  1st   inner  list)
print('2nd inner list: ',a[1]) #How  to  print  2nd   inner  list)
print('3rd inner list: ',a[2]) #How  to  print  3rd   inner  list)
print('len if 1st inner list: ',len(a[0])) #How  to  print  number  of  elements  in  1st  inner  list
print('len of 2nd inner list: ',len(a[1])) #How  to  print  number  of  elements  in  2nd  inner  list
print('len of 3rd inner list: ',len(a[2])) #How  to  print  number  of  elements  in  3rd  inner  list
--------------------------------------------------------------------------------------------------------------
Q16 #How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)
print('Each  inner  list   of   outer  list  without  indexes')
for x in a:
	print(x)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for x in a:
	for y in x:
		print(y,end = ' ')
	print()
print('Elements  in  the  form   of  matrix  using  indexes')
for x in range(len(a)):
	for y in range(len(a[x])):
		print(a[x][y],end=' ')
	print()
--------------------------------------------------------------------------------------------
Q17 #Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')

OP-
[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80
---------------------------------------------------------------------------------------------
Q18 #Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')

OP-
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90
---------------------------------------------------------------------------------------------
Q19 #Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')

OP-
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
10...20
error - because x,y are only two variable and [30,40,50] cannot unpack with only two variables
-------------------------------------------------------------------------------------------------------------------
Q20 #Find  outputs  (Home  work)
a = [[]]
print(a[0]) #How  to  print  inner  list ----> []
print(*a)   # How  to  print  inner  list  in  another  way------>[]
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Q21 #Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))                  # [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True)) #[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)                          #[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Q22 #Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension
[8, 64, 216, 512, 1000]

a = [x**3 for x in range(2,12,2)]
print(a)

OP-
[8, 64, 216, 512, 1000]
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Q23 #Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

a=eval(input('Enter list: '))
b=[]
for x in a:
	b.append(x[0].upper())
print(b)

OP-
Enter list: ['priya','swathi','Tanmai']
['P', 'S', 'T']
------------------------------------------------------------------------------------------------------------------------------------------------------------
Q24 #Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  strings  with list comprehension

a=['hyd' , 'pune' , 'chennai' , 'vijayawada']
b=[x[0].upper() for x in a]
print(b)

OP-['H', 'P', 'C', 'V']
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Q25 #Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

a=input('Enter any string: ')
b=a.split()
c=[]
for x in b:
	c.append([x.upper(),len(x)])
print(c)

OP-
Enter any string: Iam learning python
[['IAM', 3], ['LEARNING', 8], ['PYTHON', 6]]
-----------------------------------------------------------------------------------------------------------------------------------------------------
Q26 #Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list with  comprehension

a=input('Enter any string: ')
b=a.split()
c= [[x.upper(),len(x)] for x in b]
print(c)

OP-
Enter any string: my name is priyanka
[['MY', 2], ['NAME', 4], ['IS', 2], ['PRIYANKA', 8]]
----------------------------------------------------------------------------------------------------------------------------------------------------------
Q27 #Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
c=[]
i=0
while i<=len(a)-1 and i<=len(b)-1:
	c.append(a[i]+b[i])
	i+=1
print('Result: ',c)

OP-
Enter 1st list: [23,1,4,9,10,5.6]
Enter 2nd list: [2.1,3,0.1]
Result:  [25.1, 4, 4.1]
--------------------------------------------------------------------------------------------------------------------------------------------------------
Q28 #Write  a  program  to  add  two  lists  of  unequal  length  with list  comprehension

a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
c=[a[i]+b[i] for i in range(min(len(a),len(b)))]
print(c)

OP-
Enter 1st list: [10,20,30,40]
Enter 2nd list: [11,2,3]
[21, 22, 33]
-----------------------------------------------------------------------------------------------------------------------------------------------------
Q29 #Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

a=int(input('Number of inner lists: '))
b=int(input('Number of elements in each inner list: '))
c=[]
for i in range(a):
	c.append([0]*b)
print(c)

OP-
Number of inner lists: 4
Number of elements in each inner list: 5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
----------------------------------------------------------------------------------------------------------------------------------------------------------
Q30 #Write   a  program  to  initialize  a  nested  list  with  zeroes  with list  comprehension

a=int(input('Number of inner lists: '))
b=int(input('Number of elements in each inner list: '))
c=[[0]*b for i in range(a)]
print(c)

OP-
Number of inner lists: 4
Number of elements in each inner list: 2
[[0, 0], [0, 0], [0, 0], [0, 0]]
------------------------------------------------------------------------------------------------------------------------------------------------------------
Q31 #Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
c=[]
for i in a:
	if i not in b:
		c.append(i)
print('Result: ',c)

OP-
Enter 1st list: [10,4,20,3,30,1]
Enter 2nd list: [1,3,4,7,10]
Result:  [20, 30]
------------------------------------------------------------------------------------------------------------------------------------------------------------
Q32 #Write a program to extract those elements of 1st list which are not in 2nd list with list comprehension

a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
c=[i for i in a if i not in b]
print(c)

OP-
Enter 1st list: [10 , 20 , 15 , 18 , 25 , 32]
Enter 2nd list: [30 , 40 , 10 , 25 , 15]
[20, 18, 32]
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Q33 #Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

a=20
b=[i for i in range(1,21) if i%2==0]
print('Even numbers between 1 and 20: ',b)

OP-
Even numbers between 1 and 20:  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
------------------------------------------------------------------------------------------------------------------------------------------------------------
Q34 #Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension without using if condition

a=int(input('Enter range: '))
b=[i for i in range(2,a+1,2)]
print(f'Even numbers between 1 and {a}: {b}')

OP-
Even numbers between 1 and 20:  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
------------------------------------------------------------------------------------------------------------------------------------------------------------
Q35 #Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

a=int(input('Enter range: '))
b=[i**2 for i in range(1,a+1) if i%2==0]
print(f'Squares of Even numbers between 1 and {a}: {b}')

OP-
Enter range: 20
Squares of Even numbers between 1 and 20: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Q36 #Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension without  using  if

a=int(input('Enter range: '))
b=[i**2 for i in range(2,a+1,2)]
print(f'Squares of Even numbers between 1 and {a}: {b}')

OP-
Enter range: 20
Squares of Even numbers between 1 and 20: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
------------------------------------------------------------------------------------------------------------------------------------------------------------
Q37 #Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
c=[]
for i in a:
	for j in b:
		c.append(i+j)
print(c)

OP-
Enter 1st list: [10,20,15]
Enter 2nd list: [30 , 40 , 35 , 32]
[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Q38 #Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  with list  comprehension

a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
c=[i+j for i in a for j in b]
print(c)

OP-
Enter 1st list: [1,2,3,4]
Enter 2nd list: [1,2]
[2, 3, 3, 4, 4, 5, 5, 6]
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Q39 #Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

a=input('Enter 1st string: ')
b=input('Enter 2nd string: ')
c=[i+j for i in a for j in b]
print(c)

OP-
Enter 1st string: JAVA
Enter 2nd string: PYTHON
['JP', 'JY', 'JT', 'JH', 'JO', 'JN', 'AP', 'AY', 'AT', 'AH', 'AO', 'AN', 'VP', 'VY', 'VT', 'VH', 'VO', 'VN', 'AP', 'AY', 'AT', 'AH', 'AO', 'AN']
------------------------------------------------------------------------------------------------------------------------------------------------------------
Q40 #Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

a=eval(input('Enter nested list: '))
b=[]
for x in a:
	b.extend(x)
print('List: ',b)

OP-
Enter nested list: [[1,2],[3,4,5],[6,7],[8,9,10]]
List:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
---------------------------------------------------------------------------------------------------------------------------------------------------------
Q41# Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

a=eval(input('Enter nested list: '))
b=[x for sublist in a for x in sublist]
print('List: ',b)

OP-
Enter nested list: [[10,3,4,1],[12,18,16]]
List:  [10, 3, 4, 1, 12, 18, 16]
------------------------------------------------------------------------------------------------------------------------------------------------------------
Q42 #Find  outputs
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)

OP-
[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

Q43 #Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)

OP-
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Q44 #Group names by initial letter

a=eval(input('Enter list of strings : '))               #['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
b =eval(input('Enter list of starting letters : '))     #['S', 'A' , 'Z' , 'K']
c = []
for i in range(len(b)):
	g=[]
	for x in a:
		if x[0]==b[i]:
			g.append(x)
	c.append(g)
print('Nested list : 'c)

OP-
Enter list of strings : ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Enter list of starting letters : ['S', 'A' , 'Z' , 'K']
Nested list : [['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
------------------------------------------------------------------------------------------------------------------------------------------------------------
Q45 #Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list

a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
a=sorted(a)
b=sorted(b)
c=[]
i,j=0,0
while i < len(a) and j< len(b):
	if a[i] < b[j]:
		c.append(a[i])
		i+=1		
	else:
		c.append(b[j])
		j+=1
while i<len(a):
	c.append(a[i])
	i+=1
while j < len(b):
	c.append(b[j])
	j+=1
print(c)

OP-
Enter 1st list: [1,3,5,7,9]
Enter 2nd list: [2,4,6,8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
