program 1
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False'))  # converts 'False' to False
print(eval('3+4j'))   #  converts '3+4j' to 3+4j
print(eval("    'Hyd'   ")) # error 
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]')) # converts '[10,20,15,18]' to [10,20,15,18]
print(eval('{10,20,15,18,20,12,18}')) # converts {10,20,15,18,20,12,18}
print(eval('(10 , 20 , 30)')) # converts to '(10,20,30)' to (10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # converts to {10:'sec'}
print(eval(4 + 5)) # error


program 2
print(eval("    'hyd'   "))  # 'hyd'
hyd = 'Sec'
print(eval('hyd')) # 'sec'
sec = '25'
print(eval('sec'))  # '25'
print(eval(sec))   # 25
cyb = 10.8
print(eval('cyb'))  # 10.8
print(eval(cyb))   # error


program 3
print(eval('print("Hyd")')) # hyd  None


program 4
print(bool('False'))  # True 
print(eval('False'))  # False
print(bool(''))   #   False
print(eval('  ""  '))  #  empty string
print(eval(''))  # error
print(eval('  " "   ')) # " "
print(eval(' ')) # error

program 5
x = eval(input('Enter  any  input  :  ')) # 25
print(type(x)) # <class 'int'>
print(x) # 25

program 6
a = input('Enter  any  string  :  ') # Hyd
print(len(a)) # 3
print(a) # Hyd
b = eval(input('Enter   any  string  : ')) 'Hyd'
print(len(b)) # 3
print(b) # Hyd

program 7
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t')    # 25 10.8 Hyd
print(a , b , c , sep = '---')  # 25---10.8---Hyd
print(a , b , c , sep = '\n')   # 25 
                                  10.8
                                  Hyd
print(a , b , c)   # 25 10.8 Hyd
print(a , b , c , separator=':')  # error

program 8
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')  # 25 10.8 Hyd---
print(a , b , c , sep = ',,,')   # 25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')  # 25:::10.8:::Hyd
print(a , b , c)  # 25 10.8 Hyd

program 9
print('Hyd') # Hyd
print()   # nothing
print('Sec')  # Sec
print()   # nothing
print('Cyb')  # Cyb

program 10
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10,20,30,40] (10,20,30,40) {10,20,30,40}

program 11
a = 25
b = '%f'  %a  # converts object 'a' to string float 
print(b)  # 25.000000
print(type(b))  # <class'str>
x = 10.8  # convetrs object 'x' to string integer
y = '%d'  %x
print(y) # '10'
print(type(y)) # <class<'str'>
m = [10 , 20 , 15 , 18] # converts list to string list
n = '%s'  %m
print(n) # [10,20,15,18]
print(type(n)) # class<'str'>

program 12
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)  # <5 spaces> 10.9
print('%10.3f'  %a)  # <4 spaces > 10.927
print('%.2f'  %a)  # 10.93 
print('%.6f'  %a)   # 10.927400
print('%f'  %a)  # 10.927400

