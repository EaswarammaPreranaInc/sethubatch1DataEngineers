a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

index = a.rfind('is')
while index != -1:
    print(index)
    index = a.rfind('is', 0, index)
print('End')
