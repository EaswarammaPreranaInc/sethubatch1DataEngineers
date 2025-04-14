'''#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list)# [10,20,15,18]
list . append(19)
print(list) #[10,20,15,18,19]

#  Find  outputs (Home  work)
list = []
print(list)#[]
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list)#[25,10.8,;HYd',True]

# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)#[0,10,20,30,40]

#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a)#[10,20,30,'Hyd']
print(len(a))#4
#print(How  to  print  4th  element  of  list  'a')#print(a[3])
#print(How  to  print  'H')print(a[3][0])
#print(How  to  print  'y')print(a[3][1])
#print(How  to  print  'd')print(a[3][2])
'''

#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)#[10,20,[50,60,70],30,40]
print(len(a))
#print(How  to  print  inner  list) #print(a[2])
#print(How  to  print  50)#print(a[2][0])
#print(How  to  print  60)#print(a[2][0])
#print(How  to  print  70)#print(a[2][0])
