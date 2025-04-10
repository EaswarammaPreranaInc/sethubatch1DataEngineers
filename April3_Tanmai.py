#  1. Find  outputs
import  cal
print(cal . x) #100
print(cal . y) #200
print(cal . add(10 , 7)) #17
print(cal . sub(10 , 7)) #3
print(cal . mul(10 , 7)) #70
print(cal . div(10 , 7)) #1.42
a = cal . c1()
a . m1() #m1 method

'''
2. Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) Hint:  Use  startswith()  and  endswith()  methods  of  str  class

5) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
''' 
import cal
a=[]
for x in dir(cal):
	if x.startswith('_') and x.endswith('_'):
		pass
	else:
		a.append(x)
print(a)

#  3. Find  outputs
print(dir()) # print the elements of current in the form of list of strings  
print()
from  cal  import  * # importing members of cal module 
print()
print(dir()) # also add cal members
 
#  4. Find  outputs
print(dir()) # print memebers of current module 
print() 
from  cal  import  add , mul , x
print()
print(dir()) # print memebers of current module  and also add mul x 
