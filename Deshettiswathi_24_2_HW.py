'''
# eval()  function  demo  program
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False'))  # False 
print(eval('3+4j'))   #3+4j
print(eval("    'Hyd'   ")) #Hyd
print(eval('3 + 4 * 5'))    # 23
print(eval('[10 , 20 , 15 , 18]')) # [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}')) # {10,15,20,12,18}
print(eval('(10 , 20 , 30)'))   #(10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) #{10 : 'Sec'}
print(eval(4 + 5)) #error
 




eval()  function
------------------
1) What  does  eval()  function  do ?  --->  Converts  string  to  appropriate  object

2) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer

    What  does  float(x)  do  ?  ---> Converts   object  'x'   to  float
    What  does  complex(x)  do  ?  ---> Converts   object  'x'  to  complex  number
    What  does  bool…


# Gift
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #hyd
hyd = 'Sec'   
print(eval('hyd'))  #Sec
sec = '25'   
print(eval('sec'))  #25
print(eval(sec))    #25
cyb = 10.8          #
print(eval('cyb'))  #10.8
print(eval(cyb))    #error the value mst be string i.e. '10.8'


#  Gift
#  Find  output  (Home  work)
print(eval('print("Hyd")'))   #hyd

#  Find  outputs  (Home  work)
print(bool('False'))   #True 
print(eval('False'))   #False
print(bool(''))        #false
print(eval('  ""  '))  # empty
#print(eval(''))        #error because no expression inside string
print(eval('  " "   ')) #empty
#print(eval(' '))        # error - no expression inside string 


# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) 
print(type(x))  # class of respective input
print(x) # prints the input

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
print(a , b , c , sep = '\t')   #25	10.8	Hyd
print(a , b , c , sep = '---')  #25---10.8---Hyd
print(a , b , c , sep = '\n')   #25 <nl> 10.8 <nl> Hyd
print(a , b , c)                #25 10.8 Hyd -->default seperator is space 
print(a , b , c , separator = ':') #error - sep but no seperator





1) What  is  the  default  separator  for  print()  function ?  --->  Space

2) Can  separator  be  modified  ? --->  With  sep  argument  of print()  function

3) What  does  sep = 'delimeter'  do ?  --->  Modifies  the  separator  to  the  specified  delimeter

4) print(object , sep = ' , ')
    Is  sep  argument  required  in  the  above  print()  function ?  ---> No  becoz  single  object  is  being  printed

5) When  is  sep  argument  required  in  print()  function  ?  --->  When…


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')    #25 10.8 Hyd---
print(a , b , c , sep = ',,,')    #25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')  #25::: 10.8 ::: Hyd
print(a , b , c)  #25 10.8 Hyd

output of above program
25 10.8 Hyd---25,,,10.8,,,Hyd
25:::10.8:::Hyd  <three tab spaces>    25 10.8 Hyd


# Find outputs  (Home  work)
print('Hyd') #Hyd
print()     # empty
print('Sec') # Sec
print()      #empty
print('Cyb')  #Cyb


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)   #[10 , 20 , 30 , 40]  (10 , 20 , 30 , 40)  {10 , 20 , 30 , 40} - default seperator is space


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)      #25.000000
print(type(b)) #<class 'str'>
x = 10.8
y = '%d'  %x   #10
print(y)       #10
print(type(y)) #<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m   #[10,20,15,18]
print(n)       #[10,20,15,18]
print(type(n)) #<class 'str'>


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)  #  <5 spaces> 10.9
print('%10.3f'  %a) #  <4 spaces> 10.927
print('%.2f'  %a)   #  10.93
print('%.6f'  %a)   #  10.927400
print('%f'  %a)     #  10.927400


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd  - spaces are added because 7>3(length of string-hyd) - means reserve atleast 7 spaces for string
print('%-7s'  %a)  #  Hyd<4  spaces>  - left align the text within 7 spaces.  -7 so spaces after the text
print('%2s'  %a)   #  Hyd   - no spaces becasue 2 < 3(len) - %2 means reserve atleast 2 chars, already 3 chars are there no need extra spaces.
print('%s'  %a)    # Hyd 
print('%s' , a)    # %s Hyd
#print('%s'  a)     #error- comma is not there between s and a 
#print('%s' , %a)   #error
print(a)           #Hyd


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)  # converts to string - [10 , 20 , 30 , 40]
print('%s' , a)  # %s [10 , 20 , 30 , 40]
#print('%s'  a)   # error- comma missing
#print('%s' , %a) #error - should not use comma, invalid syntax
#print('%l'  %a)  # error invalid format specifier
print(a) #[10 , 20 , 30 , 40]


#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd' 
print('%d    %f    %s'  %(a , b , c))  # 25 10.927400 Hyd
print('%i    %g    %s'    %(a , b , c)) #25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c))   # 25 10.9274 Hyd
print('%d    %g    %s'  , a , b , c)   #%d %g %s 25 10.9274 Hyd
#print('%d    %g      %s'   a , b , c) 
#print('%d    %g    %s'  ,  %(a , b , c)) #error
#print('%d    %g    %s'    %a%b%c)        #error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) #25 10.927400 Hyd


#  Find  outputs  (Home  work)
x = 25
y = F'{x}' 
print(y)   #25.0
print(type(y)) #calss 'str'
x = 10.8
y = F'{x}' 
print(y)   #10.8
print(type(y)) #class 'str'
x = [10,20,30,40]
y = F'{x}'
print(y)      #  [10,20,30,40]
print(type(y)) #class 'str'


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')   #25	10.8	Hyd 
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #a = 25	b = 10.8	c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') #a=25	b=10.8	c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') #a:25	b:10.8	c:Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') #a = {a}	b = {b} c = {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')   #a = a	b = b c = c
#print(F'{x =}  \t   {y =}   \t  {z =}')  #error


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}') #{{25}}
print(F'{{{{{{x}}}}}}') #{{{x}}}
print(F'{{{{{{{x}}}}}}}') #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}') #{{{{x}}}}


1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''
