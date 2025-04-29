# -- coding: utf-8 --
'''
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) # 3
print(a . count('\t')) # 3
print(a . count('\n')) # 3
'''
'''
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) # ['15', '36', '48']
print(a) # '15:36:48'
'''

'''
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity' 
print(a . split(' ')) # ['Hyd\nis', 'green\tcity']
print(a . split())    # ['Hyd', 'is', 'green', 'city']
print(a . split('green'))  # ['Hyd\nis ', '\tcity']
#print(a . split(''))
'''
'''
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) #'Hyd' ,	'is' ,	'green' ,	'city'
print(a . split())     #'Hyd' ,	'is' ,	'green' ,	'city'
print(a . split(' ')) #['Hyd\tis\tgreen\tcity']
'''

'''
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) #['www', 'gmail', 'com']
'''

'''
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))                    # 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))                    # Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))                    # 15,10,25,20,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))                    # www.gmail.com
e = ["15 , 36 , 48"]
print(':' . join(e))                    # 15 , 36 , 48
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))                     # SankarDayalSarma
g = str(range(5))
print('-' . join(g))                    # r-a-n-g-e-(-0-,- -5-) 
'''

'''
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))             #True
print(a . endswith('town'))             #False
print(a . endswith('green' , 3 , 12))   #True
print(a . endswith('green' , 3 , 13))   #False
print(a . endswith(' ' , 3 , 13))       #True
'''


'''
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())      #  False due to 4
print('Hyd$'  . isalpha())      # False due to $
print('9247'  .  isalpha())     # False due to 9247
print('+-$'    .  isalpha())    # False due to +-$
print('A2#'  .   isalpha())     # False due to A2#
print(''  .  isalpha())         # False due to empity string  
print(' '  .  isalpha())        # False due to spaces 
'''

'''
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())   #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())  #  False due to '$'
print('Hyd' . isdigit())    # False due to every character is alphabet
print('+-$' . isdigit())    # False due to special  character
print('A2#' . isdigit())    # False due to one  character  of  the  string  is  alphabet  (or) special  character
print('' . isdigit())       # False due to empty string
print(' ' . isdigit())      # False due to wide space 
print(9247 . isdigit())     # True due all character is integer
'''

'''
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())       #  False  due  to  'd'
print('HYD' . isupper())       #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper())      # False due to number
print('RAMA  RAO' . isupper()) # True due to all the character is in upper case
print('+-$' . isupper())       # False due to special character 
print('HYD123' . isupper())    # true due to integer chr but all alphabet is in upper case
print('HYD+-$' . isupper())    # False due to special chr   
print('' . isupper())          # False due to empty string  
print('A2#' . isupper())       # True due to one chr is upr cse alphabet and no lower case alphabet int and special chr

'''

'''
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())         # False  due  to  'D'
print('hyd' . islower())         # True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower())        # False due to int
print('rama  rao' . islower())   # True due to all lower cae alphabet
print('+-$' . islower())         # False due to special chr
print('hyd+-$' . islower())      # True due all lower case alphabet
print('abc123' . islower())      # True due all lower case alphabet 
print('' . islower())            # False due to empity string
print('a2#' . islower())         # True due to atleast one alphabet is lower case 

'''

# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum())   #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())   #  False becoz of special char
print('hyd' . isalnum())   #  True becoz of alphabet
print('hYd' . isalnum())   #  True becoz all are alphabet
print('9247' . isalnum())  #  True becoz all are integer 
print('' . isalnum())      #  False Becoz of empty string
print('A7g9'  . isalnum()) #  True  becoz of alpha and int 

