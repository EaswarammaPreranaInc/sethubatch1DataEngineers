program1:
Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') #True
print('day'   in   'Sankar  dayal  sarma') #true
print('Green'   in   'Hyd  is  green  city')#False
print('d  is'   in   'Hyd  is  green  city') #True
print('dis'   in   'Hyd  is  green  city') #False
print('iniv'   in   'Srinivas') #True
print('iniv'   not   in   'Srinivas')#False

program2:
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1

a = 'Rama Rao'
print(a [ : 7 : 2])#Rm a
print(a [ : 7])# Rama Ra
print(a [2 : 4])#ma
print(a [2 : ])# ma Rao
print(a [ : 4 ])#rama
print(a [ : : 2])#Rm a
print(a [-6 : -1])# ma Ra
print(a [-6 : ])# ma Rao
print(a [: -4 : -1])#oaR
print(a [-3 : -1])#Ra
print(a [-3 : ])#Rao
print(a [ : : ])Rama Rao
print(a [ : ])#rama Rao
print(a [ : : -1])#oaR amaR
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])#ma Rao
print(a [2 : 8])#oaR a
print(a [2 : 8 : -1]#)ma
print(a [ : -6 : -1])#oaR a
print(a [2 : -3])#ma
print(a [1 : 6 : 2])aaR
print(a [ : -5 : -5])#o
print(a [2 : -5])#m
print(a [2 : -5 : 2])#m
print(a [ : 0 : -1])#oaR ama 
print(a [-5 : 0 : -2])#aa

program3:
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters
a=input('Enter the first string:')
b=input('Enter the second string:')
c=a[0:2]
d=a[2:]
e=b[0:2]
f=b[2:]
print('Result:',c+f)
output:
Enter the first string:java
Enter the second string:python
Result: jathon

program4:
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters
a=input('Enter the string:')
b=''
if len(a)>=4: b=a[:2]+a[-2:]
print('Result:',b)
output:
Enter the string:python
Result: pyon

program5:
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice
a=print('String in forward')
for i in range(len(a)):
	print(f' character at index {i} {a[i]}')
	print('string in reverse')
for i in range(-1,-len(a)-1,-1):
	print(f'character at index{i}={a[i]}')
	output:
Enter the string:vamsi
String in forward
 character at index 0 v
string in reverse
 character at index 1 a
string in reverse
 character at index 2 m
string in reverse
 character at index 3 s
string in reverse
 character at index 4 i
string in reverse
character at index-1=i
character at index-2=s
character at index-3=m
character at index-4=a
character at index-5=v

program6:
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
a=input('Enter the string:')
length=len(a)
even=''
odd=''
for i in range (length):
	if i %2==0 :
	    even=even+a[i]
	else:
		odd=odd=a[i]
		print(f'character at even indexs:{even}')
		print(f'character at odd indexs:{odd}')
output:
Enter the string:rama rao
character at even indexs:r
character at odd indexs:a
character at even indexs:rm
character at odd indexs:a
character at even indexs:rm
character at odd indexs:r
character at even indexs:rm a
character at odd indexs:o


