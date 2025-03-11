Ex- 1:-
'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes
 if x >= "a" and x <= 'z' and x >= "A" and x <= 'z' :

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'

'''

a = str(eval(input('Enter any String: ')))
out = ''
for x in a:
    if x in 'aeiouAEIOU':
        if 'a' <= x <= 'z':
            b = chr(ord(x)-32)
            if b not in out:
                out += b
print(out)

Ex-2:-
'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = -1  
while  (index := a . find('is',index+1))!=-1:
	print(index)

print('End')

Ex-3:-
'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except
'''
try:
    a = 'Hyd is green city. Hyd is hitech city. Hyd is his city'
    index = a . index('is')
    while  index != -1:
        print(index)
        index = a . index('naga' , index + 1)
    print('End')
except ValueError:
    print('Substring not found')



Ex-4:-
'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' , index + 1)
print('End')

Ex-5:-
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
        index = a . rindex('is' , index + 1)
    print('End')
except ValueError:
    print('substring not found')

Ex-6:-
#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) # 4
print(a . count('is' , 19 , 48)) # 3
print(a . count('was')) #0


Ex-7:-
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) # 3
print(a . count('\t')) #3
print(a.count('\n')) # 3

Ex-8:-
'''
Write  a  program  to  replace  every  occurrence  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()method

Enter  any  string :  babble
Result :ba**le
'''
a = eval(input('Enter any String with occurrence character: ') ) # No eval()
first_char = a[0]  # Store the first character
print(first_char)
print(a[1:].replace(first_char,'*'))
b = first_char + a[1:].replace(first_char,'*')
print('Result:', b)


# Ex-9:
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) #['15','36','48']
print(a) # '15:36:48'

# Ex-10
a = 'Hyd\nis green\tcity'
print(a . split(' ')) #['Hyd\nis','green\tcity']
print(a . split())#['Hyd','is','green','city']
print(a . split('green'))#['Hyd\nis','\tcity']
# print(a.split('')) # Error because empty separator

# Ex- 10:-
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))    #['Hyd','is','green','city']
print(a . split()) #['Hyd','is','green','city']
#print(a.split('')) # Error because empty separator

# Ex-11:-
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split()) #['Hyd','is','green','city']
#print(a.split('')) # Error because empty separator

Ex-12:-
'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result
'''
Hint:  Use  split()method

try:
    a = (input('Entera Enter the expression: '))
    b = a.split('+')
    sum = 0
    for x in b:
        sum +=eval(x)
    print(sum)
except:
    print('Print expression with + only and not float values')


# Ex- 13:-
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))                         # '15:36:48'
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))                         # 'Hyd is green city'
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))                         # '10,20,15,25,52'
d = ['www' , 'gmail', 'com']
print('.' . join(d))                         # 'www.gmail.com'
e = [15 , 36 , 48]
#print(':' . join(e))                        # Error because split method only strings but not  int
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))                          # SankarDayalSarma
g = range(5)
#print('-'.join(g))                             # Error because split method only strings but not  int

# Ex-14 :-

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) # True
print(a . endswith('town'))  # False
print(a . endswith('green' , 3 , 12)) # True
print(a . endswith('green' , 3 , 13)) # False
print(a . endswith('',3,13)) # True

Ex-15:-
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

4) Hint:  Use  endswith() method
'''
a = eval(input('Enter a String: '))
if len(a) < 3:
    print(a)
elif a.endswith('ing'):
    print(a+'ly')
else:
    print(a+'ing')

# Ex-16:-
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha()) # False due to 4
print('Hyd$'  . isalpha()) # False due to $
print('9247'  .  isalpha()) # False due to 9247
print('+-$'    .  isalpha()) # False due to special characters
print('A2#'  .   isalpha()) # False due to 2 and #
print(''  .  isalpha())  # False due to empty
print(' '  .  isalpha()) # False due to space
print()


#Ex -17:-
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())# False due to $
print('Hyd' . isdigit()) # False due to Hyd
print('+-$' . isdigit()) # False Special character
print('A2#' . isdigit()) # False due to A
print('' . isdigit()) # False due to empty
print(' ' . isdigit()) # False due to space
#print(9247 . isdigit()) # Error because 9247 is not sequence
print()

# Ex-18:-
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper()) # False due to numbers
print('RAMA  RAO' . isupper()) #  # True
print('+-$' . isupper()) # False due to special characters
print('HYD123' . isupper()) # True
print('HYD+-$' . isupper()) # True
print('' . isupper())   # False due to empty
print('A2#' . isupper()) # True
print()

# Ex-19:
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower()) # False due to numbers
print('rama  rao' . islower()) # True
print('+-$' . islower()) # False due to special Characters
print('hyd+-$' . islower()) # True
print('abc123' . islower()) # True
print('' . islower()) # False due to empty
print('a2#' . islower()) # True

# Ex-20:-
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum()) # False due to special Characters
print('hyd' . isalnum()) # True
print('hYd' . isalnum()) #True
print('9247' . isalnum()) # True
print('' . isalnum()) # False due to empty
print('A7g9'  . isalnum()) # True








