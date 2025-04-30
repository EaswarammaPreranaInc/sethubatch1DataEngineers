#1 Program
'''Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing'''
CODE:
from prog1_prime import prime
n=int(input("enter n value:"))
count=0
for i in range(2,n+1):
	if prime(i):
		print(i)
		count+=1
print(f'Number of prime numbers:{count}')

'''
OUTPUT:
enter n value:10
2
3
5
7
Number of prime numbers:4
'''




#2  Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)  # a:10      b:20
f1(b = 30 , a = 40)  # a:40      b:30
#f1(50 , 60)          #f1() takes 0 positional arguments but 2 were given
#f1(70 , b = 80)       #f1() takes 0 positional arguments but 2 were given
#f1(a = 15 , 25)  #positional argument follows keyword argument

'''
OUTPUT:
a  :  10          b :  20
a  :  40          b :  30
'''




#3 Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)    # a:10   b:20   c:30
f1(a = 40 , b = 50 , c = 60) # a:40  b:50   c:60
f1(c = 100 , b = 90 , a = 80) # a:80  b:90  c:100
#f1(70 , 80 , c = 90) #Error because  f1() takes 1 positional argument but 2 positional arguments
#f1(70 , 80 , 90)     #Error because f1() takes 1 positional argument but 3 positional arguments 
#f1(c = 15 , b = 25 , 35) #positional argument follows keyword argument
'''
OUTPUT:
a  :  10          b :  20         c  :  30
a  :  40          b :  50         c  :  60
a  :  80          b :  90         c  :  100
'''




#4 Identify error (Home  work)
#def   f1(a  , b , *):    #  error because named arguments must follow bare *
        #pass





#5 Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)               #a  :  10          b  :  20
#f1(a = 30 ,  b = 40)     #f1() got some positional-only arguments passed as keyword arguments: 'a, b'
#f1(50 , b = 60)          #f1() got some positional-only arguments passed as keyword arguments: 'b'
#f1(a = 70 , 80)    #positional argument follows keyword argument
'''
OUTPUT:
a  :  10          b  :  20
'''





#6 Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)
f1(40 , 50 , c = 60)
#f1(a = 70 , b = 80 , c = 90)   #Error because f1() got some positional-only arguments passed as keyword arguments: 'a, b'
#f1(a = 100 , b = 110 , 120)    #Error because  positional argument follows keyword argument
#f1(a = 130 , 140 , c = 150)    #Error because  positional argument follows keyword argument
#f1(160 , b = 170 , 180)        #Error because  positional argument follows keyword argument
#f1(190 , b = 200 , c = 210)    #Error because f1() got some positional-only arguments passed as keyword arguments: 'b'
'''
OUTPUT:
a  :  10          b :  20         c  :  30
a  :  40          b :  50         c  :  60
'''




#7 Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) #Error because f1() got some positional-only arguments passed as keyword arguments: 'b'
#f1(1 , 2 , 3 , 4 , 5 , f = 6)                  #Error because f1() takes 4 positional arguments but 5 positional arguments (and 1 keyword-only argument) were given
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)   #Error because positional argument follows keyword argument
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)
'''
OUTPUT:
a  :  10          b  :  20        c  :  30        d  :  40        e  :  50        f  :  60
a  :  10          b  :  20        c  :  30        d  :  40        e  :  50        f  :  60
'''





#8 Identify error (Home  work)
#def  f1(/ , a , b ,  c):    #at least one argument must precede /
        #pass
#def   f2(a , b , c , *):     #named arguments must follow bare *
        #pass






#9 Identify  error  (Home  work)
#def  f4(*, a , b , c , /):   #/ must be ahead of *
	        #pass




#10 Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)
#f1(y = 20)  #Error because f1() got an unexpected keyword argument 'y'
#f1(x = 30)   #Error because f1() got an unexpected keyword argument 'x'
'''
OUTPUT:
3rd  function :  10
'''




#11 Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d):    #Error because parameter without a default follows parameter with a default
	#pass
def   f2(b , d , a = 10 , c = 20):
	pass




#12 Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)
f1()
f1(a = 30)

'''
OUTPUT:
20
10
30
'''




