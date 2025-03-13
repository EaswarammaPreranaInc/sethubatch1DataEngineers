#1  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list)
list . append(19)
print(list)

Output:
[10, 20, 15, 18]
[10, 20, 15, 18, 19]

#2 Find  outputs (Home  work)
list = []
print(list)
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list)

Output:
[]
[25, 10.8, 'Hyd', True]

#3 Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)

Output:
[0, 10, 20, 30, 40]

#4 Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a)
print(len(a))
#print(How  to  print  4th  element  of  list  'a')
#print(How  to  print  'H')
#print(How  to  print  'y')
#print(How  to  print  'd')

Output:
[10, 20, 30, 'Hyd']
4

#5  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)
print(len(a))

Output:
[10, 20, [50, 60, 70], 30, 40]
5
#print(How  to  print  inner  list)
#print(How  to  print  50)
#print(How  to  print  60)
#print(How  to  print  70)

#6  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)
print(len(a))
#print(How  to  print  inner  list)
#print(How  to  print  50)
#print(How  to  print  60)
#print(How  to  print  70)

Output:
[10, 20, [50, 60, 70], 30, 40]
5
