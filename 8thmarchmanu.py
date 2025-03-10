
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

#3) len()  function  demo  program  (Home  work)

print(len('Hyd'))  #   Returns  number  of  characters  in  the  string-3
print(len('Rama Rao')) # Returns  number  of  characters  in  the  string-8 
print(len('9247'))# Returns  number  of  characters  in  the  string-4
print(len('+-$')) # Returns  number  of  characters  in  the  string-3
print(len('')) # Returns  number  of  characters  in  the  string-0
print(len(' ')) # Returns  number  of  characters  in  the  string-1
print(len('A2#')) # Returns  number  of  characters  in  the  string-3
print(len(3456)) # Error due to for integer cannot have length
print('Sec'. len())# Error due to string has no lenth in side the function


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

#6)


