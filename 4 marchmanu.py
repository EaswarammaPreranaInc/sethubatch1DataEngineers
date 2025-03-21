''''
#
for i in range(1,8):
	print(i)
	if i %3 ==0:
		continue 
	else:
		print('sec')
		print('Hello')
else:
	print('else suite')

	
#
for i in range(1,8):
     print(i)
      if i%3==0:
         break
      else:
         print('sec')
         print('Hello')
   else:
     print('else suite')
	

#
for i in range(1,8):
     print(i)
      if i==8:
         break
      else:
         print('sec')
         print('Hello')
 else:
     print('else suite')

	 
#
a = (10 , 20 , 15 , 18)  # Sequence of List of oject a
print(a) # [10,20,15,18] prints
print(a[0]) # 10 prints
del  a[2] # error due to Tuple does not support delete ()
del  a  # Reference a is deleted
print(a) # error due to to there is no reference to print
print(a[0]) # error due to to there is no reference to print



#
a = [10 , 20 , 15 , 18]  # Sequence of List of oject a
print(a)  # [10,20,15,18] prints
del  a[2] # delete the index 2 in object a
print(a) #[10, 20, 18]
del  a  # Reference a is deleted
print(a) # error due to to there is no reference to print
print(a[0])  # error due to to there is no reference to print



#
a , b , c = 25 , 10.8 , 'Hyd' # multipule objects are assigned
print(a , b , c) # 25 space 10.8 space Hyd
del   a , b , c # References a, b, c are deleted
print(a)  # error due to to there is no reference to print
print(b)  # error due to to there is no reference to print
print(c)  # error due to to there is no reference to print


#a = 25 # 25 is assigned to object a
print(a) # 25 prints
del   a #Reference a is deleted
print(a) # error due to to there is no reference to print


#
a = b = c = 25 # assigned same value to a,b,c 
print(a , b , c) # 25 space 25 space 25
del   a # References a is deleted
print(b , c) # 25 space 25
print(a) # error due to to there is no reference 'a' to print
del   b # References b is deleted
print(c) # 25
print(b) # error due to to there is no reference 'b' to print
del   c # References c is deleted
print(c)# error due to to there is no reference 'c' to print


#Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)


list= [10 , 20 , 15 , 12 , 18]
for i in range(len(list)):
	print(i)
	num=int(input("Enter the number you want to search in list: "))
    def search(list,num):
        if list[i]==num:
            print("Item found")
            break
        else:
            print("Not found")
        return
 search(list,num)



 
 #walrus operator

print(a := 25) # The value of object 'a' is 25 and result print 25
print(a = 25)  # The value of object 'a' is 25 and result print nothing
print(a)  # 25 prints
print(a := 6 + 7) # addition of 6 + 7= 13
print(a) # 13 prints
print((a := 6) + 7) #13  addition of 6 and 7
print(a) # 6 walrus operarion ASSIGNED 6 to object 'a'
print((a = 6) + 7) # error due to single '=' 


#
a = 0
if  a == 0:  # object 'a' is True prints Hyd
	print('Hyd')  
else:  # object 'a' is False prints Sec
print('Sec')
if  b := 0: # object 'b' is True prints Hyd
	print('Hyd')
else: # object 'b' is False prints Sec
	print('Sec : ' , b)  
if  c = 0: #object 'c' is True prints Hyd
	print('Hyd')
else: # object 'c' is Flase prints Sec
	print('Sec')



#
b = 10
a = b += 5 # error due to 'b' is not assigned value 10 bcz here single = is used to assign the value to 'b' 
print(a) # 0


#Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
(without  walrus  operator)

count = 0
 sum = 0.0
 number = 1
 while number !=0:
	 print("Input some integers to calculate their sum and average. Input 0 to exit.")
     number = int(input(" "))
else:
	 print("number")
     sum = sum + number
     count += 1
     if count == 0:
        print("Input some number")
     else:
       print("Average and sum of the above numbers are : ", sum/(count-1),sum)


#
try:
	sum =  ctr = 0
	x = eval(input('Enter input  (-1  to  stop)  :  '))
	while  x != -1:
		sum += x
		ctr +=1
		x = eval(input('Enter input  (-1  to  stop)  :  '))
	 End  of  while  loop:
	print('Average :  ' ,  sum / ctr)
#except  ZeroDivisionError:
	print('Enter  at  least   one  input')
#except  (NameError , TypeError):
	print('Input  can  not  be string')


#

mylist= [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
print("enter 10 elements for the list:")
for i in range(10):
  val = int(input(''))
mylist.append(val)
print("enter an element to be search:")
elem = int(input())
for i in range(10):
	if elem == mylist[i]:
		print("\n element found at index:", i)
		print("element found at position:", i+1)


mylist = list()

print("Enter the size of list: ", end="")
tot = eval(input())

print("Enter", tot, "elements for the list: ", end="")
for i in range(tot):
    mylist.append(input())

print("\nEnter an element to be search: ", end="")
elem = input()

#
for i in range(tot):
    if elem == mylist[i]:
        print("\nElement found at Position:", i+1)

#write a prgm to determine 1.1 +2.2+3.3+.....+n terms

n= int(input('How many terms would you like to add:'))
sum = 0
for i in range(1, n+1):
	sum += 1.1*i
print('sum : ', sum)


#write a prgm to determine sum of first 20 even numbers


sum = 0
for i in range(1, 21):
	sum += 2*i
print('sum of first 20 even numbers : ', sum)
'''
print(argv)
print(type(argv))
for i in range(len(argv)):
	print(F'argv[{i}]:{argv[i]}')
print('argv list without filename :',argv[1:])
print('number of inputs:',len(argv)-1)
