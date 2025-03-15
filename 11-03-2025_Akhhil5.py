#1 isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())
print('\n  \t' . isspace())
print('\n  7\t' . isspace())
print('\n' . isspace())
print('\n  $\t' . isspace())
print('\t' . isspace())
print('' . isspace())
print(' ' . isspace())

Output:
False
True
False
True
False
True
False
True

#2 Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))

Output:
a  :  25          b  :  10.8      c  :  Hyd
a  :  25          b  :  10.8      c  :  Hyd
a  :  Hyd         b  :  10.8      c  :  25
a  :  Hyd         b  :  Hyd       c  :  Hyd
a  :  25          b  :  10.8      c  :  Hyd
a  :  Hyd         b  :  10.8      c  :  25
a  :  25          b  :  25        c  :  25

#3 Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character
char = input("Enter a character: ")

if char.isalnum():
    print("Alphanumeric character")
    
    if char.isalpha():
        print("Alphabet character")
        
        if char.isupper(): 
            print("Upper case alphabet")
        elif char.islower(): 
            print("Lower case alphabet")

    elif char.isdigit(): 
        print("Digit character")

elif char.isspace(): 
    print("White space")

else:
    print("Special character")

Output:
Enter a character: A
Alphanumeric character
Alphabet character
Upper case alphabet

#4 Write  a  program  to  reverse  a  string  without  slice
s=str(input('Enter a string : '))
p=''
for x in reversed(s):
	p+=x
print(p)

Output:
Enter a string : abcdefgh
hgfedcba

#5 Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
s=str(input('Enter a sentence : '))
k=s.split(' ')
for x in reversed(k):
	print(x,' ',end='')
print()

Output:
Enter a sentence : hyd is green city
city  green  is  hyd

#6 Write  a  program  to  reverse  each  word  of  the  sentence
s=str(input('Enter a sentence : '))
k=s.split(' ')
for x in reversed(k):
	print(x[::-1],' ',end='')
print()

Output:
Enter a sentence : Hyd is green city
ytic  neerg  si  dyH

#7 Write  a  program  to  sort  string  in  alphabetical  order
s=str(input('Enter a string : '))
k=''.join(sorted(s))
print(k)

Output: akhil
ahikl

#8 Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
s=str(input('Enter a string : '))
a=''
n=''
for x in s:
	if x.isalpha():
		a+=x
	else:	
		n+=x
print(''.join(sorted(a)),end='')
print(''.join(sorted(n)))

Output:
Enter a string : Z9K3PA7D51
ADKPZ13579

#9
a = input('Enter  list  :  ')
print(type(a))
print(a)
b = eval(a)
print(b)
print(type(b))

Output:
Enter  list  :  [25 , 10.8 , 'Hyd' , True]
<class 'str'>
[25 , 10.8 , 'Hyd' , True]
[25, 10.8, 'Hyd', True]
<class 'list'>

#10
a = [10, 20, 15, 18]
b = a
print(a  is  b)
print(a  ==  b)
b[2] = 12
print(a)

Output:
True
True
[10, 20, 12, 18]

#11
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)
#print(a + 5)#TypeError
#print(a + '5')#TypeError
#print([10 , 20] + (30 , 40))#TypeError

Output:
[10, 20, 15, 18, 100, 200, 150]

#12
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x)
print('y : ' , y)
*p , q = list
print('p : ' , p)
print('q : ' , q)

Output:
a :  25
b :  [10.8, 'Hyd']
c :  True
<class 'list'>
x :  25
y :  [10.8, 'Hyd', True]
p :  [25, 10.8, 'Hyd']
q :  True

#13
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list
a , b , *c , d , e = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
print('e : ' , e)
#a , b , *c , d , e , f = list

Output:
a :  25
b :  10.8
c :  []
d :  Hyd
e :  True

#14
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)
print('b : ' , b)
print('_ :  ' , _)
print('d : ' , d)

Output:
a :  25
b :  10.8
_ :   Hyd
d :  True

#15
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)
print('b : ' , b)
print('d : ' , d)

Output:
a :  (3+4j)
b :  10.8
d :  True

#16
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)
print('b : ' , b)
print('_ : ' , _)
print('d : ' , d)
print('_: ' , _)

Output:
a :  25
b :  10.8
_ :  (3+4j)
d :  True
_:  (3+4j)

#17
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)
print('b :  ' , b)
print('c :  ' , c)

Output:
a :   [25, 10.8]
b :   Hyd
c :   True

#18
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
#a , b , c , d = list

Output:
a :  25
b :  10.8
c :  Hyd
d :  True

#19
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
print(a == c)

Output:
True
False
True
True
False
False
True
False
False

#20
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)
print(a  is   b)

Output:
False
False

#21
a = [ 25, 10.8, 'Hyd', True]
print(len(a))
b = []
print(len(b))
c = [[10 , 20] , 30 , 40]
print(len(c))

Output:
4
0
3

#22
a = [25 , 10.8 , True]
print(sum(a))
b= [3 + 4j , 5 + 6j]
print(sum(b))
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))
d = [10 , 20 , 15 , 18]
print(sum(d))
e = [25 , 10.8 , 'Hyd' , True]
#print(sum(e))

Output:
36.8
(8+10j)
(39.8+4j)
63

#23
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))
print(min(a))
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))
print(min(b))
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))
d = [25 , '35']
#print(max(d))
#print(max([]))
#print(min([]))

Output:
30
5
Vamsi
Amar

#24
a = (10 , 20 , 15, 18)
b = list(a)
print(b)
print(type(b))
print(a  is  b)
print(a == b)

Output:
[10, 20, 15, 18]
<class 'list'>
False
False

#25
a = range(4 , 10 , 2)
b = list(a)
print(b)
print(type(b))
a = list('Vamsi')
print(a)
a = list()
print(a)
#print(list(25))
#print(list(10.8))
#print(list(True))
#print(list(None))

Output:
[4, 6, 8]
<class 'list'>
['V', 'a', 'm', 's', 'i']
[]

#26
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))

Output:
[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
[[10, 20], (30, 40), {50, 60}]

#27
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)
c = sorted(a , reverse = True)
print(c)
print(a)

Output:
['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']

#28
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

Output:
True
False
False
False
True

#29
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

Output:
True
False
True
False
False
