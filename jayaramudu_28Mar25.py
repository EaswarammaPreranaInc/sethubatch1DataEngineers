Ex-1
#   Find  outputs
def  f1():
	a = 3
	if  a > 0:
		print(a)
		a = a - 1 # a here local variable
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
f1() # print a value infinite times RecursionError because a does not modify in f1
print('End')

#Ex-2
# Find  outputs  (Home  work)
def  f1(x , y): # (10,11)  # (21,11) # (32,11)
	if   x > 40: # False # False  # False  #True
		return
	x += y  # x = 10+11=21  # x = 21+11=32 # x = 32+11= 42
	f1(x , y) # (21,11)     # (32,11)   # (43,11)
	print(x) # 42 32 21
    # stack next statement x = 21 is 1000 2nd next statement x = 32 is 2000  3rd next statement x = 43 is 3000
#End  of  the  function
x = 10
f1(x , x :=x+1) # # Call the function with x and updated x
print(x) # 11

#Ex-3
# Find  outputs   (Home  work)
def  f1(x):            # x=3       # x =2   # x=1         # x=0
	print(x)          # 3         # 2       1             # 0
	if   x:           # True      # True    #  True      # False
		f1(x - 1)    #f1(2)      # f1(1)    # f1(0)
	print(x)  # In stack x = 3   # x = 2     # x = 1   # x = 0
# End  of  the function
f1(3) # call f1

#Ex-4
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1())) # print 25 infinite loop because every time call new generator created

#Ex-5
#  How  to  iterate  generator  with  for  loop
import  time
def   f1():
	print('One') # 1st One
	yield  25 # return 25
	print('Two')  # 2nd Two
	yield  10.8 # return  10.8
	print('Three')  # 3r Three
	yield  'Hyd' # return Hyd
	print('Four') # four
# End  of  generator
g = f1() # create new generator with empty object
for   x   in   g:
	print(x)             # 25        # 10.8   # Hyd
	time . sleep(1)
	print('Hello')       # Hello     # Hello  # Hello
#  End  of  for  loop
print('End')
print(g) # type and address of generator object
# print(next(g)) # throws error StopIteration
g = f1() # create new generator with empty object
print(next(g)) # one 25

#Ex-6
# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1() # create new generator with empty object
print(next(g)) # 25
for  x  in   g: #  take next(g)
	print(x) # 10.8 <nl> Hyd
print()
for  x  in   f1(): # f1  creates a new generator
	print(x) # 25 <nl> 10.8 <nl> Hyd
print()
gen = f1() # creates a new generator
print(next(gen)) # 25
for  x  in   f1():  # f1  creates a new generator
	print(x)   # # 25 <nl> 10.8 <nl> Hyd
print(next(gen)) # 10.8

#Ex-7
#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5)) # creates empty generator
for  y  in   g: #
	print(y) #             # 0      1       4         9        16
	time . sleep(2)
	print('Hello')        # Hello  # Hello  # Hello   # Hello  # Hello
for  y  in g: # g in there is no next element
	print(y)

#Ex-8
# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)): # creates  generator with squares of  0 to 4
	print(y) # 0 <nl> 1  <nl> 4 <nl>  9  <nl> 16
	time . sleep(2) #   creates  new generator with squares of  0 to 4
for  y  in   (x * x   for    x    in    range(5)):
	print(y)  # 0 <nl> 1  <nl> 4 <nl>  9  <nl> 16
	time.sleep(2)

#Ex-9
# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5)) # creates  empty generator
g2 = g1 # g2 points to generator g1
for  y  in  g1:  # creates  generator with squares of  0 to 4
	print(y) #  0 <nl> 1  <nl> 4 <nl>  9  <nl> 16
	time . sleep(2)
for  y  in  g2: # g2 there is no values because in g1 there is no values, g2 points same generator g1
	print(y)
print(g1 is g2) # True because g2 points to generator g1

#Ex-10
#   Find  outputs
def  f1():
	global  a # global variable a =3
	if  a:                  # True                      # True            # True             # False
		print(a)            # 3                         # 2               # 1
		a = a - 1          # a = 3-1=2 modifies g v     # a = 2-1=1       # a = 1-1 = 0
		f1()
		print('Hello') # stack in print('Hello') print('Hi') print(a) print('Bye')
		print('Hi') # stack in print('Hello') print('Hi') print(a) print('Bye')
		print(a)    # # stack in print('Hello') print('Hi') print(a) print('Bye')
	print('Bye') # Bye
a = 3
f1()
print('End') # End

#Ex-11
#  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2 function')
f1() #  RecursionError there is no termination
