# Find  outputs
import  time
class   c3:
	def  _iter_(self):
		print('_iter_  method ')
		return  reversed([10 , 20 , 15 , 18])
# End  of  the  class
itr = c3()
for  x  in   itr:
	print(x)
	time . sleep(1)
print(next(itr))
# Identify  Error  (Home  work)
class   c4:
	def  _iter_(self):
		print('_iter_  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x)
# Identify  Error
class   c5:
	def  _iter_(self):
		print('_iter_  method ')
# End  of  the  class
itr = c5()
for  x  in   itr:
	print(x)
# Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))
for  x  in  a:
        print(x)
while  True:
	print(next(a))
a . next()
 # Find  outputs(Home  work)
class   c1:
	def   _init_(self):
		self . x =  1
	def   _iter_(self):
		print('_iter_    method')
		return  self
	def   _next_(self):
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
# Find  outputs (Home  work)
import   time
class  Remote:
	def    _init_(self):
		self . list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
		self . index = -1
	def   _iter_(self):
		return  self
	def   _next_(self):
		self . index += 1
		if   self . index  ==  len(self . list):
			raise  StopIteration
		return    self . list[self . index]
# End  of  the  class
r = Remote()
for   x    in    r:
	print(x)
	time . sleep(1)