#Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator
a=eval(input("enter any list:"))
x=int(input("enter number you wanna search:"))
count=0
for i in range(len(a)):
    if x==a[i]:
        print("found at index", i)
        count+=1
        continue
print(f"{x} is found {count} times")
#average
try:
    sum = ctr = 0
    while (x := eval(input('Enter input (-1 to stop): '))) != -1:
        sum += x
        ctr += 1
    if ctr == 0:
        raise ZeroDivisionError  
    print('Average:', sum / ctr)
except ZeroDivisionError:
    print('Enter at least one input')
except (NameError, TypeError, SyntaxError):
    print('Input cannot be a string')
#Write  a  program  to  determine  largest  command  line  input
try:
        from sys import argv
        argv
        print(argv)
        a=[]
        for i in argv[1:]:
                b=eval(i)
                a.append(b)
        print("after evaluation and converting into list:",a)
        print("max int value:",max(a))
        print("max str value:",max(argv[1:]))
except TypeError:
        print("str and number cannot be compared together for max value")
except NameError:
        print("str needs to be in \"\" quotes, and within '' or ''' '''")
#Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number
try:
        from sys import argv
        argv
        for i in argv[1:]:
                a=eval(i)
                if a%2==0:
                        print("even number")
                else:
                        print("odd number")
except:
        print("Pls send an integer input")
#Write  a  program  to  determine  average  of  command  line  inputs
try:
        from sys import argv
        argv
        sum=0
        ctr=0
        for i in argv[1:]:
                a=eval(i)
                sum+=a
                ctr+=1
        print("average:",sum/ctr)
except:
        print("enter atleast one input and only int inputs")
#Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order
try:
    from sys import argv
    print("Original argv:", argv)
    a = []
    for i in argv[1:]:
        try:
            b = eval(i)  
            a.append(b)
        except:
            raise ValueError("Strings and numbers cannot be sorted together")
    print("After evaluation and converting into list:", a)
    s = sorted(a)  # Ascending sort
    a.sort(reverse=True)  # Descending sort
    print("Ascending sorting argv value:", s)
    print("Descending sort:", a)
except ValueError as e:
    print(e)
except Exception as e:
    print("An error occurred:", e)
