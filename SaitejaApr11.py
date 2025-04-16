#11/4/2025 

#1. Public  and  Private  members  demo  program

'''
class  Test:
	def  _init_(self):
		self.x=10  #How  to  initialize  public  variable  'x'  to  10
		self.__y=20 #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method') #5. m1 method
		print(self.x) #How  to  print   variable  'x' #6. 10 
		print(self.__y) #How  to  print  private  variable  'y' #7. 20 
		self.__m2() #How  to  call    private  method   m2()
		print('Back to m1 method') #11. Back to m1 method
	def  __m2(self):
		print('__m2  method') #8. __m2 method #12.  __m2 method
		print(self.x) #How  to  print   variable  'x' #9. 10  #13. 10
		print(self.__y) #How  to  print  private  variable   'y' #10. 20  #14. 20
		
# End  of  the  class
t = Test()
print('Outside') #1. Outside 
print(t.x) #How  to  print  variable  'x' #2. 10
print(t.Test_y) #How  to  print   variable  'y' #3. 20 
#print(t . __y) #Error private can't accessed directly  
print(t ._dict) #4. {'x':10,'_Test_y':20}
t.m1() #How  to  call  method  m1()
t.Test_m2() #How  to  call   method  m2()
#t . __m2() #Error private can't accessed directly  
print('End') #15. End

'''


#2.Find  outputs
'''
class  c1:
	def _init_(self):
		self.x=10 #How  to  initialize  public  variable  'x'  with  10
		self.__x=20 #How  to  initialize  private  variable  'x'  with  20
		self._x_=30 #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method') #4. public method
	def  __m1(self):
		print('private method') #6. private method
	def  _m1_(self):
		print('public Dunder method') #5. public Dunder method
#  End  of  the  class
a = c1()
print(a.x) #How  to  print   variable  'x' #1. 10 
print(a._x_) #How  to  print  public  dunder  variable  'x' #2. 30
print(a.c1_x) #How  to  print   private  variable  'x' #3. 20
#print(a . __x) #Error 
a.m1() #How  to  call  public  method  m1()
a._m1_() #How  to  call  public  dunder  method  m1()
a.c1_m1() #How  to  call  private  method  m1()
#a . __m1() #Error

'''


'''
#3. Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''

'''
class   c1:
	def _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1() #1. Object  is  created  at  address  : 1000
a = None #2. Object  at  address  1000  is  lost

b = c1() #3. Object  is  created  at  address  : 1000
del    b #4. Object  at  address  1000  is  lost

c = c1() #5. Object  is  created  at  address  : 1000
c = c1() #6. Object  is  created  at  address  : 2000 
#7. Object  at  address  1000  is  lost

d = c1() #7. Object  is  created  at  address  : 1000
e = c1() #8. Object  is  created  at  address  : 3000

#9. Object  at  address  1000  is  lost
#10. Object  at  address  2000  is  lost 
#11. Object  at  address  3000  is  lost

'''


#3.Identify  Error (Home  work)
'''
class   c1:
	def  _del_(self , x): # no arg for destructor 
		print('destructor')
		exit()
a = c1()
a . _del_(25) #No ars for destructor 

'''


#4.Find  outputs (Home  work)

'''
class   c1:
	def  _del_(self):
			print('destructor') #1. destructor
			b = c1() #2. destructor infinite 
a = c1()
 
'''

#5.Find  outputs (Home  work)

'''
class   c1:
	def  _init_(self):
		print('constructor') #1.constructor(a)
		del  self #2.destructor(a)
	def  _del_(self):
		print('destructor') #4.destructor (b) #5. destructor (b).... #infinite destructor...
		b = c1() #3.constructor (b) #5.constructor (b).... #infinite constructor...
a = c1() 

'''


#6.Find  outputs( Home  work)
'''
class   c1:
	def  _del_(self):
		print('1st  destructor')
	def  _del_(self):
		print('2nd  destructor')
	def  _del_(self):
		print('3rd  destructor')
# End  of  the  class
a = c1() #3rd  destructor

'''


#7.Find  outputs (Home  work)

'''
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1() 
#Object  is  created  at  address  :  1000 (a)
del   a 
print('Hello') # Hello
del   b 
print('Hi') #Hi
del   c # Object  at  address  1000  is  lost (c)
print('Bye') #Bye
d = c1() #Object  is  created  at  address  :  1000 (d)
print('End') #End 
# Object  at  address  1000  is  lost (d)

'''


#8. Find  outputs(Home  work)
'''
class  c1:
        def _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
#Object  is  created  at  address  :  1000 list[0]
#Object  is  created  at  address  :  2000 list[1]
#Object  is  created  at  address  :  3000 list[2]

del  list
#Object  at  address  3000  is  lost 
#Object  at  address  2000  is  lost 
#Object  at  address  1000  is  lost 

'''


#9.Find  outputs  (Home  work)
'''
class   c1:
	def  _del_(self):
		print('destructor')
		return  25
