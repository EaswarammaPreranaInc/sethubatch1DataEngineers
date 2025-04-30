#20/3/2025 

#1.Variable  number  of  arguments  demo  program

'''
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   # (10,20,15,18) \n <class 'tuple'> \n 4
f1() # () \n <class 'tuple'> \n 0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) # ([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) \n <class 'tuple'> \n 3
f1('Hyd') # ("Hyd",) \n <class 'tuple'> \n 1
tpl = (100 , 200 , 150)
f1(tpl) # ((100,200,150),) \n <class 'tuple'> \n 1
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka

'''


#2.Write  a  function  to  determine  average  of  arguments  passed  from  function  call 

'''
try:
    def  avg(*a):
        
    	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
    	return sum(a)/len(a)
    	
    # End  of  the  function
    
    print(avg(10 , 20 , 15 , 18)) #15.75
    print(avg(25 , 10.8 , True))  #12.2666666666666666
    print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) #14.26 
    #print(avg()) #Error due to  ZeroDivisionError 
    print(avg(25)) # 25.00
    print(avg(3 + 4j , 5 + 6j)) #(4+5j)
    tpl = (10 , 20 , 15 , 18)
    print(avg(tpl)) #Error Type 
    
except ZeroDivisionError:
    print('Atleast pass one number')
    
except TypeError:
    print("Can't add a 2D sequence")
    
'''



#3.Write  a  function  to  concatenate  strings  passed  from  the  function  call ?

'''
try:
    
    def  concat(*a):
    	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
    	
    	return ' '.join(a)
    	
    # End   of  the   function
    print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
    print(concat('Hyd', 'Is', 'Green', 'City')) #Hyd Is Green City
    print(concat('Python', 'Is', 'A', 'Great', 'Language')) #Python Is A Great Language
    print(concat()) #No o/p
    print(concat('Python')) #Python
    print(concat(1, 2, 3)) #Error str + int 
    
except TypeError:
    print("Can't concatinate string and int ")
  
 '''
 
 
#4.Find  outputs

'''
def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) #a : 10  \t   b  :  (20,30,40)
f1(50 , 60) #a : 50  \t   b  :  (60,)
f1(70) #a : 70  \t   b  :  ()
f1(a = 80) #a : 80  \t   b  :  ()
#f1(b = (10 , 20 , 30) , a = 40) #Error can't pass KA to *b 
f1() #a : 25  \t   b  :  ()
#f1(a = 10 , (20 , 30 , 40)) #Error due to PA after KA 
#f1(25 , b = (10 , 20 , 30)) #Error can't pass KA to *b 
#f1(25 , a = (10 , 20 , 30)) #Error due to a got multiple values 
f1((10 , 20 , 30) , 10 , 20 , 30) #a : (10,20,30) \t   b  :  (10,20,30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30) #Error due tp PA after KA


'''


#5.Find  outputs 

'''
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) #a  :  (10,20,30)   \t   b  :  40
f1(50 , b = 60) #a  :  (50,)   \t   b  :  60
f1(b = 70) #a  :  ()   \t   b  :  70
#f1(b = 10 , a = (20 , 30 , 40)) #Error due to KA to var arg a
#f1(b = 10 , (20 , 30 , 40)) #Error No PA after KA 
#f1() #Error due to no arg for b 
#f1(10 , 20 , 30 , (10 , 20 , 30)) #Error due to no arg for b 
#f1(10 , 20 , 30 , 40) #Error due to no arg for b 
#f1(25) #Error due to no arg for b
f1(10 , 20 , 30 , b = (10 , 20 , 30)) #a  :  (10,20,30)   \t   b  :  (10,20,30)

'''


#6.Find  outputs 

'''
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) #a  :  10  \t  b  :  (20,30,40)  \t  c  :  50
f1(60 , 70 , c = 80) #a  :  60  \t  b  :  (70,)  \t  c  :  80
f1(90 , c = 100) #a  :  90  \t  b  :  ()  \t  c  :  100
#f1(a = 1 , 2 , c = 3) #Error No PA after KA 
#f1(1 , 2 , 3) #Error no arg for c
#f1(a = 1 , b = 2 , c = 3) #Error no KA for *b
#f1(a = 25 , 100 , 200 , 300 , c = 35) # Error no PA after KA

'''


