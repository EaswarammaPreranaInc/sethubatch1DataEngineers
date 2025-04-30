#Homework
print({10 , 20}  |  {30 , 20}) # {10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10 : 'Hyd' ,30 : 'Cyb' , 20 : 'Vja'}
print(range(4) | range(5)) #Error Range doesnot support pipe or +

#  and  operator  program Homework
#Atleast one operand is false result is false.
#both operand should be true for result true
print(True  and  False)    #  False
print(False  and  True)  #  False
print(False  and   False)  #   False
print(True  and  True)  # True
print(10  and  20)  #  20 All non-zeros are true
print(0  and  20) #  0 
print(-25  and  0)  #  0
print(''  and  25) # ''
print(6j  and  'Hyd') # Hyd
print(0j  and  'Sec') # 0j
print('Hyd'   and  10.8)# 10.8 
print(10  and  20  and  30) # 30

#  or  operator  demo program homework
# Atleast one operand is true result is true
# Both opernads should be false for false
print(True  or  False)   #   True
print(False  or  True)   #  True
print(True  or  True) #  True
print(False  or   False)    # False
print(10  or  20) # 10
print(0   or  20) # 20
print(-25  or  0) #-25
print(''  or  35) # 35
print(6j  or  'Hyd') # 6j
print(0.0  or  3 + 4j) # 3+4j
print('Hyd'   or   10.8) #Hyd

# not  operator  demo  program
print(not  True)  #  False
print(not  False)  #  True
print(not  25) # False
print(not  0) # True 
print(not  'Hyd') # False
print(not  '') # True
print(not  -10) # False
print(not  not  'Hyd') # True

i = 10  #Reference i points to object 10
i = not  i > 14 
print(i) # True because not false is true
print(not(6 < 4  or  9 >= 5  and  6 != 6)) # True
