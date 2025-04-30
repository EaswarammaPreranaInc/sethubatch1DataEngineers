# 1 return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')
x =  f1()
print(x)
print('End')

'''
Begin
f1 function
25
End'''

# 2.Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')
'''
Begin
Hyd
Sec
Cyb
<class 'NoneType'> ###-->as it is not returning anything
End		'''

#  Gift
# 3. Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)			# (10 , 20 , 30)
print(type(x))		# <class 'tuple'>
a , b , c =  f1()
print(a)			## 10
print(b)			## 20
print(c)			## 30
print('for  loop')	#for  loop
for  k   in   f1():
	print(k)		#10 <nextline>  20 <nextline> 30
	
# 4.Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
x = f1()
print(x)
print('End')
#return   100	#Error
'''
Begin
10
End
'''

# 5. Find  outputs
#f1()	#ERROR function not defined
def   f1():
        print('Hello')
print(f1())	# Hello
print(f1)	# None  #<function f1 at 0x00000168F34A04A0>

# 6. Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
'''
Hello
Hi
f1 function
None 
## <function f1 at 0x0000021225D104A0>
Bye
'''

# 7. Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')
'''
Begin
<class 'function'>	###
Address maybe 1000
End
'''

# 8. Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)	# Three  argument  function :  10  20  30
#f1(40 , 50)		# ERROR
#f1(60)				# ERROR
#f1()				# ERROR

# 9. Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(20)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(10,20)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10,20,30)


'''
10. Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself
2) Let  input  be  25
    What  is  the  range  of  divisors ? --->  i =   2 , 3 , 4 , 5 , 6 , ..... 12
3) Let  input   be  11
    What  is   the  range  of  divisors ? --->  i =  2 , 3 , 4 , 5
4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object
5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  ---> return   False
6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
'''
'''
1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->
2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->
3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->
4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->
'''
def prime(n):
	for i in range(2,n//2+1):
		if n%i==0:
			return False
	return True

a = int(input('Enter a number : '))#How  to  read  a  number
if   a<0:#input  is  invalid:
	print('Invalid  input')
elif  prime(a):#input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')

# 11. Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)	# Emp  Number  :  25 \t  Emp Name  :  Rama  Rao \t  Salary  :  10000.0
disp('Sita' , 20000.0 , 35)			# Emp  Number  :  Sita \t  Emp Name  :  20000.0 \t  Salary  :  35

# 12. Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)		#  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')				#  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#  a :  'Cyb'  <tab>  b :  'Sec'  <tab>  c :  'Hyd'
f1(c = 3 + 4j , a = True , b = None) #  a :  True   <tab>  b :  None  <tab>  c :  3+4j
f1(25 , c = 10.8 , b = 'Hyd')		 #  a :  25   <tab>  b :  'Hyd'  <tab>  c :  10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'

# 13. Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)					  # Emp  Number : 25  \t  Emp  Name : Rama Rao  \t  Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Emp  Number : 35  \t  Emp  Name : Sita  \t  Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)		## Emp  Number : Rama  Rao  \t  Emp  Name : 30000.0  \t  Salary : 20

#  Gift
# 14. Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))						# 23
print(f1(*[6 , 7 , 8]))						# 62
#print(f1([6 , 7 , 8]))						# ERROR
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))			### 16 --> 1+3*5
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))  ### 14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))   # ERROR
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})   #### {'c': 2, 'b': 4, 'a': 6}
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))	# ERROR

# 15.Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a))	#ERROR
#print(sorted(a , rev = True))		#ERROR
#print(25 , 10.8 , 'Hyd' , separator = '\t') #ERROR
#print(25 , 10.8 , 'Hyd' , endofline = '\t') #ERROR
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') # ERROR