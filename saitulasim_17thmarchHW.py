# difference()   method  demo  program  
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)  # {10 , 20}
print(c)            # {10 , 20}
print(type(c))   # <class 'set'>
d = a - b     # {10 , 20}
print(d)      # {10 , 20}
print(type(d)) # <class 'set'>
print(c  is  d)  # False
print(c  ==  d)  # True


# symmetric_difference()   method  demo  program  
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)    #  {20 , 10 , 60 , 50}
print(type(c)) # <class 'set'>
d = a ^ b
print(d)     #  {20 , 10 , 60 , 50}
print(type(d))  # <class 'set'>
print(c   is   d)  # False
print(c  ==   d)   # True


# Find  outputs 
a = {x * x  for   x   in   range(10)}
print(a)    #  {0 , 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81}  i.e any order
print(type(a)) # <class 'set'>


'''Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
Let  input  be   Rama  Rao
 What  is  the  output  ? --->  Ram<space>o
Both  input  and  output  are  strings '''

string=input('enter string : ')
a=list(set(string))
print(''.join(a))



'''Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set
Let  input  be  RamA  Rao
 What  is  the  output  ?  ---> AO  (case  is  ignored) '''

string=input('enter string : ')
a=string.upper()
b=['A','E','I','O','U']
c=list(set(a))
out=[]
for x in c:
    if x in b:
        out.append(x)
print(''.join(out))


'''Write  a  program  to  remove  duplicate  elements  of   list  using  set
Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']
Both  input  and  output  are  lists '''

try:
    a=eval(input('enter list : '))
    b=set(a)
    print(list(b))
except:
    print("input should be list of elements")


#Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
#Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
#What  is  the  output ?  --->	[20 , 30 , 40]

try:
	a=eval(input("Enter list1 : "))
	b=eval(input("Enter list2 : "))

	c=set(a).intersection(set(b))
	print(list(c))
except:
	print("Input should be list")



#  How  to  access  values  of  dictionary 
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])  #print  value  25  in  dict  'a'
print(a['Ename'])   #print  'Rama Rao'  in  dict  'a'
print(a['Sal'])     #print  value  1000.65   in  dict  'a'


# How  to  modify  values  of  dictionary  
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)   #  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a))  # id of the a maybe 3353462355346
a['Sal']=2000    #How  to  modify  1000.65  to  2000
a['Ename']='Sita'  #How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno']=35      #How  to  modify  25   to  35
print(a)   #   {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}  
print(id(a)) #same id of the a maybe 3353462355346


#  How  to  append  key : value  pairs  to dictionary  
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)  #  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender'] = 'M'   #append  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = True  #append  'Married' :  True  to  dictionary  'a'
print(a)   #  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65 , 'Gender'  :  'M'  ,  'Married'  :  True} 


a = { }
a[10] = 'Rama'   #How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20] = 'Sita'    #How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15] = 'Rajesh'   #How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18] = 'Kiran'    #How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)   #  {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}


#  How  to  remove  key : value  pairs  of  dictionary  
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)  #  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
del a['Sal']  #How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)  #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'}


#  in  and  not  in  operators  
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())   # True
print(60  in  a . keys())   # False
print(60  in  a . values()) # True
print(30  in  a . values()) #  False
print(50  in  a)  # True
print(20  in  a)  # False
print(70  not  in  a . keys())  # False
print(40  not  in  a . values()) # False
print(25  not  in  a)  # True 


#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)   # '{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}' 
print(type(a))  # <class 'str'>
b = eval(a)    
print(b)  # {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # <class 'dict'>



#  Find  outputs  
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}  #  refernce b points to the new dict i.e {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(b)   #  {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)  #  False
print(a  ==  b)  #  True
c = a   # 'c' points the same dict where a points
print(a  is   c)  # True
print(a  ==  c)   #  True


#Find  outputs  
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)   # {10 , 15 , 14 , 25 , 20 , 18 , 19}
print(type(d)) # <class 'set'>
e = {**a , **b , **c} # {10 : 'Rama' , 20 : 'Manohar' , 15 : 'Radha' , 18 : 'Kiran' , 14 : 'Srinivas' , 25 : 'Ramesh' , 19 : 'Krishna'}
print(e)  # {10 : 'Rama' , 20 : 'Manohar' , 15 : 'Radha' , 18 : 'Kiran' , 14 : 'Srinivas' , 25 : 'Ramesh' , 19 : 'Krishna'}
print(type(e)) # <class 'dict'>


#  Find  outputs  
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b)  # error
c = {**a , **b} # {10 : 60 , 30 : 50}
print(c) # {10 : 60 , 30 : 50}
d = a | b  # in between dict
print(d) # {10 : 60 , 30 : 50}



#Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries
#Hint:  Append  each  emp  name  and  salary  to  dictionary  'a' 

n=int(input("number of employees : "))
a={}
for i in range(n):
    name=input("enter employE name : ")
    sal=float(input("Enter salary : "))
    a[name] = sal
