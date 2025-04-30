'''# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)
for  index , element  in  c:
	print(F'{element:15}  ... {b[index]}')
	time . sleep(1)

	#output
Telangana        ... Hyderabad
Andhra  Pradesh  ... Amaravathi
Karnataka        ... Bangalore
TamilNadu        ... Chennai
Maharastra       ... Mumbai
'''

# Can  dictionary  be  enumerated ?   (Home  work)
import   time
def  disp(e):
	while  True:
		try:
			print(next(e))
			time . sleep(1)
		except:
			break
	print()
a = {'Empno'  :  25 , 'Emp Name'  :  'Rama Rao' , 'Sal' : 10000.0}
b = enumerate(a . keys())
disp(b)
c = enumerate(a . values())
disp(c)
d = enumerate(a . items())
disp(d)
f = enumerate(a , start = 5)
disp(f)





