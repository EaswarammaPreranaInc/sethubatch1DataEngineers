"""
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


# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a))
print(a)
b = eval(a)
print(b)
print(type(b))



#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)
print(a  ==  b)
b[2] = 12
print(a)


#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)
# print(a + 5)
# print(a + '5')
# print([10 , 20] + (30 , 40))


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



 # Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
# a , b , c , d , e = list
a , b , *c , d , e = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
print('e : ' , e)
a , b , *c , d , e = list

 # Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)
print('b : ' , b)
print('_ :  ' , _)
print('d : ' , d)


 # Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)
print('b : ' , b)
print('d : ' , d)

 # Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)
print('b : ' , b)
print('_ : ' , _)
print('d : ' , d)
print('_: ' , _)

# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , e  = list



 # Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)
print('b :  ' , b)
print('c :  ' , c)


 # Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
# a , b , c , d = list

 # Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)#true
print(a  is   b)#false
print(a < c)
print(a > d)
print(a >= c)
print(a <= d)
print(a != c)
print(a != b)
print(a == c)

 # Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)#false
print(a  is   b)#false
 #  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))
b = []
print(len(b))
c = [[10 , 20] , 30 , 40]
print(len(c))




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



 #  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(*a))
print('How  to  determine  sum  of  inner  list  elements:',sum(*a))
print('How  to  determine  sum  of  inner  list  elements  in  another  way:')

 # max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))#30
print(min(a))#5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))#vamsi
print(min(b))#'Amar'
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))
d = [25 , '35']
#print(max(d))
#print(max([]))
#print(min([]))




# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)#[10 , 20 , 15, 18]
print(type(b))#class list
print(a  is  b)#fasle
print(a == b)

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



 # Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))

 # Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)
c = sorted(a , reverse = True)
print(c)
print(a)

 # all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))#true
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))#false
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))#false
d = [10 , 0 , 20]
print(all(d))#fasle
e = []
print(all(e))

print('\n')
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



# Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  characte

def checkchar(self):
    if c.isspace():
        print("White space")
    elif c.isalnum():
        print("Alphanumeric character")
        if c.isalpha():
            print("Alphabet character")
            if c.isupper():
                print("Upper case alphabet")
            elif c.islower():
                print("Lower case alphabet")
        elif c.isdigit():
            print("Digit character")
    else:
        print("Special character")

c = input("Enter a character: ")
checkchar(c)


# Write  a  program  to  reverse  a  string  without  slice

a = input("Enter a string: ")
s = ""
for i in range(len(a) - 1, -1, -1):
	s += a[i]
print("Reversed string:", s)


# Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

a = input("Enter a sentence: ")
b = a.split()
c = ""
for i in range(len(b) - 1, -1, -1):
	c += b[i] + " "
print("Reversed sentence:",c)


# Write  a  program  to  reverse  each  word  of  the  sentence
sentence = input("Enter a sentence: ")
reversed_sentence = ""
for word in sentence.split():
	reversed_sentence += word[::-1] + " "
print("Reversed sentence:", reversed_sentence)



# Write  a  program  to  sort  string  in  alphabetical  order
a = input("Enter a string: ")
b=''.join(sorted(a))
print("Sorted string:", b.upper())



# Write  a  program  to  sort  string  such  that  alphabets 
# in  alphabetical  order  and  digits  in  ascending  order

a = input("Enter a string: ")
alphabets = sorted([x for x in a if x.isalpha()])
digits = sorted([y for y in a if y.isdigit()])
b=''.join(alphabets + digits)
print("Sorted string:",b)

"""