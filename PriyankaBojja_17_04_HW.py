Q1 #Find  outputs
import  time
class   c3:
	def  __iter__(self):
		print('__iter__  method ')              #__iter__ method
		return  reversed([10 , 20 , 15 , 18])   
# End  of  the  class
itr = c3()
for  x  in   itr:
	print(x)          ##18 <\n> 15 <\n> 20 <\n> 10
	time . sleep(1)
print(next(itr))     #error - itr is not iterator because there is no __next__() method
#-----------------------------------------------------------------------------------------------------------------
Q2 #Identify  Error  (Home  work)

class   c4:
	def  __iter__(self):
		print('__iter__  method ')   #__iter__ method
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:   #error - class c4() is not itarable class due to no __next__() method
	print(x)
#--------------------------------------------------------------------------------------------------------------------
Q3 #Identify  Error

class   c5:
	def  __iter__(self):
		print('__iter__  method ')    
# End  of  the  class 
itr = c5()
for  x  in   itr:      #error -   __iter__() method returning None by default which is invalid, it must return iterator
	print(x)
#-----------------------------------------------------------------------------------------------------------------------
Q4 #Identify  Error

class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))  #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'iter', 'next']
#for  x  in  a:   #c6 object is not iterable due to no __iter__() and no __next__() methods in class c6()
#        print(x)
while  True:
	print(next(a))  #c6 object is not an iterator due to no __next__() method in class c6()
a . next()
#--------------------------------------------------------------------------------------------
Q5 #Find  outputs

class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('__iter__    method')
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1()
print('Elements  of  iterator  with  for  loop')
for   element   in   a:
	print(element)
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a)
	print(element)
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')
for   element   in    a:
	print(element)
	if  element  ==  15:
		break

OP-
Elements  of  iterator  with  for  loop
__iter__    method
1
2
3
4
5
Elements  of  iterator  with  next()  function
6
7
8
9
10
Elements  of  iterator  with  for  loop
__iter__    method
11
12
13
14
15
#-------------------------------------------------------------------
Q6 #Find  outputs

import   time
class  Remote:
	def    __init__(self):
		self . list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
		self . index = -1
	def   __iter__(self):
		return  self
	def   __next__(self):
		self . index += 1
		if   self . index  ==  len(self . list):
			raise  StopIteration
		return    self . list[self . index]
# End  of  the  class
r = Remote()
for   x    in    r:
	print(x)        #Tv 9   ESPN   Zee Tv   ETV
	time . sleep(1)
#------------------------------------------------------------------------------------------------------
Q7 #Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20
Hint: Use  for  loop

import time
class num():
	def __init__(self):
		self.x=9
	def __iter__(self):
		print('__iter__ method')
		return self
	def __next__(self):
		self.x+=1
		if self.x>20:
			raise StopIteration
		return self.x

itr=num()
for n in itr:
	print(n)
	time.sleep(1)

OP-
__iter__ method
10
11
12
13
14
15
16
17
18
19
20
#------------------------------------------------------------------------------------------------------
Q8 #Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7
Use  for  loop

import time
class power:
	def __init__(self):
		self.x=-1
	def __iter__(self):
		print('__iter__ method')
		return self
	def __next__(self):
		self.x+=1
		if self.x>7:
			raise StopIteration 
		return 2**self.x
itr=power()
for i in itr:
	print(i)
	time.sleep(1)


OP-
__iter__ method
1
2
4
8
16
32
64
128