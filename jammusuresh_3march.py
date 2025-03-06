#swaping of two numbers
x=float(input('enter the first number:'))
y=float(input('enter the second number:'))
print('before swaping')
print(f'x={x},y={y}')
x=x*y
y=x/y
x=x/y
print('after swaping')
print(f'x={x},y={y}')

#input=4
#input=5
/*output:
before swaping
x=4.0,y=5.0
after swaping
x=5.0,y=4.0 */


# How  to  print  each  element  and  the  corresponding  index
a = [25, 10.8, 'Hyd', True]
print('Indexed for loop')
for i in range(len(a)):
  print(f'Index: {i}, Element: {a[i]}')


/*out put

 Indexed for loop
Index: 0, Element: 25
Index: 1, Element: 10.8
Index: 2, Element: Hyd
Index: 3, Element: True*/



#Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

a=eval(input('enter the 1st list:'))
b= eval(input('enter the 2nd list:'))
c=[]
for i in range(len(a)):
    c.append(a[i] + b[i]) 
print('3rd list:', c)


#input
#1st  list  --->  [10 , 20 , 15 , 18]

#2nd  list  --->  [30 , 40 , 35 , 12]

#output
#enter the 1st list:10,20,15,18
#enter the 2nd list:30,40,35,12
#3rd list: [40, 60, 50, 30]



#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
for i in range(2,5):
 print(a[i])


print('For each loop')
for i, element in enumerate(a): 
    if 2 <= i <= 4: 
        print(element)

#output
#Indexed for loop
#Hyd
#True
#(3+4j)

#Write  a  program  to  print  first  20  even  numbers  with  while  loop
i=1
even_number=2
while i <= 20:
   print(even_number)
   even_number += 2  
   i += 1 
print("bye")


#output
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
bye


#Write  a  program  to  print  first  20  even  numbers  with  while  loop
i=1
odd_number=1
while i <= 20:
   print(odd_number)
   odd_number += 2  
   i += 1
print("bye")

#output
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
bye

