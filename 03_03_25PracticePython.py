#Hw 2 print  each element and corresponding index
a = [25,10.8,'Hyd',True]
print('Indexed for loop')
for i in range(len(a)):
    print(i,a[i])

'''o/p: Indexed for loop
        0 25
        1 10.8
        2 Hyd
        3 True'''
#hw 2 print reverse of elements without slice
a = eval(input('enter a elements: '))
for i in range(1,len(a)+1):
    print(a[-i])

'''o/p: enter a elements: [1,2,3,4,5]
        5
        4
        3
        2
        1'''
#write a program to add two lists and store results in 3rd list

a = eval(input('Enter 1st Element:'))
b = eval(input('Enter 2nd Element:'))
c=[]
for i in range(len(a)):
    c.append(a[i]+b[i])
print('3rd List:',c)    

'''o/p: Enter 1st Element:[1,2,3]
        Enter 2nd Element:[2,3,4]
        3rd List: [3, 5, 7] '''


#write a prgm to print first 20 even nos
i = 1
count=20
while i<=20:
    print(2*i)
    i += 1

''' o/p:2
        4
        6
        8
        10
        12
        14
        16
        18
        20
        22
        24
        26
        28
        30
        32
        34
        36
        38
        40 '''

#write a prgm to print odd nos upto first 20 nos
i = 1
count = 20
while i<=20:
    print(2*i-1)
    i += 1 

''' o/p:1
        3
        5
        7
        9
        11
        13
        15
        17
        19
        21
        23
        25
        27
        29
        31
        33
        35
        37
        39 '''

#10 terms of Fibbanacci series using for loop
a = 0
b = 1
n = int(input('Enter no:'))
print('Fibbanacci Series')
for i in range(n):
    print(a,end=' ')
    a = b 
    b = a+b

''' Enter no:10
    Fibbanacci Series
    0 1 2 4 8 16 32 64 128 256   '''

#write a prgm to determine 1.1+2.2+...nterms
n = int(input('hw many would you like:'))
sum = 0
for i in range(1,n+1):
    sum = sum+1.1*i
print('sum:',sum)    

''' o/p:hw many would you like:5
        sum: 16.5 '''

#write a prgm to determine sum of 1st 20 even nos
sum = 0
for i in range(1,21):
    sum = sum+2*i
print('sum of first 20 even nos:',sum)   
'''o/p : sum of first 20 even nos: 420'''
#write a prgm to determine first 20 no sum
sum = 0
for i in range(1,21):
    sum = sum+2*i-1
print('sum of first 20 odd nos:',sum)   

'''o/p : sum of first 20 odd nos: 400'''