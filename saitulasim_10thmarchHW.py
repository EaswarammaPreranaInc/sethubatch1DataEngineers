# 1: print distinct vowels of the string without using set
a=input('Enter any string: ')
if(len(a)<4):
	print(a)
else:
	a=a.upper()
	b=''
	v='AEIOU'
	for i in range(len(a)):
		if (a[i] in v) and (a[i] not in b):
			b+=a[i]
	print('Result:',b)




# 2: Modify the below program with walrus operator
'''
a='Hyd is green city. Hyd is hitec city. Hyd is his city'
index=a.find('is')
while index!=-1:
	print(index)
	index=a.find('is',index+1)
print('End')
'''
a='Hyd is green city. Hyd is hitec city. Hyd is his city'   
index=a.find('is')													
while (index:=a.find('is',index))!=-1:
	print(index)
	index=index+1
print('End')

''' Output
4
23
42
46
End '''


#index() method demo program
'''
Modify the below program with index() method
a='Hyd is green city. Hyd is hitec city. Hyd is his city'
index=a.find('is')
while index!=-1:
	print(index)
	index=a.find('is',index+1)
print('End')
'''
try:
	a='Hyd is green city. Hyd is hitec city. Hyd is his city'
	index=a.index('is')
	while index!=-1:
		print(index)
		index=a.index('is',index+1)
	print('End')
except:
	print('Given word is not present in the string')

''' Output
4
23
42
46
Given word is not present in the string '''


# 3: rfind() method demo program
'''
Modify the following program with rfind() method
a='Hyd is green city. Hyd is hitec city. Hyd is his city'
index=a.find('is')
while index!=-1:
	print(index)
	index=a.find('is',index+1)
print('End')
'''
a='Hyd is green city. Hyd is hitec city. Hyd is his city'
index=a.rfind('is')
while index!=-1:
	print(index)
	index=a.rfind('is',0,index)
print('End')

''' Output
46
42
23
4
End '''


# 4rindex() method demo program
'''
Modify the following program with rfind() method
a='Hyd is green city. Hyd is hitec city. Hyd is his city'
index=a.find('is')
while index!=-1:
	print(index)
	index=a.find('is',index+1)
print('End')
'''
try:
	a='Hyd is green city. Hyd is hitec city. Hyd is his city'
	index=a.rindex('is')
	while index!=-1:
		print(index)
		index=a.rindex('is',0,index-1)
	print('End')
except:
	print('Given word is not present in the string')

''' Output
46
42
23
4
Given word is not present in the string '''


# 5: count() demo program
a='Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a.count('is'))       #4('is' at indexes 4,23,42,46)
print(a.count('is',19,48)) #3('is' at indexes 23,42,46)
print(a.count('was'))      #0


# 6: Find outputs
a='Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a.count(' '))   #3
print(a.count('\t'))  #3
print(a.count('\n'))  #3


# 7: Replace every occurence of first character in the string with '*' except first character
a=input('Enter any string: ')
b=a.replace(a[0],'*')
res=a[:1]+b[1:]
print('Result:',res)

''' Output
Enter any string: bubble
Result: bu**le '''

# 8: Program to evaluate an expression which contains only + symbols
try:
	a=input('Enter the expression: ')
	b=a.split('+')
	sum=0
	for x in b:
		sum+=int(x)
	print('Result:',sum)
except:
	print('Give a integer sequence')

''' Output
Enter the expression: 18+12+56+14
Result: 100 '''



#Find outputs
a='15:36:48'          
print(a.split(':')) #['15','36','48']
print(a)            #15:36:48


#Find outputs
a='Hyd\nisgreen\tcity'
print(a.split(' '))    #['Hyd\nisgreen\tcity']
print(a.split())       #['Hyd', 'isgreen', 'city']
print(a.split('green'))#['Hyd\nis', '\tcity']
#print(a.split(''))     #Error


#Find outputs
a='Hydis	green	city' #There is tab between the words
print(a.split('\t'))    #['Hydis', 'green', 'city']
print(a.split())        #['Hydis', 'green', 'city']
print(a.split(' ')) #['Hydis\tgreen\tcity']


#Find outputs
a='Hyd   is   green   city'
print(a.split())     #['Hyd','is','green','city']
print(a.split(' '))  #['Hyd',' ',' ','green',' ',' ','city']


#Find outputs
a='www.gmail.com'
print(a.split('.')) #['www','gmail','com']




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
#print(a.endswith(' '.3,13))     #Error


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

''' Output
Enter any string: Hi
Hi
Enter any string: Interesting
Interestingly
Enter any string: interest
interesting '''


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
# print(9247.isdigit())    #Error


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
