Q1 # difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) #{10,20}
print(type(c)) #<class 'set'>
d = a - b 
print(d) #{10,20}
print(type(d)) #<class 'set'>
print(c  is  d) #False
print(c  ==  d) #True
----------------------------------------------------------------------------------------------
Q2 # symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)  #{10,20,50,60}
print(type(c)) #<class 'set'>
d = a ^ b 
print(d)  # {10,20,50,60}
print(type(d)) #<class 'set'>
print(c   is   d) #False
print(c  ==   d) #True
-------------------------------------------------------------------------------------------------
Q3 # Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) 
print(type(a)) 

OP-
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
<class 'set'>
---------------------------------------------------------------------------------------------------
Q4 Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

a=input('Enter string: ')
b=set(a)
c=''.join(b)
print(c)

OP-
Enter string: Rama Rao
m aoR
-------------------------------------------------------------------------------------------------------
Q5 Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

a=input('Enter string: ')
a=a.upper()
b='AEIOU'
c=''
for x in b:
	if x in a:
		c+=x
print(c)

OP-
Enter string: Hello World
EO
-----------------------------------------------------------------------------------------------------------------
Q6 Write  a  program  to  remove  duplicate  elements  of   list  using  set

a=eval(input('Enter list : '))
b=set(a)
c=list(b)
print(c)

OP-
Enter list :  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
[False, 'Hyd', 1, None, 10.8, 25, 'Sec']
-------------------------------------------------------------------------------------------------------------------
Q7 Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
c=set(a)
d=set(b)
e=c.intersection(d)
f=list(e)
print(f)

OP-
Enter 1st list: [10 , 20 , 30 , 40 , 50 , 60]
Enter 2nd list: [30 , 40 , 70 , 80 , 20]
[40, 20, 30]
-------------------------------------------------------------------------------------------------------------------
Q8 #How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno']) #How  to  print  value  25  in  dict  'a'
print(a['Ename']) #How  to  print  'Rama Rao'  in  dict  'a'
print(a['Sal'])   #How  to  print  value  1000.65   in  dict  'a'
-----------------------------------------------------------------------------------------------------------------
Q9 #How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # 2032330333376
a['Sal'] = 2000 # How  to  modify  1000.65  to  2000
a['Ename'] = 'Sita' #How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno'] = 35  #How  to  modify  25   to  35
print(a)  #{'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000  }
print(id(a)) #2032330333376
-----------------------------------------------------------------------------------------------------------------
Q10 #How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender'] = 'M' # How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = True #How  to  append  'Married' :  True  to  dictionary  'a'
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65 , 'Gender' : 'M' , 'Married' :  True}
-----------------------------------------------------------------------------------------------------------------------
Q11 #Find  outputs (Home  work)
a = { }
a[10] = 'Rama' #How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20] = 'Sita' #How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15] = 'Rajesh' #How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18] = 'Kiran' #How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a) #{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
----------------------------------------------------------------------------------------------------------
Q12 #How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
a.pop('Sal') #How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)  #{'Empno': 25, 'Ename': 'Rama  Rao'}
----------------------------------------------------------------------------------------------------
Q13 #in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) #True
print(60  in  a . keys()) #False
print(60  in  a . values()) #True 
print(30  in  a . values()) #False
print(50  in  a)            #True
print(20  in  a)            #False 
print(70  not  in  a . keys()) #False
print(40  not  in  a . values()) #False
print(25  not  in  a) #True
-------------------------------------------------------------------------------------------------------
Q15 #What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)  #{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) #<class 'str'>
b = eval(a)  
print(b) #{10: 'A', 20: 'B', 15: 'C'}
print(type(b)) #<class 'dict'>
--------------------------------------------------------------------------------------------------------
Q16 #Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) # False
print(a  ==  b) #True
c = a
print(a  is   c) # True
print(a  ==  c)  # True
------------------------------------------------------------------------------------------------------
Q17 #Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)  # {10,20,15,18,14,25,19}
print(type(d)) #<class 'set
e = {**a , **b , **c} 
print(e)  #{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) #<class 'dict'>
------------------------------------------------------------------------------------------------------------------
Q18 #Find  outputs 
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b) #error - cannot cancatenate dictionaries with + operator
c = {**a , **b}
print(c)    #{10:60,30:50}
d = a | b
print(d)    #{10:60,30:50}
-------------------------------------------------------------------------------------------------------------------
Q19 Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

a=int(input('How many Employees ? : '))
b={}
for x in range(a):
	c=input('Enter Emp Name : ')
	d=float(input('Enter Salary : '))
	b[c]= d
print(b)

OP-
How many Employees ? : 6
Enter Emp Name : PRIYA
Enter Salary : 100000
Enter Emp Name : RIYA
Enter Salary : 200000
Enter Emp Name : SWATI
Enter Salary : 30000
Enter Emp Name : RAVALI
Enter Salary : 300000
Enter Emp Name : SUDHA
Enter Salary : 400000
Enter Emp Name : KIARA
Enter Salary : 20000
{'PRIYA': 100000.0, 'RIYA': 200000.0, 'SWATI': 30000.0, 'RAVALI': 300000.0, 'SUDHA': 400000.0, 'KIARA': 20000.0}
------------------------------------------------------------------------------------------------------------------------
Q20 Write  a  program  to  convert  a  string  to  dictionary

