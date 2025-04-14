# difference()   method  demo  program  (Homework)
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a . difference(b)  # Returns a set with elements of set 'a' which are not in 'b'
print(c)  # {10,20}
print(type(c))  # <class 'set'>
d = a - b  # Returns a set with elements of set 'a' which are not in 'b'
print(d)  # {10,20}
print(type(d))  # <class 'set'>
print(c is d)  # False because c and d points to different sets
print(c == d)  # True because elements of the sets are same

'''  OUTPUT
{10, 20}
<class 'set'>
{10, 20}
<class 'set'>
False
True

'''


# symmetric_difference()   method  demo  program  (Homework)
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a . symmetric_difference(b)  # Returns a set with all the elements of set 'a' and 'b' without duplicate elements
print(c)  # {10,20,30,40,50,60}
print(type(c))  # <class 'set'>
d = a ^ b  # Returns a set with all the elements of set 'a' and 'b' without duplicate elements
print(d)  # {10,20,30,40,50,60}
print(type(d))  # <class 'set'>
print(c is d)  # False because ref 'c' and 'd' points to different sets
print(c == d)  # True because elements are the sets are same

'''  OUTPUT
{10, 50, 20, 60}
<class 'set'>
{10, 50, 20, 60}
<class 'set'>
False
True

'''



# Find  outputs  (Homework)
a = {x * x for x in range(10)}
print(a)  # {0,1,4,9,16,25,36,49,64,81}
print(type(a))  # <class 'set'>

'''   OUTPUT
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
<class 'set'>
'''


'''
(Homework)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  ---> '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but not 'Hyd'
'''

a=input('Enter a string : ')
a=set(a.upper())
print(a)
result=''.join(a)
print(result)

'''   Sample Output
Enter a string : Rama Rao
{'R', 'O', 'M', ' ', 'A'}
ROM A

'''



'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor changes
'''
a='RamA Rao'
a=set(a.upper())
b=set('AEIOU')
c=a.intersection(b)
d=''.join(c)
print(c)
print(d)

'''  OUTPUT
{'A', 'O'}
AO

'''


'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output are lists
'''
a=[False, 25, 10.8, 1, 25, 0, 'Hyd', 10.8, 1.0, None, 'Sec', 'Hyd', True]
a=set(a)
print(a)

'''   OUTPUT
{False, 1, 10.8, 'Hyd', 25, 'Sec', None}
'''



'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output are lists
'''

a=[10 , 20 , 30 , 40 , 50 , 60]
b=[30 , 40 , 70 , 80 , 20]
a=set(a)
b=set(b)
c=a.intersection(b)
print(c)

'''   OUTPUT
{40, 20, 30}
'''



#  How  to  access  values  of  dictionary (Homework)
a ={'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])  # How  to  print  value  25  in  dict  'a' --> 25
print(a['Ename'])  # How  to  print  'Rama Rao'  in  dict  'a' --> 'Rama Rao'
print(a['Sal'])  # How  to  print  value  1000.65 in dict 'a' --> 1000.65

'''  OUTPUT
25
Rama  Rao
1000.65

