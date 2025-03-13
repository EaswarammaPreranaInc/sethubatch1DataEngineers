#program1: isspace()  method  demo  program 
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace())   #  True
print('\n  7\t' . isspace())  #  False
print('\n' . isspace())       # True
print('\n  $\t' . isspace())  # False
print('\t' . isspace())       # True
print('' . isspace())         # False
print(' ' . isspace())        #  True

#program2:Find  outputs  
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))  # a : 25    b : 10.8   c : Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))   # a : 25    b : 10.8   c : Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))     # a :  Hyd    b : 10.8   c : 25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))       # a : Hyd    b : Hyd   c : Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))    # a : 25    b : 10.8   c : Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))     # a : Hyd    b : 10.8   c : 25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))      # a : 25    b : 25   c : 25

#program3:Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

a=input('enter the char : ')
if a.isalnum():
	print("Alpha  Numeric  Character")
	if a.isalpha():
		print("Alphabet  Character")
		if a.isupper():
			print("Upper  case  Alphabet")
		else:
			print("Lower  case  Alphabet")
	elif a.isdigit():
		print("Digit character")
elif a.isspace():
	print("White Space")
else:
	print("Special Character")

'''outputs : enter the char : C
Alpha  Numeric  Character
Alphabet  Character
Upper  case  Alphabet '''

'''program4:Write  a  program  to  reverse  a  string  without  slice
 Let  input  be   Hyd
 What  is  the  output ?  ---> dyH '''

a=input('Enter any string : ')
b=''
for i in range(1,len(a)+1):
	b=b+a[-i]
print(f'Reverse  String : {b}')

'''outputs : Enter any string : teja
Reverse  String : ajet'''

'''program5:Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
Let  input  be  Hyd  is  green  city
What  is  the  output ?  ---> city   green   is   Hyd '''

a=input("Enter  any  sentence : ").split()
b=''
for i in range(1,len(a)+1):
	b=b+' '+a[-i]
print(f'Reverse  order  of  words : {b}')


''' outputs : Enter  any  sentence : My name is suma
Reverse  order  of  words :  suma is name My'''

'''program6:Write  a  program  to  reverse  each  word  of  the  sentence
 Let  input  be  Hyd  is  green  city
  What  is  the  output ?  ---> dyH si neerg ytic
 Hint: Use  for  each  loop  and  also  slice '''

a=input("Enter any sentance : ").split()
b=c=''
for x in a:
	b=b+" "+x[::-1]
print(b)

'''outputs:  Enter any sentance : Hyd is green city
 dyH si neerg ytic '''

'''program7:Write  a  program  to  sort  string  in  alphabetical  order
Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
Hint:  Use   sorted()  function  and   join()  method '''

a=input('Enter any String : ')
b=sorted(a)
print(f'Sorted  string  : {''.join(b)}')

'''OUTPUTS:Enter any String : DEVIKARANI
Sorted  string  : AADEIIKNRV '''

'''program8:Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579
Hint:  sorted()  function , isalpha() , isdigit()  and   join()  method '''

a=input("Enter any string : ")
al=[]
dig=[]
for x in a:
	if x.isalpha():
		al.append(x)
		b=sorted(al)
	elif x.isdigit():
		dig.append(x)
		c=sorted(dig)
print(f'Result : {''.join(b)+''.join(c)}')

