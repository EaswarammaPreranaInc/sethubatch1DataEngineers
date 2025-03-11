#isspace() method demo program
print('\n A\t'.isspace()) #False
print('\n \t'.isspace())  #True
print('\n 7\t'.isspace()) #False
print('\n'.isspace())     #True
print('\n $\t'.isspace()) #False
print('\t'.isspace())     #True
print(''.isspace())       #False
print(' '.isspace())      #True


# Find  outputs
a,b,c=25,10.8,'Hyd'
print('a: {}\tb: {}\tc: {}'.format(a,b,c))          #a: 25<tab>b: 10.8<tab>c: Hyd
print('a: {0}\tb: {1}\tc: {2}'.format(a,b,c))       #a: 25<tab>b: 10.8<tab>c: Hyd
print('a: {2}\tb: {1}\tc: {0}'.format(a,b,c))       #a: Hyd<tab>b: 10.8<tab>c: 25
print('a: {2}\tb: {2}\tc: {2}'.format(a,b,c))       #a: Hyd<tab>b: Hyd<tab>c: Hyd
print('a: {x}\tb: {y}\tc: {z}'.format(x=a,y=b,z=c)) #a: 25<tab>b: 10.8<tab>c: Hyd
print('a: {x}\tb: {y}\tc: {z}'.format(z=a,y=b,x=c)) #a: Hyd<tab>b: 10.8<tab>c: 25
print('a: {z}\tb: {z}\tc: {z}'.format(z=a,y=b,x=c)) #a: 25<tab>b: 25<tab>c: 25


#Determine user input is alphabet, digit, white space or special character
a=input('Enter any character: ')
if a.isalnum():
	print('Alphanumeric character')
	if a.isalpha() and a.isupper():
		print('Alphabet character')
		print('Upper case alphabet')
	elif a.isalpha() and a.islower():
		print('Alphabet character')
		print('Lower case alphabet')
	else:
		print('Digit character')
else:
	if a.isspace():
		print('White space')
	else:
		print('Special character')


#Reverse a string without using slice
a=input('Enter any string: ')
b=''
for i in range(1,len(a)+1):
	b+=a[-i]
print('Reverse String:',b)

#Output
Enter any string: Radio Mirchi
Reverse String: ihcriM oidaR


#Reverse order of words in the sentence without slice
a=input('Enter any sentence: ')
b=a.split()
c=''
for i in range(1,len(b)+1):
	c+=b[-i]+' '
print('Reverse String:',c)

#Output
Enter any sentence: Have a nice day
Reverse String: day nice a Have


#Reverse each word of the sentence
a=input('Enter any sentence: ')
b=a.split()
c=''
for x in b:
	c+=x[::-1]+' '
print(c)

#Output
Enter any sentence: Have a nice day


#Sort string in alphabetical order
a=input('Enter any string: ')
b=sorted(a)
print(''.join(b))

#Output
Enter any string: JOURNEY
EJNORUY


#Sort string such that alphabets in alphabetical order and digits in ascending order
a=input('Enter any string with alphabets and digits: ')
b=sorted(a)
c,d='',''
for x in b:
	if x.isalpha():
		c+=x
	elif x.isdigit():
		d+=x
	else:
		print('Give a string with only alphaets and digits')
		exit()
print(''.join(c)+''.join(d))

#Output
Enter any string with alphabets and digits: Z9K2a8F5j4y6
FKZajy245689


#What are the outputs if input is [25, 10.8, 'Hyd', True]
a=input('Enter list: ')   #[25,10.8,'Hyd',True]
print(type(a))            #<class 'str'>
print(a)                  #[25,10.8,'Hyd',True]
b=eval(a)
print(b)                  #[25, 10.8 'Hyd', True]
print(type(b))            #<class 'str'>


#Find outputs
a=[10, 20, 15, 18]
b=a             #b points to same list that a points to
print(a is b)   #True
print(a==b)     #True
b[2]=12
print(a)        #[10, 20, 12, 18]


#Find outputs 
a=[10,20,15,18]
b=[100,200,150]
print(a+b)               #[10, 20, 15, 18, 100, 200, 150]
print(a+5)              #Error (sequence + nonsequence)
print(a+'5')             #Error (list+str)
print([10,20]+(30,40))   #Error (list+tuple)


#Find outputs
list=[25,10.8,'Hyd',True]
a,*b,c=list   #Unpacks list into 3 elements
print('a:',a) #a: 25
print('b:',b) #b: [10.8, 'Hyd']
print('c:',c) #c: True
print(type(b))#<class  'list'>
x,*y=list
print('x:',x) #x: 25
print('y:',y) #y: [10.8, 'Hyd', True]
*p,q=list
print('p:',p) #[25, 10.8, 'Hyd']
print('q:',q) #True


#Find outputs
list=[25,10.8,'Hyd',True]
a,b,c,d,e=list    #Error  
a,b,*c,d,e=list
print('a:',a)     #a: 25
print('b:',b)     #b: 10.8
print('c:',c)     #c: []
print('d:',d)     #d: Hyd
print('e:',e)     #e: True
a,b,*c,d,e,f=list #Error


#Find outputs
list=[25, 10.8, 'Hyd', True]
a,b,_,d=list
print('a:',a) #a: 25
print('b:',b) #b: 10.8
print('_:',_) #_: Hyd
print('d:',d) #d: True


