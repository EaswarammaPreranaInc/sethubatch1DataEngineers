program1:
list = [10 , 20 , 15 , 18]
print(list)#[10,20,15,18]
list . append(19)
print(list) #[10,20,15,18,19]

program2:
list = []
print(list)#[]
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) #[25,10.8.'Hyd',True]

program3:
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)

output:
[0,10,20,30,40]

program4:
a = [10 , 20 , 30]
a . append('Hyd')
print(a)#[10,20,30,'Hyd']
print(len(a))#4
print(a[3])# Hyd  (How  to  print  4th  element  of  list  'a')
print(a[3][0])#'H'
print(a[3][1])#'y'
print (a[3][2])#'d'

program5:
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)#[10,20,[50,50,70],30,40,]
print(len(a))#5
print(a[2])# [50,60,70] (How  to  print  inner  list)
print(a[2][0])# 50
print(a[2][1])#60
print(a[2][2])#70

