
# 1. How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop') 


a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
	print(i,a[i])
print('Indexed for loop')


print('For each loop')
for x in a:
	print(a.index(x),x)

# 2. How  to  print  list  elements  in  reverse  order   without  slice
a = eval(input('Enter  list  of  elements : ')) 
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable) 
a = eval(input('Enter  list  of  elements : '))  
print('Indexed for loop')
for i in range(len(a)-1,-1,-1): 
	print(a[i]) 

# not possible for for each loop bcz we cant iterate from right to left
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method '''
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = [] 
#3.
for i in range(len(a)):
		c.append(a[i]+b[i])
print(c)

# not possible for each loop bcz can only iterate one sequence at a time

'''How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop '''


#  4.How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop

print('Indexed for loop')
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range(2,len(a)-2,1):
	print(a[i])
print('for each loop')

# not possible for each loop bcz we cant iterate a part of sequence


# 5. Gift
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1 # modifies the elements of the list
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1 # x value is changed 
print('b :  ' ,  b) # b value is not affected 

'''
(Home  work)
6. Write  a  program  to  print  first  20  even  numbers  with  while  loop

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Use  while  loop '''

i=1
while(i>=1 and i<=20):
	print(2*i)
	i+=1


'''Write  a  program  to  print  first  20  odd  numbers  with  while  loop

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) In  general, print  what ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
'''

i=1
while(i>=1 and i<=20):
	print(2*i-1)
	i+=1

'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

In  general,  print  what ?  --->  Print  'i'  where  'i'  varies  from  1  to  n

Hint:  Use  for  loop '''

n=int(input("Enter a number: "))

for x in range(1,n+1):
	print(x*1)


'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

In  general, print  what ?  --->  Print  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

Hint:  Use  for  loop
'''

for i in reversed(range(1,11)):
	print(i)
 #OR
 for i in range(10, 0, -1):  # Start at 10, stop before 0, step -1
    print(i)
'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
1) chr(65) =  'A'
    chr(90) = 'Z'
    chr(97) =  'a'
    chr(122) = 'z'

2) What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character

3) ord('A') =  65
    ord('Z') = 90
    ord('a') =  97
    ord('z') =  122

4) What  does  ord()  function  do ?  --->  Converts  character  to  unicode  value 

5) Hint:  Use  two  for  loops
'''

for x in range(65,91):
	print(chr(x),end='  ')
print('\n')
for y in range(97,123):
	print(chr(y),end='  ')

'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5

Hint:  Use  for  loop
'''

n=int(input("Enter a number: "))

a=0
b=1
c=a+b
count=0
if (n==1):
	print(0)
else: 
	print(0)
	print(1)
	while(count<n-2): 
		
		a=b
		b=c
		c=a+b
		count+=1
		print(c)


n=int(input("Enter a number: "))
a=0
b=1
c=a+b
if n==1:
	print(0)
else:
	print(0)
	print(1)
	for i in(2,n):
		c=a+b
		a=b
		b=c

		print(c)

'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? ---> Found

3) Do  not  generate  fibonacci  series
'''



x = int(input("Enter a number: "))  # Take input
a, b = 0, 1  

if x == 0 or x == 1:  # Handle special cases directly
    print("Found")
else:
    for _ in range(x):  # Loop indefinitely (we break when needed)
        c = a + b
        a, b = b, c
        if x == c:
            print("Found")
            break
    else:  # This else runs if the loop completes without finding x
        print("Not found") 
'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0 + 1.1 * 1 + 1.1 * 2 + 1.1* 3 +  ......

2) What  is  added  to  sum  in  general ?  ---> 1.1 * i   where  'i'  varies  from  1  to  n
'''

n= int(input(" enter a number :  "))
sum=0
for i in range(1,n+1):
	sum=sum+(1.1*i)

print(sum)

'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? ---> 2 * i   where 'i'  varies  from   1  to  20
'''
sum=0
for i in range(21):
	 sum+=2*i
print(sum)

'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
'''
i=int(input("Enter a number:  "))
sum=0
for x in range(1,i+1):
	sum+=x
print(sum)



# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i) #1,2,3,4,5,6,7,8
	if  i % 3  == 0:
		continue
	else:
			print('Sec') # Sec,Sec,Sec,sec,sec
	print('Hello')#Hello, Hello,Hello,Hello,Hello
# End of loop
print('Outside loop')#outside loop

# Identify Error  (Home  work)
if (): # never excecuted
	print('Hyd')
	continue
	print('Sec')


# Find outputs (Home  work)
for  i   in   range(1 , 8): 
	print(i)# 1,2,3
	if   i % 3 == 0:
		break
	else:
		print('Sec')#SEc SEc
	print('Hello')#hello,hello
# End  of  the  loop
print('Outside loop')# outside loop

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd') # 'Hyd'
	#break can only be used for and while loops
	print('Sec')

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i) #  1,2,3,4,5,6,7
	if   i % 3 == 0:
		pass
		print('Hyd')#Hyd,Hyd
	else:
		print('Sec')#Sec,Sec,Sec,Sec,Sec
	print('Hello')#Hello,Hello,Hello,Hello,Hello,Hello,Hello
# End  of  the  loop
print('Outside loop')#Outside loop 

# Find  outputs  (Home  work)
for  i   in   range(1 , 8): #
	print(i)#1,2,3
	if   i % 3 == 0:#
		exit()
	else:
		print('Sec') #Sec,Sec
	print('Hello')#Hello,Hello
# End  of  the  loop
print('Outside loop')

