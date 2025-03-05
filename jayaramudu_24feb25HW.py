# Ex-1.py
print(eval('25'))  # Converts '25' to 25
print(eval('10.8'))  # Converts '10.8' to 10.8
print(eval('False')) # Converts 'False' to bool False
print(eval('3+4j'))   # Converts '3+4j' to complex 3+4j
print(eval("    'Hyd'   ")) # Converts 'Hyd' To Hyd
print(eval('3 + 4 * 5'))  # Converts '3 + 4 * 5' to 23
print(eval('[10 , 20 , 15 , 18]'))  # Converts '[10 , 20 , 15 , 18]' to [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}')) # Converts to set
print(eval('(10 , 20 , 30)'))  # Converts tuple
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # Converts dictionary

# Ex-2.py
print(eval("    'hyd'   ")) # Converts "    'hyd'   " to 'hyd'
hyd = 'Sec'
print(eval('hyd'))  # Sec
sec = '25'
print(eval('sec'))  # 25
print(eval(sec))  # 25
cyb = 10.8
print(eval('cyb'))  # 10.8

# Ex-3.py
print(eval('print("Hyd")')) # Hyd and None

# Ex-4.py
print(bool('False'))
print(eval('False'))
print(bool(''))
print(eval('  ""  '))
print(eval('  " "   '))

# Ex-5.py
x = eval(input('Enter any input: '))
print(type(x))
print(x)

# Ex-6.py
a = input('Enter any string: ')
print(len(a))
print(a)
b = eval(input('Enter any string: '))
print(len(b))
print(b)

# Ex-7.py
a, b, c = 25, 10.8, 'Hyd'
print(a, b, c, sep=',')
print(a, b, c, sep='\t')
print(a, b, c, sep='---')
print(a, b, c, sep='\n')
print(a, b, c)

# Ex-8.py
a, b, c = 25, 10.8, 'Hyd'
print(a, b, c, end='---')
print(a, b, c, sep=',,,')
print(a, b, c, sep=':::', end='\t\t\t')
print(a, b, c)

# Ex-9.py
print('Hyd')
print()
print('Sec')
print()
print('Cyb')

# Ex-10.py
l = [10, 20, 30, 40]
t = (10, 20, 30, 40)
s = {10, 20, 30, 40}
print(l, t, s)

# Ex-11.py
a = 25
b = '%f' % a
print(b)  # 25.000000
print(type(b))  # class str
x = 10.8
y = '%d' % x  # 10
print(y)  # 10
print(type(y))  # class str
m = [10, 20, 15, 18]
n = '%s' % m  # '[10 , 20 , 15 , 18]'
print(n)  # [10 , 20 , 15 , 18]
print(type(n))  # class str

# Ex-12.py
a = 10.9274
print('%8.2f' % a)  # <3 spaces>10.93
print('%9.1f' % a)  # <5 spaces>10.9
print('%10.3f' % a)  # <4 spaces>10.923
print('%.2f' % a)  # 10.93
print('%.6f' % a)  # 10.927400
print('%f' % a)  # 10.927400
