print(eval('25'))  # 25
print(eval('10.8'))  #  10.8
print(eval('False'))# False
print(eval('3+4j'))# (3+4j)
print(eval("    'Hyd'   "))# Hyd
print(eval('3 + 4 * 5'))# 23
print(eval('[10 , 20 , 15 , 18]'))# [10,20,15,18]
print(eval('{10,20,15,18,20,12,18}'))# {18,20,10,12,15}
print(eval('(10 , 20 , 30)'))# (10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))# {10:'Sec'}
#print(eval(4 + 5))

hw---2
print(eval("    'hyd'   "))# hyd
hyd = 'Sec'
print(eval('hyd'))# sec
sec = '25'
print(eval('sec'))# 25
print(eval(sec))# 25
cyb = 10.8
print(eval('cyb'))# 10.8
#print(eval(cyb))

hw---3
print(eval('print("Hyd")'))
output:
Hyd
None

hw----4
print(bool('False'))
print(eval('False'))
print(bool(''))
print(eval('  ""  '))
#print(eval(''))
print(eval('  " "   '))
#print(eval(' '))
output:
True
False
False

HW----5
x = eval(input('Enter  any  input  :  '))
print(type(x))
print(x)
output:
Enter  any  input  :  25
<class 'int'>
25

hw----6
a = input('Enter  any  string  :  ')
print(len(a))
print(a)
b = eval(input('Enter   any  string  : '))
print(len(b))
print(b)
output:
Enter  any  string  :  hyd
3
hyd
Enter   any  string  : 'eve'
3
eve

hw----7
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t')
print(a , b , c , sep = '---')
print(a , b , c , sep = '\n')
print(a , b , c)
print(a , b , c , separator = ':')
output:
25,10.8,Hyd
25      10.8    Hyd
25---10.8---Hyd
25
10.8
Hyd
25 10.8 Hyd

hw----8
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')
print(a , b , c , sep = ',,,')
print(a , b , c , sep = ':::' , end = '\t\t\t')
print(a , b , c)
output:
25 10.8 Hyd---25,,,10.8,,,Hyd
25:::10.8:::Hyd                 25 10.8 Hyd

hw----9
print('Hyd')
print()
print('Sec')
print()
print('Cyb')
ouput:
Hyd

Sec

Cyb

hw----10
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)
output:
[10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30}

hw----11
a = 25
b = '%f'  %a
print(b)
print(type(b))
x = 10.8
y = '%d'  %x
print(y)
print(type(y))
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)
print(type(n))
output:
25.000000
<class 'str'>
10
<class 'str'>
[10, 20, 15, 18]
<class 'str'>

hw----12
a = 10.9274
print('%8.2f'  %a) 
print('%9.1f'  %a)
print('%10.3f'  %a)
print('%.2f'  %a)
print('%.6f'  %a)
print('%f'  %a)
output:
10.93
     10.9
    10.927
10.93
10.927400
10.927400

hw----13
a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4  spaces>
print('%2s'  %a)
print('%s'  %a)
print('%s' , a)
print('%s'  a)
print('%s' , %a)
print(a)
output:
  Hyd
Hyd
Hyd
Hyd
%s Hyd
Hyd

hw----14
a = [10 , 20 , 30 , 40]
print('%s'  %a)
print('%s' , a)
print('%s'  a)
print('%s' , %a)
print('%l'  %a)
print(a)
output:
[10, 20, 30, 40]
%s [10, 20, 30, 40]
[10, 20, 30, 40]
