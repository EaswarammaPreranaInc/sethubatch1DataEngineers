
'''
1.Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'

#vowels --> aeiou '''

s=input("Enter a string: ")# TAKES THE INPUT
out=''# intialise out

for x in s.upper():# loops each character
	if x in 'AEIOU':
	
		if x not in out:# checks if character not in out
			out+=x # cancatenate it
print("String without duplicates: ", out) # print Result 
'''
2. Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

while  (index := a . find('is' , index + 1) )!= -1:
	print(index)
	
print('End')

'''# (Home  work)
3. index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except '''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error  when  string  is  not  found  (but  not  -1)

Syntax  is  same  as   find()  method 
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
	index = a . index('is')
	while True:
		print(index)
		index = a . index('is' , index + 1)
except:
	print('End') '''
'''(Home  work)
4. rfind()  method  demo  program

Modify  following  program  with  rfind()  method

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' , 0,index)
print('End')

'''  (Home  work)
5.rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except '''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
try:
	index = a . rindex('is')
	while True:
		print(index)
		index = a . rindex('is' , 0,index)
except:
	print('End')

# 6. count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))#4
print(a . count('is' , 19 , 48))#3
print(a . count('was'))#0


'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->   Returns  number  of  times  str2  is  found  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->  
														Returns  number  of  times  str2  is  found  in  str1  between  indexes  x  and  y - 1
'''
# 7. Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))#3
print(a . count('\t'))#3
print(a . count('\n'))#3



'''
8. Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
a=input("Enter a String")
char=a[0]
b= char+a[1:].replace(char,'*')
print("Result",b)


#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))#['15','36','48']
print(a)#'15:36:48'

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))#['Hyd\nis','green\tcity']
print(a . split())#['Hyd,is','green,city'] DEfault split is \n \t and space
print(a . split('green'))#[Hyd\nis,\tcity']
#print(a . split(''))#Error due to no separator

# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))#[Hyd,is,green,city]
print(a . split())#[Hyd,is,green,city]
print(a . split(' '))#['Hyd\tis\tgreen\tcity']

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())#[Hyd,is,green,city]
print(a . split(' '))#['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))#['www','gmail','com']

'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method '''

try:
	i=input("Enter an expresion with +: ")
	print(b:=i.split('+'))
	result=0
	for x in b:
		result+=int(x)
	print(result)
except:
	print("Invalid input! Please enter numbers separated by '+'.") 
'''rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error   but  not  -1  when  string  is  not  found

rfind()  method
-------------------
1) What  does  str1 . rfind(str2 , x , y)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  y - 1  downto  x
																			  i.e. right  to  left

2) What  does  str1 . rfind(str2)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  len(str1) - 1  downto  0
																     i.e. right  to  left

3) What  does  str1 . rfind(str2 , x)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  x  to  len(str1) - 1
														                  i.e.  left  to  right

4) How  many  arguments  can  rfind()  method  take ?  --->  1 (or) 3  but  not  2

5) What  is  the  issue  with  two  arguments ?  --->  Method  searches  from  left  to  right  even  though  it  is  rfind()  method

6) What  does  rfind()  method  return  (+ve  (or)  -ve  index) ?  --->  +ve  index  even  though  search  is  from  right  to  left

7) What  does  rfind()  method  do  if  str2  is  not  in  str1 ?  --->  Returns  -1
'''

#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())#False
print('Hyd$'  . isalpha())#False
print('9247'  .  isalpha())#False
print('+-$'    .  isalpha())#False
print('A2#'  .   isalpha())#False
print(''  .  isalpha())#False
print(' '  .  isalpha())#flase



'''
isalpha()  method
---------------------
1) When  does  it  return  True ? --->  When  every  character  of  the  string  is  alphabet

2) When  does  it  return  False  ?  ---> When  at  least  one  character  of  the  string  is  digit  (or) special  character
																					    (or)
													   When  there  are  no  alphabets  in  the  string
'''

# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit()) #False
print('Hyd' . isdigit()) #False
print('+-$' . isdigit()) #false
print('A2#' . isdigit())#false
print('' . isdigit())#FAlse
print(' ' . isdigit())#False 
#print(9247 . isdigit())#Error due to 9247 is not string object



'''
isdigit()  method
--------------------
1) When  does  it  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  alphabet  (or) special  character
																					   (or)
															  When  there  are  no  digits  in  the  string
'''

# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper()) #False
print('RAMA  RAO' . isupper())#True
print('+-$' . isupper())#False
print('HYD123' . isupper())#True
print('HYD+-$' . isupper())#True
print('' . isupper())#false
print('A2#' . isupper())#true 




'''
isupper()  method
----------------------
1) When  does  it  return  True ?  --->  When  at  least  one  character  is  uppercase  alphabet
																						and
															 there  should  not  be  any  lowercase  alphabets  in  the  string

2) When  does  it  return  False ?  --->  When  there  are  no  uppercase  alphabets  in  the  string
																							or
															  at  least  one  character  is  lowercase  alphabet  in  the  string
'''
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower()) # False
print('rama  rao' . islower())#True
print('+-$' . islower())#False
print('hyd+-$' . islower())#True
print('abc123' . islower())#TRue
print('' . islower())#False
print('a2#' . islower())#True


'''
islower()  method
---------------------
1) When  does  it  return  True ?  --->  When  at  least  one  character  is  lowercase  alphabet
																					and
														     there  should  not  be  any  uppercase  alphabets  in  the  string

2) When  does  it  return  False ?  --->  When  there  are  no  lowercase  alphabets  in  the  string
																								or
															  at  least  one  character  is  uppercase  alphabet  in  the  string

Note:
1) What  are  upper()  and  lower()  called ?  ---> Conversion  methods

2) What  are  isupper()  and  islower()  called ?  --->  Conditional  methods  becoz  they  return  True  (or)  False
'''

# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())#False
print('hyd' . isalnum())#True
print('hYd' . isalnum())#True
print('9247' . isalnum())#True
print('' . isalnum())#False
print('A7g9'  . isalnum())#True



'''
isalnum()  method
----------------------
1) When  does  it  return  True ?  --->  When  there  are  no  special  characters  in  the  string

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  speical  character
																						(or)
															  when  there  are  no  alphabets  (or)  digits

3) What  is  isalpha()  +  isdigit()  called ?  --->  isalnum()
'''

#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))#15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com
e = [15 , 36 , 48]
#print(':' . join(e))#it is not  str instance
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#SankarDayalSarma
g = range(5)
#print('-' . join(g))#range has only int values cant use join method 

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) #True
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))#True

'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

4) Hint:  Use  endswith()  method
'''
a=input("Enter a string: ")
if len(a)<3:
	print(a)
elif a.endswith('ing'):
		print(a+'ly')
else: 
	print(a+'ing')
