#1
'''
a={10,20,30,40}
b=[30,40,50,60]
print(a.union(b)) #{40, 10, 50, 20, 60, 30}
print(a|b)           # error
print(b.union(a))  # list can't have unioin
print(a+b)           #can't add
'''
#2
'''
a={10,20,15,18} #output
print(a)            #{10,20,15,18}
a.clear()           #{}
print(a)           #set()
print(len(a))    #0
'''
#3
'''
a={25,10.8,'HYD',True}
print(a)                  #{25,10.8,'HYD',True}
a.discard('HYD')       #{25,10.8,True}
print(a)                   #{25,10.8,True}
a.discard('sec')         # doesnt give error
print(a)                   #{25,10.8,True}
a.remove('sec')         # gives error by not defining 'sec'
'''
#4
'''
a={25,10.8,'HYD',True}
print(a)                     #{25,10.8,'HYD',True}
a.remove('HYD')         #{25,10.8,True}
print(a)                     #{25,10.8,True}
a.remove('sec')           #error due to 'sec'
'''
#5
'''
a={10,20,15,18}
print(a)           #{10,20,15,18}
b=a.copy()        #{10,20,15,18}
print(b)           #{10,20,15,18}
print(a is b)     #False
print(a == b)    #True
c=a                  #{10,20,15,18}
print(a is c)      #True
'''
#6
'''
a=set()
a.update('Rama Rao')  #{R,a,m,o,''}
print(a)                      #{R,a,m,o,' '}
print(len(a))                #5
a.update(3+4j,10.8,True) #error due to diff class 
'''
#7
'''
a=[10,20,30]
b={30,40,50}
c=(50,60,70)
s=set()                      #  {}
s.update(a,b,c)           #{10,20,30,40,50,60,70}
print(s)                     #{10,20,30,40,50,60,70}
print(len(s))              # 7
s.add(a,b,c)               # error due to excess arguments
'''
#8
'''
tpl=(10,20,15,18,10,20)
s=set()
s.update(tpl)   #{10,20,15,18}
print(len(s))    #4
print(s)            #{10,20,15,18}
s.update(25)    # error due to update(non-seq)
'''
#9
'''
s=set()
tpl=(10,20,15,18)
s.add(tpl)       #{(10, 20, 15, 18)}
print(s)          #{(10, 20, 15, 18)}
print(len(s))    #1
'''
#10
'''
a={25,10.8,'hyd',True}
tpl=(10,20,30)
print(a)       #{25,10.8,'hyd',True}
print(id(a))  #add1
a.add(tpl)     #{25,10.8,'hyd',True,(10,20,30)}
a.add('sec')   #{25,10.8,'hyd',True,(10,20,30),'sec'}
print(a)        #{25,10.8,'hyd',True,(10,20,30),'sec'}     
print(id(a))   #add2
print(len(a))  #6
a.add([100,200,300]) # error due to list obj
a.add(set())               # error due to set obj
a.add({})                    # error due to dict obj
'''
#11
'''
a=set()
a.add(True)  #{True}
a.add(25)     #{True,25}
a.add(10.8)   #{True,25,10.8}
a.add(1)        #{True25,10.8,1}
a.add('hyd')   #{True25,10.8,1,'hyd'}
a.add(25)    #{True25,10.8,1,'hyd'}
a.add(None) #{True25,10.8,1,'hyd',None}
a.add('hyd')  #{True25,10.8,1,'hyd',None}
a.add(1.0)     #{True25,10.8,1,'hyd',None}
print(a)        #{True25,10.8,1,'hyd',None}
#a.add(10,20,30) #error
#a.add([10,20,30]) #error
'''
#12
'''
a=range(100,151,10) #100,110,120,130,140,150
b=set(a)                  #{100,110,120,130,140,150}
print(b)                   #{100,110,120,130,140,150}
c=[10,20,15,18,10,50,20,12,18] 
d=set(c)    #{10,20,15,18,50,12}
print(d)    #{10,20,15,18,50,12}
e=set('Rama rAo')       #{'R','a','m','o',""}
print(e)                     #{'R','a','m','o',""}
#print(set(25))            #error
print(set())                #set()
'''
#13
'''
s={20,10,20,10}
print(s) #{10,20}
x,y=s       #x=10,y=20
print(x)    #x=10
print(y)    #y=20
'''
#14
'''
s = {'Hyd',  25,  True,  10.8 }
print(s)        #{'Hyd', 25, 10.8, True}
a , *b , c = s
print(a)      #Hyd
print(b)    # [25, 10.8]
print(c)      #True
'''