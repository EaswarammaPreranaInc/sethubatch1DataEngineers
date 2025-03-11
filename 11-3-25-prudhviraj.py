# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #False
print('\n  \t' . isspace())   #True
print('\n  7\t' . isspace())  #False
print('\n' . isspace())       #True
print('\n  $\t' . isspace())  #False
print('\t' . isspace())       #True
print('' . isspace())         #False
print(' ' . isspace())        #True



# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))  
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))


"""
Output:
a  :  25          b  :  10.8      c  :  Hyd
a  :  25          b  :  10.8      c  :  Hyd
a  :  Hyd         b  :  10.8      c  :  25
a  :  Hyd         b  :  Hyd       c  :  Hyd
a  :  25          b  :  10.8      c  :  Hyd
a  :  Hyd         b  :  10.8      c  :  25
a  :  25          b  :  25        c  :  25
"""


#Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character
a=input("Enter the the input: ")
if (a.isalnum()):
	print("Alphanumeric  character")
	if (a.isalpha()):
		print("Alphabet character")
		if (a.isupper):
			print("Upper case  alphabet")
		else:
			print("lower case  alphabet")
elif (a.isspace() or a=="\\t" or a=="\\n"):
	print("White  space")
else:
	print("Special Character")
"""
Output:
Enter  any  character  :  A
Alpha  Numeric  Character
Alphabet  Character
Upper  case  Alphabet
"""

#Write  a  program  to  reverse  a  string  without  slice
a=input("Enter the string: ")
b=''
for i in range(1,len(a)+1):
	b+=a[-i]
print(b)

"""
Output:
Enter  any  string : Rama Rao
Reverse  String :   oaR amaR
"""


#Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
a=input("Enter the Sentence: ").split()
b=''
for i in range(1,len(a)+1):
	if (i==len(a)):
		b+=a[-i]
	else:
		b+=a[-i]+" "
print(b)
'''
Output:
Enter  any  sententce : students are getting  bored
Reverse  order  of  words :  bored getting are students
'''

#Write  a  program  to  reverse  each  word  of  the  sentence
a=input("Enter the string: ").split()
b=''
for i in range(0,len(a)):
	b+=a[-i][::-1]+" "
print(b.strip())
'''
Output:
Enter  any  sentence  :  hyd is green city
dyh si neerg ytic
'''

#Write  a  program  to  sort  string  in  alphabetical  order
a=input("Enter the String: ")
b=sorted(a)
print(''.join(b))
'''
Output:
Enter  any  string  :  RAJESH
Sorted  string  :    AEHJRS
''' 


#Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
a=input("Enter the string: ")
b=sorted(a)
c=''
d=''
for i in b:
	if i.isdigit():
		d+=i
	else:
		c+=i
print(c+d)
"""
Output:
Enter the string: Z9K3PA7D51
ADKPZ13579
"""
# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a))   #<class 'str'>
print(a)         #[25 , 10.8 , 'Hyd' , True]
b = eval(a)      
print(b)         #[25 , 10.8 , 'Hyd' , True]
print(type(b))   #<class list>


#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) #True
print(a  ==  b) #True
b[2] = 12      
print(a)        #[10, 20, 12, 18]


#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)           #[10,20,15,18,100,200,150]
print(a + 5)           #Error due to int cannot be concatenated
print(a + '5')         #Error due to str cannot be concatenated in list
print([10 , 20] + (30 , 40)) #Error due to two different types.


# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x)   #25
print('y : ' , y)   #[10.8,'Hyd',True]
*p , q = list
print('p : ' , p)   #[25 , 10.8 , 'Hyd']
print('q : ' , q)   #True


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list   
a , b , *c , d , e = list
print('a : ' , a)        #25
print('b : ' , b)        #10.8
print('c : ' , c)        #[]
print('d : ' , d)        #'Hyd'
print('e : ' , e)        #True
a , b , *c , d , e , f = list #Error due to extra argument 'f'


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)   #25
print('b : ' , b)   #10.8
print('_ :  ' , _)  #'Hyd'
print('d : ' , d)   #True


# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)   #3+4j
print('b : ' , b)   # 10.8
print('d : ' , d)   #True


# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)   #25
print('b : ' , b)   #10.8
print('_ : ' , _)   #3+4j
print('d : ' , d)   #True
print('_: ' , _)    #3+4j


# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list       #Here the Error is multiple unpacking 

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)    #[25 , 10.8]
print('b :  ' , b)    #'Hyd'
print('c :  ' , c)    #True


# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)     #25
print('b : ' , b)     #10.8
print('c : ' , c)     #'Hyd'
print('d : ' , d)     #True
a , b , c , d = list  #Error due to values are not enough


# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)    #True
print(a  is   b) #False
print(a < c)     #True
print(a > d)     #True
print(a >= c)    #False
print(a <= d)    #False
print(a != c)    #True
print(a != b)    #False
print(a == c)    #False


# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)           #False
print(a  is   b)        #False


#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))            #4
b = []
print(len(b))            #0
c = [[10 , 20] , 30 , 40]
print(len(c))            #3


# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))                       #36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))                       #8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))                       #39.8+4j
d = [10 , 20 , 15 , 18] 
print(sum(d))                        #63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))                        #Error due string character


#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a))    #Error due to the  int and list
print(sum(*a))    #63
b=a
#print(sum(b))



# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)  
print(b)   #[10 , 20 , 15, 18]
print(type(b)) #<class list>
print(a  is  b)#False
print(a == b)  #False

# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))   #30
print(min(a))   #5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))   #vamsi
print(min(b))   #Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))   #Error due to operand types
d = [25 , '35']
#print(max(d))   #Error due to operand types
#print(max([]))  #Error due to no argument
#print(min([]))  #Error due to no argument

#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)    
print(b)            #[4,6,8]
print(type(b))      #<class list>
a = list('Vamsi')
print(a)            #['v','a','m','s','i']   
a = list()          
print(a)            #[]
#print(list(25))     #error 
#print(list(10.8))   #error
#print(list(True))   #error
#print(list(None))   #error


# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))      #[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))      #[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))      #[[10 , 20] , (30 , 40) , {50 , 60}] 


# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)      #['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c)      #['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a)      #['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

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

