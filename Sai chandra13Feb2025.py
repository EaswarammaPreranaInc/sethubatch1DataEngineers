# int object demo program 

a = 25 # Reference 'a' points to object 25
print(a) # value of object 'a' i.e, 25
print(type(a)) # <class 'int'>
print(id(a)) # Address of object 'a' (may be 1000)
b = 999999999999999999999999999999999 # valid
print(b) # 9999999999999999999999999999
# c = 75$ # Error




# float object demo program 

a = 10.8 # Ref 'a' points to float object 10.8
print(a) # Value of object 'a' i.e, 10.8
print(type(a)) # <class 'float'>
print(id(a)) # Address of object 'a' (may be 1000)
b = 25. # valid and is interpreted as 25.0
print(b) # 25.0
print(type(b)) # <class 'float'>
c = .689 # valid and is interpreted as 0.689
print(c) # 0.689
d = 3.4E2 # 3.4*10^2
print(d) # 340.0
print(type(d)) # <class 'float'>
e = 9.62e-2 # 9.62*10^-2
print(e) # 0.0962
# print(9.8.2) # Error due to 2 decimal points




# complex object demo program 

a = 3 + 4j  # Ref 'a' to complex object '3 + 4j'
print(a)  # 3 + 4j
print(type(a))  # <class 'complex'>
print(a.real)  # 3.0
print(a.imag)  # 4.0
print(type(a.real))  # <class 'float'>
print(type(a.imag))  # <class 'float'.




# complex object

a = 6j  # Ref 'a' points to complex object 6j
print(a)  # 6j
print(type(a))  # <class 'complex'.
print(a.real)  # 0.0
print(a.imag)  # 6.0
# print(5 + j6)  # Error due to j is before imag
# print(3 + 4i)  # Error due to i
# print(4 + j)  # Error becoz imag is missing 
print(4 + 1j)  # 4 + 1j
print(4 + 0j)  # 4 + 0j 




# bool object demo program

a = True 
print(a)  # True
print(type(a))  # <class 'bool'>
print(id(a))  # Address of bool of 'a' 140721741267376
b = False 
print(b)  # False
print(type(b)) <class 'bool'>
print(True + True)  # 1 + 1 = 2
print(True + False)  # 1 + 0 = 1
print(False + True)  # 0 + 1 = 1
print(False + False)  # 0 + 0 = 0
print(True + True + True)  # 1 + 1 + 1 = 3
print(25+10.8+True)  # 36.8
print(True > False)  # True
print(True)  # True
print(False)  # False
# print(true)  # Error due to 't'
# print(false)  # Error due to 'f'




Nonetype object demo program 

a = None  # Ref 'a' points to object None 
print(type(a))  # <class 'Nonetype'>
print(a)  # Value of object 'a' i.e None 
print(id(a))  # Address of object None i.e !40721661510128
# print(id(none))  # Error due to 'n'
