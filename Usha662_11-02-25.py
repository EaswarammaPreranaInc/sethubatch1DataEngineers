program-01
a = 3 + 4j# ref a points to object 3+4j
print(a) # 3+4j
print(type(a))# class<'complex'>
print(id(a)) # address of object a
print(a . real) # 3
print(a . imag) # 4j
print(type(a . real)) #class<'int'>
print(type(a . imag)) #class<'complex'>

program-02
a = 6j# ref a ponits to object 6j
print(a)# 6j
print(type(a)) # class<'complex'>
print(a . real) # 0
print(a . imag) # 6j
print(5 + j6) #error
print(3 + 4i) #error
print(4+j) #valid
print(4 + 1j) #valid
print(4 + 0j) #valid

program-03
a = True
print(a) # True
print(type(a)) #class<'bool'>
print(id(a)) # address of object a
b = False
print(b) # False
print(type(b)) # class<'bool'>
print(True + True) # 2
print(True + False) # 1
print(False + True) # 1
print(False + False) # 0
print(True + True + True) # 3
print(25 + 10.8 + True) # 36.8
print(True > False) # True
print(True) # True
print(False) # False
print(true) # error
print(false) # error


