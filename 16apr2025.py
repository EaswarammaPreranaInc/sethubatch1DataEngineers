
#1. Find   outputs (Home  work)

'''
from  itertools  import  count
c = count()
print('While  loop') #While loop 
while   True:
        x = next(c) #yeilds 0 1 2 3 4 5 6 7 8 9 (10)
        if   x > 9:
                break
        print(x) # 0 1 2 3 4 5 6 7 8 9 
        
print('For  loop') # For  loop
for  x  in  count():
	if  x  >  20: #yeilds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 (21)
		break
	print(x) # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#end  of  for  loop

print('Element :  ' , end = '\t') #Element :  0
print(next(count())) 
c = count()
print(*c) 

'''


#2.Find  outputs (Home  work)

'''
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
#end  of  the  function
a = count(start = 10)
disp(a) #10 11 12 13 
b = count(start = 10 , step = 5)
disp(b) #10 15 20 25 
c = count(start = 10 , step = -2.5)
disp(c) #10 7.5 5.0 2.5 
d = count()
disp(d) # 0 1 2 3 

'''


#3. Find  outputs (Home  work)
'''
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While  loop') #While loop
while   True:
        try:
                print(next(z1)) #(10,0) (20,1) (15,2) (18,3) 
        except:
                break
            
z2 = zip(list , cnt)
print('for  loop') #for loop
for  x   in    z2:
        print(x) #(10,4) (20,5) (15,6) (18,7) 
        
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3)) #(10,8)
print('*z3 :  ' ,  *z3) # (20,9) (15,10) (18,11) 
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4)) # (10,12)

'''


#4. Find  outputs (Home  work)

'''
from   itertools    import    count
cnt = count() 
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop') #while loop 
while   True:
        try:
                print(next(z1)) #(0,10) (1,20) (2,15) (3,18) (4,SIE)
        except:
                break
            
z2 = zip(list , cnt)
print('for  loop') #for loop
for  x   in    z2:
        print(x) #(10,5) (20,6) (15,7) (18,8) (SIE)
        
z3 = zip(cnt , list)
print(next(z3)) #(9,10)

print(*z3) # (10,20) (11,15) (12,18) (13,SIE)

z4 = zip(list , cnt)
print(next(z4)) #(10,14)

'''

#5.Find  outputs  (Home  work)

'''
from  itertools  import  zip_longest
import   time
def  disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
list = [10 , 20 , 30 , 40]
z1  =  zip(range(7) , list)
print(type(z1)) #<class 'zip'>
disp(z1) # (0,10) (1,20) (2,30) (3,40)

z2 = zip_longest(range(7) , list)
print(type(z2)) #<class 'itertools.zip_longest'>
disp(z2) # (0,10) (1,20) (2,30) (3,40) (4,None) (5 None) (6,None)

'''

#6.Find  outputs  (Home  work)
'''
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c)) #<class 'itertools.cycle'>
while   True:
	print(next(c)) #10 20 30 40 10 20 30 40 
	time . sleep(1)
	
'''

#7. Find  outputs  (Home  work)
'''
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object') #1st  repeat  object
while   True:
	try:
		print(next(r)) #25 25 25 SIE
		time . sleep(1)
	except:
		break
print('2nd  repeat  object') #2nd  repeat  object
r  =  repeat('Hyd')
while   True:
	print(next(r)) #Hyd Hyd Hyd ------
	time . sleep(1)
	
'''

#8. Find  outputs  (Home  work)

'''
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m)) # 0 1 4 9 16 25 36 49 64 81
		time . sleep(1)
	except:
		break
		
'''


#9. Find  outputs (Home  work)
"""
import  time
def  disp(itr):
	while  True:
		try:
			print(next(itr))
			time . sleep(1)
		except:
			break
from  itertools  import  combinations,permutations
list = ['A' , 'B' , 'C' , 'D']
c = combinations(list , 3)
print('Different  Combinations') # Different  Combinations
disp(c)
'''
'''
('A' , 'B', 'C')
('A' , 'B', 'D')
('A' , 'C', 'D')
('B' , 'C', 'D')

'''

print('Different   Permutations') #Different   Permutations
p = permutations(list , 3)
disp(p)

'''
('A' , 'B', 'C')
('A' , 'B', 'D')
('A' , 'C', 'B')
('A' , 'C', 'D')
('A' , 'D', 'B')
('A' , 'D', 'C')

('B' , 'A', 'C')
('B' , 'A', 'D')
('B' , 'C', 'A')
('B' , 'C', 'D')
('B' , 'D', 'A')
('B' , 'D', 'C')

('C', 'A', 'B')
('C', 'A', 'D')
('C', 'B', 'A')
('C', 'B', 'A')
('C', 'D', 'A')
('C', 'D', 'B')

('D','A','B')
('D','A','C')
('D','B','A')
('D','B','C')
('D','C','A')
('D','C','B')


'''
"""