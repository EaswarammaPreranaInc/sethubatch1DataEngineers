#13/3/2025
# 1.clear() method  demo program

"""
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . clear()
print(list) #[]

"""

# 2.reverse()  method  demo  programs

"""
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
a . reverse()
print(a) #[18,15,20,10]

"""

# 3.sort()

"""
list = [10 , 20 , 15 , 18 , 5]
print(list) #[10 , 20 , 15 , 18 , 5]
list . sort()
print(list) #[5,10,15,18,20]
list . sort(reverse = True)
print(list) #[20,18,15,10,5]

"""


# 4.Find  outputs

"""
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama','Rajesh','Amar','Sita','Vamsi','Kiran','Rama  Rao']
a . sort()
print(a) #['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']
a . sort(reverse = True)
print(a) #['Vamsi','Sita','Rama Rao','Rama','Rajesh','Kiran','Amar']

"""


# 5.Identify  error

"""
a = [25 , 10.8 ,'Hyd',  True]
#a . sort() #can't sort number and string

"""


# 6.count()  method  demo    program

"""
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #3
print(a . count(25)) #0
print(len(a)) #9

"""


# 7.Write  a  program  to  remove  all  duplicate  elements  of  list (Not  even  single  occurance)

"""
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods


"""

"""
a=eval(input("Enter a List: "))
L=[]

for i in a:
    if a.count(i)==1:
        L.append(i)
        
print(L)

"""


# 8.index()  method  demo  program

"""
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0   1     2    3    4   5     6    7   8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1) # 2 5 8
except:
	print(F'15  is  found  {a . count(15)}  times ') # 15  is  found  3 times

"""


"""
Gift
#9.Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
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
"""

"""
a=eval(input("First  list: "))
b=eval(input("Second list: "))

A=''
for i in a:
    A+=str(i)
    

B=''
for i in b:
    if i in a:
        B+=str(i)
        

if A in B:
    print("True")
    
else:
    print("False")
    
"""


'''
a=eval(input("First  list: "))
b=eval(input("Second list: "))

#a=[2,2,5]
#b=[2,2,3,4,5]

c=b.copy()

for i in c:
    if i not in a or b.count(i)>a.count(i):
        b.remove(i)
        
print(b)

if(len(a)!=len(b)):
    print(False)

else:
    for i in a:
        if a.index(i)!=b.index(i):
            print(False)
            break 
        
    else:
        print(True)


'''


# 10.copy()  method  demo program

"""
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) #[10 , 20 , 15 , 18]
print(a  is  b) #False
print(a  ==  b) #True
c = a[:] 
print(c) #[10 , 20 , 15 , 18]
print(a  is  c)#False
print(a  ==  c)#True
d = a
print(d) #[10 , 20 , 15 , 18]
print(a  is  d) #True
print(a  ==  d) #True

"""


#11.Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

'''
Enter  any  list  :  [10,10,20,10]
List   elements  are  not  identical

Enter  any  list  :  [25,25,25.0,25]
All  the  list  elements  are  identical

'''

'''
a=eval(input("Enter  any  list  : "))

if(a.count(a[0])!=len(a)):
    print("List   elements  are  not  identical")
    
else:
    print("All  the  list  elements  are  identical")
    
'''


'''
#12.Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

Hint: Use  remove()  method
'''

'''
a=eval(input("Enter  any  list  : "))
x=eval(input("element need to be removed: "))

b=a.copy()

for i in b:
    if i==x:
        a.remove(i)
        
print(a)

'''

'''
Gift
#13.Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list


Enter  List  :   [10,20,15,18,10,20,15,10,20,19,10]
Mode :  10

'''

'''
a=eval(input("Enter  List  : "))
A=[]


for i in a:
    if i not in A:
        A.append(i)
        
F=[]

for i in A:
    F.append(a.count(i))
    
M=max(F)


for i in range(len(F)):
    if(F[i]==M):
        print("Mode:",A[i])
    
'''


#14.Nested  List  demo  program

