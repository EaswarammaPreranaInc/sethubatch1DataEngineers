'''
#1)  append()  method  demo  program (Home  work)

list = [10 , 20 , 15 , 18]
print(list) #[10, 20, 15, 18]
list . append(19)# here 19 appends at the end in the list
print(list) # [10, 20, 15, 18, 19]

#2) Find  outputs (Home  work)

list = []
print(list) # prints empty list []
list . append(25) # appends '25' to the empty list
list . append(10.8) # appends '10.8' to the empty list
list . append('Hyd') # appends 'Hyd' to the empty list
list . append(True) #appends 'True' to the empty list
print(list) # [25, 10.8, 'Hyd', True]

#3) Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10): # iterates from 0 with difference of 10 upto 50
	list . append(x) # appends elements to empty list
print(list) # [0, 10, 20, 30, 40]

[0] #first 0 iterates
[0, 10] #iterates 0 and 10
[0, 10, 20] #iterates 0,10 and 20
[0, 10, 20, 30]# iterates 0 ,10,20 and 30
[0, 10, 20, 30, 40]#iterates 0, 10, 20, 30 and 40


#4) Find  outputs  (Home  work)

a = [10 , 20 , 30]
a . append('Hyd') # appends 'Hyd' to the list
print(a) # [10, 20, 30, 'Hyd']
print(len(a)) # 4
print(a[3]) #(How  to  print  4th  element  of  list  'a')
print(a[3][0]) #(How  to  print  'H')
print(a[3][1]) #(How  to  print  'y')
print(a[3][2]) #(How  to  print  'd')
'''
#5)Find  outputs (Home  work)

a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b) # insert the 'b' at index 2 in list 'a'
print(a) # [10, 20, [50, 60, 70], 30, 40]
print(len(a)) # 5
print(a[2]) #(How  to  print  inner  list)
print(a[2][0]) #(How  to  print  50)
print(a[2][1]) #(How  to  print  60)
print(a[2][2]) #(How  to  print  70)







