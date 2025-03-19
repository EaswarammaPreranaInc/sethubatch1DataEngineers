'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
a= input("Enter Name : ")
b="AEIOU"
d = a.upper()
c=""
for i in range(len(a)):
    if d[i] in b and d[i] not in c:
        c += d[i]
print(c)

'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index= 0
while  (index := a . find('is' , index + 1)) !=-1:
	print(index)
print('End')


'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except
'''
try:
    a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
    index = a . index('is')
    while  True:
        print(index)
        index = a . index('is' , index + 1)
except:
    print("End")


'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' ,0, index + 1)
print('End')

'''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
try:
    a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
    index = a . rindex('is')
    while  index != -1:
        print(index)
        index = a . rindex('is' ,0, index + 1)
except:
    print('End')

#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) # 4
print(a . count('is' , 19 , 48)) # 3
print(a . count('was')) # 0

#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a)
print(a . count(' ')) # 3
print(a . count('\t')) # 3
print(a . count('\n')) # 3


'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
a = input("Enter Value : ")
b = a[0]
c = a.replace(a[0],'*')[1:]
print(b+c)


#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)
'''
['15', '36', '48']
15:36:48
'''

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyd\nis', 'green\tcity']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split('green')) # ['Hyd\nis ', '\tcity']
print(a . split('')) # error cause of empty


# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) #['Hyd', 'is', 'green', 'city']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) #['Hyd\tis\tgreen\tcity']

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) #['www', 'gmail', 'com']

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split()) #['Hyd', 'is', 'green', 'city']
print(a . split(' ')) #['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())  # True
print('hyd' . isalnum()) # True
print('hYd' . isalnum()) #True
print('9247' . isalnum()) # True
print('' . isalnum()) # False
print('A7g9'  . isalnum()) # True


# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower()) # False
print('rama  rao' . islower()) # True
print('+-$' . islower()) # False
print('hyd+-$' . islower()) #True
print('abc123' . islower()) # True
print('' . islower()) # False
print('a2#' . islower()) #True

# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper()) # False
print('RAMA  RAO' . isupper()) # True
print('+-$' . isupper()) # False
print('HYD123' . isupper()) # True
print('HYD+-$' . isupper()) # True
print('' . isupper()) #False
print('A2#' . isupper()) # True


# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit()) # False
print('Hyd' . isdigit())  #False
print('+-$' . isdigit()) #False
print('A2#' . isdigit()) #False
print('' . isdigit()) #False
print(' ' . isdigit()) #False
print(9247 . isdigit()) # error


#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha()) #False
print('Hyd$'  . isalpha()) #False
print('9247'  .  isalpha())#False
print('+-$'    .  isalpha()) #False
print('A2#'  .   isalpha()) #False
print(''  .  isalpha()) #False
print(' '  .  isalpha()) #False


#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) #15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) # Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # 52,25,20,15,10
d = ['www' , 'gmail', 'com']
print('.' . join(d)) #www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) # error sequence
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) # SankarDayalSarma
g = range(5)
print('-' . join(g)) # error sequence


# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))  # True
print(a . endswith('town')) # False
print(a . endswith('green' , 3 , 12)) # True
print(a . endswith('green' , 3 , 13)) # False
print(a . endswith(' ' , 3 , 13)) # True


'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

4) Hint:  Use  endswith()  method
'''
a = input("Enter Name : ")
if a.endswith("ing"):
    print(a+"ly")
elif len(a)<3:
    print(a)
else:
    print(a+"ing")

'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method
'''
a= input("Enter an expression : ")
c = a.split('+')
s = 0
for i in range(len(c)):
    s+=int(c[i])
print(s)


