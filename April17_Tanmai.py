
# Find  outputs
import  time
class   c3:
	def  __iter__(self):
		print('_iter_  method ')
		return  reversed([10 , 20 , 15 , 18])
# End  of  the  class
itr = c3()
for  x  in   itr: # for x in reversed([10 , 20 , 15 , 18])
	print(x) # 18 <nl> 15 <nl>  20 <nl> 10
	time . sleep(1)
#print(next(itr))# error no __next__() it is not a iterator

# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('_iter_  method ')
		return   self # not returning iterator 
# End  of  the  class
itr = c4()
#for  x  in   itr: # error it is not iteratable bcz __iter__() is not returning an iterator 
	#print(x) 
# Identify  Error
class   c5:
	def  __iter__(self): # must reeturn an iterator 
		print('_iter_  method ')
# End  of  the  class
itr = c5()
#for  x  in   itr:  # iter() returned non-iterator of type 'NoneType'
	#print(x)
# Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))
#for  x  in  a: # not iteratable 
        #print(x)
#while  True:
	#print(next(a)) # not a iterator 
a . next() # next method  

# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('_iter_    method')
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1() # a.x=1
print('Elements  of  iterator  with  for  loop') # Elements  of  iterator  with  for  loop
for   element   in   a: # a is replaced with iterator a 
	print(element) # 1 2 3 4 5 
	if  element  ==  5:
               break 
print('Elements  of  iterator  with  next()  function') # Elements  of  iterator  with  next()  function
while    True:
	element = next(a) 
	print(element) # 6 7 8 9 10
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop') #Elements  of  iterator  with  for  loop
for   element   in    a:
	print(element) #  11 12 12 14 15
	if  element  ==  15:
		break 
# Find  outputs (Home  work)
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
r = Remote() # r.list r.index
for   x    in    r:
	print(x) # Tv 9   'Espn'  'Zee Tv'  'ETV'
	time . sleep(1) 
'''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
import time
class c1:
	def __init__(self):
		self.x=10
	def __iter__(self):
		return self
	def __next__(self):
		value=(self.x)
		self.x+=1
		if self.x>21:
			raise StopIteration 
		return value
a=c1()
for x in a:
	print(x)
	time.sleep(1)
'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Use  for  loop
'''
import time
class c1:
	def __init__(self):
		self.x=0
	def __iter__(self):
		return self
	def __next__(self):
		value=(self.x)
		self.x+=1
		if self.x>8:
			raise StopIteration 
		return 2**value
a=c1()
for x in a:
	print(x)
	time.sleep(1)
