# Modify  following  program  with  else  and  if
try:
    a = int(input('Enter month number (1 - 12): '))
    if a==1:
        print('January')
    else:
        if a==2:
            print('February')
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
    print('Input should be integer')


# Sample Outputs
'''
Enter month number (1 - 12): 6
June

Enter month number (1 - 12): 13
Input should be between 1 and 12

Enter month number (1 - 12): hemanth
Input should be integer
'''


# Find  outputs  (Homework)
#How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  using  for  loop
for x in [10,20,15,18]:
    print(x)

# Sample Output
'''
10
20
15
18
'''

#How  to  print  each  character  of   string  'Hyd'  using  for  loop
for y in 'Hyd':
    print(y)

# Sample output
'''
H
y
d
'''

#How  to  print  each  element  of   range(5) using for loop
for z in range(5):
    print(z)

# Sample output
'''
0
1
2
3
4
'''



# Find  outputs  (Homework)
# for loop with dictionary with keys
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():  # x is each element in dict_keys object
	print(x)
print()  # Empty space is printed

# Sample Output
'''
10
30
50

'''

# for loop with dictionary with values
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():   # x is each element in dict_values object
	print(x)
print()  # Empty space is printed

# Sample output
'''
20
40
60

'''

# for loop with dictionary with items
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():   # x is each element in dict_items object
	print(x)
print()  # Empty space is printed

# Sample output
'''
(10,20)
(30,40)
(50,60)

'''

# for loop with dictionary
for  x in  {10 : 20 , 30 : 40 , 50 :60}:   # x is each element in  default dict_keys object
	print(x)

# Sample output
'''
10
30
50
'''


# Find outputs  (Homework)
a = {10 : 20 , 30 : 40 , 50 : 60}  # x and y are elements in each tuple in the list of dict_items object
for  x , y  in   a . items():
	print(x , y , sep = '...')

# Sample output
'''
10...20
30...40
50...60
'''

# for loop with dictionary
'''for  x ,  y  in   a:
	print(x , y)  # Error due to two variables
'''

''''
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x, y, sep='...')   # Error due to two variables
'''


# Identify  error  (Home  work)
'''
for  x  in   123:  # Error because it is non sequence(int object)
    print(x)
'''


# Find  outputs  (Home  work)
for  x   in   ():
        print(x)  # Nothing is printed due to empty tuple
for  x   in  []:
        print(x)  # Nothing is printed due to empty List
for  x   in   {}:
        print(x)   # Nothing is printed due to empty dictionary
for  x   in   set():
        print(x)   # Nothing is printed due to empty set
for  x   in   '':
        print(x)   # Nothing is printed due to empty string
for  x  in  range(10 , 10):  
	print(x)  # Nothing is printed due to empty range object
'''
for  x  in   range():  # Error because range should contain atleast 1 argument
	print(x)
'''
'''
for  x  in  (25):  # Error because it is non sequence int object
	print(x)
'''


#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
		print(i ,  j)
	print('Hello')
print('Bye')

# Sample Output
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
Bye

'''
