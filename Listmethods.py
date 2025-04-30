#append Method
l=[10,20,15,18]
print(l)
l.append(19)
print(l)
#using for and range keywords
l=[]
for x in range(0,60,10):
    l.append(x)
print(l)
l=[10,25,True]
l.append("Hyd")
for x in range(len(l[3])):
    print(l[3][x])
a=[10,20,30,40]
b=[50,60,70]
a.insert(2,b)
print(a)
for x in range(len(a[2])):
    print(a[2][x])
    