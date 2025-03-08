a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)             #object dict
print(type(a))       #class <dict>
print(a[10])         # 'Ramesh'
print(a[20])         # 20 value of 'Kiran'
print(a[15])         # 15 value of 'Amar'
print(a[18])         # 18 value of 'Sita'
#print(a[19])         #Error
#print(a[0])          #Error
#print(a['Amar'])     #Error
a[15] = 'Krishna'    #updated to 15 value of Krishna
del   a[20]          #delete the 20 value kiran
a[25] = 'Vamsi'
print(a)             #insert 25 value Vamsi
print(len(a))        #4
#print(a*2)         #error

a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)             #{10:'Sec'}
print(len(a))        #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)             #{'R':'Red','G':'Gray','B':'Black','Y':'Yellow'}
print(len(b))        #4 


a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)          #{True:'May be'}
print(len(a))     #1

#a = { [ ] : 25}     #error
b = { ( ) : 25}     
print(b)            #object b
#c = { { } : 25}     #error   
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)            #object d
print(len(d))       #1

a = {}
print(type(a))    #class <dict>
print(len(a))     #0
print(a)          #{}
b = dict()        
print(type(b))    #class <dict>
print(len(b))     #0
print(b)          #{}
