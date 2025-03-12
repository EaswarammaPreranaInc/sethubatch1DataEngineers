for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')

	for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

if ():
	print('Hyd')
	continue
	print('Sec')


	for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

a=[25,10.8,'Hyd',True]
for x in range(len(a)):
	print(a.index(x),a)



	rows = eval(input('Enter  list  of  elements : '))
	rows=5
	for i in range(rows,0,-1):
		print(''*(-i)+'*'*(2*i-1))


a = eval(input('Enter  list  of  elements : '))
a=[10.8,25,'Hyd',True]
for i in range(len(a)):
	print((-a)+(2*a-1))



a= [10 , 20 , 15 , 18]
b= [30 , 40 , 35 , 12]
c= [a[i] + b[i] for i in range(len(a))]
print(c)


a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range(len(a)):
	print(a.index,a)


a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for x in a:
	print(a.index(x),a[x-1])

	for x in range(1,40):
		if x % 2==0:
			print(x)


for x in range(1,40):
		if x % 2!=0:
			print(x)
n=1,2,3,4,5,6,7,8,9,10
if n>0:
	print(n, end="")