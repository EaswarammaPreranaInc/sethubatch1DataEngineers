'''list=[10,20,15,18]
print(list)#[10,20,15,18]
list.append(19)#19 is append to list
print(list)#[10,20,15,18,19]

list=[]
print(list)#[]
list.append(25)#[25]
list.append(10.8)#[25,10.8]
list.append('hyd')#[25,10.8,'hyd']
list.append(True)#[25,10.8,'hyd',True]
print(list)#[25,10.8,'hyd',True]

list=[]
for x in range(0,50,10):
    list.append('hyd')
print(list)#['hyd','hyd','hyd','hyd','hyd']

a=[10,20,30]
a.append('hyd')# [10,20,30,'hyd']
print(a)# [10,20,30,'hyd']
print(len(a))# 4
print(a[3])#hyd
print(a[3][0])#h
print(a[3][1])#y
print(a[3][2])#d'''

a=[10,20,30,40]
b=[50,60,70] 
a.insert(2,b)#insert[10,20,[50,60,70],30,40]
print(a)#[10,20,[50,60,70],30,40]
print(len(a))#5
print(a[2])#[50,60,70]
print(a[2][0])#50
print(a[2][1])#60
print(a[2][2])#70