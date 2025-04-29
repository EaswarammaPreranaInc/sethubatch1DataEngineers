#12/3/2025 
#1.append()  method  demo  program

'''
list = [10,20,15,18]
print(list) #[10,20,15,18]
list . append(19)
print(list) #[10,20,15,18,19]

'''


#2.Find  outputs

'''

list = []
print(list) #[]
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) #[25,10.8,'Hyd',True]


'''


#3.Find  outputs

'''

list = []
for  x  in   range(0 , 50 , 10):
	list . append(x) 
print(list) #[0,10,20,30,40]

'''


#4.Find  outputs 

'''

a = [10 , 20 , 30]
a . append('Hyd')
print(a)      # [10 , 20 , 30,'Hyd']
print(len(a)) #4
print(a[3],a[-1]) #How  to  print  4th  element  of  list  'a'
print(a[3][0],a[-1][0]) #How  to  print  'H'
print(a[3][1],a[-1][1]) #How  to  print  'y'
print(a[3][2],a[-1][2]) #How  to  print  'd'


'''

#5.Find  outputs

'''
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b) 
print(a)       #[10,20,[50 , 60 , 70],30,40]
print(len(a))  #5
print(a[2],a[-3])       #How  to  print  inner  list
print(a[2][0],a[-3][0]) #How  to  print  50
print(a[2][1],a[-3][1]) #How  to  print  60
print(a[2][2],a[-3][2]) #How  to  print  70


'''