#13 Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))   #330
print(add(100 , 200 , 300))   #620
print(add(100 , 200 , 300 , 400))    #1000
print(add(b = 100 , a = 200))       #330
print(add(100 , 200 , d = 300))      #610
print(add(d = 100 , a = 200 , b = 300))    #610
#print(add(c = 100 , d = 200 , 300 , 400))   #Error because positional argument follows keyword argument
#print(add(100 , 200 , c = 300 , x = 400))   #Error  because  add() got an unexpected keyword argument 'x'
#print(add())   #Error because add() missing 2 required positional arguments: 'a' and 'b'
'''
OUTPUT:
330
620
1000
330
610
610
'''




#14 Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))   #10
print(f1())     #25
print(f2(20))   #20
#print(f2())     #Error because f2() missing 1 required positional argument: 'x'
'''
OUTPUT:
10
25
20
'''




#15 Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)   #------
disp('$')       #$$$$
disp()          #****
disp(n = 5)     #*****
disp(5)         #20
disp(n = 7 , ch = '%')   #%%%%%%%
disp(7 , '@')            #@@@@@@@
disp(7 , n = 6)          #42
#disp(ch = '!' ,  5)      #Error because positional argument follows keyword argument
'''
OUTPUT:
------
$$$$
****
*****
20
%%%%%%%
@@@@@@@
'''




#16 Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))   #2**6
print(power(5))       #5**2
print(power(b = 3 , a = 4.5))   #4.5**3
print(power(3 + 4j))     #(3+4j)**2
print(power(True))   #1
#def   power(b = 2 , a):    #Error because  parameter without a default follows parameter with a default
 	 #pass
'''
OUTPUT:
64
25
91.125
(-7+24j)
1
'''





#17 Find outputs  (Home  work)
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
print(add(10 , 20 , 30 , 40))
print(add(50 , 60 , 70))
print(add(80 , 90))
print(add(100))
print(add())

'''
4-argument  function
100
4-argument  function
184
4-argument  function
177
4-argument  function
109
4-argument  function
10
'''





#18 Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)
#disp(40 , 50 , 60 , 70)  #Error because disp() takes from 2 to 3 positional arguments but 4 were given
disp(80 , 90)
'''
OUTPUT:
3-argument  function  :   10 20 30
3-argument  function  :   80 90 25
'''





#19 Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))    #70  
print(add())                   #30
print(add(a = 50))             #70 
print(add(b = 60 , a = 70))    #130
#print(add(80 , 90))           #Error because  add() takes 0 positional arguments but 2 were given  
'''
OUTPUT:
70
30
70
130
'''





#20 Find  outputs(Home  work)
#def   add(a = 10 , b , c):    #error because parameter without a default follows parameter with a default
        #pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) #120
print(add(b = 60 , c = 70))          #140
print(add(c = 80 , b = 90 , a = 100)) #270
#print(add(c = 25 , a = 43)) #error  because add() missing 1 required keyword-only argument: 'b'
#print(add(1 , 2 , 3)) #Error because  add() takes 0 positional arguments but 3 were given
#def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):   #Error because parameter without a default follows parameter with a default
		#pass
'''
OUTPUT:
120
140
270
'''





#21 Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 .__defaults__) #([],)
'''
OUTPUT:
([],)
'''





#22 Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__) #_defaults_  :    ([],)
f1(3)                                      #list : [3]
print('_defaults_  :  ' , f1.__defaults__) #_defaults_  :   ([3],)
f1(4 , [1 , 2 , 3])                        #list : [1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__) #_defaults_  :   ([3],)
f1(9)                                      #list : [3,9]
print('_defaults_  :  ' , f1.__defaults__) #_defaults_  :   ([3,9],)
f1(40 , [10 , 20 , 30])                    #list : [10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__) #_defaults_  :   ([3,9],)
f1(5)                                      #list : [3,9,5]
print('_defaults_  :  ' , f1.__defaults__) #_defaults_  :   ([3,9,5],)
f1([6 , 7 , 8])                            #List :   [3, 9, 5, [6, 7, 8]]
print('_defaults_  :  ' , f1.__defaults__) #_defaults_  :   ([3, 9, 5, [6, 7, 8]],)
'''
OUTPUT:
_defaults_  :   ([],)
List :   [3]
_defaults_  :   ([3],)
List :   [1, 2, 3, 4]
_defaults_  :   ([3],)
List :   [3, 9]
_defaults_  :   ([3, 9],)
List :   [10, 20, 30, 40]
_defaults_  :   ([3, 9],)
List :   [3, 9, 5]
_defaults_  :   ([3, 9, 5],)
List :   [3, 9, 5, [6, 7, 8]]
_defaults_  :   ([3, 9, 5, [6, 7, 8]],)
'''





