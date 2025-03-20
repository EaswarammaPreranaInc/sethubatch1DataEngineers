
# 1.clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10,20,15,18]
list . clear() #clears the list 
print(list)#[]



'''
2. clear()  method
------------------
1) What  does  clear()  method  do ?  --->  Removes  all  the  elements  of  the  list  and  list  becomes  empty

2) What  about  remove()  and  pop()  methods  ?  ---> They  remove  single  element  of  the  list
'''
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10,20,15,18]
a . reverse()
print(a)#[18,15,20,10]



'''
3. reverse()  method
---------------------
1) What  does  reverse()  method  do ?  --->  Reverses  elements  of  list

2) Where  are  the  results  stored ?  ---> In  the  same  list  replacing  existing  elements  (List  is  mutable)
'''

# 4.  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) # [10,20,15,18,5]
list . sort()
print(list)# [5,10,15,18,20]
list . sort(reverse = True)
print(list)#[20,18,15,10,5] 

# 5. Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)# ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a)# ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a)# ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

# 6.Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() # not supported b/w Str and Float 

# 7. count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #3
print(a . count(25)) # 0
print(len(a))# 9


'''
What  does  list . count(x)  do ?  ---> Returns  number  of  times  'x'  is  in  the  list
'''

'''
8. Gift
Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''

a=eval(input("Enter a list: "))
c=[]
for x in a:
	b=a.count(x)
	if b==1:
		c.append(x)
print(c)
	
# 9.index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ') 


'''
index()  method
-------------------
1) What  does  index(x)  do ?  --->  Returns  index  of  first  'x'  in  the  list

2) What  does  index(invalid-element)  do  ?  --->  Throws  error

3) list . index(x , i)
    list . index(x)
    What  is  the  difference  between  the  above  two  statements ?  --->
															list . index(x , i)  searches  for  'x'  from   index  'i'  of  the  list  but
															list . index(x)   searches  for  for  'x'  from   index  0  of  the  list

Note:
1) What  are  the  four  search  methods  in  str  class  ---> find() , rfind() , index() , rindex()

2) What  is  the  single  search  method  in  list  class  --->  index()
'''
'''
*
Gift
10.Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [2,3,4]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->  True  becoz  elements  2,3,4   are   in  [2,2,3,4,5]

2) First  list :  [2,4,4]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->	False  becoz   elements  2,4,4  are  not  in  [2,2,3,4,5]

3) First  list :  [2,4,3]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->  False  becoz   elements  2,4,3   are  not  in  [2,2,3,4,5]

4) First  list :  [2,2,5]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  ---> True  becoz   elements  2,2,5    are   in  [2,2,3,4,5]

5) Hint:  Use  index()  method
'''
try:
	a = eval(input("Enter 1st list: "))
	b = eval(input("Enter 2nd list: "))

	i=-1
	for x in a:
		i=b.index(x,i+1)
	print('True')
except:
	print('False')

# 11. copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)#[10,20,15,18]
print(a  is  b)#False
print(a  ==  b)#True
c = a[:]
print(c)#[10,20,15,18]
print(a  is  c)#False
print(a  ==  c)#True
d = a
print(d)#[10,20,15,18
print(a  is  d)#True
print(a  ==  d)#True



'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Copies  elements  of  list  to  another  list  and  returns  the  new  list

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  b = a[:]  
'''

'''
12.Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  ---> All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  --->  4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  ---> All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? ---> 3

3) Hint: Use  len()  and  count()
'''

a = eval(input("Enter a list: "))
b=a.count(a[0])
if len(a) == b:
	print("Identical")
else:
	print("Not Identical")

'''
13.Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

Hint: Use  remove()  method
''' 
a = eval(input("Enter a list: "))
b=int(input("Enter a number: "))
while b in a:
	a.remove(b)
print(a)

'''
*
Gift
14.Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list 
a=eval(input('Enter List : '))
ctr=0
b=set(a)
for x in b:
	freq=a.count(x)
	if freq>ctr:
		ctr=freq
		mode=x
print('Mode: ',mode)

#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)#[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))#3
print(a[0]) #(How  to  print  1st  inner  list)
print (a[1]) #(How  to  print  2nd  inner  list)
print(a[2]) #(How  to  print  3rd  inner  list)
print (a[0][2])#(How  to  print  30)
print(a[1][3]) #(How  to  print  80)
print(a[2][1]) #(How  to  print  100)



'''
What  is  a  nested  list ?  --->  A  list  in  another  list
''' 
# 15. How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print(a) #('Nested list  with  print function')
#print(???)
print(*a) #('Each  inner  list   of   outer  list  without  indexes')

b=[]
for x in a:
	b+=x
print(b) #[10,20,30,40,50,60,70,80,90]
# 16. * How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
for x in a:
	print(x)
#('Elements  in  the  form   of  matrix   without  using  indexes')
#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)

for x in a:
	for y in x:
		print(y,end='\t')
	print()
#('Elements  in  the  form   of  matrix  using  indexes')
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)
for i in range(len(a)):
	for j in range(len(a[i])):
		print(a[i][j], end='\t')
	print()

'''	
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''

# 17. Find  outputs (Home  work) 
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
'''
[10, 20]
[30, 40]
[50, 60]
[70, 80]'''
for  x , y  in  a:
	print(x , y , sep = '...')
'''
10...20
30...40
50...60
70...80 '''

# 18. Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')

'''
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90 '''

# 19. Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
#for  x , y  in  a: #too many values to unpack 
	#print(x , y ,	sep = '...')
'''
[10,20]
[30,40,50]
[60,70,80,90]
10...20
 '''
# 20. Find  outputs  (Home  work)
a = [[]]
print(a[0]) #(How  to  print  inner  list)
print(*a) #(How  to  print  inner  list  in  another  way)

