"""
# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)#{10,20}
print(type(c))#class set
d = a - b
print(d)#{10,20}
print(type(d))#class set
print(c  is  d)#False
print(c  ==  d)#True


# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10 , 20 , 50, 60}
print(type(c))#class set
d = a ^ b
print(d)#{10 , 20 , 50, 60}
print(type(d))#class set
print(c   is   d)#False
print(c  ==   d)#True


# Find  outputs  (Homework)
a = {x * x  for   x   in   range(10)}
print(a)#{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a))#class set


#Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

a= 'Rama rao'
a=a.upper()
a=set(a)
b="".join(a)
print(b)


#Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set


a= 'Rama rao'
a=a.upper()
a=set(a)
b=['A','E','I','O','U']
c=""
for x in a:
    if x in b:
        c+=x
print(c)

#Write  a  program  to  remove  duplicate  elements  of   list  using  set
a= [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
a=set(a)
a=list(a)
print(a)

#Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
a= [10 , 20 , 30 , 40 , 50 , 60]
b=[30 , 40 , 70 , 80 , 20]
a=set(a)
b=set(b)
c=a&b
c=list(c)
print(c)

#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])#How  to  print  value  25  in  dict  'a')
print(a['Ename'])#How  to  print  'Rama Rao'  in  dict  'a')
print(a['Sal'])#How  to  print  value  1000.65 in dict 'a')


# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['Sal']=2000#How  to  modify  1000.65  to  2000
a['Ename']='Sita'#How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno']= 35#How  to  modify  25   to  35
print(a)#{'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a))

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a['Gender']= 'M'#How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married']=True#How  to  append  'Married' :  True  to  dictionary 'a'
print(a)#{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}

# Find  outputs (Home  work)
a = { }
a[10] = 'Rama'#How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20]='Sita'#How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15] = 'Rajesh'#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18]= 'Kiran'#How  to  append  18 : 'Kiran'  to  dictionary 'a'
print(a)#{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
del a['Sal'] #How  to  remove  'Sal' : 1000.65  from  dictionary 'a'
print(a)#{'Empno': 25, 'Ename': 'Rama  Rao'}

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())#True
print(60  in  a . keys())##False
print(60  in  a . values())#True
print(30  in  a . values())##False
print(50  in  a)#True
print(20  in  a)#False
print(70  not  in  a . keys())#False
print(40  not  in  a . values())#False
print(25 not in a)#True

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)#'{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'
print(type(a))#class str
b = eval(a)
print(b)#{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b))#class dict


#  Find  outputs  (Homework)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)#{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)#False
print(a  ==  b)#True
c = a
print(a  is   c)#True
print(a==c)#True

#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)#{10, 14, 15, 18, 19, 20, 25}
print(type(d))#class set
e = {**a , **b , **c}
print(e)#{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))#class dict


#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b)#error
c = {**a , **b}
print(c)#{10: 60, 30: 50}
d =a|b
print(d)#{10: 60, 30: 50}

#Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries











# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))#3
b = {}
print(len(b))#0


#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))#90
print(sum(a . values()))#120
print(sum(a))#90
#print(sum(a.items()))#error

# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))#40
print(min(a . keys()))#7
print(max(a . values()))#50
print(min(a . values()))#5
print(max(a . items()))#(40, 5)
print(min(a . items()))#(7, 28)
print(max(a))#40
print(min(a))#7


#  dict()  function  demo program (Homework))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e))#error
f = [[10] , [20] , [30]]
#print(dict(f))#error
#print(dict([10 , 20]))#error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))#{10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h))#error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))#{(10, 20): 30, (40, 50): 60, (70, 80): 90}

#Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)
a = {10: 'A', 20: 'B', 15: 'C', 5: 'D', 12: 'E'}
b = sorted(a.items())#[(5, 'D'), (10, 'A'), (12, 'E'), (15, 'C'), (20, 'B')]
c=dict(b)
print(c)

#Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)
a = "RamA raO"
b= {}
for x in a.upper():
    if x.isalpha():
        b[x] = b.get(x, 0) + 1
c=dict(sorted(b.items()))
print("Enter a String:", a)
print("Alphabetical order:", c)


"""