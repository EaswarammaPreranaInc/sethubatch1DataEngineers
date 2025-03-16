# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10 , 20 , 15 , 18]
list . clear()
print(list) # []

# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
a . reverse()
print(a) # [18 , 15 , 20 , 10]

#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) # [10 , 20 , 15 , 18 , 5]
list . sort()
print(list) # [5 , 10 , 15 , 18 , 20]
list . sort(reverse = True)
print(list) # [20 , 18 , 15 , 10 , 5]

# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
#a . sort() # Error becoz of 'Hyd' and 10.8 cannot compare because of str and float

#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3  Number of 15's in a list
print(a . count(25)) # 0  No 25 in list a.
print(len(a)) # 9

'''
Gift
Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''
a = [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
print(b)        

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) # [10 , 20 , 15 , 18]
print(a  is  b) # False
print(a  ==  b) # True
c = a[:] 
print(c) # [10 , 20 , 15 , 18]
print(a  is  c) # False
print(a  ==  c) # True
d = a
print(d) # [10 , 20 , 15 , 18]
print(a  is  d) # True
print(a  ==  d) # True

'''
Gift
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
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
# Input lists
a = [2, 3, 4]
b = [2, 2, 3, 4, 5]

try:
    start = 0
    for num in a:
        start = b.index(num, start) + 1
    print(True)
except ValueError:
    print(False)

#o/p: True

# Test case 2
a = [2, 4, 4]
b = [2, 2, 3, 4, 5]

try:
    start = 0
    for num in a:
        start = b.index(num, start) + 1
    print(True)
except ValueError:
    print(False)
#o/p: False    

# Test case 3
a = [2, 4, 3]
b = [2, 2, 3, 4, 5]

try:
    start = 0
    for num in a:
        start = b.index(num, start) + 1
    print(True)
except ValueError:
    print(False)
#o/p: False    

# Test case 4
a = [2, 2, 5]
b = [2, 2, 3, 4, 5]

try:
    start = 0
    for num in a:
        start = b.index(num, start) + 1
    print(True)
except ValueError:
    print(False)
#o/p: True

'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

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

'''a = eval(input('Enter List:'))
print('All elements are ientical' if a.count(a[0]) == len(a) else 'All elements are not identical')
print('Total elements:',len(a))
print('First elements occurs:',a.count(a[0]),'times')'''

'''o/p: Enter List:[25,25,25,25]
        All elements are ientical
        Total elements: 4
        First elements occurs: 4 times
'''
'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

