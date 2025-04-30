# Find  outputs  (Home  work)
for  i  in  range(1 , 8):#iterates loop from index 1 to 7
	print(i) # return indexes of i 
	if   i % 3 == 0: # if condition is True then executed if block 
		continue # ignore remaining statement after continue and goes to next iteration
	else: # execute if confition is false
		print('Sec') # sec
	print('Hello')#hello
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop') # outside loop


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):#iterates loop from index 1 to 7
	print(i) # return indexes of i 
	if   i % 3 == 0: # if condition is True then executed if block 
		break # stop executing  remaining statement and  next iteration
	else: # execute if confition is false
		print('Sec') # sec
	print('Hello')#hello
else:
	print('else  suite')#else suite executed 
# End  of  the  loop
print('Outside  loop') # outside loop


# Write  a  program  to  search  for  an  element  in  the  list 
list=[45,25,63,1,8,5,10]
x=eval(input("Enter a element to search :")) # reading target or search element 

n=len(list) # length of list 
for i in range(0,n):# iterate loops from 0 to n-1
    if x==list[i]:# check x with list element at index i,if True 
        print("Found",i) # return found index of element
        break # stop executing remaining stament and iterations
    else: # execute if statement ids false 
        i+=1 # moves to next index or next element 
		
print("Not found")# print not found if there is no such element ,by coming outside loop


#Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
# initializing sum,ctr to zero initial
sum=0
ctr=0
x=eval(input("Enter a input (-1 to stop): "))
while x!=-1: # runs until condition is flase
    sum+=x # updates sum by value of x
    ctr+=1 # increment ctr to 1
    x=eval(input("Enter a input (-1 to stop): "))
	
# computing average    
average=sum/ctr
print(f"Average : {average}")



# Find  outputs  (Home  work)
a = 0
if  a == 0:  
	print('Hyd') #hyd
else:
	print('Sec')
if  b := 0: 
	print('Hyd')
else:
	print('Sec : ' , b)  # Sec : 0
'''if  c = 0: # error due to single = operator
	print('Hyd')
else:
	print('Sec')
'''
#homework
b = 10
#a = b += 5   #error
print(a)


a = 25
print(a)  #  25
del a
print(a)  # Error

# Can multiple objects be deleted with the same del operator

a, b, c = 25, 10.8, 'Hyd'
print(a, b, c)  #  25 10.8 Hyd
del a, b, c
print(a)  # Error
print(b)  # Error
print(c)  # Error


# Find outputs
a = b = c = 25
print(a, b, c)  #  25 25 25
del a
print(b, c)  #  25 25
print(a)  #  Error
del b
print(c)  #  25 
print(b)  # Error b is deleted
print(c)  # Error c is deleted
