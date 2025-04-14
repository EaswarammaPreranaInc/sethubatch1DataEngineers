
'''
#1)Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI

 a="HYD"
b="VAMSI"
c =((a[0]+b[0])+(a[1]+b[1])+(a[2]+b[2])) 
print(c+a[3]+a[4])

(or)

def merge_strings(string1,string2):
	merged =" "
	for a, b in zip(string1,string2):
		merged +=(a+b)
		return merged
string1 ="abc"
string2 ="12345"
result=merge_strings(string1,string2)
merge_strings(string1,string2)
print(result)

(or)
a= input('Enter 1st string:')
b=input('Enter 2nd string:')
c =" "
i=0
while i <=len(a)-1 and i<=len(b)-1:
	c +=a[i]+b[i]
	i +=1
if len(a)>len(b):
	c += a[i:]
else:
	c +=b[i:]
print('Result:',c)



#2)Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
    What  is  the  output ? --->  RAM<space>O

2) out = '' + 'R' + 'A' + 'M' + ' ' + 'O' = 'RAM O'

a= "RAMA RAO"
b= " "
for char in a:
	if char not in b:
		b= b+char
print(b)

(or)
a= input('Enter any string:')
b=" "
for ch in a:
	if ch not in b:
		b +=ch
print('String without duplicates :',b)


#3) len()  function  demo  program  (Home  work)

print(len('Hyd'))  #   Returns  number  of  characters  in  the  string-3
print(len('Rama Rao')) # Returns  number  of  characters  in  the  string-8 
print(len('9247'))# Returns  number  of  characters  in  the  string-4
print(len('+-$')) # Returns  number  of  characters  in  the  string-3
print(len('')) # Returns  number  of  characters  in  the  string-0
print(len(' ')) # Returns  number  of  characters  in  the  string-1
print(len('A2#')) # Returns  number  of  characters  in  the  string-3
print(len(3456)) # Error due to  3456 not a sequence 
print('Sec'. len())# Error due to there is no len/() method in string str


#4) chr()  function  demo  program

print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90)) #  Z   becoz  90  is  unicode  value  of  'Z'
print(chr(97)) #  a   becoz  97  is  unicode  value  of  'a'
print(chr(122)) # z   becoz  122  is  unicode  value  of  'z'
print(chr(48)) #  0   becoz  48  is  unicode  value  of  '0'
print(chr(57)) #  9   becoz  57  is  unicode  value  of  '9'
print(chr(36)) #  $   becoz  36  is  unicode  value  of  '$'
print(chr(32)) # space becoz  32  is  unicode  value  of  'space'

#5)ord()  function  demo  program

print(ord('A'))  #  Unicode  value  of  'A'  is  65
print(ord('Z'))  #  Unicode  value  of  'Z'  is  90
print(ord('a'))  #  Unicode  value  of  'a'  is  97
print(ord('z'))  #  Unicode  value  of  'z'  is  122
print(ord('0'))  #  Unicode  value  of  '0'  is  48
print(ord('9'))  #  Unicode  value  of  '9'  is  57
print(ord('$'))  #  Unicode  value  of  '$'  is  36
print(ord(' '))  #  Unicode  value  of  ' space'  is  32

#6)Let  input  be  A4M3Z5D2

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


x = input('Enter any string with alternate one charecter and one integer')
z = " "
for i in range (0,len(x),2):
	y = ord(x[i]) + int(x[i+1])
	z += x[i]+chr(y)
	print(z)


classwork
--------------
#1) Difference between function and method
----------------------------------------------
class c1:
	def m1(hyd):
		print('method')
		def m1(self):
            #end of the class
            def f1():
	            print('function')
                #end of the function
                a = c1()
                a.m1()
                #f1()
                f1()
                #a.f1()
                m1(a)


#2)Replace()
--------------

a='Hyd is green city. Hyd is hiteccity. Hyd is his city'
b = a.replace('is', 'was')
print(b)
print(a)

#3)l(L)strip(), rstrip(), strip()
----------------------------------

a= '   shanker Dayal Sharma   '
print(a.lstrip())
print(a.rstrip())
print(a.strip())
print(a)

#3) split()
------------

a='15-Aug-1947'
b= a.split('-')
print(b)
for x in b:
	print(x)

#4)join()
----------
a=['15','Aug','1947']
print('-'.join(a))
print(''.join(a))
print(' '.join(a))
#print(a.join(':'))

#5)Case conversion method
---------------------------------
a = 'hyD is grEen cITy'
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())
print(a)
print('A7$a'.upper())

#6)startswith()
---------------
'''
a= 'Hyderabad is green city'
print(a.startswith('Hyd'))
print(a.startswith('Sec'))
print(a.startswith('hyd'))
print(a.startswith('green',13))
















