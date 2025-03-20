'''Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing


def prime(n):
    s=0
    for i in range(2, n+1):
        c=0
        for j in range(1, i+1):
            if i % j == 0:
                c += 1
        if c == 2:
            print(i)
            s=s+1
    print(f'number of prime numbers : {s}')
n = int(input("Enter a number: "))
prime(n)'''

'''
# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)  # a : 10	b : 20
f1(b = 30 , a = 40)   # a : 40	b : 30
f1(50 , 60)  # error after * only keyword argm
f1(70 , b = 80) # error only pass keyword argm due to star
f1(a = 15 , 25) # error  positional argument follows keyword argument
'''

'''#Find  outputs 
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)  # a : 10	 b : 20		c : 30
f1(a = 40 , b = 50 , c = 60)  # a : 40	 b : 50		c : 60
f1(c = 100 , b = 90 , a = 80) # a : 80	 b : 90		c : 100
#f1(70 , 80 , c = 90) # error due take only one positional argm not two
#f1(70 , 80 , 90)  # error take one positional argm
#f1(c = 15 , b = 25 , 35) # error  positional argument follows keyword argument
'''

'''# Identify error 
def   f1(a  , b , *): # error due to *, atleast one argm is required after *
        pass
'''

'''#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)  #  a : 10	 b : 20
f1(a = 30 ,  b = 40)  # error due to / at end i.e before the / all are positional argm only
f1(50 , b = 60) # error here no keyword argm is required
f1(a = 70 , 80) # error  positional argument follows keyword argument
'''

'''# Find  outputs 
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)  #  a : 10		 b : 20		 c : 30
f1(40 , 50 , c = 60)  #  a : 40		 b : 50		 c : 90
f1(a = 70 , b = 80 , c = 90) # error two positional arguments are required but all are keyword arguments
f1(a = 100 , b = 110 , 120)  # error  positional argument follows keyword argument
f1(a = 130 , 140 , c = 150)  #error due to two positional arguments are required
f1(160 , b = 170 , 180)  #   error  positional argument follows keyword argument
f1(190 , b = 200 , c = 210) # error due to two positional arguments are required
'''

'''# Find outputs
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)  #  a  :  10  \t  b  :  20  \t  c  :  30  \t  d  :  40  \t  e  :  50  \t  f  :  60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) #  error
f1(1 , 2 , 3 , 4 , 5 , f = 6)   # error
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)  #  a  :  10  \t  b  :  20  \t  c  :  30  \t  d  :  40  \t  e  :  50  \t  f  :  60
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)  #  a  :  10  \t  b  :  20  \t  c  :  30  \t  d  :  40  \t  e  :  50  \t  f  :  60
'''

'''# Identify error 
def  f1(/ , a , b ,  c): # error due begining /, atleast one argm before /
        pass
def   f2(a , b , c , *): # error due to * at end
        pass
'''

'''Identify  error  
def  f4(* , a , b , c , /):  # error 
	pass    
'''

'''# Find  outputs  
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) # 3rd  function : 10
f1(y = 20) # error keyword argm not match 
f1(x = 30) # error keyword argm not match
'''

'''# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d): # error without default argm follows default argm
	pass
def   f2(b , d , a = 10 , c = 20):
	pass
'''

'''#  Find  outputs 
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)  # 20
f1()   # 10
f1(a = 30)  # 30
'''

'''# Find  outputs 
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))  # 330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400)) # 1000
print(add(b = 100 , a = 200)) #  330
print(add(100 , 200 , d = 300)) # 610
print(add(d = 100 , a = 200 , b = 300)) #610
print(add(c = 100 , d = 200 , 300 , 400)) # error
print(add(100 , 200 , c = 300 , x = 400)) # error x is not a formal argm
print(add()) # error some argm are missing
'''

'''#  Find  outputs 
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) # 10
print(f1())  # 25
print(f2(20)) # 20
print(f2()) # error
'''

'''# Find  outputs 
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # ______
disp('$') # $$$$
disp() # ****
disp(n = 5) # *****
disp(5)  # 20
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # @@@@@@@
disp(7 , n = 6) # 42
disp(ch = '!' ,  5) # error
'''

'''# Find  outputs 
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))  # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5)) # 91.125
print(power(3 + 4j)) # (-7+24j)
print(power(True)) # 1
def   power(b = 2 , a): # error non default argm follows default argm
 	 pass
'''