a = c1()
print(a . _del_()) #1. destructor #2. 25 
print('Hello') #3. Hello 
del   a #4. destructor

'''
#Test 2 solutions 

#1. each digit to word 

'''
d={'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
n=int(input("Enter a integer number: "))
s=str(n)

for i in s:
    print(d[i],end=" ")
    
'''


#2. Number to Roman numberal 

'''
d={1000:'M',900:'CM',800:'DCCC',700:'DCC',600:'DC',500:'D',400:'CD',300:'CCC',200:'CC',
   100:'C',90:'XC',80:'LXXX',70:'LXX',60:'LX',50:'L',40:'XL',30:'XXX',20:'XX',10:'X',
    9:'IX',8:'VIII',7:'VII',6:'VI',5:'V',4:'IV',3:'III',2:'II',1:'I'
  }
  
n=int(input("Enter a integer number: "))
r=''

while(n>0):
    if(n>=1000):
        m=n//1000 
        r=r+m*d[1000]
        n=n-m*1000
        
    elif(n>=100):
        m=n//100
        r=r+d[m*100]
        n=n-m*100
        
    elif(n>=10):
        m=n//10 
        r=r+d[m*10]
        n=n-m*10
        
    elif(n>=1):
        m=n%10 
        r=r+d[m]
        n=n-m*1
        
print(r)
'''

#3.List operations 

'''
L=[]
while(True):
    n=int(input("MENU: enter 1=insert or 2=delete or 3=exit: "))
    
    if(n==1):
        L.append(int(input("Enter element to be inserted: ")))
        
    elif(n==2):
        L.remove(int(input("Enter valid element to be removed: ")))
        
    elif(n==3):
        break 
    
    else:
        print("Invalid Choice")
        
    L.sort()
    print(L)
    
'''



#4. diamond pattern 

'''
n=int(input("Enter number of rows: "))
l=n//2 + 1 
c=2
for i in range(1,n+1):
    if(i==1 or i==n):
        print((l-1)'  ',' ',sep='')
        
    elif(i<=l):
        print((l-i)'  ',c'* ')
        c=c+2 
        
       
    else:
        if(i==l+1):
            c=c-4 
            
        print((i-l)'  ',(c)'* ')
        c=c-2
        
'''


#5. nth largest number in the array 

'''
a=list(map(int,input("Enter elements of the List: ").split()))
n=int(input("Enter n: "))

def max_pop(a):
    
    m=a[0]
    
    for i in range(1,len(a)):
        if(a[i]>m):
            m=a[i]
            
    M=m 
    a.remove(m)
    
    return M

for i in range(1,n+1):
    if(i==n):
        print(max_pop(a))
        
    else:
        max_pop(a)
        
'''

#6. Largest word in the sentence 

'''
s=input("Enter a sentence: ").split()
L=[]

for i in s:
    L.append(len(i))
    
m=max(L)

for i in range(len(L)):
    if(L[i]==m):
        print(s[i])
 
'''   

#7. multiply 2 Matrices 

'''
r1,c1,r2,c2= map(int,input("Enter r1,c1,r2,c2: ").split())

if(c1!=r2):
    print("Matrix multiplication not possible")
    
else:
    A=[]
    for i in range(1,r1+1):
        a=list(map(int,input(F"Enter {i}th row elements sepearted by spaces: ").split()))
        A.append(a)
    
    
    B=[]
    for i in range(1,r2+1):
        b=list(map(int,input(F"Enter {i}th row elements sepearted by spaces: ").split()))
        B.append(b)
        
    print(F"Matrix A order {r1},{c1}")
    for i in A:
        print(*i)
        
    print(F"Matrix B order {r2},{c2}")
    for i in B:
        print(*i)
    
    C=[]
    for i in range(r1):
        c=[]
        for j in range(c2):
            s=0
            for k in range(c1):
                s+=A[i][k]*B[k][j]
                
            c.append(s)
            
        C.append(c)
        
    print(F"Matrix C order {r1},{c2}")
    for i in C:
        print(*i)
    
'''  

#8. Transpose of a Matrix 
'''
r,c=map(int,input("Enter r c : ").split()) 

A=[]

print("Matrix: ")
for i in range(1,r+1):
    a=list(map(int,input().split()))
    A.append(a)
    
B=[]
for i in range(c): 
    b=[]
    for j in range(r): 
        b.append(A[j][i])
        
    B.append(b)
   
print("Transposed Matrix")   
for i in B:
    print(*i)
'''

#9. Permutations

'''
from itertools import*
l=list(map(int,input("Enter the list: ").split()))
p=permutations(l)

for i in p:
    print(i)
    
'''

#10. Gcd of list of numbers 

'''
a=list(map(int,input("Enter the list: ").split()))
m=min(a)

for i in range(m,0,-1):
    for j in a:
        if j%i!=0:
            break 
    else:
        print(i)
        break 
'''