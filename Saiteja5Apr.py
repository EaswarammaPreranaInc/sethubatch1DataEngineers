 # 1.Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)

'''
from random import*

def d():
    return randint(0,9)
    
    
for i in range(10):
    print(d(),d(),d(),d(),d(),d(),sep='')
    
'''