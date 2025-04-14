'''
#write a prgm  loop demo
while True:
	print('Helo')
	print('Bye')

while False:
	print('Helo')
	print('Bye')

#write a prgm  loop demo

x=int(input('Enter the value of x:'))
if x ==0:
	print('Fibonacci Series')
	print(0)
else:
	a=0
	b=1
	print('Fibonacci Series')
	print(a)
	print(b)
	c = a+b
	while c <= x:
		print(c)
		a=b
		b=c
		c=a+b
#write a prgm for loop demo
		
for i in range(1,4):
	for j in range(1,5):
		print(i,j)
		print('Hello')
print('Bye')

#write a prgm to print indexes of list

a=[25,10.8,'Hyd',True]
print(a.index('Hyd'))
print(a.index(10.8))
print(a.index(True))
print(a.index(25))
print(a.index('Sec')) #Error due to there is no 'Sec' in list 'a'

#write a prgm to print First 20 Even numbers

print('First 20 even numbers')
i = 1
while i <= 20:
	print(2*i)
	i+=1
print('Bye')

#write a prgm to print First 20 odd numbers
print('First 20 Odd  numbers')
i = 1
while i <= 20:
	print(2*i-1)
	i+=1
print('Bye')

#write a prgm to print Natural numbers 

n= int(input('Enter value of n:'))
i = 1
print('Natural Number')
while i <= n:
	print(F'{i}')
	i+=1
print('Bye')

#write a prgm to print numbers from 10 to 1 reverse order

print('Number from 10 downto 1 in step of -1')
i = 10
while i > 0:
	print(F'{i}')
	i-=1
print('Bye')


#write a prgm to print upper and lower case alphabets
ch = 'A'
while ch <= 'Z':
	print(ch, end =' ')
	ch = chr(ord(ch)+1)
print()
ch = 'a'
while ch <= 'z':
	print(ch, end =' ')
	ch = chr(ord(ch)+1)
print()


#write a prgm to print first 'n' terms of fibonacci series

n = int(input('Enter number of terms:'))
print('Fibonacci Series')
a = 0
print(a)
if n>1:
	b=1
	print(b)
	c=a+b
	for i in range (n-2):
		print(c)
		a=b
		b=c
		c=a+b
#write a prgm to search for 'x' in fibonacci series

n = int(input('Enter value to be searched:'))
if n==0:
	print('Found')
else:
	a=0
	b=1
	c=a+b
	while c<=n:
		if c==n:
			print('Found')
			exit()
		a=b
		b=c
		c=a+b
		print('Not found')
	

#Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1

a = 'Rama Rao'
print(a [ : 7 : 2])#a[0:7:2] --> string from indexes 0 to 6 in steps of 2 --> Rm a
print(a [ : 7])# a[0:7:1] --> string from indexes 0 to 6 in steps of 1 --> Rama Ra
print(a [2 : 4])# a[2:4:1] --. string from indexes 2 to 3 in steps of 1 --> ma
print(a [2 : ])# a[2:8:1] --> string from indexes 2 to 7 in steps of 1--> ma Rao
print(a [ : 4 ])#a[0:4:1] --> string from indexes 0 to 3 in steps of 1 --> Rama
print(a [ : : 2])# a[0:8:2] --> string from indexes 0 to 7 in stteps of 2 --> Rm Ro
print(a [-6 : -1])# a[-6:-1:1] --. string from indexes -6 to 0 in steps of 1 --> Empty string
print(a [-6 : ])# a[-6:-9:1] --> string from indexes -6 to -10 in steps of 1 --> Empty String
print(a [: -4 : -1])# a[-1:-4:-1] --> string from indexes -1 to -3 in steps of -1  --> 0aR a
print(a [-3 : -1])# a[-3:-1: 1] --> string from indexes -3 to 0 in steps of 1 --> Rao
print(a [-3 : ])# a[-3:8:1] --> string from indexes -3 to 7 in steps of 1 -->Rao
print(a [ : : ])#a[0:8:1] --> string from indexes 0 to 7   in steps of 1   -->Rama Rao
print(a [ : ])#a[0:8:1] --> string from indexes 0 to 7   in steps of  1 -->Rama Rao
print(a [ : : -1])#a[-1:-9:-1] --> string from indexes -1 to  -8   in steps of -1  --> oaR amaR
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])#a[-2:-9:-2] --> string from indexes -2 to -8   in steps of  -2 --> a aa
print(a [2 : 8])#a[2:8:1] --> string from indexes  2 to 7  in steps of 1  --> ma Rao
print(a [2 : 8 : -1])# --> string from indexes  2 to 9  in steps of   --> ma Rao
print(a [ : -6 : -1])#a[-1:-6:-1] --> string from indexes -1 to -5   in steps of -1  --> oaR a
print(a [2 : -3])#a[2:-3:1] --> string from indexes  2 to -4  in steps of 1  --> ma(space)
print(a [1 : 6 : 2])#a[1:6:2] --> string from indexes 1 to 5    in steps of 2  --> aaRo
print(a [ : -5 : -5])#a[-1:-5:-5] --> string from indexes -1 to -5    in steps of -5  -->a
print(a [2 : -5])#a[2:-5:1] --> string from indexes 2 to -6   in steps of 1  --> m
print(a [2 : -5 : 2])# --> string from indexes  2 to -6  in steps of 2  --> Empty string
print(a [ : 0 : -1])#a[-1:0:-1 --> string from indexes -1 to  1   in steps of -1  -->oaR ama
print(a [-5 : 0 : -2])#--> string from indexes -5 to 1   in steps of  -2 --> a


#Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice 


a=input("enter 1st string: ")
b=input("enter 2nd string: ")
if(len(a)>=2 and len(b)>=2):
	c=b[:2]+a[2:]+' '+a[:2]+b[2:]
	print(c)
else:
	print("both strings should have atleast 2 characters")

	
#Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
	

a= input("enter a string: ")
if len(a)>=4:
	b=a[:2]+a[-2:]
	print(b)
else:
	print("")  

#Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
								                  Character  at  index  1  :  A
								                  Character  at  index  2  :  M
							                      Character  at  index  3  :  S
								                  Character  at  index  4  :  I

								                  Character  at  index  -1  :  I
								                  Character  at  index  -2  :  S
								                  Character  at  index  -3  :  M
								                  Character  at  index  -4  :  A
								                  Character  at  index  -5  :  V

Hint:  Use  two  for  loops


a=input('Enter a String: ')
for i in range(len(a)):
	print(f'Character at index {i} : {a[i]}')
for i in range(1,len(a)+1):
	print(f'Character at index {-i} : {a[-i]}')

                               (or)
a=input ('Enter the String:')
print('String in forward:')
for i in range(len(a)):
	print(F' Charecter at index{i}:{a[i]}"
for i in range (1,len(a)+1):
	print(F' Charecter at index{-i}:{a[-1]})

	                   

#Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop


a=input('Enter a String: ')
even=''
odd=''
for i in range(len(a)):
	if i%2 ==0:
		even+=a[i]
	
	else:
		odd+=a[i]
print('Charecters at even indexes:', even)
print('Charecters at odd indexes:'odd)


#Let  input  be    A   4   B   3   C   2   $   5
                          0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  --->  'AAAA'

2) Iteration         i        a[i]       a[i + 1]          out
   -------------------------------------------------------------------------------------------------
                                                                 ''
            1         0        'A'          '4'             '' + 'A' * 4 = 'AAAA'
            2        2        'B'           '3'             'AAAA' + 'B' * 3  = 'AAAABBB'
            3        4        'C'           '2'             'AAAABBB' + 'C' * 2 = 'AAAABBBCC'
            4        6        '$'           '5'             'AAAABBBCC' + '$' * 5 = 'AAAABBBCC$$$$$'
----------------------------------------------------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  ---> a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string


a=input("enter alternate character and number: ")
val=0
num=0
r=''
for i in range(0,len(a),2):
	val=a[i]
	if(i+1<len(a)):
		num=int(a[i+1])
		r+=val*num
	
print(r)
                or

try:
	a= input ('Enter any string with alternate charecter and digit:')
	s =' '
	for i in range(0,len(a),2):
		s+= a[i]*int(a[i+1])
		print('Result:', s)
except:
	print('String should have alternate charecter and digit')


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

#write a prgm to determine sum of first 20 odd number
sum = 0
for i in range(1, 21):
	sum += 2*i - 1
print('sum of first 20 odd numbers : ', sum)

#write a prgm to determine 1+2+3+4+.......+n without using formula n*(n+1)/2

n= int(input('How many terms would you like to add:'))
sum = 0
for i in range(1, n+1):
	sum += i
print('sum : ', sum)


# How to print list elements in reverse order without slice

a= eval(input('Enter list of elements:'))
print('Indexed for loop')
for i in range(1,len(a)+1):
	print(a[-i])


# write a prgm to add two lists and store result in 3rd list


a= eval(input('Enter list1 of elements:'))
b= eval(input('Enter list2 of elements:'))
c=[]
for i in range(len(a)):
	c.append(a[i]+b[i])
	print('3rd list:',c)


# How to print list elements  from indexes 2 to 4 without slice

a=[25,10.8, 'Hyd', True, 3+4j, None, 'Sec']
print('Indexed for loop')
for i in range(2,5):
   print(a[i])


a=[10,20,15,18]
for i in range(len(a)):
	a[i] += 1 #increments each element of list 'a' by 1
	print('a:', a) #[11,21,16,19]
b=[10,20,15,18]
for i in range (len(b)): || for x in b:
	a[i] +=1             ||    x+= 1  # increment 'x' but not the elements of list 'b'
	print('b:', b)       || print('b:', b) #[10,20,15,18]

#
for i in range (1,8):
	print(i)
    if i % 3 ==0:
		 continue
    else:
	   print('sec')
 print('Hello')

#
for i in range (1,8):
	print(i)
	if i %3==0:
		break

	else:
		print('Sec')
print('Hello')


#

for i in range (1,8):
	print(i)
	if i %3==0:
		pass

	else:
		print('Sec')
print('Hello')


#
for i in range (1,8):          
	print(i)
	if i %3==0:
		exit

	else:
		print('Sec')
print('Hello')

outputs

1
Sec
2
Sec
3
4
Sec
5
Sec
6
7
Sec
Hello

#
for i in range (1,8):          
	print(i)
	if i %3==0:
		exit()

	else:
		print('Sec')
print('Hello')

outputs

1
Sec
2
Sec
3

#
for i in range (1,8):          
	print(i)
	if i %3==0:
		continue
	else:
		print('sce')
		print('hello')
else:
	print('else suite')

#
if(): #Empty tuple is False
	print('Hyd')
	continue #Error due to there is no loop
	print('Sec')

#
if(10,20,30): # prints Hyd <next line> Sec due to non Empty tuple is True
	print('Hyd')
	#break # Error due to no loop
	print('Sec')
	
for i in range(1,8):
	print(i)
	if i ==8:
		break
	else:

		print('sec')
        print('Hello')
else:
	print('else suite')
print('outside loop')

#Nested loop demo
for i in range(1,4):
	for j in range (1,5):
		print(i,j)
	print('Hello')
print('Bye')

#index() demo
a=[25,10.8,'Hyd',True]
print(a.index('Hyd'))
print(a.index(25))
#print(a.index('Sec')) # Error due to Sec not in list
print(a.index(True))
print(a.index(10.8))

#write a prgm to print each element and the corresponding index

a=[25, 10.8,'Hyd',True]
print('Index for loop')
for i in range(len(a)):
	print(i,a[i], sep ='...')
print('For each loop')
for x in a:
	print(a.index(x),x, sep=':')

# write a progm to determine command line input is even or odd number

from sys import argv
try:
	x= int(argv[1])
	if x%2==0:
		print('Even number')
	else:
		print('Odd number')
except:
	print('Send an integer number')

# write a progm to determine average command line input 

from sys import argv
try:
	a=[]
	for x in argv[1:]:
		a.append(eval(x))
	 else:
		print('Average :',sum(a)/len(a))
except ZeroDivision Error:
	print('Send at least one input')
except(Type Error, Name Error):
	print('Do not send String')
	

# write a progm to sort command line inputs in ascending order and decending order

from sys import argv
try:
	a = []
	for x in argv[1:]:
		a.append(eval(x))
		a.sort()
		print('Ascending order:',a)
		a.sort(reverse = True)
		print('Decending order:',a)
except TypeError:
	print('Do not send number and string')
except NameError:
	print('String has to be in single or triple quote')
	
# write a progm to print employee data passed from command line

from sys import argv
class emp:
	def init(self):
		self. empno = int(argv[1])
		self. ename = argv[2]
		self. sal = float(argv[3])
		self. gender =argv[4]
		self. married = eval(argv[5])
	def disp(x):
		print('Emp number :', x.empno)
		print('Emp name :', x.ename)
		print('Emp salary :', x.sal)
		print('Emp Gender :', x.gender)
		print('Emp Married :', x.married)
try:
	e =emp()
	e . init()
	e . disp()
except IndexError:
	print('Send inputs in the order empno, emp name, salary, gender and marital status')
except Valueerror:
	print('Emp name should be in double quotes or send inputs in the order empno, empname, salary, gender and marital status')


#write a prgm to determine largest command line input



from sys import argv
try:
   a = []
   for x in argv[1:]:
	   a.append(eval(x))
	   print('Largest input :', max(a))
except ValueError:
	print('Send at least one number')
except NameError:
	print('Input string have to be in single or triple quotes')
except TypeError:
	print('Send number input or string input but not both')

# write a prgm to concatenate two strings seperated by space but swap the first two charecters of each string. Assume that each string contains a minimum of two charecters

a=input('Enter 1st string:')
b=input ('Enter 2nd string:')
if len(a)<2 or len(b)<2:
	print('Input should be a min of two charecter string')
else:
	print('Result:',b[:2]+a[2:] +' '+a[:2]+b[2:])


# write a prgm to print first and last two charecters of the string and print an empty string if string contains less than four charecters
a=input('Enter any string:')
b=' '
if len(a)>=4: #print an empty string if string contains less than four charecters
	b= a[:2]+a[-2:]
	print('Result:', b)

	A4B3C2$6.....> output
try:
	a= input ('Enter any string with alternate charecter and digit:')
	b= input ('Enter any string with alternate charecter and digit:')
	s =' '
	for i in range(0,len(a,b),2):
		s+= (a[i]*int(a[i+1]) + b[i]*int(b[i+1]))
		print('Result:', s)
except:
	print('String should have alternate charecter and digit')

not grtting

a=input ('Enter the String:')
print('String in forward:')
for i in range(len(a)):
	print(F' Charecter at index{i}:{a[i]}"
print('String in reverse :')
for i in range (1,len(a)+1):
	print(F' Charecter at index{-i}:{a[-1]})

	
# write a prgm to modify following prgm with walrus operator

try:
	sum = ctr = 0
	while(x:= eval(input('Enter any number(ctrl+z to stop):'))) != -1:
		sum += x
		ctr += 1
	#end of whileloop:
		print('Average:', sum/ctr)


except( NameError , TypeError):
	print('Input can not be string')
except ZeroDivisionError:
	print('Enter at least one input')


# Sorted function demo 

a=' RAJESH'
b=sorted(a)
print(type(b))
print(b)
c=sorted(a, reverse = True)
print(c)
print(a)


try:
	a= input ('Enter any string with alternate charecter and digit:')
	b= input ('Enter any string with alternate charecter and digit:')
	c =' '
	while range(0,len(a),2):
	     while range(0,len(b),2):
		c+= (a[i]*int(a[i+1])+b[i]*int(b[i+1])
print('Result:', c)
except:
	print('String should have alternate charecter and digit')


def remove_duplicates(input_string):
	result = ""
for char in input_string:
     if char not in result:
         result += char
         print(' result:')
		 

input_string = "aabbccddeeff"
output_string = notrepeat.(input_string)
print("Original String:", input_string)
print("String without duplicates:", output_string)

'''