'''


# How  to  modify  values  of  dictionary  (Homework)
a={'Empno':  25,  'Ename':  'Rama  Rao',  'Sal':  1000.65}
print(a)  # {'Empno':  25,  'Ename':  'Rama  Rao',  'Sal':  1000.65}
print(id(a))  # Address of the object 'a'
a['Sal']=2000  # How  to  modify  1000.65  to  2000
a['Ename']='Sita'  # How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno']=35  # How  to  modify  25   to  35
print(a)  # {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a))  # Same Address

'''    OUTPUT
{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
2456776522752
{'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
2456776522752

'''


#  How  to  append  key : value  pairs  to dictionary  (Homework)
a={'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65 }
print(a)  # {'Empno : 25,Ename:'Rama Rao','Sal':1000.65}
a['Gender']='M'  # How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married']=True  # How  to  append  'Married' :  True  to  dictionary 'a'
print(a)  # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}

'''    OUTPUT
{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}
'''


# Find  outputs (Homework)
a = { }
a[10]='Rama'  # How  to  append  10 : 'Rama'  to  dictionary  'a' --> {10:'Rama'}
a[20]='Sita'  # How  to  append  20 : 'Sita'  to  dictionary  'a' --> {10:'Rama',20:'Sita'}
a[15]='Rajesh'  # How  to  append  15 : 'Rajesh'  to  dictionary  'a' --> {10:'Rama',20:'Sita',15:'Rajesh'}
a[18]='Kiran'  # How  to  append  18 : 'Kiran'  to  dictionary 'a' --> {10:'Rama',20:'Sita',15:'Rajesh',18:'Kiran'}
print(a)  # {10:'Rama',20:'Sita',15:'Rajesh',18:'Kiran'}

'''   OUTPUT
{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
'''


#  How  to  remove  key : value  pairs  of  dictionary  (Homework)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)  # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
del a['Sal']  # How  to  remove  'Sal' : 1000.65  from  dictionary 'a'
print(a)  # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'}

'''  OUTPUT
{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
{'Empno': 25, 'Ename': 'Rama  Rao'}

'''


#  in  and  not  in  operators  (Homework)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())  # True
print(60  in  a . keys())  # False
print(60  in  a . values())  # True
print(30  in  a . values())  # False
print(50  in  a)  # True
print(20  in  a)  # False
print(70  not  in  a . keys())  # False
print(40  not  in  a . values())  # False
print(25 not in a)  # True

'''    OUTPUTS
True
False
True
False
True
False
False
False
True

'''


#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)  # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))  # <class 'str'>
b = eval(a)  # converts string to set
print(b)  # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b))  # <class 'set'>

'''   OUTPUT
Enter  dictionary  :  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
<class 'str'>
{10: 'A', 20: 'D', 15: 'C'}
<class 'dict'>

'''


#  Find  outputs  (Homework)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}  # Unpacks dictionary to form a new dictionary with same key:value pairs
print(b)  # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)  # False because ref 'a' and 'b' points to different dictionaries
print(a  ==  b)  # True because same key:value pairs in both dictionaries
c = a  # ref 'c' points to 'a'
print(a  is  c)  # True because ref 'a' and 'c' points to same dictionary
print(a == c)  # True because same key:value pairs in both dictionaries

'''   OUTPUT
{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
False
True
True
True

'''



#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}  # unpacks dictionaries to forma set of keys
print(d)  # {10,20,15,18,14,25,19}
print(type(d))  # <class 'set'>
e = {**a , **b , **c}  # unpacks dictionaries to form a new dictionaries with same key:value pairs and concatenate all the dictionaries
print(e)  # {10:'Rama',20:'Manohar',15:'Radha',18:'Kiran',14:'Srinivas',25:'Ramesh',19:'Krishna'}
print(type(e))  # <class 'dict'>

'''   OUTPUT 
{10, 14, 15, 18, 19, 20, 25}
<class 'set'>
{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
<class 'dict'>

'''


#  Find  outputs  (Homework)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
# print(a + b)  # Errror because by using + operator we can not concatenate two dictionaries
c = {**a , **b} # concatenate two dictionaries and return new dictionary
print(c)  # {10:60,30:50}
d =a|b # concatenate two dictionaries and return new dictionary
print(d)  # {10:60,30:50}

'''
{10: 60, 30: 50}
{10: 60, 30: 50}
'''



'''
(Homework)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary 'a'
'''
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

a = {}
a['AAA'] = 10000  --->   {'AAA': 10000}
a['BBB'] = 20000  --->   {'AAA': 10000 , 'BBB':20000}
'''
a=eval(input('How many employees : '))
b={}
for i in range(0,a):
    empname=eval(input('Enter Emp Name :'))
    salary=eval(input('Enter Salary : '))
    b[f'{empname}']=salary
print(b)

'''   Sample Output
How many employees : 2
Enter Emp Name :'A'
Enter Salary : 10
Enter Emp Name :'B'
Enter Salary : 20
{'A': 10, 'B': 20}

How many employees : 4
Enter Emp Name :'AAA'
Enter Salary : 10000
Enter Emp Name :'BBB'
Enter Salary : 20000
Enter Emp Name :'CCC'
Enter Salary : 30000
Enter Emp Name :'DDD'
Enter Salary : 40000
{'AAA': 10000, 'BBB': 20000, 'CCC': 30000, 'DDD': 40000}

'''


''' (Homework)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''

a = "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
b = a.split(",")
print(b)  # ['Emp no = 25 ', ' Emp name = Rama  Rao ', ' sal = 10000.0 ', ' gender = m']
c={}
for i in b:
 x,y=i.split("=")
 c.update({x:y})
print(c)  # {'Emp no ': ' 25 ', ' Emp name ': ' Rama  Rao ', ' sal ': ' 10000.0 ', ' gender ': ' m'}

'''   Sample Output
['Emp no = 25 ', ' Emp name = Rama  Rao ', ' sal = 10000.0 ', ' gender = m']
{'Emp no ': ' 25 ', ' Emp name ': ' Rama  Rao ', ' sal ': ' 10000.0 ', ' gender ': ' m'}

'''



# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))  # 3
b = {}  # Empty dict
print(len(b))  # 0

'''  OUTPUT
3
0

'''


#  sum()  function demo  program  (Homework)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))  # 90
print(sum(a . values()))  # 120
print(sum(a))  # 90
# print(sum(a.items()))  # Error due to int and string values

'''  OUTPUT
90
120
90

'''


# max()  and  min()   functions  demo  program  (Homework)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))  # 40
print(min(a . keys()))  # 7
print(max(a . values()))  # 50
print(min(a . values()))  # 5
print(max(a . items()))  # (40,5)
print(min(a . items()))  # (7,28)
print(max(a))  # 40
print(min(a))  # 7

'''   OUTPUT
40
7
50
5
(40, 5)
(7, 28)
40
7

'''


#  dict()  function  demo program (Homework))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)  # converts list of tuple to dict
print(d)  #
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
# print(dict(e))  # Error because there is 3 arguments
f = [[10] , [20] , [30]]
# print(dict(f))  # Error because there is only one argument
# print(dict([10 , 20])) # Error can not convert to dictionary
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))  # {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
# print(dict(h)) # Error due to nested list
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))  # {(10, 20): 30, (40, 50): 60, (70, 80): 90}

'''   OUTPUT
{10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
{'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
{10: [20, 30], 40: [50, 60], 70: [80, 90]}
{(10, 20): 30, (40, 50): 60, (70, 80): 90}

'''


# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)  # [5,10,15,18,20]
c = sorted(a . values())
print(c)  # ['Blue','Green','Red','White','Yellow']
d = sorted(a . items())
print(d)  # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f)  # {20,18,15,10,5}
print(a)  # {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}

'''   OUTPUT
[5, 10, 15, 18, 20]
['Blue', 'Green', 'Red', 'White', 'Yellow']
[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
[20, 18, 15, 10, 5]
{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

'''


'''
Gift
Write  a  program  to  sort  dictionary  wrt  keys  (Homework)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function

4) a = {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    b = sorted(a . items())  --->  [(5 , 'D' ) , (10 , 'A') , (12 , 'E') , (15 , 'C') , (20, 'B')]
    dict(b)  --->  {5 : 'D' , 10 : 'A',.....}
'''
a=eval(input('Enter a dictinary : '))
b=sorted(a.items())
c=dict(b)
print(c)

'''   Output
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}

'''



#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()  # Returns dict_keys object which has the list of all dictionary keys
print(b)  # dict_keys([10,20,15,18])
print(type(b))  # <class 'dict_keys'>
for  x  in   b:
        print(x)  # 10 <nextline> 20 <nextline> 15 <nextline> 18

'''   OUTPUT
dict_keys([10, 20, 15, 18])
<class 'dict_keys'>
10
20
15
18

'''


# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()  # Returns dict_values object which has the list of all dictionary values
print(b)  # dict(['Hyd','Sec','Cyb','Pune'])
print(type(b))  # <class 'dict_values'>
for  x   in   b:
	print(x)  # 'Hyd' <nextline> 'Sec' <nextline> 'Cyb' <nextline> 'Pune'

'''   OUTPUT
dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
<class 'dict_values'>
Hyd
Sec
Cyb
Pune

'''


#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()  # Returns dict_items object which has the list of tuples
print(b)  # dict_items([(10,'Hyd'),(20,'Sec'),(15,'Cyb'),(18,'Pune')])
print(type(b))  # <class 'dict_items'>
for  x   in   b:
        print(x)  # (10,'Hyd') <nextline> (20,'Sec') <nextline> (15,'Cyb') <nextline> (18,'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ')  # (10...'Hyd') <nextline> (20...'Sec') <nextline> (15...'Cyb') <nextline> (18...'Pune')

'''  OUTPUT
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

'''


# Find  outputs (Homework)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():  # Returns dict_items object which has the list of tuples
       print(x , y , sep = ' ... ')  # (10...'Hyd') <nextline> (20...'Sec') <nextline> (15...'Cyb') <nextline> (18...'Pune')
# for  x , y   in  a . keys():  # Error because there are more arguments to unpack
#        print(x , y , sep = ' ... ')
# for  x , y   in  a . values():  # Error because there are more arguments to unpack
#       print(x , y , sep = ' ... ')
# for  x , y   in  a:   # Error because loop run over only on keys so it throws error
#       print(x , y , sep='...')

'''   OUTPUT
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune

'''


# clear()  method  demo  program (Homework)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)  # {10:20,30:40,50:60}
a . clear()  # removes all key:value pairs from the dictionary
print(a)  # empty dictionary {}
del a #  deletes the dictionary
# print(a)  # Error because 'a' dictionary not exsists

'''   OUTPUT
{10: 20, 30: 40, 50: 60}
{}

'''


# copy()  method demo  program  (Homework)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()  # copies the key:value pairs from ref 'a' to 'b'
print(b)  # {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b)  # False because ref 'a' and 'b' points to different dictionaries
print(a==b)  # True because both dictionaries have same key:value pairs

'''   OUTPUT
{'R': 'Red', 'G': 'Green', 'B': 'Blue'}
False
True

'''


#  Find  outputs  (Homework)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()  # unpacks keys from the dictionary into 3 elements
print(x)  # 10
print(y)  # 20
print(z)  # 15
print()  # Empty space
x , y , z = a . values()  # unpacks values from dictionary into 3 elements
print(x)  # 'Rama'
print(y)  # 'Sita'
print(z)  # 'Rajesh'
print()  # Empty space
x , y ,  z = a . items()  # unpacks the dictionary of key:value pairs to tuples into 3 elements
print(x)  #  (10,'Rama')
print(y)  # (20,'Sita')
print(z)  # (!5,'Rajesh')
print()  # Empty space
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)  # 10 'Rama'
print(rno2 , sname2)  # 20 'Sita'
print(rno3 , sname3)  # 15 'Rajesh'

'''    OUTPUT
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

'''


'''
(Homework)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

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
    What  does  a['M']  =  1  do ?  --->  Appends  'M' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 1 , 'A' : 1 , 'M' : 1}

5) a['A'] = a . get('A' , 0) + 1 = 1 + 1 = 2
    What  does  a['A']  =  2  do ?  --->  Modifies  value  of  'A'  to  2  in dict  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 1 , 'A' : 2 , 'M' : 1}

6) a['R'] = a . get('R' , 0) + 1 =  1 + 1 = 2
    What  does  a['R']  =  2  do ?  ---> Modifies  value  of  'R'  to  2  in dict  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 2 , 'A' : 2 , 'M' : 1}

7) a['A'] = a . get('A' , 0) + 1 =  2 + 1 = 3
    What  does  a['A']  =  3  do ?  ---> Modifies  value  of  'A'  to  3  in dict  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 2 , 'A' : 3 , 'M' : 1}

8) a['O'] = a . get('O' , 0) + 1 =  0 + 1 = 1
    What  does  a['O']  =  1  do ?  --->  Appends  'O' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 2 , 'A' : 3 , 'M' : 1 , 'O' : 1}

