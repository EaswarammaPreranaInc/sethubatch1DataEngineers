try:
    a = int(input('Enter month number (1 - 12): '))
    if a == 1:
        print('January')
    elif a == 2:
        print('February')
    elif a == 3:
        print('March')
    elif a == 4:
        print('April')
    elif a == 5:
        print('May')
    elif a == 6:
        print('June')
    elif a == 7:
        print('July')
    elif a == 8:
        print('August')
    elif a == 9:
        print('September')
    elif a == 10:
        print('October')
    elif a == 11:
        print('November')
    elif a == 12:
        print('December')
    else:
        print('Input should be between 1 and 12')
except ValueError:
    print('Input should be an integer')


units = int(input('Enter  units :   '))
match  int(units/100):
	case 0:
		cost =units*3
	case 1:
	    cost =100*3+(units-100)*3.5
	case 2 | 3:
		cost =100*3+100*3.5+(units-200)*4
	case  4 | 5 | 6:
		cost =100*3+100*3.5+100*4+(units-300)*4.5
	case _:
		cost=100*3+100*3.5+100*4+100*4.5+(units-400)*5
print('Bill  amount  :  ',cost)



for x in [10,20,15,18]:
    print(x)
for x in 'Hyd':
    print(x)
for x in range(5):
    print(x)


# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)       #prints keys
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)      #prints values
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)      #prints key-value pairs
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)     #prints keys


a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')  #key values sep by ...
# for  x ,  y  in   a:
# 	print(x , y)        #error
# for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
# 	print(x , y , sep = '...') #error

#for  x  in   123:
   # print(x)  # Error non sequence cannot be iterable


# Find  outputs  (Home  work)
for  x   in   ():
        print(x)  #empty tupple
for  x   in  []:
        print(x)  #empty list
for  x   in   {}:
        print(x)  #empty dict
for  x   in   set():
        print(x)  #empty set
for  x   in   '':
        print(x)   #empty str
for  x  in  range(10 , 10):
	print(x)       #empty range
# for  x  in   range():
# 	print(x)      #Error 
# for  x  in   (25):
# 	print(x)    #Error 


#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
		print(i ,  j)
	print('Hello')
print('Bye')

