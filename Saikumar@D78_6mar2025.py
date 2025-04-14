"""                                                                                                              
# eval()  function  demo  program                                                                                
print(eval('25'))  #  Converts  '25'  to  25                                                                     
print(eval('10.8'))  #  Converts  '10.8'  to   10.8                                                              
print(eval('False'))                                                                                             
print(eval('3+4j'))                                                                                              
print(eval("    'Hyd'   "))                                                                                      
print(eval('3 + 4 * 5'))                                                                                         
print(eval('[10 , 20 , 15 , 18]'))                                                                               
print(eval('{10,20,15,18,20,12,18}'))                                                                            
print(eval('(10 , 20 , 30)'))                                                                                    
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))                                                                         
#print(eval(4 + 5)) #error due to input without string quotes                                                    
"""                                                                                                              
#1--                                                                                                             
# Gift                                                                                                           
# Find  outputs  (Home  work)                                                                                    
print(eval("    'hyd'   "))                                                                                      
hyd = 'Sec'                                                                                                      
print(eval('hyd'))                                                                                               
sec = '25'                                                                                                       
print(eval('sec'))                                                                                               
print(eval(sec))                                                                                                 
cyb = 10.8                                                                                                       
print(eval('cyb'))                                                                                               
#print(eval(cyb))#error due to input without string quotes                                                       
                                                                                                                 
                                                                                                                 
#2--                                                                                                             
# Find  outputs (Home  work)                                                                                     
a = 'Hyd'                                                                                                        
print('%7s'  %a)  #   <4  spaces>Hyd                                                                             
print('%-7s'  %a)  #  Hyd<4  spaces>                                                                             
print('%2s'  %a)                                                                                                 
print('%s'  %a)                                                                                                  
print('%s' , a)                                                                                                  
#print('%s'  a)                                                                                                  
#print('%s' , %a)                                                                                                
print(a)                                                                                                         
#3--                                                                                                             
#Find outputs  (Home  work)                                                                                      
a = 25                                                                                                           
b = 10.9274                                                                                                      
c = 'Hyd'                                                                                                        
print('%d    %f    %s'  %(a , b , c))                                                                            
print('%i    %g    %s'    %(a , b , c))                                                                          
print('%s    %s    %s'  %(a , b , c))                                                                            
print('%d    %g    %s'  , a , b , c)                                                                             
#print('%d    %g      %s'   a , b , c)                                                                           
#print('%d    %g    %s'  ,  %(a , b , c))                                                                        
#print('%d    %g    %s'    %a%b%c)                                                                               
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)                                                                  
                                                                                                                 
#4---                                                                                                            
#  Find  outputs  (Home  work)                                                                                   
x = 25                                                                                                           
y = F'{x}'                                                                                                       
print(y)                                                                                                         
print(type(y))                                                                                                   
x = 10.8                                                                                                         
y = F'{x}'                                                                                                       
print(y)                                                                                                         
print(type(y))                                                                                                   
x = [10,20,30,40]                                                                                                
y = F'{x}'                                                                                                       
print(y)                                                                                                         
print(type(y))                                                                                                   
                                                                                                                 
#5---                                                                                                            
#Find  outputs  (Home  work)                                                                                     
a ,  b , c = 25 , 10.8 , 'Hyd'                                                                                   
print(F'{a}  \t   {b}   \t  {c}')                                                                                
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')                                                                  
print(F'{a=}  \t   {b=}   \t  {c=}')                                                                             
print(F'{a:}  \t   {b:}   \t  {c:}')                                                                             
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')                                                                
print(F'a  =  a  \t  b  =  b  \t  c  =  c')                                                                      
#print(F'{x =}  \t   {y =}   \t  {z =}')                                                                         
                                                                                                                 
#6---                                                                                                            
#  Find  outputs  (Home  work)                                                                                   
x = 25                                                                                                           
print(F'{x}')  #  25                                                                                             
print(F'{{x}}')   #  {x}                                                                                         
print(F'{{{x}}}')  #   {25}                                                                                      
print(F'{{{{x}}}}')                                                                                              
print(F'{{{{{x}}}}}')                                                                                            
print(F'{{{{{{x}}}}}}')                                                                                          
print(F'{{{{{{{x}}}}}}}')                                                                                        
print(F'{{{{{{{{x}}}}}}}}')                                                                                      
                                                                                                                 
                                                                                                                 
#7---                                                                                                            
'''                                                                                                              
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself                           
                                                                                                                 
2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  str
                                                                                                                 
3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2                           
'''                                                                                                              
                                                                                                                 
                                                                                                                 
'''                                                                                                              
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  number
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input                    
                                                                                                                 
Enter 1st  integer  number :  10                                                                                 
Enter 2nd  integer  number :  7                                                                                  
10 + 7 = 17                                                                                                      
10 - 7 = 3                                                                                                       
10 * 7 = 70                                                                                                      
10 / 7 = 1.4285714285714286                                                                                      
10 % 7 = 3                                                                                                       
max(10 , 7) = 10                                                                                                 
min(10 , 7) = 7                                                                                                  
10 ^ 7 = 10000000                                                                                                
sqrt(10) = 3.1622776601683795                                                                                    
gcd(10 , 7) = 1                                                                                                  
fact(10) = 3628800                                                                                               
                                                                                                                 
Hint:  Use  F  string  to  print  results                                                                        
'''                                                                                                              
                                                                                                                 
import math                                                                                                      
a=int(input('Enter 1st integer number :'))                                                                       
b=int(input('Enter 2nd integer number :'))                                                                       
print(F'{a:}+{b:} = ',a+b)                                                                                       
print(F'{a:}-{b:} = ',a-b)                                                                                       
print(F'{a:}*{b:} = ',a*b)                                                                                       
print(F'{a:}/{b:} = ',a/b)                                                                                       
print(F'{a:}%{b:} = ',a%b)                                                                                       
print(F'max({a:},{b:}) = ',max(a,b))                                                                             
print(F'min({a:},{b:}) = ',min(a,b))                                                                             
print(F'{a:}**{b:} = ',a**b)                                                                                     
print(F'sqrt({a:}) = ',math.sqrt(a))                                                                             
print(F'gcd({a:},{b:})= ',math.gcd(a,b))                                                                         
print(F'fact({a:})= ',math.factorial(a))                                                                         
                                                                                                                 
                                                                                                                 
#8--                                                                                                             
'''                                                                                                              
Gift                                                                                                             
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
                                                                                                                 
Let  'x'  be  25  and  'y'  be   'Hyd'                                                                           
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25                                                      
                                                                                                                 
Hint:  Swap  references  but  not  objects                                                                       
'''                                                                                                              
                                                                                                                 
a=eval(input("enter 1st input : "))                                                                              
b=eval(input("enter 2nd input : "))                                                                              
print("before swapping","a:",a,"b:",b)                                                                           
a,b=b,a                                                                                                          
print("after swappping","a:",a,"b:",b)                                                                           
