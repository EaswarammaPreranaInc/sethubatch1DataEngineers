# program 1
#complex object demo program
a = 3 + 4j#In this line there are 2 elements reference and object.Here Reference a points to obj 3 + 4j
print(a)#prints the value at reference a  which is 3 + 4j here in the form of tuple() , as real and imag are unchanged which inturn obeys tuple's immutable rule.
print(type(a))#here there are two entities in a real and imag.so type is <class 'complex'>
print(id(a))#prints some random value in output console say address at that point of time
print(a.real) #prints the value 3.0 
print(a.imag)#prints the value 4.0
print(type(a.real))#prints <class'float'> by default float(number with decimal)is taken into consideration as output
print(type(a.imag))#prints <class'float'> by default float(number with decimal)is taken into consideration as output

# program 2
#complex object demo program 
a = 6j#In this line there are 2 elements reference and object.Here Reference 'a' points to obj 0 + 6j i.e., 6j
print(type(a)#here there are two entities in a real and imag.so type is <class 'complex'>
print(a.real)#prints the value 0
print(a.imag)#prints the value 6.0
#print(5+j6)#invalid syntax,as complex form is of form a + bj where a and b are real and imag respectively
#print(3+4i)#invalid syntax as i must not be replaced with j
#print(4+j)#invalid syntax due to no number before j
#print(4+1j)#prints the value in tuple
#print(4+0j)#prints the value in tuple

# program 3
#bool object demo program
a = True#reference 'a' points to object True
print(a)#prints value of a i.e., True
print(type(a))#since True is a bool type i.e.,<class'bool'>
print(id(a))#prints the address of a 
b = False#reference 'b' points to object False
print(b)#prints value of b i.e., False
print(type(b))#<class'bool'>
print(True + True)#prints some operations are performed on bool values then True sets to 1 and False sets to 0.here it prints 2
print(True + False)#prints 1
print(False + True)prints 1
print(False + False)#prints 0
print(True + True + True)#prints 3
print(25 + 10.8 + True)#prints 36.8
print(True > False)#prints True as 1>0 is correct.
print(True)#prints 1
print(False)#prints 0
#print(true)#throws errror,as true is not defined in the code,as well as True as some special meaning in Python keywords. 
#print(false)#throws errror,as false is not defined in the code,as well as False as some special meaning in Python keywords
