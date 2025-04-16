# Find  outputs (Home  work)
a = 0O6247
print(a) # 3239
print(type(a)) # <class 'int'>
print(id(a)) # Address of a
b = 0o6247
print(id(b)) # same becoz of reference change  only Address of a
print(b) # 3239
c = 3239
print(c) # 3239
print(id(c)) # Same address of a and b becoz only reference change
#print(0o9248) # Error becoz of octol cannot have no 9
# Find  outputs  (Home  work)
a = 0XA7B9
print(a) # 42937
print(type(a)) # <class 'int'>
b = 0xBEEF
print(b) # 48879
#print(A7B9) # error
print('A7B9') # A7B9
#print(0XBEER) # Error due to R
#print(0XHYD) # Error due to Y
#print(0xA7G9B) # Error due to G
# Find outputs (Home  work)
a = 9248
print(a) # 9248
print(type(a)) # <class 'int'>
#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) # <class 'str'>
print(id(a)) # Address of a
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)
'''o/p: Hyd is green city.
        Hyd is hitec city.
        Hyd is beautiful city.'''
# Index   demo  program  (Home  work)
a = 'Hyd'
print(a[0])#How  to  print  'H'  of  object  'a'
print(a[1])#How  to  print  'y'  of  object  'a'
print(a[2])#How  to  print  'd'  of  object  'a'
#print(a[3]) # Error becoz of no index
print(a[-1])#How  to  print  'd'  of  object  'a'  with  -ve  index
print(a[-2])#How  to  print  'y'  of  object  'a'  with  -ve  index)
print(a[-3])#How  to  print  'H'  of  object  'a'  with  -ve  index)
#print(a[-4]) # Error becoz of no index
print(a[0] ==  a[-3]) # True
#a[2] = 'c' #str objt doesnt support item  assignment
#print(25[0]) # Error becoz of int have no index
print('25'[0]) # 2
#print(True[1]) # Error becoz of bool have no index
print('True'[1]) # r
#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) # HydHydHyd
print(a * 2) # HydHyd
print(a * 1) # Hyd
print(a * 0) # 
print(a * -1) # 
print(25 * 3) # 75
print('25' * 3) # 252525
#print('25' * 4.0) # Error becoz of float
print(3 * 'Hyd') # HydHydHyd
# len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('')) # 0
print(len(' ')) # 1
#print(len(689)) # error becoz of int
# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # "Hyd
print(len(a)) #  4
print(a[0]) # "
#print("""Hyd"""") # Error becoz of " after Hyd
b = """""Hyd"""
print(b) # ""Hyd
print(len(b)) # 5
# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # Dayal 
print(a[7 : ]) # Dayal Sarma
print(a[ : 6]) # Sankar
print(a[ : ]) #   a[ 0 :  18 :  1]  --->  string  from  indexes  0  to   17  in  steps  of   1   ---> Sankar  Dayal  Sarma
print(a[:  : ]) # Sankar Dayal Sarma
print(a[1 : 10 : 2]) # akrDy
print(a[0 : : 2]) # Sna aa am
print(a[1 : : 2]) # akrDylSra
print(a[-5 : -1]) # Sarm
print(a[::-1])  #  a[-1 : -19 : -1]  --->  string  from  indexes  1-  to   18  in  steps  of   -1   ---> Reverse string 
print(a[-1:-5:-1]) # amraS
print(a[ : : -2]) # aSlyDrka
print(a[3 : -3]) # kar Dayal Sa
print(a[2 : -5])   #  a[2 : -5 :  1]  --->  string  from  indexes  2  to  -6   in  steps  of   1   --->  nkar<space>Dayal<space>
print(a[-1:-5]) # empty
print(a[3 : 3]) # empty



#   0      1      2      3      4      5     6         7       8       9    10    11     12         13     14     15      16     17
#   S      a      n      k      a       r                D       a       y      a      l                   S       a       r       m       a
#  -18   -17  -16   -15  -14    -13  -12       -11     -10    -9    -8    -7    -6          -5      -4      -3      -2     -1