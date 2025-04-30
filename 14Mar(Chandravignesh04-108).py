# clear() method  demo program  (Home  work)
'''
list = [10 , 20 , 15 , 18]
print(list) # [10,20,15,18]
list . clear() 
print(list) # []
'''

# reverse()  method  demo  program (Home  work)
'''
a = [10 , 20 , 15 , 18]
print(a) # [10,20,15,18]
a . reverse()
print(a) # [18,15,20,10]
'''

#  sort()  method  demo  program (Home  work)
'''
list = [10 , 20 , 15 , 18 , 5]
print(list) # [10,20,15,18,5]
list . sort()
print(list) # [5,10,15,18,20]
list . sort(reverse = True)
print(list) # [20,18,15,10,5]
'''

# Find  outputs (Home  work)
'''
a = ['Rama','Rajesh','Amar','Sita','Vamsi','Kiran','Rama Rao']
print(a) # ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a.sort()
print(a) # ['Amar' , 'Kiran' , 'Rajesh' ,  'Rama' ,  'Rama Rao' , 'Sita' , 'Vamsi']
a.sort(reverse = True)
print(a) # ['Vamsi' , 'Sita' , 'Ramo Rao' , 'Rama' , 'Rajesh' , 'Kiran' , 'Amar']
'''

# Identify  error (Home  work)
'''
a = [25,10.8,'Hyd',True] # it does not support 'Hyd'
a.sort() 
'''

#  count()  method  demo    program (Home  work)
'''
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3
print(a . count(25)) # 0
print(len(a)) # 9
'''

# Gift

# Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
# Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
# What  is  the  output ?  ---> [15 , 14 , 18 , 19]
# Hint: Use count() and append() methods
'''
a = [10,20,15,10,14,10,18,20,19]
result = []
for x in a:
	if a.count(x) == 1:
		result.append(x)
print(result)
'''

# index()  method  demo  program  (Home  work)
'''
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
# Gift

# Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
# True  if  it  is  a  sublist  and  False  otherwise
'''
a = eval(input('enter the first list : '))
b = eval(input('enter the second list : '))
try:
	i = -1
	for x in a :
		b.index(x,i+1)
	print(True)
except:
	print(False)
'''

# copy()  method  demo program  (Home  work)
'''
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) # [10,20,15,18]
print(a is b) # 
print(a == b) # True
c = a   
print(c)
print(a is c)
print(a == c)
d = a
print(d)
print(a is d)
print(a == d)
'''

'''
x=eval(input("enter the list"))
if len(x)==x.count((x[0])):
	print("elemnts identical")
else:
	print("elements unidentical")
'''

'''
x=eval(input("enter the list: "))
y=int(input("enter the element:"))
while x.count(y)!=0:
	x.remove(y)
print(x)
''' 

'''          
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) #[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))     #3
print(a[0])       #[10 , 20 , 30 ,  40]  
print(a[1])        #[50 , 60 ,  70 , 80]  ,  ]
print(a[2])       # [90 , 100 , 110 , 120]
print(a[0][2])  #30
print(a[1][3])  #80
print(a[2][1])  #100
'''

'''
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0]) #[10 , 20]
print(a[1])  # [30 , 40 , 50]
print(a[2])  # [60 , 70 , 80 , 90]
print(len(a[0])) #2
print(len(a[1])) #3
print(len(a[2])) #4
'''

'''
a=[x**3 for x in range(2,12,2)]
print(a)   #[8, 64, 216, 512, 1000]
'''

'''
a=['hyd','pune','chennai','vijayawada']
y=[]
for x  in range(len(a)):
	y+=(a[x][0]).upper()
print(y)
'''

'''
a=['hyd','pune','chennai','vijayawada','mumbai']
y=[(a[x][0]).upper() for x  in range(len(a))]
print(y)
'''

'''
a=input("enter the string : ")
x=a.split(" ")
y=[]
z=[]
for i in range(len(x)):
	y=[x[i].upper(),len(x[i])]
	z.append(y)
