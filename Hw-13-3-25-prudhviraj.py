# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)                #[10,20,15,18]
list . clear()             
print(list)                #[]


# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)                 #[10,20,15,18]
a . reverse()
print(a)                 #[18,15,20,10]

#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)                    #[10,20,15,18,5]
list . sort()      
print(list)                    #[5,10,15,18,20]
list . sort(reverse = True)    
print(list)                    #[20,18,15,10,5]


# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)            #['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()          
print(a)            #['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a)            #['vamshi','Sita','Rama Rao','Rajesh','Kiran','Amar']

# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort()  #Error due different types of objects in list cannot be sorted


#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))     #3
print(a . count(25))     #0
print(len(a))            #9


#Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
#Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
#What  is  the  output ?  ---> [15 , 14 , 18 , 19]
a=eval((input("Enter the List: ")))
b=[]
for i in a:
	if a.count(i)==1:
		b.append(i)
print(b)
'''
Output:
Enter the List:  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
[15, 14, 18, 19]
'''


# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)           #[10 , 20 , 15 , 18]
print(a  is  b)    #False
print(a  ==  b)    #True
c = a[:]           
print(c)           #[10 , 20 , 15 , 18]
print(a  is  c)    #False
print(a  ==  c)    #True
d = a
print(d)           #[10 , 20 , 15 , 18]
print(a  is  d)    #True
print(a  ==  d)    #True

#Write  a  program  to  determine  all  the  list  elements  are  identical  or  not
try:
	a=eval(input("Enter the List: "))
	b=len(a)
	for i in a:
		c=a.count(i)
	if b==c:
		print("All  the  elements  are  identical")
	else:
		print("All  the  elements  are  not  identical")
except:
	print("Enter List only")
'''
Output:
Enter the List: [25 , 25 , 25 , 25]
All  the  elements  are  identical

Enter the List: [10 , 10 , 20 ,  10]
All  the  elements  are  not  identical

Enter the List: prudhvi
Enter List only
'''

#Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

#Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
#2nd  input  be  15
#What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

try:
	a=eval(input("Enter the List: "))
	b=eval(input("Enter the number to remove: "))
	while b in a:
		a.remove(b)
	print(a)
except:
	print("Enter List Only")

"""
Output:
Enter the List: [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
Enter the number to remove: 15
[10, 20, 18, 19, 17, 20, 14]


Enter the List: prudhvi
Enter List Only
"""


#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
print(a[0])                   #How  to  print  1st  inner  list)
print(a[1])                   #How  to  print  2nd  inner  list)
print(a[2])                   #How  to  print  3rd  inner  list)
print(a[0][2])                #How  to  print  30)
print(a[1][3])                #How  to  print  80)
print(a[2][1])                #How  to  print  100)



"""
Output:
[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
3
[10, 20, 30, 40]
[50, 60, 70, 80]
[90, 100, 110, 120]
30
80
100
"""


#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])                #How  to  print  1st   inner  list
print(a[1])                #How  to  print  2nd   inner  list
print(a[2])                #How  to  print  3rd   inner  list
print(*a[0])               #How  to  print  number  of  elements  in  1st  inner  list
print(*a[1])               #How  to  print  number  of  elements  in  2nd  inner  list
print(*a[2])               #How  to  print  number  of  elements  in  3rd  inner  list


"""
Output:
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
10 20
30 40 50
60 70 80 90
"""


#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')

"""
Output:
[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80
"""


#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')


"""
Output:
[10,20,30]
[40,50,60]
[70,80,90]

10...20...30
40...50...60
70...80...90
"""


#  Find  outputs  (Home  work)
a = [[]]
print(a[0])                            #How  to  print  inner  list
print(a[0][0])                         #How  to  print  inner  list  in  another  way


#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))
print(sorted(a , reverse = True))
print(a)

"""
Output:
[[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
[[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
"""


#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)
print('Each  inner  list   of   outer  list  without  indexes')
for i in a:
	print(i)
print()
print('Elements  in  the  form   of  matrix   without  using  indexes')
for i in a:
	print(*i)
