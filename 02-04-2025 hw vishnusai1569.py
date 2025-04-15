
''' 1. Input : 123456789
Output  :  Twelve  crores  thirty  lakhs  fifty  six  thousand  seven  hundred  eighty  nine '''

from num2words import num2words

def number_to_indian_words(num):
    return num2words(num, lang='en_IN').replace(",", "").capitalize()

# Example usage
num = 123456789
print(number_to_indian_words(num)) 

'''2. with dict '''
def words(n):
	a={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
	c=''
	for x in n:
		c+= a[int(x)] +' '
	return c
n=input("Enter a number: ")
print(words(n))

'''3. Repeat roman numbers with dict'''
def roman(n):
	a= {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,'L': 50, 'XL': 40,'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
	c=''
	for sym,val in a.items():
		count=n//val
		c+=sym * count
		n-=val*count
	print(c)
n= int(input("Enter a number: "))
roman(n)
''' 
# 4.  (Home  work)
print('Begin')
print(How  to  print  variable  'x'  of  cal   module
print(y)
print(cal . x)
print
print(sub(10 , 7))
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
'''
'''
#cal.py
if  __name__=='__main__':
	
	def sub(a,b):
		return a-b
	def div(a,b):
		return a/b
x=100
y=200
def add(a,b):
	return a+b
def mul(a,b):
	return a*b

class c1:
	def m1(self):
		print('m1 Method')'''
import cal #How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ? 
print('Begin')
from cal import x,add,mul,c1 #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle  with  from  statement
print(cal.x)
#print(y) # error call with mosule name 
print(add(10,7))
#(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
#print(sub(10,7)) # error not executed  writing sub and div under if condition 
#print(div(10 , 7)) # error  not executed 
print(mul(10,7))
a=c1()
a.m1() #How to print m1() method of class c1 

# 5. Module  alias
print('Begin')
# How  to  import  cal  module  with   another  name  using  import  statement
import cal as c
print(c.x) #(How  to  print  variable  'x'  of  cal   module
print(c.y) #(How  to  print  variable  'y'  of  cal   module
print(c.add(10,7)) #(How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(c.sub(10,7)) #(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(c.mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print (c.div(10,7)) #(How  to  call  div()  function  of  cal  module  by  passing  10  and  7
#How  to  call  m1()  method  of  c1  class  in  cal  module
cl=c.c1()
cl.m1()
#print(cal . x) # error it has alias 
#from  math  as   m  import  * #  error module name cant have alias 

# 6. Member  alias
from cal import x as a,add as ad,mul as m,c1 as c # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(a)#(How  to  print  variable  'x'  of  cal   module
#print(x) # error no x in this program
print(ad(10,7))  #(How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(m(10,7)) #(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
m2=c()
m2.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module
#print(add(10 , 7)) # error it has an alias 
#b = c1() # error class as an alias 

# 7. Find  outputs  (Home  work)
x = 30
def   disp(): 
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) # 10
disp() # disp  function  of mod 1
a = c1() 
a . m1() # m1  method of  class  c1  in mod 1

# 8. Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) # 30
disp()  # disp  function  of  same  module
a = c1()
a . m1()  #m1  method of  class  c1  in  same  module

#9. How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
#How  to  import  mod1  and  mod2
import mod1,mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) #(How  to  print  variable  'x'  of  mod1
print(mod1.disp()) #How  to  call  disp()  function  of  mod1
c=mod1.c1()
c.m1() #How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x)  #(How  to  print  variable  'x'  of  mod2
print(mod2.disp()) #How  to  call  disp()  function  of  mod2
cm=mod2.c1()
cm.m1()#How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x)#(How  to  print  variable  'x'  of  current  module)
print(disp()) #How  to  call  disp()  function  of current  module
cc=c1()
cc.m1()#How  to  call  method  m1()  of  class   c1  in  current  module 

# 10.How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import * #How  to  import  members  of  mod1
from mod2 import * #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
''' #(How  to  print  variable  'x'  of  mod1)
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1 # members of mod 1 and mod 2 cant be used in this program bcz they are not replaced with current module values 
print()
print()
print(How  to  print  variable  'x'  of  mod2)
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2 '''
print()
print()
print(x)#(How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
c=c1()
c.m1()#How  to  call  method  m1()  of  class   c1  in  current  module 
