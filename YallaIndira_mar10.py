'''prigram1:Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set
 Let  input  be   RaMA  rAo
  What  is  the  output ?  ---> AO'''

a=input("Enter any string : ")
a=a.upper()
out="aeiouAEIOU"
c=''
for i in a:
	if i in out:
		if i not in c:
			c=c+i
print(f'Result : {c}')
'''outputs:Enter any string : indIRA
Result : IA'''

#program2:example for find() method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''outputs:4
23
42
46
End'''

#program3:example for index() method
try:	
	s='Hyd is green city. Hyd is hitec city. Hyd is his city'
	index=s.index('is')
	while True:
		print(index)
		index=s.index('is',index+1)
except:
	print("End")
'''outputs:4
23
42
46
End'''

#program4:example for rfind() method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rfind('is')
while  index!=-1:
	print(index)
	index = a . rfind('is',0,index+1)
print('End')
'''output:46
42
23
4
End'''

#program5:exmple for rindex() method 
try:
	s='Hyd is green city. Hyd is hitec city. Hyd is his city'
	index=s.rindex('is')
	while True:
		print(index)
		index=s.rindex('is',0,index+1)
except:
	print("End")
'''output:46
42
23
4
End'''

#program6:  count()  method  
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))   # 4
print(a . count('is' , 19 , 48))  # 3
print(a . count('was'))  # 0

#program7: count() method 
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) # 3
print(a . count('\t'))  # 3
print(a . count('\n'))  # 3

'''program8:Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
Let  input  be  'babble'
What  is  the  output ?  --->  ba**le
hint:using replace() method '''

s=input("Enter any string : ")
print(s[0]+s[1:].replace(s[0],'*'))

'''outputs:Enter any string : indira
ind*ra '''

#progrma8: split() method

a = '15:36:48'
print(a . split(':'))            # ['15','36','48']
print(a)                      #  15:36:48
a = 'Hyd\nis green\tcity'
print(a . split(' '))       # ['Hyd\nis','green\tcity']
print(a . split())       # ['Hyd','is','green','city']
print(a . split('green'))   # ['Hyd\nis','\tcity']
print(a . split(''))        #error due to empty separator
a = 'Hyd	is	green	city'   #  There  is  tab  between  the  words
print(a . split('\t'))   #  ['Hyd','is','green','city']
print(a . split())       # ['Hyd', 'is', 'green', 'city']
print(a . split(' '))    # ['Hyd\tis\tgreen\tcity']
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())   #  ['Hyd', 'is', 'green', 'city']
print(a . split(' '))  # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']
a = 'www.gmail.com' 
print(a . split('.'))  # ['www','gmail','com']

''' program9:Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result
Hint:  Use  split()  method
'''
s=input('enter the expression : ').split('+')
sum=0
for x in s:
	a=eval(x)
	sum=sum+a
print(f'sum : {sum}')

'''output:enter the expression : 23+456+7
sum : 486 '''

# program10: join() method
a = ['15' , '36' , '48']
print(':' . join(a))    # 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))     #  Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))    # 10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))  # www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))  # error due to only sequence of string elements only
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))   # SankarDayalSarma
g = range(5)
print('-' . join(g))  # error due to range contains integer numbers only

#program11: endswith()  method   progrram
a = 'Hyd is green city'
print(a . endswith('city'))  # True
print(a . endswith('town'))   # False
print(a . endswith('green' , 3 , 12))  # True
print(a . endswith('green' , 3 , 13))  # False
print(a . endswith(' ' , 3 , 13))   #True

''' program12 : Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters'''

s=input('enter string :')
length=len(s)
if length>=3 and s.endswith('ing'):
    print(s+'ly')
elif length>=3 and (not s.endswith('ing')):
    print(s+'ing')
else:
    print(s)

'''outputs:enter string :end
ending '''

#program13: isalpha()  method  program
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())  # False
print('Hyd$'  . isalpha())  # False
print('9247'  .  isalpha())  # False
print('+-$'    .  isalpha())  # False
print('A2#'  .   isalpha())  # False
print(''  .  isalpha())    # False
print(' '  .  isalpha()) # False

#program14:# isdigit()  method  program
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())  # False
print('Hyd' . isdigit())    # False
print('+-$' . isdigit())    # False
print('A2#' . isdigit())    # False
print('' . isdigit())   # False
print(' ' . isdigit())  # False
print(9247 . isdigit())  # error because 'int' object has no attribute 'isdigit'

#program15: isupper()  method  program  
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper())  # False
print('RAMA  RAO' . isupper())  # True
print('+-$' . isupper())   # False
print('HYD123' . isupper())  # True 
print('HYD+-$' . isupper())   #  True
print('' . isupper())  # False
print('A2#' . isupper()) # True

#program16: islower()  method program
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower()) #  False
print('rama  rao' . islower()) # True
print('+-$' . islower())  # False
print('hyd+-$' . islower())  # True
print('abc123' . islower())  # True
print('' . islower())     #  False
print('a2#' . islower())  #  True

#program17:isalnum()  method program 
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum()) # False
print('hyd' . isalnum())  # True
print('hYd' . isalnum()) # True
print('9247' . isalnum())  # True
print('' . isalnum())   # False
print('A7g9'  . isalnum())  # True


 



