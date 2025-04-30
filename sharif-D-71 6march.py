'''# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') #true
print('day'   in   'Sankar  dayal  sarma') #true
print('Green'   in   'Hyd  is  green  city')#false
print('d  is'   in   'Hyd  is  green  city') #true
print('dis'   in   'Hyd  is  green  city') #false
print('iniv'   in   'Srinivas') #true
print('iniv'   not   in   'Srinivas')#false'''


'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1
'''
'''a = 'Rama Rao'
print(a [ : 7 : 2])#ra a
print(a [ : 7])#rama r
print(a [2 : 4])#ma
print(a [2 : ])	#ma rao
print(a [ : 4 ])#rama
print(a [ : : 2])#rm a
print(a [-6 : -1])#ma ra
print(a [-6 : ])# ma rao
print(a [: -4 : -1])#oar
print(a [-3 : -1])#ra
print(a [-3 : ])#rao
print(a [ : : ])#rama rao
print(a [ : ])#rama rao
print(a [ : : -1])#oar amar
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])#a mr
print(a [2 : 8])#ma rao
print(a [2 : 8 : -1])#
print(a [ : -6 : -1])#oar a
print(a [2 : -3])#ma
print(a [1 : 6 : 2])#aar
print(a [ : -5 : -5])#o
print(a [2 : -5])#m
print(a [2 : -5 : 2])#m
print(a [ : 0 : -1])#oar ama
print(a [-5 : 0 : -2])#aa'''


'''#Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
#Assume  that  each  string  contains  a   minimum  of  two  characters
#Hint:  Use  slice
a=eval(input("enter a 1st string:"))
b=eval(input("enter a 2nd string:"))

c=b[0:2]+a[2:]
d=a[:2]+b[2:]
print("result:",c,d)

output:

enter a 1st string:"java"
enter a 2nd string:"python"
result: pyva jathon'''

'''#Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
a=eval(input("enter a any string:"))
b=a[0:2]+a[-2]+a[-1]
print("results:",b)
output:
enter a any string:"python"
results: pyon'''

'''#Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice
a=input('Enter the string: ')
print('String in forward:')
for i in range(len(a)):
	print(f'Character at index {i}: {a[i]}')
print('String in reverse:')
for i in range(1,len(a)+1):
	print(f'Character at index {-i}: {a[-i]}')
output:
enter a string:vamsi
string in forward:
Character at index 0:v
Character at index 1:a
Character at index 2:m
Character at index 3:s
Character at index 4:i
String in reverse:
Character at index -1:i
Character at index -2:s
Character at index -3:m
Character at index -4:a
Character at index -5:v '''

'''#Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
a=eval(input("enter a string:"))
b=''
c=''
for i in range(0,len(a)):
	if i%2==0:
		b+=a[i]
	else:
		c+=a[i]
print("even number:",b)
print("odd number:",c)

output:
enter a string:'Rama Rao'
even number: Rm a
odd number: aaRo '''

#Let  input  be    A   4   B   3   C   2   $   5
  #                0   1   2   3   4   5   6   7
# What  is  the  difference  between  a[i]   and  a[i + 1] ?  ---> a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string



try:
	a=input('Enter any string with alternate character and digit: ')
	c=''
	for i in range(0,len(a),2):
		c+=a[i]*int(a[i+1])
	print('Result:',c)
except ValueError:
	print('Please enter alternate char and digit')

'''output:
Enter any string with alternate character and digit: $5P2K3Z4
Result: $$$$$PPKKKZZZZ
Enter any string with alternate character and digit: hyd
Please enter alternate char and digit '''
