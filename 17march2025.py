# difference()   method  demo  program  (Home  work)
'''
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)# returns the elements that which are in set a that are not in set b 
print(c)#{10,20}
print(type(c))#<class'set'>
d = a - b
print(d)#{10,20}
print(type(d))#<class 'set'>
print(c  is  d)# false
print(c  ==  d) # true
'''

# symmetric_difference()   method  demo  program  (Home  work)
'''
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)#{10,20,50,60}
print(c)#{10,20,50,60}
print(type(c))# <class 'set'>
d = a ^ b
print(d)# {10,20,50,60}
print(type(d))#<class 'set'>
print(c   is   d)#false
print(c  ==   d)#true

'''
# Find  outputs  (Home  work)
'''
a = {x * x  for   x   in   range(10)}
print(a)# {0,1,4,25,36,49,64,81}
print(type(a))#<class 'set'>
'''


# Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
'''
1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  ---> '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'

a=set(input("enter the string : "))
b=set(''.join(a))
print(b)
'''


'''
List
----
insertion --->  append() , extend() , insert()
deletion  --->  pop() , remove() , clear()
modification  --->  sort() , reverse()
Access  --->  index() , count() , copy()
----------------------------------------------------
set
----
insertion --->  add() , update()
deletion  --->  pop() , remove() ,  discard() , clear()
Set  theory  --->  union() , intersection() , difference() , symmetic_difference()
Access  --->   copy()
'''


# Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set
'''
1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes

a={'a','e','i','o','u'}
b=set(input("enter the string input : ").lower())
print(a & b)
'''



# Write  a  program  to  remove  duplicate  elements  of   list  using  set
'''
1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists


print(list(set(eval(input("enter the list : ")))))
'''

# Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
'''
1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
'''
print(list((set(eval(input("enter the 1st list : ")))).intersection(set(eval(input("enter the 2nd list : "))))))
'''

#  How  to  access  values  of  dictionary (Home  work)
'''
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a.get('Empno'))
print(a.get("Ename"))
print(a.get("Sal"))
'''


# How  to  modify  values  of  dictionary  (Home  work)
'''
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['Sal']=20000
a['Ename']='Sita'
a['Empno']=35
print(a)
print(id(a))
'''

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
'''
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.update({'Gender' : 'M'})
a['Married']=True
print(a)
'''

# Find  outputs (Home  work)
'''
a = { }
a.update({10 : 'Rama'})
a[20] = 'Sita'
a.update({15 : 'Rajesh'})
a[18] ='Kiran'
print(a)
'''


#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
'''
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
del a['Sal']
print(a)
'''

#  in  and  not  in  operators  (Home  work)
'''
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())# true
print(60  in  a . keys())# false
print(60  in  a . values())# true
print(30  in  a . values())# false
print(50  in  a)# true
print(20  in  a)# false
print(70  not  in  a . keys())# false
print(40  not  in  a . values())# false
print(25  not  in  a)# true
'''


#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
'''
a = input('Enter  dictionary  :  ')
print(a)# '{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'
print(type(a))# <class 'str'>
b = eval(a)# removes quotes
print(b)# {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b))# <class 'dict'>
'''

#  Find  outputs  (Home  work)
'''
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} # copies a dict to b
print(b)# {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)# false
print(a  ==  b)# true
c = a
print(a  is   c)# true
print(a  ==  c)# true
'''


#Find  outputs  (Home  work)
'''
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)#{10:'Rama',20:'Manohar',15:'Radha',18:'Kiran',14:'Srinivas',25:'Ramesh',19:'Krishna'}
print(type(d))# <class 'dict'>
e = {**a , **b , **c}
print(e)
print(type(e))# <class 'dict'>
'''

#  Find  outputs  (Home  work)
'''
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b)# error
c = {**a , **b}
print(c)# {10:60,30:50}
d = a | b
print(d)# {10:60,30:50}
'''

# Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

# Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
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
'''
'''
a=int(input("enter the number of employess you want to add : "))
g={}
b,c=[],[]
for i in range(0,a):
    b.append(input("enter the employee name :"))
    for j in range(0,1):
        c.append(eval(input("enter the salary of the employee :")))
for i in range(0,len(b)):
    g.update({b[i]:c[i]})
print(g)
'''

# Write  a  program  to  convert  a  string  to  dictionary
'''
Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''
'''
a=(input("enter the keys and values : ").split(','))
b=[]
for i in a:
    b.append(i.split('='))
print(dict(b))
'''
'''
for i in b:
    for j in i:
        c.append((j))
for i in range(0,len(c),2):
    for j in range(1,len(c),2):
        d.update({(c[i]):(c[j])})
print(d)
'''
'''
c=[]
for i in a:
    c.append(str(i).replace('=',':'))
