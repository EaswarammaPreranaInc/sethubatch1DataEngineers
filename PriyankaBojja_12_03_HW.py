'''
#append() method
list=[10,20,15,18]
print(list) #[10,20,15,18]
list.append(19)
print(list) # [10,20,15,18,19]

#find outputs
list = []
print(list)  #[]
list.append(25)
list.append(10.8)
list.append('Hyd')
list.append(True)
print(list)  #[10,25,'Hyd',True]

#find outputs
list=[]
for x in range(0,50,10):
	list.append(x)
print(list) #[0,10,20,30,40]

#find outputs
a=[10,20,30]
a.append('Hyd')
print(a)      #[10,20,30,'Hyd']
print(len(a)) #4
print(a[3])   #how to print 4th element of list a  --Hyd
print(a[3][0]) #how to print 'H' ---H
print(a[3][1]) #how to print 'y' --y
print(a[3][2]) #how to print 'd' ---d

#find outputs
a=[10,20,30,40]
b=[50,60,70]
a.insert(2,b)
print(a)        #[10,20,[50,60,70],30,40] 
print(len(a))   #5
print(a[2])     #[50,60,70] ---  how to print inner list
print(a[2][0])  #50     ---- how to print 50
print(a[2][1])  #60       ------how to print 60
print(a[2][2])  #70  --------how to print 70
'''
