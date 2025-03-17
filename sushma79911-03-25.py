#Find outputs
a=['15','36','48']
print(':'.join(a))         #15:36:48
b=('Hyd','is','green','city')
print(' '.join(b))         #Hyd is green city
c={'10','20','15','25','52'}
print(','.join(c))         #10,20,15,25,52
d=['www','gmail','com']
print('.'.join(d))         #www.gmail.com
e=[15,36,48]
print(':'.join(e))         #Error
f=['Sanskar','Dayal','Sarma']
print(''.join(f))          #Error
g=range(5)
print('-'.join(g))         #Error


#endswith() method demo program
a='Hyd is green city'
print(a.endswith('city'))       #True
print(a.endswith('town'))       #False
print(a.endswith('green',3,12)) #True
print(a.endswith('green',3,13)) #False
print(a.endswith(' '.3,13))     #Error


'''
Append 'ing' to input string. 
Append 'ly' to the string if the string already ends with 'ing'. 
Leave the string unchanged if string has less than three characters.
'''
a=input('Enter any string: ')
if len(a)<3:
	print(a)
elif a.endswith('ing'):
	print(a+'ly')
else:
	print(a+'ing')

#Output
Enter any string: Hi
Hi

Enter any string: Interesting
Interestingly

Enter any string: interest
interesting


#isalpha() demo program
print('Hyd'.isalpha())       #True
print('Rama  Rao'.isalpha()) #False due to space
print('Hyd4'.isalpha())      #False due to 4
print('Hyd$'.isalpha())      #False due to $
print('9247'.isalpha())      #False due to numbers    
print('+-$'.isalpha())       #False due to special characters
print('A2#'.isalpha())       #False due to 2 and #
print(''.isalpha())          #False due to empty sring
print(' '.isalpha())         #False due to space


#isdigit() method demo program
print('9247'.isdigit())  #True
print('92a47'.isdigit()) #False due to 'a'
print('92$47'.isdigit()) #False due to '$'
print('Hyd'.isdigit())   #False due to 'Hyd'
print('+-$'.isdigit())   #False due to +,- and $
print('A2#'.isdigit())   #False due to 'A' and'#'
print(''.isdigit())      #False due to empty string
print(' '.isdigit())     #False due to space
print(9247.isdigit())    #Error


#isupper() method demo program
print('HYd'.isupper())        #False due to 'd'
print('HYD'.isupper())        #True becoz there are no lowercase alphabets
print('9247'.isupper())       #False
print('RAMA  RAO'.isupper())  #True
print('+-$'.isupper())        #False
print('HYD123'.isupper())     #True
print('HYD+-$'.isupper())     #True
print(''.isupper())           #False
print('A2#'.isupper())        #True


#islower() method demo program 
print('hyD'.islower())      #False due to 'D'
print('hyd'.islower())      #True becoz there are no uppercase alphabets
print('9247'.islower())     #False
print('rama  rao'.islower())#True
print('+-$'.islower())      #False
print('hyd+-$'.islower())   #True
print('abc123'.islower())   #True
print(''.islower())         #False
print('a2#'.islower())      #True


# isalnum() method demo program 
print('A7$g'.isalnum()) #False due to '$'
print('HYD'.isalnum())  #True becoz there are no special chars
print('+-$'.isalnum())  #False
print('hyd'.isalnum())  #True
print('hYd'.isalnum())  #True
print('9247'.isalnum()) #True
print(''.isalnum())     #False
print('A7g9'.isalnum()) #True
