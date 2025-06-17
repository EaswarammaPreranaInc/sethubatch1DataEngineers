# Find  outputs
import  time
class   c3:
	def  __iter__(self):
		print('__iter__  method ')
		return  reversed([10 , 20 , 15 , 18])
# End  of  the  class
itr = c3()
for  x  in   itr:
	print(x)
	time . sleep(1)
#print(next(itr))
"""
Output:
__iter__ method
18
15
20
10
"""

# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('__iter__  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:#Error is due to itr is returning none
	print(x)
"""
Output:
__iter__ method
"""

# Identify  Error
class   c5:
	def  __iter__(self):
		print('__iter__  method ')
# End  of  the  class
itr = c5()
for  x  in   itr:#Error due to itr is returning none type
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
for  x  in  a: #a is not iterable
        print(x)
while  True:
	print(next(a))
a . next()
"""
Output:
The output is the method of c6 class as list of strings
"""

# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('__iter__ method')
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
"""
Output:
Elements  of  iterator  with  for  loop
__iter__ method
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
__iter__ method
11
12
13
14
15
"""

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
r = Remote()
for   x    in  r:
	print(x)
	time . sleep(1)
"""
Output:
Tv 9
Espn
Zee Tv
ETV
"""

#Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20
#Hint: Use  for  loop
class c1:
	def __init__(self):
		self.x=9
	def __iter__(self):
		return self
	def __next__(self):
		self.x+=1
		if self.x<=20:
			return self.x
		raise StopIteration 
itr=c1()
for y in itr:
	print(y)
"""
Output:
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
"""

#Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7
#Use  for  loop
class c1:
	def __init__(self):
		self.y=0
	def __iter__(self):
		return self
	def __next__(self):
		self.y+=1
		if self.y<=7:
			result=2**self.y
			return result
		raise StopIteration
itr=c1()
for i in itr:
	print(i)
"""
Output:
2
4
8
16
32
64
128
"""
		
