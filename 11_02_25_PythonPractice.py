# complex object demo program
a = 3 + 4j
print(a) # 3+4j
print(type(a)) # <class 'complex'>
print(id(a)) # Address of a
print(a . real) # 3.0
print(a . imag) # 4.0
print(type(a . real)) # <class 'float'>
print(type(a . imag)) # <class 'float'>
# Find outputs (Home work)
a = 6j
print(a) # 6j
print(type(a)) # <class 'complex'>
print(a . real) # 0.0
print(a . imag) # 6.0
#print(5 + j6) # Error due to 6 is after j
#print(3 + 4i) # Error due to i
#print(4+j) # Error becoz of number should be before j
print(4 + 1j) # 4+1j
print(4 + 0j) # 4+0j
# bool object demo program
a = True
print(a) # True
print(type(a)) # <class 'bool'>
print(id(a)) # Address of a
b = False
print(b) # False
print(type(b)) # <class 'bool'>
print(True + True) # 2
print(True + False) # 1
print(False + True) # 1
print(False + False) # 0
print(True + True + True) # 3
print(25 + 10.8 + True) # 36.8
print(True > False) # True
print(True) # True
print(False) # False
#print(true) # Error becoz of small t
#print(false) # Error becoz of small f