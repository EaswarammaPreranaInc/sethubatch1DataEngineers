program1:
print('\n  A\t' . isspace()) #false
print('\n  \t' . isspace()) #true
print('\n  7\t' . isspace()) #false
print('\n' . isspace()) #true
print('\n  $\t' . isspace()) #false
print('\t' . isspace()) #true
print('' . isspace()) #false
print(' ' . isspace()) #true

program2:
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))

output:
a  :  25  b  :  10.8   c  :  Hyd
a  :  25  b  :  10.8   c  :  Hyd
a  :  Hyd b  :  10.8   c  :  25
a  :  Hyd b  :  Hyd    c  :  Hyd
a  :  25  b  :  10.8   c  :  Hyd
a  :  Hyd b  :  10.8   c  :  25
a  :  25  b  :  25     c  :  25

program3:
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character
a=input('Enter any charcter:')
if a.isalnum():
	print('Alpha numeric character')
	if a.isupper():
		print('uppercase character')
	else:
		print('Lower case character')
elif a.isdigit():
	print('Digit character')
elif a.isspace():
	print('While space')
output:
Enter any charcter:A
Alpha numeric character
uppercase character

program4:
Write  a  program  to  reverse  a  string  without  slice
string='Hyd'
reverse=''
for i in range(len(string)):
	reverse=string[i]+reverse
print(reverse)
output:
dyH

program5:
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
a=input('Enter any sentence:').split()
b=' '
for i in range(1,len(a)+1):
	b=b+' '+a[-1]
print(f'reverse order of word:{b}')
output:
Enter any sentence:Hyd is green city
Reverse order of words: city green is hyd

program6:
Write  a  program  to  reverse  each  word  of  the  sentence
s='python is a programing language'
words=s.split()
reverse_word=[]
for word in words:
	word=word[::-1]
	reverse_words.append(word)
reverse_str=' '.join(reverse_words)
print(reverse_str) 

program7:
Write  a  program  to  sort string  in alphabetic order
a=input('Enter any string:')
b=sorted(a)
print(f'sorted string:{''.join(b) }')
output:
Enter any string:sreshta
sorted string:aehrsst

program8:
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
a=input('Enter any string with alphabatic and digits:')
alp=[]
digit=[]
for x in a:
	if x.isalpha():
		alp.append(x)
		b=sorted(alp)
	elif x.isdigit():
		 digit.append(x)
		 c=sorted(digit)
print(f'Result:{''.join(b)+''.join(c)}')
output:
Enter any string with alphabatic and digits:z9k3pa7d51
Result:adkpz13579
    
program9:  
a = input('Enter  list  :  ') #25 , 10.8 , 'Hyd' , True] 
print(type(a)) #<class 'str'>
print(a) # [25,10.8,'hyd',True]
b = eval(a) 
print(b)# [25, 10.8, 'hyd', True]
print(type(b))#<class 'list'>

program10:
a = [10, 20, 15, 18]
b = a
print(a  is  b)#true
print(a  ==  b) #true
b[2] = 12
print(a) #[10, 20, 12, 18]

program11:
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) #[10, 20, 15, 18, 100, 200, 150]
print(a + 5)#error
print(a + '5')#error
print([10 , 20] + (30 , 40))#error

program11:
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x)#X:25
print('y : ' , y) #y:[10.8.'Hyd',true]
*p , q = list
print('p : ' , p)#p:[25,10.8,'Hyd']
print('q : ' , q)#q:True

program12:
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list
a , b , *c , d , e = list
print('a : ' , a) # a:25
print('b : ' , b) #b:10.8
print('c : ' , c) #c:[]
print('d : ' , d) #d:Hyd
print('e : ' , e) #e:True
a, b , *c , d , e , f = list #error

program13:
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) #a:25
print('b : ' , b) #b:10.8
print('_ :  ' , _) #-:Hyd
print('d : ' , d) #d:True

program14:
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) #a:(3+4j)
print('b : ' , b) #b: 10.8
print('d : ' , d) #d:True

program15:
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) #a:25
print('b : ' , b) #b:10.8
print('_ : ' , _) #-:(3+4j)
print('d : ' , d) #d:True
print('_: ' , _)  #-:(3+4j)

program16:
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list #error

program17:
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)#a:[25,10.8]
print('b :  ' , b) #b:Hyd
print('c :  ' , c) #c:true

program18:
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)#a:25
print('b : ' , b)#b:10.8
print('c : ' , c)#c:Hyd
print('d : ' , d) #d:True
#a , b , c , d = list

program19:
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)#True
print(a  is   b)#false
print(a < c)#True
print(a > d)#True
print(a >= c)#False
print(a <= d)#False
print(a != c)#True
print(a != b) #False
print(a == c) #False

program20:
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)#False
print(a  is   b) #false

program21:
a = [ 25, 10.8, 'Hyd', True]
print(len(a))#4
b = []
print(len(b))#0
c = [[10 , 20] , 30 , 40]
print(len(c)) #3

program22:
a = [25 , 10.8 , True]
print(sum(a))#36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))#(8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))#(39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))#63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))#error

program23:
a = [[10 , 20 , 15 , 18]]
print(sum(a))
print(How  to  determine  sum  of  inner  list  elements)
print(How  to  determine  sum  of  inner  list  elements  in  another  way)

program24:
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))#30
print(min(a))35
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))#VAMSI
print(min(b))#AMAR
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))
d = [25 , '35']
print(max(d))#error
print(max([]))#error
print(min([]))#error

program25:
a = (10 , 20 , 15, 18)
b = list(a)
print(b)#[10,20,15,18]
print(type(b))#<class 'list'>
print(a  is  b)#False
print(a == b)#False

program26:
a = range(4 , 10 , 2)
b = list(a)
print(b)#[4,6,8]
print(type(b))#<class 'list'>
a = list('Vamsi')
print(a)#['v','a','m','s','i']
a = list()
print(a)#[]
print(list(25))#error
print(list(10.8))#error
print(list(True))#error
print(list(None))#error

program27:
a= ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))#[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))#[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))#[[10, 20], (30, 40), {50, 60}]

program28:
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)#['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c)#['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a)#['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']

program29:
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))#True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))#False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))#False
d = [10 , 0 , 20]
print(all(d))#False
e = []
print(all(e))#True

program30:
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))#True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))#False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))#true
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))#False
e = []
print(any(e))#False


