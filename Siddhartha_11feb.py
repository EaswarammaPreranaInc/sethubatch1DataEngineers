# int object demo program
a = 25
print(a)        #class object 25
print(type(a))  #class <int>
print(id(a))    #ramdom id 1000


# complex object demo program
a = 3 + 4j
print(a)        #class object 3+4j
print(type(a))  #class <complex>
print(id(a))    #ramdom id 2000
print(a.real) #real
print(a.imag) #imag
print(type(a.real))  # class <float>
print(type(a.imag))  # class <float>


a = 6j
print(a)           #object 6j
print(type(a))     #class <complex>
print(a . real)    #real 0.0
print(a . imag)    #imag 6.0
#print(5 + j6)     #Error
#print(3 + 4i)     #Error
#print(4+j)        #Error
print(4+1j)        #4 + 1j
print(4+0j)        #4 + 0j


# bool object demo program
a = True
print(a)                      #object True
print(type(a))                #class <bool> 
print(id(a))                  #ramdom id 1000
b = False
print(b)                      #object False
print(type(b))                #class <bool>
print(True + True)            #1+1 = 2
print(True + False)           #1+0 = 1
print(False + True)           #0+1 = 1
print(False + False)          #0+0 = 0
print(True + True + True)     #1+1+1 = 3
print(25 + 10.8 + True)       #25+10.8+1 = 36.8
print(True > False)           #True
print(True)                   #True
print(False)                  #False
#print(true)                   #Error
#print(false)                  #Error
