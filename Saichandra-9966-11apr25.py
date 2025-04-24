# setattr(), getattr() and hasattr() functions demo program
class Emp:
	pass
# End of the class
e = Emp() # Creates empty Emp class object
print(e.__dict__)   # {}
setattr(e, 'empno', 25)   # Adds variable empno to object 'e' with value 25 (same as e.empno = 25)
setattr(e, 'ename', 'Rama Rao')   # Adds variable ename to object 'e' with value 'Rama Rao' (same as e.ename = 'Rama Rao')
setattr(e, 'sal', 10000.0)   # Adds variable sal to object 'e' with value 10000.0 (same as e.sal = 10000.0)
setattr(e, 'sal', 20000.0)   # Modifies e.sal to 20000.0 (same as e.sal = 20000.0)
print(e.__dict__)   # {'empno' : 25, 'ename' : 'Rama Rao', 'sal' : 20000.0}
print('Emp number :', getattr(e, 'empno'))   # Returns value of e.empno (same as print(e.empno))
print('Emp name :', getattr(e,'ename'))   # Returns value of e.ename (same as print(e.ename))
print('Salary :', getattr(e, 'sal'))   # Returns value of e.sal (same as print(e.sal))
#print('Gender :', getattr(e, 'gender'))   # Error : No gender variable in object 'e'
print(hasattr(e, 'empno'))   # True : variable empno exists in object 'e'
print(hasattr(e, 'ename'))   # True : variable ename exists in object 'e'
print(hasattr(e, 'sal'))   # True : variable sal exists in object 'e'
print(hasattr(e, 'gender'))   # False : variable gender does not exist in object 'e'



# hasattr-demo1  (Find outputs)
class rat():
	def m1():
		pass
# End of the class
a = rat()  # Empty object
a.nr = 22  # Adds variable nr to object 'a' with value 22
print(hasattr(a, 'nr'))   # True : variable 'nr' exists in object 'a'
print(hasattr(a, 'dr'))   # False : variable 'dr' does not exist in object 'a'
print(hasattr(a, 'm1'))   # True : method 'm1' exists in class rat
print(hasattr(a, 'm2'))   # False : method 'm2' does not exist in class rat
print(hasattr(rat, 'm1'))   # True : method 'm1' exists in class rat
print(hasattr(rat, 'm2'))   # False : method 'm2' does not exist in class rat
print(hasattr(rat, 'nr'))   # False : methid 'nr' does not exist in class rat 



# hasattr- demo2   ( find outputs)
class Cat:
	def talk(self):
		print('Meow Meow Meow....')
class Dog:
	def bark(self):
		print('Bhow Bhow Bhow....')
class Goat:
	def talk(self):
		print('Mehar Mehar Mehar....')

# End of the class
a = [Cat(), Dog(), Goat()]   # list of 3 objects
for x in a:   # 'x' is each object of list 'a'
	if hasattr(x, 'talk'):
		x.talk()
	else:
		x.bark()



# setattr-getattr-demo
class c1:
	pass
# End of the class
a = c1()
a.x = 10
varname = input('Enter variable name to be added to object:')   # Assume that input is 'y'
value = eval(input('Enter value of the variable:'))   # Assume that input is 20
setattr(a, varname, value)
print(a.__dict__)
print(a.x)   # 10
while True:
	try:
		varname = input('Enter variable name who value is to be retrieved:')   # Assume that input is x in 1st iteration, y in 2nd iteration and z in 3rd iteration
		print(getattr(a, varname))
	except:
	    print(F'Invalid variable name: {varname}')
	    break



# (Dict - to - object)
Write a program to connect a dictionary {'empno' : 25, 'Ename' : 'Rama Rao', 'sal' : 10000.0} to Emp class object i.e. object should contain  empno = 25, ename = 'Rama Rao', sal = 10000.0
Hint: Use setattr() and getattr() functions
'''
class emp:
	pass
# End of the class
dict = {'Empno' : 25, 'Ename' : 'Rama Rao', 'sal' : 10000.0}
e = emp()
for key, value in dict.items():
	setattr(e, key, value)
for key in dict.keys():
	print(key, getattr(e, key), sep = '...')
'''
