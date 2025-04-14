# Find  outputs  (Home  work_1)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # prints set{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class, 'set'>
print(a[10]) #prints output Ramesh
print(a[20]) #prints output Kiran
print(a[15]) #prints output Amar
print(a[18]) #prints output Sita
print(a[19]) # Error because key 19 doesn't exit in the set
print(a[0]) # Error because key 0
print(a['Amar']) # Error Value Amar
a[15] = 'Krishna' # modifies key 15 value from Amar to Krishna
del   a[20] # deletes 20: 'Kiran' from dict a
a[25] = 'Vamsi' # inserts 25:'vamsi'
print(a) # prints dict after modification, deletion, and insertion {10:'Ramesh',15:'Krishna',18:'Sita',25:'Vamsi'}
print(len(a)) # print no of key-value pairs = 4
print(a * 2) # Error

# Find  outputs  (Home  work_2)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) prints dict a {10:'Sec'}
print(len(a)) prints the no of key-value pairs = 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) prints dict b {'R':'Red','G':'Green','B':'Blue','Y':'Yellow'}
print(len(b)) prints no of key-value pairs = 4


#find output (Home work_3)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) prints dict a {True: 'May be'}
print(len(a)) prints no of key-value pairs = 1


# Find  outputs (Home work_4)
a = { [ ] : 25} # Error due to dict can not have mutable object (list)
b = { ( ) : 25} 
print(b) # prints {(): 25}
c = { { } : 25}  # Error due to dict can not have dict inside it
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #prints dict d {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) # prints no of key-value pairs = 1
e = {set() : 10.8} # #error due to set mutable


# Find  outputs (Home work_5)
a = {}
print(type(a)) # <class, 'dict'>
print(len(a)) #print no of key-value pairs = 0
print(a) #prints empty dict {}
b = dict()
print(type(b))#<class, 'dict'>
print(len(b))#print no of key-value pairs = 0
print(b)#prints empty dict {}
