'''
1.Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
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
print('Number  of  prime numbers  :  ' ,  ???) '''

from Prime import prime
a=int(input("enter a number: "))
count=0
print("Prime Numbers") 
for x in range(2,a+1):
	if prime(x): # checks if its prime num
		print(x)
		count+=1
print("Number of prime numbers :",count)

# 2.Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) #a:10	b:20
f1(b = 30 , a = 40) #a:40	b:30
#f1(50 , 60) # positional arguments are not allowed  f1() takes 0 positional arguments but 2 were given
#f1(70 , b = 80) # positional arguments are not allowed  f1() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given
#f1(a = 15 , 25) # Positional argument follows keyword  argument 

#3.Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # a:10	b:20	c:30
f1(a = 40 , b = 50 , c = 60)#a  :  40          b :  50         c  :  60
f1(c = 100 , b = 90 , a = 80)#a  :  80          b :  90         c  :  100
#f1(70 , 80 , c = 90) # error f1() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
#f1(70 , 80 , 90)# error f1() takes 1 positional argument but 3 were given
#f1(c = 15 , b = 25 , 35)# positional argument follows keyword argument 

# 4. Identify error (Home  work)
#def   f1(a  , b , *): # no arguments after * named arguments must follow bare *
        #pass
# 5. Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) #a:10	b:20
#f1(a = 30 ,  b = 40) # error only positional arguments are allowed  f1() got some positional-only arguments passed as keyword arguments: 'a, b'
#f1(50 , b = 60) # error only positional arguments are allowed f1() got some positional-only arguments passed as keyword arguments: 'b'
#f1(a = 70 , 80) # positional argument is followed by keyword arguments 

# 6. Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a:10	b:20	c:30
f1(40 , 50 , c = 60)# a  :  40          b :  50         c  :  60
#f1(a = 70 , b = 80 , c = 90)#  f1() got some positional-only arguments passed as keyword arguments: 'a, b'
#f1(a = 100 , b = 110 , 120) # error ka before pa
#f1(a = 130 , 140 , c = 150)# error positional argument follows keyword argument
#f1(160 , b = 170 , 180)#keyword argument should be at the end  positional argument follows keyword argument
#f1(190 , b = 200 , c = 210)#error f1() got some positional-only arguments passed as keyword arguments: 'b'

# 7. Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) #a:10	b:20	c:30	d:40	e:50	f:60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)# error b should be a positional argument  f1() got some positional-only arguments passed as keyword arguments: 'b'
#f1(1 , 2 , 3 , 4 , 5 , f = 6) # error  e should be a pa f1() takes 4 positional arguments but 5 positional arguments (and 1 keyword-only argument) were given
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) #error ka should be after pa
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#a:10	b:20	c:30	d:40	e:50	f:60

# 8. Identify error (Home  work)
#def  f1(/ , a , b ,  c): # nothing before / at least one argument must precede /
        #pass
#def   f2(a , b , c , *): # no arg after *  named arguments must follow bare *
       # pass 
# 9. Identify  error  (Home  work)
#def  f4(* , a , b , c , /): # both pa and ka are not possible  / must be ahead of *
	       # pass
# 10. Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)#3rd  function :  10
#f1(y = 20)#error 
#f1(x = 30)#f1() got an unexpected keyword argument 'x'

# 11. Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d):parameter without a default follows parameter with a default
	#pass
def   f2(b , d , a = 10 , c = 20):
	pass
#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)#20 
f1()#10
f1(a = 30)#30

# 12. Find  outputs (Home  work) 
def  add(a , b , c = 10 , d = 20): # default arguments c and d
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # 330
print(add(100 , 200 , 300)) #620
print(add(100 , 200 , 300 , 400)) #10000
print(add(b = 100 , a = 200))#330
print(add(100 , 200 , d = 300))#610
print(add(d = 100 , a = 200 , b = 300))#610
#print(add(c = 100 , d = 200 , 300 , 400))#positional argument follows keyword argument
#print(add(100 , 200 , c = 300 , x = 400)) # error x is not there  add() got an unexpected keyword argument 'x'
#print(add()) #error a and b ?  add() missing 2 required positional arguments: 'a' and 'b' 

# 13. Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))#10 next line none 
print(f1()) # 25
print(f2(20)) #20
#print(f2()) # error need an argument f2() missing 1 required positional argument: 'x'

# 14. Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) #------
disp('$') #$$$$
disp()#****
disp(n = 5)#*****
disp(5) #20
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # @@@@@@@
disp(7 , n = 6) #42
#disp(ch = '!' ,  5) # positional argument follows keyword argument

