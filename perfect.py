#program of menu ****************(1)
'''def menu():
	list=[]
	while True:	
		m=int(input("enter the integer : "))
		x=int(input("select the operation 1 or 2 : "))
		if x==1:
			list.append(m)
			print(sorted(list))
		elif x==2:
			list.remove(m)
			print(sorted(list))
		else:
			exit()
menu()
'''
#gcd******************(2)
'''def fact(n):
    factor_lists = []

    for i in n:
        factors = []
        for j in range(1, i + 1):
            if i % j == 0:
                factors.append(j)
        factor_lists.append(factors)
        print(f"Factors of {i}: {factors}")
    common_factors = set(factor_lists[0])
    for factors in factor_lists[1:]:
        common_factors.intersection_update(factors)

    gcd_value = max(common_factors) if common_factors else 1
    print(f"GCD of {n} is: {gcd_value}")

n = eval(input("Enter the list of numbers: "))
fact(n)
'''
'''
#pattern program****************(3)
def pattern(n):
	c=40
	print(' '*(c),"*")
	for i in range(1,n+1):
		print(' '*(c-1),'* '*i*2)
		c-=1
	for j in range(n-1,0,-1):
		print(' '*(c+1),'* '*j*2)
		c+=1
	print(' '*(c+1),"*")
n=int(input("enter number of rows"))
pattern(n)
'''
#number to words**********************(4)
'''def words(n):
	str=""
	a={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
	m=list(n)
	for x in m:
		x=int(x)
		if x in a:
			str+=a[x]+' '
	print(str)
n=input("number")
words(n)
'''

#program roman ********************(5)
'''def latin(n):
	str=" "
	while n>1000:
		n=n-1000
		str+='M'
	while n>900:
			n=n-900
			str+='CM'
	while n>500:
		n=n-500
		str+='D'
	while n>400:
			n=n-400
			str+='CD'
	while n>100:
			n=n-100
			str+='C'
	while n>90:
			n=n-90
			str+='XC'
	while n>50:
			n=n-50
			str+='L'
	while n>40:
			n=n-40
			str+='XL'
	while n>10:
			n=n-10
			str+='X'
	while n>9:
			n=n-9
			str+='IX'
	while n>5:
			n=n-5
			str+='V'
	while n>4:
			n=n-4
			str+='IV'
	while n>1:
		n=n-1
		str+='I'
	print(str)
n=int(input('enter the number'))
latin(n)
'''
'''#************************(6) permutations
 def perm(n):
	n=list(n)
	for i in n:
		for j in n:
			if j != i:
				for k in n:
					if k != i and k != j:
						print(i, j, k)
n =input("enter the number")
perm(n)
'''
# codes couldnt write properly
#matrix multiplication****************************(7)
'''def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        print("Matrix multiplication not possible")
        return

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    for row in result:
        print(row)
A=eval(input("enter matrix 1: "))
B=eval(input("enter matrix 2: "))
multiply_matrices(A, B)
'''
'''
#program to longest word finding**********************(8)
def long(n):
    words = []
    word = ""
        for char in n:
        if char != ' ':
            word += char
        else:
            if word:
                words.append(word)
            word = ""
    if word:
        words.append(word)
    longest_word = ""
    for w in words:
        if len(w) > len(longest_word):
           longest_word = w
    print("Longest word:", longest_word)
n = input("Enter the string: ")
long(n)
'''

#transpose*****************(9)
'''def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[0] * rows for _ in range(cols)]  # Initialize transpose matrix

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]  # Swap rows and columns

    return transposed

# Example Input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transposing the matrix
result = transpose(matrix)

# Displaying the result
for row in result:
    print(row)
'''
'''
def find_nth_largest(lst, n):
    for i in range(n):  
        largest = lst[0]  
        for num in lst:  
            if num > largest:
                largest = num  

        lst.remove(largest)  

    print(f"{n}th largest number:", largest)

numbers = eval(input("enter the list"))
nth = int(input("Enter N: "))
find_nth_largest(numbers, nth)
'''
def fib(x):
	a=0
	b=1
	if x==0:
		yield 0
	elif x==1:
		yield 0
		yield 1
	else:
		yield a
		yield b
		while a<x :
			c=a+b
			a=b
			b=c
			yield c
x=int(input("enter the number: "))
for i in fib(x):
	print(i)






























































































































































