
'''x=input("enter mixed case string: ")
y=x.upper()
print(y)
a={}
for i in y:
	if i.isalpha():
		a[i]=a.get(i,0)+1
		a[i]=1
print(a)
'''
''' 2 duplicates with set
a=input("enter the string :")
b=set(a)
out="".join(b)
print(out)
'''
'''3 discint vowels
a=input("enter the string :")
b=set(a)  
c="".join(b)
out=''
d=c.upper()
e="AEIOU"
for i in d:
	if i in e:
		out+=i
print(out)
'''
'''4 dulpicates from list
a=eval(input("enter the list "))
b=set(a)
c=list(b)
print(c)
'''
''' 5 addition of two list
a=eval(input("enter the list "))
b=eval(input("enter the list "))
c=a+b
d=list(set(c))
print(d)
'''
'''6 employee salary and name
a={}
n=int(input("enter the no.  of employees: "))
for i in range(n):
	x=input("enter the employee name: ")
	y=float(input("enter the employee salary: "))
	a[x]=y
print(a)
'''
'''7
a=input("enter the employee string:")
b=a.split(',')
print(b)
c={}
for x in b :
	d=x.split('=')
	c[d[0]]=d[1]
print(c)
'''
'''8 dict sorting
a=eval(input("enter the dict: "))
b=sorted(a.items())
c=dict(b)
print(c)
'''
'''9
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b) #{10,20}
print(c)                  #{10,20}
print(type(c))         #<class 'set'>
d = a - b                  #{10,20}
print(d)                  #{10,20}
print(type(d))          #<class 'set'>
print(c  is  d)             #False
print(c  ==  d)             #True
'''
'''10
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)  #{10,20,50,60}
print(c)                                    #{10,20,50,60}
print(type(c))                           #<class 'set'>
d = a ^ b                                   #{10,20,50,60}
print(d)                                    #{10,20,50,60}
print(type(d))                           #<class 'set'>
print(c   is   d)                            #False
print(c  ==   d)                            #True
'''
'''11
a = {x * x  for   x   in   range(10)}
print(a)   # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a))     #<class 'set'>
'''
'''12
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a.get('Empno'))                               #How  to  print  value  25  in  dict  'a')
print(a.get('Ename'))                   # How  to  print  'Rama Rao'  in  dict  'a')
print(a.get('Sal'))                               # How  to  print  value  1000.65   in  dict  'a')
'''
'''13
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)  #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a))   #add1
a.update({'Sal':2000}) # How  to  modify  1000.65  to  2000
a.update({'Ename':'Sita'})  #How  to  modify  'Rama  Rao'  to  'Sita'
a.update({'Empno':35})   #How  to  modify  25   to  35
print(a)                #{'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  : 2000}  
print(id(a))           #add1
'''
'''14
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.update({'Gender':'M'}) #How  to  append  'Gender' : 'M'  to  dictionary  'a'
a.update({ 'Married' :  True }) # How  to  append  'Married' :  True  to  dictionary  'a'
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65 , 'Gender':'M','Married' :  True }
'''
'''15
a = { }
a.update({10 : 'Rama'}) #How  to  append  10 : 'Rama'  to  dictionary  'a'
a.update({20 : 'Sita'})#How  to  append  20 : 'Sita'  to  dictionary  'a'
a.update({15 : 'Rajesh'})#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a.update({18 : 'Kiran'})#How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a) #{10 : 'Rama',20 : 'Sita',15 : 'Rajesh',18: 'Kiran'}
'''
'''16
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.pop('Sal')#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao' }
'''
'''17
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) #True
print(60  in  a . keys())  #False
print(60  in  a . values()) #True
print(30  in  a . values())#False
print(50  in  a)         #True
print(20  in  a)          #False
print(70  not  in  a . keys())   #False
print(40  not  in  a . values()) #False
print(25  not  in  a)    #True
'''
'''18
a = input('Enter  dictionary  :  ')
print(a)  #{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))  #<class 'str'>
b = eval(a)  #{10: 'A', 20: 'D', 15: 'C' , }
print(b)      #{10: 'A', 20: 'D', 15: 'C' }
print(type(b)) #<class 'dict'>
'''
'''19
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}   #{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(b)  
print(a  is  b)  #False
print(a  ==  b)  #True
c = a
print(a  is   c) #True
print(a  ==  c) #True
'''
'''20
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d) #{10,20,15,18,19,14,25}
print(type(d)) #<class 'set'>
e = {**a , **b , **c}
print(e) #{10:'Rama',20:'Manohar',15:'Rajesh',18:'Kiran',14:'Amar',25:'Ramesh',19:'Krishna',14:'Srinivas'}
print(type(e))  #<class 'dict'>
'''
'''21
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) #error 
c = {**a , **b}
print(c) #{10:60,30:50}
d = a | b 
print(d) #{10:60,30:50}
'''
'''22
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) #3
b = {}
print(len(b)) # 0
'''
'''23
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))   #90
print(sum(a . values())) #120
print(sum(a))      # 90
print(sum(a . items())) #error
'''
'''24
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) #40
print(min(a . keys()))  #7
print(max(a . values())) #50
print(min(a . values()))  #5
print(max(a . items())) #(40,5)
print(min(a . items()))  #(7,28)
print(max(a))  #40
print(min(a))    #7
'''
'''25
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c) #  Converts  tuple  of  lists  to  dict
print(d)  #{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'G' : 'Gray'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e)) #error due to 3 obj
f = [[10] , [20] , [30]]
#print(dict(f)) #error
#print(dict([10 , 20])) #error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) #{10:[20,30],40:[50,60],70:[80,90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h)) #error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) {(10, 20): 30, (40, 50): 60, (70, 80): 90}
'''
'''26
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys()) #[5, 10, 15, 18, 20]
print(b) #[5, 10, 15, 18, 20]
c = sorted(a . values()) #['Blue', 'Green', 'Red', 'White', 'Yellow']
print(c) #['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items()) #[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
print(d) #[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True) #[20, 18, 15, 10, 5]
print(f) #[20, 18, 15, 10, 5] 
print(a) #{10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
'''
'''27
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys() #dict_keys([10,20,15,18])
print(b)        #dict_keys([10,20,15,18])
print(type(b)) #<class 'dict_keys'>
for  x  in   b:  
        print(x)    #10,20,15,18
'''
'''28
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values() #dict_values(['Hyd','Sec','Cyb','Pune'])
print(b) #dict_values(['Hyd','Sec','Cyb','Pune'])
print(type(b)) #<class 'dict_values'>
for  x   in   b:
	print(x)        #'Hyd','Sec','Cyb','Pune'
'''
'''29
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items() #dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(b)  #dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) #<class 'dict_items'>
for  x   in   b: 
        print(x)    #(10, 'Hyd'),(20, 'Sec'),(15, 'Cyb'),(18, 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ') #10 ... Hyd,20 ... Sec,15 ... Cyb,18 ... Pune
'''
'''30
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)  #{10 : 20 , 30 : 40 , 50 : 60}
a . clear() #{}
print(a) #{}
del  a     
print(a) #error
'''
'''31
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) #{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) #False
print(a  ==  b) #True
'''
'''32
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) #10
print(y) #20
print(z) #15
print()
x , y , z = a . values()
print(x)  #rama
print(y)  #sita
print(z) #rajesh
print()
x , y ,  z = a . items()
print(x)  #(10, 'Rama')                     
print(y)  #(20, 'Sita')
print(z)  #(15, 'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)   #10, 'Rama'
print(rno2 , sname2)  #20, 'Sita'
print(rno3 , sname3)   #15, 'Rajesh'
'''
'''33
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b) #{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a . update(b) #error
'''
'''34
d = {x : x ** 3   for    x   in  range(5)}
print(d) #{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) #<class 'dict'>
'''
'''35
d = { x :  2 * x    for    x   in   range(5) }
print(d) #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
'''
'''36
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)       #{15:'Sita',17:'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)  #{10:'Rama',18:'Rajesh',12:'Rama rao'}
'''































































