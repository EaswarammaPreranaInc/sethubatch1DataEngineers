'''
Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

Note:  Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

Hint:   Refer  to  prog8
'''
# prog8.py
from prog7b import number, string

while True:
    ch = input("Enter number / string / exit : ").strip().lower()

    if ch == "number":
        n1 = number()
        n2 = number()
        res = number()

        print("Enter any number : ", end='')
        n1.get()
        print("Enter any number : ", end='')
        n2.get()

        res.add(n1, n2)
        print("Sum : ", end='')
        res.display()

    elif ch == "string":
        s1 = string()
        s2 = string()
        res = string()

        print("Enter any string : ", end='')
        s1.get()
        print("Enter any string : ", end='')
        s2.get()

        res.add(s1, s2)
        print("Join : ", end='')
        res.display()

    elif ch == "exit":
        break

    else:
        print("Invalid input. Try again.")
'''output:  Enter number / string / exit : number
			Enter any number : 10
			Enter any number : 20
			Sum : 30

			Enter number / string / exit : string
			Enter any string : Hyder
			Enter any string : abad
			Join : Hyderabad

			Enter number / string / exit : exit
'''
#  Which  of  the  following  statements  throw  ZeroDivisionError ?  (Home  work)
print(7 / 0)         # ZeroDivisionError: division by zero
print(7 / 0.0)       # ZeroDivisionError: float division by zero
print(0 / 0)         # ZeroDivisionError: division by zero
print(0.0 / 0.0)     # ZeroDivisionError: float division by zero
print(7 // 0)        # ZeroDivisionError: integer division or modulo by zero
print(7 % 0)         # ZeroDivisionError: integer division or modulo by zero




'''
1) When  is  ZeroDivisionError  raised ?  --->   When  division  by  0  (or)  0.0  is  made

2) Is  ZDE  raised  for  / , //  and  %  when  division  by  zero  is  made ?  --->  Yes
'''
#  Which  of  the  following  statements  throw  ValueError ?  (Home  work)
import math

print(int('10.8'))             # Error → '10.8' is not a valid int literal (has a decimal)
print(float('Ten'))            # Error → 'Ten' is not a valid float literal
print(complex('Ten'))          # Error → 'Ten' is not a valid complex literal
print(bool('Ten'))             # Valid → non-empty string → True
print(bool(''))                # Valid → empty string → False
print(float('10.8'))           # Valid → converts string to float → 10.8
print(float('25'))             # Valid → converts string to float → 25.0
print(int(10.8))               # Valid → converts float to int → 10
print(math.sqrt(-25))          # ValueError → cannot take square root of negative number



'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result  (not  even  None)
'''
# Which  of  the  following  statements  throw  NameError ?  (Home  work)
a = 25                 # Valid → variable `a` is assigned
print(a)               # Valid → prints 25
del a                  # Valid → deletes variable `a`
print(a)               # Error → `a` is deleted and no longer defined
print(eval("   'Ten'   "))  # Valid → evaluates to string 'Ten'
print(eval('Ten'))          # Error → variable `Ten` is not defined


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  accessed
'''
# Which  of  the  following  statements  throw  IndexError ?  (Home  work)
print('Hyd'[0])        # Valid → 'H'
print('Hyd'[1])        # Valid → 'y'
print('Hyd'[2])        # Valid → 'd'
print('Hyd'[3])        # Error → Index out of range (max valid index: 2)

list = [10, 20, 15, 18]
print(list[0])         #  10
print(list[3])         #  18
print(list[4])         # Error → Only 4 elements (valid indices: 0 to 3)
print(list[-1])        # 18 (last element)
print(list[-4])        # 10 (first element)
print(list[-5])        # Error → Out of negative index range

tpl = (10, 20, 30)
print(tpl[3])          # Error → Only 3 elements (indices: 0 to 2)

r = range(10)
print(r[10])           # Error → Valid indices: 0 to 9

s = {10, 20, 15, 18}
print(s[4])            # Error (not IndexError) → Sets are unordered and not subscriptable

d = {10: 'Hyd', 20: 'Sec'}
print(d[0])            # KeyError → Key `0` doesn't exist (also not IndexError)

'''
1) When  is  IndexError  raised  ?  --->  When  non-existing  index  is   used

2) What  is  the  range  of indexes  from  left  to  right ?  --->  0  to  len - 1
     What  is  the  range  of indexes  from  right  to  left ?  --->  -1  to  -len
'''
#  Which  of  the  following  statements  throw  TypeError ?  (Home  work)
print(10 + 20)             # 30
print('10' + '20')         # 1020
print(10 + '20')           # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(len('25'))           # 2
print(len(25))             # TypeError: object of type 'int' has no len()
s = {10 , 20 , 15 , 18}
print(s[0])                # TypeError: 'set' object is not subscriptable
b = { [10 , 20] : [30 , 40] } # TypeError: unhashable type: 'list'
print(int(3+4j))           # TypeError: can't convert complex to int
print(int([10,20,30]))     # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
print(float(None))         # TypeError: float() argument must be a string or a number, not 'NoneType'

'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression
																			            (or)
													  when  an  illegal  argument  is  passed  to  function (or)  method
'''
# Which  of  the  following  statements  throw  KeyError ?  (Home  work)
a = {'R':'Red','G':'Green','B':'Blue'}
print(a['G'])  # Green
print(a['Y'])  # KeyError: 'Y'


'''
When  is  KeyError  raised  ?  --->  When  the  dictionary  key  is  invalid
'''
# Find  outputs  (Home  work)
try:
	print(7 / 0)                     # ZeroDivisionError raised here, goes to first matching except
	print('Hello')                   # Not executed
except    ZeroDivisionError:
	print('ZDE  1')                  # ZDE 1
except    ZeroDivisionError:
	print('ZDE  2')                  # Not executed; duplicate except for same exception is ignored
print('Bye')                         # Bye

# Find  outputs  (Home  work)
try:
	print(7 / 0)                     # ZeroDivisionError raised here, goes to first matching except
	print('Hello')                   # Not executed
except    ZeroDivisionError:
	print('ZDE  1')                  # Not executed because previous line already raised ZDE
	print(8 / 0)                     # Not executed
except    ZeroDivisionError:
	print('ZDE  2')                  # Not executed
print('Bye')                         # Not executed because exception inside except is unhandled

# Find  outputs
try:
	print(7 / 0)                     # ZeroDivisionError occurs here → jumps to first except block
	print('Hello')                   # Not executed
except ZeroDivisionError:
	print('ZDE  1')                  # ZDE  1
	try:
		print(8 / 0)                 # ZeroDivisionError occurs here → goes to inner except
	except ZeroDivisionError:
		print('ZDE   2')            # ZDE   2
	print('Bye')                     # Bye
except ZeroDivisionError:           # Not executed (already handled by first except)
	print('ZDE  3')
print('End')                         # End

'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)                         # Raises ZeroDivisionError (which is a subclass of ArithmeticError)
except ArithmeticError:                 # This catches it, since it's the parent class
	print('Arithmetic Error')           # Arithmetic Error
except ZeroDivisionError:
	print('Zero Division  Error')       # Not executed, already handled above
print('End')                             # End

# Find  outputs  (Home  work)
def f1():
	try:
		print('f1  function')            # f1  function
		print(7 / 0)                     # Raises ZeroDivisionError (not caught here)
	except ValueError:
		print('Hello')                  # Not executed

	try:
		print(int('Ten'))               # Raises ValueError
	except ZeroDivisionError:
		print('Bye')                    # Not executed
	print('End  of  f1  function')      # Not executed (due to unhandled ZeroDivisionError above)
# End of f1  function
try:
	print('Begin')                     # Begin
	f1()                               # f1() raises ZeroDivisionError not caught inside
	print('Hi')                        # Not executed
except ZeroDivisionError:
	print('ZDE  is  caught  outside')  # ZDE is caught outside
except:
	print('Bye')                       # Not executed
print('End')                           # End

# Find  outputs  (Home  work)
def f1():
	try:
		print('f1  function')                          # f1  function
		print(7 / 0)                                   # Raises ZeroDivisionError
	except ValueError:
		print('Hello')                                 # Not executed
	except ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')      # ZDE  is  caught  by  f1  function
	print('End  of  f1  function')                     # End  of  f1  function

# End of function

try:
	print('Begin')                                    # Begin
	f1()                                              # Calls f1(), exception handled inside
	print('Hello')                                    # Hello
except ZeroDivisionError:
 	print("Hi")                                       # Not executed
except ValueError:
	print("Bye")                                      # Not executed

print('End')                                          # End

'''
What  are   the  outputs  if  input  is  1 ?  --->

What  are   the  outputs  if  input  is  2 ?  --->

What  are   the  outputs  if  input  is  3 ?  --->

What  are   the  outputs  if  input  is  4 ?  --->

What  are   the  outputs  if  input  is  5 ?  --->

What  are   the  outputs  if  input  is  6 ?  --->

What  are   the  outputs  if  input  is  7 ?  --->

What  are   the  outputs  if  input  is  8 ?  --->
'''
ch = eval(input('Enter  choice (9-exit) : '))
while ch < 9:
    try:
        match ch:
            case 1:
                list = [10 , 20 , 15 , 12 , 18]
                print(list[5])            # IndexError
            case 2:
                s = 'Hyd'
                print(s[3])              # IndexError
            case 3:
                print(int('Two'))        # ValueError
            case 4:
                a = 25
                print(len(a))            # TypeError
            case 5:
                print(eval('Hyd'))       # NameError
            case 6:
                print(7 / 0)             # ZeroDivisionError
            case 7:
                print('No Error')        # Normal case
            case 8:
                print('Handled Case 8')  # Normal case
    except Exception as e:
        print('Exception Caught :', e)
    ch = eval(input('Enter  choice (9-exit) : '))

#Find  outputs  (Home  work)
def f1(a):
	print('f1  function')
	if a == 20:
		raise ArithmeticError()
	elif a == 0:
		raise IndexError()
	elif a == 10:
		raise TypeError(25)
	raise ValueError()
# end of  the function

try:
	print('Begin')                                # Begin
	f1(10)                                        # f1  function
                                                 # Raises TypeError(25)
	f1(20)
	f1(30)
	f1(0)
except ArithmeticError:
	print('Hyd')
except IndexError:
	print('Sec')
except TypeError as msg:
	print('Caught  TypeError  outside  the  function :  '  , msg)
except ValueError:
	print('Hello')
except:
	print('some error')
print('End')                                      # End

# Find  outputs  (Home  work)
def f1(a):
	try:
		if a == 10:
			raise ValueError(25)
		elif a == 20:
			raise NameError(10.8)
		elif a == 30:
			raise IndexError('Hyd')
		raise EOFError(True)
	except IndexError as msg:
		print('Caught  IndexError  : ', msg)  # Caught  IndexError  :  Hyd
	except ValueError as msg:
		print('Caught  ValueError  : ', msg)  # Caught  ValueError  :  25
	except NameError as msg:
		print('Caught   NameError  : ', msg)  # Caught   NameError  :  10.8
	except EOFError as msg:
		print('Caught   EOFError  : ', msg)  # Caught   EOFError  :  True
	print('End  of  f1  function')           # End  of  f1  function

#outside the function
f1(10)   # Caught  ValueError  :  25
         # End  of  f1  function
f1(20)   # Caught   NameError  :  10.8
         # End  of  f1  function
f1(30)   # Caught  IndexError  :  Hyd
         # End  of  f1  function
f1(0)    # Caught   EOFError  :  True
         # End  of  f1  function
print('End of the program')  # End of the program

#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')  # f1 function
		raise ValueError(25)
		print('Hi')
	except ValueError as msg:
		print('Caught by f1 function  : ', msg)  # Caught by f1 function  :  25
		raise ValueError(msg)
	except:
		print('Hello')
	print('End of f1 function')  # (This line will NOT execute due to raised exception)

# End of f1() function
try:
	print('Begin')  # Begin
	f1()
	print('Hyd')    # (This line will NOT execute due to raised exception)
except ValueError as x:
	print('Recaught ValueError  : ', x)  # Recaught ValueError  :  25
except:
	print('Some other error')
print('End of the program')  # End of the program

# Find  outputs  (Home   work)
def f1():
	try:
		print('f1 function')                        # f1 function
		raise  ValueError(25)
		print('Hi')                                 # (This line won't execute)
	except  ValueError  as  msg:
		print('Caught  by  f1 function  :  ' , msg) # Caught  by  f1 function  :  25
		raise  NameError(msg)
	except:
		print('Hello')
	print('End of f1 function')                     # (This line won't execute)

# outside the function
try:
	print('Begin')                                 # Begin
	f1()
	print('Hyd')                                   # (This line won't execute)
except  ValueError  as  x:
	print('Recaught ValueError : ' , x)            # (This line won't execute)
except:
	print('Some other error')                      # Some other error
print('End of the program')                        # End of the program

# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')                   # f1  function
		raise  ValueError('Hyd')
		print('Hi')                             # (Not executed)
	finally:
		print("f1's  finally")                  # f1's  finally
	print('End  of  f1  function')              # (Not executed due to raised exception)

def  f2():
	try:
		print('f2  function')                   # f2  function
		return
		print('Hello')                         # (Not executed)
	finally:
		print("f2's  finally")                  # f2's  finally
	print('End  of  f2  function')              # (Not executed because return exits function)

def  f3():
	try:
		print('f3  function')                   # f3  function
		raise   KeyError(25)
		print('Hello')                         # (Not executed)
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)  # Caught  by  f3  function :  25
	finally:
		print("f3's  finally")                  # f3's  finally
	print('End of f3 function')                 # End of f3 function

def  f4():
	try:
		print('f4 function')                    # f4 function
		exit()
	finally:
		print("f4's  finally")                  # (Not executed; exit() terminates program)
	print('End of f4 function')                 # (Not executed)

# End  of  all  the  functions
try:
	print('Begin')                             # Begin
	f1()
	print('Hello')                             # (Not executed due to exception in f1)
except  ValueError  as  msg:
	print('ValueError  is caught :', msg)      # ValueError  is caught : Hyd

#find outputs
import sys

def  f1():
	try:
		print('f1  function')                  # f1  function
		raise  ValueError('Hyd')
		print('Hi')                            # (Not executed)
	finally:
		print("f1's  finally")                 # f1's  finally
	print('End  of  f1  function')             # (Not executed due to raised exception)

def  f2():
	try:
		print('f2  function')                  # f2  function
		return
		print('Hello')                        # (Not executed)
	finally:
		print("f2's  finally")                 # f2's  finally
	print('End  of  f2  function')             # (Not executed because return exits the function)

def  f3():
	try:
		print('f3  function')                  # f3  function
		raise   KeyError(25)
		print('Hello')                        # (Not executed)
	except  KeyError  as  msg:
		print('Caught  by  f3  function : ' , msg)   # Caught  by  f3  function :  25
	finally:
		print("f3's  finally")                 # f3's  finally
	print('End  of  f3  function')             # End  of  f3  function

def  f4():
	try:
		print("f4  function")                  # f4  function
		sys . exit()                          # Program exits here
	finally:
		print("f4's  finally")                 # (Not executed due to sys.exit())
	print('End  of  f4  function')             # (Not executed)

#End  of  all  the  functions
try:
	print('Begin')                            # Begin
	f1()                                      # Raises ValueError
	f2()                                      # (Not executed)
	f3()                                      # (Not executed)
	f4()                                      # (Not executed)
	print('Hello')                            # (Not executed)
except  ValueError  as msg:
	print('ValueError is caught :', msg)      # ValueError is caught : Hyd

'''
Find  outputs (Home  work)

Hint:  Exception  is  parent  to  all  error  classes
'''
def f1():
	try:
		print('f1  function')                 # f1  function
		raise KeyError()
		print('Hyd')                         # (Not executed)
	except KeyError:
		print('Caught  KeyError')            # Caught  KeyError
		raise Exception()                    # Raises new Exception, goes to outer except
	except:
		print('Sec')                         # (Not executed)
	finally:
		print("f1's  finally")               # f1's  finally
	print('End  of  f1  function')            # (Not executed due to raised Exception)

# End of the function
try:
	print('Begin')                           # Begin
	f1()                                     # Calls f1 and raises Exception
	print('Hello')                           # (Not executed)
except ValueError:
	print('Hello')                           # (Not executed)
except Exception:
	print('Recaught  Exception')            # Recaught  Exception
finally:
	print('Outside  finally')               # Outside  finally
print('End  of  the  program')              # End  of  the  program

# Find outputs (Home  work)
def f1():
	try:
		print('f1  function')                 # f1  function
		raise KeyError()                     # Raises KeyError
		print('Hyd')                         # (Not executed)
	except KeyError:
		print('Caught  KeyError')           # Caught  KeyError
		raise NameError()                   # Raises NameError (not caught here)
	except NameError:
		print('Sec')                         # (Not executed – already moved out due to re-raise)
	finally:
		print('f1 finally')                  # f1 finally
	print('End  of  f1 function')            # (Not executed – exception raised)

# outside function
try:
	print('Begin')                          # Begin
	f1()                                     # Calls f1
	print('Hello')                          # (Not executed – NameError raised in f1)
except ValueError:
	print('Hello')                          # (Not executed)
except Exception:
	print('Recaught  Exception')           # Recaught  Exception
except NameError:
	print('Caught  Name Error  outside')    # (Not executed – Exception is caught earlier)
finally:
	print('Outside  finally')               # Outside  finally
print('End of the program')                # End of the program

# Find  outputs  (Home   work)
def f1():
	try:
		print('f1  function')             # f1  function
		raise KeyError()                 # Raises KeyError
		print('Hyd')                     # (Not executed)
	except KeyError:
		print('Caught  KeyError')       # Caught  KeyError
		raise NameError()               # Raises NameError (unhandled in this function)
	except NameError:
		print('Sec')                    # (Not executed – not reached due to re-raise)
	finally:
		print('f1 finally')              # f1 finally
	print('End  of  f1 function')        # (Not executed – exception propagates)

# outside function
try:
	print('Begin')                      # Begin
	f1()                                 # Call to f1
	print('Hello')                      # (Not executed due to NameError)
except ValueError:
	print('Hello')                      # (Not executed – not a ValueError)
except KeyError:
	print('Recaught  KeyError')         # (Not executed – not a KeyError anymore)
finally:
	print('Outside  finally')           # Outside  finally
print('End of the program')            # End of the program

# Find  outputs  (Home  work)
try:
	print('try')              # try
	print(7 / 0)              # ZeroDivisionError occurs here
except:
	print('except')           # except
else:
	print('else')             # (not executed due to exception)
finally:
	print('finally')          # finally
print('End')                 # End

# Find  outputs  (Home  work)
try:
	print('try')          # try
except:
	print('except')       # (not executed because no exception)
else:
	print('else')         # else
finally:
	print('finally')      # finally
print('End')             # End

# Identify   error   (Home  work)
try:
	print('try')       # try
else:                 # Error: 'else' without 'except'
    print('else')
finally:
    print('finally')
print('End')

# Identify  error   (Home  work)
try:
	print('try')        # try
except:
	print('except')     # except
else:
	print('else1')      # first else is valid
else:                  # Error: duplicate 'else' clause
	print('else2')
finally:
	print('finally')    # finally
print('end')           # end

# Identify  error   (Home  work)
try:
	print('try')       # Executes the try block
else:                 # Error: 'else' cannot appear before 'except'
	print('else')
except:
	print('except')
finally:
	print('finally')
print('end')

# Find  outputs   (Home  work)
try:
	print('try')               # try
except:
	print('except')            # (not executed since no exception is raised)

if 10 > 20:                    # False
	print('if')               # (skipped)
else:
	print('else')             # else

# Find  outputs
def f1():
	try:
		return 10         # This executes successfully, so 10 is returned
	except:
		return 20         # Not executed, since there's no exception
	else:
		return 30         # Also not executed; 'else' is ignored if 'try' returns
print(f1())                 # Output: 10

# Find  outputs
def f1():
	try:
		return 10 + '20'    # TypeError occurs here: cannot add int and str
	except:
		return 20           # This gets executed due to the exception
	else:
		return 30           # This is skipped if an exception occurs

print(f1())                 # So, this prints the result from the except block

# Find  outputs
def f1():
	try:
		pass               # No error occurs here
	except:
		return 20         # Skipped since no exception
	else:
		return 30         # Executed since try succeeds

print(f1())

# Find  outputs
def f1():
	try:
		return 10       # This line will try to return 10
	except:
		return 20       # This is skipped since no exception
	else:
		return 30       # This is also skipped (else block executes only if no exception AND no return in try)
	finally:
		return 40       # This overrides the return from try block

print(f1())

'''  (Home  work)
1) What  is  the  output  if  input  is  24 ?  --->

