#1
a=[10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
k=int(input("enter the number to be searched :"))#15
count=0
if k not  in a:
    print("not found")

else:
    for i in range(len(a)):
        if k==a[i]:
            print(k,'is found at index',i)
            count+=1
            continue
    print(k,"is found",count,"times")

#2
try:
	sum =  ctr = 0
	while  (x := eval(input('Enter input  (-1  to  stop)  :  '))) != -1:
		sum += x
		ctr +=1
	# End  of  while  loop
	print('Average :  ' ,  sum / ctr)
except  ZeroDivisionError:
	print('Enter  at  least   one  input')
except  (NameError , TypeError):
	print('Input  can  not  be string')

#3
import sys

try:
    a = sys.argv[1:]
    c=[]
    for i in a:
        b=eval(i)
        c.append(b)
    print("largest input",max(c))

except (NameError):
    print("input string have to be in single or triple codes")
except (TypeError):
    print("Inputs  can  not  be  number  and  string")
except ValueError:
    print("enter the at least 1 input")

#4
import sys
if len(sys.argv) == 1:
    print("Pls  send  an  integer  input")
else:
    try:
        if int(sys.argv[1]) % 2==0:
            print("even number")
        else:
            print("Odd number")
    except ValueError:
        print("enter  an integer input")

#5
import sys

args = sys.argv[1:]
numbers = []
try:
    for i in args:
        numbers.append(eval(i))
    k = sum(numbers) / len(numbers)
    print("average:",k)
except ZeroDivisionError:
    print("send atleast one input")
except (TypeError,NameError):
    print("don't enter string:")

#6
import sys

args = sys.argv[1:]  # Exclude script name

numbers = []
try:
    for i in args:
        numbers.append(eval(i))
    numbers.sort()
    print("assending order",numbers)
    numbers.sort(reverse = True)
    print("desending order",numbers)
except (ValueError,TypeError):
    print("enter the integer values")
