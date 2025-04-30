# eval()  function  demo  program
#eval() funtion converts string to appropriate object (Removes Quotes)
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False')) # Converts string 'False' to boolen False
print(eval('3+4j')) # Converts string '3+4j' to complex (3+4j)
print(eval("    'Hyd'   ")) # Remains as string 'Hyd'
print(eval('3 + 4 * 5')) # converts string '3+4*5' to mathematical expression int 3+4*5 which results in 23
print(eval('[10 , 20 , 15 , 18]')) # converts string '[10 , 20 , 15 , 18]' to list [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}')) #converts string '{10,20,15,18,20,12,18}' to set {10,20,15,18} set doesnot contain duplicates
print(eval('(10 , 20 , 30)')) #converts string '(10 , 20 , 30)' to tuple (10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # converts string "{10 : 'Hyd' , 10 : 'Sec'}" to dict { 10 : 'Sec'}
#print(eval(4 + 5)) # Error because eval must be a string

print(eval("    'hyd'   ")) # hyd
hyd = 'Sec' 
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) # 10.8
#print(eval(cyb)) # error because 10.8 is float not string eval () must be string

#  Find  output  (Home  work) 
print(eval('print("Hyd")')) #Hyd <next line> None

#  Find  outputs  (Home  work)
print(bool('False')) # True because non empty strings are true in bool 
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # empty spaces
#print(eval('')) # Error
print(eval('  " "   ')) # white space
#print(eval(' '))

x = eval(input('Enter  any  input  :  ')) # Enter any input : ('ravali')
print(type(x)) # depending on what you type of object you give <class 'str' >
print(x) #ravali

# Which  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # Ravali
print(len(a)) # 6
print(a) # Ravali
b = eval(input('Enter   any  string  : ')) # 'Gubba'
print(len(b)) # 5
print(b) Gubba
# in this case i feel input is better and easy approach to read string input as i directly type the input without quotes

# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25	   10.8   	Hyd	
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25 <next line> 10.8 <next line> Hyd
print(a , b , c) #25 10.8 hyd due to default sep is space 
print(a , b , c , separator = ':') # Error because separator is not supported only sep is supported

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # 25 10.8 Hyd---
print(a , b , c , sep = ',,,') # 25,,,10.8,,,Hyd in previous line continuous
print(a , b , c , sep = ':::' , end = '\t\t\t') #  25:::10.8:::Hyd			
print(a , b , c) # 25 10.8 Hyd in previous line continuous

# Find outputs  (Home  work)
print('Hyd') # Hyd
print() # white space
print('Sec') # Sec
print() # white space
print('Cyb') # Cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) #[10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) # <5 spaces>10.9
print('%10.3f'  %a) # <4 spaces>10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.927400
print('%f'  %a) # 10.927400

# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4  spaces>
print('%2s'  %a) # 
print('%s'  %a) # Hyd
print('%s' , a) # %s Hyd
#print('%s'  a) # Error
#print('%s' , %a) # Error
print(a) # Hyd

#  Find  outputs  (Home  work)
#even number of braces remains x 
#odd number of braces gives value of x 
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  # {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}') # {{25}}
print(F'{{{{{{x}}}}}}') # {{{x}}}
print(F'{{{{{{{x}}}}}}}') # {{{{25}}}
print(F'{{{{{{{{x}}}}}}}}') # {{{{x}}}}