#23 Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)  #_defaults_  :   ([].)
f1(3)                                       #[3]
print('_defaults_  :  ' , f1.__defaults__)  #_defaults_  :   ([],)
f1(4 , [1 , 2 , 3])                         #[1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__)  #_defaults_  :   ([],)
f1(4)                                       #[4]
print('_defaults_  :  ' , f1.__defaults__)  #_defaults_  :   ([],)
f1(40 , [10 , 20 , 30])                     #[10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__)  #_defaults_  :   ([],)
f1(5)                                       #[5]
print('_defaults_  :  ' , f1.__defaults__)  #_defaults_  :   ([],)
f1([6 , 7 , 8])                             #[[6,7,8]]
print('_defaults_  :  ' , f1.__defaults__)  #_defaults_  :   ([],)
'''
OUTPUT:
_defaults_  :   ([],)
[3]
_defaults_  :   ([],)
[1, 2, 3, 4]
_defaults_  :   ([],)
[4]
_defaults_  :   ([],)
[10, 20, 30, 40]
_defaults_  :   ([],)
[5]
_defaults_  :   ([],)
[[6, 7, 8]]
_defaults_  :   ([],)
'''





#24 Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__)  #_defaults_  :   ([],)
print(f1(3))                                #[0,1,4]
print('_defaults  :  ' , f1.__defaults__)   #_defaults_  :   ([0,1,4],)
print(f1(4 , [10 , 20 , 15 , 18]))          #[10,20,15,18,0,1,4,9]
print('_defaults  :  ' , f1.__defaults__)   #_defaults_  :   ([0,1,4],)
print(f1(5))                                #[0,1,4,0,1,4,9,16]
print('_defaults  :  ' , f1.__defaults__)   #_defaults_  :   ([0,1,4,0,1,4,9,16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))  #[100,200,300,0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__)   #_defaults_  :   ([0,1,4,0,1,4,9,16],)
print(f1(6))                                #[0,1,4,9,16,25,0,1,4,9,16,25]
print('_defaults  :  ' , f1.__defaults__)   #_defaults_  :   ([0,1,4,9,16,25,0,1,4,9,16,25],)

'''
OUTPUT:
_defaults  :   ([],)
[0, 1, 4]
_defaults  :   ([0, 1, 4],)
[10, 20, 15, 18, 0, 1, 4, 9]
_defaults  :   ([0, 1, 4],)
[0, 1, 4, 0, 1, 4, 9, 16]
_defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
[100, 200, 300, 0, 1, 4, 9, 16, 25]
_defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
[0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
_defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)
'''





#25 Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3)) #[0,1,4]
print(f1(4 , [10 , 20 , 15 , 18])) #[10,20,15,18,0,1,4,9]
print(f1(5))                       #[0,1,4,9,16]
print(f1(a = [100 , 200 , 300],   x = 6 )) #[100,200,300,0,1,4,9,16,25]
print(f1(6))                              #[0,1,4,9,16,25]
'''
OUTPUT:
[0, 1, 4]
[10, 20, 15, 18, 0, 1, 4, 9]
[0, 1, 4, 9, 16]
[100, 200, 300, 0, 1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25]
'''





#26 Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 .__defaults__) #Default Values  :   ('Hyd',[])
f1()                                           # a : HydSec <nextline>  b : [1,2,3]
print('Default Values  :  ' , f1 .__defaults__) #Default Values  :   ('Hyd',[1,2,3])
f1()                                            # a : HydSec  <nextline> b :[1,2,3,1,2,3] 
print('Default Values  :  ' , f1 .__defaults__) #Default Values  :   (('Hyd',[1,2,3,1,2,3])
f1()                                            # a: HydSec  <nextline>  b : [1,2,3,1,2,3,1,2,3]
'''
OUTPUT:
Default Values  :   ('Hyd', [])
a :   HydSec
b :   [1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]


