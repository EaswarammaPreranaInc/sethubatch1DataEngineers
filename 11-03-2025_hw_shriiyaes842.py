# 1. isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace()) #False
print('\n  \t' . isspace())  #True
print('\n  7\t' . isspace()) #False
print('\n' . isspace())      #True
print('\n  $\t' . isspace()) #False
print('\t' . isspace())      #True
print('' . isspace())        #***False***
print(' ' . isspace())       #True
'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  not  a  white  space  
                                          i.e.  Alphabet, digit (or)  special  character
'''

'''
2. Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  ---> Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  --->  Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->   White  space

7) What  is  the  output  if  input   is   <enter>   key ?  --->  White  space #Here it is \n

8) Hint1:  Use  isalnum() , isalpha() , isupper() , islower() , isdigit()   and  isspace()  methods

9) Hint2:  Use  nested  if  and   elif
'''
a=input("Enter a character")
if a.isalpha():
	print("Alphabet character")
	print("Alphanumeric  character")
	if a.isupper():
		print("Upper case  alphabet")
	else:
		print("Lower case  alphabet")
elif a.isdigit():
	print("Alphanumeric  character")
	print("Digit character")
elif a.isspace() or '\n': # or a=='' as it is reading empty string when enter is pressed**This is actual but ok
	print("White  space")
else: 
	print("Special  character")

'''
3. Write  a  program  to  reverse  a  string  without  slice

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
  ---------------------------------------------
Enter  any  string : Rama Rao
Reverse  String :   oaR amaR
'''
a=input("Enter string")
b=""
for i in range(1,len(a)+1):
	b=b+a[-i]
print(b)

'''
4. Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

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
   --------------------------------------------------------
Enter  any  sententce : students are getting  bored
Reverse  order  of  words :  bored getting are students
'''
a=input("Enter string").split() #['Hyd' , 'is' , 'green' , 'city']
b=""
for i in range(1,len(a)+1):
	b=b+a[-i]+" "
print(b)

'''
5.Write  a  program  to  reverse  each  word  of  the  sentence
1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
Enter  any  sentence  :  hyd is green city
dyh si neerg ytic
'''
a=input("Enter string") # "Hyd is green city"
b=a.split() #['Hyd' , 'is' , 'green' , 'city']
c=""
for x in b:
	c=c+x[::-1]+" "  #***Very imp***
print(c)

'''
6. Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS

