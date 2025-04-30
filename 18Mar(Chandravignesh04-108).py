'''def  f1():
	print('1st function') # 2nd output
	return 25
	print('Hello')
print('begin')  # 1st output
x=f1()
print(x)   #none
print('end') # 3rd output
'''

'''def  f1():
	print('hyd')
	print('sec')
	print('cyb')
print('begin')  # 1st output
x=f1()
print(x)#none
print(type(x))
print('end')
output
begin
hyd
sec
cyb
None
<class 'NoneType'>
end
'''

'''
a=[10,20,15,5,12]
print(sorted(reverse=True)) #error only 1 arg should be given
print(sorted(a,rev=True))     # error no rev found
print(25,10.8,'hyd',separator='\t') #error due to no rev functin
print(25,10.8,'hyd',endofline='\t') # error due invalid endofline
print(25,sep="\t",10.8,end="\t",'hyd') #error in place pos and key arg
'''

'''
def  f1():
	print("no-argument function")
f1()
def  f1(x):
	print("one-argument function",x)
x,y,z=1,2,3
f1(x)
def  f1(x,y):
	print("two-argument function",x,y)
f1(x,y)
def  f1(x,y,z):
	print("three-argument function",x,y,z)
f1(x,y,z)
'''

'''
def f1():
	return 10,20,30
x=f1()
print(x)
print(type(x))
a,b,c=f1()
print(a)
print(b)
print(c)
print('for loop')
for k in f1():
	print(k)
'''