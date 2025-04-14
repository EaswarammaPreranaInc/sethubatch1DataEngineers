Q1 #  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)            
print(type(l))  
s = {x * x   for   x   in   range(5)}
print(s)          
print(type(s))
d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))
g = (x * x   for   x   in   range(5))
print(g)
print(type(g))

OP-
[0, 1, 4, 9, 16]
<class 'list'>
{0, 1, 4, 9, 16}
<class 'set'>
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>
<generator object <genexpr> at 0x00000285E432A5A0>
<class 'generator'>
#=====================================================
Q2 # Find  outputs (Home  work)
def  f1():
	return  10
	return  20    
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1())
print(f1())
print(f1())
print()
g = f2()
print(next(g))
print(next(g))
print(next(g))
#print(next(g))#error

OP-
10
10
10

10
20
30
