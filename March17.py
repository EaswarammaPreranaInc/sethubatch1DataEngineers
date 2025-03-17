#difference() method demo program
a={10,20,30,40}
b={30,40,50,60}
c=a.difference(b) 
print(c)         #{10,20}
print(type(c))   #<class 'set'>
d=a-b
print(d)         #{10,20}
print(type(d))   #<class 'set'>
print(c is d)    #False
print(c==d)      #True



#symmetric_difference() method demo program
a={10,20,30,40}
b={30,40,50,60}
c=a.symmetric_difference(b) 
print(c)    #{10,50,20,60}
print(type(c)) #<class 'set'>
d=a^b
print(d)    #{10,50,20,60}
print(type(d)) #<class 'set'>
print(c is d) #False
print(c==d)   #True



#Find outputs
a={x*x for x in range(10)}
print(a)  #{0,1,64,4,16,25,49,36,81,9}       
print(type(a)) #<class 'set'>



#remove duplicate characters of the string using set
a=input('Enter a string: ')
b=set(a)
print(''.join(b))  

#Output
Enter a string: Rama rAo
om rARa



#remove duplicate elements of list using set
a=eval(input('Enter any list: '))
b=set(a)
print(list(b)) 

#Output
Enter any list: [False,25,10.8,1,25,0,'Hyd',10.8,1.0,None,'Sec','Hyd',True]
[False, 1, None, 10.8, 'Hyd', 25, 'Sec']



#program to obtain common elements between two lists using sets
a=eval(input('Enter 1st list: '))
b=eval(input('Enter 2nd list: '))
print(list(set(a) & set(b)))

#Output
Enter 1st list: [10,20,30,40,50]
Enter 2nd list: [30,20,70,40]
[40, 20, 30]



#How to access vallues of dictionary
a={'Empno':25, 'Ename':'Rama Rao', 'Sal':1000.65}
print(a['Empno'])  #How to print value 25 in dict 'a'
print(a['Ename'])  #How to print value 'Rama Rao' in dict 'a'
print(a['Sal'])    #How to print value 1000.65 in dict 'a'



#How to modify values of dictionary
a={'Empno':25, 'Ename':'Rama Rao', 'Sal':1000.65}
print(a)   #{'Empno':25, 'Ename':'Rama Rao', 'Sal':1000.65}
print(id(a)) #Address of dict 'a'
a['Sal']=2000   #How to modify 1000.65 to 2000
a['Ename']='Sita' #How to modify 'Rama Rao' to 'Sita'
a['Empno']=35     #How to modify 25 to 35
print(a)    #{'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}



#How to append key:value pairs to dictionary
a={'Empno':25, 'Ename':'Rama Rao', 'Sal':1000.65}
print(a)
a['Gender']='M'    #How to append 'Gender': 'M to dict 'a'
a['Married']=True  #How to append 'Married': True to dict 'a'
print(a) #{'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}



#Find outputs
a={}
a[10]='Rama'
a[20]='Sita'
a[15]='Rajesh'
a[18]='Kiran'
print(a)  #{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}



#How to remove key:value pairs of dict
a={'Empno':25, 'Ename':'Rama Rao', 'Sal':1000.65}
print(a) #{'Empno':25, 'Ename':'Rama Rao', 'Sal':1000.65}
a.pop('Sal')
print(a) #{'Empno': 25, 'Ename': 'Rama Rao'}



#in and not in operators
a={10:20,30:40,50:60,70:80}
print(30 in a.keys())  #True
print(60 in a.keys())  #False
print(60 in a.values()) #True
print(30 in a.values())#False
print(50 in a)         #True
print(20 in a)         #False
print(70 not in a.keys())#True
print(40 not in a.values())#True
print(25 not in a)      #True



# What are the outputs if input is {10:'A',20:'B',15:'C',20:'D'}
a=input('Enter dictionary: ')
print(a)  #{10:'A',20:'B',15:'C',20:'D'}
print(type(a)) #<class 'str'>
b=eval(a)
print(b)  #{10:'A', 20:'D', 15:'C'}
print(type(b)) #<class 'dict'>



#Find outputs 
a={10:'Rama', 20:'Sita', 15:'Rajesh', 18:'Kiran'}
b={**a}
print(b)       #{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a is b)  #False
print(a==b)    #True
c=a
print(a is c)  #True
print(a==c)    #True



