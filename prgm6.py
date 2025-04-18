 #Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('__iter__    method')
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
if __name__ == '__main__':
	a = c1()
	print('Elements  of  iterator  with  for  loop')
	for   element   in   a:
		print(element)
		if  element  ==  5:
			break
			print('Elements  of  iterator  with  next()  function')
			while    True:
				element = next(a)
				print(element)
				if  element  ==  10:
					break
					#end  of  while  loop
					print('Elements  of  iterator  with  for  loop')
					for   element   in    a:
						print(element)
						if  element  ==  15:
							break