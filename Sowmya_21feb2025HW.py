---

### **1. Assignment Operators Demo Program**
```
a = 25 
print(a)  # Output: 25

b = a  
print(b)  # Output: 25

print(a is b)  # Output: True (Both refer to the same object in memory)

x = 4
y = 5
z = x + y * 6  
print(z)  # Output: 4 + (5 * 6) = 4 + 30 = 34

# Incorrect assignments (fixing them)
# 25 = a  ❌ (Syntax Error)
# a + b = x + y  ❌ (Syntax Error)
```
---
### **2. Find Outputs - Variable Assignments**
```
a = b = c = 25  
print(id(a))  # ID of variable (same for all three variables)
print(id(b))  # Same as id(a)
print(id(c))  # Same as id(a)
print(a, b, c)  # Output: 25 25 25
```
---
### **3. Multiple Assignments**
```
x, y, z = 25, 10.8, 'Hyd'  
print(x)  # Output: 25
print(y)  # Output: 10.8
print(z)  # Output: Hyd
```
---
### **4. Find Outputs - Compound Assignment**
```
a, b, c = 3, 4, 5
a *= b + c
print(a)  # Output: 3 * (4 + 5) = 3 * 9 = 27
```
---
### **5. Find Outputs - Modulus Assignment**
```
a = 20
a %= 3 + 2 * 4  
print(a)  # Output: 20 % (3 + 8) = 20 % 11 = 9
```
---
### **6. Find Outputs - Exponentiation**
```
a = 3
a **= 4 
print(a)  # Output: 3^4 = 81
```
---
### **7. Identity Operators**
```
a = 25
b = 25
print(a is b)  # Output: True (Python caches small integers)
print(a is not b)  # Output: False
print(a == b)  # Output: True
```
---
### **8. Find Outputs - Identity Operator with Different Data Types**
```
a = 25 
b = 25.0  
print(a is b)  # Output: False (Different data types)
print(a is not b)  # Output: True
print(a == b)  # Output: True (Values are equal)
```
---
### **9. Find Outputs - String and List Comparisons**
```
a = 'Hyd' 
b = 'Hyd' 
print(a is b)  # Output: True (String interning in Python)
print(a is not b)  # Output: False
print(a == b)  # Output: True

print()

x = [1, 2, 3, 4]  
y = [1, 2, 3, 4]  
print(x is y)  # Output: False (Different list objects)
print(x is not y)  # Output: True
print(x == y)  # Output: True (Lists have the same values)

print()

m = (1, 2, 3, 4) 
n = (1, 2, 3, 4)  
print(m is n)  # Output: True (Tuples are immutable and reused)
print(m is not n)  # Output: False
print(m == n)  # Output: True
```
---
### **10. Membership Operators**
```
lst = [10, 20, 15, 12, 18]
print(15 in lst)  # Output: True
print(19 in lst)  # Output: False
print(14 not in lst)  # Output: True
print(15 not in lst)  # Output: False

s = 'Hyd is green city'
print('is' in s)  # Output: True
print('was' in s)  # Output: False
print('g' in s)  # Output: True
print('z' in s)  # Output: False
print(' ' in s)  # Output: True
print('gre' in s)  # Output: True
print('yd i' in s)  # Output: True
print('' in s)  # Output: True (Empty string is always in any string)
print('' not in s)  # Output: False
```
---
### **11. Pre/Post Increment Operators (Python Fix)**
❌ **Incorrect in Python:** Python does **not** support `++` and `--` like C++ or Java.
```
a = 25
print(+a)  # Output: 25
print(-a)  # Output: -25
```
---
### **12. Semicolon Usage**
---
print('One'); print('Two'); print('Three')  # Output: One Two Three
print('Hyd'); print('Sec'); print('Cyb')  # Output: Hyd Sec Cyb
```
---
### **13. floor() and ceil() Functions**
```
import math

print(math.floor(10.8))  # Output: 10
print(math.ceil(10.8))  # Output: 11
print(math.floor(25.0))  # Output: 25
print(math.ceil(25.0))  # Output: 25
print(math.floor(-3.5))  # Output: -4
print(math.ceil(-3.5))  # Output: -3
print(math.floor(-9.0))  # Output: -9
print(math.ceil(-9.0))  # Output: -9
print(math.floor(25.1))  # Output: 25
print(math.ceil(25.1))  # Output: 26
```
---
### **14. abs() Function**
```
print(abs(-35.8))  # Output: 35.8
print(abs(-27))  # Output: 27
print(abs(29.5))  # Output: 29.5
print(abs(32))  # Output: 32
```
---
### **15. max() and min() Functions**
```
print(max(10.8, 20.6))  # Output: 20.6
print(min(10.8, 20.6, 5.9, 12.3))  # Output: 5.9
print(max(25, 10.8))  # Output: 25
print(max(10, 20, 30))  # Output: 30
print(min(10, 20, 15, 5, 12))  # Output: 5
```
---
### **16. pow() Function**
```
print(pow(10, -2))  # Output: 0.01 (10^(-2))
print(pow(4, pow(3, 2)))  # Output: 4^(3^2) = 4^9 = 262144
print(pow(2, 3))  # Output: 8
print(pow(-2, -3))  # Output: -0.125 (-2^(-3))
```
---
