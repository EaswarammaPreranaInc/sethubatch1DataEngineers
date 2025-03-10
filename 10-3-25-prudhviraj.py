#Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set
a=input("Enter the string: ")
b=['a','e','i','o','u']
c=''
for x in a:
	if x in b:
		#print(F"Vowels are:{c}")
		c+=x
print(c.upper())
#print(F"Vowels are:{c}")


"""
Output:
Enter the string: RaMA  rAo
AO
"""

#Modify  following  program  with  walrus  operator
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
#index = a . find('is')
index=-1
while  ((index:=a.find('is',index+1))!=-1):
	print(index)
print('End')
"""
Output:
4
23
42
46
End
"""
#Modify  the  following  program  with  index()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a .index('is')
while  index != -1:
	print(index)
	index = a . index('is' , index + 1)
print('End')
"""
Output:
4
23
42
46
End
"""
#Modify  following  program  with  rfind()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a .rfind('is')
while  index != -1:
	print(index)
	index = a .rfind('is' ,0,index)
print('End')
"""
Output:
46
42
23
4
End
"""
#Modify  following  program  with  rindex()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a .rindex('is')
while  index != -1:
	print(index)
	index = a .rindex('is',0,index)
print('End')

"""
Output:
46
42
23
4
End
"""
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))    #3
print(a . count('\t'))   #3
print(a . count('\n'))   #3
#Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
a=input("Enter the string: ")
b=a[1:]
print(a[0]+b.replace(a[0],'*'))
"""
Output:
Enter the string: babble
ba**le
"""


#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))  #['15','36','48']
print(a)               #[15:36:48]

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))    #['Hyd','is','green','city']
print(a . split())       #[]
print(a . split('green'))#['Hyd\nis','\tcity']
print(a . split(''))     #Error due to no argument


# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) #['Hyd','is','green','city']
print(a . split())     #['Hyd', 'is', 'green', 'city']
print(a . split(' '))  #['Hyd\tnis\tgreen\tcity']


# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())             #['Hyd', 'is', 'green', 'city']
print(a . split(' '))          #['Hyd', ' ',' ','is', ' ','', 'green', ' ','', 'city']

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))  #['www','gmail','.com']
#Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
a=input("Enter the expression: ").split('+')
b=0
for i in a:
	b+=int(i)
print(b)

"""
Output:
Enter the expression: 23+456+7
Sum:  486
"""

##  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))                    #[15:36:48]
b = ('Hyd' , 'is' , 'green' , 'city') 
print(' ' . join(b))                    #[Hyd is green city]
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))                    #[10,20,15,25,52]
d = ['www' , 'gmail', 'com']
print('.' . join(d))                    #[www.gmail.com]
#e = [15 , 36 , 48]
#print(':' . join(e))                    #Error due to e is int type
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))                     #[SankarDayalSarma]
#g = range(5)
#print('-' . join(g))                    #Error due to int type

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))            # True
print(a . endswith('town'))            # False
print(a . endswith('green' , 3 , 12))  # True
print(a . endswith('green' , 3 , 13))  # False
print(a . endswith(' ' , 3 , 13))      # True
#Write  a  program  to  append  'ing'  to  input  string
a=input("Enter The string: ")
if (len(a)<3):
	print(a)
else:
	if (a.endswith('ing')):
		print(a + 'ly')
	else:
		print(a)
"""
Output:
Enter The string: interest
interesting

Enter The string: interesting
interestingly

Enter The string: hyd
hyd
"""

#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())       #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())      #  False
print('Hyd$'  . isalpha())      #  False
print('9247'  .  isalpha())     #  False
print('+-$'    .  isalpha())    #  False
print('A2#'  .   isalpha())     #  False
print(''  .  isalpha())         #  False
print(' '  .  isalpha())        #  False

# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())   #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit())    #  False
print('+-$' . isdigit())    #  False
print('A2#' . isdigit())    #  False
print('' . isdigit())       #  False
print(' ' . isdigit())      #  False
print(9247 . isdigit())     #  Error

# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper()) # False
print('RAMA  RAO' . isupper()) #True
print('+-$' . isupper())      #False
print('HYD123' . isupper())   #True
print('HYD+-$' . isupper())   #True
print('' . isupper())         #False
print('A2#' . isupper())      #True


# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower()) #  False becoz  there  are  no  alphabets
print('rama  rao' . islower())#True
print('+-$' . islower())     # False bcoz special charecters
print('hyd+-$' . islower())  # True
print('abc123' . islower())  # True
print('' . islower())        # False
print('a2#' . islower())     # True


# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum()) #  False  due  to   '$'
print('hyd' . isalnum()) #  True  becoz  there are  no  special  chars
print('hYd' . isalnum()) #  True  becoz  there are  no  special  chars
print('9247' . isalnum())#  True  due  to 9247
print('' . isalnum())    #  False
print('A7g9'  . isalnum())# True  becoz  there are  no  special  chars
