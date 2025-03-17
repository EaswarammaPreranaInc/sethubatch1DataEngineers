''' EXP-1
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) # False
print('\n  \t' . isspace()) # True
print('\n  7\t' . isspace()) # False
print('\n' . isspace())  # True
print('\n  $\t' . isspace())# False
print('\t' . isspace())# True
print('' . isspace()) # False
print(' ' . isspace())# True
'''
'''EXP-2
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))

#outputs:
a  :  25          b  :  10.8      c  :  Hyd
a  :  25          b  :  10.8      c  :  Hyd
a  :  Hyd         b  :  10.8      c  :  25
a  :  Hyd         b  :  Hyd       c  :  Hyd
a  :  25          b  :  10.8      c  :  Hyd
a  :  Hyd         b  :  10.8      c  :  25
a  :  25          b  :  25        c  :  25
'''
'''EXP-3
#Program to print output
x = input('enter any character: ')
if x.isalnum():
	print('Alphanumeric Character')
	if x.isalpha() :
		print('Alphabet  Character')
		if x.isupper() :
		   print('Uppercase Character')
		else:
	 		print('Lowercase character')
	else:
		print('Digit  Character')
elif x.isspace():
	print("White spaces")
else:
	print('Special character')

#output:
enter any character: A
Alphanumeric Character
Alphabet  Character
Uppercase Character
'''
'''EXP-4
#Program to reverse string without slice
a=input("enter the string:")
b=""
i=1
while i<=len(a):
	b+=a[-i]
	i+=1
print(F' Reverse string: {b}')

output:
enter the string:Rama Rao
Reverse string: oaR amaR
'''
'''EXP-5
#Program to print reverse string as it is
a=input("enter the string:")
b=a.split(" ")
i=1
out=""
while i<=len(b):
	out+=b[-i]+" "
	i+=1
print(F'Reverse string: {out}')

output:
enter the string:students getting bored
Reverse string: bored getting students
'''
'''EXP-6
#program to reverse string in same position
a=input("enter the string:")
b=a.split(" ")
out=''
for x in b:
	c = x[::-1]
	out += (c) +" "
print(F'Reverse string: {out}')

output:
Enter  any  sentence  :  hyd is green city
Reverse string: dyh si neerg ytic
'''
'''EXP-7
a = input('Enter  list  :  ')
print(type(a)) #<class 'str'>
print(a) #[25, 10.8, 'Hyd', True]
b = eval(a) 
print(b)  #[25, 10.8, 'Hyd', True]
print(type(b)) #<class 'list'>
'''
'''EXP-8
#program sorted string
a= input('enter the string: ')
b = sorted(a)
c="".join(b)
print(F'sorted string: {c}')

#output:
enter the string: RAJESH
sorted string: AEHJRS
'''
'''EXP-9
#program to get sorted string
a= input('enter the string: ')
b = [] 
if a.isalpha():
	b += sorted(a)
	x+=1
else:
	b+=sorted(a ,reverse=True)
out="".join(b)
print(F'Sorted string: {out}')

#output:
enter the string: Z9K3PA7D51
Sorted string: ZPKDA97531
'''
'''EXP-10
a = [10, 20, 15, 18]
b = a
print(a  is  b) #True
print(a  ==  b)  #True
b[2] = 12   # [10, 20, 15, 18] ----> [10,20,12,18]
print(a)    # [10,20,12,18]
'''
'''EXP-11
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) #[10 , 20 , 15 , 18 ,100 , 200 , 150]
#print(a + 5)  #Error due to list ,int  operation 
#print(a + '5') #Error due to list ,str  operation 
#print([10 , 20] + (30 , 40)) #Error due to list ,tuple  operation 
'''
'''EXP-12
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x) #25
print('y : ' , y) #[10.8,'hyd',True]
*p , q = list
print('p : ' , p) #[25,10.8,'hyd']
print('q : ' , q) #True
'''
'''EXP-13
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) #25
print('b : ' , b) #10.8
print('_ :  ' , _) #'hyd'
print('d : ' , d) #True 
'''
'''EXP-14
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) #True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) #False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) #True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) #False
e = []
print(any(e)) #False
'''
'''EXP-15
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) #True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) #False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))#False
d = [10 , 0 , 20]
print(all(d))#False
e = []
print(all(e))#True
'''
''''
#EXP-16
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # 25
print('b : ' , b) #10.8
print('c : ' , c) #Hyd
print('d : ' , d) #True
a , b , c , d = list # error due to list contain 3 elemnts to assign 4 variables.
'''
'''
#EXP-17
# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) #True
print(a  is   b)  #False
print(a < c)  #True
print(a > d) #True
print(a >= c) #False
print(a <= d) #False
print(a != c) #True
print(a != b) #False
print(a == c) #False
'''
'''
#EXP-18
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list
a , b , *c , d , e = list
print('a : ' , a) # 25 
print('b : ' , b) #10.8
print('c : ' , c) #[]
print('d : ' , d) #'hyd'
print('e : ' , e) #True
a , b , *c , d , e , f = list
'''
'''
# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) #36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) #8 + 10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) #39.8 + 4j
d = [10 , 20 , 15 , 18]
print(sum(d)) #63
e = [25 , 10.8 , 'Hyd' , True]
#print(sum(e)) 
'''
'''
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(*a))
b=list(*a)
print(sum(b))#How  to  determine  sum  of  inner  list  elements
print()#How  to  determine  sum  of  inner  list  elements  in  another  way
'''
'''
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list 
#The * should be assigned to only one or remove both to remove error.
'''
'''
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #30
print(min(a)) #8
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) #Vamsi
print(min(b)) #Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) #error btw complex and int
d = [25 , '35']
#print(max(d)) #error btw int and str
#print(max([])) #max function has empty input
print(min([])) #min function has empty input
'''
#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a) #
print(b)
print(type(b))
a = list('Vamsi')
print(a)
a = list()
print(a)
#print(list(25))
#print(list(10.8))
#print(list(True))
print(list(None))




















































































































