#1 print the first 10 natural numbers using loop
n = int(input("Enter the numbers:"))
for i in range(1, 11):
    print(i)


#2 print the program to print all the even numbers with in the given range
start = int(input("Enter the start of range:"))
end = int(input("Enter the end of the range:"))
for i in range(start, end +1):
    if i % 2 == 0:
        print(i)


#3 python program to calculate the sum of all numbers from 1 to a given number
n = int(input("Enter a number:"))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print("The sum of all numbers from 1 to", n, "is:", total_sum)


#4 python program to calculate the sum of all the odd numbers with in the given range
start = int(input("Enter the start of the range:"))
end = int(input("Enter the end of the range:"))
sum = 0
for i in range(start, end + 1):
    if i % 2 != 0:
        sum += i
print("The sum of all odd numbers from", start, "to", end, "is:", sum)


#5 python program to print a multiplication table of a given number
n = int(input("Enter a number:")
for i in range(1, 10):
    print(n, "x", i, "=", n * i)




