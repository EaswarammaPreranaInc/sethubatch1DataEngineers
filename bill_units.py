'''Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)				Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(>= 700)				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
units = int(input('Enter  units :   '))  #  450
match  units // 100:
	case  0:  #  units  between  0  and  99
		cost = units * 3.00
	case  1:   #  units  between  100  and  199
		cost =  100 * 3.00 + (units - 100) * 3.50
	case  2 | 3:
		cost = 100 * 3.00 + 100 * 3.50 + (units-200) * 4.00
	case  4 | 5 | 6:
		cost = 100 *3.00 + 100 * 3.50 + 200 * 4.00 + (units-400)*4.50
	case _: 
		cost =100 *3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +(units-700)*5.00
print('Bill  amount  :  ' , cost)