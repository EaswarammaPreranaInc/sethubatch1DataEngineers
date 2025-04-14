# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())
print('\n  \t' . isspace())
print('\n  7\t' . isspace())
print('\n' . isspace())
print('\n  $\t' . isspace())
print('\t' . isspace())
print('' . isspace())
print(' ' . isspace())
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
#Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character
a=input("input bitte")
if a.isalpha():
    print("alphabets")
elif a.isupper():
    print("upper")
elif a.isdigit():
    print("digit")
elif a.isspace():
    print("spaces")
elif a.isupper():
    print("upper")
elif a.islower():
    print("lower")
elif a.alnum():
    print("alphanumeric")
else:
    print("special characters")
#
# Get user input
char = (input("Enter a single character: "))

# Check if input is a single character
if char == '':
    print("Please enter atleast one character.")
else:
    if char.isalnum():  # Check if it's alphanumeric
        print("Alphanumeric character")

        if char.isalpha():  # Check if it's an alphabet
            print("Alphabet character")

            if char.isupper():  # Check if it's an uppercase alphabet
                print("Upper case alphabet")
            elif char.islower():  # Check if it's a lowercase alphabet
                print("Lower case alphabet")

        elif char.isdigit():  # Check if it's a digit
            print("Digit character")

    elif char.isspace():  # Check if it's a whitespace
        print("White space")

    else:
        print("Special character")  # If it's none of the above, it's a special character

#reverse of str
b=input("string")
for i in range(-1,-len(b)-1,-1):
    print(b[i])
#reverse order of words of str
b=input("string")
a=b.split()
c=[]
for i in range(-1,-len(a)-1,-1):
    c.append(a[i])
print(" ".join(c))
#
''''Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice'''
b=input("string")
a=b.split()
c=[]
for i in range(len(a)):
    v=a[i]
    c.append(v[::-1])
print(" ".join(c))
'''Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS

Hint:  Use   sorted()  function  and   join()  method
'''
a=input("input:")
b=sorted(a)
print("sorted string:",''.join(b))
'''
Write  a  program  to  sort  string  such  that  alphabets  in 
alphabetical  order  and  digits  in  ascending  order'''
s=input("str:")
b=''
a=''
for i in s:
    if i.isdigit():
        b+=i
    elif i.isalpha():
        a+=i
k=sorted(a)+(sorted(b))
print("output:","".join(k))
## What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a))
print(a)
b = eval(a)
print(b)
print(type(b))
##  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)#True
print(a  ==  b)#True
b[2] = 12
print(a)#[10, 20, 12, 18]
#
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) #[10, 20, 15, 18, 100, 200, 150]
#print(a + 5)
#print(a + '5')
#print([10 , 20] + (30 , 40))
## Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x)#x :  25
print('y : ' , y)#y :  [10.8, 'Hyd', True]
*p , q = list
print('p : ' , p)#p :  [25, 10.8, 'Hyd']
print('q : ' , q)#q :  True
#
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
'''True
False
True
True
False
False
True
False
False'''
# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #False
print(a  is   b) #False
#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) #4
b = []
print(len(b))#0
c = [[10 , 20] , 30 , 40]
print(len(c))#3
# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))#36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))#(8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))#(39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))#63
#e = [25 , 10.8 , 'Hyd' , True]
#print(sum(e)) sum cannot be btw str and int 
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(*a))
print('How  to  determine  sum  of  inner  list  elements',sum(*a))
for i in a:
    k=sum(i)
print('How  to  determine  sum  of  inner  list  elements  in  another  way',k)
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))
print(min(a))
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))
print(min(b))
#c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))'>' not supported between instances of 'complex' and 'int'
#d = [25 , '35']
#print(max(d))'>' not supported between instances of 'str' and 'int'
#print(max([]))max() iterable argument is empty
#print(min([]))min() iterable argument is empty
# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)
print(type(b))
print(a  is  b)
print(a == b)
##  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)
print(type(b))
a = list('Vamsi')
print(a)
a = list()
print(a)
#print(list(25))'int' object is not iterable
#print(list(10.8))'float' object is not iterable
#print(list(True))'bool' object is not iterable
#print(list(None))#'NoneType' object is not iterable
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))#[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))#[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))#[[10, 20], (30, 40), {50, 60}]
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)
c = sorted(a , reverse = True)
print(c)
print(a)
'''['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']'''
# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))
c = [25 , 10.8 ,   True , 3+4j , 'Hyd']
print(all(c))
d = [10 , 20]
print(all(d))
e = []
print(all(e))
#True False True True True
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
#True False True False False