2) What  is  the  output  if  input  is  25 ?  --->
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert x >= 25 , 'Hyd'
	print('Sec')
except AssertionError as msg:
	print(msg)
print('End')

''' (Home  work)
1) What  is  the  output  when  input  is  24 ?  --->

2) What  is  the  output  when  input  is  25 ?  --->
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert x >= 25
	print('Sec')
except AssertionError as msg:
	print(msg)
print('End')

# Find  outputs   (Home  work)
try:
	print('Outer   try')                            # Outer   try
	try:
		print('Inner    try')                       # Inner    try
		print(7 / 0)                                # Exception: ZeroDivisionError
		int('Hyd')                                  # Skipped
		'Hyd'[5]                                    # Skipped
		eval('Hyd')                                 # Skipped
	except   ZeroDivisionError:
		print('ZDE   of   inner   try')             # ZDE   of   inner   try
		int('Ten')                                  # Raises ValueError here (unhandled in this block)
	except  ValueError:
		print('ValueError  of  inner  try')         # Skipped (not reached because above exception already raised)
	finally:
		print('Inner  try  finally')                # Inner  try  finally
	print('End  of  inner  try')                    # Skipped (exception occurred and not caught inside inner try)
except   ValueError:
	print('ValueError  of  outer  try')            # ValueError  of  outer  try
except   IndexError:
	print('IndexError  of  outer  try')            # Skipped
except:
	print('default  except  of  outer  try')       # Skipped
finally:
	print('Outer  try  finally')                   # Outer  try  finally
print('End  of  outer  try')                       # End  of  outer  try

#  Find outputs   (Home  work)
try:
	print('Outer  try')                      # Outer  try
	try:
		print('Inner  try')                  # Inner  try
		int('Hyd')                          # Raises ValueError here
		'Hyd'[5]                            # Skipped
		eval('Hyd')                         # Skipped
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')        # Skipped
		int('Ten')                          # Skipped
	except  ValueError:
		print('ValueError  of  inner  try ') # ValueError  of  inner  try 
	finally:
		print('Inner  try  finally')        # Inner  try  finally
	print('End  of  inner  try')            # End  of  inner  try
except  ValueError:
	print('ValueError  of  outer try')      # Skipped (handled in inner try)
except  IndexError:
	print('IndexError of outer try')        # Skipped
except:
	print('default except of outer try')    # Skipped
finally:
	print('Outer try finally')              # Outer try finally
print('End of outer try')                   # End of outer try
#  Find outputs   (Home  work)
try:
	print('Outer  try')                      # Outer  try
	try:
		print('Inner  try')                  # Inner  try
		'Hyd'[3]                             # Error: IndexError (index 3 is out of range)
		eval('Hyd')                          # Skipped (not reached)
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')         # Skipped
		int('Ten')                           # Skipped
	except  ValueError:
		print('ValueError  of  inner  try ') # Skipped
	finally:
		print('Inner  try  finally')         # Inner  try  finally
	print('End  of  inner  try')             # Skipped due to unhandled IndexError in inner try
except  ValueError:
	print('ValueError  of  outer  try')      # Skipped
except  IndexError:
	print('IndexError  of  outer  try')      # IndexError is caught here
except:
	print('default except of outer try')     # Skipped
finally:
	print('Outer try finally')               # Outer try finally
print('End  of  outer  try')                 # End  of  outer  try

#  Find  outputs (Home  work)
try:
	print('Outer  try')              # Outer try
	try:
		print('Inner  try')          # Inner try
		'Hyd'[3]                     # IndexError occurs here
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')  
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally') # Inner try finally
	print('End  of  inner  try')     
except  ValueError:
	print('ValueError  of  outer  try')
except  IndexError:
	print('IndexError  of  outer  try')
except:
	print('default except of outer try') # default except of outer try
finally:
	print('Outer try finally')      # Outer try finally
print('End  of  outer  try')         # End of outer try

#  Find  outputs (Home  work)
try:
	print('Outer  try')                  # Outer  try
	try:
		print('Inner  try')              # Inner  try
		print(10 + '20')                # TypeError occurs here
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')     # Inner  try  finally
	print('End of inner try')           
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer  try  finally')         # Outer  try  finally
print('End  of  outer  try')             # End  of  outer  try

# Find  outputs   (Home  work)
class MyError(BaseException):
    def _init_(self, y):                   
        self.a = y
        print('Constructor')

# End of the class

def compute(x):
    print(x)                               # prints x
    if x > 20:
        raise MyError(x)                   # raises MyError if x > 20
    print('Hello')                         # prints 'Hello' if no exception

# End of the function

try:
    compute(10)                            # 10
                                           # Hello
    compute(30)                            # 30 → raises MyError → caught in except block
except MyError as msg:
    print('Caught MyError outside : ', msg)  # Caught MyError outside :  <__main__.MyError object at 0x...>

print('End')                               # End

# Find  outputs   (Home  work)
class MyError(NameError):                  # Custom exception inheriting from NameError
    def _init_(self):                      
        self.a = 25
        print('Constructor')
# End of the class

def compute(x):
    print(x)                               # prints x
    if x > 20:
        raise MyError()                    # raises MyError (but __init__ won't be called due to typo)
    print('Hello')                         # prints only if no exception raised
# end of the function

try:
    compute(30)                            # 30
                                           # raises MyError (no 'Constructor' printed)
    compute(10)                            # not executed
except MyError as msg:
    print('Caught MyError outside  : ', msg)  # Caught MyError outside  :  <__main__.MyError object at 0x...>
print('End')                               # End

# Find  outputs (Home  work)
try:
	print(1)          # 1
	print(2)          # 2
	print(3)          # 3
except:
	print(4)
else:
	print(5)          # 5
finally:
	print(6)          # 6
print(7)              # 7

# Find  outputs   (Home  work)
try:
	print(1)          # 1
	print(7 / 0)      # Raises ZeroDivisionError
	print(3)          # Skipped
except:
	print(4)          # 4 (handled by general except block)
else:
	print(5)          # Skipped because exception occurred
finally:
	print(6)          # 6
print(7)              # 7

# Find  outputs   (Home  work)
try:
    print(1)            # 1
    print(7 / 0)        # Raises ZeroDivisionError
    print(3)            # Skipped
except:
    int('Two')         # Error inside except block (ValueError)
else:
    print(5)            # Skipped
finally:
    print(6)            # 6
print(7)                # Skipped due to unhandled exception in except

#  Find  outputs (Home  work)
from threading import Thread

def f1():
    for i in range(10):
        print('child thread')   # Prints 10 times when called in main thread or child thread

child = Thread(target=f1)      # Thread created but not started, so f1() not run in a separate thread

f1()                          # Runs f1() in main thread — prints 'child thread' 10 times

for i in range(10):
    print('main thread')       # Prints 'main thread' 10 times

#  Find  outputs  (Home  work)
from threading import Thread
def f1():
    for i in range(10):
        print('child thread')

child = Thread(target=f1())  # f1() is called immediately here in main thread, before thread creation
child.start()                # child thread target is None (since f1() returns None), so thread runs no code

for i in range(10):
    print('main thread')

# Find  outputs  (Home  work)
from threading import *

def f1():
    for i in range(10):
        print('child thread')

child = Thread()   # Thread created without target function
child.start()      # Starts the thread — but thread has no function to run

for i in range(10):
    print('main thread')
''''output: main thread
			main thread
			main thread
			main thread
			main thread
			main thread
			main thread
			main thread
			main thread
			main thread
