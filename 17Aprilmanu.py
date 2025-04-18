'''
#1)Find  outputs
import  time
class   c3:
	def  __iter__(self):
		print('__iter__  method ')
		return  reversed([10 , 20 , 15 , 18]) # reversed is a iterator.
# End  of  the  class
itr = c3()
for  x  in   itr: # There is __iter__ method in the class c3.
	print(x)
	time . sleep(1)
#print(next(itr)) # Error : There is no __next__ method in the class c3.

output:-
--------
_iter__  method
18
15
20
10



#2) Identify  Error  (Home  work)
class   c4:
	def  __iter__(self): # which prints __iter__ method and returns self.
		print('__iter__  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr: # Python now expects that itr has a __next__ method because it's being used as an iterator. Since there's no __next__ method defined, Python raises a TypeError:
	print(x) # TypeError: iter() returned non-iterator of type 'c4'

output:-
------------
TypeError

#3) Identify  Error

class   c5:
	def  __iter__(self): # Since your __iter__ method does not return anything, it implicitly returns None. The __iter__ method must return an iterator (an object that implements __next__).
		print('__iter__  method ')
# End  of  the  class
itr = c5()
for  x  in   itr: # for x in None: bcz __iter__ returns None 
	print(x) # TypeError: 'NoneType' object is not iterable

output:-
----------
TypeError

#4)Identify  Error

class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))
#for  x  in  a: # Since a does not implement __iter__,TypeError: 'c6' object is not iterable
        #print(x)
#while  True: # TypeError: 'c6' object is not an iterator
	#print(next(a))
a . next() # Error : write like this print(a.__next__())

output:-
---------
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'iter', 'next']
next  method

#5) Find  outputs(Home  work)

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

ouput:-
--------
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

#6) If we want to get from 1 onwards for every loop here.
class c1:
    def __init__(self):
        self.x = 1

    def __iter__(self):
        print('__iter__ method')
        self.x = 1  # Reset the counter every time iteration starts
        return self

    def __next__(self):
        value = self.x
        self.x += 1
        return value

# End of the class

a = c1()

print('Elements of iterator with for loop')
for element in a:
    print(element)
    if element == 5:
        break
print('Elements of iterator with next() function')
# Re-initialize to start from 1 again
a.__iter__()
while True:
    element = next(a)
    print(element)
    if element == 10:
        break

print('Elements of iterator with for loop')
for element in a:
    print(element)
    if element == 15:
        break

output:-
----------
Elements of iterator with for loop
__iter__ method
1
2
3
4
5
Elements of iterator with next() function
__iter__ method
1
2
3
4
5
6
7
8
9
10
Elements of iterator with for loop
__iter__ method
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

#7) Find  outputs (Home  work)


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
	print(x)
	time . sleep(1)


output:-
----------
Tv 9
Espn
Zee Tv
ETV


#8)Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

#Hint: Use  for  loop

class   c1:
	def   __init__(self):
		self . x =  10
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
	if  element  ==  20:
               break
	
output:-
-----------
Elements  of  iterator  with  for  loop
__iter__    method
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

(or)

class c1:
    def __iter__(self):
        print('__iter__ method')
        for i in range(10, 21):  # 21 because range is exclusive at the end
            yield i
a = c1()

# Loop through the iterator
for num in a:
    print(num)

output:-
-------------
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


#9)Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

#Use  for  loop

class c1:
    def __iter__(self):
        print('__iter__ method')
        for i in range(0, 8):  # 21 because range is exclusive at the end
            yield  2** i
a = c1()

# Loop through the iterator
for i in a:
    print(i)


output:-
----------
__iter__ method
1
2
4
8
16
32
64
128

#10)
class c1:
    def __init__(self):
        self.x = 0  # Start from exponent 0

    def __iter__(self):
        print('__iter__ method')
        self.x = 0  # Reset on each iteration
        return self

    def __next__(self):
        if self.x > 7:
            raise StopIteration
        value = 2 ** self.x
        self.x += 1
        return value

# End of class

a = c1()
print('Powers of 2 from 2^0 to 2^7:')
for element in a:
    print(element)


output:-
------------
Powers of 2 from 2^0 to 2^7:
__iter__ method
1
2
4
8
16
32
64
128

	