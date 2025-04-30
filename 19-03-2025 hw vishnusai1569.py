mN"""
# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)#a: 10	b: 20
f1(b = 30 , a = 40)#a: 40	b: 30
#f1(50 , 60)#error
#f1(70 , b = 80)#error
#f1(a = 15 , 25)#error


#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)#a: 10	b: 20	c: 30
f1(a = 40 , b = 50 , c = 60)#a: 40	b: 50	c: 60
f1(c = 100 , b = 90 , a = 80)#a: 80	b: 90	c: 100
#f1(70 , 80 , c = 90)#error
#f1(70 , 80 , 90)#error
#f1(c = 15 , b = 25 , 35)#error


# Identify error (Home  work)
#def   f1(a  , b , *):# * must be before arguments
        #pass



#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)#a: 10	b: 20
#f1(a = 30 ,  b = 40)#error
#f1(50 , b = 60)#error
#f1(a = 70 , 80)#error    



# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)#a: 10	b: 20	c: 30
f1(40 , 50 , c = 60)#a: 40	b: 50	c: 60
f1(a = 70 , b = 80 , c = 90)#error
#f1(a = 100 , b = 110 , 120)#error
#f1(a = 130 , 140 , c = 150)#error
#f1(160 , b = 170 , 180)#error
#f1(190 , b = 200 , c = 210)#error



# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)#a: 10	b: 20	c: 30	d: 40	e: 50	f: 60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)#error
#f1(1 , 2 , 3 , 4 , 5 , f = 6)#error
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)#error
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#a: 10	b: 20	c: 30	d: 40	e: 50	f: 60



# Identify error (Home  work)
#def  f1(/ , a , b ,  c):# / should be after arguments
 #       pass
#def   f2(a , b , c , *):# * should be before arguments
 #       pass



 # Identify  error  (Home  work)
#def  f4(* , a , b , c , /):# / must be ahead of *
#	        pass


 # Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)#1st  function : 30
def  f1(y):
	print('2nd  function : ' , y)#ignored
def  f1(z):
	print('3rd  function : ' , z)#ignored
f1(z = 10)
#f1(y = 20)
#f1(x = 30)


 

 # Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d):#error
#	pass
def   f2(b , d , a = 10 , c = 20):
	pass




#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)#20
f1()#10
f1(a = 30)#30




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
#print(add(100 , 200 , c = 300 , x = 400))error
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
disp('-' , 6)#------
disp('$')#$$$$
disp()#****
disp(n = 5)#*****
disp(5)#20
disp(n = 7 , ch = '%')#%%%%%%%%
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
#def   power(b = 2 , a):#error
 #	 pass



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
print(add(10 , 20 , 30 , 40))#100
print(add(50 , 60 , 70))#184
print(add(80 , 90))#177
print(add(100))#109
print(add())#10



 # Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)#10,20,30
#disp(40 , 50 , 60 , 70)#error
disp(80 , 90)#80,90,25



 # Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))#70
print(add())#30
print(add(a = 50))#70
print(add(b = 60 , a = 70))#130
#print(add(80 , 90))#error


 # Find  outputs(Home  work)
#def   add(a = 10 , b , c):
#        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))#120
print(add(b = 60 , c = 70))#140
print(add(c = 80 , b = 90 , a = 100))#270
#print(add(c = 25 , a = 43))
#print(add(1 , 2 , 3))
#def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
#		pass


 

 # Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . __defaults__)#([],)



# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1(3)#[3]
print('__defaults__  :  ' , f1.__defaults__)#([3],)
f1(4 , [1 , 2 , 3])#[1 , 2 , 3 , 4]
print('__defaults__  :  ' , f1.__defaults__)#([3],)
f1(9)#([3, 9],)
print('__defaults__  :  ' , f1.__defaults__)#([3, 9],)
f1(40 , [10 , 20 , 30])#[10 , 20 , 30, 40]
print('_defaults_  :  ' , f1.__defaults__)#([3, 9],)
f1(5)#([3, 9, 5],)
print('_defaults_  :  ' , f1.__defaults__)#([3, 9, 5],)
f1([6 , 7 , 8])#([3, 9, 5],[6 , 7 , 8])
print('_defaults_  :  ' , f1.__defaults__)#([3, 9, 5],[6 , 7 , 8])



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
f1(4 , [1 , 2 , 3])#[1 , 2 , 3, 4]
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(4)#[4]
print('_defaults_  :  ' , f1.__defaults__)#([],)
f1(40 , [10 , 20 , 30])#[10 , 20 , 30, 40]
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
print(f1(3))#[0, 1, 4]
print('_defaults  :  ' , f1.__defaults__)#([0, 1, 4],)
print(f1(4 , [10 , 20 , 15 , 18]))#[10 , 20 , 15 , 18, 0, 1, 4, 9]
print('_defaults  :  ' , f1.__defaults__)#([0, 1, 4],)
print(f1(5))#([0, 1, 4, 0, 1, 4, 9, 16],)
print('_defaults  :  ' , f1.__defaults__)#([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))#[100 , 200 , 300, 0, 1, 4, 9, 16, 25 ]
print('_defaults  :  ' , f1.__defaults__)#([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(6))#([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)
print('_defaults  :  ' , f1.__defaults__)#([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)



# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))#[0, 1, 4]
print(f1(4 , [10 , 20 , 15 , 18]))#[10 , 20 , 15 , 18, 0, 1, 4, 9]
print(f1(5))#[0, 1, 4, 9, 16]
print(f1(a = [100 , 200 , 300],   x = 6 ))#[100 , 200 , 300, 0, 1, 4, 9, 16, 25]
print(f1(6))#[0, 1, 4, 9, 16, 25]

# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)#HydSec
	print('b :  ' , b)#[1 , 2 , 3]
# End of the function
print('Default Values  :  ' , f1 . __defaults__)#('Hyd', [])
f1()#HydSec, [1 , 2 , 3]
print('Default Values  :  ' , f1 . __defaults__)#('Hyd', [1, 2, 3])
f1()#HydSec, [1, 2, 3, 1, 2, 3]
print('Default Values  :  ' , f1 . __defaults__)#('Hyd', [1, 2, 3, 1, 2, 3])
f1()#HydSec, [1, 2, 3, 1, 2, 3, 1, 2, 3]


Default Values  :   ('Hyd', [])
a :   HydSec
b :   [1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]

"""