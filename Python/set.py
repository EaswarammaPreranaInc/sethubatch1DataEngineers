# a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
# print(a)
# print(type(a))
# # print(a[10])
# # print(a[20])
# # print(a[15])
# # print(a[18])
# #  # print(a[19]) # keyvalue doesn't exist
# # # print(a[0]) # 0 key value doesn't exist
# # # print(a['Amar']) # we cannot print with elements
# # a[15] = 'Krishna'
# # del   a[20]
# # a[25] = 'Vamsi'
# # print(a)
# # print(len(a))

# a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
# a = {True : 'literal'}
# print(a)
# print(len(a))

# ''''''
# a = 25  
# print(id(a))  # Prints the memory address (ID) of the integer 25  

# a = 35  
# print(id(a))  # Prints the memory address (ID) of the integer 35
# ''''
# a = 25.7  
# print(id(a))  # Prints the memory address of 25.7  

# print(a)  # Prints the value of a -> 25.7  

# a = 35.6  
# print(id(a))  # Prints the memory address of 35.6 (different from previous id)  

# print(a)  # Prints the new value of a -> 35.6  

# b = True  
# print(id(b))  # Prints the memory address of True (fixed memory location for True in Python)  

# b = False  
# print(id(b))  # Prints the memory address of False (fixed memory location for False in Python)  

# c = None  
# print(id(c))  # Prints the memory address of None (fixed memory location for None in Python)  

# c = None  
# print(id(c))  # Prints the memory address of None again (same as before)
''''''''
a = 'Hyd'
print(id(a))
a[1] = 'e'  # 
a = 'Sec'
print(id(a))
b = (10 , 20 , 15 , 18)
print(id(b))
b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b))
c = range(5)
print(id(c))
c[3] = 10
c = range(5)
print(id(c))
