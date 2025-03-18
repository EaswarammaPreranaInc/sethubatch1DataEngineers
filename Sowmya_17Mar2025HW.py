
# 1. difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) # {10,20}
print(type(c)) # class set
d = a - b
print(d) # {10,20}
print(type(d)) # class set 
print(c  is  d) # False
print(c  ==  d) # TRue 


'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->
										Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''

#  2. symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) # {10,20,50,60}
print(type(c)) #class set 
d = a ^ b
print(d) #  {10,20,50,60}
print(type(d)) # class set 
print(c   is   d) # False
print(c  ==   d) # True 



'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'
						                                                              without  common  elements
																					  i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . symmetric_difference(b) ?  --->  a ^ b

4) Is  set ^ list  valid ?  --->  No  becoz  operands  of  ^  operator  should  be  sets  only
''' 
# 3. Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) #  {0 ,1 ,4, 9,  16, 25, 36, 49, 64,  81 }
print(type(a)) # class set

'''
4. (Home  work)
3. Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  ---> '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''
 
a = eval(input(" Enter a string :" ))
b=set(a)
print(''.join(b))

'''
5.Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
''' 
a = eval(input(" Enter a string :" ))
b=set(a.upper())
for x in b:
	if x in 'AEIOU':
		print(x)
'''
6. Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
''' 
a = eval(input(" Enter a list with duplicate elements :" ))
b=set(a)
print(list(b))

''' 
7. Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output  are  lists
''' 
a = eval(input(" Enter a list :" ))
b = eval(input(" Enter a list :" ))
print(list(set(a)&set(b)))

# 8. How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno']) #(How  to  print  value  25  in  dict  'a')
print(a['Ename']) #(How  to  print  'Rama Rao'  in  dict  'a')
print(a['Sal'])  #(How  to  print  value  1000.65   in  dict  'a')

# 9. How  to  modify  values  of  dictionary  (Home  work)  
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # address of object a
a['Sal']=2000
#How  to  modify  1000.65  to  2000
a['Ename']='Sita'
#How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno']=35
#How  to  modify  25   to  35
print(a) # {'Empno':35,'Ename':'Sita','Sal':2000}
print(id(a)) # Same address

# 10. How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender']='M'
a['Married']=True
#How  to  append  'Gender' : 'M'  to  dictionary  'a'
#How  to  append  'Married' :  True  to  dictionary  'a'
print(a) #  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65 ,  'Gender' : 'M' , 'Married' :  True }

# 11. Find  outputs (Home  work)
a = { }
'''How  to  append  10 : 'Rama'  to  dictionary  'a'
How  to  append  20 : 'Sita'  to  dictionary  'a'
How  to  append  15 : 'Rajesh'  to  dictionary  'a'
How  to  append  18 : 'Kiran'  to  dictionary  'a' '''
a[10]='Rama'
a[20]='Sita'
a[15]='Rajesh'
a[18]='Kiran'
print(a)

# 12. How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)#  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
del a['Sal']
#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao'}

# 13. in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) #True
print(60  in  a . keys()) #F
print(60  in  a . values())#T
print(30  in  a . values())#F
print(50  in  a)#T
print(20  in  a)#F
print(70  not  in  a . keys())#F
print(40  not  in  a . values())#F
print(25  not  in  a)#T  

# 14. What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) # '{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'
print(type(a)) #Class <Str>
b = eval(a) 
print(b) #{10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # Class<Dict>

# 15. Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) # FAlse
print(a  ==  b) # True
c = a
print(a  is   c) # True 
print(a  ==  c) # True 

# 16. Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d) # {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # Class set
e = {**a , **b , **c}
print(e) # {10 : 'Rama' , 20 :  'Manohar' , 15 : 'Radha',18 : 'Kiran' , 14 : 'Srinivas' ,25 : 'Ramesh' , 19 : 'Krishna' }
print(type(e)) # Class Dict 

# 17.  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
# print(a + b) # + operator not supported
c = {**a , **b}
print(c) # {10:60,30:50}
d = a | b # | is used merge two dicts
print(d) # {10:60,30:50}

'''
(Home  work)
18. Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

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
{AAA:10000 .....}

a = {}
a['AAA'] = 10000  --->   {'AAA': 10000}
a['BBB'] = 20000  --->   {'AAA': 10000 , 'BBB' : 20000}
''' 
D={}
a=eval(input("How many Employees : "))
for x in range(a):
	b=eval(input("Enter Emp Name : "))
	c=eval(input("Enter Sal : "))
	D[b]=c
print(D)