# 21. Find  outputs  (Home  work) 
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))#[[5 , 'Amar'  ,5000.0],[10 , 'Rama' , 1000.0], [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] ,[20 , 'Sita' , 2000.0] ]
print(sorted(a , reverse = True))#[[20 , 'Sita' , 2000.0],[18 , 'Kiran' , 2800.0] [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)# [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ] 

# 22. Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
a=[x**3 for x in range(2,11,2)]
print(a)

'''
(Home  work)
23. Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  --->  ['H' , 'P' , 'C' , 'V']

Hint:  Use  upper()  method
'''
a=eval(input("Enter  a List "))
b=''
for x in a:
	print(x[0].upper()+x[1:])

'''
(Home  work) 
24.Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
a=eval(input("Enter  a List "))
b=[x[0].upper()+x[1:] for x in a]
print(b)

'''
25. Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

Hint:  Use  split() , upper() , len()
'''

a=input("Write a sentence: ")
b=a.split()
print(b)
c=[]
for x in b:
	c.append([x.upper(), len(x)])
print(c)

'''
(Home  work)
26. Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
a=input("Write a sentence: ")
b=a.split()
c=[]
[c.append([x.upper(), len(x)]) for x in b]
print(c)
#OR  
a = input("Write a sentence: ")
c = [[x.upper(), len(x)] for x in a.split()]
print(c)

'''
27.Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
''' 
a=eval(input("Enter  a List "))
b=eval(input("Enter  a List "))
c=[]
x=min(len(a),len(b))
for i in range(x):
		c.append(a[i]+b[i])
print(c)

'''
(Home  work)
28.Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
''' 
a=eval(input("Enter  a List "))
b=eval(input("Enter  a List "))
x=min(len(a),len(b))
c=[(a[i]+b[i])for i in range(x)]
print(c)

'''
29. Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
''' 
a=int(input("Enter  no. of nested Lists "))#4
b=int(input("Enter no.of zeros "))#3
c=[]

for  x in range(a):
		c.append([0]*b)
print(c)

'''
(Home  work)
30. Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
a=int(input("Enter  no. of nested Lists "))#4
b=int(input("Enter no.of zeros "))#3
c=[[0]*b for  x in range(a)]
print(c)

'''
31.Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  ---> [20 , 18 ,  32]

Hint:  for  loop , if  cond , not  in  operator
''' 
a=eval(input("Enter  1st List "))
b=eval(input("Enter  2nd List "))
c=[]
for x in a:
	if x not in b:
		c.append(x)
print(c)

'''
(Home  work)
32.Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
a=eval(input("Enter  1st List "))
b=eval(input("Enter  2nd List "))
c=[x for x in a if x not in b]
print(c)

# 33. Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension  
a=[x for x in range(2,21) if x%2==0 ]
print(a)

'''
34.Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
a=[x for x in range(2,21,2)]
print(a)

'''
35.Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]
''' 
a=[x**2 for x in range(1,21) if x%2==0]
print(a)

#  36.Repeat  previous  program  with  comprehension  and  without  using  if
a=[x**2 for x in range(2,21,2)]
print(a)

'''
37.Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
''' 
a=eval(input("Enter 1 st list: "))
b=eval(input("Enter 2 nd list: "))
c=[]
for x in a:
	for y in b:
		c.append(x+y)
print(c)

'''
(Home  work)
38.Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
a=eval(input("Enter 1 st list: "))
b=eval(input("Enter 2 nd list: "))
c=[(x+y) for x in a for y in b]
print(c)
''' 
39.Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
''' ''' 
a=input("Enter 1 string : ")
b=input("Enter 2 string : ")
c=[]
for x in a:
	for y in b:
		c.append(x+y)
print(c)

'''
40.Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90] ''' 
a=eval(input("Enter a nested list: "))
b=[]
for x in a:
	for y in x:
		b.append(y)
print(b)

'''
41.Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  ---> [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a=eval(input("Enter a nested list: "))
b=[y for x in a for y in x]
print(b)
'''
# 42.Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]] 
b = [ x  for  x  in  a  for  y  in  x] # 1st outer loop is evaluated
print(b)


output:
[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
  x                y    Result(x)
 [ 10,20]         10   [10,20]
[10,20]           20    [10,20]
[30,40,50]        30    [30,40,50]
[30,40,50]        40    [30,40,50]
[30,40,50]        50    [30,40,50]
[60,70,80,90]     60    [60,70,80,90]
[60,70,80,90]     70    [60,70,80,90]
[60,70,80,90]     80    [60,70,80,90]
[60,70,80,90]     90    [60,70,80,90] '''

# 43. Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)] # execute outside for loop bcz its nested comprehension
print(a) # [[],[0],[0,1],[0,1,2],[0,1,2,3]]
'''
i    j    
0     []
1     [0]
2     [0,1]
3     [0,1,2]
4     [0,1,2,3]
''' 
'''
45.Normal  program
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
'''

a=eval(input("Enter list of strings: "))
b=[]
for str in a:
	firstchar=str[0]
	if firstchar not in b :
		b.append(firstchar)
	
c=[]
for ch in b:
	d=[]
	for str in a:
		if str.startswith(ch):
			d.append(str)
	c.append(d)
print(c)



'''
46. Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint :  Unsorted  lists  can  not  be  merged
'''  
a=eval(input("Enter 1st sorted list: "))
b=eval(input("Enter 2nd sorted list: "))
a.sort()
b.sort()
c=[]
i=j=0
while i< len(a) and j<len(b):
		if a[i]<b[j]:
			c.append(a[i])
			i+=1
		else:
			c.append(b[j])
			j+=1
c.extend(a[i:])
c.extend(b[j:])
print(c)
