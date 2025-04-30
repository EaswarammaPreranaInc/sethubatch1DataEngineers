# append() method demo program
'''
list = [10,20,15,18] 
print(list) # [10,20,15,18]
list.append(19) # 19 append to list
print(list) # [10,20,15,18,19]
'''

# Find outputs
'''
list = []
print(list) # []
list.append(25) # [25]
list.append(10.8) # [25,10.8]
list.append('Hyd') # [25,10.8,'Hyd']
list.append(True) # [25,10.8,'Hyd',True]
print(list) # [25,10.8,'Hyd',True]
'''

#find outputs
'''
list = []
for x in range(0,50,10):
	list.append(x)
print(list) # [0,10,20,30,40]
'''

# Find outputs
'''
a = [10,20,30]
a.append('Hyd') # [10,20,30,'Hyd']
print(a) # [10,20,30,'Hyd']
print(len(a)) # 4
print(a[3]) # print(How to print 4th element of list 'a') i.e Hyd
print(a[3][0]) # print(How to print 'H') i.e H 
print(a[3][1]) # print(How to print 'y') i.e y
print(a[3][2]) # print(How to print 'd') i.e d
'''

# Find outputs
'''
a = [10,20,30,40]
b = [50,60,70]
a.insert(2,b) 
print(a) # [10,20,[50,60,70],30,40]
print(len(a)) # 5
print(a[2]) # print(How to print inner list) i.e [50,60,70] 
print(a[2][0]) # print(How to print 50) i.e 50
print(a[2][1]) # print(How to print 60) i.e 60
print(a[2][2]) # print(How to print 70) i.e 70
'''
