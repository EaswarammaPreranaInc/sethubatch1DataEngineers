#Modify Prgm with else and if
'''
try:
	a=int(input('Enter month number(1-12): '))
	if a==1:
		print('January')
	else:
		if a==2:
			print('Febraury')
		else:
			if a==3:
				print('March')
			else:
				if a==4:
					print('April')
				else:
					if a==5:
						print('May')
					else:
						if a==6:
							print('June')
						else:
							if a==7:
								print('July')
							else:
								if a==8:
									print('August')
								else:
									if a==9:
										print('September')
									else:
										if a==10:
											print('October')
										else:
											if a==11:
												print('November')
											else:
												if a==12:
													print('December')
												else:
													print('Input should be between 1 and 12')
except:
	print('Input should be an integer')
'''

#Write a prgm to determine bill amount and input is units
'''
units=int(input('Enter units: '))
match units//100:
	case 0:
		cost=units*3.00
	case 1:
		cost=100*3.00+(units-100)*3.50
	case 2 |3:
		cost=100*3.00+100*3.50+(units-200)*4.00
	case 4 | 5| 6:
		cost=100*3.00+100*3.50+200*4.00+(units-400)*4.50
	case _:
		cost=100*3.0+100*3.50+200*4.0+300*4.50+(units-700)*5.0
print('Bill amount:', cost)
'''

#Find outputs
#how to print each element of list[10,20,15,18]
'''
x=[10,20,15,18]
for i in x:
	print(i)
'''

#How to print each character of string 'Hyd' using for loop
'''
a='hyd'
for i in a:
	 print(i)
'''

#How to print each element of range(5)
'''
for i in range(5):
	print(i)
'''

#Find  outputs  (Home  work)
'''
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
'''

#find output
'''
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
'''

#find output
'''
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
'''

#find output
'''
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
'''

#Find outputs  (Home  work)
'''
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
#for  x,y  in   a:#unpack non-iterable int object
	#print(x , y)
#for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:#unpack non-iterable int object
	#print(x , y , sep = '...')
'''

# Identify  error  (Home  work)
'''
for  x  in   123: # error cant be iterable
        print(x)
'''

# Find  outputs  (Home  work)
'''
for  x   in   ():# nthg is printed as it iterates 0 times
        print(x)
for  x   in  []:# nthg is printed as it iterates 0 times
        print(x)
for  x   in   {}:# nthg is printed as it iterates 0 times
        print(x)
for  x   in   set():# nthg is printed as it iterates 0 times
        print(x)
for  x   in   '':# nthg is printed as it iterates 0 times
        print(x)
for  x  in  range(10 , 10):# nthg is printed as it iterates 0 times
	print(x)
#for  x  in   range():# range should be with alteast 1 argument not zero
	#print(x)
#for  x  in   (25):# for loop iterates only sequence not non sequence elements
	#print(x)
'''

#  Nested  Loop  demo  program
'''
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
		print(i ,  j)
	print('Hello')
print('Bye')
'''
