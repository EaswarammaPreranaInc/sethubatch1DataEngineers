# Modify  following  program  with  else  and  if

try:
	a = int(input('Enter month number (1 - 12): '))
	if  a == 1:
		print('January')
	elif  a == 2:
		print('Febraury')
	elif  a == 3:
		print('March')
	elif  a == 4:
		print('April')
	elif  a == 5:
		print('May')
	elif  a == 6:
		print('June')
	elif  a == 7:
		print('july')
	elif  a == 8:
		print('August')
	elif  a == 9:
		print('September')
	elif  a == 10:
		print('October')
	elif  a == 11:
		print('November')
	elif  a == 12:
		print('December')
	else:
		print('Input  should  be  between  1  and   12')
except:
		print('Input  should  be  an  integer')

try:
	a = int(input('Enter month number (1 - 12): '))
	if  a == 1:
		print('January')
	else:
			if a == 2:
				print('Febraury')
			else: 
					if a == 3:
						print('March')
					else:
						if a == 4:
							print('April')
						else:
							if  a == 5:
								print('May')
							else:
								if  a == 6:
									print('June')
								else:
									if  a == 7:
										print('july')
									else:
										if  a == 8:
											print('August')
										else:
											if  a == 9:
												print('September')
											else:
												if  a == 10:
													print('October')
												else:
													if  a == 11:
														print('November')
													else:
														if  a == 12:
															print('December')
														else:
															print('Input  should  be  between  1  and   12')
except:
		print('Input  should  be  an  integer') 
'''
# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  using  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  using  for  loop
print()
How  to  print  each  element  of   range(5) using  for  loop '''

x=eval(input("enter a sequence: "))
for i in x:
	print(i)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)#10 next line30next line50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)#20 next line 40 next line 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)# (10 : 20) , (30 : 40 ), (50 : 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)#10,30,50  

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')# (10...20) next line (30..40) next line (50:60)
for  x ,  y  in   a:
	print(x , y)# error can only return values of keys
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x,y,sep='...') # error can only return values of keys

# Identify  error  (Home  work)
for  x  in   123: # can't have integer 
        print(x) # cant iterate int in loops '''

# Find  outputs  (Home  work)
for  x   in   ():
        print(x)# nothing
for  x   in  []:
        print(x)# nothing
for  x   in   {}:# empty dict
        print(x)# nothing
for  x   in   set():
        print(x)# nothing
for  x   in   '':
        print(x)# nothing
for  x  in  range(10 , 10): # nothing to iterate
	print(x)
#for  x  in   range(): range needs atleast one argument
	#print(x) 
#for  x  in   (25): # error int not iterable
	#print(x)

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
		print(i ,  j) 
	print('Hello') 
print('Bye')#bye
'''
1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye '''
