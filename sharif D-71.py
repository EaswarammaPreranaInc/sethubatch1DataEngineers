'''#Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator
a=eval(input("enter any list:"))
b=eval(input("enter the element to be searched:"))
c=0
for i in range (len(a)):
	if a[i]==b:
		c+=1
		print('found at index:',i)
		continue
print("found times",c)

output:
enter any list:[1,2,3,1,2,1,1,5,6,1]
enter the element to be searched:1
found at index: 0
found at index: 3
found at index: 5
found at index: 6
found at index: 9
found times 5 '''

#Modify  following   program  with  walrus  operator
#Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator
'''try:
	sum=ctr=0
	while(x := eval(input('enter a input(-1 to stop):')))!=-1:
		sum +=x
		ctr +=1
	print("avg:",sum/ctr)
except:
	print("enter at least one input")
output:
enter a input(-1 to stop):10
enter a input(-1 to stop):2
enter a input(-1 to stop):32
enter a input(-1 to stop):-1
avg: 14.666666666666666'''

'''#Write  a  program  to  determine  largest  command  line  input
from sys import argv
b=argv
c=[]
for i in range(1,len(b)):
	c.append(eval(b[i]))
print(c)
print(max(c))

output:
C:\Users\khaja>py 5march25.py 10 20 30
[10, 20, 30]
30'''

#Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number
from sys import argv
b=argv
c=[]
for i in range(1,len(b)):
	 c.append(eval(b[i])
for i in c:
	 if c[i]%2==0:
		  print("even number")
	 else:
		 print("odd number")

output:
C:\Users\khaja

#Write  a  program  to  determine  average  of  command  line  inputs
from sys import argv
b=argv
c=[]
for i in range(1,len(b)):
	 c.append(eval(b[i]))

print("avg:",sum(c)/2)
print(len(c))

output:
C:\Users\khaja>py argv1.py 12 2 3 4
avg: 10.5
4

#Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order
from sys import argv
b=argv
c=[]
for i in range(1,len(b)):
	 c.append(eval(b[i]))
print(sorted(c))
print(sorted (c)[::-1])

output:
C:\Users\khaja>py argv2.py 4 5 2 9 3 6
[2, 3, 4, 5, 6, 9]
[9, 6, 5, 4, 3, 2]













