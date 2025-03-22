#21/3/2025 

# 1.Find  outputs



def  change(b):
	b . append(25) #[10 , 20 , 15 , 18,25]
	b[2] = 17  #[10 , 20 , 17, 18,25]
	del  b[1] #[10,17,18,25]
	
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) #1. [10 , 20 , 15 , 18]
change(a)
print(a) #2. [10,17,18,25]



#2.Find  outputs


def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b) #2. [50 , 60 , 70 , 80]
	
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) #1. [10 , 20 , 30 , 40]
change(a)
print(a) #3. [10,20,30,40] 



#3.Find  outputs


def   f1(x):
	x = 20 
	print(x) #2. 20 
# End  of   the   function
x = 10
print(x) #1. 10
f1(x)
print(x) #3. 10



#4.Find  outputs


def  f1(b):
	#b[2] = 25 #error becz tuple is immutable
	pass
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) #1. (10,20 ,15 ,18)
f1(a)
print(a) #2. (10,20,15,18)

