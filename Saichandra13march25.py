# clear() method  demo program
list = [10, 20, 15, 18]
print(list)   # [10, 20, 15, 18]
list.clear()
print(list)   # []



# reverse()  method  demo  program
a = [10, 20, 15, 18]
print(a)   # [10, 20, 15, 18]
a.reverse()
print(a)   # [18, 15, 20, 10]



#  sort()  method  demo  program
list = [10, 20, 15, 18, 5]
print(list)   # [10, 20, 15, 18, 5]
list.sort()
print(list)   # [5, 10, 15, 18, 20]
list.sort(reverse=True)
print(list)   # [20, 18, 15, 10, 5]



# Find  outputs (Home  work
a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama Rao']
print(a)   # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama Rao']
a.sort()
print(a)   # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama Rao', 'Sita', 'Vamsi']
a.sort(reverse=True)
print(a)   # ['Vamsi', 'Sita', 'Rama Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']



# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
#a.sort()   # Error due to not support characters and string numbers 



# count() method demo program
a = [10, 20, 15, 18, 15, 12, 14, 15, 19]
print(a.count(15))  # 3
print(a.count(25))  # 0
print(len(a))  # 9

Sa




# Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]
Hint:  Use  count()  and  append()  methods

a = eval(input("Enter a list:"))
L = []
for i in a:
	if a.count(i) == 1:
		L.append(i)
print(L)



# index() method demo program
a = (10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25)
#    0   1   2   3   4   5   6   7   8   9   10
try:
	i = a.index(15)
	while True:
		print(i)   # 2, 5, 8
		i = a.index(15, i + 1)
except:
	print(F'15 is found {a.count(15)} times')   # 15 is found 3 times




# Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise
First  list :  [2,2,5]
Second  list :  [2,2,3,4,5]
What  is  the  output ?  ---> True  becoz   elements  2,2,5    are   in  [2,2,3,4,5]

a=eval(input("First  list: "))
b=eval(input("Second list: "))

#a=[2,2,5]
#b=[2,2,3,4,5]

c=b.copy()

for i in c:
    if i not in a or b.count(i)>a.count(i):
        b.remove(i)
        
print(b)

if(len(a)!=len(b)):
    print(False)

else:
    for i in a:
        if a.index(i)!=b.index(i):
            print(False)
            break 
        
    else:
        print(True)



# 10.copy()  method  demo program
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) #[10 , 20 , 15 , 18]
print(a  is  b) #False
print(a  ==  b) #True
c = a[:] 
print(c) #[10 , 20 , 15 , 18]
print(a  is  c)#False
print(a  ==  c)#True
d = a
print(d) #[10 , 20 , 15 , 18]
print(a  is  d) #True
print(a  ==  d) #True



# Write  a  program  to  determine  all  the  list  elements  are  identical  or  not
Enter  any  list  :  [10,10,20,10]
List   elements  are  not  identical
Enter  any  list  :  [25,25,25.0,25]
All  the  list  elements  are  identical

a = eval(input("Enter any list:"))
if (a.count(a[0]!=len(a))):
    print("List elements are not identical")
else:
    print("All the list elements are identical")



#.Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list
Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
Hint: Use  remove()  method

a = eval(input("Enter any list:")
x = eval(input("element need to be removed:")
b = a.copy()
for i in b:
	if i == x:
		a.remove(i)
print(a)



# Write  a  program  to  determine  mode
1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list
Enter  List : [10,20,15,18,10,20,15,10,20,19,10]
Mode : 10

a = eval(input("Enter list:"))
A = []
for i in a:
	if i not in A:
		A.append(i)
F = []
for i in A:
	F.append(a.count(i))
M = max(F)
for i in range(len(F)):
	if(F(i) == M):
		print("Mode:", A[i])








