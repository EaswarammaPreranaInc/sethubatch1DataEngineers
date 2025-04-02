# Gift
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') # Dictionary  with  print  function
print(a) # {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}  #How  to  print  dictionary
print('Keys  of  dictionary') # Keys  of  dictionary
#How  to  print  each  key of  dictionary  with  for  loop
for keys in a:
	print(keys)
print('Values  of  dictionary') # Values  of  dictionary
#How  to  print  each  value  of  dictionary  with  for  loop
for values in a.values() :
	print(values)
print('All  the  tuples  of  dict_items   object') # All  the  tuples  of  dict_items   object
#How  to  print  each  tuple  of  dictionary  with  for  loop
for item in a.items():
	print(item)
print('Elements  of  each   tuple') # Elements  of  each   tuple
# How  to  print  elements  of  tuple   in  dictionary  with  for  loop
for key, value in a.items():
	print(f'Key:{key}, Value:{value}')
print('Keys  and  values  of  dictionary') # Keys  and  values  of  dictionary
#How  to  print  each  key of  dictionary  with  for  loop  along   with  corresponding  value
for keys in a.items():
	print(keys)