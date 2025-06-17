# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')
def  f2():
	try:
		print('f2  function')
		return
		print('Hello')
	finally:
		print("f2's  finally")
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)
	finally:
		print("f3's  finally")
	print('End of f3 function')
def  f4():
	try:
		print('f4 function')
		exit()
	finally:
		print("f4's  finally")
	print('End of f4 function')
# End  of  all  the  functions
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
f2()
f3()
try:
	f4()
finally:
		print('Outside  finally')
print('End  of  the  program')
"""
Output:
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :   Hyd
f2  function
f2's  finally
f3  function
Caught  by  f3  function :   25
f3's  finally
End of f3 function
f4 function
f4's  finally
Outside  finally
"""

# Find  outputs  (Home  work)
import sys
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')
def  f2():
	try:
		print('f2  function')
		return
		print('Hello')
	finally:
		print("f2's  finally")
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')
	except  KeyError  as  msg:
		print('Caught  by  f3  function : ' , msg)
	finally:
		print("f3's  finally")
	print('End  of  f3  function')
def  f4():
	try:
		print("f4  function")
		sys . exit()
	finally:
		print("f4's  finally")
	print('End  of  f4  function')
#End  of  all  the  functions
try:
	print('Begin')
	f1()
	f2()
	f3()
	f4()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
print('End  of  the  program')
"""
Output:
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :   Hyd
End  of  the  program
"""


#Find  outputs (Home  work)
#Hint:  Exception  is  parent  to  all  error  classes
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise  Exception()
	except:
		print('Sec')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')
#End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')
finally:
	print('Outside  finally')
print('End  of  the  program')
"""
Output:
Begin
f1  function
Caught  KeyError
f1's  finally
Recaught  Exception
Outside  finally
End  of  the  program
"""

# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise  NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')
#outside function
try:
	print('Begin')
	f1()
	print('Hello')
except ValueError:
	print('Hello')
except   Exception:
	print('Recaught  Exception')
except  NameError:
	print('Caught  Name Error  outside')
finally:
	print('Outside  finally')
print('End of the program')
"""
Output:
Begin
f1  function
Caught  KeyError
f1 finally
Recaught  Exception
Outside  finally
End of the program
"""

# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		#raise   NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')
#outside function
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except   KeyError:
	print('Recaught  KeyError')
finally:
	print('Outside  finally')
print('End of the program')
"""
Output:
Begin
f1  function
Caught  KeyError
f1 finally
End  of  f1 function
Hello
Outside  finally
End of the program
"""
