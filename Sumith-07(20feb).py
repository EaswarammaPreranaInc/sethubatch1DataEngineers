#  Find  outputs
print({10 , 20}  |  {30 , 20}) # The output for it will be the combination of two sets as {10, 20,30} , as duplictaes can't be used.
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # The output for it will be the combination of two sets as {10:'Hyd', 20: 'Vja',30:'Cyb } , the 20:'Sec' is ignored due to the replacement with 'Vja'
print(range(4) | range(5))# The output for it will be an error occured due to the undefined operation of ranges.


#  and  operator  demo  program
print(True  and  False)    # Output: False
print(False  and  True)   # Output: False
print(False  and   False)   # Output:   False
print(True  and  True)  # Output:  True
print(10  and  20)   # Output:  20
print(0  and  20)  # Output: 0
print(-25  and  0)  # Output:  0
print(''  and  25) # Output: ''
print(6j  and  'Hyd') # Output: 'Hyd'
print(0j  and  'Sec') # Output: 0j
print('Hyd'   and  10.8) # Output: 10.8
print(10  and  20  and  30) # Output: 30


#  or  operator  demo program
print(True  or  False)   #   True
print(False  or  True)   #  True
print(True  or  True) #  True
print(False  or   False)    # False
print(10  or  20)   #  10
print(0   or  20)  #   20
print(-25  or  0)  #  -25
print(''  or  35) # 35
print(6j  or  'Hyd') # 'Hyd'
print(0.0  or  3 + 4j) # 3+4j
print('Hyd'   or   10.8) # 'Hyd'



# not  operator  demo  program
print(not  True)  #  False
print(not  False)  #  True
print(not  25)  # False
print(not  0)   #True
print(not  'Hyd') # False
print(not  '') # True
print(not  -10) # False
print(not  not  'Hyd') # True

#  Find   outputs (Home work)
i = 10
i = not  i > 14 # The Output would be True as i = 10, i>14 is False. So i = not (of it) so i will be True.
 print(i) # True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) # True as not(False or True and True ) will be it.














