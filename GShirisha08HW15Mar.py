#Find outputs 
a=25,10.8,3+4j,'Hyd',True,None,'Hyd',25
print(a) #(25,10.8,3+4j,'Hyd',True,None,'Hyd',25)
print(type(a)) #<class  'tuple'>
a[3]='Sec'   #Error
a[3:6]=60,70,80  #Error


#What are the outputs if input is (10,20,30,40)?
a=input('Enter Tuple : ')
print(a)        #(10,20,30,40)
print(type(a))  #<class 'str'>
b=eval(a)
print(b)        #(10,20,30,40)
print(type(b))  #<class 'tuple'>
print(len(b))   #4


#Find outputs 
a=(10,[20,30,40],50,60)
a[1][0]=70    #Error
print(a)      #(10,[20,30,40],50,60)
a[1]=[80,90,100]  #Error
print(a)      #(10,[20,30,40],50,60)


#Find outputs
a = [10,(20,30,40),50,60]
a[1][0]=70   #Error
print(a)     #[10,(20,30,40),50,60]
a[1]=[80,90]
print(a)     #[10,[80,90],50,60]


#Find outputs 
a=25
b=10.8
c='Hyd'
d=True
x=a,b,c,d
print(x)      #(25,10.8,'Hyd',True)
print(type(x))#<class 'tuple'>


#Find  outputs 
x=25,10.8,'Hyd',True
a,b,c,d=x
print(a)  #25
print(b)  #10.8
print(c)  #Hyd
print(d)  #True
p,q,r=x   #Error
a,b,c,d,e=x #Error


#Find outputs
x=25,10.8,'Hyd',True
a,*b,c=x
print(a) #25
print(b) #[10.8,'Hyd']
print(c) #True


tpl=25,10.8,'Hyd',True
a,b,*c,d,e=tpl
print(a) #25
print(b) #[10.8,'Hyd']
print(c) #[]
print(d) #Hyd
print(e) #True


#Find outputs 
x=25,10.8,'Hyd',True,3+4j
a,b,_,d,_=x
print(a) #25
print(b) #10.8
print(_) #(3+4j)
print(d) #True
print(_) #(3+4j)


#tuple() function demo program
a=range(100,150,10)
b=tuple(a)
print(b)   #(100,110,120,130,140)
print(type(b)) #<class 'tuple'>
c=[10,20,15,18]
d=tuple(c) 
print(d)   #(10,20,15,18)
e=tuple('Vamsi')
print(e)   #('V','a','m','s','i')
print(tuple(25)) #Error
print(tuple())   #()


a=(10,20,15,12,14,15,18,19,15,12,25)
try:
	i=a.index(15) #2
	while True:
		print('15 is found at index:'.i) 
		i=a.index(15,i+1)
except:
	print(F'15 is found {a.count(15)} times')
#Output
15 is found at index: 2
15 is found at index: 5
15 is found at index: 8
15 is found 3 times


#How to modify an element of tuple
a=10,20,30,40,50
a[2]=35     #Error
print(a)    #(10,20,30,40,50)
print(id(a))#Some address
#How to modify 30 in tuple to 35
try:
	x=list(a)
	i=x.index(30)
	x[i]=35
	a=tuple(x)
	print(a)      #(10,20,35,40,50)
	print(id(a))  #some other address
except:
	print('30 is not found')


#delete an element of tuple
a=10,20,30,40,50
a.remove(30) #Error
del a[2]    #Error
a.pop(2)   #Error
x=list(a)
x.remove(30)
a=x
print(a)      #(10,20,40,50)
print(id(a))  #some other address


#Nested tuple
a=((10,20),(30,40,50),(60,70,80,90))
print(a)       #((10,20),(30,40,50),(60,70,80,90))
print(type(a)) #<class 'tuple'>
print(len(a))  #3
print(a[0])    #How to print first inner tuple
print(a[1])    #How to print second inner tuple
print(a[2])    #How to print third inner tuple
print(a[0][1]) #How to print 20
print(a[1][2]) #How to print 50
print(a[2][3]) #How to print 90


#Find outputs
a=((10,20,30),)
print(a[0]) #How to print inner tuple
print(*a)   #How to print inner tuple
print(a[0][0]) #How to print 10
print(a[0][1]) #How to print 20
print(a[0][2]) #How to print 30


#Find outputs
a=((10,20,30),)
print(a)   #((10,20,30))
print(*a)  #(10,20,30)
b=(())
print(b)   #()
print(*b)  #?


#what are the outputs if input is {10,20,15,18,20,12,18}
a=input('Enter Set: ')
print(a)     #{10,20,15,18,20,12,18}
print(type(a)) #<class 'str'>
b=eval(a) 
print(b)     #{10,15,18,20,12,20,18}
print(type(b)) #<class 'str'>


#find outputs
print({(10,20,30)}) #{(10,20,30)}
print({[10,20,30]}) #Error
print({{10,20,30}}) #Error
print({{}})         #Error


