'''#clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)      # [10 , 20 , 15 , 18]
list . clear()
print(list)      # []  '''

'''# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)       # [10 , 20 , 15 , 18]
a . reverse()
print(a)       # [18 , 15 , 20 , 10] '''


'''#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)      #  [10 , 20 , 15 , 18 , 5]
list . sort()    #  [5 , 10 , 15 , 18 , 20]
print(list)		 #  [5 , 10 , 15 , 18 , 20]
list . sort(reverse = True)  #  [20 , 18 , 15 , 10 , 5]
print(list)   #  #  [20 , 18 , 15 , 10 , 5]   '''


'''# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)    #  ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()  #  ['Amar' , 'Kiran' , 'Rajesh' , 'Rama' , 'Rama Rao' , 'Sita' , 'Vamsi']
print(a)     #  ['Amar' , 'Kiran' , 'Rajesh' , 'Rama' , 'Rama Rao' , 'Sita' , 'Vamsi']
a . sort(reverse = True)   # ['Vamsi' , 'Sita' , 'Rama Rao' , 'Rama' , 'Rajesh' , 'Kiran' , 'Amar']
print(a)    # ['Vamsi' , 'Sita' , 'Rama Rao' , 'Rama' , 'Rajesh' , 'Kiran' , 'Amar']  '''


'''# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort()  # error due not supported for 'float' and 'str' '''


'''#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))  #  2
print(a . count(25))  #  0
print(len(a))         #  9  '''


'''Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]
Hint:  Use  count()  and  append()  methods

a= [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
b=[]
for x in a:
    c=a.count(x)
    if c==1:
       b.append(x)
print(b)  '''


'''# index()  method  demo  program  (Home  work)

try:
	a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
	i = a.index(15)
	while True:
		print(i)
		i = a.index(15, i+1)
except:
    print(f'{15} is found {a.count(15)}')  '''


'''Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise
First  list :  [2,3,4]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->  True  becoz  elements  2,3,4   are   in  [2,2,3,4,5]
 First  list :  [2,4,4]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->	False  becoz   elements  2,4,4  are  not  in  [2,2,3,4,5]


list1=eval(input("list1 : "))
list2=eval(input("list2 : "))
index=0
for x in list1:
    if x in list2[index:]:
        index=list2.index(x,index) + 1
    else:
        print(False)
        break
else:
    print(True)

	'''

'''# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()     # copy the list of a to b to form new list  i.e [10 , 20 , 15 , 18]
print(b)         # [10 , 20 , 15 , 18]
print(a  is  b)  #  False
print(a  ==  b)  #  True
c = a[:]          # copy the list of a to b to form new list  i.e [10 , 20 , 15 , 18]
print(c)         # [10 , 20 , 15 , 18]
print(a  is  c)  # False
print(a  ==  c)  # True
d = a            #  d points to the same list where a points the list 
print(d)         # [10 , 20 , 15 , 18]
print(a  is  d)  #  True
print(a  ==  d)   #  True'''


'''Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

list=eval(input('Enter any list : '))
c=list.count(list[0])
length=len(list)
if c==length:
    print("All  the  list  elements  are  identical")
else:
    print("List   elements  are  not  identical")  '''


'''Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]  

list=eval(input('Enter any list : '))
a=int(input('enter value : '))
b=list.count(a)
for x in range(b):
    list.remove(a)
print(list)       '''



'''Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list

list=eval(input('Enter list : '))
c=[]
for x in list:
    count=list.count(x)
    c.append((count,x))
print(f'mode : {max(c)[1]}')   '''



'''#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)       #  [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))  #  3
print(a[0])  #    print  1st  inner  list  i.e [10 , 20 , 30 ,  40] 
print(a[1])   #  to  print  2nd  inner  list i.e  [50 , 60 ,  70 , 80]
print(a[2])  #  to  print  3rd  inner  list  i.e  [90 , 100 , 110 , 120] 
print(a[0][2])  #to  print  30
print(a[1][3]) #  print  80
print(a[2][2])  #  print  100 '''


'''#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])  #print  1st   inner  list   #  [10 , 20]
print(a[1])  # print  2nd   inner  list  #   [30 , 40 , 50] 
print(a[2])  # print  3rd   inner  list)  #  [60 , 70 , 80 , 90]
print(len(a[0]))   # print  number  of  elements  in  1st  inner  list i.e 2
print(len(a[1]))   #  print  number  of  elements  in  2nd  inner  list i.e 3
print(len(a[2]))   # print  number  of  elements  in  3rd  inner  list i.e 4  '''


'''#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)
print('Each  inner  list   of   outer  list  without  indexes')
for x in a:
	print(x)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for x in a:
	for y in x:
		print(y,end=' ')
	print()
print('Elements  in  the  form   of  matrix  using  indexes')
for x in a:
	for i in range(len(x)):
		print(x[i],end=' ')
	print()  '''


