#Repeat   prog7b  such  that
#1) If  input  is   number ,   number  class  objects  should  be  added
#2) If  input  is  string  ,  string  class  objects  should  be  joined
#Note:  Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite
#Hint:   Refer  to  prog8
from prog7a import number,string
import math
ch=eval(input("Enter the number/string/exit: "))

if ch==number:
	obj1=number()
	obj2=number()
	result=number()
	a=eval(input("enter the input: "))
	b=eval(input("enter the input: "))
	obj1.x=a
	obj2.x=b
	result.add(obj1,obj2)
	result.display()
elif ch==string:
	obj1=string()
	obj2=string()
	result=string()
	a=str(input("enter the input: "))
	b=str(input("enter the input: "))
	obj1.x=a
	obj2.x=b
	result.add(obj1,obj2)
	result.display()
elif ch==exit:
	print("Good Bye")
else:
	print("Invalid Input")
"""
Output:
Enter  number / string / exit) : number
Enter  any  number  :  10
Enter  any  number  :  20
Sum :   30
Enter  number / string / exit) : string
Enter  any  string :  Hyder
Enter  any  string :  abad
Join :   Hyderabad
Enter  number / string / exit) : exit
"""

#  Which  of  the  following  statements  throw  ZeroDivisionError ?  (Home  work)
print(7 / 0)     #zero division Error
print(7 / 0.0)   #zero division Error
print(0 / 0)     #zero division Error
print(0.0 / 0.0) #zero division Error
print(7 // 0)    #zero division Error
print(7 % 0)     #zero division Error

#  Which  of  the  following  statements  throw  ValueError ?  (Home  work)
import  math
print(int('10.8'))   #ValueError
print(float('Ten'))  #ValueError
print(complex('Ten'))#ValueError
print(bool('Ten'))   #True
print(bool(''))      #False
print(float('10.8')) #10.8
print(float('25'))   #25.0
print(int(10.8))     #10
print(math . sqrt(-25)) #Value Error

# Which  of  the  following  statements  throw  NameError ?  (Home  work)
a = 25
print(a)  #25
del  a   
#print(a)  #NameError
print(eval("   'Ten'   ")) #Ten
print(eval('Ten'))      #NameError

# Which  of  the  following  statements  throw  IndexError ?  (Home  work)
print('Hyd'[0]) #H
print('Hyd'[1]) #y
print('Hyd'[2]) #d
#print('Hyd'[3]) #IndexError
list = [10 , 20 , 15 , 18]
print(list[0])  #10
print(list[3])  #18
#print(list[4])  #IndexError
print(list[-1]) #18
print(list[-4]) #10
#print(list[-5]) #IndexError
tpl = (10 , 20 , 30)
#print(tpl[3])   #IndexError
r = range(10)  
#print(r[10])    #IndexError
s = {10 , 20 , 15 , 18}
#print(s[4])     #IndexError
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])     #KeyError 

#  Which  of  the  following  statements  throw  TypeError ?  (Home  work)
print(10 + 20)     #30
print('10' + '20') #1020
print(10 + '20')   #TypeError
print(len('25'))   #2
print(len(25))     #TypeError
s = {10 , 20 , 15 , 18}
print(s[0])        #TypeError
b = { [10 , 20] : [30 , 40] }
print(int(3+4j))   #TypeError
print(int([10,20,30])) #TypeError
print(float(None))     #TypeError

# Which  of  the  following  statements  throw  KeyError ?  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])  #Green
print(a['Y'])  #keyError

# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')
"""
Output:
ZDE  1
Bye
"""

# Find  outputs
try:
	print(7 / 0)
	print('Hello')
except  ZeroDivisionError:
	print('ZDE  1')
	try:
		print(8 / 0)
	except  ZeroDivisionError:
		print('ZDE   2')
	print('Bye')
except  ZeroDivisionError:
	print('ZDE  3')
print('End')
"""
Output:
ZDE1
ZDE2
Bye
End
"""


#Find  outputs  (Home  work)
#Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError

try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')
"""
Output:
ArithmeticError
End
"""


# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		print(7 / 0)
	except  ValueError:
		print('Hello')
	try:
		print(int('Ten'))
	except ZeroDivisionError:
		print('Bye')
	print('End  of  f1  function')
# End of f1  function
try:
	print('Begin')
	f1()
	print('Hi')
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')
except:
	print('Bye')
