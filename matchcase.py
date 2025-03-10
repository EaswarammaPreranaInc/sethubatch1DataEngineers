Match case
==================

i)A python "Match case" statement offers a powerful mechanism for pattern matching in python. It allows us to perform more expressive and readable conditional checks.
ii)Unlike traditional if-elf-else chains, which can become unwieldy either complex conditions, the match-case statement provides a more elegant and flexible solution.

Example programs
=========================
1)m=4
match m:			
    case 1:
        print('one')
    case 2:
        print('two')
    case 3:
        print('three')
print('bye')

output: bye (Reason: In the above program there is no case-4 condition so that the reason it will print bye. bye is outside the match-case function.)
The value of m=1, then the output will be one<nextline>bye.

2)m=3
match m:
    case 1:
        print('one')
    case _:
        print('two')
    case 3:
        print('three')
print('bye')

output: Error wildcard makes remaining patterns unreachable (In case _: it is called as wildcard entry error will come. If we write the last print statement it will works please check next example)

3)m=1
match m:
    case 1:
        print('one')
    case _:
        print('two')
    case _:
        print('three')
print('bye')

ooutput: Error wildcard makes remaining patterns unreachable(Only one wildcard is possiable)

4)m=1
match m:
    case 1:
        print('one')
    case 1:
        print('two')
    case 1:
        print('three')
print('bye')

output: one<next line>bye (If we give case are same number it will take only first case.)

5)ch ='s'
match ch:
    case 'a':
        print('one')
    case 'v':
        print('two')
    case 's':
        print('three')
print('bye')

output: three<next line>bye (In these we can take string as input and case type also)


Note: a|b (or) a or b ----> | it is called as pipe operator. The work of these | pipe operator is same as (or logical operator)

6)ch ='z'
match ch:
    case 'a'|'z':
        print('one')
    case 'v'|'d':
        print('two')
    case 's'|'q':
        print('three')
print('bye')

output: one<next line>bye (The work of these | pipe operator is same as (or logical operator)


7)write a program
  i)what are the output if input is -6? #output--> hyd<next line>sec<next line>cyb<next line>bye
  ii)what are the output if input is 15? #output--> 1<next line>2<next line>3<next line>bye 
  iii)what are the output if input is 10.8? #output--> IND<next line>NZ<next line>Aus<next line>bye 
  iv)what are the output if input is 0? #output--> hyd<next line>sec<next line>cyb<next line>bye
  v)what are the output if input is -10?  #output--> 1<next line>2<next line>3<next line>bye 
  vi)what are the output if input is 7? #output--> hyd<next line>sec<next line>cyb<next line>bye

x=eval(input('enter a number: '))
match x:
	case 7|-6|0:
		print('hyd')
		print('sec')
		print('cyb')
	case -10|15:
		print('1')
		print('2')
		print('3')
	case _:
		print('IND')
		print('NZ')
		print('Aus')
print('bye')


8)write a program
  i)what is the output when input is(-10,-20)? output--> Quadrant
  ii)what is the output when input is(10,0)? output--> x-axis
  iii)what is the output when input is(0,-20)? output--> y-axis
  iv)what is the output when input is(0,0)? output--> origin
  v)what is the output when input is(10,20,30)? output--> not a point (point contains only 2 values)
  vi)what is the output when input is[10,20]? output--> Quadrant (list is accepted)
  vii)what is the output when input is[0,-25]? output--> y-axis (list is accepted)
  viii)what is the output when input is()? output--> not a point (Empty tuple)
  ix)what is the output when input is{10,20}?  output--> not a point (because the input must be in tuple form, here the input is dist form)
  x)what is the output when input is(25,)? output--> not a point

tpl=eval(input('enter any point in the form of (x,y): '))
match tpl:
	case (0,0):
		print('origin')
	case (x,0):
		print('x-axis')
	case (0,y):
		print('y-axis')
	case (x,y):
	    print('Quadrant')
	case  _:
	    print('not a point')

9)write a program to print day of the week
1-mon
2-tues
3-wed
4-thur
5-fri
6-sat
7-sun
8-Invalide


x=eval(input('enter a number: '))
match x:
	case 1:
		print('Mon')
	case 2:
		print('Tue')
	case 3:
		print('Wed')
	case 4:
	    print('Thu')
	case 5:
	    print('fri')
	case 6:
	    print('Sat')
	case 7:
	    print('Sun')
	case  _:
	    print('Invalid')


9)write a program to print day of the week
1-one
2-two
3-three
4-four
5-five
6-six
7-seven
8-Eight
9-Nine
10- not a digit


x = eval(input('Enter a number: '))
match x:
    case 0:
        print('zero')
    case 1:
        print('one')
    case 2:
        print('two')
    case 3:
        print('three')
    case 4:
        print('four')
    case 5:
        print('five')
    case 6:
        print('six')
    case 7:
        print('seven')
    case 8:
        print('eight')
    case 9:
        print('nine')
    case _:
        print('Not a digit')
