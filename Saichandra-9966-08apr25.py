MODULE-4:OBJECT ORIENTED PROGRAMMING.
Python-1: CLASSES AND OBJECTS.

# 1. Identify Error
class c1:
    def m1(self):   #  # Empty method
        pass    
class c2:    # Empty class
    pass
#class c3:   # Error : due to no method nor pass



# 2. Find Outputs
class c1:    # Empty class
    pass 
# End of the class 
a = c1()   # Creates empty c1 class object
print(id(a))   # Address of object 'a'
print(type(a))   # <class '__main__.c1'>
print(a.__dict__)   # Converts empty object to {}
print(a)   # __str__ method of object class returns type and address of object 'a'
del a   # Deletes object 'a'
#print(a)   # Error : object 'a' does not exist



# 3. 
def m1():
    print('Function')
class c1:
    def m1(self):   # Discarded becz another method is defined with same name  
        print('1st method')
    def m1(self):   # Discarded becz another method is defined with same name
        print('2nd method')
    def m1(self):   # Recognized becoz it is the last method 
        print('3rd method')
# End of the class c1
a = c1()
a. m1()   # 3rd method 
m1()   # Function



# 4.
class c1():
    def m1(self):   # Discarded becoz another method is defined withsame name
        print('No argument method')
    def m1(self, x):   # Discarded becoz another method is defined withsame name
        print('Single argument method:', x)
    def m1(self, x, y):   # Recognized
        print('Two argument method:', x, y)
# End of the class c1
a = c1()
a . m1(10,20)   # Two argument method: <space> 10 <space> 20
#a . m1(30)   # Error becoz arg is not passed for 'y'
#a . m1()   # Error becoz args are not passed for 'x' and 'y'



# 5.
class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method:', x)
    def m1(self, x = 1, y = 2):
        print('Two argument method:', x , y)
# End of the class c1
a = c1()
a . m1(10, 20)    # Two argument method : <space> 10 <space> 20 
a . m1(30)   # Two argument method : <space> 30 <space> 2 
a . m1()   # Two argument method : <space> 1 <space> 2



# 6.
class c1:
    def m1(self):
        print('Method of first c1 class')
class c1:
    def m1(self):
        print('Method of Second c1 class')
class c1:
    pass
a = c1()   # 3rd c1 class object
#a . m1()   # Error : No m1() method in 3rd c1 class



# 7.
class c1:   # Discorded becoz another class is defined with same name
    def m1(self):
        print('Method of first c1 class')
class c1:   # Discorded becoz another class is defined with same name
    def m1(self):
        print('Method of Second c1 class')
class c1:   # Recognized becoz it is the last class
    def m1(self):
        print('Method of third c1 class')
a = c1()   # 3rd c1 class object
a . m1()   # Method of 3rd c1 class



# 8.
class c1:
    pass
# End of the class
a = c1()
print(a.__dict__)   # {} : empty dict
a . x = 10
print(a.__dict__)   # {'x' : 10}
a . y = 20
print(a.__dict__)   # {'x' : 10, 'y' : 20}
a . x = 30
print(a.__dict__)   # {'x' : 30, 'y' : 20}
a . y = 40
print(a.__dict__)   # {'x' : 30, 'y' : 40}
del a . x
print(a.__dict__)   # {'y' : 40}
del a . y
print(a.__dict__)   # {} : Empty dict
del a
#print(a.__dict__)   # Error becoz 'a' does not exist







