12/03/25
#1 
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . append(19) #appends 19 to the list at end
print(list) #[10 , 20 , 15 , 18, 19]


# 2 Find  outputs (Home  work)
list = []
print(list) #empty list []
list . append(25) # appends 25 to the list [25]
list . append(10.8) # appends 10.8 to the list [25,10.8]
list . append('Hyd')# appends 'Hyd' to the list [25,10.8,'Hyd']
list . append(True) # appends True to the list [25,10.8,'Hyd',True]
print(list)  #[25,10.8,'Hyd',True]


# 3 Find  outputs  (Home  work)
list = [] #Creates an empty list
for  x  in   range(0 , 50 , 10): #Range of 0 to 49 in steps of 10
	list . append(x) # Append 0,10,20,30,40 to the list
print(list) #[0,10,20,30,40]


#4 #  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a.append('Hyd') # append 'Hyd' to list a
print(a) #[10 , 20 , 30,'Hyd']
print(len(a)) #4
print(How  to  print  4th  element  of  list  'a') #print(a[3])
print(How  to  print  'H') #print(a[3][0])
print(How  to  print  'd') #print(a[3][1])  
print(How  to  print  'y') #print(a[3][2])


#5 #  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b) #insert list b in list a at index 2
print(a) # [10,20,[50,60,70],30,40]
print(len(a)) #5
print(How  to  print  inner  list) #print(a[2])
print(How  to  print  50) #print(a[2][0])
print(How  to  print  60) #print(a[2][1])
print(How  to  print  70) #print(a[2][2])
