#programs on recursion
def f1():
    a = 3  # Initializes a to 3
    if a > 0:
        print(a)  # Prints 3
        a = a - 1  # Decreases a to 2
        f1()  # Recursive call
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')

f1()
print('End')
```

### Recursive Execution:

1. **First Call (f1()):**
   - `a = 3`
   - Prints `3`
   - Calls `f1()` again before executing the remaining lines.

2. **Second Call (f1()):**
   - `a = 3` (Each call initializes `a` again)
   - Prints `3`
   - Calls `f1()` again.

3. **Third Call (f1()):**
   - `a = 3`
   - Prints `3`
   - Calls `f1()` again.

4. **Fourth Call (f1()):**
   - `a = 3`
   - Prints `3`
   - Calls `f1()` again.

   Since there is no base case to stop the recursion, this results in an **infinite recursion**, which will eventually lead to a `RecursionError` (maximum recursion depth exceeded).

### Expected Output Before the Error:
Before hitting the recursion limit, the program prints multiple `3`s:
```
3
3
3
...
(keeps repeating until the recursion limit is reached)
```
Then, Python raises:
```
RecursionError: maximum recursion depth exceeded
```

### Fixing the Issue:
To prevent infinite recursion, `a` should be passed as an argument:
```python
def f1(a):
    if a > 0:
        print(a)
        f1(a - 1)
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')

f1(3)
print('End')
```
This will terminate correctly and print the expected output.
---------------------------------------------------------------------------------------------------------

def f1(x , y):
    if x > 40:
        return
    x += y
    f1(x , y)
    print(x)
# End of function

x = 10
f1(x , x := x + 1)
print(x)
```
---

### **Step 1: Understanding `x := x + 1`**
The **walrus operator (`:=`)** is used for assignment within an expression. 

- Initially, `x = 10`
- In `f1(x, x := x + 1)`, `x` is updated to `11` before being passed to the function.
- So, the function call is equivalent to `f1(10, 11)`.

---

### **Step 2: Function Execution (`f1(10, 11)`)**
#### **Recursive Calls**
Each call updates `x` as:
1. `x = 10 + 11 = 21`
2. `x = 21 + 11 = 32`
3. `x = 32 + 11 = 43` (Exit condition: `x > 40`, so return)

#### **Backtracking & Printing (`print(x)`)**
Since `f1(43, 11)` returns without printing, we move back:
1. `print(32)`
2. `print(21)`

After recursion ends, the `print(x)` outside the function executes, printing:
```
11
```

---

### **Final Output**
```
32
21
11
```

---
-------------------------------------------------------------------------------------------------------------------------

def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator

while True:
    print(next(f1()))
```
- The function `f1()` is a **generator** because it uses `yield`.
- `yield` allows the function to produce a series of values **one at a time**, pausing between each, and resuming from the last `yield` when `next()` is called.
- However, **every time `f1()` is called, it creates a NEW generator starting from the beginning**.

---

### **Step-by-Step Execution**
1. The `while True` loop runs indefinitely.
2. Inside the loop, `next(f1())` is executed.
3. **Each call to `f1()` creates a new generator.**  
   - `next(f1())` is always executed on a **fresh generator**, so it always starts from `yield 25`.
4. This means **only the first value (25) is printed repeatedly**, and the remaining `yield` statements are never reached.

---

### **Final Output (Infinite Loop)**
```
25
25
25
25
...
```
*(This continues indefinitely.)*

---

### **Fixing the Issue**
If the intention is to iterate through all the values, we should **create a single generator instance** and call `next()` on it:

```python
g = f1()  # Create a generator object
while True:
    try:
        print(next(g))  # Fetch the next value from the generator
    except StopIteration:
        break  # Stop when the generator is exhausted
```

### **Corrected Output**
```
25
10.8
Hyd
```
---------------------------------------------------------------------------------------------------------------------------------------------------

import time

def f1():
    print('One')
    yield 25
    print('Two')
    yield 10.8
    print('Three')
    yield 'Hyd'
    print('Four')  # This runs after the last `yield`

# End of generator

g = f1()  # Create a generator object

for x in g:  # Iterate over the generator using a for loop
    print(x)
    time.sleep(1)
    print('Hello')
# End of for loop

print('End')  # Printed after the for loop completes

print(g)  # Prints the generator object

print(next(g))  # ERROR: The generator is exhausted at this point!

g = f1()  # Creating a new generator
print(next(g))  # This will work because it's a fresh generator
```

---

