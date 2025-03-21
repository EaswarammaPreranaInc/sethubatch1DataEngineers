# Define a function named 'change' that modifies the input list
def change(b):
    # Append the value 25 to the end of the list
    b.append(25)
    
    # Change the element at index 2 (third element) to 17
    b[2] = 17
    
    # Delete the element at index 1 (second element)
    del b[1]

# Initialize a list 'a' with four elements
a = [10, 20, 15, 18]

# Print the original list before calling the function
print("Before function call:", a)

# Call the function 'change' and pass the list 'a'
change(a)

# Print the modified list after calling the function
print("After function call:", a)
```

### Expected Output:
```
Before function call: [10, 20, 15, 18]
After function call: [10, 17, 18, 25]
```  

This program demonstrates how lists are mutable in Python, meaning that modifications inside a function affect the original list.
-----------------------------------------------------------------------------------------------------------------------------------------------------
Here's the Python program with detailed comments explaining each step:  

```python
# Define a function named 'change' that attempts to modify the input list
def change(b):
    # Assign a new list to 'b', creating a local variable
    b = [50, 60, 70, 80]  # This does NOT modify the original list 'a'
    
    # Print the new local list 'b' (this is separate from 'a')
    print("Inside function:", b)

# Initialize a list 'a' with four elements
a = [10, 20, 30, 40]

# Print the original list before calling the function
print("Before function call:", a)

# Call the function 'change' and pass the list 'a'
change(a)

# Print the original list after calling the function
print("After function call:", a)
```

### **Expected Output:**
```
Before function call: [10, 20, 30, 40]  # Original list before function call
Inside function: [50, 60, 70, 80]       # New local list inside function
After function call: [10, 20, 30, 40]   # Original list remains unchanged
```

### **Explanation:**
1. The function `change(b)` is called with `a` as an argument.
2. Inside the function, `b` is assigned a **new list**, meaning it now refers to a different object in memory.
3. Since `b` is now a local variable, the original list `a` remains unchanged.
4. After the function finishes, `a` is printed again, showing that it is still `[10, 20, 30, 40]`.

### **Key Concept:**
- Assigning `b = [50, 60, 70, 80]` inside the function **creates a new list** instead of modifying the original list `a`.  
- If we wanted to modify `a`, we would need to modify `b` **in place**, e.g., `b.append(50)` or `b[0] = 99`.
------------------------------------------------------------------------------------------------------------------------------------
Here's the Python program with detailed comments explaining each step:

```python
# Define a function named 'f1' that takes a parameter 'x'
def f1(x):
    # Assign a new value to 'x', but this only affects the local copy inside the function
    x = 20  # This does NOT change the global 'x'
    
    # Print the local variable 'x'
    print("Inside function:", x)

# Initialize a global variable 'x' with the value 10
x = 10

# Print the value of 'x' before calling the function
print("Before function call:", x)

# Call the function 'f1' and pass 'x' as an argument
f1(x)  # Inside the function, 'x' is locally changed to 20

# Print the value of 'x' after calling the function
print("After function call:", x)  # 'x' remains unchanged outside the function
```

### **Expected Output:**
```
Before function call: 10  # Original global variable 'x'
Inside function: 20       # Local variable 'x' inside the function
After function call: 10   # Global 'x' remains unchanged
```

---

### **Explanation:**
1. The function `f1(x)` is called with `x = 10` as an argument.
2. Inside the function:
   - `x = 20` creates a **new local variable**, separate from the global `x`.
   - The function prints `x`, which is now `20` (but only inside the function).
3. After the function call, `x` outside the function remains `10` because the local `x` inside the function is discarded after execution.

---

### **Key Concept:**
- Assigning `x = 20` inside the function **does not change the global variable** `x`.
- If we wanted to modify the global `x`, we would need to use the `global` keyword:
  ```python
  def f1():
      global x
      x = 20
  ```
  This would allow the function to modify `x` globally.
  ------------------------------------------------------------------------------------------------------------------------------------------------------
  Here's the Python program with detailed comments explaining each step:  

```python
# Define a function 'f1' that attempts to modify the input parameter 'b'
def f1(b):
    # Try to change the element at index 2 (third element) to 25
    b[2] = 25  # This will cause an error if 'b' is a tuple

# Initialize 'a' as a tuple with four elements
a = (10, 20, 15, 18)  # Tuples are immutable (cannot be changed)

# Print the original tuple before calling the function
print("Before function call:", a)

# Call the function 'f1' and pass 'a' as an argument
# This will raise a TypeError because tuples do not allow item assignment
f1(a)

# Print the tuple after calling the function (this line won't execute due to the error)
print("After function call:", a)
```

### **Expected Output:**
```
Before function call: (10, 20, 15, 18)
Traceback (most recent call last):
  File "script.py", line X, in <module>
    f1(a)
  File "script.py", line X, in f1
    b[2] = 25
TypeError: 'tuple' object does not support item assignment
```

---

### **Explanation:**
1. `a` is defined as a **tuple**, which means its elements **cannot be modified**.
2. The first `print` statement executes successfully.
3. The function `f1(a)` is called, where it tries to change `b[2] = 25`.
4. Since `b` is a reference to `a`, and `a` is a tuple, Python raises a **TypeError** because tuples do not support element reassignment.
5. The second `print` statement (`print("After function call:", a)`) **never executes** because the program crashes with the error.

---

### **Solution (Using a List Instead of a Tuple):**
If we want to modify elements inside the function, we should use a **list** instead of a tuple:

```python
a = [10, 20, 15, 18]  # Use a list instead of a tuple
```

Then, the function would successfully change the third element (`15 → 25`), and the output would be:

```
Before function call: [10, 20, 15, 18]
After function call: [10, 20, 25, 18]
```
