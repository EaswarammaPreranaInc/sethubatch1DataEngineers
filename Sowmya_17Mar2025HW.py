#1 difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) #{10, 20}
print(type(c)) #<class 'set'>
d = a - b
print(d) #{10, 20}
print(type(d)) #<class 'set'>
print(c  is  d) #True
print(c  ==  d) #True

Explanation:
a.difference(b)

The difference() method returns a new set containing elements from a that are not in b.
{10, 20, 30, 40} - {30, 40, 50, 60} = {10, 20}
a - b

This is an alternative to difference(), performing the same operation using the - operator.
The result is also {10, 20}.
print(c is d) → True

Since c and d store the same set {10, 20}, Python optimizes memory usage by pointing both variables to the same object.
print(c == d) → True

== checks if both sets have the same elements, which they do.
Additional Clarifications:
Can set.difference(list) be valid?
✅ Yes! difference() works with any iterable, including lists, tuples, and sets.

a = {1, 2, 3, 4}
b = [3, 4, 5, 6]  # A list
print(a.difference(b))  # Output: {1, 2}
Is set - list valid?
❌ No! The - operator requires both operands to be sets.

python
a - b  # TypeError: unsupported operand type(s) for -: 'set' and 'list'

'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->
										Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
