x=int(input("Enter a Number : "))

a=0
b=1
c=a+b

if x==a:
    print(a)
elif x==b:
    print("Fibonacci series :",a,b,sep="\n")
else:
    print("Fibonacci series :",a,b,sep="\n")
    while c < x:
        print(c)
        a=b
        b=c
        c=a+b
        

    