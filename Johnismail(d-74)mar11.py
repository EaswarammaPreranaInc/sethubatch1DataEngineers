'''


prog--1 Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  ---> Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  --->  Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->   White  space

7) What  is  the  output  if  input   is   <enter>   key ?  --->  White  space

8) Hint1:  Use  isalnum() , isalpha() , isupper() , islower() , isdigit()   and  isspace()  methods

9) Hint2:  Use  nested  if  and   elif


i=input('enter any charachter:')
if (i.isalnum() and i.isalpha() and i.isupper()):
	 print('Alpha numeric character \n Alphabet character \n uppercase character')
elif (i.isalnum() and i.isalpha and i.islower()):
	 print('Alphanumeric  character \n Alphabet character \n lower case  alphabet')
elif (i.isalnum() and i.isdigit()):
	 print('Alphanumeric  character \n digit  character')
elif (i.isspace()):
	 print('white space')
else:
	 print('special character')

outputs---
enter any charachter:A
Alpha numeric character
 Alphabet character
 uppercase character

 enter any charachter:a
Alphanumeric  character
 Alphabet character
 lower case  alphabet

 enter any charachter:%
special character

enter any charachter:
white space


prog-2-Write  a  program  to  reverse  a  string  without  slice
a=input('enter any string:')#hyd
b=''#empty
for i in range(1,len(a)+1):#
	 b+=a[-i]
print(b)
	 
outputss------
enter any string:hyd
dyh

enter any string:Rama Rao
oaR amaR'''

prog-3
'''Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
    1         'city'       '' + 'city' + ' ' =  'city '
    2         'green'    'city ' + 'green' + ' ' =  'city green '
    3         'is'           'city green ' + 'is' + ' ' = 'city green is '
    4         'Hyd'       'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '

	 
a=input('enter string:')
b=a.split()
c=''
for i in range(1,len(b)+1):
	 c+=b[-i]+" "
print('reverse:',c)
	 
 outputs-----  
enter string:hyd is green city
reverse: city green is hyd

prog-4 Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice

a=input('enter any string:')#hyd is green city
b=a.split()
c=''
for i in range(len(b)):
	 c+=b[i][::-1]+" "
print(c)

outputs---
enter any string:hyd is green city
dyh si neerg ytic
	 	 

prog-5 Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS

Hint:  Use   sorted()  function  and   join()  method


a=input('enter any string:')
b=''
b=sorted(a)
print(''.join(b))

enter any string:RAJESH
AEHJRS

prog-6-Write  a  program  to  sort  string  such  that  alphabets
in  alphabetical  order  and  digits  in  ascending  order

a=input('enter any string:')
b=''
c=''
if a.isalnum():
	 b=sorted(a)
	
	 print(''.join(b))
	 
elif a.isdigit():

	 print('ans:',c)
print(''.join(c))

outputs---
enter any string:Z9K3PA7D51
13579ADKPZ

# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a))#<class 'str'>
print(a)#[25,10.8,'hyd',True]
b = eval(a)
print(b)#[25,10.8,'hyd',true]
print(type(b))#<class list>

#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)#True
print(a  ==  b)#True
b[2] = 12 
print(a) #[10,20,12,18]


#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)#[10,120,15,18,100,200,150]
print(a + 5)#error
print(a + '5')#error
print([10 , 20] + (30 , 40))#error


# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x)#x:[25]
print('y : ' , y)#y:[10.8,'hyd',True]
*p , q = list
print('p : ' , p)#p:[25,10.8,'hyd']
print('q : ' , q)#q:[True]

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list# error
a , b , *c , d , e = list
print('a : ' , a)#a:[25]
print('b : ' , b)#b:[10.8]
print('c : ' , c)# []
print('d : ' , d)#d:['hyd']
print('e : ' , e)#e:[TRue]
a , b , *c , d , e , f = list #error

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)#a:[25]
print('b : ' , b)#b:[10.8]
print('_ :  ' , _)#c:['hyd']
print('d : ' , d)#d:[True]

# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)#a:3+4j
print('b : ' , b)#b:10.8
print('d : ' , d)#True

# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)#a:[25]
print('b : ' , b)#b:[10.8]
print('_ : ' , _)#_:[3+4j]
print('d : ' , d)#d:[True]
print('_: ' , _)#_:[3+4j]

# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list #SyntaxError: multiple starred expressions in assignment

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)#a:[25,10.8]
print('b :  ' , b)#b:['Hyd']
print('c :  ' , c)#c:[True]

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)#a:[25]
print('b : ' , b)#b:[10.8]
print('c : ' , c)#c:['Hyd']
print('d : ' , d)#d:[True]
a , b , c , d = list #ValueError: not enough values to unpack (expected 4, got 3)

# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)#True
print(a  is   b)#False
print(a < c)#True
print(a > d)#True
print(a >= c)#False
print(a <= d)#False
print(a != c)#True
print(a != b)#False
print(a == c)#false

# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)#False
print(a  is   b)#False

#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))#4
b = []
print(len(b))#0
c = [[10 , 20] , 30 , 40]
print(len(c))#3

# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))#25+10.8+1=36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))#8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))#39.8+4j
d = [10 , 20 , 15 , 18]
print(sum(d))#63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))#error



What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list


# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))#30
print(min(a))#5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))#vamsi
print(min(b))#amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))# error
d = [25 , '35']
#print(max(d)) error
#print(max([])) error
#print(min([])) error

# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)#[10,20,15,18]
print(type(b))#<class 'list'>
print(a  is  b)#False
print(a == b)#False


#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)#[4,6,8]
print(type(b))
a = list('Vamsi')
print(a)#['vamsi']
a = list()
print(a)#[]
#print(list(25))#error
#print(list(10.8))#error
#print(list(True))#error
#print(list(None))#error

# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))#[(10,20),(30,40,50),(60,70,80,90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))#[(10,20),(30,40,50),{60,70,80,90}]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))#[[10 , 20] , (30 , 40) , {50 , 60}]

# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)#['Amar','kiran,'Rajesh','Rama','Rama Rao','sita','vamsi']
c = sorted(a , reverse = True)
print(c)#['vamsi','sita','Rama Rao','Rama','Rajesh','kiran,'Amar',]
print(a)#['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']


# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))#True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))#False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))#False
d = [10 , 0 , 20]
print(all(d))#false
e = []
print(all(e))#True'''



'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False

3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  above  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):
'''
'''
# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))#True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))#False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))#TRue
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))#False
e = []
print(any(e))#False'''



'''
any()   function
-------------------
1) What  does  any(list)  do ?  --->  Returns  True  when  at  least  one  element  of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  ---> When  every  element  of  the  list  is  false

3) if  cond1  or  cond2  or  cond3  or  cond4:
     How  to  reduce  the  above  four  conditions  to  a  single  condition ?  --->   if  any([cond1 , cond2 , cond3 , cond4]):

4) all()  and  any()  functions  are  used  as  an  alternative  when  there  are  too  many  conditions  in  if  and  while
'''
