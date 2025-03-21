# PROGRAM 1
# int()  function  demo  program
print(int(10.8)) #  Converts  10.8  to  10
print(int(True))  #  Converts  True  to  1
print(int(False))# Converts False to 0
print(int('25'))# Converts 25 to 25 itself
print(int('0075'))# Converts 0075 to 75
print(int(0B11010))# Converts decimal expansion of this binary number
print(0B11010)# Converts decimal expansion of this binary number
print(int(0O6247))# Converts decimal expansion of this octal number
print(0O6247)# Converts decimal expansion of this octal number
print(int(0XA7B9))# Converts decimal expansion of this hexadecimal number
print(0XA7B9)# Converts decimal expansion of this hexadecimal number
#print(int(3+4j)) throws error as 3+4j cannot be converted to integer
#print(int('25.4')) throws error as string 25.4 cannot be converted to interger
#print(int('Ten')) throws error as string cannot be converted to integer

# PROGRAM 2
# float()  function  demo  program
print(float(25)) #  Converts  25  to  25.0
print(float(True)) #  Converts   True   to   1.0
print(float(False))# Converts False to 0.0
print(float('92'))# Converts 92 to 92.0
print(float('36.4'))# Converts 36,4 to 36.4 itself.
print(float('0075'))# Converts 0075 to 75.0
print(float(0B1010101)) # Converts to floating decimal expansion of this binary number 
print(float(0O6247)) # Converts to floating decimal expansion of this octal number
print(float(0XA7B9))# Converts to floating decimal expansion of this hexadecimal number
#print(float(3 + 4j))# throws error as complex object cannot be converted to float type object.
#print(float('Ten'))# throws error as string bool type object cannot be converted to float type object.

#PROGRAM 3
# complex()  function  demo  program
print(complex(3 , 4))# prints 3+4j in tuple as real and imag positions are immutable
print(complex(0 , 4))# prints 0+4j i.e., 4j
print(complex(3))# prints (3+0j)
print(complex(3.8 , 4.6))# prints (3.8+4.6j)
print(complex(3.8))# prints (3.8+0j)
print(complex(3 , 4.5))# prints (3+4.5j)
print(complex(True , False))# prints (1+0j)
print(complex(True))# prints (1+0j)
print(complex(False))# prints 0j
print(complex(True , 4))# prints (1+4j)
print(complex('3'))# prints (3+0j)
print(complex('3.8'))# prints (3.8+0j)
#print(complex(3 , '4'))# throws error as multitype data is not acceptable by complex type object.
#print(complex('3' , 4))# throws error as multitype data is not acceptable by complex type object.
#print(complex('3' , '4'))#throws error as string type data is not acceptable by complex type object.
#print(complex('Ten'))# string type not acceptable in complex()

#PROGRAM 4
#  bool()  function  demo  program
print(bool(0)) #   Converts  0  to  False
print(bool(10))#  Converts  10  to True
print(bool(-25))#  Converts  -25  to True
print(bool(0.0))#   Converts  0.0  to  False
print(bool(0.1))#  Converts  0.1 to True
print(bool(0 + 0j))#   Converts  0+0j  to  False
print(bool(10 + 20j))#   Converts  10+20j  to  True
print(bool(-15j))#   Converts  -15j  to  True
print(bool('False'))#   Converts  'False'  to  True
print(bool(''))#   Converts  ''  to  False
print(bool('Hyd'))#   Converts  'Hyd'  to  True
print(bool(' '))# Converts ' ' to True
print(bool('True'))# Converts True to True

#PROGRAM 5
# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))# prints 10.8
print(str(3 + 4j))# prints 3+4j
print(str(True))# prints True
print(str(False))# prints False
print(str(None))# prints None

#PROGRAM 6
# oct()  function  demo  program
print(oct(195))# converts 195 to octal number of the 0o or 0O
print(oct(0B10101110010))# converts binary to octal
print(oct(0xA7B9))# converts hexadecimal to octal

#PROGRAM 7
# hex()  function  demo  program
print(hex(25))# converts decimal to hexadecimal
print(hex(0B10101111010111))# converts binary to hexadecimal
print(hex(0O6247))# converts octal to hexadecimal

