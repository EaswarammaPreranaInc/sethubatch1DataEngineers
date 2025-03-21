a  =  {10,20,30,40}
b  =  {30,40,50,60}
c =   a.symmetric_difference(b)
print(a)
print(b) 
print(c) # we get result of a elements and b elements difference and 
print(type(c))
d = a-b 
print(d)
print(type(c))
print(c is d)
print(c == d)
'output'
{40, 10, 20, 30}
{40, 50, 60, 30}
{10, 50, 20, 60}   
<class 'set'>      
{10, 20}
<class 'set'>      
False
False