'''
PROGRAM_1:
'''
print('\n  A\t' . isspace())
print('\n  \t' . isspace())
print('\n  7\t' . isspace())
print('\n' . isspace())
print('\n  $\t' . isspace())
print('\t' . isspace())
print(''.isspace())
print(' '.isspace())
'''
OUTPUT:
False
True
False
True
False
True
False
True
'''
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z=a,y=b,x=c))
'''
OUTPUT:
a  :  25          b  :  10.8      c  :  Hyd
a  :  25          b  :  10.8      c  :  Hyd
a  :  Hyd         b  :  10.8      c  :  25
a  :  Hyd         b  :  Hyd       c  :  Hyd
a  :  25          b  :  10.8      c  :  Hyd
a  :  Hyd         b  :  10.8      c  :  25
a  :  25          b  :  25        c  :  25
'''
'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  ---> Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , Alphabet character

4) What  is  the  output  if  input  is  '$' ?  --->  Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->   White  space

7) What  is  the  output  if  input   is   <enter>   key ?  --->  White  space

8) Hint1:  Use  isalnum() , isalpha() , isupper() , islower() , isdigit()   and  isspace()  methods

9) Hint2:  Use  nested  if  and   elif
'''
a=input("Enter the input : ")
if a.isalnum():
	print("Alphanumeric character")
	if a.isalpha():
		print("Alphabet character")
		if a.isupper():
			print("Upper case  alphabet")
		else:
			print("lower case alphabet")
	else:
		print("Alphabet character/ Digit")
elif a.isspace():
	print("White space")
else:
	if a:
		print("Special character ")
	else:
		print("White space")
'''
OUTPUT:
Enter the input : A
Alphanumeric character
Alphabet character
Upper case  alphabet
Enter the input : $
Special character
Enter the input : 5
Alphanumeric character
Alphabet character/ Digit
'''
'''
PROGRAM_2:

Write  a  program  to  reverse  a  string  without  slice

Let  input  be   Hyd
What  is  the  output ?  ---> dyH
'''
a=input("Enter input : ")
sum=""
for i in range(1,len(a)+1):
	sum=sum+a[-i]
print(sum)
'''
OUTPUT:
Enter input : Hyd
dyH
'''
'''
PROGRAM_3:
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'
'''
a=input("enter input : ")
b=a.split()
print(b)
c=""
for i in range(-1,-len(b)-1,-1):
	c=c+b[i]+' '
print(c)
'''
OUTPUT:
enter input : hyd is green city
['hyd', 'is', 'green', 'city']
city green is hyd
'''
'''
PROGRAM_4:

Write  a  program  to  reverse  each  word  of  the  sentence

Let  input  be  Hyd  is  green  city
   What  is  the  output ?  ---> dyH si neerg ytic
'''
a=input("enter input : ")
b=a.split()
c=""
for i in b:
	c=c+i[::-1]+' '
print(c)
'''
OUTPUT:
enter input : hyd is green city
dyh si neerg ytic
'''
'''
PROGRAM_4:
Write  a  program  to  reverse  each  word  of  the  sentence

Let  input  be  Hyd  is  green  city
   What  is  the  output ?  ---> dyH si neerg ytic
'''
a=input("enter input : ")
b=a.split()
c=""
for i in b:
	c=c+i[::-1]+' '
print(c)
'''
OUTPUT:
enter input : hyd is green city
dyh si neerg ytic
'''
'''
PROGRAM_5:
Write  a  program  to  sort  string  in  alphabetical  order
Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
a=input("Enter input : ")
b=sorted(a)
c=''.join(b)
print(c)
'''
OUTPUT:
Enter inputrajesh
aehjrs
'''
'''
PROGRAM_6:
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579
'''
a=input("Enter input : ")
c=""
b=""
for i in a:
	if i.isdigit():
		c=c+i
	else:
		b=b+i
