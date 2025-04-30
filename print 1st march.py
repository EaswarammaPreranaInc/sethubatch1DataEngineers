'''
a=[10,20,15,18]
for elements in a:
	print(10,end='\t')
	print(20,end='\t')
	print(15,end='\t')
	print(18,end='\t')

a=[10,20,15,18]
for elements in a:
	print(a)
	print(20,end='\t')
	print(15,end='\t')
	print(18,end='\t')

a=[10,20,15,18]
for elements in a:
	print(elements)

	a='HYD'
	for elements in a:
		print(elements,end='\t')


	a='HYD'
	for elements in a:
		print(elements)

		a=[10,20,15,18]
	for elements in a:
		print(elements,end='\t')

		a=[10,20,15,18]
	for elements in a:
		print(10,end='\t')

		
   
   a='HYD'
	for elements in a:
		print(H,end='\t')#error


		a=range(5)
	for elements in a:
		print(elements)
		a=range(5)
	for elements in a:
		print(elements,end='\t')

		
       a=range(5)
	for elements in a:
		print(a,='\t') # error

		'''
		for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
		print(i ,  j)
	print('Hello')
print('Bye')
'''
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
for  x  in   range():
	print(x)
for x in (25):
	print(x) ## int object is not iterable
'''
for  x  in   123:
        print(x)# int object is not iterable
		'''
		a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')
for  x ,  y  in   a:
	print(x , y) #cannot unpack non-iterable int object
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') #cannot unpack non-iterable int object
	'''
	for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)# 10 next line 30 next line 50
print()# we get gap /space in next line in printing the keys
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20 next line 40 next line 60
print() # we get gap /space in next line in printing the values
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10,20) next line (30,40) next line (50,60)
print() # we get gap /space in next line in printing the items
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # (10,20) next line (30,40) next line (50,60), we dont get any space  in next line in printing the items.
	'''

	try:
	a = int(input('Enter month number (1 - 12): '))
	if  a == 1:
		print('January')
	else:
		if a == 2:
		   print('Febraury')
	        else  a == 3:
		        print('March')
	         if a == 4:
		           print('April')
	                else  a == 5:
		                print('May')
                     if a == 6:
		                    print('June'):
						    else  a == 7:
		                        print('july')
	                         if a == 8:
		                             print('August')
								     else a == 9:
		                                 print('September')
	                                 if a == 10:
		                                     print('October')
										     else  a == 11:
		                                         print('November')
	                                          if a == 12:
		                                               print('December')
													   else:
														   print(('Input should be an integer')
     except:
		print('Input  should  be  an  integer')

		'''

def calculate_electricity_bill(units):
		units = int(input('Enter  units :   '))  #  175
match  units // 100:
	case  0:  #  units  between  0  and  99
				cost = units * 3.00
	case 1:   #  units  between  100  and  199
				cost =  100 * 3.00 + (units - 100) * 3.50
	case  2 | 3:
				cast =100*3.00 +100*3.50+(Units-200)*4.00
	case  4 | 5 | 6:
				cost =100*3.00 +100*3.50+200*4.00+(Units-400)*4.50
    case  _:
				cost =100*3.00 +100*3.50+200*4.00+300*4.50+(Units-700)*5.00
print('Bill  amount  :  ' , cost)
	 