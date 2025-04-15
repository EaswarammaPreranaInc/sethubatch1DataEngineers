'''
3/3/2025 

1.How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

'''

'''
a=[25,10.8,'Hyd',True]

print('Indexed for loop')
for i in range(len(a)):
    print(a[i],i)
    
print()

print('For each loop')
for i in a:
    print(i,a.index(i))

'''

'''
#2.How  to  print  list  elements  in  reverse  order   without  slice
a = eval(input('Enter  list  of  elements : '))
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable)

'''

'''
try:
    a = eval(input('Enter  list  of  elements : '))

    print('Indexed for loop')
    for i in range(1,len(a)+1):
        print(a[-i])
    
    print()

    print('for each loop')
    a.reverse()
    for i in a:
        print(i)
        
except:
    print("enter elements properly")
 
'''   


'''
3.Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

'''

'''
try:
    a=eval(input("Enter 1st list:"))
    b=eval(input("Enter 2nd list:"))
    c=[]
    
    print("index based for loop")
    for i in range(len(a)):
        c.append(a[i]+b[i])
        
    print(c)
    
    d=[]
    print("\nfor each loop")
    
    for i in a:
        d.append(i+b[a.index(i)])
        
        
    print(d)
    
    
except:
    print("give proper format and elements of same type and same length")
    
'''

'''
#4.How  to  print  list  elements  from  indexes  2  to  4  without  slice

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

print('Indexed for loop')
for i in range(2,5):
    print(a[i])
    
print()
print('for each loop')
for i in a:
    if a.index(i)>=2 and a.index(i)<=4 :
        print(i)
'''


'''
5.Write  a  program  to  print  first  20  even  numbers  with  while  loop
'''

'''
try:
    n=int(input("Enter how many even numbers:"))
    print(F"First {n} even numbers")
    i=1 
    
    while(i<=n):
        print(2*i,end=" ")
        i+=1 
        
    print("\nBye")
        
except:
    print("enter integer only")
 
'''

'''
6.Write  a  program  to  print  first  20  odd  numbers  with  while  loop

'''

'''
try:
    n=int(input("Enter how many odd numbers:"))
    print(F"First {n} odd numbers")
    i=1 
    
    while(i<=n):
        print(2*i-1,end=" ")
        i+=1 
        
    print("\nBye")
        
except:
    print("enter integer only")

'''

'''
7.Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'
'''

'''
try:
    n=int(input("Enter value of n : "))
    print("Natural numbers")
    i=1 
    
    while(i<=n):
        print(i,end=" ")
        i+=1 
        
    print("\nBye")
        
except:
    print("enter integer only")
    
'''

'''
8.Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1
'''

'''
try:
    n=int(input("Enter int number:"))
    print(F"Numbers from {n} downto 1 in steps of -1")
    
    for i in range(n,0,-1):
        print(i,end=" ")
        
        
except:
    print("enter integer only")
    
'''


'''
9.Write  a  program  to  print  upper  and  lower  case  alphabets

'''

'''
for i in range(ord('A'),ord('Z')):
    print(chr(i),end=" ")
    
print("\n",end="")
for i in range(ord('a'),ord('z')):
    print(chr(i),end=" ")
    
'''

'''
10.Write  a  program  to  print  first  'n'  terms  of  fibonacci  series
'''

'''
try:
    n=int(input("Enter number of terms : "))
    print("Fibonacci series")
    a=0 
    b=1 
    print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b 
        print(c,end=" ")
        a=b 
        b=c
        
except:
    print("enter integer only")

'''  

'''
11.Write  a  program  to  search  for  'x'  in  fibonacci  series

'''

'''
try:
    x=int(input("Enter  value  to  be  searched :"))
    a=0 
    b=1 
    if(x==0 or x==1):
        print("Found")
        
    else:
        for i in range(1,x+1):
            c=a+b 
            if(c==x):
                print("Found")
                break 
            a=b 
            b=c
        
        else:
            print("Not Found")
except:
    print("enter integer only")
    
'''

'''
12.Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms
'''

'''
try:
    n=int(input("How  many  terms  would  you  like  to  add   : "))
    sum=0 
    for i in range(1,n+1):
        sum+=(1.1*i)
        
    print(sum)
    
except:
    print("enter integer only")
    
'''

'''
13.Write  a  program  to  determine  sum  of  first  20  even  numbers

'''

'''
try:
    n=int(input("How  many  terms  would  you  like  to  add   : "))
    sum=0 
    for i in range(2,2*n+1,2):
        sum+=i
        
    print(sum)
    
except:
    print("enter integer only")
    
'''

'''
14.Write  a  program  to  determine  sum  of  first  20  odd  numbers

'''

'''
try:
    n=int(input("How  many  terms  would  you  like  to  add   : "))
    sum=0 
    for i in range(1,2*n+1,2):
        sum+=i
        
    print(sum)
    
except:
    print("enter integer only")
    
'''

'''
15.Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2
'''

'''
try:
    n=int(input("How  many  terms  would  you  like  to  add   : "))
    sum=0 
    for i in range(1,n+1):
        sum+=i
        
    print(sum)
    
except:
    print("enter integer only")

'''