#PROGRAM 8
# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a))# <class 'range'>
print(a)# prints range(10, 50, 5)
print(*a)# unpacks and prints elements 10 to 49 in steps of 5 i.e., 10 15 20 25 30 35 40 45
print(id(a))# prints a random address
print(len(a))# length 8
print(*a[2 : 7] , sep = ' , ')# prints index from 2 to 6 in steps on 1 sepereated by ','
print(*a[ : : -1])# prints elements in reverse order
#a[4] =32# throws error as range can not be modified
#print(a*2)#throws error as range cannot be repeated.

#PROGRAM 9
#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')# prints elements 10 to 19 in steps of 1 (default step)
b = range(5)
print(*b)# prints 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')# prints elements 10 to 2 in reverse order
d = range(-10 , 0)
print(*d)# prints elements -10 to -1 in steps of 1
e = range(-10)
print(*e)#prints nothing as 0 to -10 in steps of 1 gives no elements
f = range(2 , 2)
print(*f)# prints nothing as 2 to 1 is not possible.
#g = range(10 , 11 , 0.1)# throws error as float is not acceptable in range.
#h = range('A','F')# string is not acceptable to form list of elements unlike integers.

#PROGRAM 10
#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)# prints entire list of elements 'a' in []
print(*a)# prints only the elements of a
print(type(a))# <class 'list'>
print(id(a))# prints random address
print(len(a))#  prints the length of list is 8
a[2] = 'Sec'# 'Hyd' is replaced with 'Sec'
print(a)# prints entire list of 'a' with updated modification 
print(a[2:5])# prints the elements from 2 to 4 in steps of 1

#PROGRAM 11
# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # prints []
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)# prints the added elements respectively
a . remove('Hyd')# removes 'Hyd' from list
print(a)# prints list 'a' with modification
#a . remove('25')# throws error as string 25 is not in list
print(a)# prints entire list 'a' with updated modification

#PROGRAM 12
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a * 3)# prints list 3 times
print(a * 2)# prints list 2 times
print(a * 1)# print list a
print(a * 0)# prints empty list
print(a * -1)# prints empty list
#print(a*4.0)# throws error as 4.o float cannot be repeated upon list.

#PROGRAM 13
# list()  function  demo  program
a = list('Hyd')
print(a)  # prints ['H','y','d']
print(type(a)) # <class'list'>
print(len(a)) # string length 3
b = (10 , 20 , 15 , 18)
print(list(b))# prints list b 
print(list(range(5)))# prints range(5) in list
#print(list(25))# int object cannot be iterable

#PROGRAM 14
# Find  outputs
a = [ ]
print(type(a))# <class'list'>
print(a)# prints []
print(len(a))# prints 0
b = list()
print(b)# prints []
print(len(b))# prints 0

#PROGRAM 15
# Slice  demo  program (Home  work)

list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']

print(list[2 : 7])# prints elements from 2 to 6
print(list[ : : ])# print entire list
print(list[:])# prints entire list
print(list[ : : -1])# prints entire list in reverse order
print(list[ : : 2])# prints list from 0 to end of list in steps of 2
print(list[1 : : 2])# prints 1 to end of list in steps of 2
print(list[ : : -2])# prints reverse list in steps of -2
print(list[-2 : : -2])# prints -2 to end of list in steps of -2
print(list[1 : 4])# prints list from 1 to 3 
print(list[-4 : -1])# prints elements
print(list[3 : -3])  #  print(list[3 : -3 : 1])  --->  List  from  indexes  3  to  -4 in  steps of  1  i.e. ['Hyd' , True]
print(list[2 : -5])# prints (3+4j)
print(list[-1:-5])# prints nothing as -1 to -4 in steps of 1 is not possible

#PROGRAM 16
#  Find  outputs  (Home  work)

list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)# prints x : list[3]
print('y : ' , y)# prints y : list[4]
for  x  in  list[2:7]:
	print(x)# prints elements from 2 to 6 line by line

#PROGRAM 17
#  Find  outputs  (Home  work)

a = [10 , 20 , 30 , 40 , 50]
print(a)# prints list 'a'
a[1 : 4] = [60 , 70,80]
print(a)# modifies list of elments 1,2,3 to new list updated and prints accordingly.

#PROGRAM 18
#  Find  outputs  (Home  work)
a =  [25]
#print(a[1])# throws error as only element is available
print(a[1:])# prints empty list

#PROGRAM 19
#  Find  outputs (Home  work)
list  =  [10 , 20 , 15 , 12 , 18]
print(15   in   list)# prints True
print(19   in   list)# prints False
print(14  not  in  list)# prints True
print(12  not  in  list)# prints False



