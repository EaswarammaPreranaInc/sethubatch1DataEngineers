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


classwork
---------
#1)
a= 25
b=10.8
c='Hyd'
d= True
e=[a,b,c,d]
print(e) # [25, 10.8, 'Hyd', True]
print(type(e)) # <class 'list'>


#2)List unpacking
list=[25, 10.8, 'hyd', True]
a,b,c,d = list
print('a: ' , a) # a:  25
print('b: ' , b) #b:  10.8
print('c: ' , c) # c:  hyd
print('d: ' , d) # d: True
x,y,z = list # Error due to excess elements in the list
a,b,c,d,e =list # Error due to few  elements in the list

#3)
list = [25,10.8, 'Hyd', True]
a,b,*c = list
print('a: ' , a) # a:  25
print('b: ' , b) #b:  10.8
print('c: ' , c) # c:  ['Hyd' , True]
print(type(c))# < class 'list'>

#4)sorted function demo program

a=[10,20,15,5,12]
b= sorted(a)
print(b) #[5, 10, 12, 15, 20]
print(type(b)) #<class 'list'>
c= sorted(a, reverse =True)
print(c) # [20, 15, 12, 10, 5]
print(a) # [10, 20, 15, 5, 12]

#5)

a= input('Enter list:') #[10,25.8,'Hyd', True]
print(type(a)) #<class 'str'>
print(a)# "[10,25.8,'Hyd', True]"
b = eval(a) # str list convert to list
print(b) # [10,25.8,'Hyd', True]
print(type(b)) <class 'list'>


#6) Extend method

a =[10,20,30,40]
b =[50,60,70]
a.extend(b)
print(a) #[ 10,20,30,40,50,60,70]
print(len(a))#7
a.extend('Hyd') 
print(a) # [10,20,30,40,50,60,70, 'H','y', 'd']
print(len(a))#10
a.extend(25) #Error due to 25 is not a sequence


#7)

list=[10,20,15,18]
print(list)
list.insert(-2,25)
print(list)
list.insert(-len(list),12)
print(list)
list.insert(-10,19)
print(list)

#8)
'''
a=[10,20,30,40,50,60,70]
for x in a:
	a.remove(x)
print(a) [20,40,60]



