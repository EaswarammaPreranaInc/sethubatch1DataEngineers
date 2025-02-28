# Find  outputs (Home  work)
a = 0O6247 # reference a points to object deminal equivalent ( decimal equivalent is displayed )
print(a) # 3239 ( decimal equivalent)
print(type(a)) # class int
print(id(a)) # address of object decimal equivalent
b = 0o6247 # reference b points to object decimal equivalent
print(id(b)) # same address because the object is same it has same address 
print(b) # 3239 ( decimal equivalent)
c = 3239 # decimal number ( integer)
print(c) # 3239
print(id(c)) # same address because the object is same it has same address 
#print(0o9248) # Invalid should not use 8,9 in a octal number 


# Find  outputs  (Home  work)
a = 0XA7B9 #  reference a points to object deminal equivalent ( decimal equivalent is displayed ) < hexadecimal is converted to decimal> 
print(a) # 42937
print(type(a)) # class int
b = 0xBEEF #reference b points to object decimal equivalent
print(b)# 48879
#print(A7B9)# Invalid becuase 0X is not used as perfix
print('A7B9') # A7B9
#print(0XBEER) # invalid
#print(0XHYD) # invalid
#print(0xA7G9B) # invalid


# Find outputs (Home  work)
a = 9248 # refernce a points to decimal equivalent 9248
print(a) #9248
print(type(a)) # class int

#  Find  outputs  (Home  work)
a = "Rama Rao" # reference a points to string Rama Rao
print(a) # Rama Rao
print(type(a)) # class string
print(id(a)) # address of object string
b = 'Hyd'# refernce b points to object string 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.''' #mutli line string which in triple quotes. reference c points to multi line string object
print(c)
 '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.''' 


# Index   demo  program  (Home  work)
a = 'Hyd' # reference a points to string object Hyd 
#print(How  to  print  'H'  of  object  'a') 
print(a[0])
#print(How  to  print  'y'  of  object  'a')
print (a[1])
##print(How  to  print  'd'  of  object  'a')
print(a[2])
#print(a[3]) # invalid
#print(How  to  print  'd'  of  object  'a'  with  -ve  index)
print(a[-1])
#print(How  to  print  'y'  of  object  'a'  with  -ve  index)
print(a[-2])
#print(How  to  print  'H'  of  object  'a'  with  -ve  index)
print(a[-3])
#print(a[-4]) # invalid 
print(a[0] ==  a[-3]) # True Both of them return H
#a[2] = 'c' # False
#print(25[0]) # invalid
print('25'[0])#2
#print(True[1])# invalid
print('True'[1])#r

# Find  outputs
a = 'Sankar Dayal Sarma' # reference a points to string Sankar Dayal sarma
print(a[7 : 12]) # a[7:12:1]---> string from index 7 to 11 in strps of 1 ---> Dayal
print(a[7 : ]) # a[7:18:1] --> string from index 7 to 17 in steps of 1 ---> Dayal Sarma
print(a[ : 6]) # a[0:6:1] ---> string from index 0 to 5 in steps of 1 ---> Sankar
print(a[ : ]) #   a[ 0 :  18 :  1]  --->  string  from  indexes  0  to   17  in  steps  of   1   ---> Sankar  Dayal  Sarma
print(a[:  : ]) # a[0:18:1] --> string from index 0 to 17 in steps of 1 --> Sankar Dayal Sarma
print(a[1 : 10 : 2]) # string from indexes 1 to 9 in steps of 2 --> akrDy
print(a[0 : : 2])#a[0:18:2] --> string from indexes 0 to 17 in steps of 2 --> Sna aa am
print(a[1 : : 2])#a[1:18:2] --> string from indexes 1 to 17 in steps of 2 --> akrDylSra
print(a[-5 : -1])# a[-5:-1:1] --> string indexes -5 to -2 in steps of 1 --> Sarm
print(a[::-1])  #  a[-1 : -19 : -1]  --->  string  from  indexes  1-  to   -18  in  steps  of   -1   ---> Reverse string 
print(a[-1:-5:-1]) # string from indexes -1 to -4 in steps of -1 --> amra
print(a[ : : -2])# a[-1:-19:-2] --> string from indexes -1 to -18 in steps of 2 --> arSlyDrka
print(a[3 : -3]) # a[3:-3:1] --> string from indexes 3 to -4 in steps  of 1 --> kar Dayal Sa
print(a[2 : -5])   #  a[2 : -5 :  1]  --->  string  from  indexes  2  to  -6   in  steps  of   1   --->  nkar<space>Dayal<space>
print(a[-1:-5]) # a[-1:-5:1] --> string from indexes -1 to -6 in steps of -1 -->  no output bcz start index is greater than end index
print(a[3 : 3])# a[3:3:1] --> string indexes from 3 to 2 in steps of 1 -->  no output 



