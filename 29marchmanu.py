'''
#1) Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # [0, 1, 4, 9, 16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) # {0, 1, 4, 9, 16}
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # <generator object <genexpr> at 0x0000019827C5A5A0>
print(type(g)) # <class 'generator'>

#2)Find  outputs (Home  work)
'''
def  f1():
	return  10
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1()) # 10
print(f1()) # 10
print(f1()) # 10
print() # empty print
g = f2() # generator points to f2 ()
print(next(g)) # 10
print(next(g)) # 20
print(next(g)) # 30
print(next(g)) # This is outside the function we get Stopiteration Error