'''	

# Find  outputs (Home  work)
from threading import Thread

def f1():
    for i in range(10):
        print('Child Thread')

child = Thread(target=f1)
child.start()

for i in range(10):
    print('Main Thread')

child.start()  # This will cause an error
'''output:  Child Thread
			Main Thread
			Child Thread
			Main Thread
			Main Thread
			Child Thread
			...
			RuntimeError: threads can only be started once
'''
# Find  outputs  (Home  work)
from threading import *

class c1:
	def m1(self):
		for i in range(10):
			print('child thread')

a = c1()
child = Thread(target=a.m1)
a.m1()
for i in range(10):
	print('main thread')
'''output:  child thread
			child thread
			child thread
			child thread
			child thread
			child thread
			child thread
			child thread
			child thread
			child thread
			main thread
			main thread
			main thread
			main thread
			main thread
			main thread
			main thread
			main thread
			main thread
			main thread
'''
# Find  outputs (Home  work)
from threading import *

class c1:
    def m1(self):
        for i in range(10):
            print('child thread')

a = c1()
child = Thread(target=a.m1())   # Note the () here — m1() is being **called immediately**
child.start()
for i in range(10):
    print('main thread')
'''output:  child thread
			child thread
			child thread
			child thread
			child thread
			child thread
			child thread
			child thread
			child thread
			child thread
			Traceback (most recent call last):
			...
			TypeError: 'NoneType' object is not callable
