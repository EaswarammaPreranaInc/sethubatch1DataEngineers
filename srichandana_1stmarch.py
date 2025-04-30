#Modify  following  program  with  else  and  if
try:
    a = int(input('Enter month number (1 - 12): '))
    
    if a == 1:
        print('January')
    else: 
        if a == 2:
            print('February')
        else:
            if a == 3:
                print('March')
            else:
                if a == 4:
                    print('April')
                else:
                    if a == 5:
                        print('May')
                    else:
                        if a == 6:
                            print('June')
                        else:
                            if a == 7:
                                print('July')
                            else:
                                if a == 8:
                                    print("August")
                                else:
                                    if a == 9:
                                        print("September")
                                    else:
                                        if a == 10:
                                            print("October")
                                        else:
                                            if a == 11:
                                                print("November")
                                            else:
                                                if a == 12:
                                                    print("December")
                                                else:
                                                    print('Input should be between 1 and 12')

except ValueError:
    print('Input should be an integer')
##How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  using  for  loop
for x in [1,3,4]:
    print(x)
#How  to  print  each  character  of   string  'Hyd'  using  for  loop
for y in 'hyd':
     print(y)
#How  to  print  each  element  of   range(5) using  for  loop
for k in range(5):
     print(k)
# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
for  x   in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , end = '...')
# Identify  error  (Home  work)
'''for  x  in   123:
        print(x)'''
#int cannot be iterated as it is not a sequence
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
'''for  x  in   range():
	print(x)
for  x  in   (25):
	print(x)'''
#nested for loop
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
		print(i ,  j)
	print('Hello')
print('Bye')
