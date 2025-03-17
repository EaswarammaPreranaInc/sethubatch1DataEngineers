'''
prog-1 Write  a  program  to  merge  two  strings  to  form  a  new  string
a=input('enter a string:')
b=input('enter b string:')
c=""
i=0
m=min(len(a),len(b))
while i<m:
	 c+=a[i]+b[i]
	 i+=1
if m==len(a):
	 c+=b[m:]
elif m==len(b):
	 c+=a[m:]
	
print(c)
	
outputs---
enter a string:hyd
enter b string:vamsi
hvyadmsi


prog-2Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

                         #  0  1  2  3 4 5  6  7
a=input('enter a string:')#R  A  M  A   R  A  O
b=""#empty
i=0 
for i in range(len(a)):	 	 
	 if a[i] not in b:
		  b+=a[i]
print(b)
		 
OUTPUT---enter a string:RAMA RAO
RAM O  

# prog-3 len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) #8
print(len('9247'))#4
print(len('+-$')) #3
print(len('')) #0
print(len(' ')) #1
print(len('A2#')) #3
#print(len(3456)) #error due to object of type 'int' has no len()
print('Sec'. len()) #'str' object has no attribute 'len'


prog-4  ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))  #Unicode  value  of  'Z'  i.e.  90
print(ord('a'))  #Unicode  value  of  'A'  i.e.  97
print(ord('z'))  #Unicode  value  of  'A'  i.e.  122
print(ord('0'))  #Unicode  value  of  'A'  i.e.  48
print(ord('9'))  #Unicode  value  of  'A'  i.e.  57
print(ord('$'))  #Unicode  value  of  'A'  i.e.  36
print(ord(' '))  #Unicode  value  of  'A'  i.e.  32

prog-5 chr()  function  demo  program
print(chr(90))  #char value  value  of  90  i.e.  'A'
print(chr(97))  #char value  value  of  97  i.e.  'a'
print(chr(122)) #char value  value  of  90  i.e.  'z'
print(chr(48))  #char value  value  of  48  i.e.  '0'
print(chr(57))  #char value  value  of  57  i.e.  '9'
print(chr(36))  #char value  value  of  36  i.e.  '$'
print(chr(32))  #char value  value  of  32  i.e.  ' ' 

 prog-6  Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2


Iteration        i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                                              ''
     1               0       'A'         '4'             '' + 'A' + 'E' = 'AE'

	 2              2       'M'         '3'             'AE' + 'M' + 'P' = 'AEMP'

	 3              4       'Z'         '5'             'AEMP' + 'Z' + '' = 'AEMPZ'

	 4              6       'D'         '2'             'AEMPZ_' + 'D' +'F' = 'AEMPZ_DF'
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions 


a=input('enter any sting character with alternate digit:')
b=""

for i in range(0,len(a),2):#A2B3J2
	 b+=a[i]+chr(ord(a[i])+int(a[i+1]))
print(f'{b}')

outputs---
enter any sting character with alternate digit:a2b3h4
acbehl
'''


	
    
