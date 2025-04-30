'''  (Home  work) 28/2/2025 

1.Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
'''

'''
try: 
    n=int(input("Enter a number:"))
    
    if(n==0):
        print("Zero")
        
    elif (n%2==0):
        print("Even")
        
    else:
        print("Odd")
        
except:
    print("Enter only integer")
  
'''

'''
2. Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif 

Enter month number (1 - 12): 7
july

Enter month number (1 - 12): 13
Input  should  be  between  1  and   12

Enter month number (1 - 12): 10.8
Input  should  be  an  integer

'''

'''

try:
    m=int(input("Enter month number (1 - 12):"))
    
    if(m==1):
        print("January")
        
    elif(m==2):
        print("February")
        
    elif(m==3):
        print("March")
        
    elif(m==4):
        print("Aipril")
        
    elif(m==5):
        print("May")
        
    elif(m==6):
        print("June")
        
    elif(m==7):
        print("July")
        
    elif(m==8):
        print("August")
        
    elif(m==9):
        print("September")
        
    elif(m==10):
        print("October")
        
    elif(m==11):
        print("November")
        
    elif(m==12):
        print("December")
        
    else:
        print("Input  should  be  between  1  and   12")
        
except:
    print("Input  should  be  an  integer")
        
    
'''


'''
3.Write  a  program  to  test  year  is  leap  year  or  not

Enter  4-digit  year :  2024
Leap year

Enter  4-digit  year :  1900
Not a leap year

'''


'''
try: 
    y=int(input("Enter  4-digit  year :"))
    
    if(y%4==0 and y%100!=0 or y%400==0):
        print("Leap year")
        
    else:
        print("Not a leap year")
    
        
except:
    print("Enter only integer")
    
'''


'''
4.Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else


Enter 1st input : 10
Enter 2nd input : 20
Enter 3rd input : 15
Laregst  number  :   20

'''

'''
try:
    a=eval(input("Enter 1st input :"))
    b=eval(input("Enter 2nd input :"))
    c=eval(input("Enter 3rd input :"))
    
    if(a>b):
        if(a>c):
            print("Laregst  number  :",a)
                
        else:
            print("Laregst  number  :",c)
                
            
    else:
            
        if(b>c):
            print("Laregst  number  :",b)
                
        else:
            print("Laregst  number  :",c)
        
    
except:
    print("a,b,c values can not be complex")
'''


'''
5.Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  2
Enter  fahrenheit  temperature : 100
celsius   equivalent :  37.78

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  1
Enter  celsius  temperature :  30
Fahrenheit  Equivalent  :  86.0

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  3
Invalid input

'''

'''

try:
    n=int(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :"))

    if(n==2):
        f=float(input("Enter  fahrenheit  temperature :"))
        c= (f-32)*5/9
        print(f"celsius   equivalent : {c:.2f}")
        
    elif(n==1):
        c=float(input("Enter  celsius  temperature :"))
        f=9/5 *c + 32 
        print(f"Fahrenheit  Equivalent  : {f:.1f}")
        
    else:
        print("Invalid input")
        
except:
    print("for temp enter int or float but for selection enter only int")
  
'''  


'''
6.Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

Enter  value  of  x  co-ordinate :  -10
Enter  value  of  y  co-ordinate :  20
2nd quadrant

'''

'''

try:
    m=eval(input("Enter  value  of  x,y  co-ordinate :"))
   
    match m:
        case (0,0): print("origin")
        case (x,0): print("x-axis")
        case (0,y): print("y-axis")
        case _: 
            if(m[0]>0 and m[1]>0):
                print("1st quadrant")
                
            elif(m[0]<0 and m[1]>0):
                print("2nd quadrant")
                
            elif(m[0]<0 and m[1]<0):
                print("3rd quadrant")
                
            elif(m[0]>0 and m[1]<0):
                print("4th quadrant")
                
except:
    print("x,y should be a real numbers")
    
'''



'''
7.Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

Enter  first  input   :  10
Enter  second   input   :  20
Enter  third  input   :  7
Largest number :  20.0
Smallest number :  7.0
Middle number :  10.0

'''

'''
try:
    a=float(input("Enter 1st input :"))
    b=float(input("Enter 2nd input :"))
    c=float(input("Enter 3rd input :"))
    
    if(a>b and a>c):
        M=a 
    elif(b>c):
        M=b 
    else:
        M=c 
        
    if(a<b and a<c):
        m=a 
    elif(b<c):
        m=b 
    else:
        m=c 
        
    mid=(a+b+c)-(M+m)
    
    print("Largest number :",M)
    print("Smallest number :",m)
    print("Middle number :",mid)
        
        
    
except:
    print("enter int  or float for a,b,c")

'''


'''
8.Write  a  program  to  determine  three  sides  form  a  triangle  or  not

Enter  1st  side : 3
Enter  2nd  side : 4
Enter  3rd  side : 5
Scalene  triangle
Area : 6.00
Perimeter : 12.0

Enter  1st  side : 7
Enter  2nd  side : 8
Enter  3rd  side : 7
Isoscles  triangle
Perimeter : 22.0

Enter  1st  side : 7
Enter  2nd  side : 7
Enter  3rd  side : 7
Equilateral  triangle
Area : 21.22

Enter  1st  side : 3
Enter  2nd  side : 4
Enter  3rd  side : 8
Not  a  triangle

'''

