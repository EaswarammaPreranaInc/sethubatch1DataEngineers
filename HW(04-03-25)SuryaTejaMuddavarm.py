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
'''
my outputs:
-----------
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
else suite
Outside loop
'''


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
print('Outside loop')


'''
1
Sec
Hello
2
Sec
Hello
3
Outside loop
'''

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
print('Outside loop')

'''
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
Outside loop
'''

#  Walrus   operator (:=)  demo  program
print(a := 25)      # 25
print(a = 25)       #True
print(a)            #25
print(a := 6 + 7)   #13
print(a)            #13
print((a := 6) + 7) #13
print(a)            #13
#print((a = 6) + 7)  #error due to :


# Find  outputs  (Home  work)
a = 0
if  a == 0:  
	print('Hyd')  # Hyd
else:
	print('Sec')
if  b := 0: 
	print('Hyd')
else:
	print('Sec : ' , b)  
#if  c = 0:          #error due to :
#	print('Hyd')
#else:
#	print('Sec')
	
# Find  outputs
b = 10
#a = b += 5  # error
#print(a)

#  del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del a 
print(a)# not defined

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a 
print(b , c) # 25 25
print(a)# not defined
del   b
print(c)# 25
print(b)# not defined
del c
print(c)# not defined


#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25, 10.8, 'Hyd'
del   a , b , c
print(a) # not defined
print(b) # not defined
print(c) # not defined


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)    #[10,20,15,18]
del  a[2]
print(a)    #[10,20,15]
del  a
print(a)    #not defined
print(a[0]) # a is not defined

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)        #(10,20,15,18)
print(a[0])     #10
del  a[2]       #
del  a          #
print(a)        #not defined
print(a[0])     #not defined


'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  46 , 34.8 , False , 95 , -1

sum = 0 + 25 + 10.8 + True + 46 + 34.8 + False + 95

ctr = 0  + 1 + 1 + 1 + 1 + 1 + 1 + 1


Enter input  (-1  to  stop)  :  25
Enter input  (-1  to  stop)  :  10.8
Enter input  (-1  to  stop)  :  True
Enter input  (-1  to  stop)  :  46.2
Enter input  (-1  to  stop)  :  False
Enter input  (-1  to  stop)  :  92
Enter input  (-1  to  stop)  :  -1
Average :   29.166666666666668
'''


# my code

x,sum,count = 0,0,0
while x!=-1:
	x = eval(input('Enter input (-1 to stop) : '))
	if x==-1:
		break
	else:
		sum = sum + x
		count= count+1
average = sum/count
print('Average :',average)
'''
my outputs:
--------------
Enter input  (-1  to  stop)  :  25
Enter input  (-1  to  stop)  :  10.8
Enter input  (-1  to  stop)  :  True
Enter input  (-1  to  stop)  :  46.2
Enter input  (-1  to  stop)  :  False
Enter input  (-1  to  stop)  :  92
Enter input  (-1  to  stop)  :  -1
Average :   29.166666666666668
'''


'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Note:  Do  not  use  index()  method

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  --->  Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

3) What  action  to  be  made  if  'x'  is  not  matched  with  the  current  element  of  list ?  --->  Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  if  'x'  is   matched   with  list  element ?  --->  Print  found   message  along  with  index  and
																														  don't   search  in  rest  of  the  list

5) What  action  to  be  made  if  'x'  is   not  matched  with  all  the  elements  of  list ?  --->  Print  not  found   message

6) Hint: Use  for  loop
'''

#my code 

a = [10,20,15,12,18]
x = int(input('Enter a number to search : '))

i=0
while i<=len(a)-1:
	if x==a[i]:
		print('Found at index -',i)
		break
	else:
		i+=1
		continue
else:
	print('Not found')
'''
my outputs:
--------------------
Enter a number to search : 15
Found at index - 2

Enter a number to search : 19
Not found
'''