'''# Find outputs  
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
print(add(10 , 20 , 30 , 40)) # 4-argument  function <nextline> 100 
print(add(50 , 60 , 70))  #  4-argument  function <nextline> 184
print(add(80 , 90))  #  4-argument  function <nextline> 177 
print(add(100))  #  4-argument  function <nextline> 109
print(add())  #  4-argument  function <nextline> 10
'''

'''# Find outputs  
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :   10 20 30
disp(40 , 50 , 60 , 70) #  error
disp(80 , 90) #  # 3-argument  function  :   80 90 25
'''

'''# Find outputs
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))  # 70
print(add())   #  30
print(add(a = 50)) #  70
print(add(b = 60 , a = 70)) # 130
print(add(80 , 90)) # error only pass keyword argm
'''

'''# Find  outputs
def   add(a = 10 , b , c): # error
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) # 120
print(add(b = 60 , c = 70))  # 140
print(add(c = 80 , b = 90 , a = 100)) # 270
print(add(c = 25 , a = 43)) # error
print(add(1 , 2 , 3)) # error 
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f): # error 
		pass
'''

'''# Find  output 
def   f1(a = []):
        pass
print(f1 . __defaults__) # ([],)
'''

'''# Find  outputs 
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_ : ([],)
f1(3)    # List : [3]
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_ : ([3],)
f1(4 , [1 , 2 , 3])  # List : [1 , 2, 3, 4]
print('_defaults_  :  ' , f1.__defaults__)   # _defaults_ : ([3],)
f1(9)  # List : [3 ,9]
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_ : ([3 , 9],)
f1(40 , [10 , 20 , 30]) # [40 , [10 , 20 ,30]
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_ : ([3 , 9],)
f1(5) # List : [3, 9, 5]
print('_defaults_  :  ' , f1.__defaults__)  #  _defaults_ : ([3 , 9 , 5],)
f1([6 , 7 , 8]) # List : [3, 9, 5, [6 , 7 , 8]]
print('_defaults_  :  ' , f1.__defaults__) # _defaults_ : ([3 , 9 , 5 ,[6 , 7 , 8],)
'''

'''
#  Find  outputs 
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_  : ([],)
f1(3)   #  [3]
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_  : ([],)
f1(4 , [1 , 2 , 3]) # [1, 2, 3, 4]
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_  : ([],)
f1(4) # [4]
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_  : ([],)
f1(40 , [10 , 20 , 30]) #[10, 20, 30, 40]
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_  : ([],)
f1(5) #[15]
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_  : ([],)
f1([6 , 7 , 8])  # [[6 , 7 , 8]
print('_defaults_  :  ' , f1.__defaults__)  # _defaults_  : ([],)
'''
 

''' # Find  outputs
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__)  #  _defaults  :   ([],)
print(f1(3))    #  [0, 1, 4]
print('_defaults  :  ' , f1.__defaults__)   #  _defaults  :   ([0, 1, 4],)
print(f1(4 , [10 , 20 , 15 , 18]))      #  [10, 20, 15, 18, 0, 1, 4, 9]
print('_defaults  :  ' , f1.__defaults__) #   _defaults  :   ([0, 1, 4],)
print(f1(5))     #  [0, 1, 4, 0, 1, 4, 9, 16]
print('_defaults  :  ' , f1.__defaults__)  #  _defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))  #  [100, 200, 300, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1.__defaults__)  #  _defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(6))    #  [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1.__defaults__)  # _defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)
'''



'''# Find  output 
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))  # [0 , 1 , 4]
print(f1(4 , [10 , 20 , 15 , 18]))  # [10 ,  20 , 15 , 18 , 0 , 1 , 4 , 9]
print(f1(5)) # [0 , 1 , 4 , 9 , 16]
print(f1(a = [100 , 200 , 300],   x = 6 ))  # [100 , 200 , 300 , 0 , 1 , 4 , 9 , 16 , 25]
print(f1(6)) # [0 , 1 , 4 , 9 , 16 , 25]
'''


'''# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)  # Default Values : ('Hyd' , [])
f1() # a : HydSec <nextline> b :  [1 , 2 , 3] 
print('Default Values  :  ' , f1 . __defaults__)  # Default Values : ('Hyd' , [1 , 2 ,3])
f1() # a : HydSec <nextline> b : [1 , 2 , 3 , 1 , 2 , 3] 
print('Default Values  :  ' , f1 . __defaults__)  # Default Values : ('Hyd' , [1 , 2 ,3 , 1 , 2 , 3])
f1() # a : HydSec <nextline> b : [1 , 2 , 3 , 1 , 2 , 3 , 1 , 2 , 3] 
'''