'''
from math import sqrt
try:
    a=float(input("Enter  1st  side :"))
    b=float(input("Enter  2nd  side :"))
    c=float(input("Enter  3rd  side :"))
    
    if((a+b)>c and (b+c)>a and (a+c)>b):
        
        if(a==b and a==c):
            print("Equilateral  triangle")
            A=sqrt(3)a*2/4
            print(f"Area: {A:.2f}")
            
        elif(a==b or a==c or b==c):
            print("Isoscles  triangle")
            print(f"Perimeter: {(a+b+c)}")
            
        else:
            print("Scalene  triangle")
            s=(a+b+c)/2
            A=sqrt(s*(s-a)(s-b)(s-c))
            print(f"Area: {A:.2f}")
            print(f"Perimeter: {(a+b+c)}")
            
        
    else:
        print("Not  a  triangle")

except:
    print("enter only real values for triangle sides")

'''

'''
9.Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0 
where  a  ! = 0

Enter  value  of  a : 5
Enter  value  of  b : 6
Enter  value  of  c : 5
Roots  are  imaginary  (or) complex
Root 1 : -0.6 +  0.8j
Root 2 : -0.6 -  0.8j

Enter  value  of  a : 3
Enter  value  of  b : 10
Enter  value  of  c : 3
Roots  are  real  and  distinct
Root 1 : -0.33
Root 2 : -3.00

Enter  value  of  a : 5
Enter  value  of  b : 10
Enter  value  of  c : 5
Roots are real and equal
Root 1 : -1.0
Root 2 : -1.0

Enter  value  of  a : 0
Value  of  a  can  not  be  0

'''

'''
from math import sqrt
try:
    a=int(input("Enter  value  of  a :"))
    if(a==0):
        print("Value  of  a  can  not  be  0")
        
    else:
        b=int(input("Enter  value  of  b :"))
        c=int(input("Enter  value  of  c :"))
        
        D=b**2-4*a*c 
        
        if(D>0):
            print("Roots  are  real  and  distinct")
            x1=(-b + sqrt(D))/(2*a)
            x2=(-b - sqrt(D))/(2*a)
            print(f"Root 1 : {x1:.2f}")
            print(f"Root 2 : {x2:.2f}")
            
            
        elif(D==0):
            print("Roots are real and equal")
            x1=x2=-b/(2*a)
            print(f"Root 1 : {x1:.1f}")
            print(f"Root 2 : {x2:.1f}")
            
        else:
            print("Roots  are  imaginary  (or) complex")
            r= -b/(2*a)
            i= sqrt(-D)/(2*a)
            
            x1=f"{r} + {i}j"
            x2=f"{r} - {i}j"
            
            print("Root 1 :",x1)
            print("Root 2 :",x2)
            
except:
    print("enter only integer values for a,b,c")

''' 
         
    
   
'''
10.
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

Enter  value  of  x : 3
Enter  value  of  y : 4
Enter radius of circle : 5
Point is on the circle



'''

'''
from math import sqrt
try:
    x=float(input("Enter  value  of  x :"))
    y=float(input("Enter  value  of  y :"))
    r=float(input("Enter  radius  of the circle :"))
    
    d=x*2 + y*2
    D=sqrt(d)
    
    if(D==r):
        print("Point is on the circle")
        
    elif(D>r):
        print("Point is outside the circle")
        
    else:
        print("Point is inside the circle")
        
except:
    print("enter only int or float values")
 
''' 


'''
11.Write  a  program  to  determine  bill  amount  and  input  is  units

'''

'''
try:
    u=abs(float(input("Enter positive Units:")))
    
    match u//100:
        case 0: 
            a=u*3 
            
        case 1:
            a=100*3 + (u-100)*3.5
            
        case 2|3:
            a=100*3 + 100 *3.5 + (u-200)*4
            
        case 4|5|6:
            a=100*3 + 100*3.5 + 200*4 + (u-400)*4.5 
            
        case _:
            a=100*3 + 100*3.5 + 200*4 + 300*4.5 + (u-700)*5 
            
            
    print("Amount:",a)
            
except:
    print("enter only integer or float units ")
   
'''
     
            
'''

12.Write  a   program  to  print  day  of  the  week
'''

'''
try:
    d=int(input("Enter a day number: "))
    
    match d:
        case 1: print("Monday")
        case 2: print("Tuesday")
        case 3: print("Wednesday")
        case 4: print("Thursday")
        case 5: print("Friday")
        case 6: print("Saturday")
        case 7: print("Sunday")
        case _: print("invalid day number")
        
except:
    print("enter only integer as a day number")
    
'''


'''
13.Write  a  program  to  print  digit in  words

'''

'''

try:
    d=int(input("Enter a single digit"))
    
    match d:
        case 0: print("Zero")
        case 1: print("One")
        case 2: print("Two")
        case 3: print("Three")
        case 4: print("Four")
        case 5: print("Five")
        case 6: print("Six")
        case 7: print("Seven")
        case 8: print("Eight")
        case 9: print("Nine")
        case _: print("Not a single digit ")
        
except:
    print("enter only integer ")

'''

'''
14.Write  a  program  to  print  fibonacci  series  upto   x

Enter  value  of  x  :  10
Fibonacci  Series
0
1
1
2
3
5
8

'''



try:
    x=int(input("Enter  value  of  x  :"))
    a=0 
    b=1 
    
    if(x==0):
        print(x)
        
    elif(x>=1):
        print(a,b,sep="\n")
        c=a+b 
    
        while(c<=x):
            print(c)
            a=b 
            b=c
            c=a+b
            
         
    else:
        print("enter +ve value or 0")
        
except:
    print("enter only integer value")
        
