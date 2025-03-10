1
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

a=input('Enter any string: ')
b='aeiou'
c=''
for x in a:
	if x in b and x not in c:
		c+=x
print(c.upper())	

OP-
Enter any string: beautiful
EAUI
-------------------------------------------------------------------------------------------------------------
2
Find all occurences of a word in a string using find() and walrus  operator

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = -1
while  (index:= a . find('is' , index + 1)) != -1:
	print(index)
print('End')

OP-
4
23
42
46
End
--------------------------------------------------------------------------------------------------------------------
3 
Find all occurences of a word in a string using index()
Hint: Use   try  and  except

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . index('is')
while  index != -1:
	print(index)
	try:
		index = a . index('is' , index + 1)
	except ValueError:
		break
print('End')

OP-
4
23
42
46
End
----------------------------------------------------------------------------------------------------------------------
4
Find all occurences of a word in a string using rfind()

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' , 0 ,index)
print('End')

OP-
46
42
23
4
End
-----------------------------------------------------------------------------------------------------------------
5
Find all occurences of a word in a string using rindex()
Hint: Use   try  and  except

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rindex('is')
while  index != -1:
	print(index)
	try:
		index = a . rindex('is' ,0,index)
	except ValueError:
		break
print('End')

OP-
46
42
23
4
End
-------------------------------------------------------------------------------------------------------
6
#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))
print(a . count('is' , 19 , 48))
print(a . count('was'))
---------------------------------------------------------------------------------------------------------
7
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))  #3
print(a . count('\t')) #3
print(a . count('\n')) #3
---------------------------------------------------------------------------------------------------------------------------------------
8
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
Hint : Use  replace()  method

a = input('Enter any string: ')
first_char = a[0]
b=first_char+a[1:].replace(first_char,'*')
print('Result :', b)

OP-
Enter  any  string :  babble
Result :   ba**le
------------------------------------------------------------------------------------------------------------------------------------------
9
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) #['15,'36','48']
print(a)  # 15:36:48
--------------------------------------------------------------------------------------------------------------------------------
10
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyd\nis','green\tcity']
print(a . split())    # ['Hyd', 'is', 'green', 'city']
print(a . split('green'))  #['Hyd\nis ', '\tcity']
#print(a . split('')) #error- seperator is empty
---------------------------------------------------------------------------------------------------------------------
11
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) #['Hyd','is','green','city']
print(a . split())     #['Hyd','is','green','city']
print(a . split(' '))  #['Hyd\tis\tgreen\tcity']
---------------------------------------------------------------------------------------------------------------------------
12
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())             #['Hyd', 'is', 'green', 'city']
print(a . split(' '))          #['Hyd', '' ,'', 'is','', '',  'green', '', '', 'city']
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))         #['www', 'gmail', 'com']
-----------------------------------------------------------------------------------------------------------------------
13
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Hint:  Use  split()  method

a = input('Enter the expression: ')
b = a.split('+')
total = 0
for i in b:
	total+= int(i)
print('Sum: ',total)

OP-
Enter the expression: 23+456+7
Sum:  486
---------------------------------------------------------------------------------------------------------------
14
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))                   # 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))                    # Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))                    #10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))                  #www.gmail.com
#e = [15 , 36 , 48]
#print(':' . join(e))                  #error because for join() list must contain only strings
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))                  #SankarDayalSarma
#g = range(5)
#print('-' . join(g))                 #error because for join() list must contain only strings
---------------------------------------------------------------------------------------------------------------------
15
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))   #True
print(a . endswith('town'))   #False
print(a . endswith('green' , 3 , 12)) # True
print(a . endswith('green' , 3 , 13))  #False 
print(a . endswith(' ' , 3 , 13)) #True
---------------------------------------------------------------------------------------------------------------------
16
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

a=input('Enter string: ')
b=''
if len(a)<3:
	print(a)
else:
	if a.endswith('ing'):
		b=a+'ly'
	else:
		b=a+'ing'
	print(b)
 
OP-
Enter string: run
runing

Enter string: Hi
Hi

Enter string: Sleeping
Sleepingly
--------------------------------------------------------------------------------------------------------------------------
17
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())      #False due to 4
print('Hyd$'  . isalpha())      #False due to $  
print('9247'  .  isalpha())     #False due to all digits
print('+-$'    .  isalpha())    #False due to all special chars
print('A2#'  .   isalpha())     #False due to #
print(''  .  isalpha())         #False due to empty
print(' '  .  isalpha())        #False due to space
-----------------------------------------------------------------------------------------------------------------
18
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())  #False due to $
print('Hyd' . isdigit())    #False due to char
print('+-$' . isdigit())    #False due to special char 
print('A2#' . isdigit())    #False due to char and special char
print('' . isdigit())       #False due to empty string
print(' ' . isdigit())      #False due to space
#print(9247 . isdigit())     #error- there is no method isdigit() for int.
--------------------------------------------------------------------------------------------------------------------------------						
19
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper()) # False due to digits 
print('RAMA  RAO' . isupper()) #True
print('+-$' . isupper()) #False -there are no uppercase letters
print('HYD123' . isupper()) #True
print('HYD+-$' . isupper()) #True
print('' . isupper())       #False due to empty string
print('A2#' . isupper())    #True
-----------------------------------------------------------------------------------------------------------------------
20
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower()) #False due to digits
print('rama  rao' . islower())  #True
print('+-$' . islower())   #False there are no lowercase letters
print('hyd+-$' . islower()) #True
print('abc123' . islower()) #True
print('' . islower())       #False due to empty string
print('a2#' . islower())    #True
-------------------------------------------------------------------------------------------------------
21
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())  #False - no alphabets and there are special char
print('hyd' . isalnum())  #True
print('hYd' . isalnum())  #True
print('9247' . isalnum()) #True
print('' . isalnum())     #False
print('A7g9'  . isalnum()) #True
