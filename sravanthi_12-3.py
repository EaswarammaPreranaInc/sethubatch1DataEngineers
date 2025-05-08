12-03-2025:

list = [10 , 20 , 15 , 18]
print(list)
list . append(19)
print(list)
output:
[10, 20, 15, 18]
[10, 20, 15, 18, 19]
list = []
print(list)
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list)
output:
[]
[25, 10.8, 'Hyd', True]
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)
output:
[0, 10, 20, 30, 40]
a = [10 , 20 , 30]
a . append('Hyd')
print(a)
print(len(a))
print(How  to  print  4th  element  of  list  'a')
print(How  to  print  'H')
print(How  to  print  'y')
print(How  to  print  'd')
a = [10 , 20 , 30]
a . append('Hyd')
print(a)
print(len(a))
print(a[3])
print(a[3][0])
print(a[3][1])
print(a[3][2])
output:
[10, 20, 30, 'Hyd']
4
Hyd
H
y
d
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)
print(len(a))
print(How  to  print  inner  list)
print(How  to  print  50)
print(How  to  print  60)
print(How  to  print  70)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)
print(len(a))
print(a[2])
print(a[2][0])
print(a[2][1])
print(a[2][2])
output:
[10, 20, [50, 60, 70], 30, 40]
5
[50, 60, 70]
50
60
70

..............
11-03-2025
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))
e = []
print(any(e))
output:
True
False
True
False
False
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))
d = [10 , 0 , 20]
print(all(d))
e = []
print(all(e))
output:
True
False
False
False
True
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)
c = sorted(a , reverse = True)
print(c)
print(a)
output:
['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))
[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
[[10, 20], (30, 40), {50, 60}]
output:
[4, 6, 8]
<class 'list'>
['V', 'a', 'm', 's', 'i']
[]
a = (10 , 20 , 15, 18)
b = list(a)
print(b)
print(type(b))
print(a  is  b)
print(a == b)
output:
[10, 20, 15, 18]
<class 'list'>
False
False
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))
print(min(a))
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))
print(min(b))
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c))
d = [25 , '35']
print(max(d))
print(max([]))
print(min([]))
output:
30
5
Vamsi
Amar
a = [25 , 10.8 , True]
print(sum(a))
b= [3 + 4j , 5 + 6j]
print(sum(b))
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))
d = [10 , 20 , 15 , 18]
print(sum(d))
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))
output:
36.8
(8+10j)
(39.8+4j)
63
a = [ 25, 10.8, 'Hyd', True]
print(len(a))
b = []
print(len(b))
c = [[10 , 20] , 30 , 40]
print(len(c))
output:
4
0
3
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)
print(a  is   b)
output:
False
False
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)
print(a  is   b)
print(a < c)
print(a > d)
print(a >= c)
print(a <= d)
print(a != c)
print(a != b)
print(a == c)
output:
True
False
True
True
False
False
True
False
False
