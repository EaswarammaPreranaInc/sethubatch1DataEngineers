# int()  function  demo  program
print(int(10.8)) #  Converts  10.8  to  10
print(int(True))  #  Converts  True  to  1
print(int(False)) # Converts False to 0
print(int('25')) # Converts '25' to 25
print(int('0075')) # Converts '0075' to 75
print(int(0B11010)) # 26
print(0B11010) # 26
print(int(0O6247)) # 3239 
print(0O6247) # 3239
print(int(0XA7B9)) # 42937
print(0XA7B9) # 42937
#print(int(3 + 4j)) # Error: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#print(int('25.4')) # Error: invalid literal for int() with base 10: '25.4'
#print(int('Ten')) # Error becoz string character cannot convert to int




#int()  function

# What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer
# float()  function  demo  program
print(float(25)) #  Converts  25  to  25.0
print(float(True)) #  Converts   True   to   1.0
print(float(False)) # converts False to 0.0
print(float('92')) # Converts '92' to 92.0
print(float('36.4')) # Converts '36.4' to 36.4
print(float('0075')) # Converts '0075' to 75.0
print(float(0B1010101)) # 85.0
print(float(0O6247)) # 3239.0
print(float(0XA7B9)) # 42937.0
#print(float(3 + 4j)) # Error becoz float() argument must be a string or a real number, not 'complex'
#print(float('Ten')) # Error becoz 'Ten' to cannot float





#float()   function

# 1) What  does  float(x)  do  ?  --->  Converts  object  'x'  to  float
# complex()  function  demo  program
print(complex(3 , 4)) # 3+4j
print(complex(0 , 4)) # 4j
print(complex(3)) # 3+0j
print(complex(3.8 , 4.6)) # 3.8 + 4.8j
print(complex(3.8)) # 3.8 + 0j
print(complex(3 , 4.5)) # 3+4.5j
print(complex(True , False)) # 1+0j
print(complex(True)) # 1+0j
print(complex(False)) # 0+0j
print(complex(True , 4)) # 1+4j
print(complex('3')) # 3+0j
print(complex('3.8')) # 3.8 +0j
#print(complex(3 , '4')) # Error: complex() second arg can't be a string
#print(complex('3' , 4)) # Error: complex() can't take second arg if first is a string
#print(complex('3' , '4')) # Error: complex() can't take second arg if first is a string
#print(complex('Ten')) # Error: complex() arg is a malformed string
#  bool()  function  demo  program
print(bool(0)) #   Converts  0  to  False
print(bool(10)) # Converts 10 to True
print(bool(-25)) # Converts -25 to True
print(bool(0.0)) # Converts 0.0 to False
print(bool(0.1)) # Converts 0.1 to True
print(bool(0 + 0j)) # False
print(bool(10 + 20j)) # True
print(bool(-15j)) # True
print(bool('False')) # True
print(bool('')) # False
print(bool('Hyd')) # True
print(bool(' ')) # True
print(bool('True')) # True



# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8)) # 10.8 to '10.8'
print(str(3 + 4j)) # 3+4j to '3+4j'
print(str(True)) # True to 'True
print(str(False)) # False to 'False'
print(str(None)) # 'None'



#What  does  str(x)  do ?  --->  Converts  object  'x'  to  string

# oct()  function  demo  program
print(oct(195)) # 0o303
print(oct(0B10101110010)) # 0o2562
print(oct(0xA7B9)) # 0o123671

#oct()  function

#1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where  
#								                    'x'  can  be  binary / decimal / hexa-decimal  number
print(hex(25)) # 0x19
print(hex(0B10101111010111)) # 0x2bd7

a = range(10 , 50 , 5)
print(type(a)) # <class 'range'>
print(a) # range(10,50,5)
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) # Address of a
print(len(a)) # 8
print(*a[2 : 7] , sep = ' , ') # 20 , 25 , 30 , 35 , 40
print(*a[ : : -1]) # 45 40 35 30 25 20 15 10
#a[4] = 32 # Error: 'range' object does not support item assignment
#print(a * 2) # Error: unsupported operand type(s) for *: 'range' and 'int'
#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e) # empty
f = range(2 , 2)
print(*f) # empty
#g = range(10 , 11 , 0.1) # Error: 'float' object cannot be interpreted as an integer
#h = range('A' , 'F') # Error: 'str' object cannot be interpreted as an integer
#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # 25 10.8 Hyd True 3+4j None Hyd 25
print(type(a)) # <class 'list'>
print(id(a)) # Address of a
print(len(a)) # 8
a[2] = 'Sec' # Modify index 2
print(a) # [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) # ['Sec',True,3+4j]
# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # [ ]
a . append(25) # [25]
a . append(10.8) # [25,10.8]
a . append('Hyd') # [25,10.8,'Hyd']
a . append(True) # [25,10.8,'Hyd',True]
print(a) # [25,10.8,'Hyd',True]
a . remove('Hyd')
print(a) # [25,10.8,True]
#a . remove('25') # Error: list.remove(x): x not in list
print(a) # [25, 10.8, True]
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd'] 
print(a * 3) # [25,10.8,'Hyd',25,10.8,'Hyd',25,10.8,'Hyd']
print(a * 2) # [25,10.8,'Hyd',25,10.8,'Hyd']
print(a * 1) # [25,10.8,'Hyd']
print(a * 0) # empty []
print(a * -1) #  empty []
#print(a * 4.0) # error becoz of float
# list()  function  demo  program
a = list('Hyd')
print(a)  # ['H','y','d']
print(type(a)) # <class 'list'>
print(len(a)) # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # [10,20,15,18]
print(list(range(5))) # [0,1,2,3,4]
#print(list(25)) # error becoz it should be sequence





# Find  outputs
a = [ ]
print(type(a)) # <class 'list'>
print(a) # []
print(len(a)) # 0
b = list() 
print(b) # []
print(len(b)) # 0
# Slice  demo  program (Home  work)
#        0      1          2         3           4         5       6          7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8      -7       -6          -5        -4       -3      -2         -1
print(list[2 : 7]) # [3+4j,'Hyd',True,None,10.8]
print(list[ : : ]) # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # ['Hyd',10.8,None,True,'Hyd',3+4j,10.8,25]
print(list[ : : 2]) # [25,3+4j,True,10.8]
print(list[1 : : 2]) # [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) # ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2]) # [10.8, True, (3+4j), 25]
print(list[1 : 4]) # [True, None, 10.8]
print(list[-4 : -1]) # ['Hyd', True]
print(list[3 : -3])  #  print(list[3 : -3 : 1])  --->  List  from  indexes  3  to  -4 in  steps of  1  i.e. ['Hyd' , True]
print(list[2 : -5]) # [(3+4j)]
print(list[-1:-5]) # []
#  Find  outputs  (Home  work)
#        0      1         2        3          4         5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) # x :  Hyd
print('y : ' , y) # y :  True
for  x  in  list[2:7]:
	print(x) # Hyd <next line> True <next line> None <next line> 10.8	
#  Find  outputs  (Home  work)
#     0    1      2     3     4
a = [10 , 20 , 30 , 40 , 50]
print(a) # [10, 20, 30, 40, 50]
a[1 : 4] = [60 , 70 , 80]
print(a) # [10, 60, 70, 80, 50]
#  Find  outputs  (Home  work)
a =  [25]
#print(a[1]) # Error: list index out of range
print(a[1:]) # []
#  Find  outputs (Home  work)
list  =  [10 , 20 , 15 , 12 , 18]
print(15   in   list) # True
print(19   in   list) # False
print(14  not  in  list) # True
print(12  not  in  list) # False



