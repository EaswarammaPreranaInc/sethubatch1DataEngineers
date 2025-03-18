'''
#1.difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b) 
print(c)		# {10,20}
print(type(c))	# <class 'set'}
d = a - b		
print(d)		# {10,20}
print(type(d))	# <class 'set'}
print(c  is  d) # False
print(c  ==  d) # True

#2.symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)			# {10,20,50,60}
print(type(c))		# <class 'set'>
d = a ^ b
print(d)			# {10,20,50,60}
print(type(d))		# <class 'set'>
print(c   is   d)	# False
print(c  ==   d)	# True

#3.Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)		# {0,1,4,9,16,25,36,9,64,81} in any order because set is unordered
print(type(a))	# <class 'set'>


#4.How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a.get('Empno'))#How  to  print  value  25  in  dict  'a'
print(a.get('Ename'))#How  to  print  'Rama Rao'  in  dict  'a'
print(a.get('Sal'))#How  to  print  value  1000.65   in  dict  'a'

#5.How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)	#{'Empno':25,'Ename':'Rama Rao','Sal':1000.65}
print(id(a))# may 10000
a['Sal']=2000 #How  to  modify  1000.65  to  2000
a['Ename']='Sita' #How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno']=35 #How  to  modify  25   to  35
print(a)	#{'Empno':35,'Ename':'Sita",'Sal':2000}
print(id(a))# may be 20000

#6.How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)	#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.setdefault('Gender','M') #How  to  append  'Gender' : 'M'  to  dictionary  'a'
a.setdefault('Married', True) #How  to  append  'Married' :  True  to  dictionary  'a'
print(a)	#{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}

#7.Find  outputs (Home  work)
a = { }
a.setdefault(10,'Rama') #How  to  append  10 : 'Rama'  to  dictionary  'a'
a.setdefault(20,'Sita') #How  to  append  20 : 'Sita'  to  dictionary  'a'
a.setdefault(15,'Rajesh') #How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a.setdefault(18,'Kiran') #How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a) # { 10:'Rama',20:'Sita',15:'Rajesh',18:'Kiran'}

#8.How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)	#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a.pop('Sal')) #How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao' }

#9.in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())		# True
print(60  in  a . keys())		# False
print(60  in  a . values())		# True
print(30  in  a . values())		# False
print(50  in  a)				# True
print(20  in  a)				# False
print(70  not  in  a . keys())	# False
print(40  not  in  a . values())# False
print(25  not  in  a)			# True

#10.What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)		#{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))	# <class 'str'>
b = eval(a)		
print(b)		#{10: 'A', 20: 'D', 15: 'C'}
print(type(b))	# <class 'dict'>

#11.Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)			#{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)		# False
print(a  ==  b)		# True
c = a				
print(a  is   c)	# True
print(a  ==  c)		# True

#12.Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)	# {10, 14, 15, 18, 19, 20, 25}
print(type(d))	# <class 'set'>
e = {**a , **b , **c}	
print(e)		#{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))	# <class 'dict'>
'
#13.Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b)	# Error...
c = {**a , **b}	
print(c)		#{10:60,30:50}
d = a | b		
print(d)		#{10:60,30:50}

#14.sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))		# 90
print(sum(a . values()))	# 120
print(sum(a))				# 90
#print(sum(a . items()))	# Error..

#15.max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))		# 40
print(min(a . keys()))		# 7
print(max(a . values()))	# 50
print(min(a . values()))	# 5
print(max(a . items()))		# (40,5)
print(min(a . items()))		# (7,28)
print(max(a))				# 40
print(min(a))				# 7

#16.dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)		# Converts tuple of list to dict
print(d)		# {'R': 'Red','G': 'Gray','B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e))	# Error...
f = [[10] , [20] , [30]]
#print(dict(f)) # Error...
#print(dict([10 , 20])) # Error..
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))	#{10:[20,30],40:[50,60],70:[80,90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h))	# Error..
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))	#{(10,20):30,(40,50):60,(70,80):90}

#17.sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)	#[ 5,10,15,18,20]
c = sorted(a . values())
print(c)	#['Blue','Green','Red','White','Yellow']
d = sorted(a . items())
print(d)	#[(5:'White'),(10:'Red'),(15:'Blue'),(18:'Yellow'),(20:'Green)]
f  = sorted(a  , reverse = True)
print(f)	#[20,18,15,10,5]
print(a)	#{10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}

#18.keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)	#{10,20,15,18}
print(type(b))	#<class 'set'>
for  x  in   b:
        print(x)  #10<space>20<space>15<space>18<nextLine>

#19.values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)	#(['Hyd','Sec','Cyb','Pune'])
print(type(b))# <class 'dict_values'>	
for  x   in   b:
	print(x)	# 'Hyd'<space>'Sec'<space>'Cyb'<space>'Pune'<nextLine>

#20.clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)	#{10 : 20 , 30 : 40 , 50 : 60}
a . clear()	#clear() method  removes all the elements from dictionary 'a'	
print(a)	# {}
del  a		# del operator deletes dictionary 'a'
print(a)	# Error...

#21.copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()	# copies dict 'a' to 'b'
print(b)		#{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b)	# False
print(a  ==  b)	# True

#22.Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)	# 10
print(y)	# 20
print(z)	# 15
print()		# prints nothing and moves to next line
x , y , z = a . values()
print(x)	# 'Rama'
print(y)	# 'Sita'
print(z)	# 'Rajesh'
print()		# prints nothing and moves to next line
x , y ,  z = a . items()
print(x)	# (10:'Rama')	
print(y)	# (20:'Sita')
print(z)	# (15:'Rajesh')
print()		# prints nothing and moves to next line
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)	# 10 Rama
print(rno2 , sname2)	# 20 Sita
print(rno3 , sname3)	# 15 Rajesh
'''
