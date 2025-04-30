from prgm6 import c1  # assuming the class is defined in prog6a.py

a = c1()

print('Elements of iterator with next() function')
a__iter = iter(a)
while True:
    element = next(a__iter)
    print(element)
    if element == 5:
        break

print('Elements of iterator with next() function')
while True:
    element = next(a__iter)
    print(element)
    if element == 10:
        break

print('Elements of iterator with next() function')
a__iter = iter(a)  # get a new iterator (calls __iter__)
while True:
    element = next(a__iter)
    print(element)
    if element == 15:
        break

output:-
-----------
Elements of iterator with next() function
__iter__    method
1
2
3
4
5
Elements of iterator with next() function
6
7
8
9
10
Elements of iterator with next() function
__iter__    method
11
12
13
14
15