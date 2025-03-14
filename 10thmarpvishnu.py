"""
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))
#print(a . split())
print(a . split('green'))
#print(a . split(''))

# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))
print(a . split())
print(a . split(' '))

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))

#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))
d = ['www' , 'gmail', 'com']
print('.' . join(d))
e = [15 , 36 , 48]
#print(':' . join(e))#error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))
g = range(5)
#print('-' . join(g))

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) 
print(a . endswith('town'))
print(a . endswith('green' , 3 , 12))
print(a . endswith('green' , 3 , 13))
print(a . endswith(' ' , 3 , 13))


#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())
print('Hyd$'  . isalpha())
print('9247'  .  isalpha())
print('+-$'    .  isalpha())
print('A2#'  .   isalpha())
print(''  .  isalpha())
print(' '  .  isalpha())


# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())
print('Hyd' . isdigit())
print('+-$' . isdigit())
print('A2#' . isdigit())
print('' . isdigit())
print(' ' . isdigit())
#print(9247 . isdigit())#error


# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper())
print('RAMA  RAO' . isupper())
print('+-$' . isupper())
print('HYD123' . isupper())
print('HYD+-$' . isupper())
print('' . isupper())
print('A2#' . isupper())


# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower())
print('rama  rao' . islower())
print('+-$' . islower())
print('hyd+-$' . islower())
print('abc123' . islower())
print('' . islower())
print('a2#' . islower())


# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())
print('hyd' . isalnum())
print('hYd' . isalnum())
print('9247' . isalnum())
print('' . isalnum())
print('A7g9'  . isalnum())


#Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set
a = input('enter a string:')
b = ['a','e','i','o','u']
c=''
for x in a:
	if x in b:
		c += x
print(c.upper())


#index method
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
	index = a . index('is')
	while  index != -1:
		print(index)
		index = a . index('is' , index + 1)
	print('End')
except ValueError:
	print('end of the string')
#find method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

#Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
exp = "3+2+4+5+6+21+4+5+8+12"
a = exp.split("+")
sum = 0
for num in a:
	sum += int(num)
print("sum: ", sum)



#Modify  following  program  with  walrus  operator
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
while (index := a.find('is', index + 1 if 'index' in locals() else 0)) != -1:
    print(index)
print('End')



#Modify  following  program  with  rfind()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

index = a.rfind('is')
while index != -1:
    print(index)
    index = a.rfind('is', 0, index)

print('End')


#Modify  following  program  with  rindex()  method
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
	index = a . rindex('is')
	while  index != -1:
		print(index)
		index = a . rindex('is' ,0 ,index)
	print('End')
except ValueError:
	print("the end")


#Write  a  program  to  replace  every  occurance  of  first  character  in  
#the  string  with  '*'  except  first  character
s='bubble'
a = s[0]
result = s[0] + s[1:].replace(a, '*')
print("Output:",result)


#Write  a  program  to  append  'ing'  to  input  string.
#Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
#Leave  the  string  unchanged  if  string  has  lessthan  three  characters
def append_suffix(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'
print(append_suffix(input('enter a string')))  # Output: interesting
print(append_suffix(input('enter a string')))  # Output: interestingly
print(append_suffix(input('enter a string')))  # Output: Hi
"""