'''output : Enter any string : a8k9h3v2c1
Result : achkv12389

#program9 :What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True] #
a = input('Enter  list  :  ')  # [25 , 10.8 , 'Hyd' , True]
print(type(a))       # <class 'str'>
print(a)        # [25 , 10.8 , 'Hyd' , True]
b = eval(a)    
print(b)       #  [25 , 10.8 , 'Hyd' , True]
print(type(b))       # <class 'list'>

#  Find  outputs 
a = [10, 20, 15, 18]     
b = a        # [10, 20, 15, 18]   
print(a  is  b)  # True
print(a  ==  b)  # True
b[2] = 12        
print(a)        # [10, 20, 12, 18] 

#  Find  outputs  
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)    # [10 , 20 , 15 , 18 , 100 , 200 , 150]
print(a + 5)    # error due to 'list' and 'int' never concate
print(a + '5')      # error due to 'list' and 'str' never concate
print([10 , 20] + (30 , 40))   # error due to 'list' and 'tuple' never concate

# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list  #  Unpacks  list  into  2  elements
print('x : ' , x) # x : 25
print('y : ' , y) # y : [10.8 , 'Hyd' , True]
*p , q = list     #  Unpacks  list  into  2  elements
print('p : ' , p)  #  p : [25 , 10.8 , 'Hyd']
print('q : ' , q)    # q : True

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list  # error due to not enough values expected 5 but 4 values only
a , b , *c , d , e = list  
print('a : ' , a)    # a : 25
print('b : ' , b)    # b : 10.8
print('c : ' , c)    # c : []
print('d : ' , d)    # d : 'Hyd'
print('e : ' , e)    # e : True
a , b , *c , d , e , f = list   # error due to not enough values expected 6 but 4 values only

# Find  outputs  
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list  #  Unpacks  list  into  3  elements
print('a : ' , a)      # a : 25
print('b : ' , b)      # b : 10.8
print('_ :  ' , _)     # _ : 'Hyd'
print('d : ' , d)      # d : True

# Find  outputs 
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)  # a : (3+4j)
print('b : ' , b)  # b : 10.8
print('d : ' , d)  # c : True

# Find  outputs 
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)     # a : 25
print('b : ' , b)     # b : 10.8
print('_ : ' , _)     # _ : (3+4j)
print('d : ' , d)     # d : True
print('_: ' , _)      # _ : (3+4j)

# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list  # error due multi star assignment

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)    # a : [25 , 10.8]
print('b :  ' , b)    # b : Hyd
print('c :  ' , c)    # c : True

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)  # a : 25
print('b : ' , b)  # b : Hyd
print('c : ' , c)  # c : Hyd
print('d : ' , d)  # d : True
a , b , c , d = list  # error due to not enough values expected 4 but 3 values only

# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)   # True
print(a  is   b) # False
print(a < c)     # True
print(a > d)     # True
print(a >= c)    # False
print(a <= d)    # False
print(a != c)    # True
print(a != b)    # False
print(a == c)    # False

# Comparing  Lists  
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)   # False
print(a  is   b)  # False

#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))   # 4
b = []
print(len(b))   # 0
c = [[10 , 20] , 30 , 40]
print(len(c))   # 3

# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))       #  36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))       #  (8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))       #  (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))        #  63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))     # error unsupported 'float' and 'str'

#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a))   # error
print(sun(a[0]))  # 63
for x in a:
  print(sum(x))  # 63

sum=0
for x in a:
	for i in x:
		sum=sum+i
print(sum)      # 63

# max()  and  min()  functions  demo  program  
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))   # 30
print(min(a))   # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))   # Vamsi
print(min(b))   # Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c))   # error
d = [25 , '35']
print(max(d))   # error
print(max([]))  # error
print(min([]))  # error

# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)      #[10 , 20 , 15, 18]
print(b)        #[10 , 20 , 15, 18]
print(type(b))  # <class 'list'>
print(a  is  b) # False
print(a == b)   # False

#  Find  outputs 
a = range(4 , 10 , 2)
b = list(a) # [4 , 6 , 8]
print(b)      # [4 , 6 , 8]
print(type(b))   # <class 'list'>
a = list('Vamsi')
print(a)   # ['V' , 'a' , 'm' , 's' , 'i']
a = list()  # []
print(a)    # []
print(list(25))  # error argument should be sequence
print(list(10.8))  # error argument should be sequence
print(list(True))  # error argument should be sequence
print(list(None))  # error argument should be sequence

# Find  outputs 
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))     # [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))     # [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))     # [(10 , 20) , (30 , 40) , {50 , 60}]

# Find  outputs  
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)      #  ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c)      #  ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a)      #  ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))     # True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))     # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))     # False
d = [10 , 0 , 20]
print(all(d))    # False
e = []
print(all(e))    # True

# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))   # True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))   # False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))   # True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))   # False
e = []
print(any(e))   # False
