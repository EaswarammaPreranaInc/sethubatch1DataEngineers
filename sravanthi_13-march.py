 Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
a=[a for a in range(1,21) if a%2==0]
print("Even numbers between 1 to 20:",a)
output:
Even numbers between 1 to 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

Repeat  previous  program  with  comprehension  and  without  using  if
a=[a for a in range(2,21,2)]
print("Even numbers between 1 to 20:",a)
output:
Even numbers between 1 to 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]

a=[a**2 for a in range(1,21) if a%2==0]
print(a)
output:
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

 Repeat  previous  program  with  comprehension  and  without  using  if
a=[a**2 for a in range(2,21,2)]
print(a)
output:
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
						[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
a=[10,20,15]
b=[30,40,35,32]
c=[]
for i in a:
  for j in b:
   c.append(i+j)
print(c)
output:
[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]

Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
a=[10,20,15]
b=[30,40,35,32]
c=[i+j for i in a for j in b]
print(c)
output:
[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]

Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']
a="HYD"
b="PUNE"
c=[ch1+ch2 for ch1 in a for ch2 in b]
print(c)
output:
['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
a=[[10,20],[30,40,50],[60,70,80,90]]
b=[]
for a in a:
 for c in a:
    b.append(c)
print(b)
output:
[10, 20, 30, 40, 50, 60, 70, 80, 90]

Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  ---> [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
a=[[10,20],[30,40,50],[60,70,80,90]]
b=[c for a in a for c in a]
print(b)
output:
[10, 20, 30, 40, 50, 60, 70, 80, 90]

a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)
output:
[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)
output:
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint :  Unsorted  lists  can  not  be  merged
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')
output:
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]

a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))
print(sorted(a , reverse = True))
print(a)
output:
[[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
[[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]

a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')
output:
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90