### **Step-by-Step Execution**
1. `g = f1()` creates a generator object.
2. The `for` loop starts iterating over `g`, calling `next(g)` internally:
   - First call:
     - Prints `'One'`
     - Yields `25`, which is printed.
     - Waits for 1 second.
     - Prints `'Hello'`
   - Second call:
     - Prints `'Two'`
     - Yields `10.8`, which is printed.
     - Waits for 1 second.
     - Prints `'Hello'`
   - Third call:
     - Prints `'Three'`
     - Yields `'Hyd'`, which is printed.
     - Waits for 1 second.
     - Prints `'Hello'`
   - Fourth call:
     - Prints `'Four'` (but does **not** yield anything).
     - The generator is **exhausted**.

3. The `for` loop ends.
4. Prints `'End'`
5. `print(g)` prints something like `<generator object f1 at 0x...>`.
6. `print(next(g))` **raises an error** (`StopIteration`) because the generator is **already exhausted**.
7. `g = f1()` creates a **new** generator.
8. `print(next(g))` starts from the **beginning**, printing `'One'` and `25`.

---

### **Expected Output**
```
One
25
Hello
Two
10.8
Hello
Three
Hyd
Hello
Four
End
<generator object f1 at 0x...>
Traceback (most recent call last):
  File "script.py", line XX, in <module>
    print(next(g))  # ERROR: Generator is exhausted
StopIteration

One
25
```

---

### **Key Takeaways**
1. **A `for` loop automatically handles `StopIteration`**:
   - Unlike `next()`, it stops when the generator is exhausted.
2. **Once a generator is exhausted, you need to create a new one** if you want to iterate again.
3. **Calling `next(g)` on an exhausted generator results in `StopIteration`**.
4. **A generator resumes from where it last yielded, until it reaches the end**.
----------------------------------------------------------------------------------------------------------------------------------
import time

g = (x * x for x in range(5))  # Generator expression

for y in g:  # First loop
    print(y)
    time.sleep(2)
    print('Hello')

for y in g:  # Second loop
    print(y)  # Will this print anything?
```

---

### **Step-by-Step Execution**
1. **Generator Creation**
   ```python
   g = (x * x for x in range(5))
   ```
   - This creates a generator that **lazily** computes `x * x` for `x` in `{0, 1, 2, 3, 4}`.

2. **First `for` Loop Iteration**
   - `y = 0 * 0 = 0`
     ```
     0
     (pauses for 2 seconds)
     Hello
     ```
   - `y = 1 * 1 = 1`
     ```
     1
     (pauses for 2 seconds)
     Hello
     ```
   - `y = 2 * 2 = 4`
     ```
     4
     (pauses for 2 seconds)
     Hello
     ```
   - `y = 3 * 3 = 9`
     ```
     9
     (pauses for 2 seconds)
     Hello
     ```
   - `y = 4 * 4 = 16`
     ```
     16
     (pauses for 2 seconds)
     Hello
     ```
   - **At this point, the generator `g` is exhausted**.

3. **Second `for` Loop Iteration**
   ```python
   for y in g:
       print(y)
   ```
   - **Since the generator is exhausted, this loop does nothing.**  
   - No values are left to iterate over.

---

### **Final Output**
```
0
Hello
1
Hello
4
Hello
9
Hello
16
Hello
```
(The second loop prints **nothing**.)

---

### **Key Takeaways**
1. **A generator can only be iterated once.**  
   - After a generator is exhausted, it **cannot be reused**.
2. **The second `for` loop does nothing because `g` has already been fully consumed** in the first loop.
3. **If you need to iterate again, create a new generator** before the second loop:
   ```python
   g = (x * x for x in range(5))  # Recreate generator
   for y in g:
       print(y)
   ```
------------------------------------------------------------------------------------------------------------------

import time

for y in (x * x for x in range(5)):  # First generator expression
    print(y)
    time.sleep(2)

for y in (x * x for x in range(5)):  # Second generator expression
    print(y)
    time.sleep(2)
```

---

### **Step-by-Step Execution**
1. **First `for` Loop Iteration**
   - A **new generator** is created: `(x * x for x in range(5))`
   - Iterates over `{0, 1, 2, 3, 4}`:
     ```
     0
     (pauses for 2 seconds)
     1
     (pauses for 2 seconds)
     4
     (pauses for 2 seconds)
     9
     (pauses for 2 seconds)
     16
     (pauses for 2 seconds)
     ```