#Find outputs
a={10 : 'Rama', 20 : 'Sita', 15 : 'Rajesh'}
b={18 : 'Kiran', 14 : 'Amar', 20  : 'Manohar'}
c={25 : 'Ramesh', 19 : 'Krishna', 15 : 'Radha', 14 : 'Srinivas'}
d={*a, *b, *c}
print(d)   #{10, 14, 15, 18, 19, 20, 25}
print(type(d)) #<class 'set'>
e={**a, **b, **c}
print(e)   #{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) #<class 'dict'>



#Find outputs 
a={10 : 20, 30 : 40}
b={30 : 50, 10 : 60}
#print(a+b)
c={**a, **b}
print(c)  #{10: 60, 30: 50}
d=a|b
print(d)  #{10: 60, 30: 50}



#create a dictionary with emp names and salaries
n=int(input('How many Employees: '))
d={}
for i in range(n):
	a=input('Enter Emp Name: ')
	b=float(input('Enter Salary: '))
	d[a]=b
print(d)

#Output
How many Employees: 4
Enter Emp Name: AAA
Enter Salary: 10000
Enter Emp Name: BBB
Enter Salary: 20000
Enter Emp Name: CCC
Enter Salary: 15000
Enter Emp Name: DDD
Enter Salary: 18000
{'AAA': 10000.0, 'BBB': 20000.0, 'CCC': 15000.0, 'DDD': 18000.0}



#convert a string to dictionary
a=input('Enter a string with = and ,: ')
b=a.split(',')
res={}
for i in b:
	x=i.split('=')
	res[x[0]]=x[1]
print(res)

#Output
{'Emp no': '25', ' Emp name': 'Rama Rao', ' sal': '10000.0', ' gender': 'm'}



#len() function demo program  
a={'Empno':25,'Ename':'Rama Rao','Sal':1000.65}
print(len(a))  #3
b={}
print(len(b))  #0



#sum() function demo program 
a={10:20,30:40,50:60}
print(sum(a.keys()))    #90
print(sum(a.values()))  #120
print(sum(a))           #90
print(sum(a.items()))   #Error



#max() and min() functions demo program 
a={10:20,30:25,40:5,7:28,9:50}
print(max(a.keys()))   #40
print(min(a.keys()))   #7
print(max(a.values())) #50
print(min(a.values())) #5
print(max(a.items()))  #(40,5)
print(min(a.items()))  #(7,28)
print(max(a))          #40
print(min(a))          #7



#dict() function demo program 
a=[(10,'Hyd'),(20,'Sec'),(15,'Cyb'),(20,'Pune')]  #  List of  tuples
b= dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #{10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c= (['R','Red'],['G','Green'], ['B','Blue'], ['G','Gray'])
d= dict(c)
print(d)  #{'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e=[[10,20,30],[40,50,60], [70,80,90]]
print(dict(e))  #Error
f=[[10],[20],[30]]
#print(dict(f))
print(dict([10,20]))  #Error
g=[[10,[20,30]],[40,[50,60]],[70,[80,90]]]
print(dict(g)) #{10: [20, 30], 40: [50, 60], 70: [80, 90]}
h=[[[10,20],30],[[40,50],60],[[70,80],90]]
print(dict(h))  #Error
i=[[(10,20),30],[(40,50),60],[(70,80),90]]
print(dict(i))   #{(10, 20): 30, (40, 50): 60, (70, 80): 90}



#sorted()  function  (Home  work)
a={10:'Red',20:'Green',15:'Blue',18:'Yellow',5:'White'}
b=sorted(a.keys())
print(b)   #[5, 10, 15, 18, 20]
c=sorted(a.values())
print(c)   #['Blue', 'Green', 'Red', 'White', 'Yellow']
d=sorted(a.items())
print(d)   #[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f=sorted(a,reverse=True)
print(f)   #[20, 18, 15, 10, 5]
print(a)   #{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}



#sort dictionary wrt keys
a=eval(input('Enter dicyionary:')) #{10:'A', 20:'B', 15:'C', 5:'D', 12 'E'}
b=sorted(a.items())
print(dict(b))  #{5:'D', 10:'A', 12:'E', 15:'C', 20:'B'}



