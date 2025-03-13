#  append()  method  demo  program (Home  work)
'''
list = [10 , 20 , 15 , 18]
print(list)       # list = [10 , 20 , 15 , 18]
list . append(19)
print(list)       # list = [10 , 20 , 15 , 18, 19]
'''

# Find  outputs (Home  work)
'''
list = []
print(list) # empty list
list . append(25) # append '25' to list
list . append(10.8) # append '10.8' to list i.e [25, 10.8]
list . append('Hyd') # append 'Hyd' to list i.e [25, 10.8, 'Hyd']
list . append(True) # append 'True' to list i.e [25, 10.8, 'Hyd', True]
print(list) #[25, 10.8, 'Hyd', True]
'''

# Find  outputs  (Home  work)
'''
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) #[0, 10, 20, 30, 40]
'''

# Find  outputs  (Home  work)

a = [10 , 20 , 30]
'''
a . append('Hyd')
print(a) # [10, 20, 30, 'Hyd']
print(len(a)) #4
print(a[3])  # Hyd
print(a[3][0]) # H
print(a[3][1]) # y
print(a[3][2]) # d
'''

# Find  outputs (Home  work)

a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a) # [10, 20, [50, 60, 70], 30, 40]
print(len(a)) # 6
print(a[2])
print(a[2] [0])
print(a[2] [1])
print(a[2] [2])
