# Find  outputs
'''import  time
class   c3:
	def  __iter__(self):
		print('__iter__  method ')
		return  reversed([10 , 20 , 15 , 18])
# End  of  the  class
itr = c3()
for  x  in   itr:
	print(x) #'__iter__  method ' 18 15 20 10
	time . sleep(1)
print(next(itr))#Error 

# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('__iter__  method ')
		return self
			
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x)# error becoz __iter__ returns iterator but class c4 does not contain __next__()

# Identify  Error
class   c5:
	def  __iter__(self):
		print('__iter__  method ')
# End  of  the  class becoz it returns Nonetype but not iterator becoz __next__() not in c5 class
itr = c5()
for  x  in   itr:
	print(x)#error

# Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def   next(self):
                 print('next  method')
		         
# End  of  the  class
a  =  c6()
print(dir(c6))
a.next()

for  x  in  a:
        print(x)
while  True:
	print(next(a))
a . next()

# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('__iter__    method')
		return  self
	def   __next__(self):
		value =  self . x #
		self . x  +=  1 #6
		return  value
# End  of  the  class
a = c1() #object a is created and having varible x with value 1
print('Elements  of  iterator  with  for  loop')
for   element   in   a: #a is a i.e for element in a
	print(element) #1 2 3 4 5
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a)
	print(element) #6 7 8 9 10
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')
for   element   in    a:
	print(element) #11 12 13 14 15
	if  element  ==  15:
		break

# Find  outputs (Home  work)
import   time
class  Remote:
	def    __init__(self):
		self . list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
		self . index = -1 #-1
	def   __iter__(self): #self is r
		return  self
	def   __next__(self):
		self . index += 1 #-1+1==0+1==1
		if   self . index  ==  len(self . list):
			raise  StopIteration
		return    self . list[self . index]
# End  of  the  class
r = Remote() #object r is created 
for   x    in    r:
	print(x) #'Tv 9' 'Espn' , 'Zee Tv' , 'ETV'
	time . sleep(1)

Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop

class c1:
		def __init__(self):
				self.x=9
		
		def __next__(self):
				self.x+=1
				if self.x<=20:
					 print('__next__ method()')
					 return self.x
				raise stopiteraton
a=c1()
while True:
	try:
		print(next(a))
	except:
		break
output--
__next__ method()
10
__next__ method()
11
__next__ method()
12
__next__ method()
13
__next__ method()
14
__next__ method()
15
__next__ method()
16
__next__ method()
17
__next__ method()
18
__next__ method()
19
__next__ method()
20


Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Use  for  loop
'''
class c1:
	
	def __iter__(self):
			print('powers of 2')
			return (pow,range(9))
a=c1()
for y in a:
	print(y)
'''output---
powers of 2
1
2
4
8
16
32
64
128
'''
