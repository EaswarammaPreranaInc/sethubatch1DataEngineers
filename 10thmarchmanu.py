'''
#1)Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'


a=input("enter a string")
vowels = "AEIOUaeiou"
b =" "
i=0
for x in a:
	if x in vowels and x not in b:
		b += x.upper()
print(b)
'''

'''
#2)Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = 0
while ( index:= a.find('is',index)) != -1:
	print(index)
	index += 1
print('End')
'''
'''
#3)index()  method  demo  program
-----------------------------------

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city is'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


a = 'Hyd is green city. Hyd is hitec city. Hyd is his city is '
index = 0
while True:
    try:
        index = a.index('was', index)
        print(index)
        index += 1  
    except ValueError:
        break  
    print('End')

#4)rfind()  method  demo  program
-------------------------------------
Modify  following  program  with  rfind()  method


a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = len(a)  
while index != -1:
    index = a.rfind('is', 0, index) 
    if index != -1:
        print(index)
        index -= 1  
print('End')


#5)rindex () method demo on same program
------------------------------------------

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = len(a)  # Start searching from the end of the string

while True:
    try:
        index = a.rindex('is', 0, index)  # Search for 'is' from the start to 'index' position
        print(index)
        index -= 1  # Move the index backwards to continue the search
    except ValueError:
        break  # Break the loop if 'is' is not found anymore

print('End')

#6)count()  method  demo  program (Home  work)
-------------------------------------------------

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4 ---Returns  number  of  times 'is' is   found  in 'a'
print(a . count('is' , 19 , 48)) # 3 Returns  number  of  times str2  is  found  in 'a'.
print(a . count('was')) # 0 there is no 'was' in 'a'

#7)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) #3
print(a . count('\t')) # 3
print(a . count('\n'))# 3

#8)Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method

a = 'babble'
first_char = a[0]
b = a[0] + a[1:].replace(first_char, '*')
print(b)


#9)slipt ()

a = '15:36:48'
print(a . split(':')) # ['15','36','48']
print(a) # 15:36:48

#10)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyyd\nis','green\tcity'] here we given <space>so, we didn't get error here
print(a . split()) # ['Hyd','is','green','city']
print(a . split('green')) #['Hyd\nis','\tcity']
print(a . split(''))# error due to empty seperator

#11)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd','is', 'green','city']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) # ['Hyd\tis\tgreen\tcity]

#12)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split()) #[ 'Hyd', 'is', 'green', 'city']
print(a . split(' ')) #['Hyd', '','', 'is', '','','green','','','city']

#13)
a = 'www.gmail.com'
print(a . split('.')) # ['www', 'gmail', 'com']


#14)Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method

a = '23+456+7'
b = a.split('+')
b = [int(num) for num in b]
c = sum(b)
print(c) # 486


#15)
a = ['15' , '36' , '48']
print(':' . join(a)) # 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city') 
print(' ' . join(b)) # Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'} |
print(',' . join(c)) #10,20,52,15,25
d = ['www' , 'gmail', 'com'] 
print('.' . join(d)) # www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) # Error due to int values given
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) # SankarDayalSarma
g = range(5)
print('-' . join(g)) #Error due to range (5) functions.

#16) endswith()  method  demo  progrram (Home  work)

a = 'Hyd is green city'
print(a . endswith('city'))  # True
print(a . endswith('town')) #False
print(a . endswith('green' , 3 , 12)) # True
print(a . endswith('green' , 3 , 13)) #False
print(a . endswith(' ' , 3 , 13)) #True

#17)Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

4) Hint:  Use  endswith()  method

def modify_string(s):
    if len(s) < 3:
        return s  # Return the string unchanged if it has less than 3 characters
    if s.endswith('ing'):
        return s + 'ly'  # Append 'ly' if the string ends with 'ing'
    else:
        return s + 'ing'  # Append 'ing' if the string doesn't end with 'ing'
a = input("Enter a string: ")
b = modify_string(a)
print("Modified string:", b)

#18)isalpha()  method  demo  program (Home  work)

print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha()) #False due to When  at  least  one  character  of  the  string  is  digit  (or) special  character
print('Hyd$'  . isalpha()) #False due to When  at  least  one  character  of  the  string  is special character contains
print('9247'  .  isalpha()) #False due to When  at  least  one  character  of  the  string  is digit contains
print('+-$'    .  isalpha()) #False due to When  at  least  one  character  of  the  string  is special character contains
print('A2#'  .   isalpha()) #False due to When  at  least  one  character  of  the  string  is digit (or) special character contains
print(''  .  isalpha()) #False due to When  at  least  one  character  of  the  string  is empty string contains
print(' '  .  isalpha()) #False due to When  at  least  one  character  of  the  string  is empty string contains

#19) isdigit()  method  demo  program  (Home  work)


print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())  # False  due  to  '$'
print('Hyd' . isdigit())  # False  due  to  'Hyd'
print('+-$' . isdigit())  #False  due  to  '+-$'
print('A2#' . isdigit()) #False  due  to  'A#'
print('' . isdigit())  #False  due  to  'Empty string'
print(' ' . isdigit()) #False  due  to  'space'
print(9247 . isdigit()) # False  due  to  'digits not in quotes'

#20) isupper()  method  demo  program  (Home  work)

print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper()) #  False  due  to  '9247'
print('RAMA  RAO' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('+-$' . isupper())#  False  due  to  'special characters'
print('HYD123' . isupper())#  True  due  to  'HYD'
print('HYD+-$' . isupper())#  True  due  to  'HYD'
print('' . isupper())#  False  due  to  'empty string'
print('A2#' . isupper()) #  True  due  to  'A'

#21)Islower()  method  demo  program  (Home  work)

print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower()) # False due to '9247'
print('rama  rao' . islower()) # True becz there are no upper alphabets
print('+-$' . islower()) # False due to 'special characters'
print('hyd+-$' . islower()) # True due to 'hyd'
print('abc123' . islower())# True due to 'abc'
print('' . islower())# False due to 'space'
print('a2#' . islower())# True due to 'a'


#22) isalnum()  method  demo  program  (Home  work)

print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum()) #  False due to 'special charecters'
print('hyd' . isalnum())#  True bcz there is no special characters
print('hYd' . isalnum()) #  True bcz there is no special characters
print('9247' . isalnum()) # True bcz there is no special characters
print('' . isalnum()) # False due to empty space
print('A7g9'  . isalnum()) # True bcz there is no special characters

