
#Ex-1
# Find  outputs
import  time
class   c3:
	def  __iter__(self):
		print('__iter__  method ')
		return  reversed([10 , 20 , 15 , 18])
# End  of  the  class
itr = c3() # creating empty object
for  x  in   itr: # call ter method and return revered iterator
	print(x)  #  18 <nl> 15 <nl> 20 <nl> 10
	time . sleep(1)
# print(next(itr)) # Error there is no next element

#Ex-2
# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('_iter_  method ')
		return   self # Error because  return non - iterable  
# End  of  the  class
itr = c4() # creating empty iterator
for  x  in itr:
	print(x)

#Ex-3
# Identify  Error
class   c5:
	def  __iter__(self):
		print('_iter_  method ')  # Error because  there is no return None by default None is not iterable
# End  of  the  class
itr = c5()
for  x  in  itr:
	print(x)

#Ex-4
# Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6() # create empty object
print(dir(c6)) # list members of class , methods  and Environment variable
'''

for  x  in  a: # Error because a is not iterator
        print(x)
while  True:
	print(next(a)) # Error there is no __next__ method
a . next()
'''

#Ex-5
# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('_iter_    method') # _iter_    method ,second   _iter_    method
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1() # creating non-empty  object and initialize x value
print('Elements  of  iterator  with  for  loop') # Elements  of  iterator  with  for  loop
for   element   in   a: # call iter method  and return self after call __next__
	print(element) # 1 <nl> 2 <nl> 3 <nl> 4 <nl> 5
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a) # 6 <nl> to  10
	print(element)
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop') # Elements  of  iterator  with  for  loop
for   element   in    a: # again call iterator
	print(element)  # 11 to 15
	if  element ==15:
		break

#Ex-6
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
r = Remote() # create non-empty object  and initialize list
for   x    in    r: # call __iter__
	print(x) # T
	time . sleep(1)
