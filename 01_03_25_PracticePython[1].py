
#using if and else write prgm on months
try:
    a = int(input('Enter 1 to 12 : '))
    if a==1:
        print('January')
    else:
        if a==2:
            print('February')
        else:
            if a==3:
                print('March')
            else:
                if a==4:
                    print('April')
                else:
                    if a==5:
                        print('May')
                    else:
                        if a==6:
                            print('June')
                        else:
                            if a==7:
                                print('july')
                            else:
                                if a==8:
                                    print('August')
                                else:
                                    if a==9:
                                        print('September')
                                    else:
                                        if a==10:
                                            print('October')
                                        else:
                                            if a==11:
                                                print('November')
                                            else:
                                                if a==12:
                                                    print('December')
                                                else:
                                                    print('Enter from 1-12')    
except:
    print('Enter an integer no:')                                                    

'''o/p: Enter 1 to 12 : 6
        June
        1 1
        1 2
        1 3
        1 4
        Hello
        2 1
        2 2
        2 3
        2 4
        Hello
        3 1
        3 2
        3 3
        3 4
        Hello
        Bye'''
#printing each element using for loop
for x in [10,20,15,18]:
    print(x)
print()

for x in 'Hyd':
    print(x)
print()

for x in range(5):
    print(x)
'''o/p :10
        20
        15
        18

        H
        y
        d

        0
        1
        2
        3
        4   '''    

#nested loop
for i in range(1,4):
    for j in range(1,5):
        print(i,j)
    print('Hello')
print('Bye')        
'''o/p: 1 1
        1 2
        1 3
        1 4
        Hello
        2 1
        2 2
        2 3
        2 4
        Hello
        3 1
        3 2
        3 3
        3 4
        Hello
        Bye  '''