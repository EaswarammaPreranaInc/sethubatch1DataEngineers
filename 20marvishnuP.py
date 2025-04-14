"""
#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  Tuple  of  4  elements  is  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka


'''
(10,20,15,18)
<class  'tuple'>
4

()
<class 'tuple'>
0

([10, 20], (30, 40, 50), {80, 90, 60, 70})
<class 'tuple'>
3

('Hyd',)
<class 'tuple'>
1

((100, 200, 150),)
<class 'tuple'>
1
'''

#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)

def  avg(*a):
	return sum(a)/len(a) if a else 0 #Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #  Average  of  10 , 20 , 15  and  18 is 15.75
print(avg(25 , 10.8 , True)) # Average 12.27
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))# Average 14.26
print(avg())# Average 0
print(avg(25))# Average 25.0
print(avg(3 + 4j , 5 + 6j))# Average (4+5j)
#tpl = (10 , 20 , 15 , 18)
#print(avg(tpl))
15.75
12.266666666666666
14.26
0
25.0
(4+5j)


#Find  outputs (Home  work)
def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a : 10	b  :  (20, 30, 40)
f1(50 , 60)#a : 50   b  :  (60,)
f1(70)#a : 70   b  :  ()
f1(a = 80) #a : 80    b  :  ()
#f1(b = (10 , 20 , 30) , a = 40)
f1()#a : 25    b  :  ()
#f1(a = 10 , (20 , 30 , 40))
#f1(25 , b = (10 , 20 , 30))
#f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)#a : (10, 20, 30)    b  :  (10, 20, 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)



#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)#a  :  (10, 20, 30)   b  :  40
f1(50 , b = 60)#a  :  (50,)   b  :  60
f1(b = 70)#a  :  ()     b  :  70
#f1(b = 10 , a = (20 , 30 , 40))
#f1(b = 10 , (20 , 30 , 40))
#f1()
#f1(10 , 20 , 30 , (10 , 20 , 30))
#f1(10 , 20 , 30 , 40)
#f1(25)
f1(10 , 20 , 30 , b = (10 , 20 , 30))#a  :  (10, 20, 30)     b  :  (10, 20, 30)



#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#a  :  10     b  :  (20, 30, 40)   c  :  50
f1(60 , 70 , c = 80)#a  :  60      b  :  (70,)    c  :  80
f1(90 , c = 100)#a  :  90     b  :  ()     c  :  100
#f1(a = 1 , 2 , c = 3)
#f1(1 , 2 , 3)
#f1(a = 1 , b = 2 , c = 3)
#f1(a = 25 , 100 , 200 , 300 , c = 35)



# Which  of  the  following  are  valid  ?  (Home  work)
#def   f1(*a , *b):
 #       pass
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
#def   f6( * , a , *b , c):
 #      pass
#def   f7(a , *b , c ,  /):
 #      pass



# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
'''
([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>
'''



# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  #  Dictionary  of  2  key : value  pairs  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()#{}

'''
Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}

Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}
'''


# Find  outputs   (Home  work)
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
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)

'''
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
'''



#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)#11
	print('b : ' , b)#40
	print('c : ' , c)#31
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)#50
	print('b : ' , b)#22
	print('c : ' , c)#32
# End  of  f2()  function
c = 30
print('a : ' , a)#10
print('b : ' , b)#20
print('c : ' , c)#30
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')



# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)#20
	a += 1
#End  of  the  function
a = 10
print(a)#10
a += 1
f1()
print(a)#11



# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)#20
	dict = globals()
	print(dict['a'])#40
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)#10
a += 1
f1()
print(a)#11


# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)#10
	print(globals()['x'])#10
# end of the function
f1()



# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)#20
	#print(globals()['x'])#20
# End  of  the  function
f1()




# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)#40, 50, 60 
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])#100, 200, 300
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)#10, 20, 30
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()


# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)#20
def   f2():
	global  x
	x = 30
	print(x)#31
	x += 1
def   f3():
	global  y
	y = 40
	print(y)#40
	y += 1
def   f4():
	x = 50
	#global   x
#  End  of  the  functions
x = 10
print(x)#10
x += 1
f1()
print(x)#11
f2()
print(x)#31
x += 1
f3()
print(y)#41
f4()
print(x)#32

"""

