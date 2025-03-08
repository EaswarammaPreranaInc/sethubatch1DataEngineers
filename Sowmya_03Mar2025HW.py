### Printing each element with its index:
```
a = [25, 10.8, 'Hyd', True]

print('Indexed for loop')
for i in range(len(a)):
    print(f"Index {i}: {a[i]}")

print('For each loop')
for i, value in enumerate(a):
    print(f"Index {i}: {value}")
```

### Printing list elements in reverse order without slicing:
```
a = eval(input('Enter list of elements: '))

print('Indexed for loop')
for i in range(len(a)-1, -1, -1):
    print(a[i])

print('For each loop')
for item in reversed(a):
    print(item)
```

### Adding two lists:
```
a = [10, 20, 15, 18]
b = [30, 40, 35, 12]
c = []

# Indexed based for loop
for i in range(len(a)):
    c.append(a[i] + b[i])
print('3rd list:', c)

# For-each loop
c = [x + y for x, y in zip(a, b)]
print('3rd list:', c)
```

### Printing elements from index 2 to 4 without slicing:
```
a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']

print('Indexed for loop')
for i in range(2, 5):
    print(a[i])

print('For each loop')
count = 0
for item in a:
    if 2 <= count <= 4:
        print(item)
    count += 1
```

### First 20 even numbers:
```
i = 1
count = 0
while count < 20:
    print(2 * i)
    i += 1
    count += 1
print("Bye")
```

### First 20 odd numbers:
```
i = 1
count = 0
while count < 20:
    print(2 * i - 1)
    i += 1
    count += 1
```

### Printing natural numbers up to n:
```
n = int(input("Enter value of n: "))
print("Natural Numbers")
for i in range(1, n+1):
    print(i)
```

### Counting down from 10:
```
for i in range(10, 0, -1):
    print(i)
```

### Printing uppercase and lowercase alphabets:
```
for i in range(65, 91):
    print(chr(i), end=' ')
print()
for i in range(97, 123):
    print(chr(i), end=' ')
print()
```

### Fibonacci series up to n terms:
```
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci series")
for _ in range(n):
    print(a)
    a, b = b, a + b
```

### Searching for an element in Fibonacci series:
```
fib_set = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144}  # Predefined Fibonacci numbers

x = int(input("Enter value to be searched: "))
if x in fib_set:
    print("Found")
else:
    print("Not Found")
```

### Summing series 1.1 + 2.2 + 3.3 + ... up to n terms:
```
n = int(input("How many terms would you like to add: "))
total = sum(1.1 * i for i in range(1, n + 1))
print("Sum:", total)
```

### Summing first 20 even numbers:
```
sum_even = sum(2 * i for i in range(1, 21))
print("Sum of first 20 even numbers:", sum_even)
```

### Summing first 20 odd numbers:
```
sum_odd = sum(2 * i - 1 for i in range(1, 21))
print("Sum of first 20 odd numbers:", sum_odd)
```

### Summing natural numbers without formula:
```
n = int(input("How many terms would you like to add: "))
sum_n = sum(i for i in range(1, n + 1))
print("Sum:", sum_n)
```

