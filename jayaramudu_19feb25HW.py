Ex -1
a={
    print('Hyd'), #pri'nt 'Hyd
    print('Sec'), #print 'Sec'
    print('Cyd') }#print 'Cyd'  ,print return None ,{None,None,None}
print(type(a)) # print class set
print(a)   # {None}
print(len(a)) #1

Ex-2 :
_=25
print(_)    # address of Object 25
print(type(_))  # class int
a,_,c=10,20,30 # multiple Objects is assigns to multiple references
print(a)  # 10
print(_)  # 20
print(c)  # 30
for _ in range(5):
    print(_,'Hello')  #  0 Hello
                      #  1 Hello
                      #  2 Hello
                      #  3 Hello
                      #  4 Hello


Ex-3 
a=25   # 25 Object is assign to reference a
print(id(a)) # address of Object 25
a=35           # 35 Object is assign to reference a
print(id(a))  # address of Object 35

Ex-4:
a=25.7             # 25.7 Object is assign to reference 'a'
print(id(a))      # print address of object 25
print(a)          # print Object value 25.7
a=35.6           # 35.6 Object is Reassign to reference 'a'
print(id(a))     # print address of object 35.6
print(a)        # print Object value 35.6
b=True          # True  bool Object is assign to reference 'b'
print(id(b))    # print address of object True
b=False        # False Object is Reassign to reference 'b'
print(id(b))    # print address of object False
c=None           # None Object is assign None  to reference 'c'
print(id(c))     # print address of object None
c=None             # Same Object points to reference 'c'
print(id(c))   #  # print same address of object None

Ex-5
a = 'Hyd'                 # 'Hyd' Object is assign to refe a
print(id(a))              # print object address
#a[1] = 'e'                # Error str is Immutable
a = 'Sec'                 # 'Sec' Object is Reassign to refe a
print(id(a))              # print object address
b = (10 , 20 , 15 , 18)
print(id(b))              # print object address of tuple
#b[2] = 19                 # Error because tuple is immutable
b = (30 , 40 , 35 , 32)  # new tuple object is created
print(id(b))               # print object address of tuple
c = range(5)          # range values form 0 to 4
print(id(c))          # print range object address
#c[3] = 10           # Error because  range is immutable
c = range(5)   # new range Object created
print(id(c))  # print new address of a range object

Ex-6: 
a=25 # reference a points to object 25
b=25 # reference b points to same object 25
print(a is b) #True
c='Hyd' # reference c points to object 'Hyd'
d='Hyd'  # reference d points to object 'Hyd'
print(c is d) #True
e=False # reference e points to object False
f=False # reference d points to object False
print(e is f) # True
g=range(10) # reference g points to  range object
h=range(10) # reference h points to new  range object
print(g is h) # False


Ex-7 :
a = [10 , 20 , 15 , 18] # reference a points to list object
b = [10 , 20 , 15 , 18] # reference b points to new list object
print(a  is  b)          # False
c =  {10 : 20, 30 : 40} # reference c points to dict object
d =  {10 : 20, 30 : 40} # reference d points to new dict object
print(c  is  d)         # False
e = (10 , 20 , 15 , 18)  # reference e points to tuple object
f = (10 , 20 , 15 , 18)  # reference f points to same tuple object
print(e  is  f)          # True
g = {10 , 20 , 15 , 18} # reference g points to set object
h = {10 , 20 , 15 , 18} # reference h points to new set object
print(g is h) # False

Ex-8:
print(25 * 3)            # 75
print(10.8 * 25.6)      #276.48
print(True * False) #0
print((3 + 4j) * (5 + 6j)) #-9+38j
print(3 + 4j * 5 + 6j)# 3+26j
print('25' * 3) #252525
print(3 * '25')#252525
print('Hyd' * 4)# HydHydHyd
print([10 , 20 , 15] * 2) # [10 , 20 , 15,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) # tuple repeated 3 times
#print([10 , 20 , 15] * 3.0) #Error because can't multiply set by float
#print({10 , 20 , 15} * 2) # Error because can't multiply set by int
#print({10 : 20 , 30 : 40} * 2)  # Error because can't multiply set by int
#print([10]*[20]) Error because can't multiply list by int

Ex-9: print(10 + 20)                       # 30
print(10.8 + 20.6)                   # 31.4
print(3 + 4j + 5 + 6j)              #8+10j
print(True + False)                  # 1
print('Hyder' + 'abad')                # 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')    # 'SankarDayalSarma'
print('10' + '20')
print([10 , 20 , 30] + [1 , 2 , 3])     # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #  (25 , 10.8 , 'Hyd',3 + 4j , True , None)
#print({10 , 20} + {30 , 40}) # Error because can't concat two sets
#print({10 : 'Hyd'} + {20 : 'Sec'})  # Error because can't concat two dict
#print(range(4) + range(5)) # error because can't concat two ranges ,range is  immutable
#print(10 + '20')         # Error because can't concat int and str
#print([10 , 20 , 30] + 5) # Error because can't concat list and int
#print([10 , 20 , 30] +(40,50,60)) Error because can't concat list is mutable and tuple is immutable
Ex-10 : 
#print(7/0) # error 7 division by 0
#print(7//0) # error 7 division by 0
#print(7 % 0) # error 7 division by 0

Ex-11 :
print(3 ** 4)   #  3 ^ 4 = 81
print(10 ** -2)
print(4 ** 3 ** 2)
print(3+4 *5 -  32 / 2 ** 3)

Ex-12 :
print('Rama'   >  'Rajesh')   #   True  becoz  'm' > 'j'
print('Rama'  <  'Sita')      # True
print('Hyd'  ==  'Hyd')       # True
print('Rama'  <=   'Ramana')  # True
print('Rama  Rao'  >=  'Rama') # True
print('Hyd'  != 'Sec')         # True
print('HYD'  <   'hyd')        #True

Ex-13 :
print(10 < 20 < 30)    #   True  becoz  both  are  satisfied
print(10 >= 20 < 30)   #  False  becoz  1st  cond  is  not  satisfied
print(10 < 20 > 30)    # False
print(1 < 2 < 3 < 4)   # True
print(1 < 2 > 3 > 1)  # False
print(4 >3>= 3  >  2) # True
