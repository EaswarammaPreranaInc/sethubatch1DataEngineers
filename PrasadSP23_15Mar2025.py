#15/3/2025 

#1.Find  outputs 



a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a)) #<class 'tuple'>
#a[3] = 'Sec' #error becz tuple is immutable



#2.What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?  


a = input('Enter  Tuple  :  ')
print(a) #(10 , 20 , 30 , 40)
print(type(a)) #,class 'str'>

b = eval(a) 
print(b) # (10 , 20 , 30 , 40)
print(type(b)) #<class 'tuple'>
print(len(b)) #4




#3.Find  outputs 


a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70 
print(a) #(10 , [70 , 30 , 40] , 50 , 60)
#a[1] = [80 , 90 , 100]  #error due tuple is immutable
print(a)




#4.Find  outputs 


a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70 # error becz tuple is immutable 
print(a) #[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90] 
print(a) #[10 , [80,90] , 50 , 60]




#5.Find  outputs



a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) #(25,10.8,'Hyd',True)
print(type(x)) # <class 'tuple'>




#6.Find  outputs 



x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) #25
print(b) #10.8
print(c) #Hyd
print(d) #True
#p , q , r =  x # error becz more values to unapck
#a , b , c , d  , e = x # # error becz not enough  values to unapck




#7.Find  outputs 


x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) #25
print(b) # [10.8,'Hyd']
print(c) #True




#8.Find  outputs 


tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) #25
print(b) #10.8
print(c) #[]
print(d) #Hyd
print(e) #True




#9.Find  outputs 


x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) #25
print(b) #10.8
print(_) #(3+4j)
print(d) #True
print(_) #(3+4j)




#10.tuple()  function  demo  program 



a = range(100 , 150 , 10)
b = tuple(a) 
print(b) #(100,110,120,130,140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) #(10 , 20 , 15, 18)
e = tuple('Vamsi')
print(e) #('V','a','m','s','i')
#print(tuple(25)) #Error due to 25 
print(tuple()) #()




#11.index()  and  count()  methods  demo  program 



a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1    2    3    4   5     6    7   8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i) # 2 5 8 \n 15  is  found  3  times
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
		



#12.How  to  modify  an  element  of  tuple ? 


a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1    2       3     4
#a[2] = 35 #error becz tuple is immutable
print(a) #(10 ,  20 ,  30 ,   40 ,  50)
print(id(a)) #address
#How  to  modify  30  in  tuple  to  35
a=list(a)
a[2]=35 
a=tuple(a)
print(a) #(10 ,  20 ,  35,   40 ,  50)
print(id(a)) #different 




#13.How  to  delete  an  element  of  tuple ? 


a  = 10 , 20 , 30 , 40 , 50
#    0     1    2   3    4
#a . remove(30) #error becz tuple is immutable 
#del  a[2] #error becz tuple is immutable 
#a . pop(2) #error tuple obj doesn't have pop method 
print(a) #(10 , 20 , 30 , 40 , 50)
print(id(a)) #1000

#How  to  remove  30  from  tuple  'a'
a=a[:2]+a[2:]
print(a) #(10 , 20 , 40 , 50)
print(id(a)) #2000




#14.Nested   tuple

a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) #( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
print(a[0]) #How  to  print  1st  inner  tuple
print(a[1]) #How  to  print  2nd  inner  tuple
print(a[2]) #How  to  print  3rd  inner  tuple
print(a[0][1])  #How  to  print  20
print(a[1][-1])  #How  to  print  50
print(a[2][-1]) #How  to  print  90





#15.Find  outputs 



a = ((10 , 20 , 30),)
print(a[0])#How  to   print  inner  tuple
print(*a) #How  to   print  inner  tuple  in  another  way
print(a[0][0]) #How   to  print   10
print(a[0][1]) #How   to  print   20
print(a[0][2]) #How   to  print   30
b = ((),)
print(b[0]) #How  to   print  inner  tuple  of  tuple  'b'
print(*b)  #How  to   print  inner  tuple  of  tuple  'b'  in  another  way





#16.Find  outputs


a = ((10 , 20 , 30))
print(a) #(10 , 20 , 30)
print(*a) # 10 20 30 
b = (())
print(b) # ()
print(*b) # nothing 




