'''
PROGRAM_1:
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index=a.index('is')
print(index)
while  (index:=a.find("is",index+1))!= -1:
	print(index)
print('End')
'''
OUTPUT:
4
23
42
46
End
'''
'''
PROGRAM_2
'''
a='Hyd is green city. Hyd is hitec city. Hyd is his city'
index=a.rfind('is')
while  index != -1:
	print(index)
	index=a.rfind('is',0,index-1)
print('End')
'''
OUTPUT:
46
42
23
4
End
'''
'''
PROGRAM_3:
'''
a ='Hyd is green city. Hyd is hitec city. Hyd is his city'
index=a.rfind('is')
try:
	while index!=-1:
		print(index)
		index=a.rindex('is',0,index-1)
	print('End')
except:
	print("string is not more found")
'''
PROGRAM_4:
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a.count('is'))
print(a.count('is' , 19 , 48))
print(a.count('was'))

'''
OUTPUT: 
4 
3
0
'''
'''
PROGRAM_5:
'''
a='Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a.count(' '))
print(a.count('\t'))
print(a.count('\n'))
'''
OUTPUT:
3
3
3
'''
'''
PROGRAM_6:
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le
'''
a=input("enter input string : ")
b=a.replace("b","*")
print(b)

'''
OUTPUT:
enter input string : babble
*a**le
'''
'''
PROGRAM_7:
'''
a='15:36:48'
print(a.split(':'))
print(a)
'''
OUTPUT:
['15', '36', '48']
15:36:48
'''
'''
PROGRAM_8:
'''
a='Hyd\nis green\tcity'
print(a.split(' '))
print(a.split())
print(a.split('green'))
#print(a.split(''))--->value error
'''
OUTPUT:
['Hyd\nis', 'green\tcity']
['Hyd', 'is', 'green', 'city']
['Hyd\nis ', '\tcity']
'''
a='Hyd	is	green	city' #  There  is  tab  between  the  words
print(a.split('\t'))
print(a.split())
print(a.split(' '))
'''
OUTPUT:
['Hyd', 'is', 'green', 'city']
['Hyd', 'is', 'green', 'city']
['Hyd\tis\tgreen\tcity']
'''
a='Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a.split())
print(a.split('	'))
'''
OUTPUT:
['Hyd', 'is', 'green', 'city']
['Hyd   is   green   city']
'''
a='www.gmail.com'
print(a.split('.'))
'''
OUTPUT:
['www', 'gmail', 'com']
'''
'''
PROGRAM_9:
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result
'''
a=input("enter input string of alternate numbers and + symbol : ")
b=a.split('+')
sum=0
for i in b:
	sum=sum+eval(i)
print(sum)
'''
OUTPUT:
enter input string of alternate numbers and + symbol : 3+2+4+5+6+21+4+5+8+12
70
'''
'''
PROGRAM_10:
'''
a = ['15' , '36' , '48']
print(':' . join(a))
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))
d = ['www' , 'gmail', 'com']
print('.' . join(d))
e = [15 , 36 , 48]
#print(':' . join(e))--->Error due to list having integers
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))
g=range(5)
#print('-'.join(g))-->Error due not having string elements
'''
OUTPUT:
15:36:48
Hyd is green city
15,52,10,25,20
www.gmail.com
SankarDayalSarma
'''
a = 'Hyd is green city'
print(a.endswith('city')) 
print(a.endswith('town'))
print(a.endswith('green',3,12))
print(a.endswith('green',3,13))
print(a.endswith(' ',3,13))
'''
OUTPUT:
True
False
True
False
False
'''
'''
PROGRAM_11:
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

'''
a=input("Enter input : ")
if len(a)<3:
	print(a)
elif not a.endswith('ing'):
	b=a+"ing"
	print(b)
else:
	a.endswith('ing')
	print(a+'ly')
'''
OUTPUT:
Enter input : interest
interesting
Enter input : interesting
interestingly
Enter input : hi
hi
'''
print('Hyd'  . isalpha()) 
print('Rama  Rao'  . isalpha()) 
print('Hyd4'  . isalpha())
print('Hyd$'  . isalpha())
print('9247'  .  isalpha())
print('+-$'    .  isalpha())
print('A2#'  .   isalpha())
print(''  .  isalpha())
print(' '  .  isalpha())
'''
OUTPUT:
True
False
False
False
False
False
False
False
False
'''
print('9247' . isdigit())  
print('92a47' . isdigit())  
print('92$47' . isdigit())
print('Hyd' . isdigit())
print('+-$' . isdigit())
print('A2#' . isdigit())
print('' . isdigit())
print(' ' . isdigit())
#print(9247 . isdigit()) -->Error
'''
OUTPUT:
True
False
False
False
False
False
False
False
'''
print('HYd' . isupper()) 
print('HYD' . isupper()) 
print('9247' . isupper())
print('RAMA  RAO' . isupper())
print('+-$' . isupper())
print('HYD123' . isupper())
print('HYD+-$' . isupper())
print('' . isupper())
print('A2#' . isupper())
'''
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
'''
print('hyD' . islower()) 
print('hyd' . islower()) 
print('9247' . islower())
print('rama  rao' . islower())
print('+-$' . islower())
print('hyd+-$' . islower())
print('abc123' . islower())
print('' . islower())
print('a2#' . islower())
'''
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
'''
print()
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())
print('hyd' . isalnum())
print('hYd' . isalnum())
print('9247' . isalnum())
print('' . isalnum())
print('A7g9'  . isalnum())
'''
OUTPUT:
False
True
False
True
True
True
False
True
'''
