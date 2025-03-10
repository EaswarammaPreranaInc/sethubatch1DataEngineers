a = range(10 , 50 , 5)
print(type(a))    #class <range>
print(a)          #range object
print(*a)         #range object elements 10 to 49 in steps of 5 
print(id(a))      #random address 1000
print(len(a))     #8
print(*a[2 : 7] , sep = ' , ')   #range object elements 20 , 25 , 30 , 35 , 40
print(*a[ : : -1])               #reverse range
#a[4]=32                 # Error cannot modified immutable object
#print(a*2)              #Error

a = range(10 , 20)
print(*a , sep = ',')     #range object elements 10 to 19 in steps 1 sep  by ,
b = range(5)              
print(*b)                 #range elements 0 to 4
c = range(10 , 1 , -1)
print(*c , sep = '...')   #range elements 10 to 2 in steps -1 sep by ...
d = range(-10 , 0)
print(*d)                 #-10 to 1 in steps of 1         
e = range(-10)
print(*e)                 # Empty range
f = range(2 , 2)
print(*f)                 #Empty range
#g = range(10 , 11 , 0.1)   #Error
#h = range('A','F')          #Error


a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)               #object list
print(*a)              #object list elements
print(type(a))         #class <list>
print(id(a))           #random id 1000
print(len(a))          #8
a[2] = 'Sec'           #a[2] is 'Hyd' replaced to 'Sec'
print(a)               #modified list object
print(a[2:5])        #2 to 4 in steps of 1


a = [ ]
print(a)         #empty list
a . append(25)     #append 25
a . append(10.8)   # #append 10.8
a . append('Hyd')    #append 'Hyd'
a . append(True)      #append True
print(a)              #list object
a . remove('Hyd')     #remove 'Hyd'
print(a)              #modified object list
#a . remove('25')      #Error it is not there in this list
print(a)              #list object

a = [25 , 10.8 , 'Hyd']
print(a * 3)     #[25,10.8,'Hyd', 25,10.8,'Hyd' , 25,10.8,'Hyd']
print(a * 2)     #[25,10.8,'Hyd', 25,10.8,'Hyd']
print(a * 1)     #[25 , 10.8 , 'Hyd']
print(a * 0)     #empty list
print(a * -1)    #empty list
#print(a*4.0)   #Error

a = list('Hyd')
print(a)          #['H', 'y', 'd']
print(type(a))    #class <list>
print(len(a))     #3
b = (10 , 20 , 15 , 18)   
print(list(b))          #[10,20,15,18]
print(list(range(5)))   #[0,1,2,3,4]
#print(list(25))         #Error

a = [ ]
print(type(a))     #class <list>
print(a)           #empty list
print(len(a))      #0
b = list()
print(b)           #tupple converts to list
print(len(b))      #0

#        0      1          2         3           4         5       6          7
list = [25 , 10.8 ,     3 + 4j ,    'Hyd' ,    True ,    None ,   10.8 ,    'Hyd']
#       -8      -7        -6          -5         -4       -3       -2         -1
print(list[2 : 7])      #2 to 6 in steps of 1
print(list[ : : ])      #0 to 7 in steps of 1
print(list[:])          #0 to 7 in steps of 1
print(list[ : : -1])    # reverse list
print(list[ : : 2])     #0 to 7 in steps 2
print(list[1 : : 2])    # 1 to 7 in steps of 2
print(list[ : : -2])    #-1 to -8 in steps of -2
print(list[-2 : : -2])  #-2 to -8 in steps of -2 
print(list[1 : 4])      #1 to 3 in steps of 1
print(list[-4 : -1])    #-4 to -2 in steps of 1
print(list[3 : -3])  #  print(list[3 : -4 : 1])  --->  List  from  indexes  3  to  -4 in  steps of  1  i.e. ['Hyd' , True]
print(list[2 : -5])     #3+4j
print(list[-1:-5])      #empty


#        0      1         2        3          4         5         6        7
list = [25 ,   10.8 ,    3+4j ,   'Hyd' ,   True ,     None ,    10.8 ,   'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)        #x = 3
print('y : ' , y)        #y = 5
for  x  in  list[2:7]:   # it iterate 2 to 7
	print(x)             


	#     0    1      2     3     4
a =     [10 ,  20 ,   30 ,  40 ,  50]
print(a)                        #object list
a[1:4] = [60,70,80]       
print(a)                        #modified object list


a =  [25]
#print(a[1])    #Error
print(a[1:])   #Empty list


list  =  [10 , 20 , 15 , 12 , 18]
print(15   in   list)      #True
print(19   in   list)      #False
print(14  not  in  list)   #True
print(12  not  in  list)   #False

