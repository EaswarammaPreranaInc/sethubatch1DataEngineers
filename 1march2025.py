# Modify  following  program  with  else  and  if


# Modify  following  program  with  else  and  if
"""
try:
	a = int(input('Enter month number (1 - 12): '))
	if  a == 1:
		print('January')
	elif  a == 2:
		print('Febraury')
	elif  a == 3:
		print('March')
	elif  a == 4:
		print('April')
	elif  a == 5:
		print('May')
	elif  a == 6:
		print('June')
	elif  a == 7:
		print('july')
	elif  a == 8:
		print('August')
	elif  a == 9:
		print('September')
	elif  a == 10:
		print('October')
	elif  a == 11:
		print('November')
	elif  a == 12:
		print('December')
	else:
		print('Input  should  be  between  1  and   12')
except:
		print('Input  should  be  an  integer')
            
"""
"""
try:
	
    a = int(input('Enter month number (1 - 12): '))
    if  a == 1:
        print('January')
    else:
            if  a == 2:
                print('Febraury')
            else: 
                if  a == 3:
                    print('March')
                else:
                    if  a == 4:
                        print('April')
                    else:
                        if  a == 5:
                            print('May')
                        else:
                            if  a == 6:
                                    print('June')
                            else:
                                if  a == 7:
                                    print('july')
                                else:
                                    if  a == 8:
                                        print('August')
                                    else:
                                        if  a == 9:
                                            print('September')
                                        else:
                                            if  a == 10:
                                                print('October')
                                            else:
                                                if  a == 11:
                                                    print('November')
                                                else:
                                                    if  a == 12:
                                                        print('December')
                                                    else:
                                                        print('Input  should  be  between  1  and   12')
except:
		print('Input  should  be  an  integer')

"""


#Write  a  program  to  determine  bill  amount  and  input  is  units
'''
Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)				Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)				Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(>= 700)				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
"""
units = int(input('Enter  units :   ')) 
o=units
for units in range(units):
    for i in range(units,101):
        a=i
    cost=a*3.00
    units=a
    print(units,cost)
    for j in range (units,201):
        b=j
    cost=b*3.50
    units=b
    print(units,cost)
    for k in range(units,401):
        c=k
    cost=c*4.00
    units=c
    print(units,cost)
    for l in range(units,701):
        d=l
    cost=d*4.50
    units=d
    print(units,cost)
    for m in range(units):
        e=m
    cost=e*5.00
    units=e
    print(units,cost)
    break
print(f"total bill amount of {o} : {cost}")

units = int(input('Enter  units :   ')) 
o=units
print(o)
for units in range(0,units):
    for i in range(units,101):
        a=i
    cost=a*3.00
    x=cost
    units=a
    print(a)
    print(units,cost)
    for j in range (units,201):
        b=j
    cost=(b*3.50)-(x)
    y=cost
    print(units,cost)
    for k in range(units,401):
        c=k
    cost=(c*4.00)-(y)
    z=cost
    print(units,cost)
    for l in range(units,701):
        d=l
    cost=(d*4.50)-(z)
    p=cost
    print(units,cost)
    for m in range(units):
        e=m
    cost=(e*5.00)-(p)
    print(units,cost)
    break
print(f"total bill amount of {o} : {cost}")
"""

