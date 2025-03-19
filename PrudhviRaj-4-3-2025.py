#Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1(without  walrus  operator)
try:
	c=0
	s=0
	while True:
		n=eval(input("Enter the input(Enter -1 to stop): "))

		if n==-1:
			break
		c+=n
		s+=1
	if n<0:
		d=c/s
		print(d)
	else:
		print("No numbers were entered")
except:
	print("Invalid input")
  """
  Output:
Enter input  (-1  to  stop)  :  25
Enter input  (-1  to  stop)  :  10.8
Enter input  (-1  to  stop)  :  True
Enter input  (-1  to  stop)  :  46.2
Enter input  (-1  to  stop)  :  False
Enter input  (-1  to  stop)  :  92
Enter input  (-1  to  stop)  :  -1
Average :   29.166666666666668
  """



#Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  andprint  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)
try:
	a=eval(input("Enter the List: "))
	n=eval(input("Enter the number to search: "))
	i=0
	while i<len(a):
		if a[i]==n:
			print("Found",i)
			break
		i+=1
	else:
		print("Notfound")
except:
	print("The Input should be Number")


"""
Output:
Enter the List: [10,20,15,18]
Enter the number to search: 20
Found 1
"""
