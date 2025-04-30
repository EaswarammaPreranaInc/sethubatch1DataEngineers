#program 01:append()  method  demo  program 
list = [10 , 20 , 15 , 18]
print(list) # [10 , 20 , 15 , 18]
list . append(19)# append 19 to list
print(list) # [10 , 20 , 15 , 18,19]

#program 02:  Find  outputs 
list = []
print(list) #[]
list . append(25)# append 25 to list
list . append(10.8) #append 10.8 to list
list . append('Hyd')#append 'Hyd to list
list . append(True)#append True to list
print(list)#[25,10.8,'Hyd',True]

#program 03: Find  outputs  
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)
out put:
[0,10,20,30,40,50]

#program 04:  Find  outputs 
a = [10 , 20 , 30]
a . append('Hyd')
print(a) #[10,20,30,'Hyd']
print(len(a)) #4
print(a[3])# How  to  print  4th  element  of  list  'a i.e.Hyd
print(a[3])# Hyd
print(a[4])# error
print(a[5])# error

#program 05:  Find  outputs
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b) # insert list b at index 2 of list a
print(a)#[10 , 20 ,[50 , 60 , 70], 30 , 40]
print(len(a))# 5
print(a[2])#How  to  print  inner  list i.e.,[50 , 60 , 70]
print(a[2][0])# How  to  print  50
print(a[2][1])# How  to  print  60
print(a[2][2])# How  to  print  70'''