#17.What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}


a = input('Enter  Set  :  ')
print(a) #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) #<class 'str'>
b = eval(a)
print(b) #{10 , 20 , 15 , 18 , 12 }
print(type(b)) #<class 'sst'>



#18.Find  outputs 


print({(10 , 20 , 30)}) #{(10 , 20 , 30)}
#print({[10 , 20 , 30]}) # error no mutable objs 
#print({{10 , 20 , 30}}) # error no mutable objs 
#print({{}}) # no mutable objs 




#19.How  to  print  set  in  differnet ways  


a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop

for i in a:
    print(i)



#20.Find  outputs


a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) #{'Hyd',True,25}
print(len(s)) #3
print(type(s)) #<class 'set'>




#21.Find  outputs



s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } whatever order here 
a , b , c , d = s
print(a) #Hyd
print(b) #25
print(c) #True 
print(d) #10.8 





#22.Find  outputs


s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b = s 
print(a) #Hyd
print(b) #[ 25,  True,  10.8 ]
print(type(b)) #<class 'list'>




#23.Find  outputs


s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 }
a , *b , c = s 
print(a) #Hyd 
print(b) #[25,True]
print(c) #10.8




#24.Find  outputs 


s = {20 , 10 , 20 , 10}
print(s) #{10 , 20}
x , y = s 
print(x) #10
print(y) #20




#25.set()  function  demo  program


a = range(100 , 151 , 10)
b = set(a)
print(b) #{100,110,120,130,140}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c) 
print(d) #{20,15,18,10,50,12}
e = set('Rama  rAo')
print(e) #{'R','a','m',' ','r','A','o'}
#print(set(25)) #Error due to 25 
print(set()) #set()



#26.add()  method  demo  program


a = set()
a . add(True)
a . add(25)
a . add(10.8)
a . add(1)
a . add('Hyd')
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0)
print(a) #{True,25,10.8,'Hyd',None}
#a . add(10 , 20 , 30) #Error because add method takes 1 arg 
#a . add([10,20,30]) #Error becz set doesn't have mutable obj like list 





#27.Find  outputs 


a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25 , 10.8 , 'Hyd' , True}
print(id(a)) #1000
a . add(tpl) 
a . add('Sec')  
print(a) #{25 , 10.8 , 'Hyd' ,'Sec' ,True,(10 , 20 , 30)}
print(id(a)) #1000
print(len(a)) #6
#a . add([100 , 200 , 300]) # #Error no mutable obj in set
#a . add(set()) #Error no mutable obj in set
#a . add({ }) #Error no mutable obj in set




#28.Find  outputs


s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) 
print(s) #{(10 , 20 , 15 , 18)}
print(len(s)) #1



#29.update()  method  demo program


tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) 
print(len(s)) #4
print(s) #{10 , 20 , 15, 18 , 10 , 20}
#s . update(25) #Error for update arg should be sequence




#30.Find  outputs


a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) #{10,20,30,40,50,60,70}
print(len(s)) #7
#s . add(a , b , c) #error because 3 args 





#31.Find  outputs

a = set()
a . update('Rama Rao')
print(a) #{'R','a','m',' ','o'}
print(len(a)) #5
#a . update(3 + 4j , 10.8 , True) #Error due to non sequence 




#32.copy()  method  demo  program


a = {10 , 20 , 15 , 18}
print(a) #{10 , 20 , 15 , 18}
b = a . copy()
print(b) #{10 , 20 , 15 , 18}
print(a  is  b) #False
print(a  ==  b) #True 
c = a
print(a  is  c) #True



#33.remove()  method  demo  program 


a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd') 
print(a) #{25 , 10.8 ,True}
#a . remove('Sec') #Error 




#34.discard()  method  demo  program


a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a) #{25 , 10.8 , True}
a . discard('Sec') 
print(a) #{25 , 10.8 , True}
#a . remove('Sec') #Error 



#35.clear()  method  demo  program 


a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
a . clear()
print(a) #set()
print(len(a)) #0




#36.Find  outputs  (Home work)


a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {10 , 20 , 30 , 40,50,60}
#print(a | b), # Error due to |
#print(b . union(a)) # Error due to union 
#print(a + b) #Error due to +

