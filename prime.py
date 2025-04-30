def prime(n):
		if n<2:
			return 'Invalid Input'
		for x in range(2,(n//2)+1):
			if n%x==0:
				return 'Composite Number'
		else:
			return 'Prime Number'