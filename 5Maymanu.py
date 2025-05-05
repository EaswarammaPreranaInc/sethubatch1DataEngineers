'''
#1) Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child  = Thread(target = a . m1)
a . m1()
for  i  in  range(10):
	print('main  thread')

output:-
------
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread

#2) Find  outputs (Home  work)
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target =  a . m1())
child . start() # 2 threads
for  i  in  range(10):
        print('main  thread')

output:-
---------
child  thread---10 times <nextline>
main thread---10 times <nextline>


#3)  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(target = c1 . m1)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)
output:-
-----------
Child  Thread  :   1
Main  Thread  :   1
Child  Thread  :   2
Main  Thread  :   2
Child  Thread  :   3
Main  Thread  :   3
Child  Thread  :   4
Main  Thread  :   4
Child  Thread  :   5
Main  Thread  :   5
Child  Thread  :   6
Main  Thread  :   6
Child  Thread  :   7
Main  Thread  :   7
Child  Thread  :   8
Main  Thread  :   8
Child  Thread  :   9
Main  Thread  :   9
Child  Thread  :   10
Main  Thread  :   10

#4) Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()  
t . start() # 'Thread' object has no attribute 'start'.
for  i  in  range(10):
        print('main  thread')

output:-
----------
'Thread' object has no attribute 'start'

#5) Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread')

output:-
----------
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread

#6) Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
#end of the class
child = MyThread()
child . run()
for  i  in  range(10):
        print('main  thread')

output:-
---------
child  thread---10 times <nextline>
main thread---10 times <nextline>


#7)Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('Child  Thread')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')

output:-
-----------
main thread---10 times <nextline>


#8)# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
child = MyThread(target = f1)
child . start() # New thread is created 
print('Main  Thread')

output:-
----------
run  method
Main  Thread


#9)Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(1 , 11):
		print('f1  function : ' , i)
child = MyThread(target = f1)
child . start()
for  i  in  range(1 , 11):
	print('Main  Thread : ' , i)

output:-
-------
f1  function :  1
Main  Thread :  1
f1  function :  2
Main  Thread :  2
f1  function :  3
Main  Thread :  3
f1  function :  4
Main  Thread :  4
f1  function :  5
Main  Thread :  5
f1  function :  6
Main  Thread :  6
f1  function :  7
Main  Thread :  7
f1  function :  8
Main  Thread :  8
f1  function :  9
Main  Thread :  9
f1  function :  10
Main  Thread :  10


#10)Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')

output:-
--------
Main  Thread

#11)
from  threading  import  *
class  MyThread(Thread):
        def  run(self):
                for  i  in  range(10):
                        print('run   method  of  MyThread  class')
        def  m1(self):
                for  i  in  range(10):
                        print('m1  method  of  MyThread  class')
class  c1(Thread): 
        def  m1(self):
                for  i  in  range(10):
                        print('m1  method  of  class  c1')
        def   f1(self):
                 for  i  in  range(10):
                         print('f1  method  of  class  c1')
# end of class
def   f1():
        for  i  in  range(10):
                print('f1  function')
#end of f1 function
t1 = Thread(target = f1)
t2 = Thread(target = c1() . m1)
t3 = Thread()
t4 = MyThread()
t5 = MyThread(target = f1)
t6 = c1(target =  f1)
t7 = c1()
t8 = MyThread(target = c1() . m1)
t9 = c1(target = c1() . m1)
t10 = MyThread(target = t4 . run)
t11 = c1(target = t7 . run)
t12 = c1(target = t4 . m1)
t13 = c1(target = t7 . f1)
# Run  with  any  one  of  the  following  stmts
#t1 . start() # f1  function < nextline> 10 times
#t2 . start() # m1  method  of  class  c1 <next line> 10 times
#t3 . start() # no output
#t4 . start() # run   method  of  MyThread  class <next line> 10 times
#t5 . start() # run   method  of  MyThread  class <next line> 10 times
#t6 . start() # f1  function < nextline> 10 times
#t7 . start() # no output
#t8 . start() # run   method  of  MyThread  class < nextline> 10 times
#t9 . start() # m1  method  of  class  c1 <next line> 10 times
#t10 . start() # run   method  of  MyThread  class <next line> 10 times
#t11 . start() # no output
#t12 . start() # m1  method  of  MyThread  class <next line> 10 times
t13 . start() # f1  method  of  class  c1 <next line> 10 times

output:-
------------
1) What  are  the  outputs  for  t1 . start() ?  ---> f1  function < nextline> 10 times

2) What  are  the  outputs  for  t2 . start() ?  ---> m1  method  of  class  c1 <next line> 10 times

3) What  are  the  outputs  for  t3 . start() ?  ---> no output

4) What  are  the  outputs  for  t4 . start() ?  ---> run   method  of  MyThread  class <next line> 10 times

5) What  are  the  outputs  for  t5 . start() ?  ---> run   method  of  MyThread  class <next line> 10 times

6) What  are  the  outputs  for  t6 . start() ?  ---> f1  function < nextline> 10 times

7) What  are  the  outputs  for  t7 . start() ?  ---> no output

8) What  are  the  outputs  for  t8 . start() ?  ---> run   method  of  MyThread  class < nextline> 10 times

9) What  are  the  outputs  for  t9 . start() ?  ---> m1  method  of  class  c1 <next line> 10 times

10) What  are  the  outputs  for  t10 . start() ?  ---> run   method  of  MyThread  class <next line> 10 times

11) What  are  the  outputs  for  t11 . start() ?  ---> no output

12) What  are  the  outputs  for  t12 . start() ?  ---> m1  method  of  MyThread  class <next line> 10 times

13) What  are  the  outputs  for  t13 . start() ?  ---> f1  method  of  class  c1 <next line> 10 times


#11) What  are  the  outputs  when  start()  method  is  overridden  ?  (Home  work)
from  threading  import  *
class  MyThread(Thread):
	def   start(self):
		super() . start()
		print('Start Method')
	def   run(self):
		print('Run Method')
#  main  thread  executes  following  statements
child = MyThread()
child . start()
print('Main  Thread')

output:-
-------
Run Method
Start Method
Main  Thread


#12) Find  outputs (Home  work)
from threading import *
main_thread = current_thread() 
print ( 'main_thread:', main_thread.name ) # How  to  print  name  of  main  thread
main_thread.name = 'Hyd' # How  to  modify  name  of  main  thread  to   'Hyd'
print ('new  name  of  main  thread :',main_thread.name) # How  to  print  new  name  of  main  thread
def child_task() : 
		child = current_thread() 
		print('child thread :' , child.name) 
		child.name = 'Sec' # How  to  create  a  new  child  thread  with  name  "Sec"
		print('New child thread :' , child.name) #How  to  print  name  of  child  thread
child_thread = Thread(target = child_task, name = 'Cyd') # How  to  modify  name  of  child  thread  to   'Cyb'
child_thread . start()
child_thread.join() #How  to  print  new  name  of  child  thread
print("number of threads under execution:" , active_count()) #How  to  print  number  of  threads  under  execution

output:-
--------
main_thread: MainThread
new  name  of  main  thread : Hyd
child thread : Cyd
New child thread : Sec
number of threads under execution: 1

#13)Find  outputs (Home  work)

from threading import *
def task():
    pass
t1 = Thread(target=task, name='t1') #How  to  create  three  new  threads  t1 , t2 , t3
t2 = Thread(target=task, name='t2')
t3 = Thread(target=task, name='t3')

# Start the threads
t1.start()
t2.start()
t3.start()

# Wait for threads to complete
t1.join()
t2.join()
t3.join()

# Print names of threads
print("Names of Threads")
print(f"t1: {t1.name}") # How  to  print  name  of  each  thread
print(f"t2: {t2.name}")
print(f"t3: {t3.name}")

# Modify names of threads
t1.name = 'One' # How  to  modify  name  of  each  thread  to  "One" , "Two"   and  "Three"
t2.name = 'Two'
t3.name = 'Three'

# Print new names of threads
print("New Names of Threads")
print(f"t1: {t1.name}") # How  to  print  new  name  of  each  thread
print(f"t2: {t2.name}")
print(f"t3: {t3.name}")

# Print number of threads under execution
print("Number of threads currently under execution:", active_count()) # How  to  print  number  of  threads  under  execution

output:-
--------
Names of Threads
t1: t1
t2: t2
t3: t3
New Names of Threads
t1: One
t2: Two
t3: Three
Number of threads currently under execution: 1


#14)Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print('child thread:', current_thread().name) # How  to  print  name  of  child  thread
child = Thread(target = f1, name = "Child") # How  to  create  a  new  thread  with  name  "Child"  and  target  f1
child.start () # How  to  start  the  new  thread
print(' Main thread:', current_thread().name) # How  to  print  name  of   main  thread

output:-
----------
child thread: Child
 Main thread: MainThread

#15)Find  outputs (Home  work)
from  threading  import  *
How  to  create  a  thread  t1  with  name  'Hyd'
How  to  create  another  thread  t2  without  a  name
How  to  print  name  of  main  thread
How  to  print  name  of  thread  t1
How  to  print  name  of  thread  t2
How  to  modify  name  of  main  thread  to  'India'
How  to  modify  name  of  thread  t1  to  'Sec'
How  to  modify  name  of  thread  t2  to  'Cyb'
How  to  print  name  of  main  thread
How  to  print  name  of  thread  t1
How  to  print  name  of  thread  t2
How  to  print  number  of  threads  under  execution


#16) Find  outputs  (Home  work)
from  threading  import  *
def   f1(x):
	s = current_thread() . name
	while   True:
		print(s , ' : ' , x)
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))
t2 = Thread(target = f1 , name = 'Sec' , args = [20])
t1 . start() #  t1  executes  f1(10)
t2 . start()   #  t2  executes  f1(20)
print(active_count())
print('Press  ctrl + break  or  Fn + b  to  stop ')

output:-
--------
Hyd : 10
sec : 20 for infinite times

#17)Find  outputs (Home  work)
from  threading  import  Thread , current_thread
from  random  import  randint
def   f1(n):
	ctr = 0
	s = current_thread() . name
	while  True:
		x = randint(1 , 100)
		ctr += 1
		print(F'{s}  guess  {x}   in  attempt  :  {ctr}')
		if   x ==  n:
			break
	#end of while loop
	print(F'{s}  finish  in  {ctr}  attempts')
t1 = Thread(target = f1 , args = [75] , name = 'Rama')
t2 = Thread(target = f1 , args = [50] , name = 'Sita')
t1 . start()
t2 . start()

output:-
------------
ama  guess  76   in  attempt  :  21
Rama  guess  75   in  attempt  :  22
Rama  finish  in  22  attempts
Sita  guess  45   in  attempt  :  237
Sita  guess  50   in  attempt  :  238
Sita  finish  in  238  attempts


#18)from  threading  import  *

How  to  print  name  of  main  thread
How  to  print  name  of  thread  t1
How  to  print  name  of  thread  t2
How  to  modify  name  of  main  thread  to  'India'
How  to  modify  name  of  thread  t1  to  'Sec'
How  to  modify  name  of  thread  t2  to  'Cyb'
How  to  print  name  of  main  thread
How  to  print  name  of  thread  t1
How  to  print  name  of  thread  t2
How  to  print  number  of  threads  under  execution


'''
from threading import *

# Dummy function for threads
def task():
    pass

# Create a thread t1 with name 'Hyd'
t1 = Thread(target=task, name='Hyd') # How  to  create  a  thread  t1  with  name  'Hyd'

# How  to  create  another  thread  t2  without  a  name
t2 = Thread(target=task)  # Python will assign a default name like 'Thread-1'

# Start the threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

# Print name of main thread
print("Name of main thread:", current_thread().name)

# Print name of thread t1
print("Name of thread t1:", t1.name)

# Print name of thread t2
print("Name of thread t2:", t2.name)

# Modify name of main thread to 'India'
current_thread().name = 'India'

# Modify name of thread t1 to 'Sec'
t1.name = 'Sec'

# Modify name of thread t2 to 'Cyb'
t2.name = 'Cyb'

# Print new name of main thread
print("New name of main thread:", current_thread().name)

# Print new name of thread t1
print("New name of thread t1:", t1.name)

# Print new name of thread t2
print("New name of thread t2:", t2.name)

# Print number of threads under execution
print("Number of threads currently under execution:", active_count())
