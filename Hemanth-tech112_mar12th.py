#  append()  method  demo  program (Home  work)
list = [10, 20, 15, 18]
print(list)  # [10,20,15,18]
list . append(19)  # Appends element 19 to list
print(list)  # [10,20,15,18,19]

'''
[10, 20, 15, 18]
[10, 20, 15, 18, 19]
'''


#  Find  outputs (Homework)
list = []
print(list) # [] or empty list
list . append(25)  # Append element 25 to list
list . append(10.8)  # Append element 10.8 to list
list . append('Hyd')  # Append element 'Hyd' to list
list . append(True)  # Append element True to list
print(list)  # [25,10.8,'Hyd',True]

'''
[]
[25, 10.8, 'Hyd', True]
'''


# Find  outputs  (Homework)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)  # Appends element 0 at first iteration and 10 at second and 20 at third and 30 at fourth and 40 at fifth iteration
print(list)  # [0,10,20,30,40]

'''
[0, 10, 20, 30, 40]
'''



#  Find  outputs  (Home  work)
a = [10, 20, 30]
a . append('Hyd')  # Append element 'Hyd' to list a
print(a)  # [10,20,30,'Hyd']
print(len(a))  # 4
print(a[3])  # How  to  print  4th  element  of  list  'a'---> 'Hyd'
print(a[3][0])  # How  to  print  'H'
print(a[3][1])  # How  to  print  'y'
print(a[3][2])  # How to print 'd'

'''
[10, 20, 30, 'Hyd']
4
'Hyd'
H
y
d

'''


#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)  # Inserts b at index 2 of the list a
print(a)  # [10,20,[50,60,70],30,40]
print(len(a))  # 5
print(a[2])  # How  to  print  inner  list ---> [50,60,70]
print(a[2][0])  # How  to  print  50 ---> [50,60,70][0] ---> 50
print(a[2][1])  # How  to  print  60 ---> [50,60,70][1] ---> 60
print(a[2][2])  # How to print 70 ---> [50,60,70][2] ---> 70

'''
[10, 20, [50, 60, 70], 30, 40]
5
[50, 60, 70]
50
60
70

'''


