'''
#1) isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())# False-When  at  least  one  character  of  the  string  is  not  a  white  space
print('\n  \t' . isspace()) # True-When  every  character  of  the  string  is  white  space  character
print('\n  7\t' . isspace())# False-When  at  least  one  character  of  the  string  is  not  a  white  space
print('\n' . isspace()) # True-When  every  character  of  the  string  is  white  space  character
print('\n  $\t' . isspace())# False-When  at  least  one  character  of  the  string  is  not  a  white  space
print('\t' . isspace())# True-When  every  character  of  the  string  is  white  space  character
print('' . isspace())# False-When  at  least  one  character  of  the  string  is  not  a  white  space
print(' ' . isspace())# True-When  every  character  of  the  string  is  white  space  character


#2)Format () method

a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) #a  :  25        b   :  10.8    c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))#a  :  25        b   :  10.8    c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))#a  :  Hyd        b   :  10.8    c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))#a  :  Hyd        b   :  Hyd    c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))#a  :  25        b   :  10.8    c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a  :  Hyd        b   :  10.8    c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a  :  25        b   :  25    c  :  25

#3)
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  ---> Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  --->  Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->   White  space


def check_input(char):

    if char.isalpha():
        print("Alphanumeric character")
        if char.isupper():
            print("Upper case alphabet")
        else:
            print("Lower case alphabet")
    elif char.isdigit():
        print("Digit")
    elif char.isspace():
        print("Whitespace character")
    else:
        print("Special character")
user_input = input("Enter a character: ")
if len(user_input) == 1:
    check_input(user_input)
else:
    print("Please enter only a single character.")

#4)Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  ---> dyH

def reverse_string(a):
    reversed_string = ""
    for char in a:
        reversed_string = char + reversed_string
    return reversed_string
a = input("Enter a string: ")
print("Reversed string:", reverse_string(a))

#5)Write  a  program  to  reverse  order  of  words  in  the  sentence  with  slice

 Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

def reverse_words(sentence):
    words = sentence.split()  
    reversed_sentence = ""
    for word in words[::-1]:
        reversed_sentence += word + " "  
    return reversed_sentence.strip()
a = input("Enter a sentence: ")
print("Reversed sentence:", reverse_words(a))

#6)Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also without  slices

def reverse_each_word(sentence):
    words = sentence.split()  
    reversed_words = []
    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word  
        reversed_words.append(reversed_word)
    return " ".join(reversed_words)
a = input("Enter a sentence: ")
print("Sentence with reversed words:", reverse_each_word(a))

(or)

def reverse_each_word(sentence):
    words = sentence.split() 
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)
a = input("Enter a sentence: ")
print("Sentence with reversed words:", reverse_each_word(a))


#7)Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS

Hint:  Use   sorted()  function  and   join()  method

def sort_string(input_string):
    # Use sorted() to sort the string and join() to form the final sorted string
    sorted_string = "".join(sorted(input_string))
    return sorted_string
user_input = input("Enter a string: ")
print("Sorted string:", sort_string(user_input))

#8)Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579

1) Hint:  sorted()  function , isalpha() , isdigit()  and   join()  method

def sort_string(a):
    alphabets = [char for char in a if char.isalpha()]
    digits = [char for char in a if char.isdigit()]
    sorted_alphabets = sorted(alphabets)
    sorted_digits = sorted(digits)
    sorted_string = "".join(sorted_alphabets) + "".join(sorted_digits)  
    return sorted_string
a = input("Enter a string: ")
print("Sorted string:", sort_string(a))

#9)What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)

a = input('Enter  list  :  ')
print(type(a)) # <class str> 
print(a) # [25 , 10.8 , 'Hyd' , True]
b = eval(a) 
print(b) #[25, 10.8, 'Hyd' , True]
print(type(b)) #<class list>

#10) Find  outputs (Home  work)

a = [10, 20, 15, 18]
b = a
print(a  is  b) # True
print(a  ==  b) # True
b[2] = 12 #here 'a' is assigned to 'b' so 15 is replaced with 12
print(a) # [10, 20, 12, 18]

#11)Find  outputs  (Home  work)

a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # [10, 20, 15, 18, 100, 200, 150]
print(a + 5) # Error due to only we can concatenate list to list not to list with integer
print(a + '5') # Error due to only we can concatenate list to list not to list with str
print([10 , 20] + (30 , 40)) # Error due to only we can concatenate list to list not to list with Tuple


#12)Find  outputs

list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x)#x :  25
print('y : ' , y) # y :  [10.8, 'Hyd', True]
*p , q = list
print('p : ' , p)#p :  [25, 10.8, 'Hyd']
print('q : ' , q)#q :  True

#13)Find  outputs  (Home  work)

list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list # Error due to objects are 5 but elements in list are 4
a , b , *c , d , e = list
print('a : ' , a) # a :  25
print('b : ' , b) # b :  10.8
print('c : ' , c)#c :  []
print('d : ' , d)# d :  Hyd
print('e : ' , e)# e :  True
a , b , *c , d , e , f = list # Error due to objects are 6 but elements in list are 4

#14)Find  outputs  (Home  work)

list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) #a :  25
print('b : ' , b) #b :  10.8
print('_ :  ' , _)# _ :  Hyd
print('d : ' , d) # d :  True

#15) Find  outputs (Home  work)

list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) #a :  (3+4j)
print('b : ' , b) #b :  10.8
print('d : ' , d) # d :  True

#16)Find  outputs (Home  work)

list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) #a :  25
print('b : ' , b)# b :  10.8
print('_ : ' , _) #_ :  (3+4j)
print('d : ' , d) #d :  True
print('_: ' , _) 3_:  (3+4j)

#17) Identify  error (Home  work)

list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list # Error due to multiple starred expressions in assignment

#18) Find  outputs  (Home  work)

list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) #a :   [25, 10.8]
print('b :  ' , b) # b :   Hyd
print('c :  ' , c) # c :   True

#19)Find  outputs  (Home  work)

list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # a :  25
print('b : ' , b) # b :  10.8
print('c : ' , c) #  c :  Hyd
print('d : ' , d) #  d :  True
a , b , c , d = list # Error due to objects are 4 but elements in list are 3

#20)Comparing  Lists

a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # True
print(a  is   b) # False
print(a < c) # True
print(a > d) # True
print(a >= c)# False
print(a <= d)# False
print(a != c)# True
print(a != b)# False
print(a == c)# False

#21)Comparing  Lists  (Home  work)

a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) # False
print(a  is   b) # False

#22) len()  function demo   program  (Home  work)

a = [ 25, 10.8, 'Hyd', True]
print(len(a)) # 4
b = []
print(len(b)) #0
c = [[10 , 20] , 30 , 40]
print(len(c)) # 3

#23)sum()  function  demo  program  (Home  work)

a = [25 , 10.8 , True]
print(sum(a)) # 36.8
b= [3 + 4j , 5 + 6j]  
print(sum(b)) # (8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d)) # 63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) # Error due to 'Hyd'

#24)Find  outputs

a = [[10 , 20 , 15 , 18]]
print(sum(a)) #Error
print(How  to  determine  sum  of  inner  list  elements) #Error
print(How  to  determine  sum  of  inner  list  elements  in  another  way) #Error

#25)max()  and  min()  functions  demo  program  (Home  work)

a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # 30
print(min(a)) # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) #ERRor due to combination of int, float, complex and bool
d = [25 , '35']
#print(max(d)) # ERRor due to combination of int, str
#print(max([]))#ERRor due to  empty list
#print(min([])) #ERRor due to  empty list

#26)list()  function  demo  program

a = (10 , 20 , 15, 18)
b = list(a) # convert Tuple to List
print(b) # [10, 20, 15, 18]
print(type(b)) # <class 'list'>
print(a  is  b) # False
print(a == b) #False

#27)Find  outputs (Home  work)

a = range(4 , 10 , 2)
b = list(a) # convert range to List
print(b) #[4, 6, 8]
print(type(b)) # <class 'list'>
a = list('Vamsi')
print(a) # ['V', 'a', 'm', 's', 'i']
a = list() # assigning empty list
print(a) #[]
print(list(25))# Error due to  int 25
print(list(10.8)) #Error due to float 10.8
print(list(True)) #Error due to Bool True
print(list(None)) #Error due to None type

#28)Find  outputs (Home  work)

a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) # [(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) # [[10, 20], (30, 40), {50, 60}]

#29)Find  outputs  (Home  work)

a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) #  ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']

#30)all()  function demo  program  (Home  work)

a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) # True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) #False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) #False
d = [10 , 0 , 20]
print(all(d)) #False
e = []
print(all(e)) #True


#31) any()  function demo program  (Home  work)

a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))# True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))# False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) # True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) # False
e = []
print(any(e)) # False

12march class work
------------------

#1)

