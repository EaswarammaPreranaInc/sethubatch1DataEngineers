# Find  outputs  (Home  work)
'''for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')'''
'''o/p: 1
        Sec
        Hello
        2
        Sec
        Hello
        3
        4
        Sec
        Hello
        5
        Sec
        Hello
        6
        7
        Sec
        Hello
        else  suite
        Outside  loop '''

# Find  outputs  (Home  work)
'''for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
#End   of  the  loop
print('Outside  loop')'''

'''o/p: 1
        Sec
        Hello
        2
        Sec
        Hello
        3
        Outside  loop '''

# Find  outputs  (Home  work)
'''for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')'''

'''o/p: 1
        Sec
        Hello
        2
        Sec
        Hello
        3
        Sec
        Hello
        4
        Sec
        Hello
        5
        Sec
        Hello
        6
        Sec
        Hello
        7
        Sec
        Hello
        else  suite
        Outside loop'''
#write a prgm to search an element in list without using in operator and print found or not found message
lst = [10,20,15,12,18]
x = int(input('Enter search no:'))
found = False
for i in range(len(lst)):
	if lst[i] == x:
		print(f'Found at index {i}')
		found = True
		break
if not found:
	print('Not Found')	
'''o/p: Enter search no:15
        Found at index 2	'''
#Avg of input terminated by -1
total = 0  # To store the sum of valid inputs
count = 0  # To count the number of valid inputs

while True:
    try:
        value = input("Enter input (-1 to stop) : ")
        value = eval(value)  # Evaluating the input to handle different types like int, float, and bool
        
        if value == -1:
            break  # Stop input collection if -1 is entered
        
        total += value  # Add value to the sum
        count += 1  # Increment count
    except:
        print("Invalid input, please enter a valid number or boolean.")

# Calculate and print average
if count > 0:
    average = total / count
    print("Average :", average)
else:
    print("No valid inputs were entered.")
'''o/p: Enter input (-1 to stop) : 25
        Enter input (-1 to stop) : 10.8
        Enter input (-1 to stop) : 46.2
        Enter input (-1 to stop) : True
        Enter input (-1 to stop) : 92  
        Enter input (-1 to stop) : False
        Enter input (-1 to stop) : -1
        Average : 29.166666666666668    '''

#  del  operator  demo program  (Home  work)
a = 25
print(a)#25
del   a 
print(a) #Error
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)#25 25 25
del   a
print(b , c)#25 25
print(a)#Error
del   b
print(c)#25
print(b)#Error
del   c
print(c)#Error
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)# 25 10.8 Hyd
del   a , b , c
print(a)#Error
print(b)#Error
print(c)#Error
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
a = [10 , 20 , 15 , 18]
print(a)#[10,20,15,18]
del  a[2]#[10,20,18]
print(a)#[10,20,18]
del  a
print(a)#Error
print(a[0])#Error
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)#(10,20,15,18)
print(a[0])#10
del  a[2] # cannot delete tuple because modification is not possible
del  a 
print(a)
print(a[0])
			