'''
#  Find  outputs  (Home  work)
from threading import *

class c1:
    @classmethod
    def m1(cls):
        for i in range(1, 11):
            print('Child Thread  : ', i)

child = Thread(target=c1.m1)
child.start()

for i in range(1, 11):
    print('Main Thread  : ', i)
'''output:  Child Thread  :  1
			Main Thread  :  1
			Child Thread  :  2
			Main Thread  :  2
			Child Thread  :  3
			Main Thread  :  3
			...
			Child Thread  :  10
			Main Thread  :  10
'''
# Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start()
for  i  in  range(10):
        print('main  thread')
#output: Error: 'Thread' object has no attribute 'start'		
# Find  outputs  (Home  work)
class Thread:                         # This overrides the imported Thread class
    def run(self):
        for i in range(10):
            print('Child Thread')

from threading import Thread          # This import has no effect due to the above definition
t = Thread()                          # Refers to your custom Thread class
t.start()                             # Error: 'Thread' object has no attribute 'start'

for i in range(10):
    print('Main Thread')

# Find  outputs  (Home  work)
from threading import *

class MyThread(Thread):           # Subclassing Thread class
    def run(self):               # Overriding run() method
        for i in range(10):
            print('child  thread')

# end of the class

child = MyThread()
child.run()                      # Directly calling run() instead of start(), so it runs in main thread
for i in range(10):
    print('main  thread')

# Find  outputs (Home  work)
from threading import *

class MyThread(Thread):                 # Subclass of threading.Thread
    def walk(self):                    # Method named 'walk', NOT 'run'
        for i in range(10):
            print('Child Thread')

child = MyThread()
child.start()                          # This starts a new thread and calls the 'run()' method
for i in range(10):
    print('Main Thread')
'''output:  Main Thread
			Main Thread
			Main Thread
			Main Thread
			Main Thread
			Main Thread
			Main Thread
			Main Thread
			Main Thread
			Main Thread
