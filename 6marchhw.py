"""
# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') 
print('day'   in   'Sankar  dayal  sarma') 
print('Green'   in   'Hyd  is  green  city')
print('d  is'   in   'Hyd  is  green  city') 
print('dis'   in   'Hyd  is  green  city') 
print('iniv'   in   'Srinivas') 
print('iniv'   not   in   'Srinivas')


'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])#Rm a
print(a [ : 7])#Rama Rao
print(a [2 : 4])#ma
print(a [2 : ])#ma Rao
print(a [ : 4 ])#Rama
print(a [ : : 2])#Rm Ro
print(a [-6 : -1])#ma Ra
print(a [-6 : ])
print(a [: -4 : -1])#oaR
print(a [-3 : -1])#Ra
print(a [-3 : ])#Rao
print(a [ : : ])#Rama rao
print(a [ : ])#Rama rao
print(a [ : : -1])#oaR amaR
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])#a mR
print(a [2 : 8])#ma Rao
print(a [2 : 8 : -1])#nothing
print(a [ : -6 : -1])#oaR a
print(a [2 : -3])#ma 
print(a [1 : 6 : 2])#aaR
print(a [ : -5 : -5])#a
print(a [2 : -5])#m
print(a [2 : -5 : 2])#m
print(a [ : 0 : -1])#oaR ama
print(a [-5 : 0 : -2])#aa

#swap 1st two string and concatenate
a='java'
b='python'
c=a[0:2]+b[2:]
d=b[0:2]+a[2:]
print(d,c)

#print string characters and reverse also
a='vamsi'
for i in range(len(a)):
	print(f'character at index {i}:',a[i])
print('\n')
print('\n')

for i in range(-1,-len(a)-1,-1):
	print(f'character at index {i}:',a[i])


# print 1st 2  and last 2 character and add them
a=input('enter a string:')
if len(a)<4:
	print()
else:
	b=a[:2]+a[-2::1]
	print(b)


#print  characters  at  even  and  odd  indexes  without  slice

a=input('enter a string:')
for i in range(len(a)):
	if False:
		pass
	else:
		if i%2==0:
			print(a[i],end='')
print('\n')
for i in range(len(a)):
	if False:
		pass
	else:
		if i%2!=0:
			print(a[i],end='')
print('\n')

#or below program
a=(input("Enter the input String: "))
x=""
y=""
for i in range(len(a)):
	if i%2==0:
		x=x+a[i]
	else:
		y=y+a[i]
print("The even is",x)
print("The odd is",y)

#print charaters that multiply with next value
a=input("Enter the Input: ")
result=""
if len(a)%2!=0:
	print("The length of string must be even")
else:
	for i in range(0,len(a),2):
		c=a[i]*int(a[i+1])
		result+=c
	print(result)

"""




		