print(a)


#Write  a  program  to  convert  a  string  to  dictionary
#Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

STR=eval(input("enter string : ")).split(',')
d=[]
e={}
for x in STR:
    c=x.split('=')
    d.append(c)
for i in d:
    e[i[0]] = i[1]
print(dict(e))


# len()  function  demo  program  
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))   #  3
b = {}
print(len(b))  # 0 


#  sum()  function demo  program  
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))  # 90
print(sum(a . values())) # 120
print(sum(a))  # 90
#print(sum(a . items())) # error

# max()  and  min()   functions  demo  program  
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))  # 40
print(min(a . keys()))  # 7
print(max(a . values())) # 50
print(min(a . values())) # 5
print(max(a . items()))  # (40 , 5)
print(min(a . items()))  #  (7 , 28)
print(max(a))  # 40
print(min(a))  # 7


#  dict()  function  demo program 
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)  # {'R' : 'Red' , 'G' : 'Green , 'B' : 'Blue' , 'G' : 'Grey'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e))  #  error
f = [[10] , [20] , [30]]
#print(dict(f))
#print(dict([10 , 20])) # error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))  # {10 : [20 , 30] , 40 : [50 , 60] , 70 : [80 , 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h)) # error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))  # {(10 , 20) : 30 , (40 , 50) : 60 , (70 , 80) : 90}



# sorted()  function  
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) # [5 , 10 , 15 , 18 ,20]
c = sorted(a . values())
print(c) # ['Blue' , 'Green' , 'Red' , 'White' , 'Yellow' ]
d = sorted(a . items())
print(d)  # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f)  # [20 , 18 , 15 , 10 , 5]
print(a) # {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}



#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)  # dict_keys([10 , 20 , 15 , 18])
print(type(b)) # <class 'dict_keys'>
for  x  in   b:
        print(x) 

# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values() #  dict_values(['Hyd' , 'Sec' , 'Cyb' , 'pune'])
print(b)     #  dict_values(['Hyd' , 'Sec' , 'Cyb' , 'pune'])
print(type(b)) # <class 'dict_values'>
for  x   in   b:
	print(x)  


#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)  # dict_items([(10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyd') , (18 , 'pune')])
print(type(b)) # <class 'dict_items'>
for  x   in   b:
        print(x) 
       # print(x , y , sep = ' ... ') 


# Find  outputs 
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')  
#for  x , y   in  a . keys():
       #print(x , y , sep = ' ... ')  # error becz no need to x and y 
#for  x , y   in  a . values():
      # print(x , y , sep = ' ... ')  # error
#for  x , y   in  a:          
      # print(x , y , sep = ' ... ')  # error


# clear()  method  demo  program 
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)  #  {10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a) # {}
del  a
#print(a) # error there is no a becz delete 'a'


# copy()  method demo  program 
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)  # {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) # False
print(a  ==  b) # True


#  Find  outputs  
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)  # 10
print(y)  # 20
print(z)  # 15
print()   # empty
x , y , z = a . values()
print(x)  # Rama
print(y)  # Sita
print(z)  # Rajesh
print()   # empty
x , y ,  z = a . items()
print(x)  # (10 , 'Rama')
print(y)  # (20 , 'Sita')
print(z)  # (15 , 'Rajesh')
print()   # empty
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)  # 10  Rama
print(rno2 , sname2)  # 20  Sita
print(rno3 , sname3)  # 15  Rajesh


# Find outputs 
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) #  {'Y' : 'Yellow', 'G' : 'Green' , 'R' : 'Red' , 'B' : 'Blue' }
print(b)  #  {'Y' : 'Yellow', 'G' : 'Green' , 'R' : 'Red' , 'B' : 'Blue' }
#a . update(b) # error list doesn't contain update method

#  Find  outputs  
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {} 
#b.update(a)# error
print(b)  # set()
c = [(10,) , (20,) , (30,)]
#b . update(c) # error
print(b)   # {}

#  Find  outputs 
d = {x : x ** 3   for    x   in  range(5)}
print(d)  # {0 : 0 , 1 : 1 , 2 : 8 , 3 : 27 , 4 : 64}
print(type(d)) # <class 'dict'>

# Find outputs   
d = { x :  2 * x    for    x   in   range(5) }
print(d)  # {0 : 0 , 1 : 2 , 2 : 4 , 3 : 6 , 4 : 8}


# Find outputs 
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # {15 :'Sita' , 17 : 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # 10 : 'Rama' , 18 : 'Rajesh' , 12 : 'Rama Rao'}


''' Write  a  program  to  sort  dictionary  wrt  keys 
Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}
Both  input  and  output  are  dictionaries
Hint:  Use  sorted()  function '''

a=eval(input('enter dict : '))
c={}
b=sorted(a.items())
for x in b:
    c[x[0]]=x[1]
print(c)