'''
# Find  outputs
from threading import *

class MyThread(Thread):
    def run(self):                          # Custom run method, should be called on .start()
        print('run method')                 # But only if no 'target' is passed

def f1():
    print('f1 function')

child = MyThread(target=f1)                 # 'target=f1' overrides the run method
child.start()                               # f1() is executed instead of run()
print('Main Thread')

# Find  outputs
from threading import *

class MyThread(Thread):
    pass

def f1():
    for i in range(1, 11):
        print('f1 function :', i)

child = MyThread(target=f1)  # Thread object with f1 as the target function
child.start()                # Starts the thread and runs f1()
for i in range(1, 11):
    print('Main Thread :', i)
'''output:  f1 function : 1
			Main Thread : 1
			f1 function : 2
			Main Thread : 2
			f1 function : 3
			Main Thread : 3
			Main Thread : 4
			f1 function : 4
			Main Thread : 5
			f1 function : 5
			f1 function : 6
			Main Thread : 6
			Main Thread : 7
			f1 function : 7
			Main Thread : 8
			f1 function : 8
			Main Thread : 9
			f1 function : 9
			Main Thread : 10
			f1 function : 10
'''
# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')
#output: Main Thread
'''
1) What  are  the  outputs  for  t1 . start() ?  --->

2) What  are  the  outputs  for  t2 . start() ?  --->

