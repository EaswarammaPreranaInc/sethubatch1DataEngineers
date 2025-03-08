#Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
#print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)
'''a=eval(input("enter any list:"))
x=eval(input("enter the element to be searched:"))
for i in range (len(a)):
	if a[i]==x:
		print('found at index:',i)
		break
else:
	print("not found")
output:
enter any list:[2,3,4,5,6]
enter the element to be searched:5
found at index: 3  '''

#Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
#(without  walrus  operator)
try:
	sum =  ctr = 0
	x = eval(input('Enter input  (-1  to  stop)  :  '))
	while  x != -1:
		sum += x
		ctr +=1
		x = eval(input('Enter input  (-1  to  stop)  :  '))
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not  be string')

output:
Enter input  (-1  to  stop)  :  10
Enter input  (-1  to  stop)  :  2
Enter input  (-1  to  stop)  :  -1
Average :   6.0
