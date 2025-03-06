#program1:
#program to month with  else  and  if
try:
	m=int(input("enter month number from (1-12) : "))
	if m==1:
		print("January")
	else:
		if m==2:
			print("February")
		else:
			if m==3:
				print("March")
			else:
				if m==4:
					print("April")
				else:
					if m==5:
						print("May")
					else:
						if m==6:
							print("June")
						else:
							if m==7:
								print("July")
							else:
								if m==8:
									print("Auguest")
								else:
									if m==9:
										print("September")
									else:
										if m==10:
											print("octobure")
										else:
											if m==11:
												print("november")
											else:
												if m==12:
													print("December")
												else:
													print("Invalid month number")
except:
	print("Input should be integer number")

#program2:
#How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  using  for  loop
for x in [10,20,15,18]:
  print(x)
print()

#program3:
#How  to  print  each  character  of   string  'Hyd'  using  for  loop
for x in 'Hyd':
  print(x)
print()

#program4:
#How  to  print  each  element  of   range(5) using  for  loop
for i in range(5):
  print(i)
print()

#program5:
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)                                                             #10 <next line> 30 <next line> 50
print()                                                                #empty
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)                                                             #20 <next line> 40 <next line> 60
print()                                                                #empty
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)                                                             #(10,20) <next line> (30,40) <next line> (50,60)
print()                                                                #empty
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)                                                             #10 <next line> 30 <next line> 50

#program6:
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')         #10...20 <next line> 30...40 <next line> 50...60
for  x ,  y  in   a:                 #error
	print(x , y)
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:  #error
	print(x , y , sep = '...')

#program7:
for  x   in   ():
        print(x)
for  x   in  []:
        print(x)
for  x   in   {}:
        print(x)
for  x   in   set():
        print(x)
for  x   in   '':
        print(x)
for  x  in  range(10 , 10):
	print(x)

output:nothing to print because empty sequences

#program8:
Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
		print(i ,  j)
	print('Hello')
print('Bye')

outputs:1 1
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
        Bye
