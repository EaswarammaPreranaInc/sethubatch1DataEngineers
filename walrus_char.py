a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)

print('End')
