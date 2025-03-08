---

### **1. Modify the Month Program Using `else` and `if`**
```
try:
    a = int(input('Enter month number (1 - 12): '))
    if a == 1:
        print('January')
    elif a == 2:
        print('February')
    elif a == 3:
        print('March')
    elif a == 4:
        print('April')
    elif a == 5:
        print('May')
    elif a == 6:
        print('June')
    elif a == 7:
        print('July')
    elif a == 8:
        print('August')
    elif a == 9:
        print('September')
    elif a == 10:
        print('October')
    elif a == 11:
        print('November')
    else:  # This will handle both 12 and any other invalid inputs
        if a == 12:
            print('December')
        else:
            print('Input should be between 1 and 12')
except ValueError:
    print('Input should be an integer')
```

---

### **2. Electricity Bill Calculation Using `match...case`**
```
units = int(input('Enter units: '))

bill = 0
remaining_units = units

match units // 100:
    case 0:
        bill += units * 3.00
    case 1:
        bill += 100 * 3.00
        bill += (units - 100) * 3.50
    case 2 | 3:
        bill += 100 * 3.00
        bill += 100 * 3.50
        bill += (units - 200) * 4.00
    case 4 | 5 | 6:
        bill += 100 * 3.00
        bill += 100 * 3.50
        bill += 200 * 4.00
        bill += (units - 400) * 4.50
    case _:
        bill += 100 * 3.00
        bill += 100 * 3.50
        bill += 200 * 4.00
        bill += 300 * 4.50
        bill += (units - 700) * 5.00

print(f"Bill Amount: Rs. {bill}")
```

---

### **3. Printing Elements Using `for` Loops**
```
# Printing list elements
for x in [10, 20, 15, 18]:
    print(x)

print()

# Printing characters of a string
for x in 'Hyd':
    print(x)

print()

# Printing range elements
for x in range(5):
    print(x)
```

---

### **4. Printing Dictionary Keys, Values, and Items**
```
d = {10: 20, 30: 40, 50: 60}

# Printing keys
for x in d.keys():
    print(x)
print()

# Printing values
for x in d.values():
    print(x)
print()

# Printing items (key-value pairs)
for x in d.items():
    print(x)
print()

# Printing keys (direct iteration)
for x in d:
    print(x)
```

---

### **5. Finding Outputs (Key-Value Iteration)**
```
a = {10: 20, 30: 40, 50: 60}

# Correct way to print key-value pairs
for x, y in a.items():
    print(x, y, sep='...')

# Incorrect way (this will cause an error)
for x, y in a:  # ❌ This will cause a ValueError
    print(x, y)

# Incorrect way (this will cause an error)
for x, y in {10: 20, 30: 40, 50: 60}:  # ❌ This will also cause a ValueError
    print(x, y, sep='...')
```
🔴 **Error:** `ValueError: too many values to unpack` because iterating over a dictionary directly returns keys, not key-value pairs.

---

### **6. Identify the Error in the Code**
```
for x in 123:
    print(x)
```
🔴 **Error:** `TypeError: 'int' object is not iterable` because integers cannot be iterated over.

---

### **7. Finding Outputs (Empty Iterations)**
```
# No output (Empty Tuple)
for x in ():
    print(x)

# No output (Empty List)
for x in []:
    print(x)

# No output (Empty Dictionary - Iterating over keys)
for x in {}:
    print(x)

# No output (Empty Set)
for x in set():
    print(x)

# No output (Empty String)
for x in '':
    print(x)

# No output (Range with No Values)
for x in range(10, 10):  
    print(x)

# ❌ This will cause an error (range() needs at least one argument)
for x in range():
    print(x)

# ❌ This will cause an error (25 is an integer, not a tuple)
for x in (25):
    print(x)
```
🔴 **Errors:**
- `range()` without arguments will raise a `TypeError`.
- `(25)` is treated as an integer, not a tuple, so iterating over it raises a `TypeError`.

---

### **8. Nested Loop Output**
```
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
    print('Hello')
print('Bye')
```
#### **Output:**
```
1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye
```
---

