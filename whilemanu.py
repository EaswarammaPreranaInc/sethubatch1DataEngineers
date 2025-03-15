'''
a = [10 , 20 , 15 , 18 , 12 , 15 , 19 , 25 , 15 , 14 , 12]
while 15 in a :
	a.remove(15)
	print(a)

a = [10 , 20 , 15 , 18 , 12 , 15 , 19 , 25 , 15 , 14 , 12]
a.remove(15)
a.remove(15)
a.remove(15)
print(a)

mylist= [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
print("enter 10 elements for the list:")
for i in range(10):
   # val = int(input(''))
   #mylist.append(val)
   print("enter an element to be search:")
   #elem = int(input())
for i in range(10):
	if elem == mylist[i]:
		print("\n element found at index:", i)
		print("element found at position:", i+1)   not ok


try:
	sum =  ctr = 0
	x = eval(input('Enter input  (-1  to  stop)  :  '))
	while  x != -1:
		sum += x
		ctr +=1
		x = eval(input('Enter input  (-1  to  stop)  :  '))
	while x==-1:
	 print('Average :  ' ,  sum / ctr)
	 while loop:
		 print('Average')
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not  be string')

	
from sys import argv
print(argv)
print(type(argv))
for i in range(len(argv)):
	print(F'argv[{i}]:{argv[i]}')
print('argv list without filename :',argv[1:])
print('number of inputs:',len(argv)-1)




list=['py   prog2.py' , ' 10 ' , '  20 ',   ' 30.8' ,   ' 7 ',  ' 40 ',   '35.6' ]
for i in list range(len(argv)):
	print(argv)
	if max(argv[1:]):
		print(argv)   wrong

		

#Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

list1 = ['py','th','on']
list2 = ['ja','va'] 
print((list1[0]+list2[1])+" "+(list2[0]+list1[1]+list1[2]))

                (or)

list1 = ['py','th','on']
list2 = ['ja','va'] 
print(list1[0:1:1]+list2[1:2:1])
print(list2[0:1:1]+list1[1:3:1]) 
print((list1[0:1:1]+list2[1:2:1])+(list2[0:1:1]+list1[1:3:1]), sep="----> ") There in 6th march




Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

list = ['py','th','on']
print(list[0]+list[2])
list = ['hy','d']
print(list[0:2])



from sys import argv
try:
	a= ['v','A' ,'M', 'S', 'H', 'I']
	for x in argv[1:]:
		a.sort()
		print ('Forward order:',a)
		a.sort(reverse =True)
		print('reverse order:', a)
except:
	print('Do not send number and string')



  a= "VAMSHI"
  i = len(s) - 1
  print(s[i], "reverse order")
    
	
a= "VAMSHI"[::-1]
for i in range(len(a)):
	print(a[i],"charcter at index :")
	

a= "VAMSHI"[::1]
for i in range(len(a)):
	print(a[i],"charcter at index :")
	

given_str= 'VAMSHI'
even_characters = []  # For storing even characters
odd_characters = []  # For storing odd characters
 
for i in range(len(given_str)):
    if i % 2 == 0:  # check if the index is even
      even_characters.append(given_str[i])
	  print('Even characters: {}'.format(even_characters))
    else:
      odd_characters.append(given_str[i])  
      print('Odd characters: {}'.format(odd_characters))




try:
	a= input ('Enter any string with alternate charecter and digit:')
	s =' '
	for i in range(0,len(a),2):
		s+= (a[i]*int(a[i+1]))
		print('Result:', s)
except:
	print('String should have alternate charecter and digit')

#Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
    What  is  the  output ? --->  RAM<space>O

2) out = '' + 'R' + 'A' + 'M' + ' ' + 'O' = 'RAM O'


a= "RAMA RAO"
b= " "
for char in a:
	if char not in b:
		b= b+char
print(b)

#
import random

'''

a="VAMSI"
b="HYD"
c =((a[0]+b[0])+(a[1]+b[1])+(a[2]+b[2])) 
print(c+a[3]+a[4])