print(z)
'''

'''
a=input("enter the string : ")
x=a.split(" ")
z=[[x[i].upper(),len(x[i])] for i in range(len(x))]
print(z)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
num=min(len(a),len(b))
y=[]
for i in range(num):
	y+=[a[i]+b[i]]
print(y)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
num=min(len(a),len(b))
y=[a[i]+b[i] for i in range(num)]
print(y)
'''

'''
x=int(input("enter the no of list: "))
y=int(input("enter the no of elemts in list: "))
out=[]
for i in range((x)):
	out=[[0]*y]*x
print(out)
'''

'''
x=int(input("enter the no of list: "))
y=int(input("enter the no of elemts in list: "))
out=[[[0]*y] for i in range((x))]
print(out)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
for x in range(len(a)):
	if a[x] not in b:
		out.append(a[x])
print(out)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
out=[(a[x]) for x in range(len(a)) if a[x] not in b]
print(out)
'''

'''
a=[i for i in range(1,21) if i%2==0]
print(a)
'''

'''
a=[i for i in range(2,21,2) ]
print(a)
'''

'''
a=[i**2 for i in range(1,21) if i%2==0 ]
print(a)
'''

'''
a=[i**2 for i in range(2,21,2) ]
print(a)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
for i in range(len(a)):
	for x in range(len(b)):
		out+=[a[i]+b[x]]
print(out)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[a[i]+b[x] for i in range(len(a)) for x in range(len(b))]
print(out)
'''

'''
a=(input("enter the string 1: "))
b=(input("enter the string 2: "))
out=[a[i]+b[x] for i in range(len(a)) for x in range(len(b))]
print(out)
'''

'''
x=(input("enter the list"))
z=[]
for x in (x):
	z.append(x)
print(z)
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
b=[x for x in a for y in x]
print(b)
 output
 [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
'''

'''
a=[[j for j in range (i)] for i in range(5)]
print(a)
output
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
print(a)
for x in a:
	print(x)
for x in a:
	for i in x:
		print(i)
'''

'''
a=[[10,20],[30,40],[50,60],[70,80]]
for x in a:
	print(x)
print()
for x,y in a:
	print(x,y,sep='...')
output
[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80
'''

'''
a=[[10,20,30],[40,50,60],[70,80,90]]
for x in a:
	print(x)
print()
for x,y ,z in a:
	print(x,y,z,sep='...')
output
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
for x in a:
	print(x)
print()
for x,y in a:
	print(x,y,sep='...')
'''

'''
a=[[]]
print(a[0])
print(F'{a[0]}')
'''

'''
a=[[0,'Rama',1000.0],[20,'Sita',2000.0],[15,'Rajesh',3500.0],[18,'Kiran',2800.0],[5,'Amar',5000.0]]
print(sorted(a))
print(sorted(a,reverse=True))
print(a)
output:
[[0, 'Rama', 1000.0], [5, 'Amar', 5000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [5, 'Amar', 5000.0], [0, 'Rama', 1000.0]]
[[0, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
list=[]
for x in a:
	list.extend(x)
print(list)
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
list=[list.extend(x) for x in a]
print(list)
'''

'''
a=[10,20,15,18]
b=a.copy()
print(b)
print(a is b)
print(a == b)
c=a[:]
print(c)
print(a is c)
print(a == c)
d=a
print(d)
print(a is d)
print(a == d)
#output:
[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
True
True
'''

'''
a=eval(input("enter the list:"))
cont=0
b=set(a)
for x in b:
	freq =a.count(x)
	if freq>cont:
		cont =freq
		mode=x
print("mode:",mode)
'''

'''
try:
	a=eval(input("enter the list 1:"))
	b=eval(input("enter the list 2:"))
	i=-1
	for x in a:
		i=b.index(x,i+1)
	print(True)
except:
	print(False)
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
i=0
for i in range(len(a[i])):
	for j in range(len(a[i])):
		print(a[i][j],end='\t')
	print()
'''

'''
a=eval(input("enter the list 1:"))
print("mode:", max(a, key = a.count))
'''

