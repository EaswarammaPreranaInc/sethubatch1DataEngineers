Program1:
print({10 , 20}  |  {30 , 20})
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})
print(range(4) | range(5))#error
Output:
{10, 20, 30}
{10: 'Hyd', 20: 'Vja', 30: 'Cyb'}

Program2:
print(True  and  False)    #  False
print(False  and  True)  #  False
print(False  and   False)  #   False
print(True  and  True)  # True
print(10  and  20)  #  20
print(0  and  20) #  0
print(-25  and  0)  #  0
print(''  and  25)
print(6j  and  'Hyd')
print(0j  and  'Sec')
print('Hyd'   and  10.8)
print(10  and  20  and  30)
Output:
False
False
False
True
20
0
0

Hyd
0j
10.8
30

Program3:
print(True  or  False)   #   True
print(False  or  True)   #  True
print(True  or  True) #  True
print(False  or   False)    # False
print(10  or  20)   #  10
print(0   or  20)  #   20
print(-25  or  0)
print(''  or  35)
print(6j  or  'Hyd')
print(0.0  or  3 + 4j)
print('Hyd'   or   10.8)
Output:
True
True
True
False
10
20
-25
35
6j
(3+4j)
Hyd

program4:
print(not  True)  #  False
print(not  False)  #  True
print(not  25)
print(not  0)
print(not  'Hyd')
print(not  '')
print(not  -10)
print(not  not  'Hyd')
Output:
False
True
False
True
False
True
False
True

Program5:
i = 10
i = not  i > 14
print(i)
print(not(6 < 4  or  9 >= 5  and  6 != 6))
Output:
True
True
