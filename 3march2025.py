# how to print each element and the corresponding index 
''' 
a=list(input("enter the values of the list : "))
for i in range (len(a)):
    print(i,end=" ")
print()
for j in a:
    print(j,end=" ")


# how to print each element and the corresponding index
a=list(input("enter the values of the list : "))
for i in range (len(a)):
    print(i,end=" ")
    print(a[i])

'''
'''
a=list(input("enter the values of the list : "))
for i in (a):
        print(i,end=" ")
print()
for i in range(len(a)):
        print(i,end=" ")
'''
# reverse the string without string slicing 
"""
a=eval(input("enter the list of elements : "))
a=list(str(a))
print(a)
for i in range(len(a)-1,-1,-1):
    print(a[i])

a=eval(input("enter the list of elements : "))
a=list(str(a))
for b in reversed(a):
    print(b)


a=list(input("enter the input : "))
for i in range(len(a)):

    print(i)
"""
# add two lists and store it in 3rd list 
"""
a=list(input("enter the elements to the first lisrt : "))
b=list(input("enter the elements to the 2nd list : "))
c=[]

for i in a:
    d=eval(i)
    print(d)
    for j in b:
        e=eval(j)
        c.append(d+e)
    print(c)

for i in range(len(a)):
    c.append(a[int(i)]+b[int(i)])
print(c)"""

# access the elements of the list from 2 to 4
'''
a=list(input(" enter the elements to list : "))

for i in range(2,5):
    print(a[i])
for i in a:
    for j in range(2,5):
        print(j)
    '''
'''
# find output
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1 # add one to every element 
print('a :  ' , a) # print list with [11,21,16,19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1 # same but it only returns one element of last itration 
print('b :  ' ,  b)'''

#print  the first even numbers of the given number
"""
a=int(input("enter the number to print even numbers to : "))
b=0
i=1
while i<=a:
    b=i*2
    i+=1
    print(b)
    
"""
# odd numbers using while
'''
a=int(input("enter the number to print even numbers to : "))
b=0
i=1
while i<=a:
    b=2*i-1
    i+=1
    print(b)

'''
# print natural umbers upto the given number
"""
i=1
for i in range(int(input(" enter the value to print the natural numbers upto : "))):
    i+=1
    print(i)
"""
'''# print 10,9,8,...........1
#for i in range(0,int(input("enter the value : ")),-1):
a=input("    ")
#for i in range(0,a):
c=len(a)-1
for i in range(0,c):
    print(i)'''
'''
for i in range(10,0,-1):
    print(i)
'''
# print the alphabets using for loop chr(65) =  'A',chr(90) = 'Z',chr(97) =  'a',chr(122) = 'z'
'''
for i in range(65,91):
    print(chr(i),end=" ")
print()
for j in range (97,123):
    print(chr(j),end=" ")

    '''
# write a program to find the element is present or not 

'''
n=int(input(" enter the value : "))
a=[0,1]
for i in range(0,n):
    a.append(a[-1]+a[-2])
for i in a:
    print("found")
else:
    print("not found")
'''

