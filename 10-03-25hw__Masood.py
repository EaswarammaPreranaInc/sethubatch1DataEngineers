1st PROGRAM
'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
CODE:

a=input("enter a string:")
out='aeiou'
c=''
a=a.upper()
for i in range(len(a)):
	if a[i] in 'AEIOU' and a[i] not in c:
		c+=a[i]
print(c)

OUTPUT:
enter a string:RaMA rAo
AO

#2ND PROGRAM
'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
print()
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
while  (index := a.find('is',index+1 if 'index' in locals() else 0))!=-1:
	print(index)
print('End')

OUTPUT:
4
23
42
46
End


#3RD PROGRAM
'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except
'''
CODE:
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
try:
   index = a . index('is')
   while  index != -1:
	   print(index)
	   index = a . index('is' , index + 1)
except ValueError:
	print("end")

OUTPUT:
4
23
42
46
end


#4TH PROGRAM
'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''

CODE:
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' , index + 1)
print('End')

OUTPUT:
46
End

#5TH PROGRAM
#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))
print(a . count('is'))
print(a . count('was'))
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))
print(a . count('\t'))
print(a . count('\n'))

OUTPUT:
4
4
0
3
3
3


#6TH PROGRAM
'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
CODE:
a=input("enter a string:")
char=a[0]
b=char+a[1:].replace(char,'*')
print(b)

OUTPUT:
enter a string:babble
ba**le


#7TH PROGRAM

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)
print()
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))
print(a . split())
print(a . split('green'))
#print(a . split(''))
print()
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))
print(a . split())
print(a . split(' '))
print()
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())
print(a . split(' '))
print()
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))

OUTPUTS:
['15', '36', '48']
15:36:48

['Hyd\nis', 'green\tcity']
['Hyd', 'is', 'green', 'city']
['Hyd\nis ', '\tcity']

['Hyd', 'is', 'green', 'city']
['Hyd', 'is', 'green', 'city']
['Hyd\tis\tgreen\tcity']

['Hyd', 'is', 'green', 'city']
['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

['www', 'gmail', 'com']


#8TH PROGRAM
'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method
'''
CODE:
a = input()
b = a.split('+')          
c = [int(num) for num in b]  
print(sum(c))  
print()
print(sum(map(int, a.split('+'))))

OUTPUT:
3+2+4+5+6+21+4+5+8+12
70

#9TH PROGRAM

CODE:
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
#print(':' . join(e))
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))
g = range(5)
#print('-' . join(g))
print()
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) 
print(a . endswith('town'))
print(a . endswith('green' , 3 , 12))
print(a . endswith('green' , 3 , 13))
print(a . endswith(' ' , 3 , 13))
print()

OUTPUT:
15:36:48
Hyd is green city
15,52,10,20,25
www.gmail.com
SankarDayalSarma

True
False
True
False
True


#10TH PROGRAM
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

4) Hint:  Use  endswith()  method
'''

CODE:
a = input()
if len(a) < 3:
    result = a
elif a.endswith('ing'):
    result = a + 'ly'
else:
    result = a + 'ing'

print(result)

OUTPUT:
enter a input:interest
interesting
enter a input:interesting
interestingly


#11TH PROGRAM

CODE:
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
print()
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())
print('Hyd' . isdigit())
print('+-$' . isdigit())
print('A2#' . isdigit())
print('' . isdigit())
print(' ' . isdigit())
#print(9247 . isdigit())
print()
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
print()
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
print()
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())
print('hyd' . isalnum())
print('hYd' . isalnum())
print('9247' . isalnum())
print('' . isalnum())
print('A7g9'  . isalnum())

OUTPUT:
False
True
False
True
False
True
True
False
True

False
True
False
True
False
True
True
False
True

False
True
False
True
True
True
False
True






	
