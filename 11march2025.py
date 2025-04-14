# write a program to determine user input is alphabet ,digit,white space,or special character 
"""
a=input("enter the value : ")
if (a.isalpha() and a.isupper()):
    print(" the in put is alphabet , uppercase ")
elif (a.isalpha() and a.islower()):
    print(" the in put is alphabet , lower case ")
elif a.isdigit():
    print(" the input is digit ")
elif (a.isalnum()):
    print(" the input is digit , alphanumeric ")
elif a.isspace():
    print(" white space ")
else:
    print(" special character ")

if a.isupper():
    print("Alpha numberic character , alphabet character , Upper case alphabet ")
elif a.islower():
    print("Alpha numeric character , Alphabet character , lower case alphabet ")
elif a.isdigit() and a.isalpha():
    print("alpha numeric character ,digit character ")
elif a.isdigit():
    print("")
elif a.isspace():
    print("white space ")
else :
    print("special charqcter")
"""

# write a program to reverse a string without using slice
'''
a=list(input("enter the value : "))
for j in range (len(a)-1,-1,-1):
    print(a[j],end="")'''

# write a program to reverse oreder of words in the sentence without slice
'''
a=list(input("enter the value : ").split())
for j in range (len(a)-1,-1,-1):
    print(a[j],end=" ")
'''
# write a program to reverse each word of the sentence
'''
a=list(input("enter the value : ").split())
for i in a:
    b=i[::-1]
    print(b,end=" ")'''

# write a program to sort string in alphabetical order
'''
a=input("enter the string : ")
b=sorted(a)
for i in b:
    print(i,end="")'''

# WRITE A PROGRAM TO SORT STRING SUCH THAT ALPHABETS IN ALPHABETICAL ORDER AND DIGITS IN ASCENDING ORDER
'''
a=input("enter the value : ")
b=sorted(a)
c,d=[],[]#'',''
for i in range(len(b)): #for i in b:
    if b[i].isalpha():  # if i.isalpha():
        c+=b[i]         #c+=i
        #print(b[i],end="")
    elif b[i].isdigit(): #elif i.isdigit():
        d+=b[i]          #d+=i
        #print(b[i],end="")
    else:
        print("enter the only integers and alphabets ")
e=c+d 
#print(e)
for i in e:
    print(i,end="")

'''

## any()  function demo program  (Home  work)
'''
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))#true
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))#false
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))#true
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))#false
e = []
print(any(e))#false

'''

# all()  function demo  program  (Home  work)
'''
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))#true
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))#false
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))#false
d = [10 , 0 , 20]
print(all(d))#false
e = []
print(all(e))#true

'''
# Find  outputs  (Home  work)
'''
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)#['amar','kiran','rajesh','rama','rama rao','sita','vamsi']
c = sorted(a , reverse = True)
print(c)#['vamsi','sita','rama rao','rama','rajesh','kiran','amar']
print(a)#['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
'''
#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)#[4,6,8]
print(type(b))#<class 'list'>
a = list('Vamsi')
print(a)#['v','a','m','s','i']
a = list()
print(a)#[]
#print(list(25))#error
#print(list(10.8))#[10.8]
#print(list(True))#[true]
#print(list(None))#[none]


'''
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  --->  Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''