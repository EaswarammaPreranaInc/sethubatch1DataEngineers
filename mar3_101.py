'''for i in range(1,8):
	print(i)
	if i==8:
		break
	else:
		print("Sec")
	print("Hyd")
else:
	print("else suite")
print("Outside")
'''
'''
a=[10,20,30,40,50]
search=int(input("Enter an element\t"))
count=0
try:
	while count<=len(a):
		if search==a[count]:
			print(f"Element {search} is found at index {count}")
			break
		count+=1
except:
	print("Element not found")
'''
'''
a,b,c=25,10.8,'hyd'
a=30
print(a,b,c)
del a
print(a)
'''
'''
a=eval(input("Enter a list of inputs:\t"))
avg=0

if a[-1]!=-1:
	avg=sum(a)/len(a)
	print(avg)
else:
	avg=(sum(a)+1)/(len(a)-1)
	print(avg)
'''
'''
sum=0
count=0
while True:
	num=eval(input("Enter a number:\t"))
	if num==-1:
		break
	sum=sum+num
	count+=1
avg=sum/count
print(f"Average is {avg}")
'''
#print(a=10+10)

'''
#search using for loop
a=[10,20,30,40,50]
search=int(input("Enter a value"))
for i in range(len(a)):
	if search==a[i]:
		print(f"{search} is found at index {i}")
		break
else:
	print("Not found")
'''
