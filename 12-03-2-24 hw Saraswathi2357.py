#1
list = [10 , 20 , 15 , 18]
print(list)#[10 , 20 , 15 , 18]
list . append(19)
print(list)#[10 , 20 , 15 , 18,19]

#2
#  Find  outputs (Home  work)
list = []
print(list)#[]
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list)#[25, 10.8, 'Hyd', True]

#3
# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)#[0, 10, 20, 30, 40]

#4
#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a)
print(len(a))
print(a[3])
print(a[3][0])
print(a[3][1])
print(a[3][2])

#5
#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)#[10,20,[50,60,70],30,40]
print(len(a))
print(a[2])
print(a[2][0])
print(a[2][1])
print(a[2][2])

