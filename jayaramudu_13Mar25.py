# Ex-1:
# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10 , 20 , 15 , 18]
list . clear() # Remove all elements from the list
print(list) # empty list []
print()

#Ex-2
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)         # [10 , 20 , 15 , 18]
a . reverse() # reverse elements in a list
print(a) # [18,15,20,10]
print()

#Ex-3:-
#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)        # [10 , 20 , 15 , 18 , 5]
list . sort()   # sort elements ascending order [5,10,15,18,20]
print(list)     # [5,10,15,18,20]
list . sort(reverse = True) # reverse elements in sorted list [5,10,15,18,20]
print(list) # [20,18,15,10,5]

print()

#Ex-4:-
# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)  # ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama']
a . sort() # sort elements ascending order ['Amar','Kiran', 'Rajesh','Rama','Rama','Sita','Vamsi']
print(a)    # ['Amar','Kiran', 'Rajesh','Rama','Rama','Sita','Vamsi']
a . sort(reverse =True) # reverse elements in sorted list ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

#Ex-5:
# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
#a.sort() # Can not compare int and  str

#Ex-6:
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3
print(a . count(25)) # 0
print(len(a)) # 9


#Ex-7
'''
Gift
Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append() methods
'''

a = [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
b = []
for x in a:
    if a.count(x) == 1:
        b.append(x)

print(b)

#Ex-8
# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2     3    4     5     6    7     8    9    10
try:
	i = a . index(15) # 2
	while  True:
		print(i)  # 2,5,8
		i = a . index(15 , i + 1) # 3 5 ,6,8
except:
	print(F'15  is  found  {a . count(15)}  times ')




