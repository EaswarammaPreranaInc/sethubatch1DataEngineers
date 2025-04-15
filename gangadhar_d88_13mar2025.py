# Write a program to merge two sorted list 
a=eval(input("Enter a first sorted list : "))
b=eval(input("Enter a second sorted list : "))
a.sort()
b.sort
new_list=[]
n=len(a)
i=0
j=0
m=len(b)
while i<n and j<m:
    if a[i]<=b[j]:
        new_list.append(a[i])
        i+=1
    else:
        new_list.append(b[j])
        j+=1
while i<len(a):
    new_list.append(a[i])
    i+=1
while j<len(b):
    new_list.append(a[j])
    j+=1

print(new_list)


a=eval(input("Enter list : "))
b=[]
for x in a:
    firstchar=x[0]
    if firstchar not in b:
        b.append(firstchar)
c=[]
for ch in b:
    d=[]
    for i in a:
        if i.startswith(ch):
            d.append(i)
    c.append(d)
print(c)


# write a program to delete all occurence of X element from the list
x=eval(input("enter alist :"))
new=[]

for a in x:
    
    if x.count(a)==1:
        new.append(a)
print(new)


# Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

arr=eval(input("Enter a list :"))

for x in arr:
    count=arr.count(x)

if len(arr)==count:
    print("Enterd list are identical ")
else:
    print("Enterd list are not identical ")


# Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

arr=eval(input("Enter a list :"))
y=eval(input("Enter a element to delete :"))

while y in arr:
    arr.remove(y)
print(arr)


# Write to  program to find mode of the list

arr=eval(input("Enter a list :"))
count=0
b=set(arr)
for x in b:
    freq=arr.count(x)
    if freq>count:
        count=freq
        mode=x
print("Mode :",mode)

#Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
arr=eval(input("Enter a list :"))
arr2=eval(input("Enter a list :"))
final=[]
for i in range(len(arr)):
    for j in range(len(arr2)):
        sum=arr[i]+arr2[j]
        final.append(sum)
        

print(final)


#Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  with comprehension

arr=eval(input("Enter a list :"))
arr2=eval(input("Enter a list :"))
sum=[arr[x]+arr2[y] for x in range(len(arr)) for y in range(len(arr2))]
print(sum)


#Write a program to print a neated  list in matrix style
arr=eval(input("Enter a list :"))
for x in arr:
    for y in x:
      print(y,end=" ")
    
    print()


#write a program to create a list with cubes of 2,4,6,8,10 with list comprehension
cubes=[ i**3 for i in [2,4,6,8,10]]
print(cubes)
print(cubes :=[ i**3 for i in [2,4,6,8,10]])

# Write a program a extract first character for each string in capital letters in list of string without comprehension 
arr=eval(input("enter a list :"))
list=[]
for i in range(len(arr)):
    s=arr[i][0].upper()
    list.append(s)
print(list)

# Write a program a extract first character for each string in capital letters in list of string with comprehension 
arr=eval(input("enter a list :"))
print(list:=[arr[i][0].upper() for i in range(len(arr))])

# Write a program to add 2 lists of unequal length without comprehsion

arr=eval(input("enter a list :"))
arr1=eval(input("enter a list :"))
i=j=0
sum=[]
while i<len(arr) and j<len(arr1):
    com=arr[i]+arr1[j]
    sum.append(com)
    i+=1
    j+=1
sum.extend(arr[i:])
sum.extend(arr1[j:])
print(sum)

# Write a program to add 2 lists of unequal length without comprehsion
arr=eval(input("enter a list :"))
arr1=eval(input("enter a list :"))
n=len(arr)
m=len(arr1)
min_len=min(n,m)
sum=[(arr[i]+arr1[i]) for i in range(min_len) ]+ arr[min_len:] + arr1[min_len:]
print(sum)


# Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
x=int(input("Enter number of list :"))
y=int(input("enter number :"))
list=[]
for i in range(x):
    temp=[]
    for j in range(y):

        temp.append(j*0)
    list.append(temp)
print(list)

# Write   a  program  to  initialize  a  nested  list  with  zeroes  with  comprehension
x=int(input("Enter number of list :"))
y=int(input("enter number :"))
list=[[j*0 for j in range(y)]  for i in range(x) ]
print(list)


# Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
x=eval(input("Enter number of list :"))
y=eval(input("enter number :"))
output=[]
for i in x:
    for j in y:
        if i not in y:
            output.append(i)
            break
print(output)


# Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   with  comprehension

x=eval(input("Enter number of list :"))
y=eval(input("enter number :"))
list=[i for i in x if i not in y ]
print(list)


#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
list=[i for i in range(1,20) if i%2==0]
print(list)

#  Write   a  program  to  print  square of number which is divisible by 2  between  1  and  20  with  comprehension
list=[i**2 for i in range(1,20) if i%2==0]
print(list)


#Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
x=input("Enter number of list :")
y=input("enter number :")
list=[]
for i in range(len(x)):
    for j in range(len(y)):
        list.append(x[i]+y[j])
print(list)


#Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
x=input("Enter number of list :")
y=input("enter number :")
list=[x[i]+y[j] for i in range(len(x)) for j in range(len(y))]
print(list)