2. **Second `for` Loop Iteration**
   - A **new generator** is created **again**: `(x * x for x in range(5))`
   - The same values `{0, 1, 2, 3, 4}` are **recomputed and printed again**:
     ```
     0
     (pauses for 2 seconds)
     1
     (pauses for 2 seconds)
     4
     (pauses for 2 seconds)
     9
     (pauses for 2 seconds)
     16
     (pauses for 2 seconds)
     ```

---

### **Final Output**
```
0
1
4
9
16
(Each with a 2-second delay)

0
1
4
9
16
(Each with a 2-second delay)
```
*(Total execution time ≈ 20 seconds.)*

---

### **Key Takeaways**
1. **Each `for` loop creates a new generator expression.**  
   - Since the generator is defined **inside** the loop, it starts from the beginning each time.
2. **Unlike an assigned generator (`g = (x*x for x in range(5))`), a fresh generator is created in each loop.**  
   - That’s why both loops run independently and print the same values.
-----------------------------------------------------------------------------------------------------------------------------

import time

g1 = (x * x for x in range(5))  # Generator expression
g2 = g1  # Both g1 and g2 point to the same generator

for y in g1:  # First iteration over g1 (which is also g2)
    print(y)
    time.sleep(2)

for y in g2:  # Second iteration over g2 (same generator)
    print(y)  # Will this print anything?

print(g1 is g2)  # Check if g1 and g2 refer to the same object
```

---

### **Step-by-Step Execution**
1. **Creating the Generator**
   ```python
   g1 = (x * x for x in range(5))
   g2 = g1  # g2 is assigned the same generator object as g1
   ```
   - `g1` and `g2` **both point to the same generator**.
   - This means **iterating over `g1` will also exhaust `g2`**.

2. **First `for` Loop Execution**
   - A generator iterates over `{0, 1, 4, 9, 16}`:
     ```
     0
     (pauses for 2 seconds)
     1
     (pauses for 2 seconds)
     4
     (pauses for 2 seconds)
     9
     (pauses for 2 seconds)
     16
     (pauses for 2 seconds)
     ```
   - **Now the generator is exhausted**.

3. **Second `for` Loop Execution**
   ```python
   for y in g2:
       print(y)
   ```
   - **Since `g2` is the same generator as `g1` and it has been fully consumed, this loop prints nothing**.

4. **Checking `g1 is g2`**
   ```python
   print(g1 is g2)
   ```
   - Since `g1` and `g2` are the **same object**, it prints:
     ```
     True
     ```

---

### **Final Output**
```
0
1
4
9
16
(True, because g1 and g2 are the same object)
```
*(Total execution time ≈ 10 seconds due to `time.sleep(2)`)*
*(The second loop prints nothing.)*

---

### **Key Takeaways**
1. **A generator can only be iterated once.**
2. **Assigning a generator to another variable (`g2 = g1`) does not create a new generator; both refer to the same object.**
3. **Once exhausted, a generator does not reset.** If you need to iterate again, **create a new generator**:
   ```python
   g1 = (x * x for x in range(5))  # Create a new generator
   for y in g1:
       print(y)
   ```
-------------------------------------------------------------------------------------------------------------------------------------

def f1():
    global a  # Using global variable 'a'
    if a:  # If 'a' is nonzero, execute the block
        print(a)
        a = a - 1  # Decrease 'a'
        f1()  # Recursive call
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')

a = 3  # Initialize global variable 'a'
f1()
print('End')
```

---

### **Step-by-Step Execution**
1. **Initial State:**  
   - `a = 3`
   - Call `f1()`

---

#### **First Call (`f1()`)**
- `a = 3` (not zero, so enter the `if` block)
- Prints `3`
- `a = 2`
- Calls `f1()` **(recursive call)**

---

#### **Second Call (`f1()`)**
- `a = 2` (not zero)
- Prints `2`
- `a = 1`
- Calls `f1()`

---

#### **Third Call (`f1()`)**
- `a = 1` (not zero)
- Prints `1`
- `a = 0`
- Calls `f1()`

---

#### **Fourth Call (`f1()`)**
- `a = 0` (zero, so `if` block is skipped)
- Prints `'Bye'`
- Returns to the **third call**.

---

#### **Back to Third Call (`f1() with a=1`)**
- Prints `'Hello'`
- Prints `'Hi'`
- Prints `0` (current value of `a`)
- Prints `'Bye'`
- Returns to the **second call**.

---

#### **Back to Second Call (`f1() with a=2`)**
- Prints `'Hello'`
- Prints `'Hi'`
- Prints `0` (current value of `a`)
- Prints `'Bye'`
- Returns to the **first call**.

