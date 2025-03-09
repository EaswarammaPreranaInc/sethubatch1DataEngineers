#Merge two strings to form a new string
a=input('Enter first string: ')
b=input('Enter second string: ')
res=''
s=a if len(a)>len(b) else b
for i in range(min(len(a),len(b))):
	res+=a[i]+b[i]
res+=s[min(len(a),len(b))]
print('Result:',res)

#Output
Enter first string: HYD
Enter second string: VAMSI
Result: HVYADMSI



#Remove duplicate characters of the string without using set
a=input('Enter any string: ')
res=''
for i in range(len(a)):
	if a[i] not in res:
		res+=a[i]
print('String without duplicates:',res)

#Output
Enter any string: SEASONS
String without duplicates: SEAON



#len() functon demo program
print(len('Hyd'))      #3
print(len('Rama rao')) #8
print(len('9247'))     #4
print(len('+-$'))      #3
print(len(''))         #0
print(len(' '))        #1
print(len('A2#'))      #3
print(len(3456))       #Error
print('Sec'.len())     #Error



#chr() function demo program
print(chr(65))  #A becoz 65 unicode value of 'A'
print(chr(90))  #Z becoz 90 unicode value of 'Z'
print(chr(97))  #a becoz 97 unicode value of 'a'
print(chr(122)) #z becoz 122 unicode value of 'z'
print(chr(48))  #0 becoz 48 unicode value of '0'
print(chr(57))  #9 becoz 57 unicode value of '9'
print(chr(36))  #$ becoz 36 unicode value of '$'
print(chr(32))  #  becoz 32 unicode value of ' '



#ord() function demo program
print(ord('A')) #Unicode value of 'A' i.e. 65
print(ord('Z')) #Unicode value of 'Z' i.e. 90
print(ord('a')) #Unicode value of 'a' i.e. 97
print(ord('z')) #Unicode value of 'z' i.e. 122
print(ord('0')) #Unicode value of '0' i.e. 48
print(ord('9')) #Unicode value of '9' i.e. 57
print(ord('$')) #Unicode value of '$' i.e. 36
print(ord(' ')) #Unicode value of ' ' i.e. 32



#Print the result of a string with alternate character and digit
#Ai(digit 'i' is the next ith character from character 'A')
try:
	a=input('Enter any string with alternate character and string: ')
	res=''
	for i in range(0,len(a),2):
		x=ord(a[i])
		res+=a[i]+chr(x+int(a[i+1]))
	print('Result:',res)
except:
	print('Enter any string with alternate character and string')

#Output
Enter any string with alternate character and string: K4Z3$2h5
Result: KOZ]$&hm

Enter any string with alternate character and string: 1A2a3$
Enter any string with alternate character and string

Enter any string with alternate character and string: hyd
Enter any string with alternate character and string