9) Finally  what   is  dict  'a' ?  --->  {'R' : 2 , 'A' : 3 , 'M' : 1 , 'O' : 1}
'''
a=input('Enter a string : ')
b=a.upper()
c={}
for i in b:
    if i!=' ':
        c[i]=c.get(i,0)+1
print(c)

'''   OUTPUT
Enter a string : RamA raO
{'R': 2, 'A': 3, 'M': 1, 'O': 1}

'''


# Find outputs (Homework)
a = [('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)  # Appends elements of inner sequence to dictionary b in the form of key:value pairs
print(b)  # {'Y':'Yellow','G':Green,'R':'Red','B':'Blue'}
# a.update(b) # Error because list does not contain update() method

'''  OUTPUT
{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}

'''


#  Find  outputs  (Homework)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
# b.update(a)  # Error due to 3 arguments
print(b)
c = [(10,) , (20,) , (30,)]
# b . update(c)  # Error due to single argument
print(b)

'''   OUTPUT
{}
{}
'''


#  Find  outputs (Homework)
d = {x : x ** 3   for    x   in  range(5)}
print(d)  # {0:0,1:1,2:8,3:27,4:64}
print(type(d))  # <class 'dict>

'''  OUTPUT
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
<class 'dict'>

'''


# Find outputs   (Homework)
d = { x :  2 * x    for    x   in   range(5)}
print(d)  # {0:0,1:2,2:4,3:6,4:8}

'''  OUTPUT
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

'''


# Find outputs  (Homework)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)  # {15:'Sita',17:'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)  # {10:'Rama',18:'Rajesh',12:'Rama Rao'}

'''  OUTPUT
{15: 'Sita', 17: 'Kiran'}
{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}

'''



