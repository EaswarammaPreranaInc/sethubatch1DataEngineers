'''
#1) reverse()  method  demo  program (Home  work)

a = [10 , 20 , 15 , 18]
print(a) # [10, 20, 15, 18]
a . reverse() # reverse the elements in the list
print(a)# [18, 15, 20, 10]

#2)clear() method  demo program  (Home  work)

list = [10 , 20 , 15 , 18]
print(list) # [10, 20, 15, 18]
list . clear() # it will clear all the elements in the list but not delete the list
print(list) # []

#3) sort()  method  demo  program (Home  work)

list = [10 , 20 , 15 , 18 , 5]
print(list)# [10 , 20 , 15 , 18 , 5]
list . sort()# append elements in ascending order to list
print(list)# [5, 10, 15, 18, 20]
list . sort(reverse = True) # append elements in descending order to list
print(list) # [20, 18, 15, 10, 5]


#4)Find  outputs (Home  work)

a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a . sort() # append elements in ascending order to list
print(a)#['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)# append elements in discending  order to list
print(a) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

#5) Identify  error (Home  work)

a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort()# Error due to 'Hyd' and True bcz cannot sort the string and bool values with int and flaot values

#6)count()  method  demo    program (Home  work)

a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #3 , 15 is at index 3 
print(a . count(25))#0 ,bcz 25 is not there in given list 
print(len(a))#9 number of elements in the given list

#7)Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods

def remove_duplicates(lst):
    result = []
    for element in lst:
        if lst.count(element) == 1: 
            result.append(element)  
    return result
a = [10, 20, 15, 10, 14, 10, 18, 20, 19]
b = remove_duplicates(a)
print(b)

#8)index()  method  demo  program  (Home  work)

a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)# counts '15' at first index place
	while  True:
		print(i)
		i = a . index(15 , i + 1) # counts next '15' at which index.
except:
	print(F'15  is  found  {a . count(15)}  times ') # counts '15', how many times is there in list

2 # 15 is found at 2 index in list
5 # 15 is found at 5 index in list
8 # 15 is found at 8 index in list
15  is  found  3  times


#9)Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [2,3,4]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->  True  becoz  elements  2,3,4   are   in  [2,2,3,4,5]

2) First  list :  [2,4,4]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->	False  becoz   elements  2,4,4  are  not  in  [2,2,3,4,5]

3) First  list :  [2,4,3]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  --->  False  becoz   elements  2,4,3   are  not  in  [2,2,3,4,5]

4) First  list :  [2,2,5]
    Second  list :  [2,2,3,4,5]
    What  is  the  output ?  ---> True  becoz   elements  2,2,5    are   in  [2,2,3,4,5]

5) Hint:  Use  index()  method


def is_sublist(list1, list2):
    for i in range(len(list2) - len(list1) + 1):
        if list2[i:i+len(list1)] == list1:
            return True
    return False
list1_1 = [2, 3, 4]
list2_1 = [2, 2, 3, 4, 5]
list1_2 = [2, 4, 4]
list2_2 = [2, 2, 3, 4, 5]
list1_3 = [2, 4, 3]
list2_3 = [2, 2, 3, 4, 5]
list1_4 = [2, 2, 5]
list2_4 = [2, 2, 3, 4, 5]
print(is_sublist(list1_1, list2_1)) 
print(is_sublist(list1_2, list2_2)) 
print(is_sublist(list1_3, list2_3)) 
print(is_sublist(list1_4, list2_4)) 

(or)

def is_sublist(list1,list2):
    for i in range(len(list1)):
        if list1[i] not in list2:
            return False
        for j in range(len(list2)):
            if (list1[j] in list2) and (list2.index(list1[i+1]) > list2.index(list1[i])):
                return True
list1_1 = [2, 3, 4]
list2_1 = [2, 2, 3, 4, 5]
list1_2 = [2, 4, 4]
list2_2 = [2, 2, 3, 4, 5]
list1_3 = [2, 4, 3]
list2_3 = [2, 2, 3, 4, 5]
list1_4 = [2, 2, 5]
list2_4 = [2, 2, 3, 4, 5]
print(is_sublist(list1_1, list2_1)) 
print(is_sublist(list1_2, list2_2)) 
print(is_sublist(list1_3, list2_3)) 
print(is_sublist(list1_4, list2_4)) 

#10)copy()  method  demo program  (Home  work)

a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)# [10, 20, 15, 18]
print(a  is  b) #False bcz Copies  elements  of  list  to  another  list  and  returns  the  new  list but not the same list 
print(a  ==  b) # True bcz Copies  elements  of  list  to  another  list  
c = a[:] 
print(c)# [10, 20, 15, 18]
print(a  is  c) #False bcz Copies  elements  of  list  to  another  list  and  returns  the  new  list but not the same list
print(a  ==  c) #True bcz Copies  elements  of  list  to  another  list  
d = a
print(d)# [10, 20, 15, 18]
print(a  is  d) # True bcz Copies  elements  of  list  to  another reference object  and  returns  same list
print(a  ==  d) # True

#11)Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  ---> All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  --->  4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  ---> All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? ---> 3

3) Hint: Use  len()  and  count()



def check_identical_elements(lst):
    if lst.count(lst[0]) == len(lst):
        print("All the elements are identical")
    else:
        print("The elements are not identical")
    print(f"How many elements are in the list? ---> {len(lst)}")
    print(f"How many times is the first element repeated? ---> {lst.count(lst[0])}")
input_list = [10,10,10,10]
check_identical_elements(input_list)


#12)Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

Hint: Use  remove()  method

input_list = [10, 20, 15, 18, 19, 15, 17, 20, 15, 14]
def remove_all_occurrences(lst, value):
    while value in lst:
        lst.remove(value)
    return lst
value_to_remove = 15
output = remove_all_occurrences(input_list, value_to_remove)
print(output)

#13)Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list

Enter  List  :   [10,20,15,18,10,20,15,10,20,19,10]
Mode :  10

input_list = [10,20,15,18,10,20,15,10,20,19,10]
from collections import Counter
def find_mode(lst):
    count = Counter(lst)
    max_count = max(count.values())
    mode = [key for key, value in count.items() if value == max_count] 
    return mode
mode = find_mode(input_list)
print(f"Mode: {mode}")

#14)write a program to remove 15 from the list
Enter List  :  [15,15,15]
Enter  element  to  be  deleted : 15
List  without   15's :  []

def remove_element(lst, element):
    return [item for item in lst if item != element]
input_list = [15, 15, 15]
element_to_delete = 15
updated_list = remove_element(input_list, element_to_delete)
print(f"List without {element_to_delete}'s : {updated_list}")

#15)Nested  List  demo  program  (Home  work)

a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) #[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) # 3
print(a[0]) #(How  to  print  1st  inner  list)
print(a[1]) #(How  to  print  2nd  inner  list)
print(a[2]) #(How  to  print  3rd  inner  list)
print(a[0][2]) #(How  to  print  30)
print(a[1][3]) #(How  to  print  80)
print(a[2][1]) #(How  to  print  100)

#16)Find  outputs  (Home  work)

a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0]) #(How  to  print  1st   inner  list)
print(a[1])#(How  to  print  2nd   inner  list)
print(a[2]) #(How  to  print  3rd   inner  list)
print(len(a[0])) #(How  to  print  number  of  elements  in  1st  inner  list)
print(len(a[1])) #(How  to  print  number  of  elements  in  2nd  inner  list)
print(len(a[2])) #(How  to  print  number  of  elements  in  3rd  inner  list)

#17)How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(???)
print('Each  inner  list   of   outer  list  without  indexes')
How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)

a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print('Nested list with print function')
print(a)
print('Each inner list of outer list without indexes')
for inner_list in a:
    print(inner_list)
print('Elements in the form of matrix without using indexes')
for inner_list in a:
    for element in inner_list:
        print(element, end=' ')
    print()
print('Elements in the form of matrix using indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()  

#18)Find  outputs (Home  work)

a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x) # [10, 20]<next line>[30, 40]<next line>[50, 60]<next line>[70, 80]
print() # none
for  x , y  in  a:
	print(x , y , sep = '...') # 10 ... 20<next line>30... 40<next line>50... 60<next line>70... 80

#19)Find  outputs (Home  work)

a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x) # [10, 20, 30]<next line>[40, 50, 60]<next line>[70, 80, 90]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...') # 10... 20... 30<next line>40... 50... 60<next line>70... 80... 90<next line>

#20)Find  outputs (Home  work)

a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)# [10, 20]<next line>[30,40, 50]<next line>[60,70, 80, 90]
for  x , y  in  a:
	print(x , y ,	sep = '...')# only 10...20 prints bcz here 'x' and 'y' are assigned to print ie., is two elements are there to prints
	
#21)Find  outputs  (Home  work)

a = [[]]
print(a[0])#(How  to  print  inner  list)
for inner_list in a:
    print(inner_list)#(How  to  print  inner  list  in  another  way)

#22)Find  outputs  (Home  work)

a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a)) #[[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True))#[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)#[[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]

#23)Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension 

cubes = [x**3 for x in range(2, 11, 2)]

print(cubes)#[ 8, 64, 216, 512, 1000]

#24)Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  strings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  --->  ['H' , 'P' , 'C' , 'V']

Hint:  Use  upper()  method

input_list = ['hyd', 'pune', 'chennai', 'vijayawada']
output_list = []
for word in input_list:
    output_list.append(word[0].upper())

print(output_list)

#25)Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']

input_list = ['hyd', 'pune', 'chennai', 'vijayawada']
output_list = [word[0].upper() for word in input_list]
print(output_list)

#26)Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

Hint:  Use  split() , upper() , len()

sentence = "hyd is green city"
words = sentence.split()
output_list = []
for word in sentence.split():
    output_list.append([word.upper(), len(word)])
print(output_list)

#27)Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]

sentence = "hyd is green city"

output_list = [[word.upper(), len(word)] for word in sentence.split()]

print(output_list)

#28)Write  a  program  to  add  two  lists  of  unequal  length  without comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]

result = []
for i in range(min(len(list1), len(list2))):
    result.append(list1[i] + list2[i])
print(result)

#29)Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]

result = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]

print(result)

#30)Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *

rows = 3
cols = 4

a = []
for _ in range(rows):
    row = [0] * cols 
    a.append(row)
print(a)

#31)How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

rows = int(input("How many lists? : "))
cols = int(input("How many elements in each list? : "))
a = []
for _ in range(rows):
    row = [0] * cols
    a.append(row) 
print(a)

#32)Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]


rows = int(input("Enter number of lists: "))  # Example input: 3
cols = int(input("Enter number of elements in each list: "))  # Example input: 4

a = [[0] * cols for _ in range(rows)]

print(a)

#33)Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   with  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  ---> [20 , 18 ,  32]

Hint:  for  loop , if  cond , not  in  operator

list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]
a = []
for item in list1:
    if item not in list2:
        a.append(item)
print(a)

#34)Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]

list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]
a = [item for item in list1 if item not in list2]
print(a)

#35) Write   a  program  to  print  even  numbers  between  1  and  20  without  comprehension
 Even numbers  between  1  and  20 :   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)

#36)Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]

even_numbers =[]
for num in range(1,21):
	if num % 2 ==0:
		even_numbers.append(num)
		print(even_numbers)
output
-----------
[2]
[2, 4]
[2, 4, 6]
[2, 4, 6, 8]
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10, 12]
[2, 4, 6, 8, 10, 12, 14]
[2, 4, 6, 8, 10, 12, 14, 16]
[2, 4, 6, 8, 10, 12, 14, 16, 18]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
		
#37)Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]

a = [num ** 2 for num in range(1, 21) if (num ** 2) % 2 == 0]
print(a)

#38)Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  without  comprehension

What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]

a = []
for num in range(1, 21):
    square = num ** 2  
    if square % 2 == 0:
        a.append(square)
print(a)

#39)Repeat  previous  program  with  comprehension  and  without  using  if

a = [num ** 2 for num in range(2, 21, 2)]

print(a)

#40)Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops

list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]
result = []

for item1 in list1:
    for item2 in list2:
        result.append(item1 + item2)
print(result)

#41)Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  with comprehension

list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]

result = [item1 + item2 for item1 in list1 for item2 in list2]

print(result)

#42)Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

string1 = "HYD"
string2 = "PUNE"

result = [char1 + char2 for char1 in string1 for char2 in string2]

print(result)

#43)Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]

nested_list = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

flat_list = []

for sublist in nested_list:
    
    for item in sublist:
        flat_list.append(item)
print(flat_list)

#44)Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  ---> [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]

nested_list = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)

#45)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)

output
------
[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

#46)Nested  comprehension  demo  program (Home  work)

a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)

output
------
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

#47)Normal  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

1) b = ['S', 'A' , 'Z' , 'K']

2) c = []

3) Iteartion  1 :  d  =  ['Swathi' , 'Srinivas']
                           c =  [['Swathi' , 'Srinivas']]

4) Iteartion  2 :  d  =  ['Anand' , 'Amar']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]

5) Iteartion  3 :  d  =  ['Zebra']
                            c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]

6) Iteartion  4 :  d  =  ['King']
                            c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]


strings = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']

b = ['S', 'A', 'Z', 'K']
c = []
for char in b:
    d = []
    for s in strings:
        if s.startswith(char):
            d.append(s)
    if d:
        c.append(d)
print(c)

#48)Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint :  Unsorted  lists  can  not  be  merged


a = [10, 20, 30, 40, 50]
b = [5, 12, 20, 37]

i = 0  
j = 0  

c = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

while i < len(a):
    c.append(a[i])
    i += 1

while j < len(b):
    c.append(b[j])
    j += 1

print(c)

(or)
'''
a = eval(input('Enter 1st sorted list:'))
b = eval(input('Enter 2st sorted list:'))
c =[]
i=j=0
while i < len(a) and j < len(b):
	if a[i] <b[j]:
		c.append(a[i])
		i += 1
	else:
		c.append(b[j])
		j += 1
c.append(a[i:])
c.append(b[i:])
print(c)

