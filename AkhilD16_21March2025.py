#1.Find  outputs  (Home  work)
def  change(b):
	b . append(25)        # 25 is appended to the list 'b' at the end	
	b[2] = 17		# 25 is appended to the list 'b' at index 2
	del  b[1]		# 20 is deleted which is present at index 1 in the list 'b'
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)	# [10,20,15,18]
change(a)	# Function Call..
print(a)	# [10,17,18,25]

#2.Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]	# Local Variable is created a list of 4 elements
	print(b)					# [50,60,70,80]
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)	# [10,20,30,40]
change(a)	# Function Call....	
print(a)	# [10,20,30,40]

#3.Find  outputs  (Home  work)
def   f1(x):
	x = 20		# Local Variable 'x' is created with value 20 
	print(x)	# 20
# End  of   the   function
x = 10
print(x)	# 10
f1(x)		# Function Call....
print(x)	# 10

# 4.Find  outputs  (Home  work)
def  f1(b):
	#b[2] = 25	# Error.....tuple is immutable object, hence doesn't supports assignment operator
	pass
#end  of  the  function
a = (10 , 20 , 15 , 18)	# Global Variable is created with tuple of 4 elements
print(a)				# (10 , 20 , 15 , 18)
f1(a)					# Function Call...
print(a)				# (10 , 20 , 15 , 18)

