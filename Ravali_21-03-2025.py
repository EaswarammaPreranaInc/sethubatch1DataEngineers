#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) # [10, 20, 15, 18]
change(a) 
print(a) #[10,17,18,25]

'''
step by step
change(a):
	a.append(25) # [10,20,15,18,25]
	a[2] = 17 # [10,20,17,18,25]
	del a[1] # [10,17,18,25]
'''

# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) # [10 , 20 , 30, 40]
change(a) # [50, 60, 70, 80]
print(a) # [10, 20, 30, 40]


#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10 
print(x) # 10
f1(x) # 20
print(x) # 10

#  Find  outputs  (Home  work)
def  f1(b):
	#b[2] = 25 # Error because tuple is immutable
	pass
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20, 15 , 18 )
f1(a)
print(a) # (10 , 20 , 15 , 18)
