---

## **1. Printing a Dictionary in Different Ways**
```
a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}

print('Dictionary with print function')
print(a)  # Prints the entire dictionary

print('Keys of dictionary')
for key in a.keys():  # Printing only keys
    print(key)

print('Values of dictionary')
for value in a.values():  # Printing only values
    print(value)

print('All the tuples of dict_items object')
for item in a.items():  # Printing key-value pairs as tuples
    print(item)

print('Elements of each tuple')
for key, value in a.items():  # Printing key and value separately
    print(f'Key: {key}, Value: {value}')

print('Keys and values of dictionary')
for key in a:  # Another way to print key-value pairs
    print(f'Key: {key}, Value: {a[key]}')
```
### **Expected Output:**
```
Dictionary with print function
{10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
Keys of dictionary
10
20
15
18
Values of dictionary
Ramesh
Kiran
Amar
Sita
All the tuples of dict_items object
(10, 'Ramesh')
(20, 'Kiran')
(15, 'Amar')
(18, 'Sita')
Elements of each tuple
Key: 10, Value: Ramesh
Key: 20, Value: Kiran
Key: 15, Value: Amar
Key: 18, Value: Sita
Keys and values of dictionary
Key: 10, Value: Ramesh
Key: 20, Value: Kiran
Key: 15, Value: Amar
Key: 18, Value: Sita
```
---
## **2. Find Outputs - Set with print statements**
```
a = {
    print('Hyd'),
    print('Sec'),
    print('Cyb')
}
print(type(a))
print(a)
print(len(a))
```
### **Corrected Code & Expected Output:**
```python
print('Hyd')
print('Sec')
print('Cyb')

a = {'Hyd', 'Sec', 'Cyb'}  # Creating a set
print(type(a))  # Output: <class 'set'>
print(a)  # Output: Set with elements (order may vary)
print(len(a))  # Output: 3
```
```
Hyd
Sec
Cyb
<class 'set'>
{'Hyd', 'Cyb', 'Sec'}
3
```
---
## **3. Anonymous Object Demo Program**
```
_ = 25
print(_)  # Output: 25
print(type(_))  # Output: <class 'int'>

a, _, c = 10, 20, 30
print(a)  # Output: 10
print(_)  # Output: 20
print(c)  # Output: 30

for _ in range(5):
    print(_, 'Hello')
```
```
25
<class 'int'>
10
20
30
0 Hello
1 Hello
2 Hello
3 Hello
4 Hello
```
---
## **4. Memory Address Changes**
```
a = 25
print(id(a))  # ID of 25
a = 35
print(id(a))  # ID of 35 (Different from above)
```
Each integer has a unique memory address unless it's in Python's small integer cache.

---
## **5. Identity Operator Outputs**
```
a = 25
b = 25
print(a is b)  # True (small integer caching)

c = 'Hyd'
d = 'Hyd'
print(c is d)  # True (String interning)

e = False
f = False
print(e is f)  # True (Booleans are singletons)

g = range(10)
h = range(10)
print(g is h)  # False (Different objects)
```
---
## **6. Comparison of Different Data Types**
### **Find Outputs**
```
print(10 + 20)  # 30
print(10.8 + 20.6)  # 31.4
print(3 + 4j + 5 + 6j)  # (8+10j)
print(True + False)  # 1
print('Hyder' + 'abad')  # 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')  # 'SankarDayalSarma'
print('10' + '20')  # '1020'
print([10, 20, 30] + [1, 2, 3])  # [10, 20, 30, 1, 2, 3]
print((25, 10.8, 'Hyd') + (3 + 4j, True, None))  # Tuple concatenation

# Below lines are incorrect and will raise errors
# print({10 , 20} + {30 , 40})  ❌
# print({10 : 'Hyd'} + {20 : 'Sec'}) ❌
# print(range(4) + range(5)) ❌
# print(10 + '20') ❌
# print([10 , 20 , 30] + 5) ❌
# print([10 , 20 , 30] + (40 , 50 , 60)) ❌
```
---
## **7. Multiplication and Errors**
```
print(25 * 3)  # 75
print(10.8 * 25.6)  # 276.48
print(True * False)  # 0
print((3 + 4j) * (5 + 6j))  # (-9+38j)
print(3 + 4j * 5 + 6j)  # (3+26j)
print('25' * 3)  # '252525'
print('Hyd' * 4)  # 'HydHydHydHyd'
print([10, 20, 15] * 2)  # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3)  # Tuple repetition

# The below lines will raise TypeErrors:
# print([10, 20, 15] * 3.0) ❌
# print({10, 20, 15} * 2) ❌
# print({10: 20, 30: 40} * 2) ❌
# print([10] * [20]) ❌
```
---
## **8. Division Errors**
```
print(7 / 0)  # ZeroDivisionError ❌
print(7 // 0)  # ZeroDivisionError ❌
print(7 % 0)  # ZeroDivisionError ❌
```
---
## **9. Relational Operators**
```python
print(9 >= 5)  # True
print(9 >= 9)  # True
print(9 >= 12)  # False
print(6 <= 8)  # True
print(6 <= 6)  # True
print(6 <= 4)  # False
print(9 != 7)  # True
print(6 == 8)  # False
print(True > False)  # True
print(3 + 4j == 3 + 4j)  # True
print(3 + 4j != 5 + 6j)  # True
print(10 == 10.0)  # True
```
---
## **10. String Comparisons**
```python
print('Rama' > 'Rajesh')  # True (m > j)
print('Hyd' == 'Hyd')  # True
print('HYD' < 'hyd')  # True (Capital letters come before lowercase)
```
---
