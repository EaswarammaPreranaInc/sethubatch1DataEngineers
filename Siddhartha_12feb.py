a = 0O6247
print(a)       #object 3239
print(type(a)) #class <int>
print(id(a))   #ramdom id 1000
b = 0o6247
print(id(b))   #same id
print(b)       #3239
c = 3239
print(c)      #3239
print(id(c))  #same id
#print(0o9248) #Error invalid digit 9


a = 0XA7B9     
print(a)          #object 42937
print(type(a))    #class <int>
b = 0xBEEF
print(b)          #48879
#print(A7B9)       #Error
print('A7B9')     #A7B9
#print(0XBEER)     #Error
#print(0XHYD)      #Error
#print(0xA7G9B)    #Error

a = 9248
print(a)           #9248
print(type(a))     #class <int>


a = "Rama Rao"
print(a)           #class object Rama Rao
print(type(a))     #class <str>
print(id(a))       #ramdom id 1000
b = 'Hyd'
print(b)           #object Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)           #object


a = 'Hyd'
print(a[0])     #H
print(a[1])     #y
print(a[2])     #d
#print(a[3])    #Error   
print(a[-1])    #d
print(a[-2])    #y
print(a[-3])    #H
#print(a[-4])    #Error
print(a[0] ==  a[-3])    #True
#a[2] = 'c'               #Error
#print(25[0])             #Error nonsequence are not indexes
print('25'[0])           # 2
#print(True[1])           #Error nonsequence are not indexes
print('True'[1])         # r


a = 'Hyd'
print(a * 3)      #HydHydHyd
print(a * 2)      #HydHyd
print(a * 1)      #Hyd
print(a * 0)      #Empty str
print(a * -1)     #Empty str
print(25 * 3)     #75
print('25' * 3)   #252525
#print('25' * 4.0) #Error
print(3*'Hyd')  #HydHydHyd


print(len('Hyd'))       #3
print(len('Rama Rao'))  #8
print(len('9247'))      #4
print(len(''))          #0
print(len(' '))         #1
#print(len(689))         #Error

a = """"Hyd"""
print(a)              #"Hyd
print(len(a))         #4
print(a[0])           #"  
#print("""Hyd"""")     #Error
b = """""Hyd"""       
print(b)              #""Hyd
print(len(b))         #5 


a = 'Sankar Dayal Sarma'
print(a[7 : 12])   #a[7 :12 : 1] ---> string from indexes 7 to 11 in steps of 1 ----Dayal
print(a[7 : ])     #a[7 : 18 : 1]---> string from indexes 7 to 17 in steps of 1 ---->Dayal Sarma
print(a[ : 6])     #a[0 : 6 : 1]----> string from indexes 0 to 5 in steps of 1 ----->Sankar
print(a[ : ]) #   a[ 0 :  18 :  1]  --->  string  from  indexes  0  to   17  in  steps  of   1   ---> Sankar  Dayal  Sarma
print(a[:  : ])   #a[0 : 18 : 1]-----> string from indexes 0 to 17 in steps of 1 -----> Sankar Dayal Sarma
print(a[1 : 10 : 2]) #a string from indexes 1 to 9 in steps of 2 ------>  akrDy
print(a[0 : : 2])   #[0 : 18 : 2]-----> string from indexes 0 to 17 in steps of 2 ----->  Sna aa am
print(a[1 : : 2])   #[1 : 18 : 2]------>string from indexes 1 to 17 in steps of 2 ------> akrDylSra
print(a[-5 : -1])   #[-5 :-1 : 1]------->string from -5 to -2 in steps of 1-------> Sarm
print(a[::-1])  #  a[-1 : -19 : -1]  --->  string  from  indexes  1-  to   18  in  steps  of   -1   ---> Reverse string 
print(a[-1:-5:-1]) #------> string from -1 to -4 in steps of -1 -------> amra
print(a[ : : -2])  #[-1 : 18 : -2]----> string from indexes -1 to 19 in steps of -2 ---->   arSlyDrka
print(a[3 : -3])   #[3: -3 : 1]----->string from indexes 3 to -4 in steps of 1------->  karDayalSa
print(a[2 : -5])   #  a[2 : -5 :  1]  --->  string  from  indexes  2  to  -6   in  steps  of   1   --->  nkar<space>Dayal<space>
print(a[-1:-5])    #empty str  
print(a[3 : 3])    #empty str 


'''
 
      0       1       2       3       4       5       6        7        8        9      10      11      12       13      14       15       16       17
      S       a       n       k       a       r                D        a        y       a       l                S       a        r        m        a
      

  Conversion of Octal to Decimal equalent:

   512    64    8    1  --> weights

    6      2    4    7 --->6*512 + 2*64 + 4*8 + 7*1 =  3239

  Conversion of HexaDecimal to Decimal equalent:

   4096      256     16    1--->weights

    10        7      11    9---->10*4096 + 7*256 + 11*16 + 9*1 =  42937

	11        14      14   15---->11*4096 + 14*256 + 14*16 + 15*1 =  48879


'''


