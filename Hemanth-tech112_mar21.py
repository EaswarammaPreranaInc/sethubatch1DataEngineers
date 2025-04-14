#  Find  outputs  (Homework)
def  change(b):  # Ref 'b' changes to 'a'
	b . append(25)  # 25 appended to list 'a'
	b[2] = 17  # modifies the element at index 2   i.e. 17
	del  b[1]  # deletes the element at the index 1
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)  # [10,20,15,18]
change(a)  # [10,17,18,25]
print(a)  # [10,17,18,25]

'''
[10, 20, 15, 18]
[10, 17, 18, 25]
[10, 20, 30, 40]

'''


# Find  outputs  (Homework)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)  # [50,60,70,80]
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)  # [10,20,30,40]
change(a)
print(a)  # [10,20,30,40]

'''
[50, 60, 70, 80]
[10, 20, 30, 40]
'''


#  Find  outputs  (Homework)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)
f1(x)
print(x)

'''
10
20
10
'''



#  Find  outputs  (Homework)
def  f1(b):
	# b[2] = 25  # Error because tuple is immutable
    pass
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)
f1(a)
print(a)

'''
(10, 20, 15, 18)
(10, 20, 15, 18)

'''
