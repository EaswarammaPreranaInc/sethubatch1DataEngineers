'''
#2) Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
#end  of  the  function
a = count(start = 10)
disp(a)
b = count(start = 10 , step = 5)
disp(b)
c = count(start = 10 , step = -2.5)
disp(c)
d = count()
disp(d)

output:-
--------
10      11      12      13
10      15      20      25
10      7.5     5.0     2.5
0       1       2       3

#3)Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While  loop')
while   True:
        try:
                print(next(z1))
        except:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))
print('*z3 :  ' ,  *z3)
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4))

output:-
---------
While  loop
(10, 0)
(20, 1)
(15, 2)
(18, 3)
for  loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)
Next  element :   (10, 8)
*z3 :   (20, 9) (15, 10) (18, 11)
Next  element  :  (10, 12)


#4) Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')
while   True:
        try:
                print(next(z1))
        except:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
z3 = zip(cnt , list)
print(next(z3))
print(*z3)
z4 = zip(list , cnt)
print(next(z4))

output:-
----------
while  loop
(0, 10)
(1, 20)
(2, 15)
(3, 18)
for  loop
(10, 5)
(20, 6)
(15, 7)
(18, 8)
(9, 10)
(10, 20) (11, 15) (12, 18)
(10, 14)


#5)  Find  outputs  (Home  work)
from  itertools  import  zip_longest
import   time
def  disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
list = [10 , 20 , 30 , 40]
z1  =  zip(range(7) , list)
print(type(z1))
disp(z1)
z2 = zip_longest(range(7) , list)
print(type(z2))
disp(z2)

output:-
---------
<class 'zip'>
(0, 10)
(1, 20)
(2, 30)
(3, 40)
<class 'itertools.zip_longest'>
(0, 10)
(1, 20)
(2, 30)
(3, 40)
(4, None)
(5, None)
(6, None)


#6) Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list) # Repeates the cycle infinite times.
print(type(c))
while   True:
	print(next(c))
	time . sleep(1)

output:-
-----------
10
20
30
40
10
20
30
40
.
. so on 

KeyboardInterrupt
^CTerminate batch job (Y/N)? n

#7)Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3) # 25 Repeats for 3 times 
print('1st  repeat  object')
while   True:
	try:
		print(next(r))
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')
r  =  repeat('Hyd') # Hyd Repeats for infinite times
while   True:
	print(next(r))
	time . sleep(1)

output:-
----------
1st  repeat  object
25
25
25
2nd  repeat  object
Hyd
Hyd
Hyd
Hyd
.
.
 so on 

 
#8) Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2)) # squaring of each element upto 9 digits.
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break

output:-
-----------
0
1
4
9
16
25
36
49
64
81


#9)Find  outputs (Home  work)
import  time
def  disp(itr):
	while  True:
		try:
			print(next(itr))
			time . sleep(1)
		except:
			break
from  itertools  import  combinations,permutations
list = ['A' , 'B' , 'C' , 'D']
c = combinations(list , 3)
print('Different  Combinations')
disp(c)
print('Different   Permutations')
p = permutations(list , 3)
disp(p)


output:-
---------
Different  Combinations
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'D')
('B', 'C', 'D')
Different   Permutations
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'B')
('A', 'C', 'D')
('A', 'D', 'B')
('A', 'D', 'C')
('B', 'A', 'C')
('B', 'A', 'D')
('B', 'C', 'A')
('B', 'C', 'D')
('B', 'D', 'A')
('B', 'D', 'C')
('C', 'A', 'B')
('C', 'A', 'D')
('C', 'B', 'A')
('C', 'B', 'D')
('C', 'D', 'A')
('C', 'D', 'B')
('D', 'A', 'B')
('D', 'A', 'C')
('D', 'B', 'A')
('D', 'B', 'C')
('D', 'C', 'A')
('D', 'C', 'B')

'''
#1) Find   outputs (Home  work)
from  itertools  import  count
c = count()
print('While  loop')
while   True:
        x = next(c)
        if   x > 9:# yeilds from 0 to 9 and 10 yeids but not prints
                break
        print(x)
print('For  loop')
for  x  in  count():
	if  x  >  20:# yeilds from 0 to 20 and 21 yeids but not prints ,here 10 not prints bcz in while loop it breaks the loop
		break
	print(x)
#end  of  for  loop
print('Element :  ' , end = '\t') # Error: most recent call Error
print(next(count())) # 23
c = count()
print(*c)  # Memory Error due to infinite elelments are yeilded so it is difficult to store in count () iterator.




output:-
----------
While  loop
0
1
2
3
4
5
6
7
8
9
For  loop
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
Element :       0
Traceback (most recent call last):
  File "C:\Users\MAHENDRA\Desktop\manu documents\python files\manu\16manuApril.py", line 291, in <module>
    print(*c)  # Memory Error due to infinite elelments are yeilded so it is difficult to store in count () iterator.
    ~~~~~^^^^
MemoryError

