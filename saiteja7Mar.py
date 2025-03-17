# Programs on March 03 2025

'''
#program to print each element and correspounding index
a=[25,10.8,'hyd',True]
for i in range(len(a)):
	print(a[i], i)
'''	

'''
# program to print list elements in reverse order
a = eval(input('Enter list of elements : '))
print('Indexed for loop')
for i in range((len(a) - 1), -1, -1):
    print(a[i])
'''

"""
a=eval(input("enter the list of elements:"))
b=eval(input("enter the list of elements:"))
c=[]
for i in range(len(a)):
    c.append(a[i] + b[i])
print(c)

#for each loop
a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))
c = []
i = 0
for x in a:
    c.append(x + b[i])
    i = i + 1

print('3rd list : ', c)

"""
'''
a=[10.8,'hyd',25,True,3+4j,None,'sec']
for i in range(len(a)):
	z=a[i]
print(a[2],a[3],a[4])
'''


a=[10.8,'hyd',25,True,3+4j,None,'sec']
for i in range(2,5):
	x=a[i]
	print(x)









