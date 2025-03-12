isspace() method demo program
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
