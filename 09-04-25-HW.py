#
'''class  Rat:
	def  __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def  __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat() #   Object  is  initialized  with  nr =  22 , dr = 7  by  constructor
b = Rat(9)
c = Rat(5,8)
d = Rat(dr1 = 9)
e = Rat(dr1 = 3 , nr1 = 2)
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)
print('a  :  ' , a)
print('b  :  ' , b)
print('c  :  ' , c)
print('d  :  ' , d)
print('e  :  ' , e)
print('f  :  ' , f)
c . __init__()
print('c  :  ' , c)
a . __init__(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a)
#g = Rat(nr1 = 9 , 5)  # positional argument follows keyword argument
#h = Rat(nr = 9 , dr = 5)  # positional argument follows keyword argument
'''

#
'''class  Date:
        def  __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)  # a  :   {'dd': 15, 'mm': 8, 'yy': 1947}
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)  #  b  :   {'dd': 26, 'mm': 1, 'yy': 1950}
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985) # c  :   {'dd': 19, 'mm': 7, 'yy': 1985}
print('a  :  ' , a .__dict__) # 'Date' object has no attribute '_dict_'. Did you mean: '__dict__'?
print('b  :  ' , b . __dict__)
print('c  :  ' , c . __dict__)
#d = Date()
#e = Date(dd = 30 , mm = 4 , yy = 2022)
#f = Date(dd1 = 26 , mm1 = 8 , 2023)'''


#
'''class  c1:
	def  __init__(self):
		print('c1  class constructor')
		#return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1()
b = c2()
print(b)
print(b . __init__())
c = c3()
print(c . __init__())

#output
c1  class constructor
c2  class  constructor
<__main__.c2 object at 0x000001D11CEF6A50>
c2  class  constructor
None
c3  class  constructor
c3  class  constructor
None'''


#
'''class  c1:
	def  __init__(self):
		print('Constructor')
		#b = c1()
# End  of  class
a = c1()'''


#  Difference  between  init()    and  __init__()   methods
'''class c1:
    def __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1()
print(a . __dict__)
b = c2()
print(b . __dict__)
b . init()
print(b . __dict__)


#output
Constructor
{'x': 10, 'y': 20}
{}
Method
{'x': 30, 'y': 40}
'''


#
'''class   c1:
        def  __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1()
print(x .__dict__) # {'a': 10}
x . m1()
print(x .__dict__)  # {'a': 10, 'b': 20}
f1()
print(x .__dict__)  # {'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x .__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y . m3()
print(x .__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z .__dict__) # {'a': 10}'''


#
'''class   c1:
	def  __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)  # {'x': 10, 'y': 20, 'z': 30}
print(b . __dict__)  # {'x': 10, 'y': 20, 'z': 30}
#del  a . x
#del  b . y
print(a . __dict__)  # {'x': 10, 'y': 20, 'z': 30}
print(b . __dict__)  # {'x': 10, 'y': 20, 'z': 30}
print(a . x)   # 10
print(b . y)   # 20'''



#
'''class   c1:
	def __init__(self):
		print('1st  constructor')
	def __init__(self):
		print('2nd  constructor')
	def __init__(self):
		print('3rd  constructor')  # 3rd  constructor
# End  of  the  class
a = c1()'''


#
'''class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
#a = c1(10 , 20)
#b = c1(30)
c = c1()'''


#  Find  outputs
'''class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
#a = c1(10 , 20)
#b = c1(30)
c = c1()'''


# What  happens  when  function  and  class  have  same  name ?
'''def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
#end of the  class
a = f1()
print(a) # type and address'''


# Find  outputs (Home  work)
'''class    c1:
	def   _init_(self):
		print('Constructor')
def  c1(): #recognised
	print('Function') # Function
#end of the  class
a = c1()
print(a)  # None'''


# Find outputs  (Home  work)
'''class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25)
print(b)

Function :  25
None'''


