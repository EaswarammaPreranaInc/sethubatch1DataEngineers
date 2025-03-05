import math

a = int(input(" "))

if a<=1:
    print("flase")
else:
    Isprime=True
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
         Isprime= False
         break
         
    if Isprime:
        print("is prime number")
    else:
        print ("non primenumber")
