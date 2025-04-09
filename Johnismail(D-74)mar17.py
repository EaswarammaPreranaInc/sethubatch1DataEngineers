'''# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)#{10,20}
print(type(c))#<class 'set'>
d = a - b
print(d)#{10,20}
print(type(d))#<class 'set'>
print(c  is  d)#False
print(c  ==  d)#True

# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10,20,50,60}
print(type(c))#<class 'set'>
d = a ^ b
print(d)#{10,20,50,60}
print(type(d))#<class 'set'>
print(c   is   d)#False
print(c  ==   d)#True

# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)#{0,1,4,9,16,25,36,,49,64,81}
print(type(a))#<class 'set'>



(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  ---> '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'

a=input('enter any string:')#Rama Rao
b=set(a)
c=''.join(b)
print(c)

outputs--
enter any string:Rama Rao
o Rma

Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes

a=input('enter any string:')#rama rao
v='AEIOU'
b=set(a)
c=''
for i in b:
		i=i.upper()
		if i in v and i not in c:
				c+=i
print(c)

outputs---
enter any string:Rama Rao
AO

Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists

a=eval(input('enter any list:'))
b=set(a)
c=list(b)
print(c)

output---
enter any list: [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
[False, 1, 'Sec', 10.8, 25, 'Hyd', None]

Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output  are  lists

a=eval(input('enter first lis elements:'))
b=eval(input('enter second list elements:'))
c=set(a)
d=set(b)
e=c.intersection(d)
f=list(e)
print(f)

outputs---

enter first lis elements:[10,20,30,40,50,60]
enter second list elements:[30 , 40 , 70 , 80 , 20]
[40, 20, 30]

#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
#print(How  to  print  value  25  in  dict  'a')
print(a.get('Empno'))
#print(How  to  print  'Rama Rao'  in  dict  'a')
print(a[ 'Ename'])
#print(How  to  print  value  1000.65   in  dict  'a')
print(a.get('Sal'))

outputs--
25
Rama  Rao
1000.65

# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a))#random adress
#How  to  modify  1000.65  to  2000
a['Sal']=2000

#How  to  modify  'Rama  Rao'  to  'Sita'
a['Rama Rao']='Sita'
#How  to  modify  25   to  35
a['Empno']=35
print(a)#{'Empno': 35, 'Ename': 'Rama  Rao', 'Sal': 2000, 'Rama Rao': 'Sita'}
print(id(a))#same address


#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
#How  to  append  'Gender' : 'M'  to  dictionary  'a'
a.setdefault('Gender','M')
#How  to  append  'Married' :  True  to  dictionary  'a'
a.setdefault('Married',True)
print(a)

# Find  outputs (Home  work)
a = { }
#How  to  append  10 : 'Rama'  to  dictionary  'a'
a.setdefault(10 , 'Rama')
#How  to  append  20 : 'Sita'  to  dictionary  'a'
a.setdefault(20 , 'Sita')
#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a.setdefault(15 , 'Rajesh')
#How  to  append  18 : 'Kiran'  to  dictionary  'a'
a.setdefault(18 , 'Kiran')
print(a)#{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}


#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
a.pop('Sal')
print(a)#{'Empno': 25, 'Ename': 'Rama  Rao'}

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())#True
print(60  in  a . keys())#False
print(60  in  a . values())#True
print(30  in  a . values())#False
print(50  in  a)#True
print(20  in  a)#False
print(70  not  in  a . keys())#False
print(40  not  in  a . values())#False
print(25  not  in  a)#True

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)#{10: 'A', 20: 'B', 15: 'C' ,20:'D'}
print(type(a))#<class 'str'>
b = eval(a)
print(b)#{10: 'A', 20: 'D', 15: 'C' , }
print(type(b))#<class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)#{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)#False
print(a  ==  b)#True
c = a
print(a  is   c)#True
print(a  ==  c)#True

#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)#{10,20,15,18,14,25,19}
print(type(d))#<class 'set'>
e = {**a , **b , **c}
print(e)#{10 : 'Rama' , 20 : 'Manohar' , 15 : 'Radha',18 : 'Kiran' , 14 : 'Srinivas' ,25 : 'Ramesh' , 19 : 'Krishna' , }
print(type(e))#class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b)#error unsupportes operand 
c = {**a , **b}
print(c)#{10:60,30:50}
d = a | b
print(d)#{10:60,30:50}

(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'

How many Employees ? : 4
Enter Emp Name : AAA
Enter Salary : 10000
Enter Emp Name : BBB
Enter Salary : 20000
Enter Emp Name : CCC
Enter Salary : 15000
Enter Emp Name : DDD
Enter Salary : 18000
{'AAA': 10000.0, 'BBB': 20000.0, 'CCC': 15000.0, 'DDD': 18000.0}
a=int(input('enter How many employes:'))
d={}
for i in range(0,a):
		if i<a:
			b=input('enter Emp name:')
			c=float(input('enter Emp salary:'))
			d['AAA']=10000.0
			d['BBB']=2000.0
			d['CCC']=30000.0
			d['ddd']=40000.0
print(d)
outputs---
enter How many employes:4
enter Emp name:'AAA'
enter Emp salary:10000.0
enter Emp name:'BBB'
enter Emp salary:2000.0
enter Emp name:'CCC'
enter Emp salary:30000.0
enter Emp name:'ddd'
enter Emp salary:40000.0
{'AAA': 10000.0, 'BBB': 2000.0, 'CCC': 30000.0, 'ddd': 40000.0}

Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice


a =  "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
b = ['Emp no = 25' , 'Emp name = Rama  Rao' , 'sal = 10000.0' , 'gender = m']
c = {}
x =  'Emp no = 25'  --->  ['Emp  no' , '25']  ---> {'Emp  no': '25'}
x = 'Emp name = Rama  Rao'  --->  ['Emp name' , 'Rama  Rao']  --->  {'Emp  no': '25' , 'Emp  name': 'Rama Rao'}}

a=input('enter a string:')
b=a.split(',')
c=b.split('=')
print(c)

# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))#3
b = {}
print(len(b))#0

What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary

#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))#{90}
print(sum(a . values()))#{120}
print(sum(a))#{90}
print(sum(a . items()))#error


# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))#40
print(min(a . keys()))#7
print(max(a . values()))#50
print(min(a . values()))#5
print(max(a . items()))#{40:5}
print(min(a . items()))#{7:28}
print(max(a))#{40}
print(min(a))#{7}


#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)#
print(d)#{'R' , 'Red' , 'G' , 'Gray' , 'B' , 'Blue' , }
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e))#error
f = [[10] , [20] , [30]]
#print(dict(f))#error
#print(dict([10 , 20]))#error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))#{10:[20,30] , 40:[50,60], 70:[80,90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h))#error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))#{(10, 20): 30, (40, 50): 60, (70, 80): 90}

# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)#{5}
c = sorted(a . values())
print(c)#{'Blue','Green','Red','White','Yellow'}
d = sorted(a . items())
print(d)#{5 : 'White',10 : 'Red',15 : 'Blue','Green' ,18, 20 : 'Green'}
f  = sorted(a  , reverse = True)
print(f)#{ 20,18,15,10,5}
print(a)#{10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}

Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function

4) a = {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    b = sorted(a . items())  --->  [(5 , 'D' ) , (10 , 'A') , (12 , 'E') , (15 , 'C') , (20, 'B')]
    dict(b)  --->  {5 : 'D' , 10 : 'A' , .....}
a=eval(input('enter dict:'))
b=sorted(a.items())
c=dict(b)
print(c)

outputs---
enter dict:{10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}

#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)#{10,20,15,18}
print(type(b))#<class 'dict_keys'>
for  x  in   b:
        print(x)#10
		#20
		#18
		#15
# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)#{'Hyd','Sec','Cyb','Pune'}
print(type(b))#{<class 'dict_values'>
for  x   in   b:
	print(x)#'Hyd'
	#'Sec'
	#'Cyb'
	#'Pune'

#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)#([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b))#<class 'dict_item'>
for  x   in   b:
        print(x)#(10 , 'Hyd')
		#(20 , 'Sec')
		#(15 , 'Cyb')
		#(18  'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ')
	  #10...'Hyd'
	  #20...'Sec'
	  #15...'Cyb'
	  #18...'Pune'

# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')#10 ... Hyd
#20 ... Sec
#15 ... Cyb
#18 ... Pune
#for  x , y   in  a . keys():
       #print(x , y , sep = ' ... ')
#for  x , y   in  a . values():
      # print(x , y , sep = ' ... ')
#for  x , y   in  a:
       #print(x , y , sep = ' ... ')

# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)#{10 : 20 , 30 : 40 , 50 : 60}
a . clear()#
print(a)#{}
del  a
#print(a)#


# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)#{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b)#False
print(a  ==  b)#True


#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)#10
print(y)#20
print(z)#15
print()#{}
x , y , z = a . values()
print(x)#'Rama'
print(y)#'Sita'
print(z)#'Rajesh'
print()#{}
x , y ,  z = a . items()
print(x)#(10 , 'Rama')
print(y)#(20 : 'Sita')
print(z)#(15 : 'Rajesh')
print()#{}
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)#{10 : 'Rama'}
print(rno2 , sname2)#{20 : 'Sita'}
print(rno3 , sname3)#{15 : 'Rajesh'}

# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)#{'R' , 'Red','G' , 'Gray','B' , 'Blue',Y' : 'Yellow',}
#a . update(b)

#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a)#error
#print(b)#error
c = [(10,) , (20,) , (30,)]
#b . update(c)
print(b)#{}

#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)#{0:0,1:1,2:8,3:27,4:64}
print(type(d))#{class'dict>}

# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)#{0:0,1:2,2:4,3:6,4:8}

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)#{15:'Sita',17:'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)#{10:'Rama',18:'Rajesh',12:'Rama Rao}


(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

Hint: Use  get()  method

s=input('enter string:').upper()
a={}
a['R']=a.get('R',0)+1
a['A']=a.get('A',0)+1
a['M']=a.get('M',0)+1
a['A']=a.get('A',0)+1
a['R']=a.get('R',0)+1
a['A']=a.get('A',0)+1
a['O']=a.get('O',0)+1
print(a)
