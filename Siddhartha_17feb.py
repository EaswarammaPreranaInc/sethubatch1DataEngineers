a = [10 , 20 , 15 , 18 , 12 , 15 , 19 , 25 , 15 , 14 , 12]
while 15 in a:
	a.remove(15)	
print(a)


a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)            #tuple object
print(*a)           #tuple object elements
print(type(a))      #class tuple
print(len(a))       #6 or 8
print(a[2 : 5])     #2 to 4
print(*a[2 : 5])    #unpack elements 2 to 4
#a[2] = 'Sec'
#a . append('Sec')   #Error
#a . remove('Hyd')   #Error
b =  10 , 20 , 30
print(b)            #object b
print(b * 2)        #it prints twice in one tuple
c = 40 , 50 , 60, 
print(c)            #object c
print(type(c))      #class <tuple>


a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))     #class <int>
print(type(b))     #class <tuple>
print(type(c))     #class <int>
print(type(d))     #class <tuple>
print(a * 4)       #100 ---->multiplication
print(b * 4)       #(25,25,25,25)---->repeatation
print(c*4)       #100
print(d*4)       #(25,25,25,25)


a = tuple('Hyd')
print(a)            #('H','y','d')
print(type(a))      #class tuple
print(len(a))       #3
b = [10 , 20 , 15 , 18]
print(tuple(b))          #(10,20,15,18)
print(tuple(range(5)))   #(0,1,2,3,4)
#print(tuple(25))         #Error

a = ()
print(type(a))       #class tuple
print(a)             #()
print(len(a))        #0
b = tuple()         
print(b)             #()
print(len(b))        #0

# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)            #object tuple
print(id(a))        #ramdom tuple
a = a * 2
print(a)            #(10,20,30,10,20,30)---->repeatation
print(id(a))        #ramdom id 1000

a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)            #object set
print(type(a))      #class set
print(len(a))       #6
#print(a[2])         #error
#print(a[1 : 4])     #error
#a[2] = 'Sec'        #error
#print(a*2)       #error
#print(a*a)       #error


a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)              #object set
print(len(a))         #8
print(type(a))        #class <set>


a = set('Rama rAo')
print(a)          #{'R','a','m','a','','r','A','o'}
print(len(a))      #7
print(set([10 , 20 , 15 , 20]))      #{10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))  #{25,10.8,'Hyd'}
print(set(range(10 , 20 , 3)))          #{10,13,16,19}
#print(set(25))                          #Error



a =   [ ]
b =   ( )
c =   { }
d =   set()
print(type(a))    #class <list>
print(type(b))    #class <tuple>
print(type(c))    #class <dict>
print(type(d))    #class <set>
print(a)          #[]
print(b)          #()
print(c)          #{}
print(d)          #set()


a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)        #{25,10.8,'Hyd',True,None}
a . remove(25)
print(a)        #{None, True, 10.8, 'Hyd'}
#a.append(100)
#a.add(set())


a = {25 , True , 'Hyd' , 10.8}
print(a) #object set
for x in a:
	print(x)




