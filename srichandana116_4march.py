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
'''1
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
Outside  loop'''
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
'''1
Sec
Hello
2
Sec
Hello
3
Outside  loop'''
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
'''1
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
#  Walrus   operator (:=)  demo  program
print(a := 25) #getting assigned and printed within same line using ':='
print(a := 25)#getting assigned and printed within same line using ':='
print(a)
print(a := 6 + 7)#getting added and assigned and printed within same line using ':='
print(a)
print((a := 6) + 7)#getting assigned 1st and then added and printed within same line using ':='
print(a)
'''25
25
25
13
13
13
6'''
# Find  outputs
b = 10
a = b += 5  
print(a) #error becoz 2 assignment operators cant be in one stmt 
# Find  outputs
b = 10 
print(a:= b + 5 ) #executes adding 10 into b and assigning into a
#  del  operator  demo program  (Home  work)
a = 25
print(a)#25
del   a
print(a) #error name 'a' is not defined
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) #25 25 25
del   a
print(b , c) #25 25
del   b
print(c)  #25
del   c
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)
del   a , b , c #multiple  objects  be  deleted  with  same  del  operator
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10, 20, 15, 18]
del  a[2]
print(a)#[10, 20, 18]
del  a
#print(a)
#print(a[0])
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) #(10, 20, 15, 18)
print(a[0]) #10
#del  a[2] elements of tuple cannot be deleted
del  a #entire tuple deleted
#print(a) once tuple deleted cannot be found, a is lost
#print(a[0]) 
#(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
s=0
for i in range(1,100):
    a=eval(input("enter input (-1 to stop)"))
    if a!=-1:
        s=s+a
    else:
        break
else:
    print(" ")
print(s,i-1)
print("average:",s/(i-1))
#Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
#print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)
a=eval(input("enter any list:"))
x=int(input("enter number you wanna search:"))
for i in range(len(a)):
    if x==a[i]:
        print("found at index", i)
        break
else:
    print("not found")

