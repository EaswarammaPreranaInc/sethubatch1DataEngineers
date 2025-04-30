# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) #{10,20}
print(type(c))# <class 'set'>
d = a - b
print(d)##{10,20}
print(type(d))# <class 'set'>
print(c  is  d)# Flase
print(c  ==  d)#True

# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10,20,50,60} any order
print(type(c))# <class 'set'>
d = a ^ b
print(d)#{10,20,50,60} any order
print(type(d))# <class 'set'>
print(c   is   d)#False
print(c  ==   d)#True

# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)#{0,1,4,9,16,25,36,49,81,64} any order
print(type(a))# <class 'set'>

# Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
x=input("Enter a sring : ")
b=set(x)
c=" ".join(b)
print(c)

#Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set
x=input("Enter a sring : ")
vowels = {'a', 'e', 'i', 'o', 'u'}
c=x.lower()
dist=set()
for x in c:
    if x in vowels:
        dist.add(x)
final=" ".join(dist).upper()
print(final)

#Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
s=eval(input("Enter a second list"))
v=eval(input("Enter a second list"))

set=s&v
lst=list(set)
print(lst)

# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a))# 20394 may be 
#How  to  modify  1000.65  to  2000
a['Sal']=2000

#How  to  modify  'Rama  Rao'  to  'Sita'
a['Ename']='Sita'
#How  to  modify  25   to  35
a['Empno']=35
print(a)#{'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  : 2000  }
print(id(a))# 20394 same as above printa

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
#How  to  append  'Gender' : 'M'  to  dictionary  'a'
list=[('Gender','m')]
a.update(list)
#How  to  append  'Married' :  True  to  dictionary  'a'
list=[('Married',True)]
a.update(list)
print(a)#{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'm', 'Married': True}

# Find  outputs (Home  work)
a = { }
'''
How  to  append  10 : 'Rama'  to  dictionary  'a'
How  to  append  20 : 'Sita'  to  dictionary  'a'
How  to  append  15 : 'Rajesh'  to  dictionary  'a'
How  to  append  18 : 'Kiran'  to  dictionary  'a'
'''
list=[(1,'Rama'),(20,'Sita'),(15,'Rajesh'),(18,'Kiran')]
a.update(list)
print(a)#{1: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
a.popitem()
print(a)#{'Empno'  :  25,  'Ename'  :  'Rama  Rao' }

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())#True
print(60  in  a . keys())#false
print(60  in  a . values())#True
print(30  in  a . values())#Flase
print(50  in  a)#True
print(20  in  a)#Flase
print(70  not  in  a . keys())#false
print(40  not  in  a . values())#flase
print(25  not  in  a)#True

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)#{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))#<class 'str'>
b = eval(a)
print(b)#{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b))#<class 'dict'>
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)#{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)# false
print(a  ==  b)#True
c = a
print(a  is   c)#True
print(a  ==  c)#true
#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)#{10, 14, 15, 18, 19, 20, 25}
print(type(d))#<class 'set'>
e = {**a , **b , **c}
print(e)#{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))#<class 'dict'>
# write a program to create a dictionary with emp names ans salaries
n=int(input("Enter how many employees : "))
c={}
for i in range(n):# loop executes upto the n
    ename=input("Enter ename :") # emp name input
    esal=input("Enter emp salary :")# emp salary input 
    c[ename]=esal # adding or updating to dictionary
print(c)

# write a program to convert a string to dictionary 
a=input("Enter string :")
b=a.split(",")
d={}
e=[]
for i in b:
    e.append(i.split("="))
d.update(e)
print(d)

# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))#3
b = {}
print(len(b))#0

#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))#90
print(sum(a . values()))#120
print(sum(a))#90
#print(sum(a . items())) # error
# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))#40
print(min(a . keys()))#7
print(max(a . values()))#50
print(min(a . values()))#5
print(max(a . items()))#(40,5)
print(min(a . items()))#(7,28)
print(max(a))#40
print(min(a))#7

#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)#
print(d)#{'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
#e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e)) # error ,inner loop must be 2 elements only
f = [[10] , [20] , [30]]
#print(dict(f))
#print(dict([10 , 20]))# error ,inner loop must be 2 elements only
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))#{10: [20, 30], 40: [50, 60], 70: [80, 90]}
#h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h))# error , key always single element 
#i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
#print(dict(i))## error , key always single element

# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)#[5, 10, 15, 18, 20]
c = sorted(a . values())
print(c)#['White','Red' , 'Blue' ,'Yellow' ,'Green']
d = sorted(a . items())
print(d)#[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f)#[20, 18, 15, 10, 5]
print(a)#{10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}

#Write  a  program  to  sort  dictionary  wrt  keys 
x=eval(input("Enter adictionary : "))
print(sorted(x.keys()))

#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)#[10,20,15,18]
print(type(b))#<class 'dict_keys">
for  x  in   b:
        print(x)#10 <nextlilne> 20 <nextlilne> 15 <nextlilne> 18 <nextlilne>

# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)#['hyd','sec','cyb','pune']
print(type(b))#<class 'dict_values">
for  x   in   b:
	print(x)# Hyd <nextlilne> Sec <nextlilne> Cyb <nextlilne> Pune <nextlilne>

# Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

x=input("Enter a String : ")
x=x.upper()
b=sorted(x)
c={}
for i in b:
    if i.isalpha():
        c[i]=c.get(i,0)+1
print(c)

#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)#[(10 ,'Hyd'),(20 ,'Sec'),(15 ,'Cyb'),(18 ,'Pune')]
print(type(b))#<class "dict_items">
for  x   in   b:
        print(x)#(10, 'Hyd')<next line>20 ,'Sec')<next line>(15 ,'Cyb')<next line>(18 ,'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ')#10 ... Hyd <next line>20 ... Sec<next line> 15 ... Cyb<next line> 18 ... Pune
