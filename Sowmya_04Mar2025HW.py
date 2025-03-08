
### 1️⃣ **First Loop (with `continue`)**
```
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')

print('Outside  loop')
```
**Output:**
```
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
else  suite
Outside  loop
```
🔹 The `continue` statement skips printing `"Sec"` and `"Hello"` when `i` is a multiple of `3`.

---

### 2️⃣ **Second Loop (with `break`)**
```
for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')

print('Outside  loop')
```
**Output:**
```
1
Sec
Hello
2
Sec
Hello
3
Outside  loop
```
🔹 The `break` statement exits the loop when `i == 3`, so `"else suite"` is **not** printed.

---

### 3️⃣ **Third Loop (with `break` for `i == 8`)**
```
for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')

print('Outside loop')
```
**Output:**
```
1
Sec
Hello
2
Sec
Hello
3
Sec
Hello
4
Sec
Hello
5
Sec
Hello
6
Sec
Hello
7
Sec
Hello
else  suite
Outside loop
```
🔹 Since `i` **never** reaches `8`, the `break` is **never executed**, so `"else suite"` is printed.

---

### 4️⃣ **Search for an Element Without Using `in`**
```
lst = [10, 20, 15, 12, 18]
x = int(input("Enter a number to search: "))
found = False

for index in range(len(lst)):
    if lst[index] == x:
        print(f"Found at index {index}")
        found = True
        break  # Stop searching once found

if not found:
    print("Not found")
```
**Outputs:**
```
Input: 15  →  Found at index 2
Input: 19  →  Not found
```

---

### 5️⃣ **Walrus Operator (`:=`) Demo**
```
print(a := 25)  # 25
print(a = 25)   # SyntaxError
print(a)        # Won't execute due to SyntaxError above
print(a := 6 + 7)  # 13
print(a)        # 13
print((a := 6) + 7)  # 13
print(a)        # 6
print((a = 6) + 7)  # SyntaxError
```
❌ **Errors:** `a = 25` and `(a = 6) + 7` are invalid because `=` is **not** an expression.

---

### 6️⃣ **Find Outputs (Walrus Operator with If)**
```
a = 0
if a == 0:  
	print('Hyd')  # Hyd
else:
	print('Sec')

if b := 0:  # 0 evaluates to False
	print('Hyd')
else:
	print('Sec:', b)  # Sec: 0

if c = 0:  # SyntaxError (Assignment inside if)
	print('Hyd')
else:
	print('Sec')
```
🔹 The `if c = 0` **causes a syntax error**.

---

### 7️⃣ **Find Outputs (Augmented Assignment Error)**
```
b = 10
a = b += 5  # SyntaxError
print(a)
```
❌ **Error:** `a = b += 5` is invalid. The correct way:
```python
b = 10
b += 5
a = b
print(a)  # 15
```

---

### 8️⃣ **Average of Inputs Until `-1` (Without Walrus Operator)**
```
sum = 0
ctr = 0

while True:
    x = eval(input("Enter input (-1 to stop): "))
    if x == -1:
        break
    sum += x
    ctr += 1

if ctr == 0:
    print("No valid inputs")
else:
    print("Average:", sum / ctr)
```
✅ **Sample Output:**
```
Inputs: 25, 10.8, True, 46.2, False, 92, -1
Sum: 25 + 10.8 + 1 + 46.2 + 0 + 92 = 175
Count: 6
Average: 29.166666666666668
```

---

### 9️⃣ **`del` Operator Demo**
```
a = 25
print(a)  # 25
del a
print(a)  # NameError: 'a' is not defined
```
🔹 `del a` **deletes `a` from memory**, causing an error when accessed.

---

### 🔟 **Find Outputs (Multiple Deletes)**
```
a = b = c = 25
print(a, b, c)  # 25 25 25
del a
print(b, c)  # 25 25
print(a)  # NameError: 'a' is not defined
del b
print(c)  # 25
print(b)  # NameError: 'b' is not defined
del c
print(c)  # NameError: 'c' is not defined
```
❌ **Errors:** Once deleted, accessing `a`, `b`, or `c` **raises an error**.

---

### 1️⃣1️⃣ **Deleting Multiple Variables**
```
a, b, c = 25, 10.8, 'Hyd'
print(a, b, c)  # 25 10.8 Hyd
del a, b, c
print(a)  # NameError
print(b)  # NameError
print(c)  # NameError
```
🔹 **All variables deleted**, so accessing them causes **NameError**.

---

### 1️⃣2️⃣ **Deleting Elements from List**
```python
a = [10, 20, 15, 18]
print(a)  # [10, 20, 15, 18]
del a[2]
print(a)  # [10, 20, 18]
del a
print(a)  # NameError: 'a' is not defined
print(a[0])  # Error because a is deleted
```
🔹 **List `a` is deleted**, so `print(a[0])` **raises an error**.

---

### 1️⃣3️⃣ **Deleting Elements from Tuple**
```
a = (10, 20, 15, 18)
print(a)  # (10, 20, 15, 18)
print(a[0])  # 10
del a[2]  # TypeError: 'tuple' object doesn't support item deletion
del a
print(a)  # NameError: 'a' is not defined
print(a[0])  # Error because a is deleted
```
🔹 **Tuples are immutable**, so `del a[2]` causes **TypeError**.

---

🔹 **Final Notes:**
- `continue` skips to the next loop iteration.
- `break` **exits** the loop.
- `del` removes variables or list elements but **not** tuple elements.
- The **walrus operator (`:=`)** assigns and evaluates in one step.
- **Syntax errors occur** when misusing assignment inside expressions.
