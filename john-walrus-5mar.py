try:
	
	sum =  ctr = 0
	
	while(x := eval(input('Enter input  (-1  to  stop)  :  ')))!=-1:
		
		sum += x
		ctr +=1
		
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not  be string')

#output--
Enter input  (-1  to  stop)  :  10
Enter input  (-1  to  stop)  :  20
Enter input  (-1  to  stop)  :  -1
Average :   15.0
