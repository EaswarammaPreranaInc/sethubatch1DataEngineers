#Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set
a=input("enter a str")
c=['a','e','i','o','u']
b=''
for i in a:
    if i in c and i not in b:
        b=b+i
print(b.upper())
#Modify  following  program  with  walrus  operator
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = -1
while  (index := a.find('is',index+1))!= -1:
	print(index)
	#index = a . find('is' , index + 1)
print('End')
#Modify  the  following  program  with  index()  method
try:
    a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
    index = a . index('is')
    while  index != -1:
        print(index)
        index = a . index('is' , index + 1,(len(a)-1))
except:
    print("End")
#Modify  following  program  with  rfind()  method
try:
    a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
    index = a . rfind('is')
    while  index != -1:
        print(index)
        index = a . rfind('is' ,-(len(a)),index-1)
except:
    print("End")
#rindex()   method  demo  program
try:
    a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
    index = a . rindex('is')
    while  index != -1:
        print(index)
        index = a . rindex('is' ,-(len(a)), index - 1)
except:
    print("End")
#  count()  method  demo 
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a.count('is'))
print(a . count('is' , 19 , 48))
print(a . count('was'))
print(a.count(' is'))
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a)
print(a . count(' '))
print(a . count('\t'))
print(a . count('\n'))
#Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
a=input("enter any string")
b=a[0]
print("result: ",b+a[1:].replace(b,'*'))
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))
print(a . split())
print(a . split('green'))
#print(a . split(''))
# Find  outputs  (Home  work)
a = 'Hyd\tis\tgreen\tcity' #  There  is  tab  between  the  words
print(a . split('\t'))
print(a . split())
print(a . split(' '))
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())
print(a . split(' '))
a = 'www.gmail.com'
print(a . split('.'))
'''Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result'''
s=input("input:")
k=s.split('+')
su=0
for i in k:
    su+=int(i)
print("sum",su)
##  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))
d = ['www' , 'gmail', 'com']
print('.' . join(d))
#e = [15 , 36 , 48] join method of list only allows string sequence concatenation
#print(':' . join(e))
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))
#g = range(5)
#print('-' . join(g))
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) 
print(a . endswith('town'))
print(a . endswith('green' , 3 , 12))
print(a . endswith('green' , 3 , 13))
print(a . endswith(' ' , 3 , 13))
print(a . endswith('gr',1,9))
'''Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters'''
a=input("input")
if len(a)<=3:
    pass
elif a.endswith('ing'):
    a+='ly'
else:
    a+='ing'
print(a)
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())
print('Hyd$'  . isalpha())
print('9247'  .  isalpha())
print('+-$'    .  isalpha())
print('A2#'  .   isalpha())
print(''  .  isalpha())
print(' '  .  isalpha())
## isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())
print('Hyd' . isdigit())
print('+-$' . isdigit())
print('A2#' . isdigit())
print('' . isdigit())
print(' ' . isdigit())
print('9247' . isdigit())
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())
print('hyd' . isalnum())
print('hYd' . isalnum())
print('9247' . isalnum())
print('v' . isalnum())
print('A7g9'  . isalnum())
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
