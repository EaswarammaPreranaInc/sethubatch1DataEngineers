print(int(10.8)) #  Converts  10.8  to  10
print(int(True))  #  Converts  True  to  1
print(int(False))  # Convert False to 0
print(int('25'))    #Convert '25' to 25
print(int('0075'))   #Convert '0075' to 75
print(int(0B11010))  #26
print(0B11010)        #26
print(int(0O6247))    #3239
print(0O6247)         #3239
print(int(0XA7B9))    #42937
print(0XA7B9)         #42937
#print(int(3 + 4j))   #Error
#print(int('25.4'))   #Error
#print(int('Ten'))    #Error

print(float(25)) #  Converts  25  to  25.0
print(float(True)) #  Converts   True   to   1.0
print(float(False))  #Convert False to 0.0
print(float('92'))   #Convert '92' to 92.0
print(float('36.4'))  #Convert '36.4' to 36.4
print(float('0075'))   # Convert '0075' to 75.0
print(float(0B1010101))   #85.0
print(float(0O6247))       #3239.0
print(float(0XA7B9))      #42937.0
#print(float(3 + 4j))      #Error
#print(float('Ten'))        #Error

print(complex(3 , 4))          #3 + 4j
print(complex(0 , 4))          #4j
print(complex(3))              #3 + 0j
print(complex(3.8 , 4.6))      #3.8 + 4.6j
print(complex(3.8))            #3.8 + 0j
print(complex(3 , 4.5))        #3 + 4.5j
print(complex(True , False))   #1 + 0j
print(complex(True))           #1  + 0j
print(complex(False))          #0j
print(complex(True , 4))       # 1 + 4j
print(complex('3'))            # 3 + 0j
print(complex('3.8'))          # 3.8 + 0j
#print(complex(3 , '4'))        #Error
#print(complex('3' , 4))        #Error
#print(complex('3' , '4'))      #Error
#print(complex('Ten'))          #Error

print(bool(0)) #   Converts  0  to  False
print(bool(10))   #Converts 10 to True
print(bool(-25))   #Converts -25 to True
print(bool(0.0))   # Converts 0.0 to False
print(bool(0.1))    # Converts 0.1 to True
print(bool(0 + 0j))    # Converts 0 +0j to false
print(bool(10 + 20j))    # Converts 10+20j to True
print(bool(-15j))       #True
print(bool('False'))    #True
print(bool(''))         #False
print(bool('Hyd'))      #True
print(bool(' '))        #True
print(bool('True'))     #True


print(str(25))    #Converts   25  to  '25'
print(str(10.8))    # Converts 10.8 to '10.8'
print(str(3 + 4j))   #3+4j to '3+4j'
print(str(True))     #True to 'True'
print(str(False))    #False to 'False'
print(str(None))     #None to 'None'


print(oct(195))             #0o303
print(oct(0B10101110010))   #0o2562
print(oct(0xA7B9))          #0o123671


print(hex(25))                 #0x19
print(hex(0B10101111010111))   #0x2bd7
print(hex(0O6247))             #0xca7


'''
Convertion of Decimal to Octal :
	number  quotient  reminder
	195      24         3
	24        3         0
	3         0         3
reminders in the reverse order =  303

Convertion of Binary to Octal :
	4 2 1     4 2 1     4 2 1   4 2 1------weights
    1 0 1     0 1 1     1 0 0   1 0 0
	 
	 
''' 
'''
Convertion Binary to Decimal equelent :
	                     
			16 	8	4	 2    1----->weights
			 1  1   0    1    0----->16 + 8 + 2 = 26

			512    64    8    1----->weights
			 6      2    4    7----->3239

			4096   256   16   1------>weights
			 10     7    11   9------>42937

	64	32	 16 	8	4	 2    1----->weights
	1	0	 1     0    1    0    1----->64 + 16 + 4 + 1 = 85

'''
