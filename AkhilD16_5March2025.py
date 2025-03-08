#1.Program to search for an element in the list without using in operator
try:
	a=eval(input("Enter list: ")) # [10,20,15,12,18,15,19,14,15,14]
	num=int(input("Enter a number: "))
	count=0
	for x in range(len(a)):
		if a[x]==num:
			print(num," Found at index: ",x)
			count+=1
	print(num," Found ",count," times")
except:
	print("Input should be a number")

#2.Program to determine largest command line input

from sys import argv # let command line input be py DetermineLargestCommandLineInput.py 10 20 30 40 50
print(argv)
a=[]
for x in range(1,len(argv)):
	print(x)
	a.append(argv[x])
print(a)
print("Largest input is: ",max(a))

#3.Program to determine command line input is Even or Odd
try:
	from sys import argv
	print(argv)
	for x in range(1,len(argv)):
		num=int(argv[x])
		if num%2==0:
			print(num," is Even number")
		else:
			print(num," is Odd number")
except:
	print("Input should be an integer")

#4.Program to determine average of command line inputs

from sys import argv #Let command line inputs be 10,20,30,40,50
print(argv)
a=[]
for x in range(1,len(argv)):
	a.append(int(argv[x]))
print("Average of command line inputs: ",sum(a)/len(a))

#5.Program to sort command line inputs in ascending order and descending order

from sys import argv
print(argv)
a=[]
for x in range(1,len(argv)):
	a.append(int(argv[x]))
print("List 'a' elements before sorting: ",a)
a.sort()
print("Ascending Order:",a)
a.sort(reverse=True)
print("Descending order: ", a)


