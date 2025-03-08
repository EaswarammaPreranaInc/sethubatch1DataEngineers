### **1. Area and Perimeter of a Rectangle**
```
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
```

---

### **2. Volume of a Sphere**
```
import math

radius = float(input("Enter radius: "))
volume = (4 / 3) * math.pi * radius ** 3

print(f"Volume: {volume:.2f}")
```

---

### **3. Simple and Compound Interest**
```
p = float(input("Enter principle: "))
t = float(input("Enter time: "))
r = float(input("Enter rate of interest: "))

si = (p * t * r) / 100
ci = p * (1 + r / 100) ** t - p

print(f"Simple Interest: {si:.2f}")
print(f"Compound Interest: {ci:.2f}")
```

---

### **4. Swapping Two Numbers Using a Third Variable**
```
x = float(input("Enter 1st input: "))
y = float(input("Enter 2nd input: "))

print(f"Before swap: x={x} y={y}")

temp = x
x = y
y = temp

print(f"After swap: x={x} y={y}")
```

---

### **5. Swapping Two Numbers Without a Third Variable (Using Addition & Subtraction)**
```
x = float(input("Enter 1st input: "))
y = float(input("Enter 2nd input: "))

print(f"Before swap: x={x} y={y}")

x = x + y
y = x - y
x = x - y

print(f"After swap: x={x} y={y}")
```

---

### **6. Swapping Two Numbers Without a Third Variable (Using Multiplication & Division)**
```
x = float(input("Enter 1st input: "))
y = float(input("Enter 2nd input: "))

print(f"Before swap: x={x} y={y}")

x = x * y
y = x / y
x = x / y

print(f"After swap: x={x} y={y}")
```

---

### **7. Operations on Complex Numbers**
```
a = complex(input("Enter first complex number: "))
b = complex(input("Enter second complex number: "))

print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Division: {a / b}")
```

---

### **8. Various Operations on Two Numbers**
```
import math

x = int(input("Enter 1st integer number: "))
y = int(input("Enter 2nd integer number: "))

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} % {y} = {x % y}")
print(f"max({x}, {y}) = {max(x, y)}")
print(f"min({x}, {y}) = {min(x, y)}")
print(f"{x} ^ {y} = {x ** y}")
print(f"sqrt({x}) = {math.sqrt(x)}")
print(f"gcd({x}, {y}) = {math.gcd(x, y)}")
print(f"fact({x}) = {math.factorial(x)}")
```

---

### **9. Swapping Two Variables in a Single Statement**
```
x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")

print(f"Before swap: x={x} y={y}")

x, y = y, x  # Single statement swap

print(f"After swap: x={x} y={y}")
```

---

### **10. Largest of Two Inputs Without `max()`**
```
x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")

largest = x if x > y else y

print(f"Largest Input: {largest}")
```

---

### **11. Largest of Three Inputs Without `max()`**
```
x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")
z = input("Enter 3rd input: ")

largest = x if (x > y and x > z) else (y if y > z else z)

print(f"Largest Input: {largest}")
```

---

### **12. Print Comparison (`>`, `<`, `=`)**
```
x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")

result = ">" if x > y else "<" if x < y else "="

print(f"Result: {result}")
```

---

### **13. Check if a Number is Positive, Negative, or Zero**
```
x = float(input("Enter any number: "))

result = 1 if x > 0 else -1 if x < 0 else 0

print(f"Result: {result}")
```

---

### **14. Check If a Number is Even or Odd**
```
x = int(input("Enter any positive integer: "))

result = "Even number" if x % 2 == 0 else "Odd number"

print(result)
```

---
