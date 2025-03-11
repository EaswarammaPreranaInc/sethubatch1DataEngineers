program1:
string=input('Enter any name:')
string=string.upper()
out='aeiouAEIOU'
c=''
for  i  in  string:
	if i in out:
		if i not in c:
			c=c+i
print(c)
 OUTPUT:
	 Enter any name:IndirA
IA

program2:
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
outpit:
4
23
42
46
End

program3:
a='Hyd is green city.Hyd is hitec city.Hyd is his city'
index=0
while(index:=a.find('is',index))!=-1:
	print(index)
	index=index+1
print('End')
output:
4
22
40
44
End

program4:
try:
	s='hyd is green city.hyd is hitec city.hyd is his city'
	index=s.index('is')
	while index!=-1:
		print(index)
		index=s.index('is',index+1)
except:
	print('End')
output:
4
22
40
44
End

program5:
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' , index + 1)
print('End')
output:
46
End

program6:
try:
	a = 'Hyd is green city'
    index = a . rindex('is')
    while  index != -1:
	      print(index)
	      index = a . find('is' , index + 1)
    print('End')
except:
	print('Enter only string')
output:
46
42
23
4
end

program7:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #3
print(a . count('is' , 19 , 48)) #4
print(a . count('was'))#0

program8:
	Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
s=input('Enter  any string:')
print(s[0]+s[1:].replace(s[0],'*'))
output:
Enter  any string:babble
ba**le

program9:
	a = '15:36:48'
print(a . split(':')) #['15','36','48']
print(a)#15:36:48

program10:
	a = 'Hyd\nis green\tcity'
print(a . split(' ')) #['Hyd\nis', 'green\tcity']
print(a . split())#['Hyd','is', 'green','city']
print(a . split('green'))#['Hyd\nis','\tcity']
print(a . split(''))#error

program11:
	a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))#['Hyd','is', 'green','city']
print(a . split()) #['Hyd','is', 'green','city']
print(a . split(' '))#['Hyd\tis\tgreen\tcity']

program12:
	a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split(' '))#['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

program13:
	a = 'www.gmail.com'
print(a . split('.'))#['www', 'gmail', 'com']

program14:
	Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
s=input('Enter the expression:')
sum=0
for x in s:
	a=eval(x)
	sum=sum+a
print(sum)
output:
	Enter the expression:23+456+7
	486

program15:
	a = ['15' , '36' , '48']
print(':' . join(a)) #15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#25,10,52,15,20
d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))#error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#SankarDayalSarma
g = range(5)
print('-' . join(g))#error

program16:
a = 'Hyd is green city'
print(a . endswith('city')) #true
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))#true

program17:
	Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters
s=input('Enter string:')
length=len(s)
if length>=3 and s.endswith('ing'):
	print(s+'ly')
elif length>=3 and (not s.endwith('ing')):
	print(s+'ing')
else:
	print(S)
output:
	Enterstring: end
	ending
   
program18:
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())# False
print('Hyd$'  . isalpha()) #false
print('9247'  .  isalpha())#false
print('+-$'    .  isalpha())#false
print('A2#'  .   isalpha())#false
print(''  .  isalpha())#false
print(' '  .  isalpha()) #false

program19:
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit()) #false
print('Hyd' . isdigit()) #false
print('+-$' . isdigit()) #false
print('A2#' . isdigit()) #false
print('' . isdigit()) #false
print(' ' . isdigit()) #false
print(9247 . isdigit()) #error

program20:
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper()) # false
print('RAMA  RAO' . isupper()) #true
print('+-$' . isupper()) #false
print('HYD123' . isupper()) #true
print('HYD+-$' . isupper()) #true
print('' . isupper()) #false
print('A2#' . isupper()) #true

program21:
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower()) #false
print('rama  rao' . islower()) #True
print('+-$' . islower()) #false
print('hyd+-$' . islower()) #true
print('abc123' . islower()) #true
print('' . islower()) #false
print('a2#' . islower())# True

program22:
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum()) #false
print('hyd' . isalnum()) #true
print('hYd' . isalnum()) #true
print('9247' . isalnum()) #true
print('' . isalnum()) #false
print('A7g9'  . isalnum()) #true