a=input('Enter string with its values seperated by comma(,) : ')
b=a.split(',')
e={}
for x in b:
	Key,Value=x.split('=')
	e[Key.strip()]=Value.strip()
print(e)

OP-
Enter string with its values seperated by comma(,) : Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m
{'Emp no': '25', 'Emp name': 'Rama  Rao', 'sal': '10000.0', 'gender': 'm'}

Q21 # len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3
b = {}
print(len(b))  #0
-----------------------------------------------------------------------------------------------------------------------------
Q22 #sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90
print(sum(a . values())) #120
print(sum(a)) #90 
print(sum(a . items())) #error  
------------------------------------------------------------------------------------------------
Q23 #max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) #40
print(min(a . keys())) #7
print(max(a . values())) #50 
print(min(a . values())) #5
print(max(a . items())) # (40,5)
print(min(a . items())) #(7,28)
print(max(a)) #40
print(min(a)) #7
------------------------------------------------------------------------------------------------
Q24 #dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c) 
print(d)  # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e)) # error due to 3 elements in inner list
f = [[10] , [20] , [30]]
#print(dict(f))  # error due to 1 element in the inner list, 2 is needed
#print(dict([10 , 20])) #error - elements 10,20 cannot convert to dict because they are not in key , value pairs
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) #{10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h)) #error because kekys are in the list are mutable. keys must be immutable
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) #{(10, 20): 30, (40, 50): 60, (70, 80): 90}
---------------------------------------------------------------------------------------------------------------------
Q25 #sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)   #[5, 10, 15, 18, 20]
c = sorted(a . values())
print(c)   #['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d)   #[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f)   #[20, 18, 15, 10, 5]
print(a) #{10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
-----------------------------------------------------------------------------------------------------------------
Q26 Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

a=eval(input('Enter key,value pairs in dictionary: '))
b=sorted(a.items())
c=dict(b)
print(c)

OP-
Enter key,value pairs in dictionary: {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}
-----------------------------------------------------------------------------------------------------------------
Q27 #keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys() 
print(b)         # #dict_keys([10, 20, 15, 18])
print(type(b))  ##<class 'dict_keys'>
for  x  in   b:  
        print(x)  #10 \n 20 \n 15 \n 18
-------------------------------------------------------------------------------------------------------------
Q28 #values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)    #dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b))  #<class 'dict_values'>
for  x   in   b:
	print(x)     # Hyd \n Sec \n Cyb \n Pune
-------------------------------------------------------------------------------------------------------------
Q29 #items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)   #dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b))  #<class 'dict_items'>
for  x   in   b:
        print(x)
for  x , y   in  b:
        print(x , y , sep = ' ... ')

OP-
dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
<class 'dict_items'>
(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
------------------------------------------------------------------------------------------------------------
Q30 #Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')     # 10...Hyd \n 20...Sec \n 15...Cyb  \n 18...Pune 
#for  x , y   in  a . keys():
#       print(x , y , sep = ' ... ')     #error- y is not needed to unpack keys
#for  x , y   in  a . values():
#       print(x , y , sep = ' ... ')      #error- x is not needed to unpack values
#for  x , y   in  a:
#       print(x , y , sep = ' ... ')       #error - y is not needed to unpack keys
-----------------------------------------------------------------------------------------------------------------
Q31 #clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)  #{10 : 20 , 30 : 40 , 50 : 60}
a . clear() 
print(a)  #{}
del  a    
print(a)  # error- dictionary is deleted
------------------------------------------------------------------------------------------------------------------
Q32 #copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)      #{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b)  #False 
print(a  ==  b)  #True
--------------------------------------------------------------------------------------
Q33 #Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # 10
print(y) #20
print(z) #15
print()
x , y , z = a . values()
print(x) # Rama
print(y) #Sita
print(z) #Rajesh
print()
x , y ,  z = a . items()
print(x)  #(10,Rama)
print(y)  #(20,Sita)
print(z) #(15,Rajesh)
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) #10 Rama
print(rno2 , sname2) #20 Sita
print(rno3 , sname3) #15 Rajesh
-------------------------------------------------------------------------------------------------------------------------------
Q34 Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

a=input('Enter mixed case string: ')
b=sorted(a)
c={}
for x in b:
	if x.isalpha():
		c[x.upper()]=c.get(x.upper(),0)+1
print(c)

OP-
Enter input: missisipi
{'I': 4, 'M': 1, 'P': 1, 'S': 3}
----------------------------------------------------------------------------------------------------------------------------------------- 
Q35 #Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)      #{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a . update(b) #error -list dont have update method
-------------------------------------------------------------------------------------------------------
Q36 #Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a)
#print(b)  # error- there are 3 values in  tuple in list. only 2 are needed
c = [(10,) , (20,) , (30,)]
#b . update(c) # error - dict requires two elements for key value pairs
print(b) #{}
----------------------------------------------------------------------------------------------------
Q37 #Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)  #{0:0,1:1,2:8,3:27,4:64}
print(type(d)) #<class 'dict'>
-----------------------------------------------------------------------------------------------------
Q38 #Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) #{0:0,1:2,2:4,3:6,4:8}
--------------------------------------------------------------------------------------------------------
Q39 #Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) #{15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) #{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}
