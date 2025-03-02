'''
Example 1: Print the first 10 natural numbers using for loop.
Example 2: Python program to print all the even numbers within the given range.
Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
Example 4: Python program to calculate the sum of all the odd numbers within the given range.
Example 5: Python program to print a multiplication table of a given number
Example 6: Python program to display numbers from a list using a for loop.
Example 7: Python program to count the total number of digits in a number.
Example 8: Python program to check if the given string is a palindrome.
Example 9: Python program that accepts a word from the user and reverses it.
Example 10: Python program to check if a given number is an Armstrong number
'''

#Example 1: Print the first 10 natural numbers using for loop
'''
for i in range(0, 10+1):
	print(i)
'''

#Example 2: Python program to print all the even numbers within the given range.
'''
a=int(input('Enter the input:'))
for a in range(10):
	if a%2==0:
		print(a,end=' ')
'''


#Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
'''
x=int(input('Enter the Number:'))
sum=0
for x in range(1,10):
	print(x)
	sum+=x
	print("The sum is", sum)
'''


#Example 4: Python program to calculate the sum of all the odd numbers within the given range
try:
	x=int(input('Enter any integer:'))
	sum=0
	for i in range(1,11): 
		if i%2!=0:
			print(sum)
except:
	print('Input should be a integer number only')
#Example 5: Python program to print a multiplication table of a given number
'''
try:
	x=int(input('Enter the number:'))
	print('Displaying the multiplication table of given number')
	for i in range(1,11,1):
		print(x,'X',i, '=', x*i)
except:
	print('The input should be an integer only')
'''	

#Example 6: Python program to display numbers from a list using a for loop
'''
a=[10,20,30,40,50]
for i in a:
	print(i)
'''

#Example 7: Python program to count the total number of digits in a num
'''
try:
	a=int(input('Enter the number:'))
	count=0
	while a!= 0:
		a //= 10
		count += 1
	print('Number of digits:'+ str(count))
except:
	print('The input should be an integer')
'''

#Example 8: Python program to check if the given string is a palindrome.
'''
try:
	s=str(input('Enter the String:'))
	i,j=0, len(s) -1
	is_palindrome=True
	while i<j:
		if s[i] != s[j]:  # mismatch found
			is_palindrome=False
			break
		i += 1
		j -= 1
	if is_palindrome:
		 print('Yes')
	else:
		print('No')
except:
	print('Input should be a string')
'''

#Example 9: Python program that accepts a word from the user and reverses it
'''
a=str(input('Enter the input:'))
print('The Reverse input is:', a[::-1])
'''

#Example 10: Python program to check if a given number is an Armstrong number
'''
try:
	a=int(input('Enter the number:'))
	sum=0
	temp=a
	while temp > 0:
		digit = temp % 10
		sum += digit**3
		temp = temp//10
	if sum==a:
		print('It is an Armstrong number')
	else:
		print('It is not an Armstrong number')
except:
	print('Enter only integer values')
'''