#7.Which  of  the  following  are  valid  ?

'''
#def   f1(*a , *b): #Error ambiguity and no KA 
        #pass
def  f2(*a , b): #valid 
        pass
def  f3(a , *b): #valid
        pass
def  f4(a , b): #valid
        pass
def    f5(a , *b , c): #valid
        pass
#def   f6( * , a , *b , c): #invalid DF non DF ambiguity
       #pass
#def   f7(a , *b , c ,  /): #invalid first / next *
       #pass
       
'''


#8.Find  outputs

'''
def   f1(*a):
	print(a) #([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a)) #<class 'tuple'>
	for  x  in  a:
		print(x) #[10,20] \n <class 'list'> \n {30,40} \n <class 'set'> \n (50,60) \n <class 'tuple'>
		print(type(x)) 
		
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))

'''

#9.Variable  number  of  keyword  arguments  demo  program
'''
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  
#Results \n <class 'dict'>  {'RollNo' : 10 , 'StudName' : 'Rama  Rao'}
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
#Results \n <class 'dict'>  {'EmpNo' : 25 , 'EmpName' : 'Sita' , 'Salary' : 10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
#Results \n <class 'dict'>  {'AcNo': 30 , 'CustName' : 'Kiran' , 'Balance' : 20000.0 , 'Gender' : 'm'}
disp() 
#Results \n <class 'dict'>  {}

'''

#11.Find  outputs 

'''
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
#Results \n 'Empno'...25 \n  'Empname'... 'Rama  Rao' \n 'Salary'...10000.0  \n 'Gender'...'m'
f1() #Results \n

'''


#12.Find  outputs 

'''
def   f1(*a):
	print(type(a)) #<class 'tuple'>
	print(a) #(25 , 10.8 , 'Hyd' , True)
def   f2(**a):
	print(type(a)) #<class 'dict'>
	print(a) #{'EmpNum':25 , 'EmpName' : 'Sita' , 'Salary' : 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

'''

#13.Find  outputs

'''
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
	
def   f2(**a):
	print(a)
# End  of  the  function

f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
#Emp  Number  :  25  \t  Emp  Name  :  'Sita'  \t  Salary  :	10000.0

#f1(eno = 25 , empname = 'Sita' , salary = 10000.0)
#Error no KA eno empname salary 

f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
#{'empno': 25 , 'ename' : 'Sita' , 'sal' : 10000.0}

f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
#{'eno': 25 , 'empname' : 'Sita' , 'salary' : 10000.0}

'''

#14.Find  outputs 

'''
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function

f1(25) # 25 \n 
print()
f1('Hyd' , 10 , 20 , 30) # 'Hyd' \n (10,20,30) 
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
# 10.8 \n (25,'Hyd',True), {'EmpNo':12 , 'EmpName':'Rama Rao', 'Salary': 10000.0}

'''


#15.Find  outputs

'''
a = 10
def   f1():
	b = 40
	print('a : ' , a) #5. a: 11
	print('b : ' , b) #6. b: 40
	print('c : ' , c) #7. c: 31
	print() #8. blank 
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a) #9.  a: 50
	print('b : ' , b) #10. b: 22
	print('c : ' , c) #11. c: 32
# End  of  f2()  function
c = 30
print('a : ' , a) #1. a: 10
print('b : ' , b) #2. b: 20
print('c : ' , c) #3. c: 30
print() #4. blank 

a +=  1 #a(11)
b +=  1 #b(21)
c +=  1 #c(31)
f1()
a +=  1 #a(12)
b +=  1 #b(22)
c +=  1 #c(32)
f2()
print('Bye') #12. Bye

'''

#16.Find  outputs

'''
def   f1():
	a = 20
	print(a) #2. 20
	a += 1 #a(21) Local 
	
#End  of  the  function
a = 10
print(a) #1. 10
a += 1 #a(11)
f1()
print(a) #3. 11

'''

#17.Find  outputs 

'''
def   f1():
	a = 20
	print(a) #2. 20
	dict = globals() #{'a':11}
	print(dict['a']) #3. 11
	a = 30 #local a(30)
	dict['a'] = 40 #{'a':40}
#  End  of  f1()  function
a = 10
print(a) #1. 10
a += 1 #a(11)
f1()
print(a) # 4. 40

'''

