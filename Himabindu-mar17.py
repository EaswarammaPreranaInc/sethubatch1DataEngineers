#prgm1
#difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)        #{10, 20}
print(type(c))  #<class 'set'>
d = a - b    
print(d)        #{10, 20}
print(type(d))  #<class 'set'>
print(c  is  d) #False
print(c  ==  d) #True

#prgm2
# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)          # {10, 50, 20, 60}
print(type(c)) <class 'set'>
d = a ^ b
print(d)          # {10, 50, 20, 60}
print(type(d))    # <class 'set'>
print(c   is   d) #False
print(c  ==   d)  #True

#prgm3
# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)  {x * x  for   x   in   range(1}
print(type(a))



#prgm4
#Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
a = "Rama Rao"
b = set(a)
c = ''.join(b)
print(c)



#prgm5
#Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set
a = "Rama Rao"
b = set()
c = ''
for i in a:
    if i not in b:
        c+= i
        b.add(i)
print(c)
#Output
Ram o

#prgm6
#Write  a  program  to  remove  duplicate  elements  of   list  using  set
a = [False, 25, 10.8, 1, 25, 0, 'Hyd', 10.8, 1.0, None, 'Sec', 'Hyd', True]
b = set(a)
c = list(b)
print(c)    #[False, 1, None, 10.8, 'Sec', 25, 'Hyd']

#prgm7
#Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
a = [10, 20, 30, 40, 50, 60]
b = [30, 40, 70, 80, 20]
c= list(set(a) & set(b))
print(c)  # Output: [20, 30, 40]

#prgm8
#  How  to  access  values  of  dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a['Empno'])  # 25
print(a['Ename'])  # Rama Rao
print(a['Sal'])    # 1000.65

#prgm9
# How  to  modify  values  of  dictionary 
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print("a:", a)
a['Sal'] = 2000       # Change 1000.65 to 2000
a['Ename'] = 'Sita'   # Change 'Rama Rao' to 'Sita'
a['Empno'] = 35       # Change 25 to 35
print("a:", a)

#prgm10
# Empty dictionary
a = {}
a[10] = 'Rama'     # Append 10: 'Rama'
a[20] = 'Sita'     # Append 20: 'Sita'
a[15] = 'Rajesh'   # Append 15: 'Rajesh'
a[18] = 'Kiran'    # Append 18: 'Kiran'
print(a)
#Output
{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

#prgm11
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print("a:", a)
del a['Sal']
print(("a:", a)
#Output
a: {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
a: {'Empno': 25, 'Ename': 'Rama Rao'}

#prgm12
#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())
print(60  in  a . keys())
print(60  in  a . values())
print(30  in  a . values())
print(50  in  a)
print(20  in  a)
print(70  not  in  a . keys())
print(40  not  in  a . values())
print(25  not  in  a)
#Output
True
False
True
False
True
False
False
False

#prgm13
#What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))

#prgm14
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)
print(a  is  b)
print(a  ==  b)
c = a
print(a  is   c)
print(a  ==  c)
#Output
{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
False
True
True
True

#prgm15
#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)
print(type(d))
e = {**a , **b , **c}
print(e)
print(type(e))
#Output
{10, 14, 15, 18, 19, 20, 25}
<class 'set'>
{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
<class 'dict'>

#prgm16
#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) #Error
c = {**a , **b}
print(c)
d = a | b
print(d)
#Output
{10: 60, 30: 50}
{10: 60, 30: 50}

#prgm17
#Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

#Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
# print(a + b) # + operator not supported
c = {**a , **b}
print(c) # {10:60,30:50}
d = a | b # | is used merge two dicts
print(d) # {10:60,30:50}

#prgm18
#Write  a  program  to  convert  a  string  to  dictionary
#prgm19
# len()  function  demo  program
#prgm20
#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))
print(sum(a . values()))
print(sum(a))
#print(sum(a . items()))
#Output
90
120
90

#prgm21
# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))
print(min(a . keys()))
print(max(a . values()))
print(min(a . values()))
print(max(a . items()))
print(min(a . items()))
print(max(a))
print(min(a))
#Output
40
7
50
5
(40, 5)
(7, 28)
40
7

#prgm22
#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e))
f = [[10] , [20] , [30]]
#print(dict(f))
#print(dict([10 , 20]))
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h))
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))
#Output
{10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
{'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
{10: [20, 30], 40: [50, 60], 70: [80, 90]}
{(10, 20): 30, (40, 50): 60, (70, 80): 90}

#prgm23
# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)
c = sorted(a . values())
print(c)
d = sorted(a . items())
print(d)
f  = sorted(a  , reverse = True)
print(f)
print(a)
#Output
[5, 10, 15, 18, 20]
['Blue', 'Green', 'Red', 'White', 'Yellow']
[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
[20, 18, 15, 10, 5]
{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

#prgm24
#Write  a  program  to  sort  dictionary  wrt  keys
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) #[5,10,15,18,20]
c = sorted(a . values())
print(c) #['Blue','Green','White','Red','Yellow']
d = sorted(a . items())
print(d)  # [(5:'White'),(10:'Red'),(15:'Blue'),(18:'Yellow'),(20:'Green')]
f  = sorted(a  , reverse = True)
print(f) # [20,18, 15,10,5]
print(a) # {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}


#prgm25
#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)
print(type(b))
for  x  in   b:
        print(x)
#Output
dict_keys([10, 20, 15, 18])
<class 'dict_keys'>
10
20
15
18

#prgm26
# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)
print(type(b))
for  x   in   b:
	print(x)
#Output
dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
<class 'dict_values'>
Hyd
Sec
Cyb
Pune

#prgm27
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)
a . clear()
print(a)
del  a #Error
print(a)
#Output
{10: 20, 30: 40, 50: 60}
{}
{}

#prgm28
# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b) #Error
#Output
{'R': 'Red', 'G': 'Green', 'B': 'Blue'}
False

#prgm29
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)
print(y)
print(z)
print()
x , y , z = a . values()
print(x)
print(y)
print(z)
print()
x , y ,  z = a . items()
print(x)
print(y)
print(z)
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)
print(rno2 , sname2)
print(rno3 , sname3)
#Output
10
20
15
Rama
Sita
Rajesh
(10, 'Rama')
(20, 'Sita')
(15, 'Rajesh')
10 Rama
20 Sita
15 Rajesh
























