# Write  a  program  to  merge  two  strings  to  form  a  new  string
1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI
1) What  action  to  be  made  when  1st  string  got  exhausted ?  --->  Concatenate  remaining  chars  of  2nd    string  to  object  'c'
2) What  action  to  be  made  when  2nd  string  got  exhausted ?  --->  Concatenate  remaining  chars  of  1st  string  to  object  'c'
3) Hint:  Use  while  loop  and  slice (outside)

a = input("Enter first string:")   # HYD
b = input("Enter second string:")   # VAMSI
C = ' '
i = 0
while i <= len(a) - 1 and i <= len(b) - 1:
        c += a[i] + b[i]
        i += 1
if len(a) > len(b):
        c += a[i:]
else:
        c += b[i:]
print('Result:', c)



# Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
1) Let  input  be   RAMA  RAO
    What  is  the  output ? --->  RAM<space>O
2) out = '' + 'R' + 'A' + 'M' + ' ' + 'O' = 'RAM O'
3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																						Concatenate  the  character  to  out  object
4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->  Ignore  the  character
5) Hint:  Use  not  in   operator

a = input("Enter any string:")
b = ''
for ch in a:
      if ch not in b:
              b += ch
print('String without duplicates:', b)



# len()  function  demo  program 

print(len('Hyd'))   # 3
print(len('Rama Rao'))   # 8
print(len('9247'))   # 4
print(len('+-$'))   # 3
print(len(''))   # 0
print(len(' '))   # 1
print(len('A2#'))   # 3
print(len(3456))   # Error becoz 3456 is not a sequence
print('Sec'. len())   # Error becoz there is no len() method in str class 



# chr()  function  demo  program

print(chr(65))   # A becoz 65 is unicode value of 'A'
print(chr(90))   # Z becoz 90 is unicode value of 'Z'
print(chr(97))   # a becoz 97 is unicode value of 'a'
print(chr(122))   # z becoz 122 is unicode value of 'z'
print(chr(48))   # 0 becoz 48 is unicode value of '0'
print(chr(57))   # 9 becoz 57 is unicode value of '9'
print(chr(36))   # $ becoz 36 is unicode value of '$'
print(chr(32))   # " " becoz 32 is unicode value of space character " "



# ord()  function  demo  program

print(ord('A'))   # Unicode value of 'A' i.e. 65
print(ord('Z'))   # Unicode value of 'Z' i.e. 90
print(ord('a'))   # Unicode value of 'a' i.e. 97
print(ord('z'))   # Unicode value of 'z' i.e. 122
print(ord('0'))   # Unicode value of '0' i.e. 48
print(ord('9'))   # Unicode value of '9' i.e. 57
print(ord('$'))   # Unicode value of '$' i.e. 36
print(ord(" "))   # Unicode value of '" "' i.e. 32



# Let  input  be  A4M3Z5D2
What  is  the  output ?  --->  AEMPZ_DF
0     1     2     3    4    5    6     7
A    4     M    3    Z    5    D     2
Iteration        i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
   1               0       'A'         '4'             '' + 'A' + 'E' = 'AE'
   2              2       'M'         '3'             'AE' + 'M' + 'P' = 'AEMP'
   3              4       'Z'         '5'             'AEMP' + 'Z' + '' = 'AEMPZ'
   4              6       'D'         '2'             'AEMPZ_' + 'D' +'F' = 'AEMPZ_DF' 
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions

try:
       a = input("Enter any string with alternate character and digit:")
       b = ' '
       for i in range (0, len(a), 2):
              b += a{i] + chr(ord(a[i]) + int(a[i + 1]))
       print('Result:', b)
except:
       print('please enter string with alternate char and digit')
















