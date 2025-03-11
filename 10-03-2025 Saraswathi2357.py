#1
k= input("enter the string:")
vowels='AEIOU'
c=""
for i in k:
    i=i.upper()
    if i in vowels and i not in c:
        c=c+i
print(c)


#2
'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index=-1
while  (index:=a.find('Hyd',index+1)) != -1:
	print(index)
print('End')

#3
'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except
'''
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
	index = a . index('is')
	while  index != -1:
		print(index)
		index = a .index('is' , index + 1)
	print('End')
except ValueError:
	print("substring not found")

'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error  when  string  is  not  found  (but  not  -1)

Syntax  is  same  as   find()  method
'''

#4
'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a.rfind('is')
while  index != -1:
	print(index)
	index = a.rfind('is',0,index)
print('End')

#5
'''
(Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
try:
	index = a . rindex('is')
	while  index != -1:
		print(index)
		index = a . rindex('is',0 , index )
	print('End')
except ValueError:
	pass

#6
#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))#4
print(a . count('is' , 19 , 48))#3
print(a . count('was'))#0
#7
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'

print(a . count(' '))#3
print(a . count('\t'))#3
print(a . count('\n'))#3

#8
'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
k=input("enter the string:")
if len(k)>0:
    first=k[0]
    result=first+k[1:].replace(first,'*')
print(result)

#9
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)#'15:36:48'

#10
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))#['Hyd\nis', 'green\tcity']
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split('green'))#['Hyd\nis ', '\tcity']
print(a . split(''))#empty seperator

#11
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))#['Hyd', 'is', 'green', 'city']
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split(' '))#['Hyd\tis\tgreen\tcity']

#12
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split(' '))#['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

#13
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))#['www','gmail','com']


#14
'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method
'''
k=input("enter the input:").split('+')
sum=0
for i in range(len(k)):
    sum=sum+eval(k[i])
print(sum)

#15
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))#15:36:48

b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#Hyd is green city

c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#25,10,52,15,20

d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com

e = [15 , 36 , 48]
#print(':' . join(e))all are integer values

f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#SankarDayalSarma

g = range(5)
print('-' . join(g))#error

#16
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))#true
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))#True

#17
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

4) Hint:  Use  endswith()  method
'''
k=input("enter the input:")
if len(k)<3:
    print(k)
elif k.endswith("ing"):
    result=k+"ly"
    print(result)
else:
    result=k+'ing'
    print(result)

#18
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())#True
print('Hyd$'  . isalpha())#FAlse
print('9247'  .  isalpha())#Flase
print('+-$'    .  isalpha())#False
print('A2#'  .   isalpha())#False
print(''  .  isalpha())#False
print(' '  .  isalpha())#false

#19
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())#False
print('Hyd' . isdigit())#False
print('+-$' . isdigit())#False
print('A2#' . isdigit())#False
print('' . isdigit())#flase
print(' ' . isdigit())#False
#print(9247 . isdigit())#ERROR method not define



'''
isdigit()  method
--------------------
1) When  does  it  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  alphabet  (or) special  character
																					   (or)
															  When  there  are  no  digits  in  the  string
'''

#20
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper())#false
print('RAMA  RAO' . isupper())#TRUE
print('+-$' . isupper())#False
print('HYD123' . isupper())#TRUE
print('HYD+-$' . isupper())#TRUE
print('' . isupper())#False
print('A2#' . isupper())#True

#21
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower())#False
print('rama  rao' . islower())#True
print('+-$' . islower())#False
print('hyd+-$' . islower())#True
print('abc123' . islower())#True
print('' . islower())#False
print('a2#' . islower())#True

#22
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())#False
print('hyd' . isalnum())#true
print('hYd' . isalnum())#true
print('9247' . isalnum())#true
print('' . isalnum())#false
print('A7g9'  . isalnum())#true