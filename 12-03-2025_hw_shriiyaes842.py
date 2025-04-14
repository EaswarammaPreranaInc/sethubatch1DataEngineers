# 1. append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . append(19) 
print(list) # **[10 , 20 , 15 , 18,19]


# 2. Find  outputs (Home  work)
list = []
print(list)                      #[]
list . append(25)   #[25]
list . append(10.8) #[25,10.8]
list . append('Hyd')#[25,10.8,'Hyd']
list . append(True)#[25,10.8,'Hyd',True]
print(list)			               ##[25,10.8,'Hyd',True]


# 3. Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)         # [0,10,20,30,40]


# 4. Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')  
print(a)       #[10 , 20 , 30,'Hyd']
print(len(a))  # 4
print("How  to  print  4th  element  of  list  'a'",a[3])
print("How  to  print  'H'",a[3][0])
print("How  to  print  'y'",a[3][1])
print("How  to  print  'd'",a[3][2])


# 5. Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)		# [10 , 20 ,[50 , 60 , 70], 30 , 40]
print(len(a))	# 5
print("How  to  print  inner  list",a[2])
print("How  to  print  50",a[2][0])
print("How  to  print  60:",a[2][1])
print("How  to  print  70",a[2][2]
)