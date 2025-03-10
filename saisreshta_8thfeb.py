program1:
Write  a  program  to  merge  two  strings  to  form  a  new  string
a=input('Enter the first string:')
b=input('Enter the second string:')
num = min(len(a),len(b))
c=''
for i in range(num):
    c=c+a[i]+b[i]
if len(a)>len(b):
    print(f'Result:{c+a[num:]}')
else:
    print(f'Result:{c+b[num:]}')
Output:
Enter the first string:HYD
Enter the second string:VAMSI
Result:HVYADMSI

program2:
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
a=input('Enter any string:')
out=''
for x in a:
	if x not in out:
		out=out+x
		print(f'string without duplicants:{out}')
output:
Enter any string:Rama Rao
string without duplicants:R
string without duplicants:Ra
string without duplicants:Ram
string without duplicants:Ram
string without duplicants:Ram o

program3:
# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) #8
print(len('9247'))#4
print(len('+-$'))#3 
print(len('')) #0
print(len(' ')) #1
print(len('A2#')) #3
print(len(3456)) #error because it is not a sequence 
print('Sec'. len()) #error because there is no length method in string 

program4:
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90)) #Z
print(chr(97)) #a
print(chr(122))#z
print(chr(48))#0
print(chr(57)) #9
print(chr(36)) #$
print(chr(32)) #space

program5:
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))  #90
print(ord('a')) # 97
print(ord('z')) #122
print(ord('0')) #48
print(ord('9')) #57
print(ord('$')) #36
print(ord(' ')) #32

