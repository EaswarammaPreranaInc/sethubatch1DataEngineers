
'''
Repeat  prog6a  with  next()  function.

Import  and  use  class  c1  defined  in  prog6a  but   donot  rewrite  class  c1  again
'''
from april17 import c1
a=c1()
while True:
    try:
        print(next(a))
    except:
        break

  
