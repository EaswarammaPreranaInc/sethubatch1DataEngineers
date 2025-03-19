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

# output:
# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
# 4
# Sec
# Hello
# 5
# Sec
# Hello
# 6
# 7
# Sec
# Hello
# else  suite
# Outside  loop



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

"""
output:
1
Sec
Hello
2
Sec
Hello
3
Outside  loop"""

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
else  suite
Outside loop '''


#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25)  #error
print(a) #25
print(a := 6 + 7) #13
print(a) #13
print((a := 6) + 7) #13
print(a) #6
print((a = 6) + 7) # error

# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec') # Hyd
if  b := 0: # not error because we can use walrus in if condition
	print('Hyd')
else:
	print('Sec : ' , b) # Sec : 0
if  c = 0: # error because we are assigning not comparing
	print('Hyd')
else:
	print('Sec')

# Find  outputs
b = 10
a = b += 5
print(a)
#error

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

6) Hint: Use  for  loop
'''

a= [10 , 20 , 15 , 12 , 18]
n = int(input("Enter Value : "))
b = 0
for x in a:
    if n == x:
     print(F"Found at index : {b}")
     break
    b+=1
else:
    print("Not Found")

'''
output: Enter Value : 15 
Found at index : 2'''

'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  46 , 34.8 , False , 95 , -1

sum = 0 + 25 + 10.8 + True + 46 + 34.8 + False + 95

ctr = 0  + 1 + 1 + 1 + 1 + 1 + 1 + 1
'''
Sum = 0
Ctr = 0
try:
    while True:
        a = eval(input("Enter value (-1 to exit) : "))
        if a==-1:
            break
        Sum+=a
        Ctr +=1
    avg = Sum/Ctr
    print(f"Average : {avg}")
except:
    print("Enter valid data")

'''
Enter value (-1 to exit) : 25
Enter value (-1 to exit) : 10.8
Enter value (-1 to exit) : True
Enter value (-1 to exit) : 46
Enter value (-1 to exit) : 34.8
Enter value (-1 to exit) : False
Enter value (-1 to exit) : 95
Enter value (-1 to exit) : -1
Average : 30.37142857142857
'''


