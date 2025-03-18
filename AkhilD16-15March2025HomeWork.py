'''# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)		#(25,10.8,(3+4j),'HYD',True,None,'HYD',25)
print(type(a))	#<calss tuple>
#a[3] = 'Sec'	#Error...item assignment is not supported by tuple
#a[3 : 6] = 60 , 70 , 80  #Error...item assignment is not supported by tuple

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)		# (10,20,30,40)
print(type(a))	# <class str>
b = eval(a)		
print(b)		# (10,20,30,40)
print(type(b))	# <class tuple>
print(len(b))	#4

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)  # (10 , [70 , 30 , 40] , 50 , 60)
#a[1] = [80 , 90 , 100]	# Error...item assignment is not supported by tuple
print(a)

# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70	# Error...
print(a)		#[10, (20, 30, 40), 50, 60]
a[1] = [80 , 90]
print(a)		#[10, [80, 90], 50, 60]

# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)	# (25,10.8,'HYD',true)
print(type(x))#<class 'tuple'>

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)	#25
print(b)	#10.8
print(c)	#'Hyd'
print(d)	#True
#p , q , r =  x # Error.... 
#a , b , c , d  , e = x  # Error....

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)	# 25
print(b)	# [10.8,'Hyd']
print(c)	# True

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)	# 25
print(b)	# 10.8
print(c)	# []
print(d)	# 'Hyd'
print(e)	# True

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)	# 25
print(b)	# 10.8
print(_)	# (3+4j)
print(d)	# True
print(_)	# (3+4j)

# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)		#(100,110,120,130,140)
print(type(b))	#<class 'tuple')
c = [10 , 20 , 15, 18]
d = tuple(c)	
print(d)		#(10,20,15,18)
e = tuple('Vamsi')
print(e)		#('V','a','m','s','i')
#print(tuple(25))# Error...
print(tuple())	# ()
'''

#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1    2    3    4    5    6    7    8    9   10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')