#keys() method demo program
a={10:'Hyd', 20:'Sec', 15:'Cyb', 18:'Pune'}
b=a.keys() 
print(b)   #[10,20,15,18]
print(type(b)) #<class 'dict'>
for x in b:
	print(x) #10<next line>20<next line>15<next line>18



#values() method demo program
a={10:'Hyd', 20:'Sec', 15:'Cyb', 18:'Pune'}
b=a.values()
print(b)    #dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b)) #<class 'dict_values'>
for x in b:
	print(x) #Hyd<next line>Sec<next line>Cyb<next line>Pune



#items() method demo program
a={10:'Hyd', 20:'Sec', 15:'Cyb', 18:'Pune'}
b=a.items()
print(b)  #dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) #<class  'dict_items'>
for x in b:
	print(x) #(10,'Hyd')<next line>(20,Sec)<next line>(15,'Cyb')<next line>(18,'Pune')
for x,y in b:
	print(x,y,sep='...') #10...Hyd<next line>20...Sec<next line>15...Cyb<next line>18...Pune



#Find outputs
a={10:'Hyd', 20:'Sec', 15:'Cyb', 18:'Pune'}
for x,y in a.items():
	print(x,y,sep='...') #10...Hyd<next line>20...Sec<next line>15...Cyb<next line>18...Pune
for x,y in a.keys():
	print(x,y,sep='...') #Error
for x,y in a.values():
	print(x,y,sep='...') #Error
for x,y in a:            #Error
	print(x,y,sep='...')



#clear() method demo program
a={10:20,30:40,50:60}
print(a) #{10: 20, 30: 40, 50: 60}
a.clear() 
print(a)  #{}
del a
print(a)  #Error



#copy() method demo program 
a={'R':'Red', 'G':'Green', 'B':'Blue'}
b=a.copy()
print(b) #{'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a is b) #False
print(a==b)   #True



#Find outputs 
a={10:'Rama', 20:'Sita', 15:'Rajesh'}
x,y,z=a.keys()
print(x)#10
print(y)#20
print(z)#15
print()#<next line>
x,y,z=a.values()
print(x)#Rama
print(y)#Sita
print(z)#Rajesh
print() #new line
x,y,z=a.items()
print(x)#(10,'Rama')
print(y)#(20,'Sita')
print(z)#(15,'Rajesh')
print()#new line
(rno1,sname1),(rno2,sname2),(rno3,sname3)=a.items()
print(rno1,sname1) #10 'Rama'
print(rno2,sname2) #20 'Sita'
print(rno3,sname3) #15 'Rajesh'



#determine frequency of each alphabet in the string in alphabetical order
a=input('Enter mixed case string: ')
a=a.upper()
d={}
for i in range(len(a)):
	if a[i].isalpha():
		x=d.get(a[i],0)+1
		d[a[i]]=x
print(d)

#Output
Enter mixed case string: Rama Rao
{'R': 2, 'A': 3, 'M': 1, 'O': 1}



#Find outputs 
a=[('R','Red'), ('G','Green'), ('B','Blue')]
b={'Y':'Yellow','G':'Gray'}
b.update(a)
print(b)  #{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a.update(b) #Error



#Find  outputs  (Home  work)
a=[(10, 20, 30), (40, 50, 60), (70, 80, 90)]
b={}
b.update(a)
print(b) #Error
c=[(10,), (20,), (30,)]
b.update(c) #Error
print(b)



#Find outputs 
d={x:x**3 for x in range(5)}
print(d) #{0:0,1:1,2:8,3:27,4:64}
print(type(d)) #<class 'dict'>



#Find outputs 
d={x:2*x for x in range(5)}
print(d) #{0:0, 1:2, 2:4, 3:6, 4:8}



#Find outputs 
a={10:'Rama', 15:'Sita', 18:'Rajesh', 17:'Kiran', 12:'Rama Rao'}
b={k:v for k,v in a.items() if k%2!=0}
print(b) #{15:'Sita', 17:'KKiran'}
c={k:a[k] for k in a if a[k].startswith('R')}
print(c) #{10:'Rama', 18:'Rajesh', 12:'Rama Rao'}