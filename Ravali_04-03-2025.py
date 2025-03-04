Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  searched ?  --->  Found  at  index  2

2) What  is  the  output  if  19  is  searched ?  --->  Not  found

3) What  action  to  be  made  if  'x'  is  not  matched  with  the  current  element  of  list ?  --->  Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  if  'x'  is   matched   with  list  element ?  --->  Print  found   message  along  with  index  and
																														  don't   search  in  rest  of  the  list

5) What  action  to  be  made  if  'x'  is   not  matched  with  all  the  elements  of  list ?  --->  Print  not  found   message

6) Hint: Use  for  loop

x = int(input('Enter number: '))
a = [10,20,15,12,18]
for i in range(len(a)):
	if x == a[i]:
		print(F'found at index {i} ')
		break
else:
	print('Not found')

#  Walrus   operator (:=)  demo  program
print(a := 25) #25
#print(a = 25) #ERROR
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7)
print(a) #6
#print((a = 6) + 7) # error