'''a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)   # [10 , 20] nextline [30 , 40] nextline  [50 , 60] nextline [70 , 80]
print()        # empty
for  x , y  in  a:
	print(x , y , sep = '...')   #   10 ... 20 nextline 30 ... 40 nextline  50 ... 60 nextline 70 ... 80  '''



'''a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)    #  [10 , 20 , 30] nextline [40 , 50 , 60] nextline [70 , 80 , 90]]
print()         #  empty
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')    #  10 ... 20 ... 30 nextline 40 ... 50 ... 60 nextline 70 ... 80 ... 90  '''


'''#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)     #  [10 , 20] nextline [30 , 40 , 50] nextline [60 , 70 , 80 , 90]
for  x , y  in  a:   #  error
	print(x , y ,	sep = '...')  '''
	

'''#  Find  outputs  (Home  work)
a = [[1,2,3,4]]
print(a[0])  # print inner list
print(*a)    # print inner list  '''


'''#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))   #  [[5 , 'Amar'  ,5000.0] , [10 , 'Rama' , 1000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [20 , 'Sita' , 2000.0]]
print(sorted(a , reverse = True))  #  [[20 , 'Sita' , 2000.0] , [18 , 'Kiran' , 2800.0] , [15 , 'Rajesh' , 3500.0] ,  [10 , 'Rama' , 1000.0] ,[5 , 'Amar'  ,5000.0]]
print(a)   #  [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]  '''


'''# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)

a=[i**3 for i in range(2,11,2)]
print(a)

# or

n=int(input("value : "))
a=[i**3 for i in range(2,n+1,2)]
print(a)  '''


'''Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  --->  ['H' , 'P' , 'C' , 'V']   
try:
	a=eval(input("enter only list of string elements : "))
	b=[]
	for x in a:
		c=x.upper()
		b.append(c[0])
	print(b)
except:
	print("Enter only str elements only")

# withcomprehension
try:
	a=eval(input("enter only list of string elements : "))
	b=[x[0].upper() for x in a]
	print(b)
except:
	print("list contains string elements only") '''


'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

Hint:  Use  split() , upper() , len()

a=input("enter the sentance : ").split()
b=[]
for x in a:
	e=x.upper()
	l=len(x)
	b.append([e,l])
print(b)

#withcomperhension

a=input("enter the sentance : ").split()
b=[[x.upper(),len(x)] for x in a]
print(b)  

'''


'''Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]

try:
	a=eval(input("input1 : "))
	b=eval(input("input2: "))
	c=[]
	min=min(len(a),len(b))
	for i in range(min):
		c.append(a[i]+b[i])
	print(f'output : {c}')
except:
	print("List contains only intergers")

#withcomperhension
try:
	a = eval(input("input1: "))
	b = eval(input("input2: "))
	c = [a[i] + b[i] for i in range(min(len(a), len(b)))]
	print(f'output : {c}')
except:
	print("list contains integers only) 
'''

'''Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

a=int(input())
b=int(input())
c=[]
for x in range(a):
    c.append([0]*b)
print(c)

#withcomperhension

a=int(input())
b=int(input())
c=[[0]*b for x in range(a)]
print(c)
'''

'''Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  ---> [20 , 18 ,  32] 
try:
	a=eval(input('enter list : '))
	b=eval(input('enter list : '))
	c=[]
	for x in a:
		if x not in b:
			c.append(x)
	print(c)
except:
	print('list of elements only')

#withcomperhension

try:
	a=eval(input('enter list : '))
	b=eval(input('enter list : '))
	c=[x for x in a if x not in b]
	print(c)
except:
	print('list of elements')
'''

'''#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

a=[i for i in range(1,21) if i%2==0]
print(a)

#without using if

a=[i for i in range(2,21,2)]
print(a)

#withoutcomperhension

a=[]
for i in range(2,21,2):
    a.append(i)
print(a)
'''

'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

# withcomperhension using if condition

a=[i*2 for i in range(1,21) if i*2%2==0]
print(a)

# withcomperhension without using if condition

a=[i**2 for i in range(2,21,2)]
print(a)

# withoutcomperhension

a=[]
for i in range(1,21):
    b=i**2
    if b%2==0:
        a.append(b)
print(a)
'''

'''Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

d=[]
a=eval(input("enter list1:"))
b=eval(input("enter list2:"))
for i in range(len(a)):
    for j in range(len(b)):
        c=a[i]+b[j]
        d.append(c)
print(d)

#withcomperhension

a=eval(input("enter list1:"))
b=eval(input("enter list2:"))
d=[a[i]+b[j]  for i in range(len(a)) for j in range(len(b))]
print(d)'''


'''Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

a=input("string1:")
b=input("string2:")
d=[a[i]+b[j]  for i in range(len(a)) for j in range(len(b))]
print(d)

#without comperhension
d=[]
a=input("string1:")
b=input("string2:")
for i in range(len(a)):
    for j in range(len(b)):
        c=a[i]+b[j]
        d.append(c)
print(d)
'''
