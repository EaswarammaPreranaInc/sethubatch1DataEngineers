Here's a simple demo program showing how the `append()` method works in Python:

```python
# Define a list
my_list = [10, 20, 15, 18]

# Print the original list
print("Original list:", my_list)

# Append an element (19) to the list
my_list.append(19)

# Print the updated list
print("Updated list after append:", my_list)
```

### **Output:**
```
Original list: [10, 20, 15, 18]
Updated list after append: [10, 20, 15, 18, 19]
```

### **Explanation:**
- The `append()` method adds an element to the end of the list.
- Here, `19` is added to the list `[10, 20, 15, 18]`, making it `[10, 20, 15, 18, 19]`.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define an empty list
my_list = []

# Print the empty list
print("Original list:", my_list)

# Append different types of elements
my_list.append(25)      # Integer
my_list.append(10.8)    # Float
my_list.append('Hyd')   # String
my_list.append(True)    # Boolean

# Print the updated list
print("Updated list after append:", my_list)
```

### **Output:**
```
Original list: []
Updated list after append: [25, 10.8, 'Hyd', True]
```

### **Explanation:**
- The list is initially empty (`[]`).
- `append(25)` adds an integer.
- `append(10.8)` adds a floating-point number.
- `append('Hyd')` adds a string.
- `append(True)` adds a boolean value.
- The final list contains multiple data types: `[25, 10.8, 'Hyd', True]`.

This shows that Python lists can store different types of data in the same list. 
----------------------------------------------------------------------------------------------------------------------------------------------------------
# Define an empty list
list = []

# Loop through numbers from 0 to 50 with a step of 10
for x in range(0, 50, 10):
    list.append(x)

# Print the updated list
print(list)
```

### **How it Works:**
- `range(0, 50, 10)` generates numbers starting from `0` up to `50` (excluding `50`), with a step of `10`.
- The generated numbers are: `0, 10, 20, 30, 40`.
- Each number is appended to the list.

### **Expected Output:**
```
[0, 10, 20, 30, 40]
```

This program successfully creates and prints a list of numbers increasing by 10 from 0 to 40. 
------------------------------------------------------------------------------------------------------------------------------------------------------------
a = [10, 20, 30]  # Define a list
a.append('Hyd')   # Append 'Hyd' to the list
print(a)          # Print the updated list
print(len(a))     # Print the length of the list

# Printing specific elements
print(a[3])       # Print the 4th element (index 3)
print(a[3][0])    # Print 'H' (first character of 'Hyd')
print(a[3][1])    # Print 'y' (second character of 'Hyd')
print(a[3][2])    # Print 'd' (third character of 'Hyd')
```

---

### **Step-by-step Execution:**
1. Initially, `a = [10, 20, 30]`.
2. `a.append('Hyd')` → Now, `a = [10, 20, 30, 'Hyd']`.
3. `print(a)` → Outputs:
   ```
   [10, 20, 30, 'Hyd']
   ```
4. `print(len(a))` → The list has **4 elements**, so it prints:
   ```
   4
   ```
5. `print(a[3])` → The 4th element (index **3**) is `'Hyd'`, so it prints:
   ```
   Hyd
   ```
6. `print(a[3][0])` → `'H'` is the **first** character of `'Hyd'`, so it prints:
   ```
   H
   ```
7. `print(a[3][1])` → `'y'` is the **second** character of `'Hyd'`, so it prints:
   ```
   y
   ```
8. `print(a[3][2])` → `'d'` is the **third** character of `'Hyd'`, so it prints:
   ```
   d
   ```

---

### **Final Output:**
```
[10, 20, 30, 'Hyd']
4
Hyd
H
y
d
```

This program demonstrates how list elements and string indexing work in Python. 
----------------------------------------------------------------------------------------------------------------------------------------------------
a = [10, 20, 30, 40]  # Define list 'a'
b = [50, 60, 70]      # Define list 'b'

a.insert(2, b)        # Insert list 'b' at index 2 in 'a'

print(a)              # Print the updated list 'a'
print(len(a))         # Print the length of list 'a'

# Accessing elements
print(a[2])           # Print the inner list (list 'b')
print(a[2][0])        # Print 50 (first element of list 'b')
print(a[2][1])        # Print 60 (second element of list 'b')
print(a[2][2])        # Print 70 (third element of list 'b')
```

