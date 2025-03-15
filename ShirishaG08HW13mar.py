# clear() method  demo program  (Home  work)
'''
list = [10 , 20 , 15 , 18]
print(list) # [10, 20, 15, 18]
list . clear() # removes all elements from the list
print(list) # Empty list
'''

# reverse()  method  demo  program (Home  work)
'''
a = [10 , 20 , 15 , 18]
print(a) # [10,20, 15, 18]
a . reverse() 
print(a) # [18, 15, 20, 10]
'''

# sort()  method  demo  program (Home  work)
'''
list = [10 , 20 , 15 , 18 , 5]
print(list) # [10, 20, 15, 18, 5]
list . sort() 
print(list)  #[5, 10, 15, 18, 20]
list . sort(reverse = True)
print(list) # [20, 18, 15, 10, 5]
'''

# Find  outputs (Home  work)
'''
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
'''

# Identify  error (Home  work)
'''
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() # as the list containing str and float values it is error
'''

#  count()  method  demo    program (Home  work)
'''
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #3
print(a . count(25)) #0
print(len(a))  #9
'''

#Gift
#Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
'''
l=eval(input('Enter a list: '))
res=[]
for x in l:
	if l.count(x)==1:
		res.append(x)
print(res)

Output:
Enter a list: [10,20,15,10,14,10,18,20,19]
[15, 14, 18, 19]
'''

#index() method demo program
'''
a=[10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]
try:
	i=a.index(15) #2
	while True:
		print(i)  
		i=a.index(15,i+1)
except:
	print(F'15 is found {a.count(15)} times')

Output
2
5
8
15 is found 3 times
'''

#Gift
#Determine first list is a sublist of 2nd list or not
'''
try:
	a=eval(input('Enter first list: '))
	b=eval(input('Enter second list: '))
	i=0
	for x in a:   
		c=b.index(x,i)
		i=c+1
	print('True')
except:
	print('False')

Output
Enter first list: [2,4,3]
Enter second list: [2,2,3,4,5]
False
Enter first list: [2,3,4]
Enter second list: [2,2,3,4,5]
True
'''

#copy() method demo program 
'''
a=[10,20,15,18]
b=a.copy()
print(b)       #[10, 20, 15, 18]
print(a is b)  #False
print(a==b)    #True
c=a[:]
print(c)       #[10, 20, 15, 18]
print(a is c)  #False
print(a == c)  #True
d=a
print(d)       #[10, 20, 15, 18]
print(a is d)  #True
print(a == d)  #True
'''

#Determine all the list elements are identical or not
'''
l=eval(input('Enter any list: '))
if l.count(l[0])==len(l):
	print('All the list elements are identical')
else:
	print('List elements are not identical')

Output
Enter any list: [10,10,10,10]
All the list elements are identical
Enter any list: [10,10,20,10]
List elements are not identical
'''

#Delete 'all' occurences of 'x' from the list
'''
a=eval(input('Enter any list: '))
x=int(input('Enter element to be deleted: '))
while x in a:
	a.remove(x)
print(F"List without {x}'s: {a}")

Output
Enter any list: [10,20,15,20,15,10,25,30,15,12]
Enter element to be deleted: 15
List without 15's: [10, 20, 20, 10, 25, 30, 12]
'''

#Gift
#Determine mode
'''
a=eval(input('Enter any list: '))
mode,count,s=-1,0,-1
for x in a:
	if a.count(x)>mode:
		count=a.count(x)
		mode=x
		s=-1
	elif a.count(x)==count:
		s=x
if s<0:
	print('Mode :',mode)
else:
	print('Mode :',mode,s)

Output
Enter any list: [10,20,30,12,10,20,19,15,30,10]
Mode : 10
Enter any list: [10,20,10,30,20]
Mode : 10 20
'''

#  Nested  List  demo  program  (Home  work)
'''
a=[[10,20,30,40],[50,60,70,80],[90,100,110,120]]
print(a)       #[[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
print(len(a))  #3
print(a[0])    #How to print 1st inner list
print(a[1])    #How to print 2nd inner list
print(a[2])    #How to print 3rd inner list
print(a[0][2]) #How to print 30
print(a[1][3]) #How to print 80
print(a[2][1]) #How to print 100
'''

#Find outputs
'''
a=[[10,20], [30,40,50], [60,70,80,90]]
print(a[0])       #print 1st inner list
print(a[1])       #print 2nd inner list
print(a[2])       #print 3rd inner list
print(len(a[0]))  #print number of elements in 1st inner list
print(len(a[1]))  #print number of elements in 2nd inner list
print(len(a[2]))  #print number of elements in 3rd inner list
'''