print()
print('Elements  in  the  form   of  matrix  using  indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
"""
Output:
Nested list  with  print function
[[10, 20], [30, 40, 50], [60, 70, 80, 90]]
Each  inner  list   of   outer  list  without  indexes
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]

Elements  in  the  form   of  matrix   without  using  indexes
10 20
30 40 50
60 70 80 90

Elements  in  the  form   of  matrix  using  indexes
10 20
30 40 50
60 70 80 90
"""
# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
a=[x**3 for x in range(2,11,2)]
print(a)

"""
Output:
[8, 64, 216, 512, 1000]
"""


#Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
#Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
#What  is  the  output ?  --->  ['H' , 'P' , 'C' , 'V']
a=eval(input("Enter the the List: "))
b=[]
for i in a:
	#print(i[0].upper())
	b.append(i[0].upper())
print(b)
"""
Output:
Enter the the List: ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
"""

#Repeat   previous  program  with  comprehension
#Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
#Output :  ['H' , 'P' , 'C' , 'V']

a=eval(input("Enter the List: "))
print([i[0].upper() for i in a])
"""
Output:
Enter the List: ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
"""


#Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
#Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
#What  is  the  output ?  ---> [20 , 18 ,  32]
#Hint:  for  loop , if  cond , not  in  operator

a=eval(input("Enter the First List: "))
b=eval(input("Enter the Second List: "))
c=[]
for i in a:
	if i not in b:
		c.append(i)
print(c)


"""
Output:
Enter the First List: [10 , 20 , 15 , 18 , 25 , 32]
Enter the Second List: [30 , 40 , 10 , 25 , 15]
[20, 18, 32]
"""


#Repeat   previous  program  with  comprehension
#Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
#Input2 :  [30 , 40 , 10 , 25 , 15]
#Output :  [20 , 18 , 32]

a=eval(input("Enter the First List: "))
b=eval(input("Enter the Second List: "))
print([i for i in a if i not in b])
"""
Output:
Enter the First List: [10 , 20 , 15 , 18 , 25 , 32]
Enter the Second List: [30 , 40 , 10 , 25 , 15]
[20, 18, 32]
"""
#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
a=[i for i in range(21) if i%2==0]
print(a)

"""
Output:
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
"""


'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
a=[]
for i in range(2,21):
	if i%2==0:
		a.append(i)
print(a)
"""
Output:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
"""

#Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
#What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]
a=[x**2 for x in range(0,21) if x%2==0]
print(a)
"""
Output:
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
"""

#  Repeat  previous  program  with  comprehension  and  without  using  if
a=[x**2 for x in range(2,21,2)]
print(a)
"""
Output:
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
"""

#Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
#Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
#What  is  the  result ?  --->
#[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
a=eval(input("Enter the First List: "))
b=eval(input("Enter the Second List: "))
c=[]
for i in a:
	for j in b:
		c.append(i+j)
print(c)
"""
Output:
Enter the First List: [10 , 20 , 15]
Enter the Second List: [30 , 40 , 35 , 32]
[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]
"""

#Repeat   previous  program  with  comprehension
#Input1 :  [10 , 20 , 15]
#Input2 :  [30 , 40 , 35 , 32]
#Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
a=eval(input("Enter the First List: "))
b=eval(input("Enter the Second List: "))
c=[(i+j) for i in a for j in b]
print(c)
"""
Output:
Enter the First List: [10 , 20 , 15]
Enter the Second List: [30 , 40 , 35 , 32]
[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]
"""

#Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
#Let  1st string  be  HYD  and   2nd string  be   PUNE
#What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']
a=input("Enter the First string: ")
b=input("Enter the Second string: ")
c=[(i+j) for i in a for j in b]
print(c)
"""
Output:
Enter the First string: HYD
Enter the Second string: PUNE
['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']
"""


#Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
#Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
#What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
a=eval(input("Enter the List: "))
b=[]
for i in a:
	b.extend(i)
print(b)
"""
Output:
Enter the List: [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
"""
#Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
#Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
#What  is  the  output ?  ---> [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
a=eval(input("Enter the List: "))
c=[x for i in a for x in i ]
print(c)
"""
Output:
Enter the List: [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
"""
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)
"""
Output:
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
"""

# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)
"""
Output:
[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
"""

#Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
#Print  True  if  it  is  a  sublist  and  False  otherwise
a=eval(input("First  list: "))
b=eval(input("Second list: "))

A=''
for i in a:
    A+=str(i)
   
B=''
for i in b:
    if i in a:
        B+=str(i)     

if A in B:
    print("True")
    
else:
    print("False")
"""
Output:
First  list:  [2,4,4]
Second list: [2,2,3,4,5]

First  list: [2,4,4]
Second list: [2,2,3,4,5]
False

First  list: [2,4,3]
Second list: [2,2,3,4,5]
False

First  list: [2,2,5]
Second list: [2,2,3,4,5]
True
"""

#Write  a  program  to  determine  mode
#1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list
a=eval(input("Enter  List  : "))
A=[]
for i in a:
    if i not in A:
        A.append(i)
        
F=[]

for i in A:
    F.append(a.count(i))
    
M=max(F)


for i in range(len(F)):
    if(F[i]==M):
        print("Mode:",A[i])
"""
Output:
Enter  List  : [10,20,15,18,10,20,15,10,20,19,10]
Mode: 10
"""

#Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list
a=eval(input("Enter 1st List: "))
b=eval(input("Enter 2nd List: "))
c=a+b 
c.sort()
print(c)
"""
Output:
Enter 1st List: [10  ,  20  , 30   ,  40   ,  50]
Enter 2nd List: [5  ,  12  , 20   ,  37]
[5, 10, 12, 20, 20, 30, 37, 40, 50]
"""

a=['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
L=[]
for i in a:
    if i[0] not in L:
        L.append(i[0])
R=[]
for i in L:
    l=[]
    for j in a:
        if j[0]==i:
            l.append(j)     
    R.append(l) 
print(R)
"""
Output:
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
"""
