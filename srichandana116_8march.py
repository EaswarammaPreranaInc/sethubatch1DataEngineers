#Write  a  program  to  merge  two  strings  to  form  a  new  string
a=input("enter a string")
b=input("enter b string")
c=''
d=min(len(a),len(b))
for i in range(d):
    c=c+a[i]+b[i]
if len(a)!=d:
    c=c+a[d:]
elif len(b)!=d:
    c=c+b[d:]
print(c)
##Enter  any  string  with  alternate  character  and  digit
a=input("Enter  any  string  with  alternate  character  and  digit:")
b=''
print(a[0],a[1])
try:
    for i in range(0,len(a)-1,2):
        b=b+a[i]+chr(ord(a[i])+int(a[i+1]))
    print("RESULT:",b)
except:
    print("Pls  enter  string  with  alternate  char  and  digit")
#
print(chr(90))
print(chr(97))
print(chr(122))
print(chr(48))
print(chr(57))
print(chr(36))
print(chr(32))
#
print(len('Hyd'))  #  3
print(len('Rama Rao')) 
print(len('9247'))
print(len('+-$')) 
print(len('')) 
print(len(' ')) 
print(len('A2#')) 
#print(len(3456)) 
#print('Sec'. len())
#
#Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
a=input("enter a string")
c=''
for i in range(len(a)):
    if a[i] in a and a[i] not in c:
        c=c+a[i]
print(c)
