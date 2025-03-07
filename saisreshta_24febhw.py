program1:
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False')) #false
print(eval('3+4j')) #3+4j
print(eval("    'Hyd'   ")) #Hyd
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]')) #[10,20,15,18]
print(eval('{10,20,15,18,20,12,18}')) # {15,10,20,12,18}
print(eval('(10 , 20 , 30)')) #(10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10:sec}
print(eval(4 + 5)) #error

program2:
print(eval("    'hyd'   "))#hyd
hyd = 'Sec'
print(eval('hyd'))#sec
sec = '25'
print(eval('sec'))#25
print(eval(sec))#25
cyb = 10.8
print(eval('cyb'))#10.8
print(eval(cyb))

program3:
print(bool('False')) #True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  '))
print(eval('')) #error
print(eval('  " "   ')) #error
print(eval(' '))#error

program4:
x = eval(input('Enter  any  input  :  '))#25
print(type(x))# <class 'int'>
print(x) #25

program5:
a = input('Enter  any  string  :  ') #25
print(len(a)) #2
print(a)#25
b = eval(input('Enter   any  string  : '))#27
print(len(b))#2
print(b)#27

program6:
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t')   #25 10.8 hyd
print(a , b , c , sep = '---')  # 25---10.8---hyd
print(a , b , c , sep = '\n')   # 25
                                  10.8
                                  Hyd
print(a , b , c)  # 25 10.8 hyd
print(a , b , c , separator = ':') # error because here it is written seperator fully

program7:
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') #25 10.8 hyd---
print(a , b , c , sep = ',,,') # 25,,,10.8,,,hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') #25:::10.8:::hyd
print(a , b , c) #25 10.8 hyd

program8:
print('Hyd') #Hyd
print()
print('Sec') #sec
print()
print('Cyb')# cyb

program9:
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10,20,30,40] (10,20,30,40) {10,20,30,40}

program10:
a = 25
b = '%f'  %a
print(b) #25
print(type(b)) # <class 'int'>
x = 10.8
y = '%d'  %x
print(y) #10
print(type(y))# <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) #[10,20,15,18]
print(type(n)#< class 'str'>

program11:
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)  #  10.9
print('%10.3f'  %a)  # 10.927
print('%.2f'  %a)   # 10.93
print('%.6f'  %a) # 10.92740
print('%f'  %a)  #10.927400

program12:
a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4  spaces>
print('%2s'  %a)   # Hyd
print('%s'  %a)#Hyd
print('%s' , a) #%s hyd
print('%s'  a) #error
print('%s' , %a) #error
print(a) #hyd

program13:
a = [10 , 20 , 30 , 40]
print('%s'  %a) #[10,20,30,40]
print('%s' , a) #%s[10,20,30,40]
print('%s'  a) #error
print('%s' , %a) #error
print('%l'  %a)#error
print(a)#[10,20,30,40]

program14:
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # 25 10.9274  Hyd
print('%i    %g    %s'    %(a , b , c)) # 25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c))# 25 10.9274 Hyd
print('%d    %g    %s'  , a , b , c) # %d %g %s 25 10.9274 hyd
print('%d    %g      %s'   a , b , c) # error
print('%d    %g    %s'  ,  %(a , b , c)) #error
print('%d    %g    %s'    %a%b%c) #error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25 10.9274 hyd

program15:
x = 25
y = F'{x}'
print(y) # 25
print(type(y)) @<class 'str'>
x = 10.8
y = F'{x}'
print(y) #10.8
print(type(y)) #class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) # [10,20,30,40]
print(type(y)) # <class 'str'>

pprogram16:
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # 25 10.8 hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a=25 b=10.8 c=hyd
print(F'{a=}  \t   {b=}   \t  {c=}') # a=25 b=10.8 c=hyd
print(F'{a:}  \t   {b:}   \t  {c:}')# 25 10.8 hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')# a={a} b={b} c={c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a=a b=b c=c
print(F'{x =}  \t   {y =}   \t  {z =}') 

program17:
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}') #{{25}}
print(F'{{{{{{x}}}}}}') #{{{x}}}
print(F'{{{{{{{x}}}}}}}') #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}') #{{{{x}}}}