print('End')
"""
Output:
Begin
f1  function
ZDE  is  caught  outside
End
"""

# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		print(7 / 0)
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')
	print('End  of  f1  function')
#end of the  function
try:
	print('Begin')
	f1()
	print('Hello')
except  ZeroDivisionError:
 	print("Hi")
except  ValueError:
	print("Bye")
print('End')
"""
Output:
Begin
f1  function
ZDE  is  caught  by  f1  function
End  of  f1  function
Hello
End
"""

#Find Outputs
ch = eval(input('Enter  choice (9-exit) : '))
while  ch  <  9:
	try:
		match  ch:
			case  1:
				list = [10 , 20 , 15 , 12 , 18]
				print(list[5])
			case  2:
				s = 'Hyd'
				print(s[3])
			case  3:
				print(int('Two'))
			case  4:
				a = 25
				print(len(a))
			case  5:
				print(eval('Hyd'))
			case  6:
				print(7 / 0)
			case  7:
				print(10 + '20')
			case   _:
				d = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb'}
				print(d[18])
	except   ZeroDivisionError:
		print('Div by 0 is not allowed')
	except  ValueError:
		print('No  result')
	except  IndexError:
		print('Invalid  index')
	except  TypeError:
		print('Invalid   argument (or)  operand')
	except  KeyError:
		print('Invalid dict key')
	except  NameError:
		print('Object  does  not  exist')
	except:
		print('A new error')
	ch = eval(input('Enter  choice(9 - Exit) : '))
# End of while loop
print('Bye')
"""
Output:
What  are   the  outputs  if  input  is  1 ?  --->Invalid index

What  are   the  outputs  if  input  is  2 ?  --->Invalid index

What  are   the  outputs  if  input  is  3 ?  --->No result

What  are   the  outputs  if  input  is  4 ?  --->Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  5 ?  --->Object  does  not  exist

What  are   the  outputs  if  input  is  6 ?  --->Div by 0 is not allowed

What  are   the  outputs  if  input  is  7 ?  --->Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  8 ?  --->Invalid dict key
"""

#Find  outputs  (Home  work)
def  f1(a):
	print('f1  function')
	if   a == 20:
		raise  ArithmeticError()
	elif   a == 0:
		raise  IndexError()
	elif  a == 10:
		raise  TypeError(25)
	raise ValueError()
# end of  the function
try:
	print('Begin')
	f1(10)
	f1(20)
	f1(30)
	f1(0)
except  ArithmeticError:
	print('Hyd');
except  IndexError:
	print('Sec')
except  TypeError  as   msg:
	print('Caught  TypeError  outside  the  function :  '  , msg)
except  ValueError:
	print('Hello')
except:
	print('some error')
print('End')
"""
Output:
Begin
f1  function
Caught  TypeError  outside  the  function :   25
End
"""

# Find  outputs  (Home  work)
def  f1(a):
	try:
		if   a == 10:
			raise  ValueError(25)
		elif   a == 20:
			raise  NameError(10.8)
		elif   a == 30:
			raise  IndexError('Hyd')
		raise  EOFError(True)
	except  IndexError  as  msg:
		print('Caught  IndexError  :  ' , msg)
	except ValueError  as  msg:
		print('Caught  ValueError  :  ' , msg)
	except  NameError  as  msg:
		print('Caught   NameError  :  ' , msg)
	except  EOFError  as  msg:
		print('Caught   EOFError  :  '  , msg)
	print('End  of  f1  function')
#outside the function
f1(10)
f1(20)
f1(30)
f1(0)
print('End of the program')
"""
Output:
Caught  ValueError  :   25
End  of  f1  function
Caught   NameError  :   10.8
End  of  f1  function
Caught  IndexError  :   Hyd
End  of  f1  function
Caught   EOFError  :   True
End  of  f1  function
End of the program
"""

#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  : ' , msg)
		raise   ValueError(msg)
	except:
		print('Hello')
	print('End  of  f1  function')
# End  of  f1()  function
try:
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program')
"""
Output:
Begin
f1 function
caught ValueError:25
Recaught ValueError:25
End of the Program
"""

# Find  outputs  (Home   work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  :  ' , msg)
		raise  NameError(msg)
	except:
		print('Hello')
	print('End of f1 function')
#outside the function
try:
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError : ' , x)
except:
	print('Some other error')
print('End of the program')
"""
Output:
Begin
f1 function
caught by f1 function:25
Some other error
End of the Program
"""
