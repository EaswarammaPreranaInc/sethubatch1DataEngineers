# Modify  following   program  with  walrus  operator
# Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator
# '''
# try:
# 	sum =  ctr = 0
# 	x = eval(input('Enter input  (-1  to  stop)  :  '))
# 	while  x != -1:
# 		sum += x
# 		ctr +=1
# 		x = eval(input('Enter input  (-1  to  stop)  :  '))
# 	# End  of  while  loop
# 	print('Average :  ' ,  sum / ctr)
# except  ZeroDivisionError:
# 	print('Enter  at  least   one  input')
# except  (NameError , TypeError):
# 	print('Input  can  not  be string')


try:
    sum = ctr = 0
    while (x := eval(input('Enter input (-1 to stop) : '))) != -1:
        sum += x
        ctr += 1
    # End of while loop
    print('Average : ', sum / ctr)
except ZeroDivisionError:
    print('Enter at least one input')
except (NameError, TypeError):
    print('Input can not be string')
