#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)
f1(a = 40 , b = 50 , c = 60)
f1(c = 100 , b = 90 , a = 80)
#f1(70 , 80 , c = 90)
#f1(70 , 80 , 90)
#f1(c = 15 , b = 25 , 35)
#output
a  :  10          b :  20         c  :  30
a  :  40          b :  50         c  :  60
a  :  80          b :  90         c  :  100

#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)
#f1(a = 30 ,  b = 40
#f1(50 , b = 60)
#f1(a = 70 , 80)
#output
a  :  10   b  :  20

a  :  10          b  :  20
