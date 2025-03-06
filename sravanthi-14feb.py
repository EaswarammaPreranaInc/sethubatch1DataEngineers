print(int(10.8)) #  Converts  10.8  to  10
print(int(True))  #  Converts  True  to  1
print(int(False))
print(int('25'))
print(int('0075'))
print(int(0B11010))
print(0B11010)
print(int(0O6247))
print(0O6247)
print(int(0XA7B9))
print(0XA7B9)
print(int(3 + 4j))
print(int('25.4'))
print(int('Ten'))
output:
10
1
0
25
75
26
26
3239
3239
42937
42937
''''
print(float(25)) #  Converts  25  to  25.0
print(float(True)) #  Converts   True   to   1.0
print(float(False))
print(float('92'))
print(float('36.4'))
print(float('0075'))
print(float(0B1010101))
print(float(0O6247))
print(float(0XA7B9))
print(float(3 + 4j))
print(float('Ten'))
output:
25.0
1.0
0.0
92.0
36.4
75.0
85.0
3239.0
42937.0
''''
print(complex(3 , 4))
print(complex(0 , 4))
print(complex(3))
print(complex(3.8 , 4.6))
print(complex(3.8))
print(complex(3 , 4.5))
print(complex(True , False))
print(complex(True))
print(complex(False))
print(complex(True , 4))
print(complex('3'))
print(complex('3.8'))
print(complex(3 , '4'))
print(complex('3' , 4))
print(complex('3' , '4'))
print(complex('Ten'))
output:
(3+4j)
4j
(3+0j)
(3.8+4.6j)
(3.8+0j)
(3+4.5j)
(1+0j)
(1+0j)
0j
(1+4j)
(3+0j)
(3.8+0j)
''''
print(bool(0)) #   Converts  0  to  False
print(bool(10))
print(bool(-25))
print(bool(0.0))
print(bool(0.1))
print(bool(0 + 0j))
print(bool(10 + 20j))
print(bool(-15j))
print(bool('False'))
print(bool(''))
print(bool('Hyd'))
print(bool(' '))
print(bool('True'))
output:
False
True
True
False
True
False
True
True
True
False
True
True
True
''''
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))
print(str(3 + 4j))
print(str(True))
print(str(False))
print(str(None))
output:
25
10.8
(3+4j)
True
False
None
''''
print(oct(195))
print(oct(0B10101110010))
print(oct(0xA7B9))
output:
0o303
0o2562
0o123671
''''
print(hex(25))
print(hex(0B10101111010111))
print(hex(0O6247))
output:
x19
0x2bd7
0xca7
''''
a = range(10 , 50 , 5)
print(type(a))
print(a)
print(*a)
print(id(a))
print(len(a))
print(*a[2 : 7] , sep = ' , ')
print(*a[ : : -1])
a[4] = 32
print(a * 2)
output:
<class 'range'>
range(10, 50, 5)
10 15 20 25 30 35 40 45
1530646015136
8
20 , 25 , 30 , 35 , 40
45 40 35 30 25 20 15 10
''''
a = range(10 , 20)
print(*a , sep = ',')
b = range(5)
print(*b)
c = range(10 , 1 , -1)
print(*c , sep = '...')
d = range(-10 , 0)
print(*d)
e = range(-10)
print(*e)
f = range(2 , 2)
print(*f)
g = range(10 , 11 , 0.1)
h = range('A' , 'F')
output:
10,11,12,13,14,15,16,17,18,19
0 1 2 3 4
10...9...8...7...6...5...4...3...2
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
''''
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)
print(*a)
print(type(a))
print(id(a))
print(len(a))
a[2] = 'Sec'
print(a)
print(a[2 : 5])
output:
[25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
25 10.8 Hyd True (3+4j) None Hyd 25
<class 'list'>
2093764993472
8
[25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
['Sec', True, (3+4j)]
''''
a = [ ]
print(a)
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)
a . remove('Hyd')
print(a)
a . remove('25')
print(a)
output:
[]
[25, 10.8, 'Hyd', True]
[25, 10.8, True]
[25, 10.8, True]
''''
a = [25 , 10.8 , 'Hyd']
print(a * 3)
print(a * 2)
print(a * 1)
print(a * 0)
print(a * -1)
print(a * 4.0)
output:
[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
[25, 10.8, 'Hyd']
[]
[]
''''
a = list('Hyd')
print(a)  
print(type(a)) 
print(len(a)) 
b = (10 , 20 , 15 , 18)
print(list(b))
print(list(range(5)))
print(list(25))
output:
['H', 'y', 'd']
<class 'list'>
3
[10, 20, 15, 18]
[0, 1, 2, 3, 4]
''''
a = [ ]
print(type(a))
print(a)
print(len(a))
b = list()
print(b)
print(len(b))
output:
<class 'list'>
[]
0
[]
0
''''
a = [10 , 20 , 30 , 40 , 50]
print(a)
a[1 : 4] = [60 , 70 , 80]
print(a)
output:
[10, 20, 30, 40, 50]
[10, 60, 70, 80, 50]
''''
list  =  [10 , 20 , 15 , 12 , 18]
print(15   in   list)
print(19   in   list)
print(14  not  in  list)
print(12  not  in  list)
output:
True
False
True
False
''''
a =  [25]
print(a[1])
print(a[1:])
output:
[]
''''
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[2 : 7])
print(list[ : : ])
print(list[:])
print(list[ : : -1])
print(list[ : : 2])
print(list[1 : : 2])
print(list[ : : -2])
print(list[-2 : : -2])
print(list[1 : 4])
print(list[-4 : -1])
print(list[3 : -3]) 
print(list[2 : -5])
print(list[-1:-5])
output:
[(3+4j), 'Hyd', True, None, 10.8]
[25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
[25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
[25, (3+4j), True, 10.8]
[10.8, 'Hyd', None, 'Hyd']
['Hyd', None, 'Hyd', 10.8]
[10.8, True, (3+4j), 25]
[10.8, (3+4j), 'Hyd']
[True, None, 10.8]
['Hyd', True]
[(3+4j)]
[]


