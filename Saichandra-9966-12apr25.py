MODULE :4 : OOPS.
Python - 2 : Constructors

# 1 . Constructor demo (find outputs)
class Rat:
    def __init__(self, nr1 = 22, dr1 = 7):
        self.nr = nr1
        self.dr = dr1
    def __str__(self):
        return F'{self.nr}/{self.dr}'
# End of the class
a = Rat()   # object is initialized with nr = 22, dr = 7 by constructor 
b = Rat(9)   #  object is initialized with nr = 9, dr = 7 by constructor
c = Rat(5,8)   # object is initialized with nr = 5, dr = 8 by constructor
d = Rat(dr1 = 9)   # object is initialized with nr = 22, dr = 9 by constructor
e = Rat(dr1 = 3, nr1 = 2)   # Object is initialized with nr = 2, dr = 3 by constructor
x = eval(input('Enter numerator:'))   # Assume that input is 11
y = eval(input('Enter denominator:'))   # assume that input is 15
f = Rat(x, y)   # object is initialized with nr = 11, dr = 15 by constructor
print('a:', a)   # __str__() method returns 22/7 i.e. a : 22/7
print('b:', b)   # __str__() method returns 9/7 i.e. b: 9/7
print('c:', c)   # __str__() method returns 5/8 i.e. c: 5/8
print('d:', d)   # __str__() method returns 22/9 i.e. d : 22/9
print('e:', e)   # __str__() method returns 2/3 i.e. e : 2/3
print('f:', f)   # __str__() method returns 11/15 i.e. f : 11/15
c. __init__()   # object 'c' is modified to nr = 22, dr = 7 by constructor
print('c:', c)  # __str__() method returns 22/7 i.e. c ; 22/7
e. __init__(3.8, 4.6)   # object e is modified to nr = 3.8 , dr = 4.6 i.e. e : 3.8/4.6
print('e:', e)   # __str__() method returns 3.8/4.6 i.e. e: 3.8/4.6
#g = Rat(nr1 = 9, 5)   # Error : PA 5 is not permitted atter KA nr1 = 9
#h = Rat(nr = 9, dr = 5)   # Error : No args nr and dr for constructor



# 2. Date - Constructor (find outputs)
class Date:
    def __init__(self, dd1, mm1, yy1):
        self.dd = dd1
        self.mm = mm1
        self.yy = yy1
        
# End of the class
a = Date(15, 8, 1947)   # object is initialized with dd =15, mm=8, yy=1947 by constructor
b = Date(yy1 = 1950, mm1 = 1, dd1 = 26)   #  object is initialized with dd =26, mm=1, yy=1950 by constructor
c = Date(mm1 = 7, dd1 = 19, yy1 = 1985)   #  object is initialized with dd =19, mm=7, yy=1985 by constructor
print('a:', a.__dict__)   # a: {'dd': 15, 'mm': 8, 'yy': 1947}
print('b:', b.__dict__)   # b: {'dd': 26, 'mm': 1, 'yy': 1950}
print('c:', c.__dict__)    # c: {'dd': 19, 'mm': 7, 'yy': 1985}
#d = Date()   # Error : args are not passed for dd1, mm1, and yy1 of constructor
#e = Date(dd=30, mm=4, yy=2022)   # Error : threre are no args dd, mm, yy for constructor
#f = Date(dd1 =26, mm1 =8, 2023)  # Error : PA 2023 after KA = mm1 =8



# 3. return,py (find outputs)
class c1:
    def __init__(self):
        print('c1 class constructor')
        return 25
class c2:
    def __init__(self):
        print('c2 class constructor')
        return None
class c3:
    def __init__(self):
        print('c3 class constructor')

# End of the class
#a = c1()   # Error due to return 25 in the constructor
b = c2()   # Executes constructor of class c2
print(b)   # Type and address of object 'b'
print(b.__init__())   # Executes constructor of class c2 which returns None
c = c3()   # Executes constructor of class c3
print(c.__init__())   # Executes constructor of class c3 which returns None'



# 4. recursion (find outputs)
class c1:
    def __init__(self):
        print('constructor')
        b = c1()   # Executes same constructor and leads to recursion

# End of the class
a = c1()   # Executes constructor of class c1



# 5. (init - __init__)
# difference between init() and __init__() method
class c1:
    def __init__(self):
        print('constructor')
        self.x = 10
        self.y = 20
class c2:
    def init(self):
        print('Method')
        self.x = 30
        self.y = 40
a = c1()  # object is initialized with x = 10, y = 20 by constructor
print(a. __dict__)  # {'x' : 10, 'y' : 20}
b = c2()   # Empty object
print(b. __dict__)  # {}
b.init()   # object is initialized with x =30 , y = 40 by the method
print(b. __dict__)   # {'x' : 30, 'y' : 40}


