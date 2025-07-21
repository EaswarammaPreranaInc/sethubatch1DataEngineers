# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(a[10]) # Ramesh
print(a[20]) # Kiran
print(a[15]) # Amar
print(a[18]) # Sita
#print(a[19]) # Error becoz no key 19 in a
#print(a[0]) # Error becoz No indexing in dict
#print(a['Amar']) # KeyError
a[15] = 'Krishna'
del   a[20]
a[25] = 'Vamsi'
print(a) # {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) # 4
#print(a * 2) # Error: unsupported operand type(s) for *: 'dict' and 'int'
# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10: 'Sec'}
print(len(a))# 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b)) # 4
#  Gift 
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True : 'May be'}
print(len(a)) # 1
# Find  outputs 
#a = { [ ] : 25} # Error becoz imutable list
b = { ( ) : 25} 
print(b) # { ( ) : 25}
#c = { { } : 25} # Error: unhashable type: 'dict'
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
#e = {set() : 10.8} # Error becoz mutable set
# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict() 
print(type(b)) # <class 'dict'> 
print(len(b)) # 0
print(b) # {}