'''

a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) #[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) #3
print(a[0])    #How  to  print  1st  inner  list
print(a[1])     #How  to  print  2nd  inner  list
print(a[2])    #How  to  print  3rd  inner  list
print(a[0][2]) #How  to  print  30
print(a[1][3]) #How  to  print  80
print(a[2][1])      #How  to  print  100

    
'''


#15.Find  outputs

'''
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])#How  to  print  1st   inner  list
print(a[1])#How  to  print  2nd   inner  list
print(a[2])#How  to  print  3rd   inner  list
print(*a[0])#How  to  print  number  of  elements  in  1st  inner  list
print(*a[1])#How  to  print  number  of  elements  in  2nd  inner  list
print(*a[2])#How  to  print  number  of  elements  in  3rd  inner  list

'''



#16.How  to  print  nested  list  in  differnent  ways

'''

a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]

print('Nested list  with  print function')
print(a)

print('Each  inner  list   of   outer  list  without  indexes')
#How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)

print(*a)
for i in a:
    print(i,end=" ")
    
print()
    
    
print('Elements  in  the  form   of  matrix   without  using  indexes')
#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style(use  nested  loop)
for i in a:
    print(*i)

print('Elements  in  the  form   of  matrix  using  indexes')
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
        
    print()
'''

'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''


#17.Find  outputs

'''
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x) #[10 , 20] \n [30 , 40] \n [50 , 60] \n [70 , 80] \n
print() #\n
for  x , y  in  a:
	print(x , y , sep = '...') #10...20 \n 30...40 \n 50...60 \n 70...80 \n

'''

#18.Find  outputs

'''
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x) #10 , 20 , 30] \n [40 , 50 , 60] \n [70 , 80 , 90]\n
print() #\n
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...') #10...20...30 \n 40...50...60 \n 70...80...90 \n

'''


#19.Find  outputs

'''
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x) #[10 , 20] \n [30 , 40 , 50] \n [60 , 70 , 80 , 90] \n
#for  x , y  in  a:
	#print(x , y ,	sep = '...') #error due to more values to un pack 

'''


#20.Find  outputs

'''
a = [[]]
print(a[0])#How  to  print  inner  list
print(*a,a[-1])#How  to  print  inner  list  in  another  way

'''


#21.Find  outputs 

'''

a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))
#[[5 , 'Amar'  ,5000.0],[10 , 'Rama' , 1000.0],[15 , 'Rajesh' , 3500.0],[18 , 'Kiran' , 2800.0],[20 , 'Sita' , 2000.0]]
print(sorted(a , reverse = True))
#[[20 , 'Sita' , 2000.0],[18 , 'Kiran' , 2800.0],[15 , 'Rajesh' , 3500.0],[10 , 'Rama' , 1000.0],[5 , 'Amar'  ,5000.0]]
print(a)
[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]

'''


#22.Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension 
#[8, 64, 216, 512, 1000]

'''
print([i**3 for i in range(2,11,2)])

'''


#23.Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

'''
Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  --->  ['H' , 'P' , 'C' , 'V']

Hint:  Use  upper()  method
'''

'''
s=eval(input("Enter list of strings: "))
#s=['hyd' , 'pune' , 'chennai' , 'vijayawada']

C=[]

for i in s:
    C.append(i[0].upper())
    
print(C)

'''


'''
(Home  work)
#24.Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''

'''
s=eval(input("Enter list of strings: "))
#s=['hyd' , 'pune' , 'chennai' , 'vijayawada']
print([i[0].upper() for i in s])

'''



'''
25.Write  a  program  to  append  each  word  of  the  sentence  and  its  length 
to  a  list (word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

Hint:  Use  split() , upper() , len()


'''

'''
s=input("Enter any sentence :").split()

#s="hyd  is  green  city".split()

L=[]
for i in s:
    L.append([i.upper(),len(i)])
    
print(L)


'''

'''
26.
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''

'''
s=input("Enter any sentence :").split()

#s="hyd  is  green  city".split()

print([[i.upper(),len(i)] for i in s])


'''



'''
27.
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

'''
a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 30 , 40 , 50 , 60 , 70]

