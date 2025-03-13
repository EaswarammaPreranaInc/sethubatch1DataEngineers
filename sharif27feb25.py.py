#prog-1-Write  a  program  to  determine  area  and  perimeter  of  rectangle
'''=int(input("enter lenght of rectanglr:"))
b=int(input("enter breadth of rectanglr:"))
area=l*b
perimeter=2*(l+b)
print(F'area:{area:.2f}')
print(F'perimeter:{perimeter:.2f}')

output--
enter lenght of rectanglr:4
enter breadth of rectanglr:5
area:20.00
perimeter:18.00'''


#prog-2-Write  a  program  to  determine  volume  of  a  sphere
'''import math 
r=eval(input("enter radius:"))
volume=4/3*math.pi*r**3
print(F'volume: {volume:.2f}')

output--
enter radius:3.5
volume: 179.59'''

#prog-3-Write  a  program  to  determine  simple  interest  and  compound  interest
'''p=eval(input("enter principle intrest:"))
t=eval(input("enter time:"))
r=eval(input("enter rate of intrest:"))
si=p*t*r/100
ci=p*(1+r/100)**t-p
print(F'si: {si:}')
print(F'ci: {ci:.2f}')

output--
enter principle intrest:10000
enter time:3
enter rate of intrest:7.5
si: 2250.0
ci: 2422.97'''

#prog-4-Write  a  program  to  swap  values  of  two  objects  using  3rd   object
'''x=int(input("enter first input:"))
y=int(input("enter second input:"))
print(F'before swapping: x={x:} y={y:}')
temp=x
x=y
y=temp
print(F'after swapping: x={x:} y={y:}')

output--
enter first input:10
enter second input:25
before swapping: x=10 y=25
after swapping: x=25 y=10'''


#prog-5-Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
'''x=int(input("enter first input:")) #x=-200
y=int(input("enter second input:"))#y=100
print(F'before swapping: x={x:} y={y:}')
x=x+y  #x=-200+100-->-100

y=x-y  #y-->-100-100-->-200

x=x-y #x-->-100-(-200)-->100

print(F'after swapping : x={x:} y={y:}')'''

#outputs--
'''enter first input:-200
enter second input:100
before swapping: x=-200 y=100
after swapping : x=100 y=-200'''


#prog-6-Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
'''x=int(input("enter first input:")) #x=25
y=int(input("enter second input:"))#y=10
print(F'before swapping: x={x:} y={y:}')

x=x*y #x=25*10-->250

y=x/y #y=250/10-->25

x=x/y #-->x=250/25-->10


print(F'after swapping : x={x:} y={y:}')

outputs--
enter first input:25
enter second input:10
before swapping: x=25 y=10
after swapping : x=10.0 y=25.0'''

#prog-7-Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
'''a=eval(input("enter first complex number:"))
b=eval(input("enter second complex number:"))
sum=a+b
sub=a-b
mul=a*b
div=a/b
print(sum)
print(sub)
print(mul)
print(div)

outputs--
enter first complex number:3+4j
enter second complex number:5+6j
(8+10j)
(-2-2j)
(-9+38j)
(0.6393442622950819+0.03278688524590165j)'''

#prog-8-Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
#Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
'''import math
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(max(a,b))
print(min(a,b))
print(a**b)
print(math.sqrt(a))
print(math.gcd(a))
print(math.factorial(10))

outputs--
enter first number:10
enter second number:7
17
3
70
1.4285714285714286
10
7
10000000
3.1622776601683795
10
3628800'''



#prog-9-Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
'''a=int(input("enter int value:"))
b=eval(input("enter str value:"))
print(F'before swapping: a={a:} b={b:}')
a,b=b,a
print(F'after swapping: a={a:} b={b:} ')'''

#prog-10-Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
'''a=eval(input("enter first value:"))
b=eval(input("enter second value:"))

print(a if a>b else b)


enter first value:10
enter second value:20
second is the largest value: 20

enter first value:10.2
enter second value:20.3
second is the largest value: 20.3

enter first value:'rama'
enter second value:'rajesh'
first is the largest value: rama

enter first value:[10,20,30]
enter second value:[10,20,35,45]
second is the largest value: [10, 20, 35, 45]'''

#prog-11-Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

'''a=eval(input("enter first value:"))
b=eval(input("enter second value:"))
c=eval(input("enter third value:"))
print(a if a>b else bif b>c else c)
	  
		 
enter first value:10
enter second value:20
enter third value:5
second is the largest value: 20

enter first value:10.2
enter second value:20.3
enter third value:5.6
second is the largest value: 20.3

enter first value:'rama'
enter second value:'rajesh'
enter third value:'rafi'
first is the largest value: rama'''

'''a=eval(input("enter first value:"))
b=eval(input("enter second value:"))
print( '>' if a>b else '<')

enter first value:10
enter second value:20
<

enter first value:20
enter second value:10
>'''
#prog-12-Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
'''a=eval(input("enter first value:"))

print('1' if a>0 else '-1' if a<0 else 0)

enter first value:10
1

enter first value:-98
-1
enter first value:0
0'''

#prog-13-Write  a  program  to  test  input  is  even  number  or  odd  number

a=int(input("enter a value:"))
print('even number'if a%2==0  else 'odd number')

enter a value:24
even number  

enter a value:23
odd number'''



