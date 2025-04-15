#search for an element in list without in operator
lst=[10,20,15,12,18,15,19,14,15,14]
x = 15
count = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(f'{x} is {i}')
        count += 1
if count>0:
    print(f'{x} is found {count}')
else:
    print(f'{x} is not found')           
'''o/p: 15 is 2
        15 is 5
        15 is 8
        15 is found 3''' 
#modify  prgm with walrus 
try:
    sum = ctr = 0
    while (x := eval(input('Enter input (-1 to stop): '))) != -1:
        sum += x
        ctr += 1
    print('Avg:', sum / ctr)
except ZeroDivisionError:
    print('At least one valid input is required.')
except (NameError, TypeError, SyntaxError):
    print('Input cannot be a string or invalid expression.')
        

#find the Largest cmd line input
import sys
try:
    if len(sys.argv)<2:
        print('Please send inputs:')
    else:
        a = [eval(i) for i in sys.argv[1:]]
        print('Largest input:',max(a))
except(ValueError,TypeError):
    print('Inputs cannot be mix of nos and strings')      

'''o/p: python 05_03_25_PracticePython.py 10 20 30.8 7 40 35.6
        Largest input: 40         '''


#check if cmd line input even or odd
import sys
try:
    if len(sys.argv)<2:
        print('Please send inputs:')
    else:
        n = int(sys.argv[1])
        print('Even no' if n%2==0 else 'odd no')
except ValueError:
    print('Please send integer:')

'''o/p:  py 05_03_25_PracticePython.py 60
         Even no         '''

#calculate avg of cmd line 
import sys
try:
    if len(sys.argv)<2:
        print('Please send no')
    else:
        a = [eval(i) for i in sys.argv[1:]]    
        print('Avg',sum(a)/len(a))
except (ValueError,TypeError):
    print('Please send no input:')        

'''o/p:  py 05_03_25_PracticePython.py 10.8 25 True 14.6 19 False 7.4
         Avg 11.114285714285716       '''

