# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
#print('Dictionary  with  print  function')
#print(a)
#print(How  to  print  dictionary)
#print('Keys  of  dictionary')
print(a.keys)
'''print('Values  of  dictionary')
How  to  print  each  value  of  dictionary  with  for  loop
print('All  the  tuples  of  dict_items   object')
How  to  print  each  tuple  of  dictionary  with  for  loop
print('Elements  of  each   tuple')
How  to  print  elements  of  tuple   in  dictionary  with  for  loop
print('Keys  and  values  of  dictionary') How  to  print  each  key of  dictionary  with  for  loop  along   with  corresponding  value'''
#How  to  print  each  key of  dictionary  with  for  loop
for i in a:
	print(a.keys)
# Gift
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
     } # should not use indentation
print(type(a)) # error
print(a) #error
print(len(a))#error

#  Anonymous  object  demo  program
_ = 25 # an anonymous object _ has value of 25
print(_) # 25 is printed
print(type(_)) # class int
a , _ , c = 10 , 20 , 30 # a=10,_=20,c=30
print(a)#10
print(_)#20
print(c)#30
for  _  in  range(5): #range from 0,1,2,3,4
	print(_,"Hello")
	'''0 Hello
	   1 Hello
	   2 Hello
	   3 Hello
	   4 Hello '''

#  Find  outputs
a = 25 # reference a points to object 25
print(id(a)) #address of object is displayed
a = 35 # reference is modified to the object
print(id(a)) # address is displayed which is different 
	            # int is immutable thats why a new object is created and refernce is modified, and we get a new address


# Find  outputs (Home  work)
a = 25.7 # reference a points to object 25.7
print(id(a)) # address of object is shown 
print(a) # 25.7
a = 35.6 # a now pints to a new object 35.6 whose address will be changed
print(id(a)) # a new address is printed
print(a) # 35.6
b = True # b points to True
print(id(b)) # address of b 
b = False # b now points to False object
print(id(b)) # address of b is printed which is new one
c = None # c points to none 
print(id(c)) #address is shown 
c = None #  no change 
print(id(c)) # address of c is same 
#  Find  outputs (Home  work)
a = 'Hyd' # a points to str object 'Hyd'
print(id(a))# address of object is displayed
#a[1] = 'e'# error
a = 'Sec'# reference a of now points to new object Sec
print(id(a))# a new address is displayed
b = (10 , 20 , 15 , 18) # b points to tuple
print(id(b)) # address of b is displayed
#b[2] = 19 # error
b = (30 , 40 , 35 , 32) # b now points to a new tuple
print(id(b)) # address  of b is changed now
c = range(5) # c points to range object
print(id(c))# address of it is shown
#c[3] = 10 # error range is immutable object 
c = range(5) # a new c and object range are created
print(id(c)) # new address is shown though range is immutable it is not reusable.

# Find  outputs  (Home  work)
a = 25 # a points to object 25
b = 25 # b points to object 25
print(a  is  b) # reference of a is comapared with reference of b True is displayed 
c = 'Hyd' # c points to object hyd  
d = 'Hyd' # d points to same object hyd bcz string is reusable
print(c  is  d) #True
e = False 
f = False
print(e  is  f)# True
g = range(10)
h = range(10)
print(g is h)# False
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18] 
b = [10 , 20 , 15 , 18]
print(a  is  b) # False mutable objects are not reusable
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g is h) # True

# Find outputs (Home work)
print(10 + 20) #30
print(10.8 + 20.6) #30.14
print(3 + 4j + 5 + 6j) # error
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') #1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #(25,10.8,'Hyd',3+4j,True,None
print({10 , 20} + {30 , 40})# {10,20,30,40}
print({10 : 'Hyd'} + {20 : 'Sec'}) #{10:'Hyd',20:'Sec'}
print(range(4) + range(5)) #
print(10 + '20')  # error
print([10 , 20 , 30] + 5) #
print([10 , 20 , 30] + (40 , 50 , 60)) #
 loops for reverse list 
a=[25,10.8,'Hyd',True]
for i in range(1,len(a)+1): 
	print(a[-i])

for i in a[::-1]:
	print(i)
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
#print('Dictionary  with  print  function')
print(a)
print(*a) # when you extract only keys of the dictionary are printed

# how to print keys of Dictionary with for loop 

19 Feb HW
for i in  a :
	print(i)
 
 #OR we can also do it in another way

for i in a.keys() :
	 print(i)
#How  to  print  each  value  of  dictionary  with  for  loop

for i in a.values():
	print(i)

#How  to  print  each  tuple  of  dictionary  with  for  loop
for i in a.items():
	print(i)

#How  to  print  elements  of  tuple   in  dictionary  with  for  loop

for i in a.items():
	print(*i)
# How  to  print  each  key of  dictionary  with  for  loop  along   with  corresponding  value


for i in a.keys():
	print(i,a[i],sep="..")
