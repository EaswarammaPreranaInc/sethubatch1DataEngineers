 # eval()  function  demo  program
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False'))
print(eval('3+4j'))
print(eval("    'Hyd'   "))
print(eval('3 + 4 * 5'))
print(eval('[10 , 20 , 15 , 18]'))
print(eval('{10,20,15,18,20,12,18}'))
print(eval('(10 , 20 , 30)'))
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))
print(eval(4 + 5))




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
''

# Find  outputs  (Home  work)
print(eval("    'hyd'   "))
hyd = 'Sec'
print(eval('hyd'))
sec = '25'
print(eval('sec'))
print(eval(sec))
cyb = 10.8
print(eval('cyb'))
print(eval(cyb))


#  Find  output  (Home  work)
print(eval('print("Hyd")'))
[11:10, 24/2/2025] +91 99482 50500: #  Find  outputs  (Home  work)
print(bool('False'))
print(eval('False'))
print(bool(''))
print(eval('  ""  '))
print(eval(''))
print(eval('  " "   '))
print(eval(' '))

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))
print(x)

 # Which  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))
print(a)
b = eval(input('Enter   any  string  : '))
print(len(b))
print(b)

# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t')
print(a , b , c , sep = '---')
print(a , b , c , sep = '\n')
print(a , b , c)
print(a , b , c , separator = ':')




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
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')
print(a , b , c , sep = ',,,')
print(a , b , c , sep = ':::' , end = '\t\t\t')
print(a , b , c)

# Find outputs  (Home  work)
print('Hyd')
print()
print('Sec')
print()
print('Cyb')

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)

 #  Find  outputs (Home  work)
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

 # Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)
print('%10.3f'  %a)
print('%.2f'  %a)
print('%.6f'  %a)
print('%f'  %a)

 # Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4  spaces>
print('%2s'  %a)
print('%s'  %a)
print('%s' , a)
print('%s'  a)
print('%s' , %a)
print(a)

 # Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)
print('%s' , a)
print('%s'  a)
print('%s' , %a)
print('%l'  %a)
print(a)

 #Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))
print('%i    %g    %s'    %(a , b , c))
print('%s    %s    %s'  %(a , b , c))
print('%d    %g    %s'  , a , b , c)
print('%d    %g      %s'   a , b , c)
print('%d    %g    %s'  ,  %(a , b , c))
print('%d    %g    %s'    %a%b%c)
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)

 #  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)
print(type(y))
x = 10.8
y = F'{x}'
print(y)
print(type(y))
x = [10,20,30,40]
y = F'{x}'
print(y)
print(type(y))

 #Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}')
print(F'{a:}  \t   {b:}   \t  {c:}')
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')
print(F'a  =  a  \t  b  =  b  \t  c  =  c')
print(F'{x =}  \t   {y =}   \t  {z =}')

 #  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')
print(F'{{{{{x}}}}}')
print(F'{{{{{{x}}}}}}')
print(F'{{{{{{{x}}}}}}}')
print(F'{{{{{{{{x}}}}}}}}')



'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''
