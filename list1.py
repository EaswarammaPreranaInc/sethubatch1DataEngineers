a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)
print(*a)
print(type(a))
print(len(a))
print(a[2 : 5])
print(*a[2 : 5])
a[2] = 'Sec'
a . append('Sec')
a . remove('Hyd')
b =  10 , 20 , 30
print(b)
print(b * 2)
c = 40 , 50 , 60,
print(c)
print(type(c))

a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a * 4)
print(b * 4)
print(c * 4)
print(d * 4)

a = tuple('Hyd')
print(a)
print(type(a))
print(len(a))
b = [10 , 20 , 15 , 18]
print(tuple(b))
print(tuple(range(5)))
print(tuple(25))


a = ()
print(type(a))
print(a)
print(len(a))
b = tuple()
print(b)
print(len(b))


a = (10 , 20 , 30)
print(a)
print(id(a))
a = a * 2
print(a)
print(id(a))



a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)
print(type(a))
print(len(a))
print(a[2])
print(a[1 : 4])
a[2] = 'Sec'
print(a * 2)
print(a * a)




a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)
print(len(a))
print(type(a))



a = set('Rama rAo')
print(a)
print(len(a))
print(set([10 , 20 , 15 , 20]))
print(set((25 , 10.8 , 'Hyd' , 10.8)))
print(set(range(10 , 20 , 3)))
print(set(25))


Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   { }
d =   set()
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a)
print(b)
print(c)
print(d)


a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)
a . remove(25)
print(a)
a . append(100)
a . add(set())


