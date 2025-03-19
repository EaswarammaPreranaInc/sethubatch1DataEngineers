# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) # False
print('\n  \t' . isspace()) # True
print('\n  7\t' . isspace()) # False
print('\n' . isspace()) # True
print('\n  $\t' . isspace()) # False
print('\t' . isspace()) # True
print('' . isspace()) # False
print(' ' . isspace()) # True

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
a  :  25  	  b  :  10.8  	  c  :  Hyd  
a  :  25  	  b  :  10.8  	  c  :  Hyd  
a  :  Hyd  	  b  :  10.8  	  c  :  25  
a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd  
a  :  25  	  b  :  10.8  	  c  :  Hyd  
a  :  Hyd  	  b  :  10.8  	  c  :  25  
a  :  25  	  b  :  25  	  c  :  25  
'''

# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a)) #<class 'str'>
print(a) #[25 , 10.8 , 'Hyd' , True]
b = eval(a)
print(b)# [25 , 10.8 , 'Hyd' , True]
print(type(b)) #<class 'list'>

#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a # b ref points to a ref both contains same obj
print(a  is  b) # True
print(a  ==  b) # True
b[2] = 12
print(a) #[10, 20, 12, 18]


#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # [10, 20, 15, 18, 100, 200, 150]
print(a + 5)  #can only concatenate list to list
print(a + '5') #can only concatenate list to list
print([10 , 20] + (30 , 40)) #can only concatenate list to list

# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x) #25
print('y : ' , y) #10.8 , 'Hyd' ,  True
*p , q = list
print('p : ' , p) #25 , 10.8 , 'Hyd'
print('q : ' , q) #True

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list #not enough values in list
a , b , *c , d , e = list #not enough values in list
print('a : ' , a) # a :  25
print('b : ' , b) # b :  10.8
print('c : ' , c) # c : []
print('d : ' , d) # d : 'Hyd'
print('e : ' , e) # e : True
a , b , *c , d , e , f = list # not enough values to unpack

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) # a : 25
print('b : ' , b) # b : 10.8
print('_ :  ' , _) # _ : 'Hyd'
print('d : ' , d) # d : True

# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) # a :  (3+4j)
print('b : ' , b) # b :  10.8
print('d : ' , d) # d :  True

# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) #a :  25
print('b : ' , b) #b :  10.8
print('_ : ' , _) #_ :  (3+4j)
print('d : ' , d) #d :  True
print('_: ' , _) #_:  (3+4j)

# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list # Multiple *s

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) #a :   [25, 10.8]
print('b :  ' , b) #b :   Hyd
print('c :  ' , c) #c :   True

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) #a :  25
print('b : ' , b) #b :  10.8
print('c : ' , c) #c :  Hyd
print('d : ' , d) #d :  True
a , b , c , d = list #not enough values

# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # True
print(a  is   b) # False
print(a < c) #True
print(a > d) #True
print(a >= c) #False
print(a <= d) # False
print(a != c) #True
print(a != b) #False
print(a == c) # False

# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #False
print(a  is   b) #False

#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) # 4
b = []
print(len(b)) #0
c = [[10 , 20] , 30 , 40]
print(len(c)) # 3

# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) #36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) #(8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) #(39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d)) #63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) #error str in b/w

# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #30
print(min(a)) #5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) #Vamsi
print(min(b)) #Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) #error
d = [25 , '35']
print(max(d)) #error
print(max([])) # error empty list
print(min([])) # error empty list


# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b) #[10,20,15,18]
print(type(b)) #<class 'list'>
print(a  is  b) #False
print(a == b) #False

#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b) #[4,6,8]
print(type(b))# <class 'list'>
a = list('Vamsi')
print(a) #['V', 'a', 'm', 's', 'i']
a = list()
print(a) # []
print(list(25)) #error
print(list(10.8)) #error
print(list(True))#error
print(list(None))#error


# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) #[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) #[[10, 20], (30, 40), {50, 60}]

# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) #['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) #['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) #['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']

# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) #True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) # False
d = [10 , 0 , 20]
print(all(d)) #False
e = []
print(all(e)) # True


# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) # True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) # False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) # True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) # False
e = []
print(any(e)) # False

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
a = input("Enter value : ")
if a.isalnum():
    print("Alphanumeric  character")
    if a.isdigit():
        print("Digit  character")
    elif a.isalpha():
            print("Alphabet character")
            if a.isupper():
                print("Upper case alphabet")
            elif a.islower():
                print("lower case  alphabet")
elif a.isspace():
   print("White  space")
else:
     print("Special Character")


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

a = input("Enter name : ")
b = ""
for i in range(1,len(a)+1):
    b+=a[-i]
print(b)

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
a= "Hyd  is  green  city"
b = a.split()
print(b)
c= ''
for i in range(1,len(b)+1):
    c+=b[-i] + " "
print(c.strip())

'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
a = "Hyd  is  green  city"
b = a.split()
c = ""
for i in range(len(b)):
    c+=b[i][::-1] + " "
print(c)


'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS

Hint:  Use   sorted()  function  and   join()  method
'''
a = "RAJESH"
b = sorted(a)
c = "".join(b)
print(c)


'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579

1) Hint:  sorted()  function , isalpha() , isdigit()  and   join()  method'''
a = "Z9K3PA7D51"
b = []
c = []
for i in a:
    if i.isalpha():
        b.append(i)
    else:
        c.append(i)
print(sorted(b))
print(sorted(c))
d = sorted(b)+sorted(c)
print("".join(d))


