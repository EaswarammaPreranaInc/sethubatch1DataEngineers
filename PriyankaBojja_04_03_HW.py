1
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)   
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')

OP-
1
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
Outside  loop
----------------------------------------------------------------------------------------------------------------
2
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
#End   of  the  loop
print('Outside  loop')

OP-
1
Sec
Hello
2
Sec
Hello
3
Outside  loop
-----------------------------------------------------------------------------------------------------------
3
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)     
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')

OP-
1
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
Outside loop
---------------------------------------------------------------------------------------------------------------------
4
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)
Note:  Do  not  use  index()  method

a= [10 , 20 , 15 , 12 , 18]
x=int(input('Enter value to be searched: '))
for i in range(len(a)):
	if a[i]==x:
		print('Found at index: ',i)
		
OP-
Enter value to be searched: 10
Found at index:  0

Enter value to be searched: 9
Not found
-------------------------------------------------------------------------------------------------------------------------------------------
5
#  Walrus   operator (:=)  demo  program
print(a := 25)   #25
#print(a = 25)    #error
print(a)         #25
print(a := 6 + 7) #13
print(a)           #13
print((a := 6) + 7)  #13
print(a)             #6
#print((a = 6) + 7)    #error
----------------------------------------------------------------------------------------------------------
6
# Find  outputs  (Home  work)
a = 0
if  a == 0:  
	print('Hyd')   #Hyd
else:
	print('Sec')   
if  b := 0:     
	print('Hyd')     # b=0 is false 
else:
	print('Sec : ' , b)   #Sec : 0
#if  c = 0: 
#	print('Hyd')    #error because assigning 0 to c in if condition is not allowed
#else:
#	print('Sec')
-----------------------------------------------------------------------------------------------------------
7
# Find  outputs
b = 10
a = b += 5   
print(a)     #error- += cannot be used during assignment 
---------------------------------------------------------------------------------------------------
8
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1 (without  walrus  operator)

sum=0
ctr=0
while True:
	a=input('Enter input(-1 to stop): ')
	if a=='True':
		a=1
	elif a=='False':
		a=0
	else:
		a=float(a)
	if a==-1:
		break
	sum+=a
	ctr+=1
print('Average: ',sum/ctr)

OP-
Enter input(-1 to stop): 2
Enter input(-1 to stop): True
Enter input(-1 to stop): 9
Enter input(-1 to stop): False
Enter input(-1 to stop): 0
Enter input(-1 to stop): -1
Average:  2.4
------------------------------------------------------------------------------------------
9
#  del  operator  demo program  (Home  work)
a = 25   
print(a) #25
del   a   #delete reference a pointing to object 25
#print(a)  #error-reference a is deleted
-------------------------------------------------------------------------------------------------
10
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)  #25 25 25
del   a            #delete only reference a 
print(b , c)      # 25 25
#print(a)          #error-ref a deleted
del   b           #delete reference b
print(c)          #25 
#print(b)          #error-ref b deleted 
del   c           #delete reference c
#print(c)          #error-ref c deleted
----------------------------------------------------------------------------------------------------
11
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)   #25 10.8 Hyd
del   a , b , c    # ref are deleted
print(a)           #error- reference deleted nothing is there to print
print(b)           #error
print(c)            #error
--------------------------------------------------------------------------------------------------------
12
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)   #[10 , 20 , 15 , 18]
del  a[2]  #deletes 15 
print(a)   #[10 , 20 , 18]
del  a      #delete entire list 
print(a)    #error - list is deleted , nothing is there to print
print(a[0]) #error
--------------------------------------------------------------------------------------------------------------
13
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)   #(10 , 20 , 15 , 18)
print(a[0]) #10
#del  a[2]   #error- tuple is immutable so deletion is not allowed
del  a
#print(a)    #error- ref a is deleted 
print(a[0])  #error