# 15. Find  outputs (Home  work) 
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6)) # 2^6 =64
print(power(5)) #5^2 =25
print(power(b = 3 , a = 4.5)) #4.5^3 =91.125
print(power(3 + 4j)) #(-7+24j)
print(power(True)) #  1^2 =1
#def   power(b = 2 , a): #error  parameter without a default follows parameter with a default
 	# pass 

# 16. Find outputs  (Home  work)
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
print(add(10 , 20 , 30 , 40)) # '4-argument  function' next line 100
print(add(50 , 60 , 70)) #'4-argument  function' next line 184
print(add(80 , 90)) # '4-argument  function' next line 177
print(add(100))#'4-argument  function' next line 109
print(add())#'4-argument  function' next line 10

# 17. Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :   10 20 30
#disp(40 , 50 , 60 , 70) #Error we need only 3 arguments  disp() takes from 2 to 3 positional arguments but 4 were given
disp(80 , 90) # 3-argument  function  :  80 90 25
# 18.Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) #70
print(add())#30
print(add(a = 50)) #70
print(add(b = 60 , a = 70)) #130
#print(add(80 , 90)) # add() takes 0 positional arguments but 2 were given

# 19.Find  outputs(Home  work)
#def   add(a = 10 , b , c): #parameter without a default follows parameter with a default
        #pass
def   add( * , a = 10 , b , c ): #Since Python enforces keyword-only arguments here, the usual default-before-non-default error does not apply.
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))  #120
print(add(b = 60 , c = 70)) #140
print(add(c = 80 , b = 90 , a = 100)) #270
#print(add(c = 25 , a = 43)) # argument b is missing 
#print(add(1 , 2 , 3)) # need ka 
#def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f): # default arg should after non default arguments  parameter without a default follows parameter with a default
		#pass
# 20. Find  output (Home  work) 
def   f1(a = []):
        pass
print(f1 . __defaults__) #([],) 

# 21. Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__) #([],)
f1(3) #List : [3] 
print('_defaults_  :  ' , f1.__defaults__) #([3],)
f1(4 , [1 , 2 , 3]) #List : [1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__) # ([3],)
f1(9) # List : [3,9]
print('_defaults_  :  ' , f1.__defaults__) #([3,9],)
f1(40 , [10 , 20 , 30]) # List : [10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__) # ([3,9],)
f1(5) # List : [3,9,5]
print('_defaults_  :  ' , f1.__defaults__) # ([3,9,5],)
f1([6 , 7 , 8]) # List : [3,9,5,[6 , 7 , 8]]
print('_defaults_  :  ' , f1.__defaults__) # ([3,9,5,[6 , 7 , 8]],) 

# 22. Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__) #([],)
f1(3) # [3]
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(4 , [1 , 2 , 3]) # [1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__) ##([],)
f1(4) #[4]
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(40 , [10 , 20 , 30]) #[10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(5)# [5]
print('_defaults_  :  ' , f1.__defaults__) #([],)
f1([6 , 7 , 8]) #[[6,7,8]]
print('_defaults_  :  ' , f1.__defaults__)#([],)


# 23. Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__) #([],)
print(f1(3)) #[0,1,4]
print('_defaults  :  ' , f1.__defaults__)#([0,1,4],)
print(f1(4 , [10 , 20 , 15 , 18])) # [10 , 20 , 15 , 18,0,1,4,9]
print('_defaults  :  ' , f1.__defaults__) #([0,1,4],)
print(f1(5)) # [0,1,4,0,1,4,9,16]
print('_defaults  :  ' , f1.__defaults__) ## ([0,1,4,0,1,4,9,16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))#[100 , 200 , 300,0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__) #([0,1,4,0,1,4,9,16],)
print(f1(6)) #[0,1,4,0,1,4,9,16,0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__)  #([0,1,4,0,1,4,9,16,0,1,4,9,16,25],)

# 24.Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3)) # [0,1,4] ,default not changed 
print(f1(4 , [10 , 20 , 15 , 18])) # [10 , 20 , 15 , 18,0,1,4,9]
print(f1(5)) #[0,1,4,9,16]
print(f1(a = [100 , 200 , 300],   x = 6 )) # [100,200,300,0,1,4,9,16,25]
print(f1(6)) #[0,1,4,9,16,25] 

# 25. Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)#('Hyd',[])
f1() # a :  HydSec next line b: [1,2,3]
print('Default Values  :  ' , f1 . __defaults__) #('Hyd',[1,2,3])
f1() # a: HydSec next line b: [1,2,3,1,2,3]
print('Default Values  :  ' , f1 . __defaults__)# (Hyd,[1,2,3,1,2,3])
f1() # a:HydSec next line b:[1,2,3,1,2,3,1,2,3]
'''
outputs:
Default Values  :   ('Hyd', [])
a :   HydSec
b :   [1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3] '''
