# -- Function to calculate the average of given numbers --  
def avg(*a):  
    return sum(a) / len(a) if a else 0  # Returns 0 if no numbers are passed  

print(avg(10, 20, 15, 18))  # 15.75  
print(avg(25, 10.8, True))  # 12.93 (True is treated as 1)  
print(avg(10.8, 20.6, 15.2, 14.9, 9.8))  # 14.26  
print(avg())  # 0 (no arguments given)  
print(avg(25))  # 25 (only one number, so average is the number itself)  
# print(avg(3 + 4j, 5 + 6j))  # Error: Complex numbers cannot be averaged  
# print(avg((10, 20, 15, 18)))  # Error: Tuple needs to be unpacked like avg(*tpl)  

# -- Function to concatenate strings --  
def concat(*a):  
    return " ".join(map(str, a))  # Converts all inputs to strings before joining  

print(concat('Sankar', 'Dayal', 'Sarma'))  # 'Sankar Dayal Sarma'  
print(concat('Hyd', 'Is', 'Green', 'City'))  # 'Hyd Is Green City'  
print(concat('Python', 'Is', 'A', 'Great', 'Language'))  # 'Python Is A Great Language'  
print(concat())  # '' (empty string)  
print(concat('Python'))  # 'Python'  
print(concat(1, 2, 3))  # '1 2 3' (numbers are converted to strings)  

# -- Function with default and variable arguments --  
def f1(a=25, *b):  
    print(f'a: {a} \tb: {b}')  # Prints a and tuple of remaining arguments  

f1(10, 20, 30, 40)  # a: 10  b: (20, 30, 40)  
f1(50, 60)  # a: 50  b: (60,)  
f1(70)  # a: 70  b: () (no extra arguments)  
f1(a=80)  # a: 80  b: ()  
f1(b=(10, 20, 30), a=40)  # a: 40  b: ((10, 20, 30),) (tuple inside tuple)  
f1()  # a: 25  b: () (default value used)  

# -- Function with required and keyword arguments --  
def f2(*a, b):  
    print(f'a: {a} \tb: {b}')  # b is mandatory  

f2(10, 20, 30, b=40)  # a: (10, 20, 30)  b: 40  
f2(50, b=60)  # a: (50,)  b: 60  
f2(b=70)  # a: ()  b: 70 (no extra args)  
# f2(b=10, a=(20, 30, 40))  # Error: a is positional, cannot be assigned as a keyword  
# f2()  # Error: b is required  

# -- Function with a required argument, variable args, and a keyword argument --  
def f3(a, *b, c):  
    print(f'a: {a}  b: {b}  c: {c}')  

f3(10, 20, 30, 40, c=50)  # a: 10  b: (20, 30, 40)  c: 50  
f3(60, 70, c=80)  # a: 60  b: (70,)  c: 80  
f3(90, c=100)  # a: 90  b: ()  c: 100  
# f3(a=1, 2, c=3)  # Error: 2 is a positional argument after keyword  
# f3(1, 2, 3)  # Error: c is missing  

# -- Function with variable keyword arguments --  
def disp(**a):  
    print('Results:', a)  # Prints dictionary of keyword arguments  

disp(RollNo=10, StudName='Rama Rao')  # {'RollNo': 10, 'StudName': 'Rama Rao'}  
disp(EmpNo=25, EmpName='Sita', Salary=10000.0)  # {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}  
disp(AcNo=30, CustName='Kiran', Balance=20000.0, Gender='m')  
disp()  # Empty dictionary  

# -- Function using both positional and keyword arguments --  
def f4(a, *b, **c):  
    print(a)  
    if b: print(b)  
    if c: print(c)  

f4(25)  # a: 25  
f4('Hyd', 10, 20, 30)  # a: 'Hyd', b: (10, 20, 30)  
f4(10.8, 25, 'Hyd', True, EmpNo=12, EmpName='Rama Rao', Salary=10000.0)  
# a: 10.8, b: (25, 'Hyd', True), c: {'EmpNo': 12, 'EmpName': 'Rama Rao', 'Salary': 10000.0}  

# -- Global variable demo --  
a = 10  
def f5():  
    global a  
    print(a)  # Prints global a (10)  
    a = 20  # Updates global a  

f5()  
print(a)  # a is now 20  

# -- Local vs Global variable demo --  
b = 10  
def f6():  
    b = 20  # Local b, does not affect global b  
    print(b)  # Prints local b (20)  

f6()  
print(b)  # Prints global b (10)  

# -- Using globals() dictionary --  
c = 10  
def f7():  
    global c  
    print(c)  # 10  
    c = 30  # Updates global c  

f7()  
print(c)  # Now 30  

# -- Function modifying global dictionary directly --  
d = 10  
def f8():  
    print(d)  # 10  
    globals()['d'] = 50  # Modifies global d  

f8()  
print(d)  # Now 50  

# -- Error cases --  
# def f9():  
#     global e  
#     print(e)  # Error: e is not defined before using it  

# def f10():  
#     x = x + 5  # Error: x is used before being assigned a value  

# def f11():  
#     global f  
#     f = 10  
#     print(f)  # 10  
#     f = 20  

# f11()  
# print(f)  # 20  

# -- Testing invalid function declarations --  
# def f12(*a, *b):  # Error: Multiple *args not allowed  
#     pass  
# def f13(*a, b):  # Valid: *a collects values, b is required  
#     pass  
# def f14(a, *b):  # Valid: First argument is required, *b is optional  
#     pass  
# def f15(a, b):  # Valid: Two required arguments  
#     pass  
# def f16(a, *b, c):  # Valid: a is required, *b collects values, c is required  
#     pass  
# def f17(*, a, *b, c):  # Error: * and *args cannot be together  
#     pass  
# def f18(a, *b, c, /):  # Valid: Positional-only with *args and required keyword  
#     pass
