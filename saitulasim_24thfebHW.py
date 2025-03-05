# eval()  function  1 PROGRAM 
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False')) #False
print(eval('3+4j')) #(3+4j)
print(eval("    'Hyd'   ")) #Hyd
print(eval('3 + 4 * 5')) #23
print(eval('[10 , 20 , 15 , 18]')) #[10, 20, 15, 18]
print(eval('{10,20,15,18,20,12,18}')) #{18, 20, 10, 12, 15}
print(eval('(10 , 20 , 30)')) #(10, 20, 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) #{10: 'Sec'}
print(eval('4 + 5')) #9

# 2 PROGRAM
print(eval("    'hyd'   ")) #hyd
hyd = 'Sec'
print(eval('hyd')) #Sec
sec = '25'
print(eval('sec')) #25
print(eval(sec)) #25
cyb = 10.8
print(eval('cyb')) #10.8
print(eval('cyb')) #10.8
k=print("Hyd")
print(eval('k')) #None

# 3 PROGRAM
print(bool('False')) #True
print(eval('False')) #False
print(bool('')) #False
print(eval('  ""  ')) #<empty space>
#print(eval('')) #error there nothing to evaluate
print(eval('  " "   ')) #<empty space>
#print(eval(' ')) # #error empty space without quotes cannot be evaluated

# 4 PROGRAM
x = eval(input('Enter  any  input  :  ')) #6
print(type(x)) #<class 'int'>
print(x) #6

# 5 PROGRAM
a = input('Enter  any  string  :  ') #helo
print(len(a)) #4
print(a) #helo
b = eval(input('Enter   any  string  : ')) #"just oe"
print(len(b)) #7
print(b) #just oe

# 6 PROGRAM
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t') #25	10.8	Hyd
print(a , b , c , sep = '---') #25---10.8---Hyd
print(a , b , c , sep = '\n') 
#25
#10.8
#Hyd
print(a , b , c) #25 10.8 Hyd 
print(a , b , c , sep= ':') #25:10.8:Hyd
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') #25 10.8 Hyd---25,,,10.8,,,Hyd
print(a , b , c , sep = ',,,')
print(a , b , c , sep = ':::' , end = '\t\t\t') #25:::10.8:::Hyd			25 10.8 Hyd
print(a , b , c)

# 7 PROGRAM
print('Hyd') #Hyd
print() #emptyline
print('Sec') #Sec
print() #emptyline
print('Cyb') #Cyb
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) #[10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30}

# 8 PROGRAM
a = 25
b = '%f'  %a
print(b) #25.000000
print(type(b)) #<class 'str'>
x = 10.8
y = '%d'  %x
print(y) #10
print(type(y)) #<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m 
print(n) #[10, 20, 15, 18]
print(type(n)) #[10, 20, 15, 18]

# 9 PROGRAM
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) #  <5 spaces>10.9
print('%10.3f'  %a) #  <4  spaces>10.927
print('%.2f'  %a) #  10.93
print('%.6f'  %a) #10.927400
print('%f'  %a) #10.927400

# 10 PROGRAM
a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4  spaces>
print('%2s'  %a)  #Hyd as it reserves 2 spaces for 3 char string & it print entire str
print('%s'  %a)  #Hyd
print('%s' , a) #%s Hyd
#print('%s'  a) #error no comma
#print('%s' , %a) #error because of comma
print(a) #Hyd
a = [10 , 20 , 30 , 40]
print('%s'  %a)  #[10, 20, 30, 40]
print('%s' , a)  #%s [10, 20, 30, 40]
#print('%s'  a)
#print('%s' , %a)
#print('%l'  %a)
print(a) #[10 , 20 , 30 , 40]

# 11 PROGRAM
x = 25
y = F'{x}'
print(y) #25
print(type(y)) #<class 'str'>
x = 10.8
y = F'{x}'
print(y) #10.8 
print(type(y))  #<class 'str'>
x = [10,20,30,40]
y = F'{x}' 
print(y) #[10, 20, 30, 40]
print(type(y)) #<class 'str'>

# 12 PROGRAM
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #25  	   10.8   	  Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #a = 25  	  b  =  10.8  	  c  =  Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') #a=25  	   b=10.8   	  c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') #25  	   10.8   	  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') #a  =  {a}  	  b  =  {b}  	  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') #a  =  a  	  b  =  b  	  c  =  c
#print(F'{x =}  \t   {y =}   \t  {z =}')

# 13 PROGRAM
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) #25    10.927400    Hyd
print('%i    %g    %s'    %(a , b , c)) #25    10.9274    Hyd
print('%s    %s    %s'  %(a , b , c)) #25    10.9274    Hyd
print('%d    %g    %s'  , a , b , c) #%d    %g    %s 25 10.9274 Hyd
#print('%d    %g      %s'   a , b , c)
#print('%d    %g    %s'  ,  %(a , b , c))
#print('%d    %g    %s'    %a%b%c)
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) #25 10.927400 Hyd

# 14 PROGRAM
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') #{{x}}
print(F'{{{{{x}}}}}') #{{25}}
print(F'{{{{{{x}}}}}}') #{{{x}}}
print(F'{{{{{{{x}}}}}}}') #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{{{x}}}}
