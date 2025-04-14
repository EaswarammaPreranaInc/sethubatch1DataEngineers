'''
#1)difference()   method  demo  program  (Home  work)

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b) # Returns  a  set  with  elements  of  set  'a'  which  are  not  in  'b'
print(c) # {10,20} in any order
print(type(c)) #<class 'set'>
d = a - b # Returns  a  set  with  elements  of  set  'a'  which  are  not  in  'b'
print(d)# {10,20} in any order
print(type(d)) #<class 'set'>
print(c  is  d) # False , both sets are differents
print(c  ==  d) # True , comparing the elements of sets 'c' and 'd'.


#2) symmetric_difference()   method  demo  program  (Home  work)

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b) # Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b' without common elements
print(c) # {10,20,50,60} in any order
print(type(c)) #< class 'set'>
d = a ^ b # Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b' without common elements
print(d) # {10,20,50,60} in any order
print(type(d)) # <class 'set'>
print(c   is   d) # False , both sets are differents
print(c  ==   d) # True , comparing the elements of sets 'c' and 'd'.

#3)Find  outputs  (Home  work)

a = {x * x  for   x   in   range(10)}  #  x multiply with x number upto 9 iterations
print(a) # {0,1,4,9,16,25,36,49,64,81} in any order
print(type(a)) # <class 'set'>

#4)(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  ---> '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'


a="Rama Rao"
lst= set(a)
def remove_duplicates(lst):
    result = []
    for element in lst:
      
            result.append(element)  
    return result

b = remove_duplicates(lst)
b=set(b)
print(b) #{'R', ' ', 'o', 'a', 'm'} in any order


#5)Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

input = "RamA Rao"
def distinct_vowels(input):
    vowels = {'A', 'E', 'I', 'O', 'U'}  # Set of vowels
    input = input.upper()  # Convert input to uppercase
    found_vowels = set()  # Set to store distinct vowels 
    for char in input: # Check each character in input string
        if char in vowels:
            found_vowels.add(char)  # Add vowel to set
    output = ''.join(sorted(found_vowels))  # Join the sorted vowels into a string for output
    return output
output = distinct_vowels(input) # Test the function with the provided input
print(output)

#6)Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists

a=[False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
def remove_duplicates(a):
    seen = set()  # Set to track seen elements
    output_list = []  # List to store unique elements
    for item in a:
        if item not in seen:
            seen.add(item)  # Add item to set if not seen
            output_list.append(item)  # Add item to output list
    return output_list
output = remove_duplicates(a)
print(output)


#7)Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output  are  list

a = [10 , 20 , 30 , 40 , 50 , 60]
b =  [30 , 40 , 70 , 80 , 20]
a = set(a)
b = set(b)
c = a & b
print(c) # {40, 20, 30}

#8) How  to  access  values  of  dictionary (Home  work)

a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print( a['Empno']) #How  to  print  value  25  in  dict  'a'
print(a['Ename']) #How  to  print  'Rama Rao'  in  dict  'a'
print(a['Sal']) # How  to  print  value  1000.65   in  dict  'a'

#9)How  to  modify  values  of  dictionary  (Home  work)

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a))# 1377228495744 ---- same Address
a.update({'Sal' : 2000}) #How  to  modify  1000.65  to  2000
a.update({'Ename' : 'Sita'}) #How  to  modify  'Rama  Rao'  to  'Sita'
a.update({'Empno' : 35}) #How  to  modify  25   to  35
print(a) # {'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000 }
print(id(a)) # 1377228495744 --- same Address

#10) How  to  append  key : value  pairs  to dictionary  (Home  work)

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.update({'Gender' : 'M'}) # How  to  append  'Gender' : 'M'  to  dictionary  'a'
a.update({'Married' :  True}) # How  to  append  'Married' :  True  to  dictionary  'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}

#11)Find  outputs (Home  work)
a = { }
a.update({10 : 'Rama'}) #How  to  append  10 : 'Rama'  to  dictionary  'a'
a.update({20 : 'Sita'}) #How  to  append  20 : 'Sita'  to  dictionary  'a'
a.update({15 : 'Rajesh'}) #How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a.update({18 : 'Kiran'}) #How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a) # {10 : 'Rama', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}

#12)How  to  remove  key : value  pairs  of  dictionary  (Home  work)

a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
a.pop('Sal') #How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao'}

#13)n  and  not  in  operators  (Home  work)

a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True
print(60  in  a . keys()) # False
print(60  in  a . values()) # True
print(30  in  a . values()) # False
print(50  in  a) # True
print(20  in  a) # False
print(70  not  in  a . keys()) # False
print(40  not  in  a . values()) # False
print(25  not  in  a) # True

#14)What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}

a = input('Enter  dictionary  :  ')
print(a) #  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # <class 'dict'>

#15)Find  outputs  (Home  work)

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} # unpacking all the key:values pairs of dict 'a' to form a new dictionary with same key : value pairs
print(b) # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a  is  b) # False
print(a  ==  b) # True
c = a # object 'a' is assigned to object 'c'
print(a  is   c) # True
print(a  ==  c) #True

#16)Find  outputs  (Home  work)

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c} # unpacking all the keys of dict 'a', 'b' and 'c' to form a new dictionary with same keys
print(d) # {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # < class 'set'>
e = {**a , **b , **c} # unpacking all the key:values pairs of dict 'a', 'b' and 'c' to form a new dictionary with same key : value pairs
print(e) # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) #< class 'dict'>

#17)Find  outputs  (Home  work)

a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b) # Error due to dict does not support '+' operand to concatinate
c = {**a , **b} # concatinate 'a' and 'b' dictionaries
print(c) # {10: 60, 30: 50}
d = a | b # it is alternate of concatinate dict
print(d) # {10: 60, 30: 50}

#18)Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'

a = {}
num_employees = int(input("Enter the number of employees: ")) #  Number of employees to add

for _ in range(num_employees): # Loop to get employee details and add to dictionary
    emp_name = input("Enter employee name: ")
    emp_salary = float(input("Enter employee salary: "))
    
    # Append employee name and salary to dictionary
    a[emp_name] = [emp_salary] # Append employee name and salary to dictionary
print("Employee Salary Dictionary:", a)

#19)a = {}
a['AAA'] = 10000  --->   {'AAA': 10000}
a['BBB'] = 20000  --->   {'AAA': 10000 , 'BBB' : 20000}

a ={}
a.update({'AAA':1000})
a.update({'BBB':2000})
print(a)


#20)Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice


a = "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"
b = ['Emp no = 25', 'Emp name = Rama Rao', 'sal = 10000.0', 'gender = m']
c = {}

for item in b:
    key, value = item.split(' = ', 1)  # Split on ' = ', max 1 split
    c[key] = value  # Add key-value pair to dictionary

print("Dictionary from list 'b':", c)
c = {}  # Reset dictionary
items = a.split(' , ')  # Split string by ' , '
for item in items:
    key, value = item.split(' = ', 1)  # Split on ' = ', max 1 split
    c[key] = value  # Add key-value pair to dictionary

print("Dictionary from string 'a':", c)

#21) len()  function  demo  program  (Home  work)

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3
b = {}
print(len(b)) # 0

#22)sum()  function demo  program  (Home  work)

a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90 -- sum of all keys in 'a'
print(sum(a . values())) # 120 --- sum of all values in 'a'
print(sum(a)) # 90 --  by default keys are sumed  in 'a'
print(sum(a . items())) #Error not supported sum for 'int' and 'Tuple'

#23)max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # 40
print(min(a . keys())) # 7
print(max(a . values()))# 50
print(min(a . values()))# 5
print(max(a . items()))# (40, 5)
print(min(a . items()))#(7, 28)
print(max(a))#40
print(min(a))#7


#24)dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c) #  Converts  list  of  tuples  to  dict
print(d) # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e)) # Error due to list
f = [[10] , [20] , [30]]
print(dict(f)) # Error due to  list
print(dict([10 , 20])) # Error due to Tuple 
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) #{10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h)) # Error due to list
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) # {(10, 20): 30, (40, 50): 60, (70, 80): 90}


#25)sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) # [5, 10, 15, 18, 20]
c = sorted(a . values())
print(c) # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d) # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f) # [20, 18, 15, 10, 5]
print(a) # {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

#26)Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function

4) a = {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    b = sorted(a . items())  --->  [(5 , 'D' ) , (10 , 'A') , (12 , 'E') , (15 , 'C') , (20, 'B')]
    dict(b)  --->  {5 : 'D' , 10 : 'A' , .....}

input = {10: 'A', 20: 'B', 15: 'C', 5: 'D', 12: 'E'}

output = {key: input[key] for key in sorted(input)} # Sort the dictionary by keys and create a new sorted dictionary

print(output) # {5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}


#27)keys()  method  demo  program

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) # dict_keys([10, 20, 15, 18])
print(type(b)) # <class 'dict_keys'>
for  x  in   b:
        print(x) #10 <next line>20<next line>15<next line>18

#28) values()  method  demo  program

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) # dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b)) #  <class 'dict_values'>
for  x   in   b:
	print(x) #Hyd <next line>Sec<next line>Cyb<next line>pune

#29) items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) # dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) # <class 'dict_items'>
for  x   in   b:
        print(x) #(10, 'Hyd') <next line>(20, 'Sec')<next line>(15, 'Cyb')<next line>(18, 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ') # 10 ... Hyd <next line> 20 ... Sec <next line> 15 ... Cyb <next line> 18 ... Pune
 

#30) Find  outputs (Home  work)

a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ') # 10 ... Hyd <next line> 20 ... Sec <next line> 15 ... Cyd <next line> 18 ... Pune
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ') # Error only one keys  are there in 'a' but here 2 variables taken to seperste the keys
for  x , y   in  a . values():
       print(x , y , sep = ' ... ') # Error only one Values  are there in 'a' but here 2 variables taken to seperste the Values
for  x , y   in  a:
       print(x , y , sep = ' ... ') # Error by default only keys printed  so, only one keys  are there in 'a' but here 2 variables taken to seperste the keys

#31)clear()  method  demo  program (Home  work)

a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # {10: 20, 30: 40, 50: 60}
a . clear()
print(a) # {}
del  a
print(a) # Error due to del operator notthere in dict 

#32) copy()  method demo  program  (Home  work)

a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) # {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a  is  b) # False
print(a  ==  b) # True
	   
#33)Find  outputs  (Home  work)

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # 10
print(y) # 20
print(z) # 15
print() # empty key
x , y , z = a . values()
print(x) # Rama
print(y) # Sita
print(z) # Rajesh
print() # empty value
x , y ,  z = a . items()
print(x) # (10, 'Rama')
print(y) # (20, 'Sita')
print(z) # (15, 'Rajesh')
print() # empty item
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) # 10 Rama
print(rno2 , sname2) # 20 Sita
print(rno3 , sname3) # 15 Rajesh

#34)Find outputs (Home  work)

a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b) # {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a . update(b) # Error due to list has no method update()

#35) Find  outputs  (Home  work)

a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a) #Error due to list has no method update()
print(b)
c = [(10,) , (20,) , (30,)]
b . update(c) # Error due to list has no method update() 
print(b)

#36) Find  outputs (Home  work)

d = {x : x ** 3   for    x   in  range(5)}
print(d) # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) # <class 'dict'>

#37)Find outputs   (Home  work)

d = { x :  2 * x    for    x   in   range(5) }
print(d) # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

#38)Find outputs  (Home  work)

a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}

#39)Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

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
input_str = "RamA raO"

# Initialize an empty dictionary to store frequencies
a = {}

# Loop through each character in the string
for char in input_str:
    if char.isalpha():  # Check if character is an alphabet
        char = char.upper()  # Convert character to uppercase
        a[char] = a.get(char, 0) + 1  # Update frequency

# Create a sorted dictionary by keys
sorted_freq = {key: a[key] for key in sorted(a)}

# Print the sorted frequency dictionary
print(sorted_freq) # {'A': 3, 'M': 1, 'O': 1, 'R': 2}
