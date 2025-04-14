
print({10 , 20}  |  {30 , 20}) #{10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})#{10:'Hyd',20:'Vja',30:'Sec'}
#print(range(4) | range(5))
hw-2
print(True  and  False)    #  False
print(False  and  True)  #  False
print(False  and   False)  #   False
print(True  and  True)  # True
print(10  and  20)  #  20
print(0  and  20) #  0
print(-25  and  0)  #  0
print(''  and  25)
print(6j  and  'Hyd')#Hyd
print(0j  and  'Sec')#0j
print('Hyd'   and  10.8)#10.8
print(10  and  20  and  30)#30
hw-3
print(True  or  False)   #   True
print(False  or  True)   #  True
print(True  or  True) #  True
print(False  or   False)    # False
print(10  or  20)   #  10
print(0   or  20)  #   20
print(-25  or  0)#-25
print(''  or  35)#35
print(6j  or  'Hyd')#6j
print(0.0  or  3 + 4j)#(3+4j)
print('Hyd'   or   10.8)#Hyd
hw-4
print(not  True)  #  False
print(not  False)  #  True
print(not  25)# False
print(not  0)# True
print(not  'Hyd')# False
print(not  '')# True
print(not  -10)# False
print(not  not  'Hyd')# True
hw-5
i = 10
i = not  i > 14
print(i)# True
print(not(6 < 4  or  9 >= 5  and  6 != 6))# True

