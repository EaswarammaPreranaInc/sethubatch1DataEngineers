# print the first 10 natural number using for loop
'''
for i in range(10):
    print(i)
'''
#print all the even numbers with in the given range 
'''
a=int(input("enter the value to print even numbers upto : "))
for i in range(0,a,2):
    print("the even numbers form one to the given range are : ",i) 

'''
# to print the sum of all numbers upto from 1 to given range 
'''
a=int(input("enter the value to calculate the sum upto : ")) 
for i in range(1,a):
    a+=i
print("the sum of numbers upto the given range : ",a)

'''
#to print the sum of all the odd numbers upto the given range 

'''
a=int(input("enter the value to print odd numbers upto : "))
c=0
for i in range(0,a):
    if i%2!=0:
        print(i)
        c+=i
print("the odd numbers form one to the given range are : ",c)

'''

# print the multiplication table for the given number
"""
a=int(input("enter the number to print the multiplication table for : "))
for i in range(1,11):
    print(f"{a}*{i}=",(a*i))

"""
# program to display numbers from a list using a for loop

'''
a=list(input("enter the elements to the list : "))
print(type(a))
print(a)
for i in a:
    print(i)

'''
#program to print the total number of digts in a number 
"""

print("length of the given number :",len(input(" enter the number : ")))

a=int(input("enter the number : "))
c=str(a)
for i in c:
    c=i
print("the length of given value is :",c)

"""

# check if the given number is palindrome or not 
'''
a=input("enter the number : ")
c=a[::-1]
print(f"The given number is palindrome :{a}" if (a==c) else f"not a palindrome :{c}")

'''
# To reverse the word
'''

print("reverse of the given word : ",input("enter the word : ")[::-1])

'''
# check given number is amstrong or not
'''
a=int(input("enter the number : "))
c=str(a)
g=0
for i in c:  
    b=eval(i)
    d=b**3
    g=g+d
print(f"{a} is amstrong number" if a==g else f"{a} is not amstrong number")

'''
