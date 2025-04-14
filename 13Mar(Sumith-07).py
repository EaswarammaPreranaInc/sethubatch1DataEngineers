'''1
list=[10,20,15,18]
print(list) #[10,20,15,18]
list.clear()
print(list) #[]
'''
'''2
a=[10,20,15,18]
print(a) #[10,20,15,18]
a.reverse() #[18,15,20,10]
print(a) #[18,15,20,10]
'''
'''3
list=[10,20,15,18,5]
print(list) #[10,20,15,18,5]
list.sort() #[5,10,15,18,20]
print(list) #[5,10,15,18,20]
list.sort(reverse = True) #[20,18,15,10,5]
print(list) #[20,18,15,10,5]
'''
'''4
a=['Rama','Rajesh','Amar','Sita','Vamsi','Kiran','Rama Rao']
print(a) #['Rama','Rajesh','Amar','Sita','Vamsi','Kiran','Rama Rao']
a.sort() #[Amar,Kiran,Rajesh,Rama,Rama Rao,Sita,Vamsi]
print(a) #[Amar,Kiran,Rajesh,Rama,Rama Rao,Sita,Vamsi]
a.sort(reverse=True) #[Vamsi,Sita,Rama Rao,Rajesh,Kiran,Amar]
print(a)  #[Vamsi,Sita,Rama Rao,Rajesh,Kiran,Amar]
'''
'''5
a=[25,10.8,'hyd',True] # error due 'hyd' as all are int type
a.sort()
'''
'''6
a=[10,20,15,18,15,12,14,15,19]
print(a.count(15)) #3
print(a.count(25)) #0
print(len(a) )#9
'''
'''7
x = [10,20,10,15,14,20,18,10,19]
i=0
y=[]
while x.count(x[i])==1:
	y.append(x[i])
	i+=1
print(y)
'''
'''8
a=[10,20,15,12,14,15,18,19,15,12,25]
try:
	i=a.index(15)
	while True:
		print(i) #2,5,8
		i=a.index(15,i+1)
except:
	print(F'15 is found at {a.count(15)} times')
'''
'''9
x=eval(input("enter the list"))
if len(x)==x.count((x[0])):
	print("elemnts identical")
else:
	print("elements unidentical")
'''
'''10
x=eval(input("enter the list"))
y=int(input("enter the element"))
while x.count(y)!=0:
	x.remove(y)
print(x)
'''
'''11
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
'''12
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0]) #[10 , 20]
print(a[1])  # [30 , 40 , 50]
print(a[2])  # [60 , 70 , 80 , 90]
print(len(a[0])) #2
print(len(a[1])) #3
print(len(a[2])) #4
'''
'''13
a=[x**3 for x in range(2,12,2)]
print(a)   #[8, 64, 216, 512, 1000]
'''
'''14
a=['hyd','pune','chennai','vijayawada']
y=[]
for x  in range(len(a)):
	y+=(a[x][0]).upper()
print(y)
'''
'''15
a=['hyd','pune','chennai','vijayawada']
y=[(a[x][0]).upper() for x  in range(len(a))]
print(y)
'''
'''16
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
17
a=input("enter the string : ")
x=a.split(" ")
z=[[x[i].upper(),len(x[i])] for i in range(len(x))]
print(z)
'''
'''
18
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
num=min(len(a),len(b))
y=[]
i=0
print(num)
for i in range(num):
	y+=[a[i]+b[i]]
print(y)
'''
'''
19
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
num=min(len(a),len(b))
y=[a[i]+b[i] for i in range(num)]
print(y)
'''
'''20
x=int(input("enter the no of list: "))
y=int(input("enter the no of elemts in list: "))
out=[]
for i in range((x)):
	out=[[0]*y]*x
print(out)
'''
'''21
x=int(input("enter the no of list: "))
y=int(input("enter the no of elemts in list: "))
out=[[[0]*y] for i in range((x))]
print(out)
'''
'''22
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
for x in range(len(a)):
	if a[x] not in b:
		out.append(a[x])
print(out)
'''
'''23
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
out=[(a[x]) for x in range(len(a)) if a[x] not in b]
print(out)
 '''
'''23
a=[i for i in range(1,21) if i%2==0]
print(a)
'''
'''24
a=[i for i in range(2,21,2) ]
print(a)
'''
'''25
a=[i**2 for i in range(1,21) if i%2==0 ]
print(a)
'''
'''26
a=[i**2 for i in range(2,21,2) ]
print(a)
'''
'''27
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
for i in range(len(a)):
	for x in range(len(b)):
		out+=[a[i]+b[x]]
print(out)
'''
'''28
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[a[i]+b[x] for i in range(len(a)) for x in range(len(b))]
print(out)
'''
'''29
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
'''31
a=[[10,20],[30,40,50],[60,70,80,90]]
b=[x for x in a for y in x]
print(b)
 output
 [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
'''
'''32
a=[[j for j in range (i)] for i in range(5)]
print(a)
output
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
'''
'''33
a=[[10,20],[30,40,50],[60,70,80,90]]
print(a)
for x in a:
	print(x)
for x in a:
	for i in x:
		print(i)
'''
'''34
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
'''35
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
'''36
a=[[10,20],[30,40,50],[60,70,80,90]]
for x in a:
	print(x)
print()
for x,y in a:
	print(x,y,sep='...')
'''
'''37
a=[[]]
print(a[0])
print(F'{a[0]}')
'''
'''38
a=[[0,'Rama',1000.0],[20,'Sita',2000.0],[15,'Rajesh',3500.0],[18,'Kiran',2800.0],[5,'Amar',5000.0]]
print(sorted(a))
print(sorted(a,reverse=True))
print(a)
output:
[[0, 'Rama', 1000.0], [5, 'Amar', 5000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [5, 'Amar', 5000.0], [0, 'Rama', 1000.0]]
[[0, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
'''
'''39
a=[[10,20],[30,40,50],[60,70,80,90]]
list=[]
for x in a:
	list.extend(x)
print(list)
'''
'''40
a=[[10,20],[30,40,50],[60,70,80,90]]
list=[list.extend(x) for x in a]
print(list)
'''
'''41
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
a=[10,20,30,40]
b=[5,12,20,37]
a=sorted(a)
b=sorted(b)
c=[a+b]
print(c)





























































































































































































