#hw1
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a)#Dictionary  with  print  function
print(' keys of dictionary')
print(a.keys())#How  to  print  keys of dictionary
print('values of dictionary')
print(a.values())#How  to  print  values of dictionary
print('items of dictionary')
print(a.items())#How  to  print  items of dictionary
print('All  the  tuples  of  dict_items   object')
print(*(a.items()))#All  the  tuples  of  dict_items   object
print('each  key of  dictionary  with  for  loop')
for i in a.keys():
    print(i) 
print('each  value of  dictionary  with  for  loop')
for value in a.values():
    print(value)
print('elements  of  tuple   in  dictionary  with  for  loop')
for (item) in a.items():
    print(item)
    print(*item)
print('Each  key of  dictionary  with  for  loop  along   with  corresponding  value')
for key, value in a.items():
    print(key,':',value)
    print(f'Key: {key}, Value: {value}')
#output1
'''Dictionary  with  print  function
{10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
 keys of dictionary
dict_keys([10, 20, 15, 18])
values of dictionary
dict_values(['Ramesh', 'Kiran', 'Amar', 'Sita'])
items of dictionary
dict_items([(10, 'Ramesh'), (20, 'Kiran'), (15, 'Amar'), (18, 'Sita')])
All  the  tuples  of  dict_items   object
(10, 'Ramesh') (20, 'Kiran') (15, 'Amar') (18, 'Sita')
each  key of  dictionary  with  for  loop
10
20
15
18
each  value of  dictionary  with  for  loop
Ramesh
Kiran
Amar
Sita
elements  of  tuple   in  dictionary  with  for  loop
(10, 'Ramesh')
10 Ramesh
(20, 'Kiran')
20 Kiran
(15, 'Amar')
15 Amar
(18, 'Sita')
18 Sita
Each  key of  dictionary  with  for  loop  along   with  corresponding  value
10 : Ramesh
Key: 10, Value: Ramesh
20 : Kiran
Key: 20, Value: Kiran
15 : Amar
Key: 15, Value: Amar
18 : Sita
Key: 18, Value: Sita
'''
#hw2
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
     }
print(type(a))
print(a)
print(len(a))
#output2
'''Hyd
Sec
Cyb
<class 'set'>
{None}
1'''
#3
_= 25
print(_)
print(type(_))
a , _ , c = 10 , 20 , 30
print(a)
print(_)
print(c)
for  _  in  range(5):
	print(_ , 'Hello')
#output3
'''25
<class 'int'>
10
20
30
0 Hello
1 Hello
2 Hello
3 Hello
4 Hello'''
#4
a = 25
print(id(a))
a = 35
print(id(a))
#output4
'''4342800912
4342801232'''
#5
a = 25.7
print(id(a))
print(a)
a = 35.6
print(id(a))
print(a)
b = True
print(id(b))
b = False
print(id(b))
c = None
print(id(c))
c = False
print(id(c))
#output5
'''4395362896
25.7
4831205040
35.6
4342797344
4342797312
4342796840
4342797312'''
#6
a = 'Hyd'
print(id(a))
#a[1] = 'e'
a = 'Sec'
print(id(a))
b = (10 , 20 , 15 , 18)
print(id(b))
#b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b))
c = range(5)
print(id(c))
#c[3] = 10
c = range(5)
print(id(c))
#output6
'''4747775312
5005633376
5017999840
5017507440
5005650864
5005649520
'''
#7
a = 25
b = 25
print(a  is  b)
c = 'Hyd'
d = 'Hyd'
print(c  is  d)
e = False
f = False
print(e  is  f)
g = range(10)
h = range(10)
print(g  is  h)
#output7
'''True
True
True
False'''
#8
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)
e = (10 , 20 , 15 , 18)#doubtnote  tuple is immutable & it is not reusable like range
f = (10 , 20 , 15 , 18)
print(e  is  f)
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)
#output8
'''False
False
False
False'''
#9
print(10 + 20)
print(10.8 + 20.6) 
print(3 + 4j + 5 + 6j) 
print(True + False) 
print('Hyder' + 'abad') 
print('Sankar' + 'Dayal' + 'Sarma') 
print('10' + '20') 
print([10 , 20 , 30] + [1 , 2 , 3]) 
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) 
#print({10 , 20} + {30 , 40}) #doubt sequences without duplicates are not concatenable!!? set are unordered hence not able to concat
#print({10 : 'Hyd'} + {20 : 'Sec'}) #doubt
#print(range(4) + range(5)) 
#print(10 + '20')
#print([10 , 20 , 30] + 5) 
#print([10 , 20 , 30] + (40 , 50 , 60))
#output9
'''30
31.400000000000002
(8+10j)
1
Hyderabad
SankarDayalSarma
1020
[10, 20, 30, 1, 2, 3]
(25, 10.8, 'Hyd', (3+4j), True, None)'''
#10
print(25 * 3)
print(10.8 * 25.6) 
print(True * False) 
print((3 + 4j) * (5 + 6j)) 
print(3 + 4j * 5 + 6j) 
print('25' * 3) 
print(3 * '25') 
print('Hyd' * 4)
print([10 , 20 , 15] * 2) 
print((25, 10.8, 'Hyd', True) * 3) 
#print([10 , 20 , 15] * 3.0) 
#print({10 , 20 , 15} * 2) 
#print({10 : 20 , 30 : 40} * 2) 
#print([10] * [20])
a=(2,4,5,6,7,7)
print(a)
#output10
'''75
276.48
0
(-9+38j)
(3+26j)
252525
252525
HydHydHydHyd
[10, 20, 15, 10, 20, 15]
(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
(2, 4, 5, 6, 7, 7)'''
#11
print(3 ** 4)   #  3 ^ 4 = 81
print(10 ** -2)#
print(4 * 3 * 2)
print(3 + 4 * 5 - 32 / 2 ** 3)
#output11
'''81
0.1
24
19.0'''
#12
print(9 >= 5)  #  True  becoz  >  is  satisfied
print(9 >= 9)   #  True  becoz  =  is  satisfied
print(9 >= 12)   #  False  becoz    both  are  not  satisfied
print(6 <= 8)
print(6 <= 6)
print(6 <= 4)
print(9 != 7)
print(6 == 8)
print(True  >  False)
print(3 + 4j == 3 + 4j)
print(3 + 4j == 5 + 6j)
print(3 + 4j != 5 + 6j)
print(10 == 10.0)
#print(3 + 4j >  3 + 4j)#error
#output12
'''True
True
False
True
True
False
True
False
True
True
False
True
True'''
#13
print('Rama'   >  'Rajesh')   #   True  becoz  'm' > 'j'
print('Rama'  <  'Sita')
print('Hyd'  ==  'Hyd')
print('Rama'  <=   'Ramana')
print('Rama  Rao'  >=  'Rama')
print('Hyd'  != 'Sec')
print('HYD'  <   'hyd')
#output13
'''True
True
True
True
True
True
True
'''
#14
print(10 < 20 < 30)    #   True  becoz  both  are  satisfied
print(10 >= 20 < 30)   #  False  becoz  1st  cond  is  not  satisfied
print(10 < 20 > 30)   
print(1 < 2 < 3 < 4)  
print(1 < 2 > 3 > 1)  
print(4 > 3 >= 3 > 2)
#output14
'''True
False
False
True
False
True'''
