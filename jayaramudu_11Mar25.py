#Ex-1:-
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) # False due to A
print('\n  \t' . isspace()) # True there is no character
print('\n  7\t' . isspace()) # False due to 7
print('\n' . isspace()) # True  there is no char and digit
print('\n  $\t' . isspace()) # False due to special character
print('\t' . isspace()) # True  there is no char and digit
print('' . isspace()) # False  due to empty
print(' ' . isspace()) # True because space

#Ex-2:-
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # a   :  25   b   :   10.8    c   :   Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # a  :   25  b   :   10.8    c   :   Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # a  :   Hyd b   :  10.8 c   :   25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) #a   :   Hyd b   :   Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a ,y=b,x=c)) # a  :  25  	  b  :  25  	  c  :  25

#Ex-3:-
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

9) Hint2:  Use  nested  if and elif
'''

a = input("Enter any character: ")

if a.isalnum():
    print("Alpha Numeric Character")

    if a.isalpha():
        print("Alphabet Character")

        if a.isupper():
            print("Upper case Alphabet")
        elif a.islower():
            print("Lower case Alphabet")

    elif a.isdigit():
        print("Digit Character")

elif a.isspace():
    print("White Space")

else:
    print("Special Character")

# Ex-4 :-
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
try:
    a = eval(input('Enter any string: '))
    b = ''
    for i in range(1,len(a)+1):
        b +=a[-i]
        print(-i)
    print(b)
except TypeError:
    print('Pleas enter a String')


# Ex-5:-
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

   Enter  any  sententce : students are getting  bored
Reverse  order  of  words :  bored getting are students

'''
from os.path import split

try:
    a = eval(input('Enter any string: '))
    b = a.split(' ')
    c = ''
    for i in range(1,len(b)+1):
        c +=b[-i]+" "
    print(c)
except TypeError:
    print('Pleas enter a String')


# Ex-6
'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and also slice
Enter  any  sentence  :  hyd is green city
dyh si neerg ytic
'''
try:
    a = input('Enter any string: ')
    b = a.split(' ')
    d = ''
    for x in b:
        c = ''
        for j in range(1,len(x)+1):
            c +=x[-j]
        d += c +" "
    print(d)
except TypeError:
    print('Pleas enter a String')
  
# Ex-7
'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS

Hint:  Use   sorted()  function  and   join() method
'''
a = input('Enter a  any string : ')
b = sorted(a)
c=''.join(b)
print(c)


# Ex-8:
'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579

1) Hint:  sorted()  function , isalpha() , isdigit()  and  join() method



a = input('Enter a string : ')
isAlpha = ''
isDigit = ''
for x in a:
    if x.isalpha():
        isAlpha +=x
    elif x.isdigit():
        isDigit +=x