#18.Find  outputs

'''
x = 10
def   f1():
	print(x) #10
	print(globals()['x']) #10
# end of the function
f1()

'''

#19.Find  outputs

'''
def  f1():
	x = 20
	print(x) #20
	#print(globals()['x']) #KeyError 
# End  of  the  function
f1()

'''


#20.Find outputs 

'''
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c) #1. 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c']) #2. 10 20 30 
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c) #3. 100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()

'''

#21.global  keyword  demo  program

'''
def    f1():
	x = 20
	print(x) #2. 20 
def   f2():
	global  x #x(11)
	x = 30
	print(x) #4.30 
	x += 1 # x(31)
def   f3():
	global  y
	y = 40
	print(y) #6. 40
	y += 1 #y(41)
def   f4():
	x = 50
	#global   x #Error no global variable if local x is there 
#  End  of  the  functions
x = 10
print(x) #1. 10
x += 1 #x(11)
f1()
print(x) #3. 11
f2()
print(x) #5. 31
x += 1 # x(32)
f3()
print(y) #7. 41
f4()
print(x) #8. 32

'''


#22.Find outputs 

'''
def  f1():
	global  a
	a = 20 #a(20) global 
	print(a) #2. 20 
	print(globals()['a']) #3. 20 
	a = 30 # a(30) global 
	
# End of the function
a = 10
print(a) #1. 10
f1()
print(a) #4. 30

'''


#23. Find  outputs

'''
def  f1():
	global  a
	#print(a) #Error a not initailized 
	a = 10 #a(10)
	print(globals()['a']) #1.10 
	a = 20 #a(20)
	print(a) #2. 20
	a = 30 #a(30)
def  f2():
	print(a) #3. 30
# End  of   f2   function
f1()
f2()
print(a) #4. 30

'''


#24.Find outputs

'''
def  f1():
	global   a
	a = 10 
	print(a) #1. 10
	a = 20 # a(20)
def  f2():
	global  a
	print(a) #2. 20
	a = 30 #a(30)
def  f3():
	print(a) #3. 30 
	globals()['a'] = 40 #a(40)
# End  of  the  function
f1()
f2()
f3()
print(a) #4. 40

'''

#25.Find outputs

'''
def  f1():
	global   a
	a = 10
	print(a) #1. 10 
	a = 20 #a(20)
def  f2():
	#print(a) #Error no local and global in one region 
	a = 30 # local a(30)
	print(a) # 2. 30 
def  f3():
	print(a) #3. 20
	globals()['a'] = 40 #global a(40)
# End  of  the  function
f1()
f2()
f3()
print(a) #4. 40

'''


#26.Find  outputs

'''
def  f1():
        a = 10 
        #global  a #Error  ambiguity
        print(a) #1. 10 
        global  b
        b = 20 #b(20)
# End  of  f1()  function
f1()
#print(a) #Error not defined a
print(b) #20

'''


#27.Find outputs

'''
def  f1():
        global  a
        print(a) #2. 11
        a += 1 #a(12)
def  f2():
        global  a
        print(a) #4. 13
        a += 1 #a(14)
# End  of  the  function
a = 10
print(a) #1. 10 
a += 1 #a(11)
f1()
print(a) #3. 12
a += 1 #a(13)
f2()
print(a) #5. 14

'''

#28.Find  outputs

'''

def   f1():
	a = 20
	print(a) #2. 20 
def  f2():
	print(a) #3.11
	#a += 1 #Error we can't modify without global function 
# End of the function
a = 10
print(a) #1. 10
f1()
a += 1 #a(11)
f2()
print(a) #4. 11

'''


#29.Find outputs

'''
def  f1():
	a = 20
	#global   a #Error already assigned locally 
	print(a) #2. 20 
	print(globals()['a']) #3. 11
	a = 30
	globals()['a'] = 40 #global a(40)
#  End  of  f1()   function
a = 10
print(a) #1. 10
a += 1 #a(11)
f1()
print(a) #4. 40

'''

#30.Find   outputs

'''
def   f1():
	#x = x + 5 #Error no local x
	pass
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5 # local x(15)
	print(x) #1. 15
# End of f2  function
x = 10
f1()
f2()
print(x) #2. 10

'''
