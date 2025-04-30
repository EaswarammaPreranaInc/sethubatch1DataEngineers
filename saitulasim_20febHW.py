#1 PROGRAM
# Pipe Operator
print({10 , 20}  |  {30 , 20}) # {10,20,30} sets operator can concatinated with pipe operator
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) #{10:'Hyd',20:'Vja',30:'Sec'} dict can be concatinated with pipe operator
print(range(4) | range(5))  

#2 PROGRAM
#  and  operator program
print(True  and  False)    #  False (in and operator both conditions are True it returns True, otherwise returns False)
print(False  and  True)  #  False
print(False  and   False)  #   False
print(True  and  True)  # True
print(10  and  20)  #  20
print(0  and  20) #  0
print(-25  and  0)  #  0
print(''  and  25)  # 25
print(6j  and  'Hyd')	# Hyd
print(0j  and  'Sec')	# 0j
print('Hyd'   and  10.8)	# 10.8
print(10  and  20  and  30)	# 30

#3 PROGRAM
# not  operator  demo  program
print(not  True)  #  False
print(not  False)  #  True
print(not  25)	# False
print(not  0)	# True
print(not  'Hyd')	# False	
print(not  '')	# True
print(not  -10)	# False
print(not  not  'Hyd')	# True

#4 PROGRAM
# not in operator 
i = 10
i = not  i > 14 # not 10 > 14 ..> not False
print(i) # True
print(not(6 < 4  or  9 >= 5  and  6 != 6))	# not(False or True and False) True



