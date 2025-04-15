# # a = '15:36:48'
# # print(a . split(':'))
# # print(a)
# # # #;;;output
# # # ['15', '36', '48']
# # # 15:36:48

# a= 'Hyd\nis green\tcity'
# print(a . split(' '))
# print(a . split())
# print(a . split('green'))
# #print(a . split(''))
# output
# # ['Hyd\nis', 'green\tcity']
# # ['Hyd', 'is', 'green', 'city']
# # ['Hyd\nis ', '\tcity'] 

# a = 'Hyd\tis\tgreen\tcity'  # There is a tab between the words

# print(a.split('\t'))  # ['Hyd', 'is', 'green', 'city']
# print(a.split())  # ['Hyd', 'is', 'green', 'city']
# print(a.split(' '))  # ['Hyd\tis\tgreen\tcity'] (no effect since there are no spaces)
# ''
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())
# print(a . split(' '))

op:

['Hyd', 'is', 'green', 'city']
''

a = 'www.gmail.com'

print(a.split('.'))  # ['www', 'gmail', 'com']
''
expression = '3+2+4+5+6+21+4+5+8+12'  # Input expression

numbers = expression.split('+')
sum_result = sum(map(int, numbers))

print(sum_result)  # Output: 70
