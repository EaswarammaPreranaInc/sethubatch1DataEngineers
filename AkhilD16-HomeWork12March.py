#1.  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list)			# [10,20,15,18]
list . append(19)	# 19 is appended into the list at the end i.e.[10,20,15,18,19]
print(list)			#[10,20,15,18,19]

#2.Find  outputs (Home  work)
list = []
print(list)				#[]
list . append(25)		#25 is appended to the list
list . append(10.8)		#10.8 is appended to the list at the end
list . append('Hyd')	#'HYD' is appended to the list at the end
list . append(True)		#TRUE is appended to the list at the end
print(list)				#[25,10.8,'HYD',TRUE]

#3.Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)		#[0,10,20,30,40,50] 

#4.Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')	#'HYD' is appended into the list 'a' at the end
print(a)			#[10,20,30,'HYD']
print(len(a))		# 4
print(a[3])	#How  to  print  4th  element  of  list  'a'
print(a[3][0])#How  to  print  'H'
print(a[3][1])#How  to  print  'y'
print(a[3][2])#How  to  print  'd'

#5.Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)	#
print(a)			#[10,20,[50,60,70],30,40
print(len(a))		# 5
print(a[2])		#How  to  print  inner  list
print(a[2][0])	#How  to  print  50
print(a[2][1])	#How  to  print  60
print(a[2][2])	#How  to  print  70


