program1:
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) #[10,20,15,18]
change(a)
print(a)#[10,17,18,25]

program2:
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)
change(a)
print(a)
output:
[10.20.30.40]
[50,60,70,80]
[10,20,30,40]

program3:
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)
f1(x)
print(x)
output:
10
20
10

program4:
def  f1(b):
	#b[2] = 25
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)#error
f1(a)#error
print(a)
