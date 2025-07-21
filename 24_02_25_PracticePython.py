# eval()  function  demo  program
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False')) # Converts 'False' to False
print(eval('3+4j')) # Converts '3+4j' to (3+4j)
print(eval("    'Hyd'   ")) #    'Hyd'  to   Hyd
print(eval('3 + 4 * 5')) # '3+4*5' to 23
print(eval('[10 , 20 , 15 , 18]')) # [10,20,15,18]
print(eval('{10,20,15,18,20,12,18}')) # 10,20,15,12,18}
print(eval('(10 , 20 , 30)')) # (10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10 : 'Sec'}
#print(eval(4 + 5)) # Error becoz of no codes inside eval



# Gift
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8 
print(eval('cyb')) # 10.8
#print(eval(cyb)) # Error: eval() arg 1 must be a string, bytes or code object
#  Gift
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd <nl> None
#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # empty
#print(eval('')) # Error: invalid syntax
print(eval('  " "   ')) # empty
#print(eval(' ')) # Error: invalid syntax
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x)) # <class 'int'>
print(x) # 25
# Which  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # Hyderabad
print(len(a)) # 9
print(a) # Hyderabad
b = eval(input('Enter   any  string  : ')) # 'SaiRam'
print(len(b)) # 6
print(b) # SaiRam
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25  10.8    Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25 <next line> 10.8 <next line> Hyd
print(a , b , c) # 25 <next line> 10.8 <next line> Hyd
#print(a , b , c , separator = ':') # Error becoz of separator can use sep


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # 25 10.8 Hyd---
print(a , b , c , sep = ',,,') # 25 , 10.8 , Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') # 25:::10.8:::Hyd <tab> <tab> <tab>
print(a , b , c) # 25 10.8 Hyd
# Find outputs  (Home  work)
print('Hyd') # Hyd
print()
print('Sec') # Sec
print()
print('Cyb') # Cyb'''
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]  
t = (10 , 20 , 30 , 40)  
s = {10 , 20 , 30 , 40} 
print(l , t , s) # [10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}
#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # 25.000000
print(type(b)) # <class 'str'>
x = 10.8
y = '%d'  %x
print(y) # 10
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # [10, 20, 15, 18]
print(type(n)) # <class 'str'>
# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) # <5 spaces>10.9
print('%10.3f'  %a) # <4 spaces>10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.927400
print('%f'  %a) # 10.927400
# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4  spaces>
print('%2s'  %a) # Hyd
print('%s'  %a) # Hyd
print('%s' , a) # %s Hyd
#print('%s'  a) # Error becoz of no comma
#print('%s' , %a) # Error becoz of comma and %
print(a) # Hyd
# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) # [10, 20, 30, 40]
print('%s' , a) # %s [10, 20, 30, 40]
#print('%s'  a) # Error becoz of comma
#print('%s' , %a) # Error becoz of , and %
#print('%l'  %a) # Error: incomplete format
print(a) # [10 , 20 , 30 , 40]
#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # 25   10.927400   Hyd
print('%i    %g    %s'    %(a , b , c)) # 25   10.9274   Hyd
print('%s    %s    %s'  %(a , b , c)) # 25   10.9274   Hyd
print('%d    %g    %s'  , a , b , c) # %d    %g    %s 25 10.9274 Hyd
#print('%d    %g      %s'   a , b , c) # Error becoz of % is not there
#print('%d    %g    %s'  ,  %(a , b , c)) # Error of Comma and % 
#print('%d    %g    %s'    %a%b%c) # Error: not enough arguments for format string
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25 10.927400 Hyd
#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) # 25
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}'
print(y) # 10.8
print(type(y)) # <class 'str'>
x = [10,20,30,40]
y = F'{x}' 
print(y) # [10, 20, 30, 40]
print(type(y)) # <class 'srt'>
#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # 25         10.8           Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25            b  =  10.8      c  =  Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') # a=25       b=10.8         c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') # 25         10.8           Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # a  =  {a}         b  =  {b}       c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a  =  a           b  =  b         c  =  c
#print(F'{x =}  \t   {y =}   \t  {z =}') # Error: name 'z' is not defined
#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') #  {{x}}
print(F'{{{{{x}}}}}') # {{25}}
print(F'{{{{{{x}}}}}}') # {{{x}}}
print(F'{{{{{{{x}}}}}}}') # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}') # {{{{x}}}}