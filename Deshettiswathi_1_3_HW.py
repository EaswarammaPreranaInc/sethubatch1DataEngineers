# Find  outputs  (Home  work)
#How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  using  for  loop
l=[10 , 20 , 15 , 18]
for x in l:
	print(x)
#How  to  print  each  character  of   string  'Hyd'  using  for  loop
a='Hyd'
for x in a:
	print(x)
#How  to  print  each  element  of   range(5) using  for  loop
r=range(5)
for x in r:
	print(x)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)   #print keys 10 30 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)    #print values  20 40 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)  #print (key,value)  
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)   #print keys 10 30 50


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():      
	print(x , y , sep = '...')       #print key and values with separator ...  
#for  x ,  y  in   a:
#	print(x , y)                    #error because a only prints value of x i.e. keys, y should not be defined. y values cannot unpack
#for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
#	print(x , y , sep = '...')       #error


# Identify  error  (Home  work)
for  x  in   123:   #123 is not a sequence
        print(x)

# Find  outputs  (Home  work)
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
#for  x  in   range():   #error atleast one argument is needed
#	print(x)
#for  x  in   (25):
#	print(x)          #error


#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
		print(i ,  j)             
	print('Hello')
print('Bye')

OP-
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
