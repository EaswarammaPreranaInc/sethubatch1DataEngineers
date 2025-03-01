# Modify  following  program  with  else  and  if
try:
	a = int(input('Enter month number (1 - 12): '))
	if 1<= a <=12:
		print("Month", end=" : ")
		if a == 1:
			print('January')
		if  a == 2:
			print('February')
		if  a == 3:
			print('March')
		if  a == 4:
			print('April')
		if  a == 5:
			print('May')
		if  a == 6:
			print('June')
		if  a == 7:
			print('july')
		if  a == 8:
			print('August')
		if  a == 9:
			print('September')
		if  a == 10:
			print('October')
		if  a == 11:
			print('November')
		if  a == 12:
			print('December')
	else:
		print("Please enter between 1-12")
except:
		print('Input  should  be  an  integer')
# Output:
# Enter month number (1 - 12): 2
# Month : February

# Find  outputs  (Home  work)
# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  using  for  loop
# print()
# How  to  print  each  character  of   string  'Hyd'  using  for  loop
# print()
# How  to  print  each  element  of   range(5) using  for  loop

a = [10,20,15,18]
for x in a:
 print(x)
# Output :10
# 20
# 15
# 18

a = "Hyd"
for x in a:
 print(x)
# Output: H
# y
# d

a= range(5)
for x in a:
 print(x)
#output:0
# 1
# 2
# 3
# 4

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) #prints keys 10,30,50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) #prints values 20,40,60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)# prints items(10,20),(30,40),(50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # prints keys as default (10,30,50)

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')#10...20<nextline>30...40<nextline>50...60
for  x ,  y  in   a: # error because here i gave two variables x,y but by default this prints only keys
	print(x , y)
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')#error because here i gave two variables x,y but by default this prints only keys

# Identify  error  (Home  work)
for  x  in   123:
        print(x) # int is not iterable

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # empty prints nothing
for  x   in  []:
        print(x)# empty prints nothing
for  x   in   {}:
        print(x)# empty prints nothing
for  x   in   set():
        print(x)# empty prints nothing
for  x   in   '':
        print(x)# empty prints nothing
for  x  in  range(10 , 10):
	print(x) # range 10 to 9 in steps of 1 prints nothing
# for  x  in   range():
	print(x) #error range must contain some integer
# for  x  in   (25):
	print(x) # int is not iterable

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
 for  j  in  range(1 , 5):
   print(i,j)
 print('Hello')
print('Bye')
#output : 1st iteration :1 1
# # 1 2
# 1 3
# 1 4
# Hello
#2nd iteration
# 2 1
# 2 2
# 2 3
# 2 4
# Hello
# 3rd iteration
# 3 1
# 3 2
# 3 3
# 3 4
# Hello
# Bye


'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)				Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(>= 700)				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
from idlelib.help import copy_strip

units = int(input('Enter  units : '))  #  175
match  units // 100:
 case 0:
  cost = units * 3.00
 case 1 :
  cost = 100 * 3.00+ (units-100) *3.50
 case 2 :
  cost = 100 * 3.00 + 100 * 3.50+ (units-200)*4.00
 case 3 :
  cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00  + (units-400)*4.50
 case _ :
  cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50  + (units-700)*5.00
print("Amount : ", cost)

#output:
#Enter  units : 32423
# Amount :  161415.0