#How to print set in different ways
a={25,True,'Hyd',10.8}
print('Set with print function')
print(a)  #{25,True,'Hyd',10.8} (in any order)
print('Iterate elements of set with for loop')
for x in a:
	print(x)


#Find outputs
a='Hyd'
b=True
c=25
d=1
e='Hyd'
s={a,b,c,d,e}
print(s)   #{'Hyd', True, 25} in any order
print(len(s)) #3
print(type(s)) #<class 'set'>


#Find outputs
s={'Hyd', 25, True, 10.8}
print(s) #{'Hyd', 25, True, 10.8} in some order
a,b,c,d=s
print(a) #Hyd                 25
print(b) #25         or       True
print(c) #True                10.8
print(d) #10.8                Hyd


#Find outputs
s={'Hyd', 25, True, 10.8}
print(s) #{'Hyd',True,25,10.8} 
a,*b=s   #Assigned same as it is printed 
print(a) #Hyd
print(b) #[True,25,10.8]
print(type(b)) #<class 'list'>


#Find outputs
s={'Hyd', 25, True, 10.8}
print(s) #{'Hyd',True,25,10.8} 
a,*b,c=s #Assigned same as it is printed 
print(a) #Hyd
print(b) #[True,25]
print(c) #10.8


#Find outputs
s={20,10,20,10}
print(s) #20,10} in some order
x,y=s    #Assigned same as it is printed
print(x) #20
print(y) #10


#set() function demo program 
a=range(100,151,10)
b=set(a)
print(b)    #{100,110,120,130,140,150} in some order
c=[10,20,15,18,10,50,20,12,18]
d=set(c)
print(d)    #{10,20,15,18,50,12} in some order
e=set('Rama rAo')
print(e)    #{'R','a','m',' ','r','A','o'} in any order
print(set(25)) #Error
print(set()) #Error


#add() method demo program 
a=set()
a.add(True)
a.add(25)
a.add(10.8)
a.add(1)
a.add('Hyd')
a.add(25)
a.add(None)
a.add('Hyd')
a.add(1.0)
print(a)    #{True,25,10.8,'Hyd',None} insetrted in any order
a.add(10,20,30)   #Error (add() method takes only one argument
a.add([10,20,30]) #Error (set cannot hold mutables)


#Find outputs 
a={25,10.8,'Hyd',True}
tpl=(10,20,30)
print(a)      #{10.8,True,25,'Hyd'}
print(id(a))  #Some address maybe 1000
a.add(tpl)    #{10.8,True,(10,20,30),25,'Hyd'}
a.add('Sec')  
print(a)      #{10.8,'Sec',True,(10,20,30),25,'Hyd'}
print(id(a))  #Address  1000
print(len(a)) #6
a.add([100,200,300]) #Error (set cannot hold mutables)
a.add(set())   #Error (set cannot hold mutables)
a.add({})     #Error (set cannot hold mutables)


#Find outputs
s=set()
tpl=(10,20,15,18)
s.add(tpl) 
print(s)    #{(10,20,15,18)}
print(len(s)) #1


# update()  method  demo program  (Home  work)
tpl=(10,20,15,18,10,20)
s=set()
s.update(tpl)   
print(len(s))  #4
print(s)       #{10, 18, 20, 15}
s.update(25)   #Error


#Find  outputs  (Home  work)
a=[10,20,30]
b={30,40,50}
c=(50,60,70)
s=set()
s.update(a,b,c) 
print(s)       #{20,40,50,10,30,70,60}
print(len(s))  #7
s.add(a,b,c)   #Error


#Find  outputs  (Home  work)
a=set()
a.update('Rama Rao')
print(a)    #{'a','R',' ','m','o'}
print(len(a)) #5
a.update(3+4j,10.8,True) #Error


# copy()  method  demo  program  (Home  work)
a={10,20,15,18}
print(a)   #{15,18,10,20}
b=a.copy()
print(b)   #{15,18,10,20}
print(a is b) #False
print(a==b)   #True
c=a
print(a is c) #True


#remove() method demo program
a={25,10.8,'Hyd',True}
print(a)   #{25, 10.8, 'Hyd', True}
a.remove('Hyd')
print(a)   #{25, 10.8, True}
a.remove('Sec') #Error


#remove() method demo program
a={25,10.8,'Hyd',True}
print(a)   #{25, 10.8, 'Hyd', True}
a.discard('Hyd')  
print(a)   #{25, 10.8, True}
a.discard('Sec')
print(a)   #{25, 10.8, True}
a.remove('Sec')  #Error


#clear() method demo program
a={10,20,15,18}
print(a)   #{10, 18, 20, 15}
a.clear()  
print(a)   #set()
print(len(a)) #0


#Find outputs
a={10,20,30,40}
b=[30,40,50,60]
print(a.union(b)) #{10,20,30,60,50,40}
print(a|b)        #Error
print(b.union(a)) #Error
print(a+b)        #Error
