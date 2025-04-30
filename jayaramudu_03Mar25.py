# Ex-1: Print elements with index

a = [25, 10.8, 'Hyd', True]
for i in range(len(a)):
    print(i, a[i])
print()
for i in a:
    print(a.index(i), i)

# Ex-2: Reverse list order
a = eval(input('Enter list of elements : '))
a.reverse()
for i in range(len(a)):
    print(i, a[i])
print()
for i in a:
    print(i)

# Ex-3: Add two lists
a = eval(input('Enter a 1st list :- '))
b = eval(input('Enter a 2nd list :- '))
c = [a[i] + b[i] for i in range(len(a))]
print(c)

# Ex-4: Print elements from index 2 to 4
a = [25, 10.8, 'Hyd', True, 3+4j, None, 'Sec']
for i in range(2, 5):
    print(i, a[i])

# Ex-5: First 20 even numbers
try:
    n = int(input('Enter a number : '))
    l = 1
    while l <= n:
        print(2 * l)
        l += 1
except:
    print('Input should be an integer')

# Ex-6: First 20 odd numbers
try:
    n = int(input('Enter a number : '))
    l = 1
    while l <= n:
        print(2 * l - 1)
        l += 1
except:
    print('Input should be an integer')

# Ex-7: Print natural numbers up to n
try:
    n = int(input('Enter a number : '))
    for i in range(1, n+1):
        print(i)
except:
    print('Input should be an integer')

# Ex-8: Print numbers from 10 to 1
try:
    n = int(input('Enter a number : '))
    for i in range(n, 0, -1):
        print(i)
except:
    print('Input should be an integer')

# Ex-9: Print uppercase and lowercase alphabets
for i in range(65, 91):
    print(chr(i), end='  ')
print()
for i in range(97, 123):
    print(chr(i), end='  ')
print()

# Ex-10: Fibonacci series
try:
    n = int(input('Enter a number : '))
    a, b = 0, 1
    print(a, b, end=' ')
    for _ in range(2, n):
        a, b = b, a + b
        print(b, end=' ')
except:
    print('Input should be an integer')

# Ex-11: Search for x in Fibonacci series
try:
    n = int(input('Enter value to be searched : '))
    a, b, c = 0, 1, 1
    found = n in {0, 1}
    while c <= n and not found:
        a, b = b, c
        c = a + b
        found = c == n
    print('Found' if found else 'Not Found')
except:
    print('Input should be an integer')

# Ex-12: Sum of sequence 1.1 + 2.2 + 3.3 + ...
try:
    n = int(input('Enter a number : '))
    total = sum(1.1 * i for i in range(1, n+1))
    print(total)
except:
    print('Input should be an integer')

# Ex-13: Sum of first 20 even numbers
try:
    n = int(input('Enter a number : '))
    total = sum(2 * i for i in range(1, n+1))
    print('Sum of first 20 even numbers:', total)
except:
    print('Input should be an integer')

# Ex-14: Sum of first 20 odd numbers
try:
    n = int(input('Enter a number : '))
    total = sum(2 * i - 1 for i in range(1, n+1))
    print('Sum of first 20 odd numbers:', total)
except:
    print('Input should be an integer')

# Ex-15 & Ex-16: Sum of first n natural numbers
try:
    n = int(input('Enter a number: '))
    if n < 1:
        print('Please enter a number at least 1')
    else:
        total = sum(range(1, n+1))
        print(total)
except ValueError:
    print('Input should be an integer')