Hint: Use  remove()  method
'''

a = eval(input('Enter list:'))
x = int(input('Enter element to delete:'))
while x in a:
    a.remove(x)
print('Updated list:',a)  

'''o/p: Enter list:[10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
        Enter element to delete:15
        Updated list: [10, 20, 18, 19, 17, 20, 14] '''

'''
Gift
Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list
'''
a = eval(input('Enter a List:'))
mode = a[0]
max_count = a.count(mode)
for i in a:
    if a.count(i)> max_count:
        mode = i
        max_count = a.count(i)
print('Mode:',mode)        

'''o/p: Enter a List:[10,20,15,18,10,20,15,10,20,19,10]
        Mode: 10 '''

#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) # [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) # 3
print(a[0]) #How  to  print  1st  inner  list
print(a[1]) #How  to  print  2nd  inner  list
print(a[2]) #How  to  print  3rd  inner  list
print(a[0][2]) #How  to  print  30
print(a[1][3]) #How  to  print  80
print(a[2][1]) #How  to  print  100

'''o/p: [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
        3
        [10, 20, 30, 40]
        [50, 60, 70, 80]
        [90, 100, 110, 120]
        30
        80
        100 '''


'''
What  is  a  nested  list ?  --->  A  list  in  another  list
'''
#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])#How  to  print  1st   inner  list
print(a[1])#How  to  print  2nd   inner  list
print(a[2])#How  to  print  3rd   inner  list
print(*a[0])#How  to  print  number  of  elements  in  1st  inner  list
print(*a[1])#How  to  print  number  of  elements  in  2nd  inner  list
print(*a[2])#How  to  print  number  of  elements  in  3rd  inner  list



'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')
'''o/p: [10, 20]
        [30, 40]
        [50, 60]
        [70, 80]

        10...20
        30...40
        50...60
        70...80    '''
#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')
'''o/p: [10, 20, 30]
        [40, 50, 60]
        [70, 80, 90]

        10...20...30
        40...50...60
        70...80...90 '''   
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')
'''o/p: [10, 20]
        [10, 20]...80
        [30, 40, 50]
        [30, 40, 50]...80
        [60, 70, 80, 90]
        [60, 70, 80, 90]...80     '''
#  Find  outputs  (Home  work)
a = [[]]
print(a[0])#How  to  print  inner  list
print(*a)#How  to  print  inner  list  in  another  way
#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))
print(sorted(a , reverse = True))
print(a)
'''o/p: [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
        [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
        [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
'''
# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
a = [a**3  for a in [2 , 4 , 6 , 8 , 10]]
print(a)
#o/p: [8, 64, 216, 512, 1000]

'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  --->  ['H' , 'P' , 'C' , 'V']

Hint:  Use  upper()  method
'''
a = ['hyd' , 'pune' , 'chennai' , 'vijayawada']
b = []
for i in a:
    b.append(i[0].upper())
print(b)
#o/p: ['H', 'P', 'C', 'V']

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada'] '''
a = ['hyd' , 'pune' , 'chennai' , 'vijayawada'] 
b = [i[0].upper() for i in a]
print(b)
#o/p: ['H', 'P', 'C', 'V']

'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

Hint:  Use  split() , upper() , len()
'''
a = input('enter a string:')
b = a.split()
c = []
for i in b:
    c.append([i.upper(),len(i)])
print(c)    
#o/p: [['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]

'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

a = [10 , 20 , 30 , 40 , 50 , 60 , 70]
b = [100 , 200 , 300 , 400]
c = []
for i in range(len(b)):
   c.append(a[i] + b[i])
print(c)   

#o/p: [110, 220, 330, 440]

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
a = [10 , 20 , 30 , 40 , 50 , 60 , 70]
b = [100 , 200 , 300 , 400]
c = [a[i]+b[i] for i in range(len(b))]
print(c)

#o/p: [110, 220, 330, 440]

'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''

a = int(input('hw many lists:'))
b = int(input('hw many lists:'))
c = []
for _ in range(a):
    c.append([0]*b)
print(c)    

#o/p: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  ---> [20 , 18 ,  32]

Hint:  for  loop , if  cond , not  in  operator
'''
a = [10 , 20 , 15 , 18 , 25 , 32]
b = [30 , 40 , 10 , 25 , 15]
c = []
for i in a:
    if i not in b:
        c.append(i)
print(c)        
#o/p: [20, 18, 32]

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
a = [10 , 20 , 15 , 18 , 25 , 32]
b = [30 , 40 , 10 , 25 , 15]
c = [i for i in a if i not in b]
print(c)
#o/p: [20, 18, 32]

#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

b = [i for i in range(1,21) if i%2==0]
print('Even no b/w 1 and 20:',b)
#o/p: Even no b/w 1 and 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]
'''
a = [n**2 for n in range(1,21) if n**2%2 ==0]
print(a)
#o/p: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
a = [10 , 20 , 15]
b = [30 , 40 , 35 , 32]
c = []
for x in a:
    for y in b:
      c.append(x+y)
print(c)    

#o/p: [40,50,45,24,50,60,55,52,45,55,50,47]
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
a = [10 , 20 , 15]
b = [30 , 40 , 35 , 32]
c = [x+y for x in a for y in b]
print(c)
#o/p: [40,50,45,24,50,60,55,52,45,55,50,47]
'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a = 'HYD'
b = 'PUNE'
c = []
for i in a:
    for j in b:
        c.append(i+j)
print(c)        
#o/p: ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']

a = 'HYD'
b = 'PUNE'
c = [i+j for i in a for j in b]
print(c)
#o/p: ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']

'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a = [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
c = []
for i in a:
    for j in i:
        c.append(j)
print(c)        

#o/p: [10, 20, 30, 40, 50, 60, 70, 80, 90]
'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  ---> [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a = [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
c = [j for i in a for j in i]
print(c)
#o/p: [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)

'''o/p: [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
        [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]] '''