print(set(c))
'''

# len()  function  demo  program  (Home  work)
'''
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))#3
b = {}#empty dictonary
print(len(b))#0
'''


# What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary

#  sum()  function demo  program  (Home  work)
'''
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))# 90
print(sum(a . values()))# 120
print(sum(a)) # 90
print(sum(a . items())) # error becz all the items are in the from of tuple tuple addition not possible
'''
# max()  and  min()   functions  demo  program  (Home  work)
'''
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))# 40
print(min(a . keys()))# 7
print(max(a . values()))# 50
print(min(a . values()))# 5
print(max(a . items()))# {40:5} in dict the first preferance is keys if not mentinoed specially values
print(min(a . items()))# {7:28}
print(max(a))# 40
print(min(a))# 7
'''

#  dict()  function  demo program (Home  work))
'''
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Gray'] , ['B' , 'Blue'] )
d = dict(c)
print(d)# {'R':'Red','G':'Green' , 'B':'Blue'] ,'G':'Gray'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e))# error becz items are in tuple
f = [[10] , [20] , [30]]
print(dict(f))# error becz items are in tuple
print(dict([10 , 20]))# error becz the values are immutable
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))# {10:(20,30),40:(50,60),70:(80,90)}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h))#error becz keys are must be immutable
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))# {(10 , 20) : 30 , (40 , 50) : 60 , (70 , 80) : 90}
'''

# sorted()  function  (Home  work)
'''
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)# [5,10,15,18,20]
c = sorted(a . values())
print(c)# ['blue','green','red','white','yellow']
d = sorted(a . items())
print(d)# [(5,'white'),(10,'red'),(15,'blue'),(18,'yellow'),(20,'green')]
f  = sorted(a  , reverse = True)
print(f)# [20, 18, 15, 10, 5]
print(a)# {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
'''


# Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)
'''
1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function

4) a = {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    b = sorted(a . items())  --->  [(5 , 'D' ) , (10 , 'A') , (12 , 'E') , (15 , 'C') , (20, 'B')]
    dict(b)  --->  {5 : 'D' , 10 : 'A' , .....}

Enter  dictionary  :  {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}
'''

'''
print(dict(sorted(eval(input("enter the dictonary : ")).items())))
'''

#  keys()  method  demo  program
'''
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) #dict_keys([10,20,15,18])
print(type(b))# <class 'dict_keys'>
for  x  in   b:
        print(x)
'''
'''
10
20
15
18
'''


# What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys

# values()  method  demo  program
'''
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)# dict_values(['hyd','sec','cyb','pune'])
print(type(b))# <class 'dict_values'>
for  x   in   b:
	print(x)
#'hyd'
# 'sec'
# 'cyb'
# 'pune'

'''

# What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values

#  items()  method  demo  program
'''
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)#dict_items([(10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (18 , 'Pune')])
print(type(b))# <class 'dict_items'>
for  x   in   b:
        print(x)#(10 , 'Hyd') 
                #(20 , 'Sec')  
                #(15 , 'Cyb')
                #(18 , 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ')
#10 ... 'Hyd'
#20 ... 'Sec'  
#15 ... 'Cyb'
#18 ... 'Pune'
'''

 # Find  outputs (Home  work)
'''
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')
                #10 ...'Hyd'
                #20 ... 'Sec'  
                #15 ... 'Cyb'
                #18 ... 'Pune'
for  x , y   in  a . keys():#error
       print(x , y , sep = ' ... ')
for  x , y   in  a . values():#error
       print(x , y , sep = ' ... ')
for  x , y   in  a:#error
       print(x , y , sep = ' ... ')
'''

# clear()  method  demo  program (Home  work)
'''
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)#{10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a)#{}
del  a
print(a)#erroe
'''
# copy()  method demo  program  (Home  work)
'''
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)# {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b)# false
print(a  ==  b)# true
'''

#  Find  outputs  (Home  work)
'''
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)# 10
print(y)# 20
print(z)# 15
print()# new line
x , y , z = a . values()
print(x)# rama
print(y)# sita
print(z)# rajesh
print()# new line
x , y ,  z = a . items()
print(x)#(10 , 'Rama')
print(y)#(20 , 'Sita')
print(z)#(15 , 'Rajesh')
print()# new line
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)#10  'Rama'
print(rno2 , sname2)#20  'Sita'
print(rno3 , sname3)#15  'Rajesh'
'''

# Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)
'''
Let  input  be   RamA raO
What  is  the  output ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

Hint: Use  get()  method


1) a = { }

2) a['R'] = a . get('R' , 0) + 1 = 0 + 1 = 1
    What  does  a['R']  =  1  do ?  ---> Appends  'R' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  ---> {'R' : 1}

3) a['A'] = a . get('A' , 0) + 1 =  0 + 1 = 1
    What  does  a['A']  =  1  do ?  ---> Appends  'A' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  ---> {'R' : 1 , 'A' : 1}

4) a['M'] = a . get('M' , 0) + 1 =  0 + 1 = 1
    What  does  a['M']  =  1  do ?  --->  Appends  'M' : 1  to  dict…

Enter  mixed  case  string : RamA raO
{'A': 3, 'M': 1, 'O': 1, 'R': 2}


a=input("enter the string input : ")
b={}
for i in a:
    b.update({i:a.count(i)})
print(b)
'''

# Find outputs (Home  work)
'''
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)#{'Y' : 'Yellow', 'G' : 'Green','R' , 'Red' , 'B' , 'Blue'}
a . update(b)# error
'''
#  Find  outputs  (Home  work)
'''
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)#error a consisits of 3 elements 
print(b)
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b)# error
'''
'''
#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))#<class 'dict'>
# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)#{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
'''
# Find outputs  (Home  work)
'''
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)#{15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)#{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}
'''