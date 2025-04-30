#1
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())#False
print('\n  \t' . isspace())#True
print('\n  7\t' . isspace())#False
print('\n' . isspace())#True
print('\n  $\t' . isspace())#False
print('\t' . isspace())#true
print('' . isspace())#false
print(' ' . isspace())#true
#2
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))#a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))#a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))#a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))#a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))#a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a  :  25  	  b  :  25  	  c  :  25

#3
'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  ---> Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  --->  Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->   White  space

7) What  is  the  output  if  input   is   <enter>   key ?  --->  White  space

8) Hint1:  Use  isalnum() , isalpha() , isupper() , islower() , isdigit()   and  isspace()  methods

9) Hint2:  Use  nested  if  and   elif
'''
a=input("enter the no:")
if len(a)==1:
    if a.isalnum():
        print("Alphanumeric  character")
        if a.isalpha():
            print("Alphabet character")
            if a.isupper():
                print("Upper case  alphabet")
            elif a.islower():
                print("lower case  alphabet")
        elif a.isdigit():
            print("Digit character")
    elif a.isspace():
        print("White  space")
    else:
        print("special character")
else:
    print("enter only one input")

#4
'''
Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  ---> dyH

2)   H       y      d
      -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1         'd'            '' + 'd' = 'd'
     2         'y'            'd' + 'y' = 'dy'
     3         'H'            'dy' + 'H' = 'dyH'
  ---------------------------------------------
'''

k=input("enter the string:")
sum=''
for i in range(1,len(k)+1):
    sum+=k[-i]
print(sum)

#5
'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

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
   --------------------------------------------------------
'''
k= input("input:")
b=k.split()
sum=''
for i in range(1,len(b)+1):
    sum+=b[-i]+' '
print(sum)

#6
'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
k= input("input:")
b=k.split()
sum=''
for i in b:
    sum=sum+i[::-1]+" "
print(sum)

#7
'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS

Hint:  Use   sorted()  function  and   join()  method
'''

k=input("enter the string:")
b="".join(sorted(k))

#8
'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579

1) Hint:  sorted()  function , isalpha() , isdigit()  and   join()  method
'''
k=input("enter the string:")
sum=''
m=''
for i in range(len(k)):
    if k[i].isalpha():
        sum=sum+k[i]
    elif k[i].isdigit():
        m=m+k[i]
    else:
        print("enter only alpha and numeric:")
o=sorted(sum)+sorted(m)
r="".join(o)
print(r)

#9
a = input('Enter  list  :  ')#1
print(type(a))#<class'string'>
print(a)#1
b = eval(a)
print(b)#1
print(type(b))#<class'int'>

#10
#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)#true
print(a  ==  b)#true
b[2] = 12
print(a)#[10, 20, 12, 18]

#11
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)#[10,20,15,18,100,200,150
#print(a + 5)#error
#print(a + '5')#error
#print([10 , 20] + (30 , 40))#error only list to list not tuple to list

#12
# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x)#25
print('y : ' , y)#[10.8,hyd,True]
*p , q = list
print('p : ' , p)#[25, 10.8, 'Hyd']
print('q : ' , q)#True

#13
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list#list error not enough tp unpack
#a , b , *c , d , e = list error not enough tp unpack
print('a : ' , a)#25
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
print('e : ' , e)
a , b , *c , d , e , f = list

#14
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)#25
print('b : ' , b)#10.8
print('_ :  ' , _)#Hyd
print('d : ' , d)#True

#15
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)#3+4j
print('b : ' , b)#10.8
print('d : ' , d)#True

#16
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)#25
print('b : ' , b)#10.8
print('_ : ' , _)#3+4j
print('d : ' , d)#True
print('_: ' , _)#3+4j

#17
# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list# multiple stars

#18
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)#[25 , 10.8]
print('b :  ' , b)#'Hyd'
print('c :  ' , c)#True

#19
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
a , b , c , d = list

#20
# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)#true
print(a  is   b)#False
print(a < c)#True
print(a > d)#True
print(a >= c)#False
print(a <= d)#False
print(a != c)#True
print(a != b)#False
print(a == c)#False

#21
# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)#False
print(a  is   b)#False

#22
#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))#4
b = []
print(len(b))#0
c = [[10 , 20] , 30 , 40]
print(len(c))#3

#23
# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))#36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))#8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))#39.8+4j
d = [10 , 20 , 15 , 18]
print(sum(d))#63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))#error str is not supported

#24
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a))#error
print(sum(a[0]))#63
print(sum(x for x in a[0]))#63

#25
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))#30
print(min(a))#5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))#vamsi
print(min(b))#Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))#not supported
d = [25 , '35']
#print(max(d))#error not supported
#print(max([]))#error argument is empty
#print(min([]))#error argument is empty

#26
# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)#[10, 20, 15, 18]
print(type(b))#<class 'list'>
print(a  is  b)#False
print(a == b)#False

#27
#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)#[4, 6, 8]
print(type(b))#<class 'list'>
a = list('Vamsi')
print(a)#['V', 'a', 'm', 's', 'i']
a = list()
print(a)#[]
#print(list(25))#int object is not interable
#print(list(10.8))#int object is not interable
#print(list(True))#bool object is not interable
#print(list(None))#bool object is not interable

#28
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))#[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))#[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))#[[10, 20], (30, 40), {50, 60}]

#29
# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)#['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c)#['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
['
print(a)#['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

#30
# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))#True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))#False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))#False
d = [10 , 0 , 20]
print(all(d))#False
e = []
print(all(e))#True

#31
# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))#True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))#False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))#True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))#False
e = []
print(any(e))#False

