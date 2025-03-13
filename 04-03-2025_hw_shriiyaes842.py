'''
1. Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Note:  Do  not  use  index()  method

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  --->  Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

3) What  action  to  be  made  if  'x'  is  not  matched  with  the  current  element  of  list ?  --->  Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  if  'x'  is   matched   with  list  element ?  --->  Print  found   message  along  with  index  and
																														  don't   search  in  rest  of  the  list

5) What  action  to  be  made  if  'x'  is   not  matched  with  all  the  elements  of  list ?  --->  Print  not  found   message

6) Hint: Use  for  loop
'''
a = [10 , 20 , 15 , 12 , 18]
x=eval(input("Enter value to be searched:"))
for i in range(len(a)):
	if x==a[i]:
		print("Found at index",i)
		break
else:
	print("Not found")
''' 
OUTPUT:
Enter value to be searched:12
Found at index 3
Enter value to be searched:33
Not found
'''


"""
2. (Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  46 , 34.8 , False , 95 , -1

sum = 0 + 25 + 10.8 + True + 46 + 34.8 + False + 95

ctr = 0  + 1 + 1 + 1 + 1 + 1 + 1 + 1
 """
s=0
ctr=0
while True:
	a=eval(input("Enter input  (-1  to  stop)  :"))
	if a==-1:
		break
	
	s=s+a       
	ctr=ctr+1
average=s/ctr
print("Average",average)

'''
OUTPUT:
Enter input  (-1  to  stop)  :  25
Enter input  (-1  to  stop)  :  10.8
Enter input  (-1  to  stop)  :  True
Enter input  (-1  to  stop)  :  46.2
Enter input  (-1  to  stop)  :  False
Enter input  (-1  to  stop)  :  92
Enter input  (-1  to  stop)  :  -1
Average :   29.166666666666668 '''



# 3. Find  outputs  (Home  work)
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
OUTPUT:
1
Sec '''


# 4. Find  outputs  (Home  work)
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


# 5. Find  outputs  (Home  work)
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


#6.  Walrus   operator (:=)  demo  program
print(a := 25)       # 25
#print(a = 25)       # Error
print(a)             # 25
print(a := 6 + 7)    # 13
print(a)             # 13
print((a := 6) + 7)  # 13
print(a)             # 6
#print((a = 6) + 7)  # Error