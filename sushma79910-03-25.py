 a='Hyd is green city. Hyd is hitec city. Hyd is his city'
index=a.find('is')
while (index:=a.find('is',index))!=-1:
	print(index)
	index=index+1
print('End')
#print distinct vowels of the string without using set
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

#Output
Enter any string: RamA raO
Result: AO

Enter any string: Hyd
Hyd



#Modify the below program with walrus operator
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

#Output
4
23
42
46
End


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

#Output
4
23
42
46
Given word is not present in the string


#rfind() method demo program
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

#Output
46
42
23
4
End


#rindex() method demo program
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

#Output
46
42
23
4
Given word is not present in the string


#count() demo program
a='Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a.count('is'))       #3 ('is' at indexes 4,23,42,46)
print(a.count('is',19,48)) #2('is' at indexes 23,42,46)
print(a.count('was'))      #0


#Find outputs
a='Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a.count(' '))   #3
print(a.count('\t'))  #3
print(a.count('\n'))  #3


#Replace every occurence of first character in the string with '*' except first character
a=input('Enter any string: ')
b=a.replace(a[0],'*')
res=a[:1]+b[1:]
print('Result:',res)

#Output
Enter any string: bubble
Result: bu**le


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


#Program to evaluate an expression which contains only + symbols
try:
	a=input('Enter the expression: ')
	b=a.split('+')
	sum=0
	for x in b:
		sum+=int(x)
	print('Result:',sum)
except:
	print('Give a integer sequence')

#Output
Enter the expression: 18+12+56+14
Result: 100
