'''print( 'green'   in   'Hyd  is  green  city') 
print('day'   in   'Sankar  dayal  sarma') 
print('Green'   in   'Hyd  is  green  city')
print('d  is'   in   'Hyd  is  green  city') 
print('dis'   in   'Hyd  is  green  city') 
print('iniv'   in   'Srinivas') 
print('iniv'   not   in   'Srinivas')

#progrm to find outputs
a = 'Rama Rao'
print(a [ : 7 : 2]) 
print(a [ : 7])
print(a [2 : 4])
print(a [2 : ])
print(a [ : 4 ])
print(a [ : : 2])
print(a [-6 : -1])
print(a [-6 : ])
print(a [: -4 : -1])
print(a [-3 : -1])
print(a [-3 : ])
print(a [ : : ])
print(a [ : ])
print(a [ : : -1])
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])
print(a [2 : 8])
print(a [2 : 8 : -1])
print(a [ : -6 : -1])
print(a [2 : -3])
print(a [1 : 6 : 2])
print(a [ : -5 : -5])
print(a [2 : -5])
print(a [2 : -5 : 2])
print(a [ : 0 : -1])
print(a [-5 : 0 : -2])


outputs---
Rm a
Rama Ra
ma
ma Rao
Rama
Rm a
ma Ra
ma Rao
oaR
Ra
Rao
Rama Rao
Rama Rao
oaR amaR
oRaa
a mR
ma Rao

oaR a
ma
aaR
o
m
m
oaR ama
aa


Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

code-->
a=eval(input('enter first string:'))#java
b=eval(input('enter second string:'))#python
c=(b[0:2]+a[2:])
d=(a[0:2]+b[2:])#jathon
print(F'{c} {d}')

outputs----
enter first string:'java'
enter second string:'python'
pyva jathon


Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

prog-->

a=eval(input('enter any string:'))#python
b=len(a)
if b>=4:

    print(a[0:2]+a[-2]+a[-1])
else:
	 print('nothing')


outputs---	
enter any string:'python'
pyon

Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

program--->
a=eval(input('enter a string:'))
b=""
b=a[::-1]
for i in range(0,len(a)):

  
     print(f'character at index {i}:{a[i]}')
 

print('\n')
for i in range(-1,-len(b)-1,-1):
	 
     print(f'character at index {i}:{b[-i-1]}')


outputs----
enter a string:'vamsi'
character at index 0:v
character at index 1:a
character at index 2:m
character at index 3:s
character at index 4:i


character at index -1:i
character at index -2:s
character at index -3:m
character at index -4:a
character at index -5:v
     
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
prog-->
a='Rama Rao'
b=""
c=""
for i in range(0,len(a)):

	  if i%2==0:
		     b+=a[i]
	  else:
		  c+=a[i]

		     
print(f'even:{b} \n odd:{c}')
output-----
even:Rm a
 odd:aaRo


#Let  input  be    A   4   B   3   C   2   $   5
                  0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  --->  'AAAA'

2) Iteration    i        a[i]       a[i + 1]          out
   -------------------------------------------------------------------------------------------------
                                                                 ''
            1         0        'A'          '4'             '' + 'A' * 4 = 'AAAA'
            2        2        'B'           '3'             'AAAA' + 'B' * 3  = 'AAAABBB'
            3        4        'C'           '2'             'AAAABBB' + 'C' * 2 = 'AAAABBBCC'
            4        6        '$'           '5'             'AAAABBBCC' + '$' * 5 = 'AAAABBBCC$$$$$
 
 
a=eval(input('Enter  any  string  with  alternate  character  and  digit :'))
b=""
for i in range(0,len(a),2):
	b+=a[i]*int(a[i+1])		 
print(f'{b} ')


output----
Enter  any  string  with  alternate  character  and  digit :'$5A4B3C2D1'
$$$$$AAAABBBCCD'''
		  


		  
	      
		  

	 
	  
	  
	       

		 
		      


		 
	 