Hint:  Use   sorted()  function  and   join()  method
Enter  any  string  :  RAJESH
Sorted  string  :    AEHJRS
'''
a=input() #"hello"
b=sorted(a) #['e', 'h', 'l', 'l', 'o']
print("".join(b))

# 7. Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))  #a  :  25  \t  b  :  10.8  \t  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) #***a  :  25		b  :  10.8      c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) #***a  :  Hyd	b  :  10.8		c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) #***a  :  Hyd	b  :  Hyd	c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) #a  :  25  \t  b  :  10.8  \t  c  :  Hyd 
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #a  :  Hyd  \t  b  :  10.8  \t  c  : 25  
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #a  :  25  \t  b  :  25  \t  c  : 25 

'''
8. Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51A
What  is  the  output ?  ---> ADKPZ13579
1) Hint:  sorted()  function , isalpha() , isdigit()  and   join()  method 
'''
n=input()	
a,d="",""
for x in n:
	if x.isalpha():
		a=a+x
	elif x.isdigit():
		d=d+x
	else:
		print("Enter digits and alphabets only")
		exit()
c=sorted(a)+sorted(d)
print("".join(c))

# 9. What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ') #[25 , 10.8 , 'Hyd' , True]
print(type(a)) # *****<class 'str'>*****
print(a)       # [25 , 10.8 , 'Hyd' , True]
b = eval(a)    
print(b)       # [25 , 10.8 , 'Hyd' , True]
print(type(b)) # <class 'list'>	

# 10. Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a ##[10, 20, 15, 18]
print(a  is  b) # ****True****
print(a  ==  b) # True
b[2] = 12      #Modifying list b is as good as modifying list b
print(a)        #*****[10, 20, 12, 18]

# 11. Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # **** [10 , 20 , 15 , 18, 100 , 200 , 150]
#print(a + 5) # **** ERROR, can only concatenate list (not "int") to list***
#print(a + '5') # ERROR can only concatenate list (not "str") to list
#print([10 , 20] + (30 , 40)) #***Error, can only concatenate list (not "tuple") to list

# 12. Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list 
print('x : ' , x) # x : 25
print('y : ' , y) # y : [10.8 , 'Hyd' ,  True]
*p , q = list
print('p : ' , p) # p : [25 , 10.8 , 'Hyd']
print('q : ' , q) # q : True

# 13. Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list  # ERROR-->not enough values to unpack (expected 5, got 4)-->due to few elements in list
a , b , *c , d , e = list
print('a : ' , a) # 25
print('b : ' , b) # 10.8
print('c : ' , c) # *** [] ***
print('d : ' , d) # Hyd
print('e : ' , e) # True
#a , b , *c , d , e , f = list #Error-->not enough values to unpack (expected at least 5, got 4)-->due to few elements in list
#  * can be zero(emptylist) or more

# 14. Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list 
print('a : ' , a) # a:25
print('b : ' , b) # b:10.8
print('_ :  ' , _)  # _: 'Hyd***
print('d : ' , d) #d:True
#'_' means anonymous object or nameless object

# 15. Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list 
print('a : ' , a) # a: (3+4j) *imp*
print('b : ' , b) # b: 10.8
print('d : ' , d) # d: True

# 16. Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) #a: 25
print('b : ' , b)#b: 10.8
print('_ : ' , _)# _ : (3+4j)
print('d : ' , d)# d: True
print('_: ' , _) #_ : (3+4j)

# 17. Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' ,22, True , 3 + 4j]
a , *b , c , *d , e  = list # Cant have two *variables--> multiple starred expressions in assignment

# 18. Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # a: 25
print('b : ' , b) # b: 10.8
print('c : ' , c) # c: 'Hyd' 
print('d : ' , d) # d: True
#a , b , c , d = list #not enough values to unpack (expected 4, got 3)-->due to few elements in 'list'

# 19. Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)   # True
print(a  is   b)# True        **** List is mutable and not reusable
print(a < c)    # True    **** first not matching elements 15<25
print(a > d)    # True 15>7
print(a >= c)   #False 15 is not >= 25
print(a <= d)   #False 15 is not <= 7
print(a != c)   # True  15!=25
print(a != b)   # False due to same elements
print(a == c)   # False 15 is not equal to 25

# 20. Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)    # False 10!=20
print(a  is   b) # False bcoz a and b points to different lists
#first non matching elements are compared

# 21. len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True] 
print(len(a)) #4
b = []
print(len(b)) #0
c = [[10 , 20] , 30 , 40]
print(len(c)) #3
'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''

# 22. sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))       # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))       # 8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))       # ***(39.8+4j)
d = [10 , 20 , 15 , 18] 
print(sum(d))       # 63
e = [25 , 10.8 , 'Hyd' , True]
#print(sum(e))       # ERROR
'''
What  does  sum(list)  do ?  --->  Returns  sum  of  list  elements
'''

# 23. Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a))   #ERROR ---> Internally 0 + [10 , 20 , 15 , 18] not possible
#print(How  to  determine  sum  of  inner  list  elements)
print(sum(a[0])) #63

#print(How  to  determine  sum  of  inner  list  elements  in  another  way)
print(sum(*a))  #  **** Unpacks a to innerlist then use sum()

print((sum(x for x in a[0])))

s=0
for x in a[0]:
	s=s+x
print(s)

# 24. max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # 30
print(min(a)) # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) # Error due to complex number
d = [25 , '35']
#print(max(d)) #Error due to string and integer
#print(max([]))#Error,max() arg is an empty sequence
#print(min([]))#Error,min() arg is an empty sequence
'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''

# 25. list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)      # [10,20,15,18]
print(type(b)) #<class 'list'>
print(a  is  b) # False 
print(a == b)   #False

# 26. Find  outputs (Home  work)
a = range(4 , 10 , 2) ## 4,6,8
b = list(a)          
print(b)         # [4,6,8]
print(type(b))   # <class 'list'>
a = list('Vamsi')
print(a)         # ['V','a','m','s','i']
a = list()
print(a)         #[] Empty list
#print(list(25))  #*** ERROR,'int' object is not iterable--->not a sequence
#print(list(10.8))#*** ERROR,'float' object is not iterable  --->not a sequence
#print(list(True)) #***ERROR, 'bool' object is not iterable  --->not a sequence
#print(list(None))# *** ERROR, 'NoneType' object is not iterable --->not a sequence
'''
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list
2) What  does  list(no-args)  do ?  --->  Returns  an  empty  list
3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''

# 27. Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))  #nested tuple
print(list(a))	# [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)] -->converts nested tuples to list of tuples
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)} #set of tuples
print(list(b))  # [(30, 40, 50), (60, 70, 80, 90), (10, 20)] or [(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
                 #     ***    ---> converts set of tuples tuples to list of tuples--> order may change
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))  # [[10 , 20] , (30 , 40) , {50 , 60}] converts nested sequence to list of sequence
                  # tuple        tuple    set->or {60,50}

# 28. Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)   #['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c)   #['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) #['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

# 29. all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))		# True 
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))       # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))       # *FALSE --> 3rd element is empty string i.e. False
d=[10,0,20]
print(all(d))       # *False due to 0
e = []
print(all(e))       #True bcoz there are no False elements in list'e' -->**Empty list is True in all()
'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise
2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False
3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  above  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):
'''

# 30. any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))	# True due to 2nd element is True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))	# False , no element is True
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))   # True due to 4th elemnt is nonzero           **Atleast one is False, it is True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))   # False
e = []
print(any(e))            #False , no True elements is list'e'   ** Empty list is False in any()
'''
any()   function
-------------------
1) What  does  any(list)  do ?  --->  Returns  True  when  at  least  one  element  of  the  list  is  True  and  False  otherwise
2) When  does  it  return  False ?  ---> When  every  element  of  the  list  is  false
3) if  cond1  or  cond2  or  cond3  or  cond4:
     How  to  reduce  the  above  four  conditions  to  a  single  condition ?  --->   if  any([cond1 , cond2 , cond3 , cond4]):
4) all()  and  any()  functions  are  used  as  an  alternative  when  there  are  too  many  conditions  in  if  and  while
'''

# 31. Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) # a: [25 , 10.8] 
print('b :  ' , b) # b: 'Hyd' 
print('c :  ' , c) # c: True