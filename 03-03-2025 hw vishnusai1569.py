a=[25,10.8,'hyd',True]
for i in range(len(a)):
    print(i)
print("each  element  and  the  corresponding  index  with  index  based  for  loop")

for i in range(len(a)):
    print(i,a[i])
print("each  element  and  the  corresponding  index  with  for  ...  each  loop")
for i in a:
    print(a.index(i),i)

#2
a =eval(input('Enter  list  of  elements : '))
for i in range(len(a)-1,-1,-1):
    print(a[i])
print("\n")
for i in reversed(a):
    print(i)

#3
a =  eval(input('Enter 1st list : '))
b =  eval(input('Enter 2st list : '))
c = []
for i in range(len(a)):
	c.append(a[i]+b[i])
print('3rd list : ',c)
for a,b in zip(a,b):
	print(end="")
print(c)

#4
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range(2,len(a)-2):
    print(a[i])
print()
for i in a[2:5]:
    print(i)

#5
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
#a :   [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)
#b :   [10, 20, 15, 18]

#6
num = int(input("Enter the number of even numbers to print: "))
count = 0
i = 2
while count < num:
    print(count,i)
    i += 2
    count += 1

#7
num = int(input("Enter the number of even numbers to print: "))
count = 0
i = 1
while count < num:
    print(count,i)
    i += 2
    count += 1

#8
n= int(input("Enter the number : "))
i=1
for i in range(1,n):
    print(i)
    i+=1

#9
n=int(input("enter the number :"))
for i in range(n,0,-1):
    print(i)

#10
for i in range(65,91):
    print(chr(i),end=" ")
    i+=1
print("")
for i in range(97,123):
    print(chr(i),end=" ")
    i+=1

#11
n=int(input("enter the number :"))
a, b = 0, 1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c

#12
k=int(input('enter the number x :'))
a=0
b=1
c=a+b
mylist=[0,1]
for i in range(100):
    c=a+b
    a=b
    b=c
    mylist.append(c)
if k in mylist:
    print('found')
else:
    print("not found")

#13
n=int(input("enter the n :"))
sum=0
for i in range(0,n+1):
	sum+=i*1.1
print(f'sum :{sum:.2f}')

#14
n=int(input("enter the number :"))
sum=0
i=1
while i<=n:
    sum=sum+2*i
    i = i + 1
print(sum)

#15
n=int(input("enter the number :"))
sum=0
i=1
while i<=n:
    sum=sum+2*i-1
    i = i + 1
print(sum)

#16
n=int(input("enter the number :"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i = i + 1
print(sum)

#17
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

'''
1
sec
hello
2
sec
hello
3
4
sec
hello
5
sec
hello
6
7
sec
hello
outside loop
'''

'''
#18
if ():
	print('Hyd')
	continue
	print('Sec')
'''


'''	
hyd
sec
'''
"""'continue' not properly in loop"""

'''
#19
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
'''


'''
1
sec
hello
2
sec
hello
3
outside loop
'''
'''
#20
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')

#'break' outside loop
'''
#21
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')


'''
1
sec
hello
2
sec
hello
3
hyd
hello
4
sec
hello
5
sec
hello
6
hyd
hello
7
sec
hello
outside loop
'''

#22
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

'''
1
sec
hello
2
sec
hello
3

outside loop
'''