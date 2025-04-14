#1ST PROGRAM
# isspace()  method  demo  program  (Home  work)
print('\n  A\t'.isspace())  # False - because 'A' is not whitespace
print('\n  \t'.isspace())   # True  - only whitespace characters
print('\n  7\t'.isspace())  # False - because '7' is not whitespace
print('\n'.isspace())       # True  - newline is whitespace
print('\n  $\t'.isspace())  # False - because '$' is not whitespace
print('\t'.isspace())       # True  - tab is whitespace
print(''.isspace())         # False - empty string returns False
print(' '.isspace())        # True  - space is whitespace



#2 PROGRAM
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) 
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) 
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) 
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) 
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) 
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) 
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) 
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



#3RD PROGRAM
#Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character
a = input("Enter input: ")

if a.isalnum():
    print("Alphanumeric character")
    
    if a.isalpha():
        print("Alphabet character")
        
        if a.isupper():
            print("Upper case alphabet")
        elif a.islower():
            print("Lower case alphabet")
            
    elif a.isdigit():
        print("Digit character")
        
elif a.isspace():
    print("White space")
    
else:
	if a=='':
		print("white space")
	else:
		print("special character")

'''
OUTPUT:
Enter input: A
Alphanumeric character
Alphabet character
Upper case alphabet
'''



#4TH PROGRAM
#Write  a  program  to  reverse  a  string  without  slice
a=input("enter input:")
b=''
for i in range(1,len(a)+1):
	b+=a[-i]
print(b)
'''
OUTPUT:
enter input:hyd
dyh
'''



#5TH PROGRAM
#Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
a=input("enter input:")
b=a.split()
c=''
for i in range(1,len(b)+1):
	if i==1:
		c=b[-i]
	else:
		c+=' '+b[-i]
print(c)
'''
OUTPUT:
enter input:Hyd is green city
city green is Hyd
	'''



#6TH PROGRAM
#Write  a  program  to  reverse  each  word  of  the  sentence
a=input("enter input:")
b=a.split()
c=''
for i in b:
	c+=' '+i[::-1]
print(c)
'''
OUTPUT:
enter input:Hyd is green city
 dyH si neerg ytic

'''



#7TH PROGRAM
a=input("enter string:")
b=sorted(a)
print(b)
c=''.join(b)
print(c)
'''
OUTPUT:
enter string:RAJESH
['A', 'E', 'H', 'J', 'R', 'S']
AEHJRS
	
'''



#8TH PROGRAM
a = input("Enter input: ")
letters =''
digits = ''
for i in a:
    if i.isalpha():
        letters+=i
    elif i.isdigit():
        digits+=i
sorted_letters=sorted(letters)
sorted_digits=sorted(digits)
sorted_letters = ''.join(sorted_letters)
sorted_digits = ''.join(sorted_digits)
c= sorted_letters + sorted_digits
print(c)

'''
OUTPUT:
Enter input: Z9K3PA7D51
ADKPZ13579

'''



#9TH PROGRAM
# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
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
print()


#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)
print(a  ==  b)
b[2] = 12
print(a)
'''
OUTPUT:
True
True
[10, 20, 12, 18]
'''
print()



#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)
#print(a + 5)
#print(a + '5')
#print([10 , 20] + (30 , 40))
'''
OUTPUT:
[10, 20, 15, 18, 100, 200, 150]
'''
print()



# Find  outputs
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

'''
OUTPUT:
a :  25
b :  [10.8, 'Hyd']
c :  True
<class 'list'>
x :  25
y :  [10.8, 'Hyd', True]
p :  [25, 10.8, 'Hyd']
q :  True
'''
print()



# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list
a , b , *c , d , e = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
print('e : ' , e)
#a , b , *c , d , e , f = list
'''
OUTPUT:
a :  25
b :  10.8
c :  []
d :  Hyd
e :  True
'''
print()



# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)
print('b : ' , b)
print('_ :  ' , _)
print('d : ' , d)
'''
OUTPUT:

a :  25
b :  10.8
_ :   Hyd
d :  True
	
	'''



# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)
print('b : ' , b)
print('d : ' , d)
'''
OUTPUT:
a :  (3+4j)
b :  10.8
d :  True
'''


list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)
print('b : ' , b)
print('_ : ' , _)
print('d : ' , d)
print('_: ' , _)
'''
OUTPUT:
a :  25
b :  10.8
_ :  (3+4j)
d :  True
_:  (3+4j)
	
'''


# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
#a , *b , c , *d , e  = list        #syntax error due to multiple starred expressions in assignment

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)
print('b :  ' , b)
print('c :  ' , c)

'''
OUTPUT:
a :   [25, 10.8]
b :   Hyd
c :   True
	
'''



# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
#a , b , c , d = list
'''
OUTPUT:
a :  25
b :  10.8
c :  Hyd
d :  True
'''



# Comparing  Lists
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
print()



# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)
print(a  is   b)
'''
OUTPUT:
False
False
'''


#  len()  function demo   program  (Home  work)
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
print()



# sum()  function  demo  program  (Home  work)
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

'''
OUTPUT:
36.8
(8+10j)
(39.8+4j)
63
'''


#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a))
print("How  to  determine  sum  of  inner  list  elements")
print(sum(a[0]))
print("How  to  determine  sum  of  inner  list  elements  in  another  way")
for i in a:
	print(sum(i))
'''
OUPUT:
63
'''


# max()  and  min()  functions  demo  program  (Home  work)
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
'''
OUTPUT:
30
5
Vamsi
Amar
'''


# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)
print(type(b))
print(a  is  b)
print(a == b)
'''
OUTPUT:
[10, 20, 15, 18]
<class 'list'>
False
False
'''
print()



#  Find  outputs (Home  work)
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
'''
OUTPUT:
[4, 6, 8]
<class 'list'>
['V', 'a', 'm', 's', 'i']
[]
'''



# Find  outputs (Home  work)
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
print()



# Find  outputs  (Home  work)
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
print()




# all()  function demo  program  (Home  work)
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
print()



# any()  function demo program  (Home  work)
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