#How to print nested list in different ways
'''
a=[[10,20],[30,40,50],[60,70,80,90]]
print('Nested list with print function')
print(a)
print('Each inner list of outer list without indexes')
for x in a:
	print(x)
print('Elements in the form of matrix without using indexes')
for x in a:
	for y in x:
		print(y,end=' ')
	print()
#Another way
#for x in a:
#	print(*x,sep=' ')
print('Elements in the form of matrix using indexes')
for x in a:
	for y in range(len(x)):
		print(x[y],end=' ')
	print()
'''

#Find outputs
'''
a=[[10,20],[30,40],[50,60],[70,80]]
for x in a:
    print(x)     #[10,20]<next line>[30,40]<next line>[50,60]<next line>[70,80]
print()          #<next line>
for x,y in a:
	print(x,y,sep='...') #10...20<next line>30...40<next line>50...60<next line>70...80
'''

#Find outputs
'''
a=[[10,20,30],[40,50,60],[70,80,90]]
for x in a:
    print(x)  #[10,20,30]<next line>[40,50,60]<next line>[70,80,90]
print()       #<next line>
for x,y,z in a:
	print(x,y,z,sep='...') #10...20...30<next line>40...50...60<next line>70...80...90
'''

#Find outputs
'''
a=[[10,20],[30,40,50],[60,70,80,90]]
for x in a:
	print(x)  #[10,20]<next line>[30,40,50]<next line>[60,70,80,90]
for x,y in a:
	print(x,y,sep='...') #Error
'''

#Find outputs'
'''
a=[[]]
print(*a)  #How to print inner list
print(a[0])#How to print inner list in another way
'''

#Find outputs 
'''
a=[[10,'Rama',1000.0],[20,'Sita',2000.0],[15,'Rajesh',3500.0],[18,'Kiran',2800.0],[5,'Amar',5000.0]]
print(sorted(a))   #[[5,'Amar',5000.0],[10,'Rama',1000.0],[15,'Rajesh',3500.0],[18,'Kiran',2800.0],[20,'Sita',2000.0]]
print(sorted(a,reverse=True)) #[[20,'Sita',2000.0],[18,'Kiran',2800.0],[15,'Rajesh',3500.0],[10,'Rama',1000.0],[5,'Amar',5000.0]]
print(a)         #[10,'Rama',1000.0],[20,'Sita',2000.0],[15,'Rajesh',3500.0],[18,'Kiran',2800.0],[5,'Amar',5000.0]
'''

#Create a list with cubes of 2,4,6,8,10 with list comprehension
'''
a=[x**3 for x in range(2,11,2)]
print(a)  #[8, 64, 216, 512, 1000]
'''

#Extract 1st character of each string in capital letters in a list of strings without comprehension
'''
a=eval(input('Enter list of strings: '))
res=[]
for x in a:
	res.append(x[0].upper())
print(res)

#Output
Enter list of strings: ['hyd', 'pune', 'chennai', 'vijayawada']
['H', 'P', 'C', 'V']
'''

#Extract 1st character of each string in capital letters in a list of strings with comprehension
'''
a= eval(input('Enter any list: '))
r=[x[0].upper() for x in a]
print(r)

#Output
Enter any list: ['hyd', 'pune', 'chennai', 'vijayawada']
['H', 'P', 'C', 'V']
'''

#Append each word of the sentence and its length to a list
#words should be in capital letters without comprehension
'''
a=input('Enter any string: ').split()
r=[]
for x in a:
	res.append([x.upper(),len(x)])
print(r)

#Output
Enter any string: Hyd is green city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]
'''

#Append each word of the sentence and its length to a list
#words should be in capital letters with comprehension
'''
a=input('Enter any string: ').split()
r=[[x.upper(),len(x)] for x in a]
print('Result:', r)

#Output
Enter any string: Hyd is green city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]
'''

#Add two lists of unequal length without comprehension
'''
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
r=[]
for i in range(min(len(a),len(b))):
	res.append(a[i]+b[i])
print('Result:',r)

#Output
Enter 1st list: [10,20,30,40,50,60,70]
Enter 2nd list: [100,200,300,400]
Result: [110, 220, 330, 440]
'''

#Add two lists of unequal length with comprehension
'''
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
r=[a[i]+b[i] for i in range(min(len(a),len(b)))]
print('Result:',r)

#Output
Enter 1st list: [10,20,30,40,50,60,70]
Enter 2nd list: [100,200,300,400]
Result: [110, 220, 330, 440]
'''

#Initialize a nested list with zeroes without comprehension
'''
a=int(input('Number of many lists: '))
b=int(input('Number of elements in each list: '))
r=[]
for x in range(a):
	c=[]
	for y in range(b):
		c.append(0)
	r.append(c)
print('Result:', r)

#Output
Number of many lists: 3
Number of elements in each list: 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''


#Initialize a nested list with zeroes with comprehension
'''
a=int(input('Number of many lists: '))
b=int(input('Number of elements in each list: '))
res=[[0 for j in range(b)] for i in range(a)]
print(res)

