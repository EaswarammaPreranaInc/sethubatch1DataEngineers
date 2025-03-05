# Ex-1: Search for an element in a list without using 'in' operator
try:
    l = eval(input('Enter a list of Values: '))
    a = int(input('Enter a search element: '))
    for i in range(len(l)):
        if l[i] == a:
            print('Found at index', i)
            break
    else:
        print('Not found')
except ValueError:
    print('Search element must be an integer')
except:
    print('Please enter a list of integer elements')

# Ex-2: Determine average of inputs terminated with -1
try:
    total = count = 0
    while True:
        n = eval(input('Enter input (-1 to stop): '))
        if n == -1:
            break
        total += n
        count += 1
    print('Average:', total / count if count else 'No inputs were provided')
except:
    print('Input should be an integer')

# Ex-3: Find outputs from the given loop
print('\nEx-3 Output:')
for i in range(1, 8):  # 1 to 7
    print(i)
    if i % 3 == 0:
        continue
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')

# Ex-4: Find outputs from another loop example
print('\nEx-4 Output:')
for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        break
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')
