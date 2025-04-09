# how to print each element & the corresponding index.
a=[25,10.8,'Hyd',True]
print('indexed for loop')
for i in range(len(a)):
	print(i,a[i])
# how to print each element & the corresponding index with index based for loop	
print('for each loop')
for i in range(len(a)):
	print(i,a[i])
# how to print each element & the corresponding index with for each loop(do not use 2nd variable)	
print('for each loop')
for i,element in enumerate(a):
	print(i,a[i])
	output:
indexed for loop
0 25
1 10.8
2 Hyd
3 True
for each loop
0 25
1 10.8
2 Hyd
3 True
for each loop
0 25
1 10.8
2 Hyd
3 True
............
............
# how to print each element in reversed order without slice.
# how to print each element in reverse order with indexed based for loop.
a=eval(input('Enter list of elements:'))
a=[1,2.2,'Hyd',0,3]
print('indexed for loop')
for i in range(len(a)-1,-1,-1):
	print(a[i])
# how to print each element of list in reverse order with for each loop(do not use 2nd variable).
print('for each loop')
for i in reversed(a):
	print(i)
output:
Enter list of elements:5
indexed for loop
3
0
Hyd
2.2
1
for each loop
3
0
Hyd
2.2
1
........
........
# how tp print each element from indexes 2 to 4 without slice.
# how to print each element from indexex 2 to 4 of list 'a' with indexed based for loop.
a=[25,10.0,'Hyd',True,3+4j,None,'Sec']
print('indexed for loop')
for i in range(2,5):
	print(a[i])
# how to print ech element from indexex 2 to 4 of list 'a' with for each loop.
print('for each loop')
for element in a[2:5]:
	print(element)
output:
indexed for loop
Hyd
True
(3+4j)
for each loop
Hyd
True
(3+4j)
........
........
# find outputs:
a=[10,20,15,18]
for i in range(len(a)):
	a[i]+=1
	print('a:',a)

b=[10,20,15,18]
for x in b:
	x+=1
	print('b:',b)
output:
a: [11, 20, 15, 18]
a: [11, 21, 15, 18]
a: [11, 21, 16, 18]
a: [11, 21, 16, 19]
b: [10, 20, 15, 18]
b: [10, 20, 15, 18]
b: [10, 20, 15, 18]
b: [10, 20, 15, 18]

