#  Variable  number  of  arguments  demo  program
'''def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  (10,20,15,18)
f1()#()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})#([10,20],(30,40,50),{60,70,80,90})
f1('Hyd')#('hyd',)
tpl = (100 , 200 , 150)
f1(tpl)#((100,200,300),)
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka'''

#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
'''try:
	def  avg(*a):
				 return sum(a)/len(a)

	


	# End  of  the  function
	print(avg(10 , 20 , 15 , 18)) #  Average  of  10 , 20 , 15  and  18
	print(avg(25 , 10.8 , True))
	print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
	print(avg(25))
	print(avg(3 + 4j , 5 + 6j))
	tpl = (10 , 20 , 15 , 18)
	#print(avg(tpl))
	print(avg())
except ZeroDivisionError:

	print('error for 0 element')
#Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)'''

'''def  concat(*a):
	
	return ' '.join(a)

	
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
#print(concat(1, 2, 3))'''

#Find  outputs (Home  work)
'''def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)
f1(50 , 60)
f1(70)
f1(a = 80)
#f1(b = (10 , 20 , 30) , a = 40)
f1()
#f1(a = 10 , (20 , 30 , 40))
#f1(25 , b = (10 , 20 , 30))
#f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)'''

#Find  outputs (Home  work)
'''def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)#error
f1(50 , b = 60)#a=(50,)b=60
f1(b = 70)#a(),b=70
#f1(b = 10 , a = (20 , 30 , 40))#error
#f1(b = 10 , (20 , 30 , 40))
#f1()
#f1(10 , 20 , 30 , (10 , 20 , 30))#((10,20,30),)=a,b=(10,20,300
#f1(10 , 20 , 30 , 40)#
#f1(25)
f1(10 , 20 , 30 , b = (10 , 20 , 30))'''

#Find  outputs (Home  work)
'''def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#a=10 b=(20,30,40) c=50
f1(60 , 70 , c = 80)# a=60 b=(70,) c=80
f1(90 , c = 100)
#f1(a = 1 , 2 , c = 3)
#f1(1 , 2 , 3)
#f1(a = 1 , b = 2 , c = 3)#error
#f1(a = 25 , 100 , 200 , 300 , c = 35)# a=25 b=(100,200,300) c=3'''

'''# Which  of  the  following  are  valid  ?  (Home  work)
#def   f1(*a , *b):
    #    pass
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
def   f6( * , a , *b , c):
       pass
def   f7(a , *b , c ,  /):
       pass

# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))'''

# Variable  number  of  keyword  arguments  demo  program
'''def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao') 
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()'''

'''# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)'''

'''#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0)
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)'''

'''# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)
print()
f1('Hyd' , 10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)'''

#Find  outputs (Home  work)
#Find  outputs (Home  work)
'''a = 10
def   f1():
	b = 40
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')'''

'''# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1

a = 10
print(a)
a += 1
f1()
print(a)'''

# Find  outputs  (Home  work)
'''def   f1():
	a = 20
	print(a)
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)
a += 1
f1()
print(a)'''


'''# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	
	print(globals()['x'])
	
# end of the function
f1()'''

# Find  outputs (Home  work)
'''def  f1():
	x = 20
	print(x)
	print(globals()['x'])
# End  of  the  function
f1()'''

# Find outputs (Home  work)
'''def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()'''

'''# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)#20
def   f2():
	global  x
	x = 30
	print(x)#30
	x += 1 #31
def   f3():
	global  y
	y = 40
	print(y)#40
	y += 1
def   f4():
	x = 50
#	global   x
#  End  of  the  functions
x = 10
print(x)#10
x += 1 #11
f1()
print(x)#11
f2()
print(x)#31
x += 1 #32
f3()
print(y)#41
f4()
print(x)'''

'''# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)#20
	print(globals()['a'])#20
	a = 30
# End of the function
a = 10
print(a) #10
f1()
print(a)#30'''

# Find  outputs(Home  work)
'''def  f1():
	global  a
	#print(a)
	a = 10
	print(globals()['a'])#10
	a = 20
	print(a)#20
	a = 30
def  f2():
	print(a)#30
# End  of   f2   function
f1()
f2()
print(a)'''

# Find outputs (Home  work)
'''def  f1():
	global   a
	a = 10
	print(a)#10
	a = 20
def  f2():
	global  a
	print(a)#20
	a = 30
def  f3():
	print(a)#30
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)#40'''

'''#  Find  outputs (Home  work)
def  f1():
        a = 10
        #global  a
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()
#print(a)#10
print(b)#120'''

# Find outputs (Home  work)
'''def  f1():
        global  a
        print(a)#11
        a += 1 #12
def  f2():
        global  a
        print(a)#13
        a += 1
# End  of  the  function
a = 10
print(a)#10
a += 1 #11
f1()
print(a)#12
a += 1 #13
f2()
print(a)#14'''

'''# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)#20
def  f2():
	pass
	#print(a)#11
	#a += 1 #12
# End of the function
a = 10
print(a)#10
f1()
a += 1 #11
f2()
print(a)#11'''

#  Find   outputs
def   f1():
	x = x + 5
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)#15
# End of f2  function
x = 10
f1()
f2()
print(x)#10