---

#### **Back to First Call (`f1() with a=3`)**
- Prints `'Hello'`
- Prints `'Hi'`
- Prints `0` (current value of `a`)
- Prints `'Bye'`
- Returns to main execution.

---

#### **After `f1()` completes**
- Prints `'End'`

---

### **Final Output**
```
3
2
1
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
End
```

---

### **Key Takeaways**
1. **Recursive calls keep decreasing `a` until it reaches `0`**.
2. **Once `a` is `0`, the recursion stops** and starts backtracking.
3. **Backtracking prints `'Hello'`, `'Hi'`, and `a` before each function call ends**.
4. **Since `a` is global, it remains `0` after recursion completes**.
---------------------------------------------------------------------------------------------------------------

def f1():
    print('f1 function')
    f2()  # Calls f2()
    print('End of f1 function')

def f2():
    print('f2 function')
    f1()  # Calls f1()
    print('End of f2 function')

f1()  # Initial call
```

---

### **Step-by-Step Execution**
1. The program starts with `f1()`.
2. Inside `f1()`, it prints:
   ```
   f1 function
   ```
3. Then, `f1()` calls `f2()`.
4. Inside `f2()`, it prints:
   ```
   f2 function
   ```
5. `f2()` then calls `f1()` again, restarting the process.
6. This **recursion never stops**, leading to **infinite recursion**.
7. Eventually, Python reaches the **recursion depth limit** and raises a `RecursionError`.

---

### **Output (Before Error)**
```
f1 function
f2 function
f1 function
f2 function
f1 function
f2 function
...
(Repeats infinitely)
```
Eventually, Python throws:
```
RecursionError: maximum recursion depth exceeded
```

---

### **Key Takeaways**
1. **The function calls itself infinitely, causing a recursion error.**
2. **There is no base case** to stop recursion.
3. **Fix**: Add a stopping condition, like a counter:
   ```python
   def f1(n):
       if n == 0:
           return
       print('f1 function')
       f2(n - 1)
       print('End of f1 function')

   def f2(n):
       if n == 0:
           return
       print('f2 function')
       f1(n - 1)
       print('End of f2 function')

   f1(3)  # Controls recursion depth
   ```
   -----------------------------------------------------------------------------------------------------------------------

import time

def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator

g = f1()  # Create a generator object
print(next(g))  # Get the first yielded value

for x in g:  # Continue iterating from where `next(g)` left off
    print(x)

print()

for x in f1():  # New generator starts from the beginning
    print(x)

print()

gen = f1()  # Another generator object
print(next(gen))  # Get the first value

for x in f1():  # New generator starts from the beginning again
    print(x)

print(next(gen))  # Continue iteration from where `next(gen)` left off
```

---

### **Step-by-Step Execution**
1. **Create `g = f1()`**
2. **Call `next(g)`**  
   - `g` starts execution and yields `25`:
     ```
     25
     ```
3. **First `for` loop (`for x in g:`)**  
   - Continues from where `next(g)` left off:
     ```
     10.8
     Hyd
     ```
   - Now `g` is **exhausted**.
4. **Prints a blank line (`print()`)**
5. **Second `for` loop (`for x in f1():`)**  
   - A **new generator** is created, so it **starts from the beginning**:
     ```
     25
     10.8
     Hyd
     ```
6. **Prints another blank line (`print()`)**
7. **Create `gen = f1()` (new generator)**
8. **Call `next(gen)`**  
   - `gen` starts execution and yields `25`:
     ```
     25
     ```
9. **Third `for` loop (`for x in f1():`)**  
   - A **new generator** is created, so it **starts from the beginning**:
     ```
     25
     10.8
     Hyd
     ```
10. **Call `next(gen)` again**  
    - `gen` continues from where it left off and yields `10.8`:
      ```
      10.8
      ```

---

### **Final Output**
```
25
10.8
Hyd

25
10.8
Hyd

25
25
10.8
Hyd
10.8
```

---

### **Key Takeaways**
1. **A generator remembers its state.**
   - `next(g)` picks up from where the last call left off.
2. **A `for` loop fully consumes a generator.**
   - The first `for` loop resumes `g`, exhausting it.
3. **Each call to `f1()` creates a new generator.**
   - This is why `for x in f1():` starts fresh.
4. **If a generator is partially consumed, it resumes from there.**
   - `gen = f1()`, `next(gen)`, then `next(gen)` resumes where it left off.

