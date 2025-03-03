a = 0O6247
print(a)
print(type(a))
print(id(a))
b = 0o6247
print(id(b))
print(b)
c = 3239
print(c)
print(id(c))
print(0o9248)
output:
3239
<class 'int'>
1634215699056
1634215699056
3239
3239
1634215699056
''''
a = 0XA7B9
print(a)
print(type(a))
b = 0xBEEF
print(b)
print(A7B9)
print('A7B9')
print(0XBEER)
print(0XHYD)
print(0xA7G9B)
output:
42937
<class 'int'>
48879
A7B9
''''
a = 9248
print(a)
print(type(a))
output:
9248
<class 'int'>
''''
a = "Rama Rao"
print(a)
print(type(a))
print(id(a))
b = 'Hyd'
print(b)
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)
output:
Rama Rao
<class 'str'>
2903160843184
Hyd
Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.
''''
a = 'Hyd'
print(a * 3)
print(a * 2)
print(a * 1)
print(a * 0)
print(a * -1)
print(25 * 3)
print('25' * 3)
print('25' * 4.0)
print(3 * 'Hyd')
output:
HydHydHyd
HydHyd
Hyd


75
252525
HydHydHyd
''''
print(len('Hyd'))
print(len('Rama Rao'))
print(len('9247'))
print(len(''))
print(len(' '))
print(len(689))
output:
3
8
4
0
1
''''
a = """"Hyd"""
print(a)
print(len(a))
print(a[0])
print("""Hyd"""")
b = """""Hyd"""
print(b)
print(len(b))
output:
"Hyd
4
"
""Hyd
5
''''
a = 'Sankar Dayal Sarma'
print(a[7 : 12])
print(a[7 : ])
print(a[ : 6])
print(a[ : ]) #   a[ 0 :  18 :  1]  --->  string  from  indexes  0  to   17  in  steps  of   1   ---> Sankar  Dayal  Sarma
print(a[:  : ])
print(a[1 : 10 : 2])
print(a[0 : : 2])
print(a[1 : : 2])
print(a[-5 : -1])
print(a[::-1])  #  a[-1 : -19 : -1]  --->  string  from  indexes  1-  to   18  in  steps  of   -1   ---> Reverse string 
print(a[-1:-5:-1])
print(a[ : : -2])
print(a[3 : -3])
print(a[2 : -5])   #  a[2 : -5 :  1]  --->  string  from  indexes  2  to  -6   in  steps  of   1   --->  nkar<space>Dayal<space>
print(a[-1:-5])
print(a[3 : 3])
output:
Dayal
Dayal Sarma
Sankar
Sankar Dayal Sarma
Sankar Dayal Sarma
akrDy
Sna aa am
akrDylSra
Sarm
amraS layaD raknaS
amra
arSlyDrka
kar Dayal Sa
nkar Dayal

