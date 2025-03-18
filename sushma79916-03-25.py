Normal program
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



#Merge two sorted lists to produce another sorted list
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

#Output
Enter 1st sorted list: [10,30]
Enter 2nd sorted list: [20,40,50]
Result: [10, 20, 30, 40, 50]





#Extract 1st character of each string in capital letters in a list of strings without comprehension
a=eval(input('Enter list of strings: '))
res=[]
for x in a:
	res.append(x[0].upper())
print(res)

#Output
Enter list of strings: ['hyd', 'pune', 'chennai', 'vijayawada']
['H', 'P', 'C', 'V']



#Extract 1st character of each string in capital letters in a list of strings with comprehension
a= eval(input('Enter any list: '))
res=[x[0].upper() for x in a]
print(res)

#Output
Enter any list: ['hyd', 'pune', 'chennai', 'vijayawada']
['H', 'P', 'C', 'V']



#Append each word of the sentence and its length to a list
#words should be in capital letters without comprehension
a=input('Enter any string: ').split()
res=[]
for x in a:
	res.append([x.upper(),len(x)])
print(res)

#Output
Enter any string: Hyd is green city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]



#Append each word of the sentence and its length to a list
#words should be in capital letters with comprehension
a=input('Enter any string: ').split()
res=[[x.upper(),len(x)] for x in a]
print(res)

#Output
Enter any string: Hyd is green city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]



#Add two lists of unequal length without comprehension
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
res=[]
for i in range(min(len(a),len(b))):
	res.append(a[i]+b[i])
print('Result:',res)

#Output
Enter 1st list: [10,20,30,40,50,60,70]
Enter 2nd list: [100,200,300,400]
Result: [110, 220, 330, 440]



#Add two lists of unequal length with comprehension
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
res=[a[i]+b[i] for i in range(min(len(a),len(b)))]
print('Result:',res)

#Output
Enter 1st list: [10,20,30,40,50,60,70]
Enter 2nd list: [100,200,300,400]
Result: [110, 220, 330, 440]



#Initialize a nested list with zeroes without comprehension
a=int(input('Number of many lists: '))
b=int(input('Number of elements in each list: '))
res=[]
for x in range(a):
	c=[]
	for y in range(b):
		c.append(0)
	res.append(c)
print(res)

#Output
Number of many lists: 3
Number of elements in each list: 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]



#Initialize a nested list with zeroes with comprehension
a=int(input('Number of many lists: '))
b=int(input('Number of elements in each list: '))
res=[[0 for j in range(b)] for i in range(a)]
print(res)

#Output
Number of many lists: 3
Number of elements in each list: 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]



#Extract the elements of 1st list which are not in 2nd list without comprehension
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



#Extract the elements of 1st list which are not in 2nd list with comprehension
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
res=[x for x in a if x not in b]
print(res)

#Output
Enter 1st list: [10,25,18,15,20,12]
Enter 2nd list: [10,20,15]
[25, 18, 12]



#Print even numbers between 1 and 20 with comprehension
print('Even numbers between 1 and 20:',[x for x in range(1,21) if x%2==0])
#Output
Even numbers between 1 and 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



#Print even numbers between 1 and 20 with comprehension and without using if condition
print('Even numbers between 1 and 20:',[x for x in range(2,21,2)])
#Output
Even numbers between 1 and 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



#print the squares of 1,2,3,4,...20 which are divisible by 2 with comprehension
print('Squares of 1-20 divisible by 2:',[x*2 for x in range(1,21) if (x*2)%2==0])
#Output
Squares of 1-20 divisible by 2: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]



#print the squares of 1,2,3,4,...20 which are divisible by 2 with comprehension and without if condition
print('Squares of 1-20 divisible by 2:',[x**2 for x in range(2,21,2)])
#Output
Squares of 1-20 divisible by 2: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]



#Add each element of 1st list with all the elements of 2nd list without comprehension
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



#Add each element of 1st list with all the elements of 2nd list with comprehension
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
res=[x+y for x in a for y in b]
print(res)

#Output
Enter 1st list: [10,20,30]
Enter 2nd list: [40,50,60,70]
[50, 60, 70, 80, 60, 70, 80, 90, 70, 80, 90, 100]



#Concatenate each character of 1st string with every character of 2nd string with comprehension
a=input('Enter 1at string: ')
b=input('Enter 2nd string: ')
res=[x+y for x in a for y in b]
print(res)

#Output
Enter 1at string: HYD
Enter 2nd string: PUNE
Result: ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']



#Convert a nested list to list without comprehension
a=eval(input('Enter any nested list: '))
res=[]
for x in a:
	for y in x:
		res.append(y)
print('Result:',res)

#Output
Enter any nested list: [[10,20],[30,40,50],[60,70]]
Result: [10, 20, 30, 40, 50, 60, 70]



#Convert a nested list to list with comprehension
a=eval(input('Enter any nested list: '))
res=[y for x in a for  y  in x]
print(res)

#Output
Enter any nested list: [[10,20],[30,40,50],[60,70,80,90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]



#Find outputs 
a=[[10,20],[30,40,50],[60,70,80,90]]
b=[x for x in a for y in x]
print(b) #[[10,20],[10,20],[30,40,50],[30,40,50],[30,40,50],[60,70,80,90],[60,70,80,90],[60,70,80,90],[60,70,80,90]]



#Nested comprehension demo program
a=[[j for j in range(i)] for i in range(5)]
print(a)   #[[],[0],[0,1],[0,1,2],[0,1,2,3]]
