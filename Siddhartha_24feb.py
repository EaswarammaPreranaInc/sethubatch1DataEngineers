# eval()  function  demo  program
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False'))  # Converts 'False' to False
print(eval('3+4j'))    # Converts '3+4j' to 3+4j
print(eval("    'Hyd'   "))  # 'Hyd'
print(eval('3 + 4 * 5'))     #23
print(eval('[10 , 20 , 15 , 18]'))  #[10, 20, 15, 18]
print(eval('{10,20,15,18,20,12,18}')) #{10,20,15,18,12}
print(eval('(10 , 20 , 30)'))          # (10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) #{10 : 'Sec'}
#print(eval(4 + 5))                      #Error

print(eval("    'hyd'   "))    #hyd
hyd = 'Sec'
print(eval('hyd'))     #Sec
sec = '25'
print(eval('sec'))    #25
print(eval(sec))      #25
cyb = 10.8
print(eval('cyb'))   #10.8
#print(eval(cyb))     #Error

print(eval('print("Hyd")')) # Hyd None

print(bool('False'))   #True
print(eval('False'))   #False
print(bool(''))         #False
print(eval('  ""  '))   #empty
#print(eval(''))         #Error
print(eval('  " "   '))  #Empty
#print(eval(' '))        #Error

x = eval(input('Enter  any  input  :  '))  #10.8
print(type(x))                             #class <float>
print(x)                                   #10.8

a = input('Enter  any  string  :  ')  #Siddu
print(len(a))                           #5
print(a)                               #Siddu
b = eval(input('Enter   any  string  : '))   #'Siddharth'
print(len(b))                              #9
print(b)                                     #Siddharth

a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t')   # 25<tab>10.8<tab>'Hyd'
print(a , b , c , sep = '---')  #25---10.8---'Hyd'
print(a , b , c , sep = '\n')   #25\n 10.8\n 'Hyd'
print(a , b , c)                #25,10,8,Hyd
print(a , b , c , separator = ':') #Error

a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')  #25 10.8 Hyd---25,,,10.8,,,Hyd
print(a , b , c , sep = ',,,')  
print(a , b , c , sep = ':::' , end = '\t\t\t') #25:::10.8:::Hyd     25 10.8 Hyd
print(a , b , c)

print('Hyd')  #Hyd
print()       #empty
print('Sec')  #Sec
print()       #empty
print('Cyb')  #Cyb

l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)    #[10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30}

a = 25
b = '%f'  %a
print(b)        #25.000000
print(type(b))  #class <str>
x = 10.8
y = '%d'  %x
print(y)      #10
print(type(y)) #class <str>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)         #[10, 20, 15, 18]
print(type(n))   #class <str>

a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)    #10.9             
print('%10.3f'  %a)  #10.927
print('%.2f'  %a)   # 10.93
print('%.6f'  %a)  # 10.927400
print('%f' %a)    #10.92740

a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4  spaces>
print('%2s'  %a)  #Hyd
print('%s'  %a)  #Hyd
print('%s' , a)  #%s Hyd
# print('%s'  a)
# print('%s' , %a)
print(a)           #Hyd

a = [10 , 20 , 30 , 40]
print('%s'  %a) #[10,20,30,40]
print('%s' , a) #%s[10,20,30,40]
# print('%s'  a)
# print('%s' , %a)
# print('%l'%a)
print(a)   #[10,20,30,40]

a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) #25    10.927400    Hyd
print('%i    %g    %s'    %(a , b , c)) #25    10.9274    Hyd
print('%s    %s    %s'  %(a , b , c)) # 25    10.9274    Hyd
print('%d    %g    %s'  , a , b , c) #%d    %g    %s 25 10.9274 Hyd
# print('%d    %g      %s'   a , b , c)
# print('%d    %g    %s'  ,  %(a , b , c))
# print('%d    %g    %s'    %a%b%c)
print('%d'    %a  ,  '%f'     %b , '%s'  %c)#25 10.927400 Hyd 

x = 25
y = F'{x}'   
print(y)    #25
print(type(y)) #<class 'str'>
x = 10.8
y = F'{x}'
print(y)      #10.8
print(type(y)) #<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)     #[10,20,30,40]
print(type(y)) #<class 'str'>

a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #25 10.8 Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #a=25 b=10.8 c=Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')#a=25 b=10.8 c=Hyd
print(F'{a:}  \t   {b:}   \t  {c:}') #25  10.8  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')#a={a} b={b c={c}}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') #a=a b=b c=c
# print(F'{x =}  \t   {y =}  \t {z =}')

x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') #   {{x}}
print(F'{{{{{x}}}}}') #  {{25}}
print(F'{{{{{{x}}}}}}') # {{{x}}}
print(F'{{{{{{{x}}}}}}}') #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}') #  {{{x}}}}