#Output
Number of many lists: 3
Number of elements in each list: 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''

#Extract the elements of 1st list which are not in 2nd list without comprehension
'''
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
res=[]
for x in a:
	if x not in b:
		res.append(x)
print(res)

#Output
Enter 1st list: [10,20,15,18,25,12]
Enter 2nd list: [15,10,20]
[18, 25, 12]
'''

#Extract the elements of 1st list which are not in 2nd list with comprehension
'''
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
res=[x for x in a if x not in b]
print(res)

#Output
Enter 1st list: [10,25,18,15,20,12]
Enter 2nd list: [10,20,15]
[25, 18, 12]
'''


#Print even numbers between 1 and 20 with comprehension
'''
print('Even numbers between 1 and 20:',[x for x in range(1,21) if x%2==0])
#Output
Even numbers between 1 and 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''


#Print even numbers between 1 and 20 with comprehension and without using if condition
'''
print('Even numbers between 1 and 20:',[x for x in range(2,21,2)])
#Output
Even numbers between 1 and 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''

#print the squares of 1,2,3,4,...20 which are divisible by 2 with comprehension
'''
print('Squares of 1-20 divisible by 2:',[x*2 for x in range(1,21) if (x*2)%2==0])
#Output
Squares of 1-20 divisible by 2: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''

#print the squares of 1,2,3,4,...20 which are divisible by 2 with comprehension and without if condition
'''
print('Squares of 1-20 divisible by 2:',[x**2 for x in range(2,21,2)])
#Output
Squares of 1-20 divisible by 2: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''

#Add each element of 1st list with all the elements of 2nd list without comprehension
'''
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
res=[]
for x in a:
	for y in b:
		res.append(x+y)
print(res)

#Output
Enter 1st list: [10,20,30]
Enter 2nd list: [40,50,60,70]
[50, 60, 70, 80, 60, 70, 80, 90, 70, 80, 90, 100]
'''

#Add each element of 1st list with all the elements of 2nd list with comprehension
'''
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
res=[x+y for x in a for y in b]
print(res)

#Output
Enter 1st list: [10,20,30]
Enter 2nd list: [40,50,60,70]
[50, 60, 70, 80, 60, 70, 80, 90, 70, 80, 90, 100]
'''

#Concatenate each character of 1st string with every character of 2nd string with comprehension
'''
a=input('Enter 1at string: ')
b=input('Enter 2nd string: ')
res=[x+y for x in a for y in b]
print(res)

#Output
Enter 1at string: HYD
Enter 2nd string: PUNE
Result: ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']
'''

#Convert a nested list to list without comprehension
'''
a=eval(input('Enter any nested list: '))
res=[]
for x in a:
	for y in x:
		res.append(y)
print('Result:',res)

#Output
Enter any nested list: [[10,20],[30,40,50],[60,70]]
Result: [10, 20, 30, 40, 50, 60, 70]
'''

#Convert a nested list to list with comprehension
'''
a=eval(input('Enter any nested list: '))
res=[y for x in a for  y  in x]
print(res)

#Output
Enter any nested list: [[10,20],[30,40,50],[60,70,80,90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''

#Find outputs 
'''
a=[[10,20],[30,40,50],[60,70,80,90]]
b=[x for x in a for y in x]
print(b) #[[10,20],[10,20],[30,40,50],[30,40,50],[30,40,50],[60,70,80,90],[60,70,80,90],[60,70,80,90],[60,70,80,90]]
'''

#Nested comprehension demo program
'''
a=[[j for j in range(i)] for i in range(5)]
print(a)   #[[],[0],[0,1],[0,1,2],[0,1,2,3]]
'''

#Normal program
'''
a=eval(input('Enter list of strings: '))
b=[]
for x in a:
	if x[0] not in b:
		b.append(x[0])
res=[]
for x in b:
	d=[]
	for y in a:
		if y.startswith(x):
			d.append(y)
	res.append(d)
print('Nested list:',res)

#Output
Enter list of strings: ['Swathi','Anand','Srinivas','Zebra','King','Amar']
Nested list: [['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
'''

#Merge two sorted lists to produce another sorted list
'''
a=eval(input('Enter 1st sorted list: '))
b=eval(input('Enter 2nd sorted list: '))
i,j=0,0
res=[]
for x in range(len(a)+
len(b)):
	if i==len(a) or j==len(b):
		break
	elif a[i]<b[j]:
		res.append(a[i])
		i+=1
	else:
		res.append(b[j])
		j+=1
if i>j:
	res.extend(b[j:])
else:
	res.extend(a[i:])
print('Result:',res)

Output
Enter 1st sorted list: [10,30]
Enter 2nd sorted list: [20,40,50]
Result: [10, 20, 30, 40, 50]
'''