b=sorted(b)
c=sorted(c)
print(''.join(b)+''.join(c))
'''
OUTPUT:
Enter input : Z9K3PA7D51
ADKPZ13579
'''
'''
PROGRAM_7:
'''
a = input('Enter  list  :  ')
print(type(a))
print(a)
b = eval(a)
print(b)
print(type(b))
'''
OUTPUT:
Enter  list  :  [25 , 10.8 , 'Hyd' , True]
<class 'str'>
[25 , 10.8 , 'Hyd' , True]
[25, 10.8, 'Hyd', True]
<class 'list'>
'''
a = [10, 20, 15, 18]
b = a
print(a  is  b)
print(a  ==  b)
b[2]=12
print(a)
'''
OUTPUT:
True
True
[10, 20, 12, 18]
'''
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)
#print(a + 5)-->cannot concatenate list to integer
#print(a + '5')--->cannot concatenate list and string
#print([10,20]+(30,40))--->cannot concatenate different sequence
'''
OUTPUT:
[10, 20, 15, 18, 100, 200, 150]
'''
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list 
print('a : ' , a) 
print('b : ' , b)
print('c : ' , c)
print(type(b))
x,*y = list
print('x : ' , x)
print('y : ' , y)
*p,q = list
print('p : ',p)
print('q : ',q)
'''
OUTPUT:
a :  25
b :  [10.8, 'Hyd']
c :  True
<class 'list'>
x :  25
y :  [10.8, 'Hyd', True]
p :  [25, 10.8, 'Hyd']
q :  True
'''
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list--> not enough values to unpack
a , b , *c , d , e = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
print('e : ' , e)
#a , b , *c , d , e , f = list --->--> not enough values to unpack
'''
OUTPUT:
a :  25
b :  10.8
c :  []
d :  Hyd
e :  True
'''
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)
print('b : ' , b)
print('_ :  ' , _)
print('d : ',d)
'''
OUTPUT:
a :  25
b :  10.8
_ :   Hyd
d :  True
'''
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)
print('b : ' , b)
print('d : ',d)
'''
OUTPUT:
a :  (3+4j)
b :  10.8
d :  True
'''
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)
print('b : ' , b)
print('_ : ',_)
print('d : ' , d)
print('_: ',_)
'''
OUTPUT:
a :  25
b :  10.8
_ :  (3+4j)
d :  True
_:  (3+4j)
'''
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
#a , *b , c , *d , e  = list--->cannot have two star operators to assign
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)
print('b :  ' , b)
print('c :  ',c)
'''
OUTPUT:
a :   [25, 10.8]
b :   Hyd
c :   True
'''
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
#a , b , c , d = list--->more number of list elements for few references 
'''
OUTPUT:
a :  25
b :  10.8
c :  Hyd
d :  True
'''
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)
print(a  is   b)
print(a < c)
print(a > d)
print(a >= c)
print(a <= d)
print(a != c)
print(a != b)
print(a==c)
'''
OUTPUT:
True
False
True
True
False
False
True
False
False
'''
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)
print(a is b)
'''
OUTPUT:
False
False
'''
a = [ 25, 10.8, 'Hyd', True]
print(len(a))
b = []
print(len(b))
c = [[10 , 20] , 30 , 40]
print(len(c))
'''
OUTPUT:
4
0
3
'''
a = [25 , 10.8 , True]
print(sum(a))
b= [3 + 4j , 5 + 6j]
print(sum(b))
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))
d = [10 , 20 , 15 , 18]
print(sum(d))
e = [25 , 10.8 , 'Hyd' , True]
#print(sum(e))--->cannot sum a string to int or float
'''
OUTPUT:
36.8
(8+10j)
(39.8+4j)
63
'''
a = [[10 , 20 , 15 , 18]]
#print(sum(a))
#(How  to  determine  sum  of  inner  list  elements)
#(How  to  determine  sum  of  inner  list  elements  in  another  way)
print(sum(a[0]))
print(sum(a[-1]))
'''
OUTPUT:
63
63
'''
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))
print(min(a))
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))
print(min(b))
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))--->cannot support 
d = [25 , '35']
#print(max(d))--->cannot support this for list having int and string elements
#print(max([]))--->should be atleast one argument
#print(min([]))--->should be atleast one argument
'''
OUTPUT:
30
5
Vamsi
Amar
'''
a=(10,20,15,18)
b=list(a)
print(b)
print(type(b))
print(a is b)
print(a==b)
'''
OUTPUT:
[10, 20, 15, 18]
<class 'list'>
False
False
'''
a = range(4 , 10 , 2)
b = list(a)
print(b)
print(type(b))
a = list('Vamsi')
print(a)
a = list()
print(a)
#print(list(25))--->object int is not modified into list bcoz of int being non-sequence
#print(list(10.8))--->object float is not modified into list bcoz of int being non-sequence
#print(list(True))--->object bool is not modified into list bcoz of int being non-sequence
#print(list(None))--->object none type is not modified into list bcoz of int being non-sequence
'''
OUTPUT:
[4, 6, 8]
<class 'list'>
['V', 'a', 'm', 's', 'i']
[]
'''
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))
'''
OUTPUT:
[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
[[10, 20], (30, 40), {50, 60}]
'''
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)
c = sorted(a , reverse = True)
print(c)
print(a)
'''
OUTPUT:
['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
'''
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))
d = [10 , 0 , 20]
print(all(d))
e = []
print(all(e))
'''
OUTPUT:
True
False
False
False
True
'''
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))
e = []
print(any(e))
'''
OUTPUT:
True
False
True
False
False
'''
