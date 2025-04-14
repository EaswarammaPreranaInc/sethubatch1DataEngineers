


def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) #a:10 b:20
f1(b = 30 , a = 40) #a:40 b:30
#f1(50 , 60)
#f1(70 , b = 80)
#f1(a = 15 , 25)

def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # a:10 b:20 c:30
f1(a = 40 , b = 50 , c = 60) # a:40 b:50 c:60
f1(c = 100 , b = 90 , a = 80) # a:80 b:90 c:100
#f1(70 , 80 , c = 90)
#f1(70 , 80 , 90)
#f1(c = 15 , b = 25 , 35)

def   f1(a  , b , *): #error
        pass'''

'''def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) #a:10 b:20
#f1(a = 30 ,  b = 40)
#f1(50 , b = 60)
#f1(a = 70 , 80)


def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) #a:10 b:20 c:30
f1(40 , 50 , c = 60) #a:40 b:50 c:60
#f1(a = 70 , b = 80 , c = 90)
#f1(a = 100 , b = 110 , 120)
#f1(a = 130 , 140 , c = 150)
#f1(160 , b = 170 , 180)
#f1(190 , b = 200 , c = 210)


def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) #a:10 b:20 c:30 d:40 e:50 f:60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)
#f1(1 , 2 , 3 , 4 , 5 , f = 6)
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) #a:10 b:20 c:30 d:40 e:50 f:60


#def  f1(/ , a , b ,  c):
        #pass
#def   f2(a , b , c , *):
        #pass

def  f4(* , a , b , c , /): #error
	        pass #error

def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)#10
f1(z = 10)
#f1(y = 20)
#f1(x = 30)


#def   f1(a = 10 ,  b ,  c = 20 ,  d):
	#pass
def   f2(b , d , a = 10 , c = 20):
	pass

def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)
f1()
f1(a = 30)

''' output:
20
10
30'''

def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) #330
print(add(100 , 200 , 300)) #620
print(add(100 , 200 , 300 , 400)) #1000
print(add(b = 100 , a = 200)) #330
print(add(100 , 200 , d = 300)) #610
print(add(d = 100 , a = 200 , b = 300)) #610
#print(add(c = 100 , d = 200 , 300 , 400))
#print(add(100 , 200 , c = 300 , x = 400))
#print(add())


def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))
print(f1())
print(f2(20))
#print(f2())

''' output:
10
25
20'''

def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)
disp('$')
disp()
disp(n = 5)
disp(5)
disp(n = 7 , ch = '%')
disp(7 , '@')
disp(7 , n = 6)
#disp(ch = '!' ,  5)

''' output:
------
$$$$
****
*****
20
%%%%%%%
@@@@@@@
42'''

def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5))#91.125
print(power(3 + 4j))#(-7+24j)
print(power(True))#1
#def   power(b = 2 , a):
 	# pass


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

'''output:
4-argument  function
100
4-argument  function
184
4-argument  function
177
4-argument  function
109
4-argument  function
10'''


def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)
#disp(40 , 50 , 60 , 70)
disp(80 , 90)

'''output:
3-argument  function  :   10 20 30
3-argument  function  :   80 90 25'''



def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))#70
print(add())#30
print(add(a = 50))#70
print(add(b = 60 , a = 70))#130
#print(add(80 , 90))


#def   add(a = 10 , b , c):
      #  pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))  #120
print(add(b = 60 , c = 70))   #140
print(add(c = 80 , b = 90 , a = 100)) #270
#print(add(c = 25 , a = 43))
#print(add(1 , 2 , 3))
#def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		#pass



def   f1(a = []):
        pass
#print(f1 . defaults)




def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
#print('defaults  :  ' , f1.defaults)
f1(3)
#print('defaults  :  ' , f1.defaults)
f1(4 , [1 , 2 , 3])
#print('defaults  :  ' , f1.defaults)
f1(9)
#print('defaults  :  ' , f1.defaults)
f1(40 , [10 , 20 , 30])
#print('defaults  :  ' , f1.defaults)
f1(5)
#print('defaults  :  ' , f1.defaults)
f1([6 , 7 , 8])
#print('defaults  :  ' , f1.defaults)

''' List :   [3]
List :   [1, 2, 3, 4]
List :   [3, 9]
List :   [10, 20, 30, 40]
List :   [3, 9, 5]
List :   [3, 9, 5, [6, 7, 8]]'''



def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
#print('defaults  :  ' , f1.defaults)
f1(3)
#print('defaults  :  ' , f1.defaults)
f1(4 , [1 , 2 , 3])
#print('defaults  :  ' , f1.defaults)
f1(4)
#print('defaults  :  ' , f1.defaults)
f1(40 , [10 , 20 , 30])
#print('defaults  :  ' , f1.defaults)
f1(5)
#print('defaults  :  ' , f1.defaults)
f1([6 , 7 , 8])
#print('defaults  :  ' , f1.defaults)

'''[3]
[1, 2, 3, 4]
[4]
[10, 20, 30, 40]
[5]
[[6, 7, 8]]'''




def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
#print('defaults  :  ' , f1._defaults)
print(f1(3))
#print('defaults  :  ' , f1._defaults)
print(f1(4 , [10 , 20 , 15 , 18]))
#print('defaults  :  ' , f1._defaults)
print(f1(5))
#print('defaults  :  ' , f1._defaults)
print(f1(a = [100 , 200 , 300],   x = 6 ))
#print('defaults  :  ' , f1._defaults)
print(f1(6))
#print('defaults  :  ' , f1._defaults)

'''[0, 1, 4]
[10, 20, 15, 18, 0, 1, 4, 9]
[0, 1, 4, 0, 1, 4, 9, 16]
[100, 200, 300, 0, 1, 4, 9, 16, 25]
[0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]'''





def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))
print(f1(4 , [10 , 20 , 15 , 18]))
print(f1(5))
print(f1(a = [100 , 200 , 300],   x = 6 ))
print(f1(6))

'''[0, 1, 4]
[10, 20, 15, 18, 0, 1, 4, 9]
[0, 1, 4, 9, 16]
[100, 200, 300, 0, 1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25]'''




def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
#print('Default Values  :  ' , f1 . defaults)
f1()
#print('Default Values  :  ' , f1 . defaults)
f1()
#print('Default Values  :  ' , f1 . defaults)
f1()

'''a :   HydSec
b :   [1, 2, 3]
a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]'''
