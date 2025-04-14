#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list)           # [10 , 20 , 15 , 18]
list . append(19) # 19 added in end of the list  # [10 , 20 , 15 , 18,19]
print(list)         # [10 , 20 , 15 , 18,19]

print()

 #  Find  outputs (Home  work)
list = []                 # Empty list
print(list)              #   []
list . append(25)    # 25 added to list [25]
list . append(10.8)  # 10.8 added to list [25,10.8]
list . append('Hyd') # Hyd is added to list   [25,10.8,'Hyd']
list . append(True)  #  True is added to list   [25,10.8,'Hyd',True]
print(list)          # [25,10.8,'Hyd',True]

print()

# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x) # [0,10,20,30,40]
print(list)          # [0,10,20,30,40]

print()

 #  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd') # 'Hyd' is added to list at end # [10 , 20 , 30,'Hyd']
print(a)           # [10 , 20 , 30,'Hyd']
print(len(a))         # 4
print(a[len(a)-1]) #How  to  print  4th  element  of  list  'a')
print(a[len(a)-1][0]) #  (How  to  print  'H')
print(a[len(a)-1][1])#How  to  print  'y')
print(a[len(a)-1][2]) #How  to  print  'd')

print()

#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b) # list b is sublist added to list a [10 , 20 ,[50 , 60 , 70], 30 , 40]
print(a)               # [10 , 20 ,[50 , 60 , 70], 30 , 40]
print(len(a))          # 5
print(a[2])#How  to  print  inner  list)
print(a[2][0]) #How  to  print  50)
print(a[2][1])#How  to  print  60)
print(a[2][2]) #How  to  print  70)

print()

