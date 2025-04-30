*18 Feb 2025 HW*

#Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)        # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))  #<class 'dict'>
print(type(a))  # <class 'dict'>
print(a[10])    # Ramesh
print(a[20])    #Kiran
print(a[15])    #Amar
print(a[18])    #Sita
#print(a[19])    #error
#print(a[0])     #error
#print(a['Amar'])   #error
a[15] = 'Krishna'  #replace amar with Krishna
del   a[20]       #delete a[20] 
a[25] = 'Vamsi'   #new key value pair is created
print(a[20])    # Kiran 
print(a[15])    # Amar
print(a[18])    # Sita
#print(a[19])    #error because key 19 is not there in the given dictionary 
#print(a[0])     #error because key 10 is not there in the given dictionary
#print(a['Amar'])   #error because key must be immutable and string is mutable
a[15] = 'Krishna'  # value of key 15 is changed from amar to Krishna
del   a[20]       # delete the key 20
a[25] = 'Vamsi'   # new key value pair is created , key is 25 and value is 'Vamsi'
print(a)           #{10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita' , 25  : 'Vamsi'}
print(len(a))     #4
#print(a * 2)     #error
print(len(a))     #4 because of 4 unique keys
#print(a * 2)     #error because dictionary do not support repetation that will create duplicate keys which is invalid




# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}              
print(a) #     {10 : 'Sec'}
print(len(a))  #1
a = {10 : 'Hyd' , 10 : 'Sec'}       #dictionay with one key value pair. value hyd is replaced with sec for key 10          
print(a)                            #{10 : 'Sec'} 
print(len(a))                       #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)    #{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))  #4
print(b)         #{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}  Keys G and B  has two values, for G- Green is replaced with Grey and for B- Blue is replaced with Black.
print(len(b))    #4 because of 4 unique keys.


#  Gift 
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}   
print(a)   # {True :  'May  be'} 
print(len(a))   #1
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}    #True,1,1.0 are all same 
print(a)   # {True :  'May  be'}  - values 1 and 1.0 are replaced with May be because True,1,1.0 are same
print(len(a))   #1 because 1 unique key.


# Find  outputs
#a = { [ ] : 25} #invalis due to list is mutable in key     
#a = { [ ] : 25}   #invalid due to list is mutable. key must be immutable in Dictionary    
b = { ( ) : 25}
print(b)        #{ ( ) : 25}
print(b)           #{ ( ) : 25}  valid because tuple is immutable 
#c = { { } : 25}   #invalid because set is mutable 
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)      #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))  #1
#e = {set() : 10.8}   #invalid
print(d)           #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))      #1 because of 1 unique key 
#e = {set() : 10.8}   #invalid because set is mutable. key must be immutable.

''' 
 
# Find  outputs
a = {}
print(type(a))     #<class 'dict'>
print(len(a))   #0
print(a)   #{}
print(type(a))      #prints type of the class i.e. <class 'dict'>
print(len(a))       #0 because it is an empty dictionary
print(a)            #{}
b = dict()
print(type(b))  #class'dict'>
print(len(b))  #0
print(b)     #{}
print(type(b))      # prints type of the class i.e. <class'dict'>
print(len(b))       #0 because it is an empty dictionary
print(b)            #{} - prints empty dictionary
