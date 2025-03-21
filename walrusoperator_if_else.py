# a = 0
# if  a == 0:  
# 	print('Hyd')  
# else:
# 	print('Sec')
# if  b := 0: 
# 	print('Hyd')
# else:
# 	print('Sec : ' , b)  
# # if  c = 0: #(bro wrong interptation done by you) After walrus operator no if condition  condition
# #syntax error 
# if  c == 0:
# 	print('Hyd')
# else:
# 	print('Sec')
'''walrus assignment operator'''
# b = 10
# a = b += 5  # incorrect assignment 
# print(a)
b = 10
b += 5  # Correct way to update b
a = b   # Assign the updated value of b to a
print(a)
