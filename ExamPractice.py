def prime(n):
    for i in range(2, n//2 + 1):
        if n%i == 0:
            return False

    return True

n = int(input('Enter a Number:'))
if n<2:
    print('Invalid Input:',n)
elif prime(n):
    print('Prime Number:',n)
else:
    print('Composite Number:',n)       