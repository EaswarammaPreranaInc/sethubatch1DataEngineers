# Find  outputs
import  time
class   c3:
	def  __iter__(self):
		print('_iter_  method ')
		return  reversed([10 , 20 , 15 , 18])
# End  of  the  class
itr = c3()
for  x  in   itr:
	print(x)
	time . sleep(1)
#print(next(itr))
'''
Output:
_iter_ method
18
15
20
10
'''
# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('_iter_  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in itr:
	print(x)
'''
Output:
_iter_  method
iterator has to be returned but no iterator
'''
# Identify  Error
class   c5:
	def  __iter__(self):
		print('_iter_  method ')
# End  of  the  class
itr = c5()
for x in itr:
	print(x)
'''
Output:
_iter_  method 
itr returning none but object for for loop has to be iterator
'''
# Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a=c6()
print(dir(c6))
for  x  in  a:
        print(x)
while  True:
	print(next(a))
a.next()
'''
Output:
c6 is not iterable
and is not iterator
'''
# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('_iter_    method')
		return  self
	def  __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
a = c1()
print('Elements  of  iterator  with  for  loop')
for   element   in   a:
	print(element)
	if  element==5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a)
	print(element)
	if  element==10:
		break
print('Elements  of  iterator  with  for  loop')
for   element   in    a:
	print(element)
	if  element==15:
		break
'''
Output:
Elements  of  iterator  with  for  loop
_iter_    method
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
11
12
13
14
15
'''
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
		if   self.index==len(self . list):
			raise  StopIteration
		return    self.list[self . index]
# End  of  the  class
r = Remote()
for   x    in    r:
	print(x)
	time.sleep(1)
'''
Output:
Tv 9
Espn
Zee Tv
ETV
'''
'''
PROGRAM:

Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
class sol:
	def __iter__(self):
		self.first=int(input("enter starting number :"))
		self.last=int(input("enter starting number :"))
		print(self.first)
		return self
	def __next__(self):
		if self.first<self.last:
			self.first+=1
			return self.first
		else:
			raise StopIteration
a=sol()
for i in a:
	print(i)
'''
Output:
enter starting number :10
enter starting number :20
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
'''
'''
PROGRAM :
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Use  for  loop
'''
class c1:
	def __iter__(self):
		self.x=-1
		return self
	def __next__(self):
		if self.x<=7:
			self.x+=1
			return 2**self.x
		else:
			raise StopIteration
if __name__=="__main__":
	a=c1()
	for i in a:
		print(i)
'''
Output:
1
2
4
8
16
32
64
128
256
'''
