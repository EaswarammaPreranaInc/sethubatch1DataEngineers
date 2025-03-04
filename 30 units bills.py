units = int(input('Enter  units :   '))

match  int(units/100):
	case 0:
		cost =units*3
	case 1:
	    cost =100*3+(units-100)*3.5
	case 2 | 3:
		cost =100*3+100*3.5+(units-200)*4
	case  4 | 5 | 6:
		cost =100*3+100*3.5+100*4+(units-300)*4.5
	case _:
		cost=100*3+100*3.5+100*4+100*4.5+(units-400)*5
print('Bill  amount  :  ',cost)
