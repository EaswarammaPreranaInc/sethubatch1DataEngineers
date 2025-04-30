'''
prog-1--Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index=0
while  (index :=(a.find('is',index+1)))!=-1:
	         print(index)
	
print('End')

outputs---
4
23
42
46
End

prog--2  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except

try:
   a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
   index1 =0
   while  (index1:=a.index('is' ,index1+1))!=-1:
               print(index1)
		             
   print('End')
except:
	print('there is no more is')

outputs--
4
23
42
46
there is no more is

prog-3
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a .rfind('is')
x=0
while  index !=-1:
	print(index)
	index = a .rfind('is',x,index+1)
	
print('End')

outputs----
46
42
23
4
End

prog-4
Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
try:
   a ='Hyd is green city. Hyd is hitec city. Hyd is his city'  
   index1=a.rindex('is')
   x=0
   while index1!=-1:
	    print(index1)
	    index1=a.rindex('is',x,index1-1)

   print('End')
except:
	   print('there is no more is')
outputs---
46
42
23
4
there is no more is

prog-5
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))
print(a . count('is' , 19 , 48))
print(a . count('was'))
outputs--
4
3
0


#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))#3
print(a . count('\t'))#3
print(a . count('\n'))#3
outputs---
3
3
3

prog-6
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method


a=input('enter any string:')
b=a[1:]
for i in range(len(a)):
	 d=b.replace(a[0],'*')
	 d=a[0]+d
print(d)


outputs---
enter any string:bubble
bu**le


#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))#['15,'36','48']
print(a)#15:36:48

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))#['Hyd\nis', 'green\tcity']
print(a . split())#['Hyd' ,'is','green','city']
print(a . split('green'))#['Hyd\nis','\tcity']
print(a . split(''))#value error

# Find  outputs  (Home  work)
a = 'Hyd    is    green    city' #  There  is  tab  between  the  words
print(a . split('\t'))#['Hyd' , 'is', 'green','city'] 
print(a . split())#['Hyd','is','green','city']
print(a . split(' '))#['Hyd', 'is', 'green', 'city']

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())#['Hyd','is','green','city']
print(a . split(' ')) #['Hyd','is','green','city']

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))#['www','gmail','com']

prog-7 Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method


a=input('enter numbers:').split('+')
b=0
for i in a:
	 b+=int(i)
	 print(b)


#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']#[15:36:48]
print(':' . join(a))
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#['Hyd' 'is' 'green' 'city']
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#['10','20','15','25','25']
d = ['www' , 'gmail', 'com']
print('.' . join(d))#[www.gmail.com]
e = [15 , 36 , 48]
print(':' . join(e))#error due to non-string list
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#['sankarDayalsharma']
g = range(5)#error
print('-' . join(g))

a = 'Hyd is green city'
print(a . endswith('city')) #True
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))#True

prog-8 Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

4) Hint:  Use  endswith()  method


a=input('enter string:')
if len(a)<3:
	   print('itself',a)
elif a.endswith('ing'):
	 print('a+ly:',a+'ly')
elif a.endswith('st'):
	 print('a+ing:',a+'ing')

output--
enter string:intrest
a+ing: intresting

enter string:intresting
a+ly: intrestingly

enter string:hi
itself hi


 #  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())#False due to 4
print('Hyd$'  . isalpha())#False due to $
print('9247'  .  isalpha())#False due to number 9247
print('+-$'    .  isalpha())#False due to special character
print('A2#'  .   isalpha())#False due to #
print(''  .  isalpha())#False due to empty
print(' '  .  isalpha())#False due to empty

print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())#  False  due  to  '$'
print('Hyd' . isdigit())#  False  due  to  'Hyd'
print('+-$' . isdigit())#  False  due  to  special characters
print('A2#' . isdigit())#  False  due  to  A2#
print('' . isdigit())#  False  due  to  empty
print(' ' . isdigit())#  False  due  to  empty
print(9247 . isdigit())#  error due  to  non-string

print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper())# False due to digit
print('RAMA  RAO' . isupper())#True
print('+-$' . isupper())#False due no upper case
print('HYD123' . isupper())#True
print('HYD+-$' . isupper())#True
print('' . isupper())#False due to empty
print('A2#' . isupper())#True

# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower())#False due to digits
print('rama  rao' . islower())#True
print('+-$' . islower())#False due to no lower case letters
print('hyd+-$' . islower())#True
print('abc123' . islower())#True
print('' . islower())#False due to empty
print('a2#' . islower())#True 

# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())#False due to special characters
print('hyd' . isalnum())#True 
print('hYd' . isalnum())#True
print('9247' . isalnum())#True
print('' . isalnum())#false
print('A7g9'  . isalnum())#True'''





     