3) What  are  the  outputs  for  t3 . start() ?  --->

4) What  are  the  outputs  for  t4 . start() ?  --->

5) What  are  the  outputs  for  t5 . start() ?  --->

6) What  are  the  outputs  for  t6 . start() ?  --->

7) What  are  the  outputs  for  t7 . start() ?  --->

8) What  are  the  outputs  for  t8 . start() ?  --->

9) What  are  the  outputs  for  t9 . start() ?  --->

10) What  are  the  outputs  for  t10 . start() ?  --->

11) What  are  the  outputs  for  t11 . start() ?  --->

12) What  are  the  outputs  for  t12 . start() ?  --->

13) What  are  the  outputs  for  t13 . start() ?  --->
'''
from  threading  import  *
class  MyTh…
#  What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start()
		print('Start Method')
	def   run(self):
		print('Run Method')
#  main  thread  executes  following  statements
child = MyThread()
child . start()
print('Main  Thread')
# Find  outputs (Home  work)
from threading import *

print(current_thread().name)                     # MainThread

current_thread().name = 'Hyd'                    # Changing name to 'Hyd'
print(current_thread().name)                     # Hyd

def f1():
    print(current_thread().name)                 # Sec
    current_thread().name = 'Cyb'
    print(current_thread().name)                 # Cyb
    print(active_count())                        # 2 (Main thread + Child thread)

child = Thread(target=f1, name='Sec')            # Creating a child thread with name 'Sec'
child.start()
child.join()

# Find  outputs (Home  work)
from threading import *

# Creating 3 threads
t1 = Thread(name='t1')
t2 = Thread(name='t2')
t3 = Thread(name='t3')

print('Names of Threads')                      # Names of Threads
print(f't1 : {t1.name}')                       # t1 : t1
print(f't2 : {t2.name}')                       # t2 : t2
print(f't3 : {t3.name}')                       # t3 : t3

# Modifying thread names
t1.name = 'One'
t2.name = 'Two'
t3.name = 'Three'

print('New Names of Threads')                 # New Names of Threads
print(f't1 : {t1.name}')                      # t1 : One
print(f't2 : {t2.name}')                      # t2 : Two
print(f't3 : {t3.name}')                      # t3 : Three

# Number of active threads
print(active_count())                         # 1 (Only main thread is running)

# Find  outputs (Home  work)
from threading import *

def f1():
    print('Name of child thread:', current_thread().name)

# Create a new thread with name "Child" and target function f1
t = Thread(target=f1, name='Child')

# Start the new thread
t.start()

# Print name of the main thread
print('Name of main thread:', current_thread().name)

# Find  outputs (Home  work)
from threading import *

# Create a thread t1 with name 'Hyd'
t1 = Thread(name='Hyd')

# Create another thread t2 without a name
t2 = Thread()

# Print name of main thread
print('Main thread name:', current_thread().name)

# Print name of thread t1
print('Thread t1 name:', t1.name)

# Print name of thread t2
print('Thread t2 name:', t2.name)

# Modify name of main thread to 'India'
current_thread().name = 'India'

# Modify name of thread t1 to 'Sec'
t1.name = 'Sec'

# Modify name of thread t2 to 'Cyb'
t2.name = 'Cyb'

# Print name of main thread
print('Modified main thread name:', current_thread().name)

# Print name of thread t1
print('Modified t1 name:', t1.name)

# Print name of thread t2
print('Modified t2 name:', t2.name)

# Print number of threads under execution
print('Active threads:', active_count())

# Find  outputs  (Home  work)
from threading import *

def f1(x):
    s = current_thread().name
    while True:
        print(s, ':', x)      # e.g. Hyd : 10  (repeated forever)

t1 = Thread(target=f1, name='Hyd', args=(10,))
t2 = Thread(target=f1, name='Sec', args=[20])

t1.start()                   # starts Hyd thread → begins printing "Hyd : 10"
t2.start()                   # starts Sec thread → begins printing "Sec : 20"

print(active_count())        # 3  (MainThread + Hyd + Sec)

# After this, you'll see interleaved infinite output such as:
# Hyd : 10
# Sec : 20
# Hyd : 10
# Sec : 20
# ... and so on

print('Press  ctrl + break  or  Fn + b  to  stop ')
# Find  outputs (Home  work)
from  threading  import  Thread , current_thread
from  random  import  randint
def   f1(n):
	ctr = 0
	s = current_thread() . name
	while  True:
		x = randint(1 , 100)
		ctr += 1
		print(F'{s}  guess  {x}   in  attempt  :  {ctr}')
		if   x ==  n:
			break
	#end of while loop
	print(F'{s}  finish  in  {ctr}  attempts')
t1 = Thread(target = f1 , args = [75] , name = 'Rama')
t2 = Thread(target = f1 , args = [50] , name = 'Sita')
t1 . start()
t2 . start()
'''output:  Rama  guess  12   in  attempt  :  1
			Sita  guess  34   in  attempt  :  1
			Rama  guess  67   in  attempt  :  2
			Sita  guess  29   in  attempt  :  2
			Rama  guess  75   in  attempt  :  3
			Rama  finish  in  3  attempts
			Sita  guess  60   in  attempt  :  3
			Sita  guess  50   in  attempt  :  4
			Sita  finish  in  4  attempts
'''
