#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)
change(a)
print(a)
'''
OUTPUT:
[10, 20, 15, 18]
[10, 17, 18, 25]
'''

# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)
change(a)
print(a)
'''
OUTPUT:
[10, 20, 30, 40]
[50, 60, 70, 80]
[10, 20, 30, 40]
'''


#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)
f1(x)
print(x)
'''
OUTPUT:
10
20
10
'''


#  Find  outputs  (Home  work)
def  f1(b):
	#b[2] = 25        #Error because 'tuple' object does not support item assignment
	pass
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)
f1(a)
print(a)
'''
OUTPUT:
(10, 20, 15, 18)
(10, 20, 15, 18)
'''