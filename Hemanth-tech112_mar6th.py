# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')  # True
print('day'   in   'Sankar  dayal  sarma')  # True
print('Green'   in   'Hyd  is  green  city')  # False
print('d  is'   in   'Hyd  is  green  city')  # True
print('dis'   in   'Hyd  is  green  city')  # False
print('iniv'   in   'Srinivas')  # True
print('iniv'   not   in 'Srinivas')  # False

''' Output
True
True
False
True
False
True
False
'''


'''  (Homework)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a       m       a                R       a       o
-8    -7      -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])  # a[0:7:2] --> String from indexes 0 to 6 in steps of 2 i.e. Rm a
print(a [ : 7])  # a[0:7:1] --> String from indexes 0 to 6 in steps of 1 i.e. Rama Ra
print(a [2 : 4])  # a[2:4:1] --> String from indexes 2 to 3 in steps of 1 i.e. ma
print(a [2 : ])  # a[2:8:1] --> String from indexes 2 to 7 in steps of 1 i.e. ma Rao
print(a [ : 4 ])  # a[0:4:1] --> String from indexes 0 to 3 in steps of 1 i.e. Rama
print(a [ : : 2])  # a[0:8:2] --> String from indexes 0 to 7 in steps of 2 i.e. Rm a
print(a [-6 : -1])  # a[-6:-1:1] --> String from indexes -6 to -2 in steps of 1 i.e. ma Ra
print(a [-6 : ])  # a[-6:0:1] --> String from indexes -6 to -1 in steps of 1 i.e. ma Rao
print(a [: -4 : -1])  # a[-1:-4:-1] --> String from indexes -1 to -3 in steps of -1 i.e. oaR
print(a [-3 : -1])  # a[-3:-1:1] --> String from indexes -3 to -2 in steps of 1 i.e. Ra
print(a [-3 : ])  # a[-3:0:1]  --> String from indexes -3 to -1 in steps of 1 i.e. Rao
print(a [ : : ])  # a[0:8:1] --> String from indexes 0 to 7 in steps of 1 i.e. Rama Rao
print(a [ : ])  # a[0:8:1] --> String from indexes 0 to 7 in steps of 1 i.e. Rama Rao
print(a [ : : -1])  # a[-1:-9:-1] --> String from indexes -1 to -8 in steps of -1 i.e. oaR amaR
print(a [ : : -2]) # a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])  # a[-2:-9:-2] --> String from indexes -2 to -8 in steps of -2 i.e. a mR
print(a [2 : 8])  # a[2:8:1] --> String from indexes 2 to 7 in steps of 1 i.e. ma Rao
print(a [2 : 8 : -1])  # a[2:8:-1] --> x<=y --> 2<=8 --> result is empty string
print(a [ : -6 : -1])  # a[-1:-6:-1] --> String from indexes -1 to -5 in steps of -1 i.e. oaR a
print(a [2 : -3])  # a[2:-3:1] --> String from indexes 2 to -4 in steps of 1 i.e. ma 
print(a [1 : 6 : 2])  # a[1:6:2] --> String from indexes 1 to 5 in steps of 2 i.e. aaR
print(a [ : -5 : -5])  # a[-1:-5:-5] --> String from indexes -1 to -4 in steps of -5 i.e. o
print(a [2 : -5])  # a[2:-5:1] --> String from indexes 2 to -6 in steps of 1 i.e. m
print(a [2 : -5 : 2])  # a[2:-5:2] --> String from indexes 2 to -6 in steps of -2 i.e. m 
print(a [ -1: 0 : -1])  # a[-1:0:-1] --> String from indexes -1 to 1 in steps of -1 i.e. oaR ama
print(a [-5 : 0 : -2]) # a[-5:0:-2] --> String from indexes -5 to 1 in steps of -2 i.e. aa

''' Output
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
'''


'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint: Use slice
'''
try:
    a=eval(input('Enter a input string : '))
    b=eval(input('Enter a input string2 : '))
    c=b[:2]+a[2:]
    d=a[:2]+b[2:]
    print(c,d,sep=" ")
except:
    print('Input string should contains must be equal or more than four characters. ')



'''  Sample output
Enter a input string : 'Java'
Enter a input string2 : 'Python'
Pyva Jathon
'''



'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
								                  Character  at  index  1  :  A
								                  Character  at  index  2  :  M
							                      Character  at  index  3  :  S
								                  Character  at  index  4  :  I

								                  Character  at  index  -1  :  I
								                  Character  at  index  -2  :  S
								                  Character  at  index  -3  :  M
								                  Character  at  index  -4  :  A
								                  Character  at  index  -5  :  V

Hint:  Use  two for loops
'''
try:
    a=eval(input('Enter a string : '))
    for i in range(len(a)):
        print(f'Character at index {i}: {a[i]}')
    print()
    for i in range(len(a)):
        print(f'Character at index {-(i+1)}: {a[-(i+1)]}')
except:
    print('Input string should be in quotes')


''' Sample Output
Enter a string : 'VAMSI'
Character at index 0: V
Character at index 1: A
Character at index 2: M
Character at index 3: S
Character at index 4: I

Character at index -1: I
Character at index -2: S
Character at index -3: M
Character at index -4: A
Character at index -5: V
'''



'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object

3) Hint: Use  single for loop
'''
try:
    a=eval(input('Enter a input : '))
    odd=''
    even=''
    for i in range(len(a)):
        if i%2==0:
            even+=a[i]
        else:
            odd+=a[i]
    print('Characters at even indexes :',even)
    print('Characters at odd indexes :',odd)
except:
    print('Input string should be in quotes')
    
''' Sample output
Enter a input : 'Rama Rao'
Characters at even indexes : Rm a
Characters at odd indexes : aaRo
'''


'''
Let  input  be    A   4   B   3   C   2   $   5
                          0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  --->  'AAAA'

2) Iteration    i        a[i]       a[i + 1]          out
   -------------------------------------------------------------------------------------------------
                                                                 ''
            1         0        'A'          '4'             '' + 'A' * 4 = 'AAAA'
            2        2        'B'           '3'             'AAAA' + 'B' * 3  = 'AAAABBB'
            3        4        'C'           '2'             'AAAABBB' + 'C' * 2 = 'AAAABBBCC'
            4        6        '$'           '5'             'AAAABBBCC' + '$' * 5 = 'AAAABBBCC$$$$$'
----------------------------------------------------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  ---> a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char of string
'''
try:
    a=eval(input('Enter the input : '))  # 'A4B3C2$5'
    result=''
    for i in range(0,len(a),2):
        first=a[i]
        second=int(a[i+1])
        result+= first * second
    print(result)  #  AAAABBBCC$$$$$
except:
    print('Input should be alternate char and number')

'''
Enter the input : 'A4B3C2$5'
AAAABBBCC$$$$$

Enter the input : '$5P2K3Z4'
$$$$$PPKKKZZZZ

Enter the input : 'Hyd'
Input should be alternate char and number
'''


