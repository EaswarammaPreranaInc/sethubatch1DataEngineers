'''
#1.What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ') #[25,10.8,'Hyd',True]
print(type(a)) #<class 'str'>
print(a) # [25,10.8,'Hyd',True]
b = eval(a) # [25,10.8,'Hyd',True]
print(b)  # [25,10.8,'Hyd',True]
print(type(b)) # <class 'list'>

'''

# 2.Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a #same reference
print(a  is  b) # True
print(a  ==  b) # True same Value
b[2] = 12 
print(a) # [10,20,12,18]



# 3.Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # [10 , 20 , 15 , 18 , 100 , 200 , 150]
#print(a + 5) # Error list + int 
#print(a + '5') # Error list + str
#print([10 , 20] + (30 , 40)) # error list + tuple 



#4.Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  25,[10.8,'Hyd'],True
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list # 25,[10.8,'Hyd',True]
print('x : ' , x) #25
print('y : ' , y) #[10.8,'Hyd',True]
*p , q = list #[25 , 10.8 , 'Hyd'],True
print('p : ' , p) #[25 , 10.8 , 'Hyd']
print('q : ' , q) #True




#5.Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list #error due to less args 
a , b , *c , d , e = list #25,10.8,[],'Hyd',True
print('a : ' , a) #25
print('b : ' , b) #10.8
print('c : ' , c) #[]
print('d : ' , d) #'Hyd'
print('e : ' , e) #True
#a , b , *c , d , e , f = list #error due to less args 




#6.Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list 
print('a : ' , a) #25
print('b : ' , b) #10.8
print('_ :  ' , _) #'Hyd'
print('d : ' , d)  #True




#7.Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list  
print('a : ' , a) #(3+4j)
print('b : ' , b) #10.8
print('d : ' , d) #True





#8.Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)  #25
print('b : ' , b)  #10.8
print('_ : ' , _)  #(3+4j)
print('d : ' , d)  #True
print('_: ' , _)   #(3+4j)




#9.Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list #error due to multiple *






#10. Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) #[25,10.8]
print('b :  ' , b) #'Hyd'
print('c :  ' , c) #True





#11. Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # 25
print('b : ' , b) #10.8
print('c : ' , c) #'Hyd'
print('d : ' , d) #True
#a , b , c , d = list #error due to less unpack args 





#12. Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)  # True
print(a  is   b) # False
print(a < c) #True
print(a > d) #True
print(a >= c) #False
print(a <= d) #False
print(a != c) #True
print(a != b) #False
print(a == c) #False




#13.Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #False
print(a  is   b) #False




# 14.len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) #4
b = []
print(len(b)) #0
c = [[10 , 20] , 30 , 40]
print(len(c)) #3




#15.sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) #36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # (8+10j)
c = [25 , 10.8 , True , 3 + 4j , False] 
print(sum(c)) # (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d)) #63
e = [25 , 10.8 , 'Hyd' , True] 
#print(sum(e)) #error due to 'Hyd'




#16.Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a)) #error 
print(sum(a[0]))
print(sum(*a))




#17.max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #30
print(min(a)) #5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) #'Vamsi'
print(min(b)) #'Amar'
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) #error due to complex
d = [25 , '35'] 
#print(max(d)) # error 
#print(max([])) #error
#print(min([])) #error





#18.list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b) # [10,20,15,18]
print(type(b)) #,class 'int'>
print(a  is  b) # False
print(a == b) # False




#19.Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a) 
print(b)  #[4,6,8]
print(type(b)) #<class 'list'>
a = list('Vamsi')
print(a) #['V','a','m','s','i']
a = list()
print(a) #[]
#print(list(25)) #error 
#print(list(10.8)) #error
#print(list(True)) #error
#print(list(None)) #error list arg is nothing or any sequence






#20.Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) #[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) #[[10 , 20] , (30 , 40) , {50 , 60}]




#21.Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a) 
print(b) #['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']
c = sorted(a , reverse = True)
print(c) #['Vamsi','Sita','Rama Rao','Rama','Rajesh','Kiran','Amar']
print(a) #['Rama','Rajesh','Amar','Sita','Vamsi' ,'Kiran','Rama  Rao']





#22.all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) #True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) #False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) #False
d = [10 , 0 , 20]
print(all(d)) #False
e = []
print(all(e)) #True *





#23. any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) #True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) #False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) #True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) #False
e = []
print(any(e)) #False

