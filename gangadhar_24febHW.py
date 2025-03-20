# eval()  function  demo  program
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False')) #False
print(eval('3+4j')) #3+4j
print(eval("    'Hyd'   ")) # hyd
print(eval('3 + 4 * 5')) #23
print(eval('[10 , 20 , 15 , 18]'))# [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}')) #{10,20,15,18,12,}
print(eval('(10 , 20 , 30)')) # (10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))# {10 : 'Sec'}
#print(eval(4 + 5)) #Type error : print(eval(4 + 5)) #error

print(eval("    'hyd'   ")) #hyd
hyd = 'Sec'
print(eval('hyd'))# sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb'))#10.8
#print(eval(cyb)) #error due to cyb not defined 

print(bool('False'))# True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  '))# empty
#print(eval('')) # invalid syntax due to empty 
print(eval('  " "   ')) # ''(a space) 
#print(eval(' '))

x = input('Enter  any  input  :  ')
print(type(x))# <class 'str'>
print(x)# ganga

a = input('Enter  any  string  :  ')
print(len(a))#4
print(a)#from
b = eval(input('Enter   any  string  : '))
print(len(b))#6
print(b)# string


# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t')  #  25    10.8    Hyd
print(a , b , c , sep = '---')#  25---10.8---Hyd
print(a , b , c , sep = '\n')#  25<next line>10.8<next line>Hyd
print(a , b , c) #25 10.8 hyd
#print(a , b , c , separator = ':')# error due to invaild 'separator' argument instead of sep

# Assigning a,b,c to 25,10.8,'hyd'
a , b , c = 25 , 10.8 , 'Hyd'

# Printing values with --- end
print(a , b , c , end = '---')  # 25 10.8 Hyd---

# Printing values with ,,, seperator
print(a , b , c , sep = ',,,')  #  25,,,10.8,,,Hyd

# prints value withh ::: sep and \t\t\t end 
print(a , b , c , sep = ':::' , end = '\t\t\t')  # 25::: 10.8::: Hyd			

print(a , b , c)  #  25 10.8 Hyd

# Printing strings separately
print('Hyd')  #  Hyd
print()  # blank line
print('Sec')  # Sec
print()  #  blank line
print('Cyb')  #  Cyb

# Lists, tuples, and sets
a_list = [10 , 20 , 30 , 40]
a_tuple = (10 , 20 , 30 , 40)
a_set = {10 , 20 , 30 , 40}


print(a_list , a_tuple , a_set)  # [10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30} Set may print in any order

# Formatting 
a = 25
b = '%f'  %a  # Converts integer to float string 
print(b)  # '25.000000'
print(type(b))  #  <class 'str'>

# Formatting 
x = 10.8
y = '%d'  %x  # Converts float to integer string 
print(y)  #  '10'
print(type(y))  # <class 'str'>

# Formatting 
m = [10 , 20 , 15 , 18]
n = '%s'  %m  # Converts list to string
print(n)  # '[10, 20, 15, 18]'
print(type(n))  #<class 'str'>

# Formatting 
a = 10.9274
print('%8.2f'  %a)  #'   10.93' (3 spaces 10.93)
print('%9.1f'  %a)  #'     10.9' (5 spaces  10.9)
print('%10.3f'  %a)  # '    10.927' (4 spaces 10.927)
print('%.2f'  %a)  # '10.93'
print('%.6f'  %a)  # '10.927400'
print('%f'  %a)  # '10.927400'

# Formatting 
a = 'Hyd'
print('%7s'  %a)  # '    Hyd' (4 spaces  'Hyd')
print('%-7s'  %a)  #'Hyd    ' ('Hyd'  4 spaces)
print('%2s'  %a)  # 'Hyd' 
print('%s'  %a)  # 'Hyd'
print('%s' %a)  # 'Hyd' 
#print('%s' a)  # invalid syntax due to missing comma between 2 operators
#print('%s' ,%a)  # invalid syntax error  due to %a
print(a)  #  'Hyd'

# Formatting
a = [10 , 20 , 30 , 40]
print('%s'  %a)  #'[10, 20, 30, 40]'
print('%s' %a)  # '[10, 20, 30, 40]'
#print('%s'  a)  # invalid syntax due to missing comma between 2 operators
#print('%s' ,%a)  #  invalid syntaxerror due to  %a
#print('%l'  %a)  # error due to unsupport format character %l
print(a)  #'[10, 20, 30, 40]'
