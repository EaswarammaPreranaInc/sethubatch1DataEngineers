try:
    a = int(input('Enter month number (1 - 12): '))

    if a == 1:
        print('January')
    else:
        if a == 2:
            print('February')
        else:
            if a == 3:
                print('March')
            else:
                if a == 4:
                    print('April')
                else:
                    if a == 5:
                        print('May')
                    else:
                        if a == 6:
                            print('June')
                        else:
                            if a == 7:
                                print('July')
                            else:
                                if a == 8:
                                    print('August')
                                else:
                                    if a == 9:
                                        print('September')
                                    else:
                                        if a == 10:
                                            print('October')
                                        else:
                                            if a == 11:
                                                print('November')
                                            else:
                                                if a == 12:
                                                    print('December')
                                                else:
                                                    print('Input should be between 1 and 12')

except ValueError:
    print('Input should be an integer')