#Find outputs
list=[25,10.8,'Hyd',True,3+4j]
a,b,a,d,a=list
print('a:',a) #a: (3+4j)
print('b:',b) #b: 10.8
print('d:',d) #c: True


#Find outputs
list=[25,10.8,'Hyd',True,3+4j]
a,b,_,d,_ =list
print('a:',a) #a: 25
print('b:',b) #b: 10.8
print('_:',_) #_: (3+4j)
print('d:',d) #d: True
print('_:',_) #_: (3+4j)


#Identify error 
list=[25, 10.8, 'Hyd', True, 3+4j]
a,*b,c,*d,e=list   #Error (multiple '*' operators)


#Find outputs 
list=[[25,10.8],'Hyd',True]
a,b,c=list
print('a:',a) #a: [25, 10.8]
print('b:',b) #b: Hyd
print('c:',c) #True


#Find outputs
list=[[25,10.8],'Hyd',True]
[a,b],c,d=list
print('a:',a) #a: 25
print('b:',b) #b: 10.8
print('c:',c) #c: Hyd
print('d:',d) #d: True
a,b,c,d=list  #Error


#Comparing Lists
a=[10,20,15,18]
b=[10,20,15,18]
c=[10,20,25,9]
d=[10,20,7,22]
print(a==b)   #True
print(a is b) #False
print(a<c)    #True
print(a>d)    #True
print(a>=c)   #False
print(a<=d)   #False
print(a!=c)   #True
print(a!=b)   #False
print(a==c)   #False


#Comparing Lists
a=[10,20,15,18]
b=[20,18,15,10]
print(a==b)   #False
print(a is b) #Flase


#len() function demo program
a=[25,10.8,'Hyd',True]
print(len(a))      #4
b=[]
print(len(b))      #0
c=[[10,20],30,40]
print(len(c))      #3


#sum() function demo program
a=[25,10.8,True]
print(sum(a))     #36.8
b=[3+4j,5+6j]
print(sum(b))     #(8+10j)
c=[25,10.8,True,3+4j,False]
print(sum(c))     #(39.8+4j)
d=[10,20,15,18]
print(sum(d))     #63
e=[25,10.8,'Hyd',True]
print(sum(e))     #Error due to 'Hyd'


#Find outputs
a=[[10,20,15,18]]
#print(sum(a))      #Error
#How to determine sum of inner list elements
print('Sum:',sum(*a))     #63
#How to determine sum of inner list elements in another way
b,sum=*a,0
for i in range(len(b)):
	sum+=b[i]
print('Sum:',sum)


# max()  and  min()  functions  demo  program  (Home  work)
a=[10,20,15,18,30,5,12]
print(max(a))         #30
print(min(a))         #5
b=['Rama','Sita','Rajesh','Kiran','Amar','Vamsi','Manohar']
print(max(b))         #Vamsi
print(min(b))         #Amar
c=[25,10.8,3+4j,True]
print(max(c))         #Error due to 3+4j
d=[25,'35']
print(max(d))         #Error due to int and str
print(max([]))        #Error due to no arguments in max
print(min([]))        #Error due to no arguments in min


#list() function demo program
a=(10,20,15,18)
b=list(a)
print(b)       #[(10, 20, 15, 18)]
print(type(b)) #<class 'list'>
print(a is b)  #False
print(a==b)    #False


#Find outputs
a=range(4,10,2)
b=list(a)
print(b)          #[4, 6, 8]
print(type(b))    #<class 'list'>
a=list('Vamsi')
print(a)          #['V','a','m','s','i']
a=list()
print(a)          #[]
print(list(25))   #Error (list(nonsequence))
print(list(10.8)) #Error
print(list(True)) #Error
print(list(None)) #Error


#Find outputs
a=((10,20),(30,40,50),(60,70,80,90))
print(list(a))   #[(10,20),(30,40,50),(60,70,80,90)]
b={(10,20),(30,40,50),(60,70,80,90)}
print(list(b))   #[(30,40,50),(60,70,80,90),(10,20)]
c=([10,20],(30,40),{50,60})
print(list(c))   #[[10,20],(30,40),{50,60}]


#Find outputs 
a=['Rama','Rajesh','Amar','Sita','Vamsi','Kiran','Rama Rao']
b=sorted(a)    
print(b)      #['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama Rao', 'Sita', 'Vamsi']
c=sorted(a,reverse = True)
print(c)      #['Vamsi', 'Sita', 'Rama Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a)      #['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama Rao']


#all() function demo program 
a=[12>10, 5<20, 30==30]
print(all(a))     #True
b=[9>=6, 12<=9, 6==6]
print(all(b))     #False
c=[25, 10.8, '', True, 3+4j, 'Hyd']
print(all(c))     #False
d=[10,0,20]
print(all(d))     #False
e=[]
print(all(e))     #True


#any() function demo program 
a =[12>18,5<20,35==30]
print(any(a))   #True
b=[12>18,25<20,35==30]
print(any(b))   #False
c=[0, 0.0, '', 25, 0+0j, False]
print(any(c))   #True
d=[0, 0.0, '', 0+0j, False]
print(any(d))   #False
e=[]
print(any(e))   #True
