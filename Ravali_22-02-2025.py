# Find  outputs
#How  to  import   kw  list 
from keyword import kwlist
#How  to  print  kwlist
print(kwlist) #['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#How  to  print  number  of  keywords
print(len(kwlist)) # 35
#How  to  print  type  of kwlist
print(type(kwlist)) # <class 'list'>
print(keyword . kwlist) # Error because keyword is not imported

#How  to  import   keyword  module
import keyword
#How  to  print  kwlist
print(keyword.kwlist) # displays all the keywords in kwlist ie.,['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',....so on]
#How  to  print  number  of  keywords
print(len(keyword.kwlist)) # 35
#How  to  print  type  of kwlist
print(type(keyword.kwlist)) # <class 'list'>
#print(kwlist) # Error because kwlist is not imported
