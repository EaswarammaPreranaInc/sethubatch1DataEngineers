print({10 , 20}  |  {30 , 20})#prints without duplicates {10,20,30} and set will be done operation by pipe operator
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})#prints {10:'Hyd',20:'Vja',30:'Cyb'} and Dictionary will be done operation by pipe operator
print(range(4) | range(5))#Error due to we cannot do pipe operation between range and anothe range object 
							



#  and  operator  demo  program
print(True  and  False)    #  False , we have one operand is False we get False
print(False  and  True)  #  False , we have atleast one operand is False we get False
print(False  and   False)  #   False
print(True  and  True)  # True we have both operand True we get True
print(10  and  20)  #  20 , we take operand2 if we have two operands True
print(0  and  20) #  0, we have atleast one operand is False we get False
print(-25  and  0)  #  0 , we have atleast one operand is False we get False
print(''  and  25)#       Empty operand we get here
print(6j  and  'Hyd')# Hyd ,we take operand2 if we have two operands True
print(0j  and  'Sec')#0j , we have one operand is False we get False
print('Hyd'   and  10.8)#10.8 , we take operand2 if we have two operands True
print(10  and  20  and  30)#30 , we take operand3 if we have all operands True



#  or  operator  demo program
print(True  or  False)   #   True , we have atleast one operand is True we get True
print(False  or  True)   #  True , we have atleast one operand is True we get True
print(True  or  True) #  True , we take operand1 if we have two operands True
print(False  or   False)    # False , we have both operand False we get false 
print(10  or  20)   #  10, we take operand1 if we have two operands True
print(0   or  20)  #   20 , we have atleast one operand is True we  get True
print(-25  or  0)# -25, we have atleast one operand is True we  get True
print(''  or  35)# 35  , we have atleast one operand is True we  get True
print(6j  or  'Hyd')#6j , we take operand1 if we have two operands True
print(0.0  or  3 + 4j)# (3+4j) , we have atleast one operand is True we  get True
print('Hyd'   or   10.8)# Hyd , we take operand1 if we have two operands True


# not  operator  demo  program
print(not  True)  #  False , we have to take nagotiation to the given operands
print(not  False)  #  True , we have to take nagotiation to the given operands
print(not  25)# False , we have to take nagotiation to the given operands
print(not  0)# True , we have to take nagotiation to the given operands
print(not  'Hyd')# False , we have to take nagotiation to the given operands
print(not  '')# True , we have to take nagotiation to the given operands
print(not  -10)# False , we have to take nagotiation to the given operands
print(not  not  'Hyd')#True , we have to take nagotiation to the given operands



i = 10 # ref object i is 10
i = not  i > 14 # 10 is not > 14
print(i)# True  , here the  above condition is satisfied
print(not(6 < 4  or  9 >= 5  and  6 != 6))#(not(False or True =True and 6!=6.....>False   i.,e True and False = False ) i.e (not(False)=True