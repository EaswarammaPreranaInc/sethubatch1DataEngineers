# eval()  function  demo  program
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False')) # False
print(eval('3+4j')) # (3+4j)
print(eval("    'Hyd'   ")) #Hyd
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]')) #[10,20,15,18]
print(eval('{10,20,15,18,20,12,18}')) #{10,20,15,12,18} not in order
print(eval('(10 , 20 , 30)')) #(10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) #{10 : 'Sec'}
print(eval(4 + 5)) # error eval must be string


# Gift
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) #25
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # error even if the value is assigned to any obj that obj must be also str


#  Gift
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # First it will print hyd then print function returns none in the next line


#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # True
print(bool('')) # False
print(eval('  ""  ')) #Empty str Because of empty str in the str
print(eval('')) #eval function cant contain an empty string
print(eval('  " "   ')) #Empty str Because of empty str in the str
print(eval(' ')) #eval function cant contain an empty string


# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) # 25 or # if i try to enter any str it will give error cause of eval() but if i try to enter anything other than str i will get the output to encounter this i have to enter the str with '' then i will not get the error
print(type(x)) # <class 'int'>
print(x) # 25


# Which  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') #akash
print(len(a)) #5
print(a) #akash
b = eval(input('Enter   any  string  : ')) #'akash' or # if i try to enter str without '' i will get the error cause of eval function to encounter this i have to enter the str with '' then i will not get the error
print(len(b)) #5
print(b) #akash


# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25  10.8    Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25<nextline>10.8<nextline>Hyd
print(a , b , c)# 25 10.8 Hyd
print(a , b , c , seperator = ':') # error it is sep not seperator


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') #25 10.8 Hyd---
print(a , b , c , sep = ',,,') # continues with previous one 25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') #New line #25:::10.8:::Hyd
print(a , b , c) #continues with previous one 25 10.8 Hyd 
#Final output
25 10.8 Hyd---25,,,10.8,,,Hyd
25:::10.8:::Hyd			25 10.8 Hyd


# Find outputs  (Home  work)
print('Hyd') #Hyd
print() #empty
print('Sec') #Sec
print() #empty
print('Cyb') #Cyb


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) #[10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30}


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) #25.000000 Convert obj to str float with 6 digits after decimal point due to %f
print(type(b)) # <class 'str'>
x = 10.8
y = '%d'  %x
print(y) #10 converts obj to str int due to %d
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) #[10, 20, 15, 18] converts list to obj str due to %s
print(type(n)) # <class 'str'>


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) #      10.9
print('%10.3f'  %a) #    10.927
print('%.2f'  %a) #10.93
print('%.6f'  %a) #10.927400
print('%f'  %a) #10.927400


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4  spaces>
print('%2s'  %a) #Hyd
print('%s'  %a)#Hyd
print('%s' , a) #%s Hyd
print('%s'  a) # error format is missing
print('%s' , %a) # error format is  missing
print(a) #Hyd


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) #[10 , 20 , 30 , 40]
print('%s' , a) #%s [10, 20, 30, 40]
print('%s'  a) # error invalid format
print('%s' , %a) # error invalid format
print('%l'  %a) #%l is not a valid format
print(a) #[10 , 20 , 30 , 40]


#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) #25    10.927400    Hyd
print('%i    %g    %s'    %(a , b , c)) #25    10.9274    Hyd
print('%s    %s    %s'  %(a , b , c)) #25    10.9274    Hyd
print('%d    %g    %s'  , a , b , c) #%d    %g    %s 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c) #invalid format
print('%d    %g    %s'  ,  %(a , b , c)) #invalid format
print('%d    %g    %s'    %a%b%c) #invalid format
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) #25 10.927400 Hyd


#  Find  outputs  (Home  work)
x = 25
y = f'{x}'
print(y) #25
print(type(y)) #<class 'str'>
x = 10.8
y = F'{x}'
print(y) #10.8
print(type(y)) #<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) #[10, 20, 30, 40]
print(type(y)) #<class 'str'>


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #25  	   10.8   	  Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #a = 25  	  b  =  10.8  	  c  =  Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') #a=25  	   b=10.8   	  c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') #':' will be ignored and will get  25  	   10.8   	  Hyd
print('a  = {a}  \t  b  =  {b}  \t  c  =   {c}') #f is not called will get a  =  {a}  	  b  =  {b}  	  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # no {} used so we will get a  =  a  	  b  =  b  	  c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') #error x not defined 


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') #{{x}}
print(F'{{{{{x}}}}}') #   {{25}}
print(F'{{{{{{x}}}}}}') #{{{x}}}
print(F'{{{{{{{x}}}}}}}') #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}') #{{{{x}}}}