b=eval(input("Enter 2nd list:"))
#b=[100 , 200 , 300 , 400]

i=0 
r=[]
while(i<len(a) and i<len(b)):
    r.append(a[i]+b[i])
    i=i+1 
    
print(r)

'''


'''
28.Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''


'''

a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 30 , 40 , 50 , 60 , 70]

b=eval(input("Enter 2nd list:"))
#b=[100 , 200 , 300 , 400]

m=min(len(a),len(b))

print([a[i]+b[i] for i in range(m) ])

'''


'''
29.Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *


How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''

'''
r=int(input("How  many  lists  ?  :"))
c=int(input("How  many  elements  in  each  list ?  :"))

L=[]
for i in range(r):
    L.append([0]*c)
    
print(L)
    
'''


'''
30.Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

'''
r=int(input("How  many  lists  ?  :"))
c=int(input("How  many  elements  in  each  list ?  :"))

print([[0]*c for i in range(r)])

'''


'''
31.Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  ---> [20 , 18 ,  32]

Hint:  for  loop , if  cond , not  in  operator
'''

'''
a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 15 , 18 , 25 , 32]

b=eval(input("Enter 2nd list:"))
#b=[30 , 40 , 10 , 25 , 15]

L=[]

for i in a:
    if i not in b:
        L.append(i)
        
print(L)

'''


'''
32.Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''

'''

a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 15 , 18 , 25 , 32]

b=eval(input("Enter 2nd list:"))
#b=[30 , 40 , 10 , 25 , 15]

print([i for i in a if i not in b])

'''

#33.Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
#Even numbers  between  1  and  20 :   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
print([i for i in range(1,21) if i%2==0])

'''


'''
34.
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''

'''
print([i for i in range(2,21,2) ])

'''

'''
35.
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  
which  are  divisible   by  2  with  comprehension

What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]
'''

'''
print([i**2 for i in range(1,21) if i%2==0])
'''

#36.Repeat  previous  program  with  comprehension  and  without  using  if

'''
print([i**2 for i in range(2,21,2) ])

'''


'''
37.Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''

'''
a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 15]

b=eval(input("Enter 2nd list:"))
#b=[30 , 40 , 35 , 32]

L=[]
for i in a:
    for j in b:
        L.append(i+j)
        
print(L)

'''


'''
38.Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''

'''

a=eval(input("Enter 1st list:"))
#a=[10 , 20 , 15]

b=eval(input("Enter 2nd list:"))
#b=[30 , 40 , 35 , 32]

print([i+j for i in a for j in b])

'''


'''
39.Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''

'''

a=input("Enter 1st string: ")
b=input("Enter 1st string: ")

print([i+j for i in a for j in b])


'''


'''
40.
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

'''
a=eval(input("Enter nested list:"))
#a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

L=[]

for i in a:
    L.extend(i)
    
print(L)

'''


#41.Find  outputs

'''
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x] #[10 , 20] 2 times ,[30 , 40 , 50] 3 times ,[60 , 70 , 80 , 90] 4 times 
print(b)

'''


#42.Nested  comprehension  demo  program 

'''
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)] #[],[0],[0,1],[0,1,2],[0,1,2,3]
print(a)

'''



'''
43.
Normal  program
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
'''


'''
a=['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]

L=[]
for i in a:
    if i[0] not in L:
        L.append(i[0])
            
#print(L)

R=[]

for i in L:
    l=[]
    for j in a:
        if j[0]==i:
            l.append(j)
            
    R.append(l)
    
print(R)
   
'''     
        
        
'''
44.Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                        0      1      2       3      4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]

       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                     0     1       2       3
	                     
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint :  Unsorted  lists  can  not  be  merged
'''

'''

a=eval(input("Enter 1st List: "))
#a=[10  ,  20  , 30   ,  40   ,  50]

b=eval(input("Enter 2nd List: "))
#b=[5  ,  12  , 20   ,  37]

c=a+b 

c.sort()
print(c)

'''