''' *19. (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice


a =  "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
b = ['Emp no = 25' , 'Emp name = Rama  Rao' , 'sal = 10000.0' , 'gender = m']
c = {}
x =  'Emp no = 25'  --->  ['Emp  no' , '25']  ---> {'Emp  no': '25'}
x = 'Emp name = Rama  Rao'  --->  ['Emp name' , 'Rama  Rao']  --->  {'Emp  no': '25' , 'Emp  name': 'Rama Rao'}} ''' 



a= input("Enter a string with Emp no. = ' ' in this format : " )
b=a.split(',')
c={}
for x in b:
	d=x.split('=')
	c[d[0]]=d[1]
print(c) 

# 20. len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3
b = {}
print(len(b)) # 0


'''
What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary
'''

# *21. sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90
print(sum(a . values())) # 120
print(sum(a)) # 90
# print(sum(a . items())) # Error bcz int and tuples can be added 

# *22. max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # 40
print(min(a . keys())) #7
print(max(a . values())) #50
print(min(a . values())) #5
print(max(a . items())) # (40, 5)
print(min(a . items())) # (7, 28)
print(max(a)) # 40
print(min(a)) # 7 

# *23 dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d) # {'R': 'Red','G':'Gray','B':'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e)) # Error 
f = [[10] , [20] , [30]]
#print(dict(f)) # Error 
#print(dict([10 , 20])) #cannot convert dictionary update sequence element #0 to a sequence
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) #{10:[20,30],40:[50,60],70:[80,90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
# print(dict(h))#Error 
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))#{(10,20):30,(40,50):60,(70,80):90}

# 24. sorted()  function  (Home  work)
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

'''
Gift
25. Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function

4) a = {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    b = sorted(a . items())  --->  [(5 , 'D' ) , (10 , 'A') , (12 , 'E') , (15 , 'C') , (20, 'B')]
    dict(b)  --->  {5 : 'D' , 10 : 'A' , .....}

x= eval(input("enter a string: "))
a={}
for char in x:
	if char.isalpha():
		char=char.upper()
		a[char]=a.get(char,0)+1
sorted_freq={key:a[key] for key in sorted(a)}
print(sorted_freq)
''' 
a=eval(input("Enter a Dictionary : "))
b=sorted(a.items())
print(dict(b))

# 26.  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) # dict_keys([10, 20, 15, 18])
print(type(b)) #class <Dict Keys>
for  x  in   b:
	print(x)# 
'''
10
20
15
18'''

'''
What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys
''' 
# 27.values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) #dict_values(['Hyd','Sec','cyb','Pune'])
print(type(b)) # Class Dict_values
for  x   in   b:
	print(x) # 'Hyd','Sec','Cyb','Pune'



'''
What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values
'''
# 28. items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) #dict_items[(10,'Hyd'),(20:'Sec'),(15:'Cyb'),(18:'Pune')]
print(type(b)) # dict_items
for  x   in   b:
        print(x)#(10,'Hyd) ..
for  x , y   in  b:
        print(x , y , sep = ' ... ') # 10...'Hyd' ..
'''(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune '''

'''
1) What  does  items()  method  do  --->  Returns  dict_items  object  which  has  list  of  tuples

2) What  are  the  two  elements  of  each  tuple ?  --->  (key , value)
''' 
# 29. Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ') #10..Hyd
''' 10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
for  x , y   in  a . keys(): # error 
       print(x , y , sep = ' ... ') 
for  x , y   in  a . values(): # errortoo many values to unpack 
       print(x , y , sep = ' ... ') 
for  x , y   in  a: # error only returns keys and keys is one value   cannot unpack non-iterable int object
       print(x , y , sep = ' ... ') '''

# 30. clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # {10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a) # {}
del  a # deleted a 
#print(a) # nothing  is there so error 

# 31.copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy() 
print(b) # {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) #  False
print(a  ==  b) # True 

# 32. Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # 10
print(y) #20
print(z) # 30
print() # next line 
x , y , z = a . values()
print(x) # 'Rama' 
print(y)
print(z)
print()
x , y ,  z = a . items()
print(x) #(10,Rama )
print(y)
print(z)
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) #10,Rama
print(rno2 , sname2)
print(rno3 , sname3)
'''
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
15 Rajesh'''

'''
(Home  work)
33*.Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

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
# 34.Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) 
print(b)# {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a . update(b) # error list has no attritube update 

# 35. Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a) #Error
#print(b)
c = [(10,) , (20,) , (30,)]
#b . update(c) #Error 
#print(b)

# 36. Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) #{0:0,1:1,2:8,3:27,4:64}
print(type(d)) #class Dict

# 37. Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) #{0:0,1:2,2:4,3:6,4:8}

# 38. Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)#{15:'sita',17:'Kiran}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # {10:'Rama',18:'Rajesh',12:'Rama Rao'}




