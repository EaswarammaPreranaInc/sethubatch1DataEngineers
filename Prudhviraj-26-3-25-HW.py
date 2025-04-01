#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1)
print('End')

"""
Output:
Begin
f2  function
f1  function
Back  to  f2  function
End
"""

#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	#fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')
"""
Output:
Begin
f1  function
f2  function
Back  to  f2  function
End
"""

# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer()
print('Hello')
fun()
print('Bye')
#inner()
"""
Output:
Outer  Function
Hello
Inner function
Bye
"""

# Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function')
	def  inner1():
		print('1st  inner  function')
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function")
	# End  of  inner2
	if   x == 10:
		return  inner1
	else:
		return  inner2
#end of the function
f1 = outer(10)
f2 = outer(20)
f1()
f2()

"""
Output:
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function
"""

# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()
"""
Output:
Hi
Hello
"""

#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun .__name__)
	def   inner():
		return   fun() +  2
	return  inner
@decor
def   f1():
	return  10
# End of the function
print('End')
"""
Output:
f1
End
"""

#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1)
print(f1())
"""
Output:
12
"""

# Find  outputs(Home  work)
def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))
print(div(10 , 0))
#print(inner(10 , 3))
"""
Output:
3.3333333333333335
Division   by  0  is  not  permitted
"""

# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(div):
	def inner(a,b):
		if a<b:
			a,b=b,a
		print(div(a,b))
	return inner
@decor
def  div(a , b):
    return   a /b
div(9 , 2) #  4.5
div(2 , 9) #  4.5

#  Find  outputs (Home  work)
def   decor(fun):
	def   inner():
		print(F'Decorating  {fun . __name__}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')
"""
Output:
Decorating  f1  function
Hello
Decoration  is  finished
Bye
"""

# Gift
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)
	def   inner(*x):  #  x  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unapcks  object   'x'  to  elements
		print('End  of  decoration')
	return  inner
@decor
def   f1(x):
	print('f1  function  :  ' , x)
@decor
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor
def   f4():
	print('f4 function')
# end of function
f1(10)
f2(25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j)
f4()
"""
Output:
f1
f2
f3
f4
(10,)
f1  function  :   10
End  of  decoration
(25, 10.8)
f2  function  :   25 10.8
End  of  decoration
('Hyd', True, (3+4j))
f3 function :  Hyd True (3+4j)
End  of  decoration
()
f4 function
End  of  decoration
"""

# Find  outputs  (Home  work)
def  square(fun):
	def  inner1():
		x = fun()
		return  x * x
	return  inner1
def   double(fun):
	def  inner2():
		y = fun()
		return  2 * y
	return   inner2
@double
@square
def  num():
	return  10
#end of the function
print(num())
"""
Output:
200
"""

# Find  outputs  (Home  work)
def   bold(fun):
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'
	return  inner1
def   italic(fun):
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun):
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1())
"""
Output:
<b><i><u>Hello  World</u></i></b>
"""

'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3

2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
def  gcd(m , n):
	if n == 0:
		return m
	else:
		return gcd(n, m % n)
'''
1) gcd(4 , 6)  --->
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,gcd(m,n))
