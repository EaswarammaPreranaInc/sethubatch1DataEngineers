Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  ---> Alphanumeric  character , Alphabet character , Upper case  alphabet
2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  --->  Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->   White  space

7) What  is  the  output  if  input   is   <enter>   key ?  --->  White  space

c=input("Enter any character:")
if c.isalnum():
  print("Alpanumeric character")
if c.isalpha():
  print("Alphabet character")
if c.isupper():
    print("upper case alphabet")
elif c.islower():
     print("lower case alphabet")
elif c.isdigit():
        print("digit character")
elif c.isspace():
	 print("white space")
else:
  print("special character")
OUTPUT:
Enter any character:A
Alpanumeric character
Alphabet character

Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  ---> dyH

2)   H       y      d
      -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1         'd'            '' + 'd' = 'd'
     2         'y'            'd' + 'y' = 'dy'
     3         'H'            'dy' + 'H' = 'dyH'

d=input("Enter any string:")
b=""
i=1
print("Reverse string:")
for c in d:
  b+=d[-i]
  i+=1
print(b)
OUTPUT:
Enter any string:Hyd
Reverse string:
dyH

Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
    1         'city'       '' + 'city' + ' ' =  'city '
    2         'green'    'city ' + 'green' + ' ' =  'city green '
    3         'is'           'city green ' + 'is' + ' ' = 'city green is '
    4         'Hyd'       'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '
a=input("Enter any string:")
c=""
b=a.split()
print("Reverse order of words:")
for i in range(1,len(b)+1):
 if i==len(b):
  c+=b[-i]
 else:
  c+=b[-i]+" "
print(c)
OUTPUT:
Enter any string:Hyd is green city
Reverse order of words:
city green is Hyd

Enter any string:Students are getting bored
Reverse order of words:
bored getting are Students

Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic
a=input("Enter any string:")
b=sorted(a)
print("Sorted string:")
c=''.join(b)
print(c)
OUTPUT:
Enter any string:RAJESH
Sorted string:
AEHJRS

Enter any string:SRAVANTHI
Sorted string:
AAHINRSTV
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579
a=input("Enter any string:")
b=c=""
for d in a:
  if d.isalpha():
   b+=d
  elif d.isdigit():
   c+=d
e=''.join(sorted(b))+''.join(sorted(c))
print(e)
OUTPUT:
Enter any string:Z9K3PA7D51
ADKPZ13579
