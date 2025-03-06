'''
# eval()  function  demo  program
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False'))#False
print(eval('3+4j'))#3+4j
print(eval("    'Hyd'   "))#Hyd
print(eval('3 + 4 * 5'))#23
print(eval('[10 , 20 , 15 , 18]'))#[10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}'))#{10,20,15,12,18}
print(eval('(10 , 20 , 30)'))#(10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))#{10:'Sec'}
#print(eval(4 + 5))#error



'''
'''
eval()  function
------------------
1) What  does  eval()  function  do ?  --->  Converts  string  to  appropriate  object

2) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer
    What  does  float(x)  do  ?  ---> Converts   object  'x'   to  float
    What  does  complex(x)  do  ?  ---> Converts   object  'x'  to  complex  number
    What  does  bool(x)  do  ?  ---> Converts   object  x'  to  boolean

3) What  is  the  advantage  of  eval()  function ?  --->
													It  can  be  used  as  an  alternative  to  int() , float() ,  complex() , bool()  and  so  on
'''
'''
# Gift
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#hyd
hyd = 'Sec'
print(eval('hyd'))#Sec
sec = '25'
print(eval('sec'))#'25'
print(eval(sec))#25
cyb = 10.8
print(eval('cyb'))#10.8
#print(eval(cyb))#error

#  Gift
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#Hyd,None

#  Find  outputs  (Home  work)
print(bool('False'))#True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  '))#""
#print(eval(''))#error
print(eval('  " "   '))#" "
#print(eval(' '))#error

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))#accepts list,string float int all types of data
print(type(x))#based on the type of input
print(x)#Enter any input :

# Which  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')# this is one is the better way
print(len(a))#return the length
print(a)#a is displayed
b = eval(input('Enter   any  string  : '))# considers all datatypes and also we need ''  quotes to be mentioned to have a string input
print(len(b))
print(b) '''
'''
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t')#a	b	c
print(a , b , c , sep = '---')#a---b---c
print(a , b , c , sep = '\n')#a<nextline>b<nextline>c
print(a , b , c)#a<nextline>b<nextline>c
#print(a , b , c , separator = ':')#use sep


'''

'''
1) What  is  the  default  separator  for  print()  function ?  --->  Space

2) Can  separator  be  modified  ? --->  With  sep  argument  of print()  function

3) What  does  sep = 'delimeter'  do ?  --->  Modifies  the  separator  to  the  specified  delimeter

4) print(object , sep = ' , ')
    Is  sep  argument  required  in  the  above  print()  function ?  ---> No  becoz  single  object  is  being  printed

5) When  is  sep  argument  required  in  print()  function  ?  --->  When  more  than  one  object  is  being  printed

6) What  is  the  separator  between  hours , minutes  and  seconds ?  --->  ':'  i.e.  sep = ':'
    What  is  the  separator  between  date , month  and  year ?  --->  '-'  (or) '/'  (or)  '.'
'''
'''
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')#25<nextline>10.8<nextline>Hyd---
print(a , b , c , sep = ',,,')#25,10.8,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')#25:::10.8:::Hyd tab keys 3 times
print(a,b,c)#25<nextline>10.8<nextline>Hyd

# Find outputs  (Home  work)
print('Hyd')#Hyd
print()#empty  line
print('Sec')#Sec
print()#empty line
print('Cyb')#Cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l,t,s)# prints all elements in same line

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a # converts 25 to 25.000..
print(b)#25.00..
print(type(b))#class str
x = 10.8
y = '%d'  %x #conversion to int no
print(y) # 10
print(type(y)) # class Str
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) #'[10 , 20 , 15 , 18]'
print(type(n))#class str


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) #<7 spaces>10.9
print('%10.3f'  %a)#<6 spaces>10.927
print('%.2f'  %a)#10.92
print('%.6f'  %a)#10.9274..
print('%f' %a)#10.927400

# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4  spaces>
print('%2s'  %a)#Hyd
print('%s'  %a)#Hyd
print('%s' , a)#%s Hyd
print('%s'  a)#error
print('%s',%a)#error
print(a)#Hyd


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)#'[10 , 20 , 30 , 40]'
print('%s' , a)#'%s'[10 , 20 , 30 , 40]
#print('%s'  a)#error % missing
#print('%s' , %a)#error
#print('%l' %a) error
print(a)[10 , 20 , 30 , 40]

#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))#"25 10.927400 Hyd"
print('%i    %g    %s'    %(a , b , c))#"25 10.927400 Hyd"
print('%s    %s    %s'  %(a , b , c))# '25 ''10.927400'' Hyd'
print('%d    %g    %s'  , a , b , c)#'%d    %g      %s'25 10.927400 Hyd
print('%d    %g      %s'   a , b , c)#error
print('%d    %g    %s'  ,  %(a , b , c))#error
print('%d    %g    %s'    %a%b%c)#error
print('%d' %a,'%f'%b,'%s'%c)#"25 10.927400 Hyd" 
'''


#  Find  outputs  (Home  work)
x = 25
y = F'{x}'#'25'
print(y)#25
print(type(y))#class str
x = 10.8
y = F'{x}'
print(y)#10.8
print(type(y))#class str
x = [10,20,30,40]
y = F'{x}'
print(y)#[10,20,30,40]
print(type(y))#class str

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')#25	10.8	Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')#a=25	b=10.8	c=Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')#25	10.8	'Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}')#25	10.8	Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')#'a  =  {a}  \t  b  =  {b}  \t  c  =   {c}'
print(F'a  =  a  \t  b  =  b  \t  c  =  c')#'a  =  a  \t  b  =  b  \t  c  =  c'
#print(F'{x=}\t{y=}\t{z=}#x y z variables are not declared

#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')#{{x}}
print(F'{{{{{x}}}}}')#{{25}}
print(F'{{{{{{x}}}}}}')#{{{x}}}
print(F'{{{{{{{x}}}}}}}')#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{{{x}}}}



'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''
