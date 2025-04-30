# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)
#f1(y = 20)
#f1(x = 30)


# Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d):
	#pass
def   f2(b , d , a = 10 , c = 20):
	pass

#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)
f1()
f1(a = 30)


# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))
print(add(100 , 200 , 300))
print(add(100 , 200 , 300 , 400))
print(add(b = 100 , a = 200))
print(add(100 , 200 , d = 300))
print(add(d = 100 , a = 200 , b = 300))
#print(add(c = 100 , d = 200 , 300 , 400))
#print(add(100 , 200 , c = 300 , x = 400))
#print(add())

# Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))
print(f1())
print(f2(20))
#print(f2())

# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)
disp('$')
disp()
disp(n = 5)
disp(5)
disp(n = 7 , ch = '%')
disp(7 , '@')
disp(7 , n = 6)
#disp(ch = '!' ,  5)

 # Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))
print(power(5))
print(power(b = 3 , a = 4.5))
print(power(3 + 4j))
print(power(True))
#def   power(b = 2 , a):
 	 #pass


# Find outputs  (Home  work)
def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40))
print(add(50 , 60 , 70))
print(add(80 , 90))
print(add(100))
print(add())


# Find outputs  (Home  work)
#def  disp(a , b):
        #print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)
#disp(40 , 50 , 60 , 70)
disp(80 , 90)

 # Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))
print(add())
print(add(a = 50))
print(add(b = 60 , a = 70))
#print(add(80 , 90))


#outputs
3rd  function :  10
20
10
30
330
620
1000
330
610
610
10
25
20
------
$$$$
****
*****
20
%%%%%%%
@@@@@@@
42
64
25
91.125
(-7+24j)
1
4-argument  function
100
4-argument  function
184
4-argument  function
177
4-argument  function
109
4-argument  function
10
3-argument  function  :   10 20 30
3-argument  function  :   80 90 25
70
30
70
130