b = sorted(isAlpha)+sorted(isDigit)
res = ''.join(b)
print(res)
'''


# Ex-9
# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a))    # class str
print(a)          # [25 , 10.8 , 'Hyd' , True]
b = eval(a)
print(b)          # [25 , 10.8 , 'Hyd' , True]
print(type(b))    # class int

#Ex-10
#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)  # True
print(a  ==  b) # True
b[2]=12          # modified b[2] is 12
print(a)   #[10, 20, 12, 18]

# Ex-11:
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # [10, 20, 15, 18, 100, 200, 150]
#print(a + 5) # Error becoz concat only list to list but not int
#print(a + '5') # Error becoz concat only list to list but not str
#print([10 , 20]+(30,40)) # Error becoz concat only list to list but not tuple


#Ex-12
# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list  # x = 25, y=[10.8 , 'Hyd' ,  True]
print('x : ' , x) # 25
print('y : ' , y) # [10.8 , 'Hyd' ,  True]
*p , q = list  # q = True  p =[[25 , 10.8 , 'Hyd']
print('p : ' , p) # [[25 , 10.8 , 'Hyd']
print('q:',q) # True


#Ex-13
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list  # Error because list have 4 elements but right side 5 references
a , b , *c , d , e = list # a = 25 b = 10.8 c =[] d = 'Hyd' e =True
print('a : ' , a)  # 25
print('b : ' , b) # 10.8
print('c : ' , c) # []
print('d : ' , d) # Hyd
print('e : ' , e) # True
#a , b , *c , d ,e,f=list # Error because list have 4 elements but right side 6 references


#Ex-14:
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list # a =25 b=10.8 _ = 'Hyd' d=True
print('a : ' , a) # 25
print('b : ' , b) # 10.8
print('_ :  ' , _) # 'Hyd'
print('d:',d) # True

#Ex-15
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list # a =25 b=10.8 a='Hyd' d = True a=3+4j
print('a : ' , a) # 3+4j
print('b : ' , b) # 10.8
print('d:',d) # True

#Ex-16:
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list # a=25 b=10.8 _='hyd' d=True -=3+4j
print('a : ' , a) # 25
print('b : ' , b) # 10.8
print('_ : ' , _) # 3+4j
print('d : ' , d) # True
print('_:',_) # 3+4j

#Ex-17:
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c ,*d,e=list

#Ex-18
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list      # a=[25 , 10.8] # b='Hyd' c=True
print('a :  ' , a)  # a=[25 , 10.8]
print('b :  ' , b) # b='Hyd'
print('c:',c) # c=True

#Ex-19
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list # [a , b]= [25 , 10.8] c='Hyd' d=True
print('a : ' , a) # 25
print('b : ' , b) # 10.8
print('c : ' , c) # 'Hyd'
print('d : ' , d) # True
#a , b,c,d=list # Error because list contains 3 elements but we have found 4

#Ex-20
# Find  outputs  (Home  work)
# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)         # True
print(a  is   b)      # True
print(a < c)           # True
print(a > d)           # True
print(a >= c)          # True
print(a <= d)          # False
print(a != c)           # True
print(a != b)          # False
print(a==c)            # False

#Ex-21
# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)  # False
print(a is b) # False

#Ex-22
#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))                   # 4
b = []
print(len(b))                  # 0
c = [[10 , 20] , 30 , 40]
print(len(c))                  # 3

#Ex-23
# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))                                 # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))                                 # 8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))                                  # 39.8=4j
d = [10 , 20 , 15 , 18]
print(sum(d))                                  # 63
e = [25 , 10.8 , 'Hyd' , True]    # can't possible sum string and float
#print(sum(e))

#Ex-24
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a))
print(*a)
print(sum(a[0]))
print(sum(*a)) #How  to  determine  sum  of  inner  list  elements)
print()#How  to  determine  sum  of  inner  list  elements  in another way)

#Ex-25
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))                      # 30
print(min(a))                      # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))                     # 'Vamsi'
print(min(b))                     # 'Amar'
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))            # not compare int to complex
d = [25 , '35']
#print(max(d))        # not compare int to str
#print(max([]))     # Error bacause list is empty at list one
#print(min([]))   # Error bacause list is empty at list one

#Ex-26
# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a) # Converts tuple to list
print(b)     # [10 , 20 , 15, 18]
print(type(b))  # class list
print(a  is  b) # False
print(a==b)  #  False


#Ex-27
#  Find  outputs (Home  work)
a = range(4 , 10 , 2) # (4,6,8)
b = list(a) #  [4,6,8] converts range to list
print(b)     # [4,6,8]
print(type(b)) # class list
a = list('Vamsi') # ['V','a','m','s','i']
print(a)  # ['V','a','m','s','i']
a = list() # Empty list
print(a) #[]
#print(list(25))   # Error because can not convert non sequence to list
#print(list(10.8)) # Error because can not convert non sequence to list
#print(list(True))  # Error because can not convert non sequence to list
#print(list(None)) # Error because can not convert non sequence to list


# Ex-28
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))              # converts tuple list of tuple    [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))                  # converts set to list of tuple [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))   # coverts tuple to list  [[10 , 20] , (30 , 40) , {50 , 60}]

# Ex-29:-
# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)  # ['Amar','Kiran','Rajesh','Rama','Rama  Rao','Sita','Vamsi']
print(b) # ['Amar','Kiran','Rajesh','Rama','Rama  Rao','Sita','Vamsi']
c = sorted(a , reverse = True)
print(c) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

#Ex-30:-
# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))                                      # True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))                                     # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))                                     # False
d = [10 , 0 , 20]
print(all(d))                                      # False
e = []
print(all(e))                                      # True


# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))                            # True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))                           # False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))                             # True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))                             # False
e = []
print(any(e))                           # False


