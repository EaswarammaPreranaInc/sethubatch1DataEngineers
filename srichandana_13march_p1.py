# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)
list . clear()
print(list)
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)
a . reverse()
print(a)
a . sort()
print(a)
a. sort(reverse = True)
# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)
a . sort()
print(a)
a . sort(reverse = True)
print(a)
# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
#a . sort() # sorting cannot be performed between different class objects
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))
print(a . count(25))
print(len(a))
'''
Gift
Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''
a=[10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
print(b)
print([i for i in a if a.count(i)==1])
# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#    0    1    2    3     4     5    6   7    8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')
## copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b)
c = a[:]
print(c)
print(a  is  c)
print(a  ==  c)
d = a
print(d)
print(a  is  d)
print(a  ==  d)
'''[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
True
True'''
#Write  a  program  to  determine  all  the  list  elements  are  identical  or  not
a=eval(input("enter any list:"))
if len(a)==a.count(a[0]):
    print("All  the  list  elements  are  identical")
else:
    print("List   elements  are  not  identical")
##Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list
a = eval(input("1st list: "))
b = int(input("enter number to delete: "))
i=0
while i<len(a):
    if a[i]==b:
        a.remove(a[i])
    else:
        i+=1
print(a)
c=[i for i in a if a!=b]
print(c)
##Gift Write  a  program  to  determine  mode
a=eval(input("a list to determine mode"))
maxi=0
k=[]
for i in a:
    if a.count(i)>maxi:
        maxi=a.count(i)
        p=i
    k.append(a.count(i))
print("mode:",p,"number of times",max(k))
##  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
print("How  to  print  1st  inner  list", *a[0])
print("How  to  print  2nd  inner  list",*a[1])
print("How  to  print  3rd  inner  list",*a[2])
print("How  to  print  30", a[0][2])
print("How  to  print  80",a[1][3])
print("How  to  print  100",a[2][1])
#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print("How  to  print  1st   inner  list",*a[0])
print("How  to  print  2nd  inner  list",*a[1])
print("How  to  print  3rd  inner  list",*a[2])
print("How  to  print  number  of  elements  in  1st  inner  list",len(a[0]))
print("How  to  print  number  of  elements  in  2nd  inner  list",len(a[1]))
print("How  to  print  number  of  elements  in  3rd  inner  list",len(a[2]))
#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a,*a)
print('Each  inner  list   of   outer  list  without  indexes')
for i in a:
    print(i)
#How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for i in a:
    for j in i:
        print(j,end=' ')
    print()
for i in range(len(a)) :
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
print( "printing elements in a new way \n",*a[0]," \n",*a[1],"\n",*a[2])
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')# unpacks as x...y
##  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')# unpacks as x...y...z
##  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')#error as it cant unpack as x...y for 2nd & 3rd element
##  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))
print(sorted(a , reverse = True)) #sorts based on 1st element value of list
print(a)
#  Find  outputs  (Home  work)
a = [[]]
print("How  to  print  inner  list",*a)
print("How  to  print  inner  list  in  another  way",a[0])
# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work
print([i**3 for i in range(1,11) if i%2==0])
'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  --->  ['H' , 'P' , 'C' , 'V']

Hint:  Use  upper()  method
'''
a=eval(input("enter list"))
b=[]
for i in a:
    k=i[0]
    b.append(k.upper())
print(b)
#with comprehesion
print('with comprehesion',[i[0].upper() for i in a])
'''Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
b=input("enter a str")
c=[]
for i in b.split("  "):
    k=[i.upper(),len(i)]
    c.append(k)
print(c)
'''Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
b=input("enter a str")
c=[]
for i in b.split("  "):
    k=[i.upper(),len(i)]
    c.append(k)
print(c)
#with comprehesion
print('with comprehesion',[[i.upper(),len(i)] for i in b.split("  ")])
'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
a=eval(input("enter 1st list of numbers"))
b=eval(input("enter 2nd list of numbers"))
c=[]
for i in range(min(len(a),len(b))):
    c.append(a[i]+b[i])
print(c)
#with comprehesion
print('with comprehesion',[a[i]+b[i] for i in range(min(len(a),len(b))) ])
'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
Hint:  Use  repetition  operator  *
'''
x=int(input("enter x:"))
y=int(input("enter y:"))
print([y*[0]]*x)
'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  ---> [20 , 18 ,  32]

Hint:  for  loop , if  cond , not  in  operator
'''
a=eval(input("enter 1st list of numbers"))
b=eval(input("enter 2nd list of numbers"))
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)
##with comprehesion
print('with comprehesion',[i for i in a if i not in b])
#  #Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
print("Even numbers  between  1  and  20 :",[i for i in range(1,21) if i%2==0])
#without comprehension
a=[]
for i in range(1,21):
    if i%2==0:
        a.append(i)
print("Even numbers  between  1  and  20 :",a)
'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
Hint : Nested  for  loops
'''
a=eval(input("enter 1st list of numbers"))
b=eval(input("enter 2nd list of numbers"))
c=[]
for i in a:
    for j in b:
        c.append(i+j)
print("result:",c)
print("result:",[i+j for i in a for j in b])
'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a=input("1st string")
b=input("2nd string")
c=[]
for i in a:
    for j in b:
        c.append(i+j)
print("Result:",c)
#with comprehension
print("Result:",[i+j for i in a for j in b]) 
