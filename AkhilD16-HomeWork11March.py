#1. Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))	# a : 25	b : 10.8	c : hyd	
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))	# a : 25	b : 10.8	c : hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))	# a : Hyd   b : 10.8    c : 25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))	# a : Hyd   b :  Hyd	c : Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))# a : 25	b : 10.8	c : hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))# a : Hyd	b : 10.8	c : 25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))# a : 25	b : 25		c : 25


#2. What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a)) # <class str>
print(a)		#[25 , 10.8 , 'Hyd' , True]
b = eval(a)		# eval() method converts str 'a' to list and points to reference 'b'
print(b)		#[25 , 10.8 , 'Hyd' , True]
print(type(b))	# <class list>


#3.Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a			# Reference 'b' points to reference 'a' object i.e.[10, 20, 15, 18]
print(a  is  b)	# True ('is' compares reference  )
print(a  ==  b)	# True	('==' compares object and list objects are not reussable)
b[2] = 12		# 12 is added at index 2
print(a)		#[10, 20, 12,15, 18]


#4.Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)	#[10 , 20 , 15 , 18,100 , 200 , 150]
#print(a + 5)	# Error list and integers are cannot be concatenated
#print(a + '5')	# Error list and str are cannot be concatenated
#print([10 , 20] + (30 , 40)) #Error list and tuple cannot be concatenated

#5.Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list	# Unpacks  list  into  3  elements
print('a : ' , a)	# a :  25
print('b : ' , b)	# b : [10.8 , 'Hyd']
print('c : ' , c)	# c : True
print(type(b))		# <class  'list'>
x , *y = list		# Unpacks list into 2 elements
print('x : ' , x)	# x : 25
print('y : ' , y)	# y : [10.8 , 'Hyd' ,  True]
*p , q = list		# Unpacks list into 2 elements
print('p : ' , p)	# p: [25 , 10.8 , 'Hyd']
print('q : ' , q)	# q : True



#6.Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list		#Error due to less elements(expected elements 5,got 4)
a , b , *c , d , e = list		# Unpacks list into 5 elements
print('a : ' , a)				# a : 25
print('b : ' , b)				# b : 10.8
print('c : ' , c)				# c : []
print('d : ' , d)				# d : Hyd
print('e : ' , e)				# e : True
#a , b , *c , d , e , f = list	#Error due to less elements(expected elements 5,got 4)


#7.Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list	# Unpacks list into 4 elements
print('a : ' , a)		# a : 25	
print('b : ' , b)		# b : 10.8
print('_ :  ' , _)		# _ : Hyd
print('d : ' , d)		# d : True


#8.Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list	# Unpacks list into 3 elements
print('a : ' , a)			# a : 3+4j
print('b : ' , b)			# b : 10.8
print('d : ' , d)			# d : True


#9.Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list  # Unpacks list into 4 elements
print('a : ' , a)			# a : 25
print('b : ' , b)			# b : 10.8
print('_ : ' , _)			# _ : 3+4j
print('d : ' , d)			# d : True
print('_: ' , _)			# _ : 3+4j

#10.Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
#a , *b , c , *d , e  = list  # Error due multiple '*'

#11. Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list	# Unpacks list into 3 elements
print('a :  ' , a)	# a : [25,10.8]  
print('b :  ' , b)	# b : Hyd
print('c :  ' , c)	# c : True


#12.Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list  # Unpacks list into 3 elements
print('a : ' , a)		# a : 25
print('b : ' , b)		# b : 10.8
print('c : ' , c)		# c : Hyd
print('d : ' , d)		# d : True
#a , b , c , d = list	# Error due to less elements (expected 4,got 3) 

#13.Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)		# True (compares elements of the lists 'a' and 'b')
print(a  is   b)	# False(compares reference of 'a' and 'b'
print(a < c)		# True(compares first matching elements)
print(a > d)		# True(compares first matching elements)
print(a >= c)		# False(compares first matching elements)
print(a <= d)		# False(compares first matching elements)
print(a != c)		# True 
print(a != b)		# False
print(a == c)		# False


#14.Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)		# False (compares objects/elemets and both lists 'a' and 'b' are different objects)
print(a  is   b)	# False	(compares reference since 'a' and 'b' are pointing to different ojects condition becomes False)



#15.len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) #4
b = []
print(len(b))	#0
c = [[10 , 20] , 30 , 40]
print(len(c))	#3

#16.sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # (8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))	# (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))	# 63
e = [25 , 10.8 , 'Hyd' , True]
#print(sum(e))	# Error due to 'Hyd'(Integers and Strings cannot be added)

# 17.Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a)) #Error
print(sum(a[0])) #How  to  determine  sum  of  inner  list  elements i.e. 60

#18.max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))	# 30
print(min(a))	# 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))	# Vamsi
print(min(b))	# Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) # Error due to 3 + 4j
d = [25 , '35'] 
#print(max(d))	# Error due '35'
#print(max([])) # Error due to empty list
#print(min([])) # Error due to empty list


#19.list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a) # 'list(a)' converts tuple to list
print(b)	#[10,20,15,18]
print(type(b))# <class list>
print(a  is  b) # False
print(a == b)	#False

#20.Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)		# 'list(a)' converts range to list
print(b)		# [4,6,8]
print(type(b))	# <class list>
a = list('Vamsi')# Coverts string "Vamsi' to list
print(a)		 # ['V','a','m','s','i']
a = list()
print(a)		# []
#print(list(25)) # Error
#print(list(10.8)) #Error
#print(list(True)) #Error
#print(list(None))#Error


#21.Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) #[ (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) # [[10 , 20] , (30 , 40) , {50 , 60}]

#22.Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) # ['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']
c = sorted(a , reverse = True)
print(c) # ['Vamsi','Sita','Rama Rao', 'Rama','Rajesh','Kiran','Amar']
print(a) # ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

#23.all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) #True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))	# False
d = [10 , 0 , 20]
print(all(d)) # False
e = []
print(all(e)) # True

#24.any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))	# True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))	# False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))	# True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) #False
e = []
print(any(e)) #True
