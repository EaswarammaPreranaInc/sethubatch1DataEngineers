# PROGRAM 1

# Find  outputs (Home  work)
a = 0O6247
print(a) # prints decimal number of a i.e.,3239
print(type(a)) # prints <class 'int'>
print(id(a)) # prints random address of a 
b = 0o6247
print(id(b)) # prints random address of b same as a
print(b) # prints decimal number of b i.e.,3239
c = 3239
print(c) # prints 3239
print(id(c)) # prints random address of c i.e.,same as a
#print(0o9248) # throws error as octal accept digits 0-7 but not 8 and 9.

# PROGRAM 2

# Find  outputs  (Home  work)
a = 0XA7B9
print(a) # prints decimal number of a i.e.,42937
print(type(a)) # <class 'int'>
b = 0xBEEF # b is assigned a decimal number of b i.e., 48879
print(b) # prints deciaml number of b 
#print(A7B9) # throws error as it is not defined or prefix is not there.
print('A7B9') # prints A7B9
#print(0XBEER) # throws error as hexadecimal accept 0-9,a to f, A to F.
#print(0XHYD) # throws error as hexadecimal accept 0-9,a to f, A to F.
#print(0xA7G9B) # throws error as hexadecimal accept 0-9,a to f, A to F.

#PROGRAM 3
# Find outputs (Home  work)
a = 9248
print(a) # prints 9248
print(type(a)) # <class 'int'>

#PROGRAM 4

#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # prints Rama Rao
print(type(a)) # prints <class 'str'>
print(id(a)) # prints random address of a
b = 'Hyd'
print(b) #prints Hyd 
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # prints Hyd is green city <nextline> Hyd is hitec city <next line> Hyd is beautiful city.

#PROGRAM 5
# Index   demo  program  (Home  work)
a = 'Hyd'
print(a[0])#print(How  to  print  'H'  of  object  'a')
print(a[1])#print(How  to  print  'y'  of  object  'a')# print(a[1])
print(a[2])#print(How  to  print  'd'  of  object  'a') print(a[2])
#print(a[3]) # throws error as index is out of range.
print(a[-1])#print(How  to  print  'd'  of  object  'a'  with  -ve  index)
print(a[-2])#print(How  to  print  'y'  of  object  'a'  with  -ve  index)
print(a[-3])#print(How  to  print  'H'  of  object  'a'  with  -ve  index)
#print(a[-4])# throws error as index is out of range
print(a[0] ==  a[-3]) #prints 1 as its True
#a[2] = 'c' # throw error as string is immutable
#print(25[0]) # throws error
print('25'[0])# prints 2
#print(True[1])# throws error as True is non sequence
print('True'[1])# prints r

#PROGRAM 6

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) #prints Hyd 3 times in a single line
print(a * 2) #prints Hyd 2 times in a single line
print(a * 1) # prints Hyd ina single line
print(a * 0)# prints nothing
print(a * -1)# prints nothing
print(25 * 3)# prints 75
print('25' * 3)# prints 25 3 times
#print('25' * 4.0) # throws error as float cannot be repeated on a string
print(3*'Hyd') # prints Hyd 3 times

#PROGRAM 7

# len()  function  (Home  work)
print(len('Hyd')) # prints 3
print(len('Rama Rao')) # prints 8
print(len('9247')) # prints 4
print(len('')) # prints 0
print(len(' ')) # prints 1
#print(len(689))# throws error

#PROGRAM 8

# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # prints "Hyd
print(len(a)) # prints 4
print(a[0]) # prints "
#print("""Hyd"""") # throws error
b = """""Hyd"""
print(b) # ""Hyd
print(len(b))# prints 5

#PROGRAM 9

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #prints from index 7 to 11 in steps of 1
print(a[7 : ]) # prints from index 7 to end of the string length
print(a[ : 6])# prints from 0 to 5 in steps of 1
print(a[ : ]) #   a[ 0 :  18 :  1]  --->  string  from  indexes  0  to   17  in  steps  of   1   ---> Sankar  Dayal  Sarma
print(a[:  : ]) # prints everything
print(a[1 : 10 : 2])# prints 1 to 9 in steps of 2
print(a[0 : : 2])# prints 0 to end of string length in steps of 2
print(a[1 : : 2])# prints 1 to end of string length in steps of 2
print(a[-5 : -1])# prints from index of -5 to -2 in steps of 1
print(a[::-1])  #  a[-1 : -19 : -1]  --->  string  from  indexes  1-  to   18  in  steps  of   -1   ---> Reverse string 
print(a[-1:-5:-1]) # prints from index -1 to  -4 in steps of -1
print(a[ : : -2]) # prints -1 to end of length string but in reverse of step -2
print(a[3 : -3])# prints index 3 to index -3 or index 1 in steps of 1
print(a[2 : -5])   #  a[2 : -5 :  1]  --->  string  from  indexes  2  to  -4   in  steps  of   1   --->  nkar<space>Dayal<space>
print(a[-1:-5])# prints from index -1 to -6 in steps of 1 but nothing prints here.
print(a[3 : 3])# prints nothing as 3 to 2 in steps of 1 is not there.
