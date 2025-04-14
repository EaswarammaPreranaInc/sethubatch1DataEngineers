'''
def f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
f1()
f1('hyd')
f1([10,20],(30,40,50),{60,70,80,90})
tpl=(100,200,150)
f1(tpl)

output
()
<class 'tuple'>
0

('hyd',)
<class 'tuple'>
1

([10, 20], (30, 40, 50), {80, 90, 60, 70})
<class 'tuple'>
3

((100, 200, 150),)
<class 'tuple'>
1
'''
'''
def  avg(*a):
	for i in range(len(a)):
		x=sum(a)/len(a)
		return F'Avg is {x}'
print(avg(10,20,30))
print(avg(10.8,25,True))
print(avg(10.8,20.6,15.2,14.9,9.8))
print(avg())
print(avg(25))
print(avg(3+4j,5+6j))
#tpl=(10,20,15,18)   error due to int operand over tuple
#print(avg(tpl))
output
Avg is 20.0
Avg is 12.266666666666666
Avg is 14.26
None
Avg is 25.0
Avg is (4+5j)
'''
'''
def concat(*a):
	y=" ".join(a)
	return y
print(concat('sankar', 'dayal', 'sharma')) 
print(concat('Hyd','is','green','City'))
print(concat('Python', 'is ','a', 'Great','language')) 
print(concat()) 
print(concat('python')) 
print(concat(1,2,3))  #error due to int
output
sankar dayal sharma
Hyd is green City
Python is  a Great language

python
'''
'''
def f1(a=25, *b):
	print(F'a:{a} \t b:{b}') 
f1(10,20,30,40)
f1(50,60)
f1(70)
f1(a=80)
#f1(b=(10,20),a=40)
#f1(25, a=(10,20,30))
#f1(a=(10,20),40)
f1((50,60),50,60)
output
a:10     b:(20, 30, 40)
a:50     b:(60,)
a:70     b:()
a:80     b:()
a:(50, 60)       b:(50, 60)
'''
'''
def f1(*a):
	print(a)
	print(type(a))
	for x in a:
		print(x)
		print(type(x))
f1([10,20],{30,40},(50,60))
output
([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>
'''
'''
def disp(**a):
	print("res")
	print(type(a))
	print(a)
	print()
disp(rn=10,sn="rama")
disp(em=20,sn="rama",sal=10000.0)
disp(rn=10,sn="rama",bal=9000.0,g='m')
disp()
'''
'''
def f1(emn,em,sal):
	print(F'empn :{emn} \t em: {em} \t sal:{sal}')
def f2(**a):
	print(a)
f1(emn =25,em='sait', sal=1000.0)
#f1(empn=25,em='sita',salary=10000.0) error due to wrong keyword arg
f2(emn =25,em='sait', sal=1000.0)
f2(empn=25,em='sita',salary=10000.0)
output
empn :25         em: sait        sal:1000.0
{'emn': 25, 'em': 'sait', 'sal': 1000.0}
{'empn': 25, 'em': 'sita', 'salary': 10000.0}
'''































































































