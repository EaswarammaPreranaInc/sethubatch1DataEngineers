'''
4/3/2025

1.Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

'''

'''
a=eval(input("Enter the List:"))
e=eval(input("Entee the element need to be search in the list:"))
    
for i in range(len(a)):
    if a[i]==e :
        print(F"Found  at  index {i}")
        break
            
else:
    print("Not  found")

'''

'''
2.Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  46 , 34.8 , False , 95 , -1

sum = 0 + 25 + 10.8 + True + 46 + 34.8 + False + 95

ctr = 0  + 1 + 1 + 1 + 1 + 1 + 1 + 1
'''

'''
sum=c=0 

try:
    while(True):
        e=eval(input("Enter input  (-1  to  stop)  :"))
        if(e==-1):
            break 
        
        sum+=(e)
        c+=1 
        
        
    print("Average :",sum/c)
    
except:
    print("Don't enter sequence None complex")
    
'''