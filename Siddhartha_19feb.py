# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)                 #dict object a
for x in a.keys():
	print(x)             #all keys in object a
for x in a.values():
	print(x)             #all values in object a
for x in a.items():
	print(x)              #all key-values
for x,y in a.items():
	print(x,y, sep='...')  #all key-values sep by ...


a = {
		print('Hyd') ,   #Hyd
		print('Sec') ,   #Sec
		print('Cyb')     #Cyb
     }
print(type(a))   #class <set>
print(a)         #None
print(len(a))    #1

_ = 25
print(_)         #25
print(type(_))   #class int
a , _ , c = 10 , 20 , 30
print(a)        #10
print(_)        #20
print(c)        #30
for _ in  range(5):
	print(_,'Hello')  #iterate 0 to 4

a = 25
print(id(a))   #ramdom adress 1000
a = 35
print(id(a))   #ramdom address 2000

a = 25.7
print(id(a))  #ramdom id 1000
print(a)      #25.7
a = 35.6
print(id(a))  #ramdom id 2000
print(a)      #35.6
b = True
print(id(b))  #ramdom id 3000
b = False    
print(id(b))  #ramdom id 4000
c = None
print(id(c))  #ramdom id 5000
c = None
print(id(c))  #same id


a = 'Hyd'
print(id(a)) #ramdom id 1000
#a[1] = 'e'
a = 'Sec'    
print(id(a))   #ramdom id 2000
b = (10 , 20 , 15 , 18)
print(id(b))   #ramdom id 3000
#b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b))   #ramdom id 4000
c = range(5)
print(id(c))   #ramdom id 5000
#c[3] = 10
c = range(5)
print(id(c))   #ramdom id 6000


a = 25
b = 25
print(a  is  b)   #True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)   #True
e = False
f = False
print(e  is  f)   #true
g = range(10)
h = range(10)
print(g is h)   #False

a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)           #False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)           #False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)          #True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g is h)          #False


print(10 + 20)           #30
print(10.8 + 20.6)       #31.4
print(3 + 4j + 5 + 6j)   #8+10j
print(True + False)      #1
print('Hyder' + 'abad')     #Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') #SankarDayalSarma
print('10' + '20')                    #1020
print([10 , 20 , 30] + [1 , 2 , 3])      #[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))   # concatenate two tuples using the + operator
# print({10 , 20} + {30 , 40})                 #Error
# print({10 : 'Hyd'} + {20 : 'Sec'})           #Error
# print(range(4) + range(5))                   #Error
# print(10 + '20')                             #Error
# print([10 , 20 , 30] + 5)                     #Error
# print([10,20,30]+(40,50,60))        #Error

print(25 * 3)                      #75
print(10.8 * 25.6)                 #276.48
print(True * False)                #0  
print((3 + 4j) * (5 + 6j))         #-9+38j
print(3 + 4j * 5 + 6j)             #3+4j
print('25' * 3)                    #252525
print(3 * '25')                    #252525
print('Hyd' * 4)                   #HydHydHydHyd
print([10 , 20 , 15] * 2)          #[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3) #(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
#print([10 , 20 , 15] * 3.0)        #Error
#print({10 , 20 , 15} * 2)          #Error
#print({10 : 20 , 30 : 40} * 2)     #Error
#print([10]*[20])                 #Error

#print(7 / 0) #Error
#print(7 // 0) #Error
#print(7%0)   #Error

print(3 ** 4)   #  3 ^ 4 = 81
print(10 ** -2)    #0.01
print(4 ** 3 ** 2)   #262144
print(3+4*5-32/2**3)  #19.0

print(9 >= 5)  #  True  becoz  >  is  satisfied
print(9 >= 9)   #  True  becoz  =  is  satisfied
print(9 >= 12)   #  False  becoz    both  are  not  satisfied
print(6 <= 8)    #True
print(6 <= 6)     #True
print(6 <= 4)     #False
print(9 != 7)     #True
print(6 == 8)     #False
print(True  >  False)    #True
print(3 + 4j == 3 + 4j)  #True
print(3 + 4j == 5 + 6j)  #False
print(3 + 4j != 5 + 6j)  #True
print(10 == 10.0)        #True
#print(3+4j>3+4j)   #Error

print('Rama'   >  'Rajesh')   #   True  becoz  'm' > 'j'
print('Rama'  <  'Sita')      #True
print('Hyd'  ==  'Hyd')       #True
print('Rama'  <=   'Ramana')   #True
print('Rama  Rao'  >=  'Rama')  #True
print('Hyd'  != 'Sec')        #True
print('HYD'  <   'hyd')      #True


print(10 < 20 < 30)    #   True  becoz  both  are  satisfied
print(10 >= 20 < 30)   #  False  becoz  1st  cond  is  not  satisfied
print(10 < 20 > 30)    #False
print(1 < 2 < 3 < 4)   #True
print(1 < 2 > 3 > 1)   #False
print(4>3>=3>2)   #True


