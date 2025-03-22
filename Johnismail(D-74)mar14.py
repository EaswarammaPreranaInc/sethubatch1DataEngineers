'''# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)#[10 , 20 , 15 , 18]
list . clear()
print(list)#[]

# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10 , 20 , 15 , 18]
a . reverse()
print(a)#[18,15,20,10]

#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)#[10 , 20 , 15 , 18 , 5]
list . sort()
print(list)#[5,10,15,18,20]
list . sort(reverse = True)
print(list)#[20,18,15,10,5]

# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)#['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a)#['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita' , 'Vamsi']
a . sort(reverse = True)
print(a)#['vamsi','sita','Rama Rao','Rama',Rajesh','kiran','Amar']

# Identify  error (Home  work)
#a = [25 , 10.8 ,  'Hyd' ,  True]
#a . sort()#TypeError: '<' not supported between instances of 'str' and 'float'

#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))#3
print(a . count(25))#0
print(len(a))#9


Gift
Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods


a=eval(input('enter list values:'))
b=[]
for i in a:
	 if a.count(i)==1:
		  
		  b.append(i)
print(b)

outputs---
enter list values:[10,20,15,10,20,30,18,19]
[15, 30, 18, 19]

# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')

outputs--
2
5
8
15  is  found  3  times

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)##[10,20,15,18]
print(a  is  b)#false
print(a  ==  b)#true
c = a[:]
print(c)##[10,20,15,18]
print(a  is  c)#False
print(a  ==  c)#true
d = a
print(d)##[10,20,15,18]
print(a  is  d)#true
print(a  ==  d)#true

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


a=eval(input("Enter  any  list  : "))#[1,2,1,1]
b=a.count(a[0])#3
c=len(a)#4
if(b!=c):		
		print("List   elements  are  not  identical")
		print('count:',b) 
		print('total elements:',c)
else:

		print("All  the  list  elements  are  identical")
		print('count:',b) 
		print('total elements:',c)

enter list elements:[1,1,1,1]
elements are identical
4
Total elements  are  in  the  list:4
first  element  repeated :4
 
enter list elements:[1,2,1,1]
elements are not identical
4
Total elements  are  in  the  list :4
first  element  repeated :3

Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

Hint: Use  remove()  method


a=eval(input('enter list values:'))#[10,20,30,15,10,10,35]
b=eval(input('enter element to be deleted:'))#[15]
c=[]
i=0
for i in range(len(a)):
		i+=1
		if a.count(i)>1:
				if b in a:
					 a.remove(b)
					 c+=a[i]
print(c)
				 

Gift
Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list
	
a=eval(input('enter list elements:'))#[1,1,12,2]
i=0
for i in range(len(a)):
		if a.count(i)>a.count(a[i+1]):
			print(a[i])


#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)#[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))#3
#print(How  to  print  1st  inner  list)
print(a[0])
#print(How  to  print  2nd  inner  list)
print(a[1])
#print(How  to  print  3rd  inner  list)
print(a[2])
#print(How  to  print  30)
print(a[0][2])
#print(How  to  print  80)
print(a[1][3])
#print(How  to  print  100)
print(a[2][1])

What  is  a  nested  list ?  --->  A  list  in  another  list

#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
#print(How  to  print  1st   inner  list)
print(a[0])
#print(How  to  print  2nd   inner  list)
print(a[1])
#print(How  to  print  3rd   inner  list)
print(a[2])
#print(How  to  print  number  of  elements  in  1st  inner  list)
print(a[0][::])
#print(How  to  print  number  of  elements  in  2nd  inner  list)
print(a[1][::])
#print(How  to  print  number  of  elements  in  3rd  inner  list)			
print(a[2][::])

#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
#print('Nested list  with  print function')
print(a)
#print('Each  inner  list   of   outer  list  without  indexes')

for i in a:
    print(i,end='\n')
    


    
How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')

for i in a:
		print(*i)

How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
#print('Elements  in  the  form   of  matrix  using  indexes')
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)
	         
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
        
    print()

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)#[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]
print()#[10 , 20] 
      # [30 , 40] 
       #[50 , 60] 
       #[70 , 80]
for  x , y  in  a:
	print(x , y , sep = '...') 
10...20
30...40
50...60
70...80	  
 	
#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()#[10 , 20 , 30] 
       #[40 , 50 , 60] 
       #[70 , 80 , 90]
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')
	#10...20...30
	#40...50 ...60
	#70...80...90

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)#[10 , 20] 
	       #[30 , 40 , 50] 
	        #[60 , 70 , 80 , 90]
for  x , y  in  a:
	print(x , y ,	sep = '...')
	# 10...20
	ValueError: too many values to unpack (expected 2)

#  Find  outputs  (Home  work)
a = [[]]
#print(How  to  print  inner  list)
print(a[0])
#print(How  to  print  inner  list  in  another  way)
for i in a:
		print(i)

#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))#[[5 , 'Amar'  ,5000.0] ],[10 , 'Rama' , 1000.0],[15 , 'Rajesh' , 3500.0], [18 , 'Kiran' , 2800.0] ,[20 , 'Sita' , 2000.0]]
print(sorted(a , reverse = True))#[20 , 'Sita' , 2000.0],[18 , 'Kiran' , 2800.0],[15 , 'Rajesh' , 3500.0],[10 , 'Rama' , 1000.0],[5 , 'Amar'  ,5000.0]]
print(a)#[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]

# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
#without comprehension
a=[]
for x in range(0,11,2):
		a.append(x**3)
print(a[1::])

#with comperhension
a=[x**3 for x in range(0,11,2)]
print(a[1:])
#output---
[8, 64, 216, 512, 1000]
[8, 64, 216, 512, 1000]

(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  --->  ['H' , 'P' , 'C' , 'V']

Hint:  Use  upper()  method

a=eval(input('enter any string: '))
b=[]
for i in range(len(a)):
		b.append(a[i][0].upper())
		i+=1
print(b)
outputs---
enter any string: ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']

(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']

a=eval(input('enter any list:'))

print([i[0].upper() for i in a])

output--
enter any list: ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']

Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

Hint:  Use  split() , upper() , len()

a=input('enter any string:').split(' ')#['hyd','is','green']
b=[]
for i in a:
		b.append([i.upper(),len(i)])	
print(f'{b}')

outputs--
enter any string:hyd is
[['HYD', 3], ['IS', 2]]

(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]

a=input('enter any string:').split(' ')
print([[i.upper(),len(i)] for i in a])
output----
enter any string:hyd is green
[['HYD', 3], ['IS', 2], ['GREEN', 5]]


Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]


a=eval(input('enter any first list:'))
b=eval(input('enter any second list:'))
c=[]
i=0
while i<len(a) and i<len(b):
		
		c.append(a[i]+b[i])
		i+=1
print(c)
		
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]


a=eval(input('enter any first list:'))
b=eval(input('enter any second list:'))
c=min(len(a),len(b))

print([a[i]+b[i] for i in range(c)])

outputs---
enter any first list:[1,2,3,4]
enter any second list:[1,2,3]
[2, 4, 6]


Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  ---> [20 , 18 ,  32]

Hint:  for  loop , if  cond , not  in  operator

a=eval(input('enter first list:'))
b=eval(input('enter second list:'))
c=[]
i=0
for i in a:
		if i not in b:
				c.append(i)
				i+=1
print(c)

outputs----				
enter first list: [10 , 20 , 15 , 18 , 25 , 32]
enter second list:[30 , 40 , 10 , 25 , 15]
[20, 18, 32]

(Home  work)
Repeat   previous  program  with  comprehension

a=eval(input('enter first list:'))
b=eval(input('enter second list:'))
c=print([i   for i in a if i not in b])

outputss----
enter first list:[10 , 20 , 15 , 18 , 25 , 32]
enter second list:[30 , 40 , 10 , 25 , 15]
[20, 18, 32]

#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

a=[i for i in range(0,21,2) if i%2==0]

print(f'even numbers between 1 and 20 are:{a[1:]}')

#outputs---
#even numbers between 1 and 20 are:[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

a=[i for i in range(0,21,2)]
print(a[1:])

Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]

b=[i**2 for i in range(0,21,2)  ]
print(b[1:])

#outputs---
#[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


		
