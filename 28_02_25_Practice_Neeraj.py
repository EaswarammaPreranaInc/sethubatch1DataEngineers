#write a prgm to determine a number is even or odd 
'''try:
    num = int(input('Enter No:'))
    if(num%2==0):
        print('Even',num)
    else:
        print('Odd',num)
except:
    print('Enter a Integer No:')   '''

#find outputs
'''if{10:20,30:40}:
    print('Hyd')
print('Bye')
#Leap Year
try:
    leap = int(input('Enter a No: '))
    if(leap%4==0 and leap%100!=0):
        print('Leap Year',leap)
    elif(leap%400==0):
        print('Leap Year')
    else:
        print('Not Leap Year')
except:
    print('Enter Integer input')  '''
    
#Largest of three numbers
'''try:
    num1 = int(input('Enter 1st input:'))  
    num2 = int(input('Enter 1st input:')) 
    num3 = int(input('Enter 1st input:'))   
    if(num1>num2 and num1>num3):
        print('1st input is greater',num1)
    elif(num2>num1 and num2>num3):
        print('2nd input is greater:',num2)
    else:
        print("3rd input is greater:",num3)    
except:
    print('Enter positive Integer:')                          '''

#write a prgm to convert celsices to fareh=nheit and vice-versa
'''try:
    n = int(input('enter 1  celsius to farenheit and 2 for farenheit to celsius: '))
    if(n==1):
        c = float(input('Enter celsius:'))
        print('Farenheit:',1.8*c+32)
    elif(n==2):
        f = float(input('Enter Farenheit:'))
        print(F'Celsius:{(f-32)/1.8:.2f}')
    else:
        print('Invalid Input')
except:
    print('Input should be number')     '''

#write a prgm to determine largest,smallest and middle of three numbers
a = float(input('Enter a value:'))
b = float(input('Enter b value:'))
c = float(input('Enter c value:'))
max = a
if(b>max):
    max = b
if(c>max):
    max = c
min = a
if(b<min):
    min = b
if(c<min):
    min = c
mid = (a+b+c) - (max-min)                
