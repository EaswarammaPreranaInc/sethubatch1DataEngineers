'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15 is  found  at  index  2
                 15 is  found  at  index  5
                 15 is  found  at  index  8
                 15 is  found   3  times
'''

a= [15,10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
n = int(input("Enter Value : "))
b = 0
for x in range(len(a)):
    if a[x] == n:
     print(F"Found at index : {x}")
     b+=1

if b>0:
 print(f"{n} is found {b} times")
else:
 print("Not found")
'''
Enter Value : 15
Found at index : 0
Found at index : 3
Found at index : 6
Found at index : 9
15 is found 4 times'''

'''
Modify  following   program  with  walrus  operator
Hint:  Combine  lines  7 , 8   and  11  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	while  (x :=eval(input('Enter input  (-1  to  stop)  :  ')))and x!= -1:
		sum += x
		ctr +=1
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not  be string')