---

### **Step-by-step Execution:**
1. **Initial Lists:**  
   - `a = [10, 20, 30, 40]`
   - `b = [50, 60, 70]`
   
2. **Insert Operation:**  
   - `a.insert(2, b)` inserts `b` **at index 2** in `a`, shifting other elements to the right.  
   - Now, `a = [10, 20, [50, 60, 70], 30, 40]`
   
3. **`print(a)` Output:**  
   ```
   [10, 20, [50, 60, 70], 30, 40]
   ```

4. **`print(len(a))` Output:**  
   - The list `a` now has **5 elements** (`10`, `20`, `[50, 60, 70]`, `30`, `40`).
   ```
   5
   ```

5. **How to print the inner list?**  
   - The inner list is at **index 2**, so:
   ```
   print(a[2])
   ```
   - **Output:**  
   ```
   [50, 60, 70]
   ```

6. **How to print `50`?**  
   - The first element of the inner list is at `a[2][0]`, so:
   ```
   print(a[2][0])
   ```
   - **Output:**  
   ```
   50
   ```

7. **How to print `60`?**  
   - The second element of the inner list is at `a[2][1]`, so:
   ```
   print(a[2][1])
   ```
   - **Output:**  
   ```
   60
   ```

8. **How to print `70`?**  
   - The third element of the inner list is at `a[2][2]`, so:
   ```
   print(a[2][2])
   ```
   - **Output:**  
   ```
   70
   ```

---

### **Final Output:**
```
[10, 20, [50, 60, 70], 30, 40]
5
[50, 60, 70]
50
60
70
```

This demonstrates **list insertion** and **nested list indexing** in Python.
---------------------------------------------------------------------------------------------------------------------------------------
a = [10, 20, 30, 40]  # Define list 'a'
b = [50, 60, 70]      # Define list 'b'

a.insert(2, b)        # Insert list 'b' at index 2 in 'a'

print(a)              # Print the updated list 'a'
print(len(a))         # Print the length of list 'a'

# Accessing elements
print(a[2])           # Print the inner list (list 'b')
print(a[2][0])        # Print 50 (first element of list 'b')
print(a[2][1])        # Print 60 (second element of list 'b')
print(a[2][2])        # Print 70 (third element of list 'b')
```

---

### **Step-by-step Execution:**
1. **Initial Lists:**  
   - `a = [10, 20, 30, 40]`
   - `b = [50, 60, 70]`
   
2. **Insert Operation:**  
   - `a.insert(2, b)` inserts `b` **at index 2** in `a`, shifting other elements to the right.  
   - Now, `a = [10, 20, [50, 60, 70], 30, 40]`
   
3. **`print(a)` Output:**  
   ```
   [10, 20, [50, 60, 70], 30, 40]
   ```

4. **`print(len(a))` Output:**  
   - The list `a` now has **5 elements** (`10`, `20`, `[50, 60, 70]`, `30`, `40`).
   ```
   5
   ```

5. **How to print the inner list?**  
   - The inner list is at **index 2**, so:
   ```python
   print(a[2])
   ```
   - **Output:**  
   ```
   [50, 60, 70]
   ```

6. **How to print `50`?**  
   - The first element of the inner list is at `a[2][0]`, so:
   ```python
   print(a[2][0])
   ```
   - **Output:**  
   ```
   50
   ```

7. **How to print `60`?**  
   - The second element of the inner list is at `a[2][1]`, so:
   ```python
   print(a[2][1])
   ```
   - **Output:**  
   ```
   60
   ```

8. **How to print `70`?**  
   - The third element of the inner list is at `a[2][2]`, so:
   ```python
   print(a[2][2])
   ```
   - **Output:**  
   ```
   70
   ```

---

### **Final Output:**
```
[10, 20, [50, 60, 70], 30, 40]
5
[50, 60, 70]
50
60
70
```

---

### **Explanation:**
- The `.insert(2, b)` method **does not merge** `b` into `a`. Instead, it **inserts `b` as a single element** (a sublist) at index 2.
- This is why `a[2]` contains `[50, 60, 70]`, and we need **two-level indexing** to access its elements.

---

This demonstrates **list insertion** and **nested list indexing** in Python. 
