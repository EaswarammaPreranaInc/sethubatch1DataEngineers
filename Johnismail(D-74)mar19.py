# Keyword  only   arguments  demo  program
'''def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)#a:10 b:20
f1(b = 30 , a = 40)#a:40 b:30
#f1(50 , 60)#error becoz after * we have to use keyword arguments only
#f1(70 , b = 80)#error
#f1(a = 15 , 25)#error becoz pa after ka'

#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)#a:10 b:20 c:30
f1(a = 40 , b = 50 , c = 60)#a:40 b:50 c:60
f1(c = 100 , b = 90 , a = 80)#a:80 b:90 c:100
#f1(70 , 80 , c = 90)#error
#f1(70 , 80 , 90)#error
#f1(c = 15 , b = 25 , 35)#error

# Identify error (Home  work)
def   f1(a  , b , *):#error becoz after '*' atleast one argument should be provided
        pass


#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)#a:10 b:20
#f1(a = 30 ,  b = 40)#error
#f1(50 , b = 60)#error
#f1(a = 70 , 80)#error


# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)#a:10 b:20 c:30
f1(40 , 50 , c = 60)#a:40 b:50 c:60
#f1(a = 70 , b = 80 , c = 90)#error a and b should be positional arguments only
#f1(a = 100 , b = 110 , 120)#error a and b should be positional arguments only
#f1(a = 130 , 140 , c = 150)#error  b should be positional arguments only
#f1(160 , b = 170 , 180)##error  b should be positional arguments only
#f1(190 , b = 200 , c = 210)#error  b should be positional arguments only

# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)#a:10 b:20 c:30 d:40 e:50 f:60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)#error b should be positional argument only
#f1(1 , 2 , 3 , 4 , 5 , f = 6)#error e should be keyword argument only
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)#error due to positional argument after keyword argument
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#a:10 b:20 c:30 d:40 e:50 f:60

# Identify error (Home  work)
#def  f1(/ , a , b ,  c):#before '/' atleast there should be one argument
       # pass
#def   f2(a , b , c , *):#after '*' atleast there should be one argument
        #pass
	
	# Identify  error  (Home  work)
def  f4(* , a , b , c , /):#error becoz positional arguments after keyword arguments
	        pass

	# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)#3rd  function :10
#f1(y = 20)#error
#f1(x = 30)#error

# Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d):#error becoz postional argument after keyword argument
	#pass
def   f2(b , d , a = 10 , c = 20):#no function call
	pass

#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)#20
f1()#a=10
f1(a = 30)#a=30

# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))#330
print(add(100 , 200 , 300))#620
print(add(100 , 200 , 300 , 400))#1000
print(add(b = 100 , a = 200))#330
print(add(100 , 200 , d = 300))#610
print(add(d = 100 , a = 200 , b = 300))#610
#print(add(c = 100 , d = 200 , 300 , 400))#error
#print(add(100 , 200 , c = 300 , x = 400))#error due to 'x'
#print(add())#error

#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))#10
print(f1())#25
print(f2(20))#20
#print(f2())#error


# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)#----
disp('$')#$$$$
disp()#****
disp(n = 5)#*****
disp(5)#20
disp(n = 7 , ch = '%')#%%%%%%%
disp(7 , '@')#@@@@@@@
disp(7 , n = 6)#42
#disp(ch = '!' ,  5)#error

# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5))#91.125
print(power(3 + 4j))#(-7+24j)
print(power(True))#1
#def   power(b = 2 , a):#function not called
 	# pass

# Find outputs  (Home  work)
def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40))#'4-argument  function' :100
print(add(50 , 60 , 70))#'4-argument  function':184
print(add(80 , 90))#'4-argument  function':177
print(add(100))#'4-argument  function':109
print(add())#'4-argument  function':10

# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)# a:10  b:20  c:30
#disp(40 , 50 , 60 , 70)#error
disp(80 , 90)#a:80 b:90 c=25

# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))#70
print(add())#30
print(add(a = 50))#70
print(add(b = 60 , a = 70))#130
print(add(80 , 90))#error

# Find  outputs(Home  work)
#def   add(a = 10 , b , c):#error
        #pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))#120
print(add(b = 60 , c = 70))#140
print(add(c = 80 , b = 90 , a = 100))#270
#print(add(c = 25 , a = 43))#error
#print(add(1 , 2 , 3))#error
#def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):#error
		#pass
# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . _defaults_)#error due to single underscore

# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(3)#'List : [3]
print('_defaults_  :  ' , f1.__defaults__)#([3],)
f1(4 , [1 , 2 , 3])#'List :[1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__)#([3,],)
f1(9)#'List :[3,9]
print('_defaults_  :  ' , f1.__defaults__)#([3,9],)
f1(40 , [10 , 20 , 30])#'List :[10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__)#([3,9],)
f1(5)#List:[3,9,5]
print('_defaults_  :  ' , f1.__defaults__)#([3,9,5],)
f1([6 , 7 , 8])#List:[3,9,5,[6,7,8]]
print('_defaults_  :  ' , f1.__defaults__)#([3,9,5[6,7,8]],)

#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(3)#[3]
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(4 , [1 , 2 , 3])#[1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(4)#[4]
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(40 , [10 , 20 , 30])#[10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(5)#[5]
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1([6 , 7 , 8])#[6 , 7 , 8]
print('_defaults_  :  ' , f1.__defaults__)#([],)

# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__)#([],)
print(f1(3))#[0,1,4]
print('_defaults  :  ' , f1.__defaults__)#([0,1,4],)
print(f1(4 , [10 , 20 , 15 , 18]))#[10,20,15,18,0,1,4,9]
print('_defaults  :  ' , f1.__defaults__)#([0,1,4],)
print(f1(5))#[0,1,4,0,1,4,9,16]
print('_defaults  :  ' , f1.__defaults__)#([[0,1,4,0,1,4,9,16]],)
print(f1(a = [100 , 200 , 300],   x = 6 ))#[100,200,300,0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__)#([[0,1,4,0,1,4,9,16]],)
print(f1(6))#[0,1,4,0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__)#([[0,1,4,0,1,4,9,16,0,1,4,9,16,25]],)

# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))#[0,1,4]
print(f1(4 , [10 , 20 , 15 , 18]))#[10,20,15,18,0,1,4,9]
print(f1(5))#[0,1,4,9,16]
print(f1(a = [100 , 200 , 300],   x = 6 ))#[100,200,300,0,1,4,9,16,25]
print(f1(6))#[0,1,4,9,16,25]

# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)#('Hyd',[])
f1()#hydsec [1,2,3]
print('Default Values  :  ' , f1 . __defaults__)#('Hyd',[1,2,3])
f1()#hydsec [1,2,3,1,2,3]
print('Default Values  :  ' , f1 . __defaults__)#('hyd'[1,2,3]
f1()#hydsec [1,2,3,4]

Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
																		   2
																		   3
																		   5
																		   7
																		   Number  of   prime  numbers : 4

How  to  read  a  number
How  to  print  all  prime  numbers  between  2  and  user  input
print('Number  of  prime numbers  :  ' ,  ???)'''

write a program to print prime numbers bwtween 2 to n

n=int(input('enter any number:'))			
def f2():
		c=0
		for i in range(2,n+1):
				i+=1
				for j in range(2,i//2+1):
						if i%j==0:
								
								break
				else:
					print(i,end=' ')
					c+=1
		return c
if n<1:
		print('invalis')
else:
	print(f'count:{f2()}')
outputs----
enter any number:20
3 5 7 11 13 17 19 count:7
