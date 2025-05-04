'''
#1) Find  outputs  (Home  work)
try:
	print('try')
	print(7 / 0)
except:
	print('except')
else:
	print('else') # Else shoot executes onlt when try suite does not executes Error.
finally:
	print('finally')
print('End')

output:-
--------
try
except
finally
End


#2)Find  outputs  (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')

output:-
---------
try
else
finally
End


#3) Identify   error   (Home  work)
try:
	print('try')
#else:
    #print('else') # Error : we should not write else suite without except suite here.
finally:
    print('finally')
print('End')

output:-
---------
try
finally
End


#4) Identify  error   (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else1')
else:
	print('else2') # Error : Else suite must be one.
finally:
	print('finally')
print('end')

output:-
---------
try
else1
else2
finally
end
Press

#5) Identify  error   (Home  work)
try:
	print('try')
#else:
	print('else') #Error : we have to write Except suite than Else suite
except:
	print('except')
finally:
	print('finally')
print('end')

output:
-------
try
else
finally
end

#6) Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except') # skipped due to no error raised by try suites.
if   10 > 20:
	print('if') # condition 'False' so it will not prints.
else:
	print('else')

output:-
----------
try
else


#7) Find  outputs
def   f1():
	try: 
		return  10 # The try block runs and executes return 10.

	except:
		return  20 # Since return 10 succeeds without error, the except block is skipped.
	else:
		return  30 # But importantly, the else block is never executed if a return has already happened in the try block.
print(f1())

output:-
---------
10


#8) Find  outputs
def   f1():
	try:
		return  10 + '20' # This tries to add an integer (10) and a string ('20'), which is not allowed in Python. This raises a TypeError
	except:
		return  20 # immediately jumps to the except block:
	else:
		return  30 # skipped due to  error raised by try suites.
print(f1())

output:-
----------
20

#9)Find  outputs
def   f1():
	try:
		pass # here nothing is there to return the statements
	except:
		return  20 # skipped due to no error in try suit
	else:
		return  30 # 30 Executed
print(f1())

output:-
-----------
30

#10) Find  outputs
def   f1():
	try:
		return  10
	except:
		return   20
	else:
		return  30
	finally:
		return  40 # the finally suite always executes , even if there a return in the try, except , or else. finally overrides any earlier return in the try, except or else
print(f1())

output:-
-----------
40

#11)Homework
1)What  is  the  output  if  input  is  24 ?  --->Hyd
                                                  End
2) What  is  the  output  if  input  is  25 ?  --->Sec
                                                   End
try:
	x = eval(input('Enter  any  number  :  '))
	assert    x >= 25 ,  'Hyd'
	print('Sec')
except  AssertionError  as   msg:
	print(msg)
print('End')

output:-
-------
Enter  any  number  :  24
Hyd
End
Enter  any  number  :  25
Sec
End

The assert statement is used to test if a condition is True (or) not . If condition is True: nothing happens, program continues.
                                                                       If condition is False : it raises Assertion Error(message).

#12)(Home  work)
1) What  is  the  output  when  input  is  24 ?  --->

2) What  is  the  output  when  input  is  25 ?  --->

try:
	x = eval(input('Enter  any  number  :  '))
	assert   x >= 25
	print('Sec')
except  AssertionError   as    msg:
	print(msg)
print('End')

output:-
----------
Enter  any  number  :  24
<space>
End
Enter  any  number  :  25
Sec
End


#13)Find  outputs   (Home  work)
try:
	print('Outer   try')
	try:
		print('Inner    try')
		print(7 / 0)
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except   ZeroDivisionError: # it will search in inner try 
		print('ZDE   of   inner   try')
		int('Ten')
	except  ValueError: # it will search in inner try ,if it not found it will search in outer try.
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally') # executed
	print('End  of  inner  try')
except   ValueError:
	print('ValueError  of  outer  try')
except   IndexError:
	print('IndexError  of  outer  try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally') # Executed
print('End  of  outer  try') # Executed due to sequential Executions.

output:-
-----------
Outer   try
Inner    try
ZDE   of   inner   try
Inner  try  finally
ValueError  of  outer  try
Outer  try  finally
End  of  outer  try


#14) Find outputs   (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		int('Hyd')
		'Hyd'[5]
		eval('Hyd') # Value Error
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ') # Value Error is caught here 
	finally:
		print('Inner  try  finally') # Executes 
	print('End  of  inner  try') # Executes due to sequential executions
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally') # executes
print('End of outer try') # Executes.

output:-
---------------
outer  try
Inner  try
ValueError  of  inner  try
Inner  try  finally
End  of  inner  try
Outer try finally
End of outer try


#15) Find outputs   (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		'Hyd'[3] # IndexError
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally') # skipped
	print('End  of  inner  try') # skipped due to Error is not caught here
except  ValueError:
	print('ValueError  of  outer  try') #skipped
except  IndexError:
	print('IndexError  of  outer  try') # IndexError is caught here.
except:
	print('default except of outer try')  # skipped
finally:
	print('Outer try finally') # Executed
print('End  of  outer  try') # Executed

output:-
-----------
Outer  try
Inner  try
Inner  try  finally
IndexError  of  outer  try
Outer try finally
End  of  outer  try

#16)  Find  outputs (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally') # Executed
	print('End of inner try') # skipped due to Error is not caughts.
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try') # executed
finally:
	print('Outer  try  finally') # executed
print('End  of  outer  try') # executed

output:-
---------
Outer  try
Inner  try
Inner  try  finally
default  except  of  outer  try
Outer  try  finally
End  of  outer  try


#17)Find  outputs (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		#print(10 + '20') unsupported operand type(s) for +: 'int' and 'str': TypeError
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')

output:-
------------
Outer  try
Inner  try
Inner  try  finally
End of inner try
Outer  try  finally
End  of  outer  try


#18) Find  outputs   (Home  work)
class   MyError(BaseException):
	def    __init__(self , y):
		self . a = y
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise   MyError(x)
	print('Hello')
# End of  the function
try:
	compute(10)
	compute(30)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')

output:-
----------
10
Hello
30
Constructor
Caught  MyError  outside  :   30
End


#19) Find  outputs   (Home  work)
class   MyError(NameError):
	def    _init_(self):
		self . a =  25
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise   MyError()
	print('Hello')
#end of  the functrion
try:
	compute(30)
	compute(10)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')

output:-
--------------
30
Caught  MyError  outside  :
End

#20) Find  outputs (Home  work)
try:
	print(1)
	print(2)
	print(3)
except:
	print(4) # not Executed due to try suite does not raises Error.
else:
	print(5)
finally:
	print(6)
print(7)

output:-
----------
1
2
3
5
6
7

#21) Find  outputs   (Home  work)
try:
	print(1)
	print(7 / 0) # raises ZDError
	print(3) # skipped due to Error raised.
except:
	print(4)
else:
	print(5) # not Executed to to try suite raises an Error.
finally:
	print(6)
print(7)

output:-
----------
1
4
6
7


#22) Find  outputs   (Home  work)
try:
	print(1)
	print(7 / 0) # raised ZDError here
	print(3)
#except:
	#int('Two') # Error : Type Error
#else:
       # print(5)
finally:
        print(6)
print(7)

output:-
----------
1
3
6
7


#23)Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')

output:-
-----------
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread


#24) Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')

output:-
-----------
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread


#25)Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread() # Target is not there.
child . start()
for  i   in   range(10):
        print('main  thread')
output:-
----------
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread


#26) from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . run()
for  i  in  range(10):
        print('main  thread')

output:-
----------
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
'''


#27) Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
#child . start() # Error 




