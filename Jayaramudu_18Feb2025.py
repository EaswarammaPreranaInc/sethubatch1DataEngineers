# Home Work 1
a={10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}
print(a)         #  print dict Object with Key value pair {10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}
print(type(a))   # class dict
print(a[10])     # print key(10) of  value 'Ramesh'
print(a[20])     # print key(20) of  value 'Kiran'
print(a[15])   # print key(15) of  value 'Kiran'
#print(a[19])     # Error there is no key 19 in dict
#print(a[0])      # Error dict is not indexed
#print(a['Amar']) # Error We can not get key based on value
a[15]='Krishna'  # key 15 value is modified
del a[20]        # Remove the key:value pair in dict by key 20
a[25]='Vamsi'    #new Key pair appended to dict
print(a)         # print key : value pairs in dict object a ,a={10:'Ramesh',15:'Krishna',18:'Sita',25:'Vamsi'}
print(len(a))    # print how many key :value pairs present in dict  4
#print(a*2)       # Error because multiplication is not support in dict

Home Work 2 :
a={10:'Hyd',10:'Sec'}   #dict can not store duplicates keys only uniques key   # a={10:'Sec'}
print(a)                # {10:'Sec'}
print(len(a))
b={'R':'Red','G':'Green','B':'Blue','Y':'Yellow','G':'Gray','B':'Black'} #dict can not store duplicates keys only uniques key {'R':'Red','G':'Gray','B':'Black','Y':'Yellow',}
print(b)   #{'R':'Red','G':'Gray','B':'Black','Y':'Yellow',}
print(len(b)) # count how many key : value pairs are present in dict  4

Home work 3: 
a={True:'Yes',1:'No',1.0:'May be'}   # dict can not store  duplicate keys a={True:'May be'}
print(a)                             # {True:'May be'}
print(len(a))                        # 1


Home Work 4:
#a={[]:25} # Error because a key in a dictionary must be immutable
#b={():25}   # Error because key is not empty
#print(b) # Error
c={{}:25} # Error because a dictionary key must be immutable,but not Empty
d={'Ramesh':[9948250500,9848565090,9440250404]}
print(d) #print  {'Ramesh':[9948250500,9848565090,9440250404]}
print(len(d)) # 1
e={set():10.8}   # Error because a set is mutable and cannot be used as a dictionary key.

Home Work 5:
a={}             # Empty dict
print(type(a))  # print class type <class dict>
print(len(a))   # how many key:value pairs present in a dict
print(a)        # Empty dict {}
b=dict()         # Empty dict
print(type(b))   # print class type <class dict>
print(len(b))     # how many key:value pairs present in a dict
print(b)          # Empty dict {}

