def f1():
    print('f1 function')

def f2(fun):
    print('f2 function')
    fun()  # Calls the function passed as an argument
    print('Back to f2 function')

# end of the function

print('Begin')
f2(f1)  # Calling f2 and passing f1 as an argument
print('End')
```

### Step-by-step Execution:

1. **`print('Begin')`**  
   Output:  
   ```
   Begin
   ```

2. **`f2(f1)`** is called, which means:
   - The function `f2` is executed, and `fun` refers to `f1`.
   - Inside `f2`, `print('f2 function')` executes.
   - Output:  
     ```
     f2 function
     ```

3. **Calling `fun()`, which is `f1()`**  
   - `f1` executes, which prints `'f1 function'`.
   - Output:  
     ```
     f1 function
     ```

4. **Returning to `f2`, executing `print('Back to f2 function')`**  
   - Output:  
     ```
     Back to f2 function
     ```

5. **`print('End')`** executes.  
   - Output:  
     ```
     End
     ```

### Final Output:
```
Begin
f2 function
f1 function
Back to f2 function
End
```
--------------------------------------------------------------------------------------------------------------------------------
Let's analyze the execution of the given Python script step by step:

```python
def f1():
    print('f1 function')

def f2(fun):
    print('f2 function')
    fun()
    print('Back to f2 function')

# end of the function

print('Begin')
f2(f1())  # Calling f1() first, then passing its result to f2
print('End')
```

### Step-by-step Execution:

1. **`print('Begin')`** executes:  
   **Output:**
   ```
   Begin
   ```

2. **`f2(f1())`** is called:
   - **First, `f1()` is executed immediately before calling `f2`.**
   - `f1()` prints `'f1 function'`.  
     **Output:**
     ```
     f1 function
     ```
   - **`f1()` does not return anything (implicitly returns `None`).**
   - The result of `f1()` (`None`) is passed to `f2`, so `f2(None)` is executed.

3. **Inside `f2(None)`:**
   - `print('f2 function')` executes.  
     **Output:**
     ```
     f2 function
     ```
   - The next line `fun()` tries to execute `None()`, which causes an **error**:  
     **TypeError: 'NoneType' object is not callable**  
     The program crashes here, and **the remaining lines are not executed.**

### **Final Output before the Error:**
```
Begin
f1 function
f2 function
```
Then, a **TypeError** occurs.

### **Corrected Code:**
If you intended to pass `f1` as a function reference instead of calling it first, you should write:
```python
f2(f1)  # Pass function reference, not f1()
```
This would correctly output:
```
Begin
f2 function
f1 function
Back to f2 function
End
```
-------------------------------------------------------------------------------------------------------------------------
Let's analyze the execution of the given Python script step by step:

```python
def outer():
    print('Outer Function')
    
    def inner():
        print('Inner function')
    
    return inner

# End of the function

fun = outer()  # Calling outer(), which prints 'Outer Function' and returns inner
print('Hello')
fun()  # Calling the function returned by outer(), which is inner()
print('Bye')
inner()  # This will cause an error because inner() is not defined in the global scope.
```

### **Step-by-step Execution:**

1. **`fun = outer()`**  
   - Calls `outer()`, which prints `'Outer Function'`.  
   - The function `inner` is **returned** but not executed yet.  
   **Output so far:**
   ```
   Outer Function
   ```

2. **`print('Hello')`** executes.  
   **Output so far:**
   ```
   Outer Function
   Hello
   ```

3. **`fun()`** (which is `inner()`) executes.  
   - This prints `'Inner function'`.  
   **Output so far:**
   ```
   Outer Function
   Hello
   Inner function
   ```

4. **`print('Bye')`** executes.  
   **Output so far:**
   ```
   Outer Function
   Hello
   Inner function
   Bye
   ```

5. **`inner()`** is called directly.  
   - However, `inner` is a local function **inside** `outer()` and is **not defined globally**.  
   - This causes a **NameError**:  
     ```
     NameError: name 'inner' is not defined
     ```

### **Final Output before the Error:**
```
Outer Function
Hello
Inner function
Bye
```
Then, a **NameError** occurs.

---

### **Fixing the Error:**
If you want to call `inner()` properly, you should use `fun()`, since `fun` holds the reference to `inner`.  
```python
fun()  # Instead of inner()
```
Or, you can directly call it after `outer()` like this:
```python
outer()()  # This calls outer(), then calls inner() immediately
```
--------------------------------------------------------------------------------------------------------------------
Let's analyze the execution of the given Python script step by step:

```python
def outer(x):
    print('Outer Function')

    def inner1():
        print('1st inner function')

    def inner2():
        print('2nd inner function')

    if x == 10:
        return inner1
    else:
        return inner2

# End of the function

f1 = outer(10)  # Calls outer(10)
f2 = outer(20)  # Calls outer(20)

f1()  # Calls the function returned by outer(10), which is inner1()
f2()  # Calls the function returned by outer(20), which is inner2()
```

---

### **Step-by-step Execution:**

1. **`f1 = outer(10)`**
   - Calls `outer(10)`, so **`print('Outer Function')`** executes.  
   - Since `x == 10`, **`inner1` is returned**.
   **Output so far:**
   ```
   Outer Function
   ```

2. **`f2 = outer(20)`**
   - Calls `outer(20)`, so **`print('Outer Function')`** executes again.  
   - Since `x != 10`, **`inner2` is returned**.
   **Output so far:**
   ```
   Outer Function
   Outer Function
   ```

3. **`f1()` executes (which is `inner1()`)**
   - **`print('1st inner function')`** executes.  
   **Output so far:**
   ```
   Outer Function
   Outer Function
   1st inner function
   ```

4. **`f2()` executes (which is `inner2()`)**
   - **`print("2nd inner function")`** executes.  
   **Final Output:**
   ```
   Outer Function
   Outer Function
   1st inner function
   2nd inner function
   ```

---

### **Final Output:**
```
Outer Function
Outer Function
1st inner function
2nd inner function
```
----------------------------------------------------------------------------------------------------------
Let's analyze the execution of the given Python script step by step:

```python
def outer(msg):
    def inner():
        print(msg)
    return inner

# End of the function

hi_fun = outer('Hi')      # Calls outer('Hi'), which returns inner
hello_fun = outer('Hello') # Calls outer('Hello'), which returns inner

hi_fun()     # Calls the inner function returned by outer('Hi')
hello_fun()  # Calls the inner function returned by outer('Hello')
```

---

### **Step-by-step Execution:**

1. **`hi_fun = outer('Hi')`**
   - Calls `outer('Hi')`, which **creates `inner()` and captures `msg='Hi'`**.
   - Returns `inner`, which is now stored in `hi_fun`.

2. **`hello_fun = outer('Hello')`**
   - Calls `outer('Hello')`, which **creates `inner()` and captures `msg='Hello'`**.
   - Returns `inner`, which is now stored in `hello_fun`.

3. **`hi_fun()` executes**
   - This calls `inner()` that was created in `outer('Hi')`, so **`print(msg)` prints `'Hi'`**.
   **Output so far:**
   ```
   Hi
   ```

4. **`hello_fun()` executes**
   - This calls `inner()` that was created in `outer('Hello')`, so **`print(msg)` prints `'Hello'`**.
   **Final Output:**
   ```
   Hi
   Hello
   ```

---

### **Final Output:**
```
Hi
Hello
```
--------------------------------------------------------------------------------------------------------------
Let's analyze the execution of the given Python script step by step:

```python
def decor(fun):
    print(fun.__name__)  # Prints the name of the function being decorated
    def inner():
        return fun() + 2
    return inner

@decor  # This applies the decor function to f1()
def f1():
    return 10

# End of the function
print('End')
```

---

### **Step-by-step Execution:**

1. **Applying the `@decor` decorator to `f1()`**  
   - The `decor` function is called with `fun = f1`.  
   - `print(fun.__name__)` executes, printing:  
     ```
     f1
     ```
   - The `decor` function **returns the `inner` function**, replacing `f1` with `inner`.  
   - Now, `f1()` **is no longer the original function but instead refers to `inner()`**.

2. **`print('End')`** executes.  
   **Final Output:**
   ```
   f1
   End
   ```

---

### **Key Observations:**
- The function `f1()` **is never called in this script**, so `inner()` is never executed.
- The decorator executes **at the time of function definition**, printing `f1`.
- Since `f1()` is not called anywhere, `inner()` is never executed, and we don’t see any additional output.

---

### **Final Output:**
```
f1
End
```

---

### **What if `f1()` were called?**
If we added `print(f1())` at the end:
```python
print(f1())
```
Then, the execution would be:

1. `f1` (actually `inner`) is called.
2. `inner()` calls `fun()`, which is the original `f1()`, returning `10`.
3. `inner()` adds `2` to the result (`10 + 2`), returning `12`.

**Modified Output:**
```
f1
End
12
```
--------------------------------------------------------------------------------------------------------------
If the `@decor` decorator tag is missing, you can manually apply the decorator function to `f1` by explicitly passing `f1` to `decor`, as shown in your code:

```python
def decor(fun):
    def inner():
        x = fun()
        return x + 2
    return inner

def f1():
    return 10

# end of the function

f1 = decor(f1)  # Manually applying the decorator
print(f1())  # Calling the decorated function
```

### **Step-by-step Execution:**
1. `f1 = decor(f1)`  
   - Calls `decor(f1)`, passing the original `f1` function.
   - `decor` returns `inner`, so now `f1` refers to `inner`.

2. `print(f1())`  
   - Since `f1` now refers to `inner`, `inner()` executes.
   - `inner()` calls `fun()`, which is the original `f1()`, returning `10`.
   - `inner()` adds `2` to the result (`10 + 2`), returning `12`.

### **Final Output:**
```
12
```

This is how you manually apply a decorator when the `@decor` syntax is not used. 
----------------------------------------------------------------------------------------------------------
Let's analyze the execution of the given Python script step by step:

```python
def decor(fun):
    def inner(x, y):
        try:
            return fun(x, y)
        except:
            return 'Division by 0 is not permitted'
    return inner

@decor  # Applying the decorator to div
def div(a, b):
    return a / b

# End of the function

print(div(10, 3))  # Calling the decorated div function
print(div(10, 0))  # Calling the decorated div function
print(inner(10, 3))  # This will cause an error!
```

---

### **Step-by-step Execution:**

1. **Applying the `@decor` decorator to `div`**  
   - The `decor` function is called with `fun = div`.  
   - The `decor` function returns `inner`, so `div` is now replaced with `inner`.

2. **Executing `print(div(10, 3))`**  
   - Since `div` is now `inner`, `inner(10, 3)` executes.
   - Inside `inner`, `fun(10, 3)` (which is `div(10, 3)`) is called.
   - `div(10, 3)` returns `10 / 3 = 3.3333...`, so `inner` returns `3.3333...`.  
   **Output so far:**
   ```
   3.3333333333333335
   ```

3. **Executing `print(div(10, 0))`**  
   - `div(10, 0)` is actually `inner(10, 0)`.
   - Inside `inner`, `fun(10, 0)` (which is `div(10, 0)`) is called.
   - `div(10, 0)` raises a `ZeroDivisionError`, so `except` block runs.
   - `inner` returns `'Division by 0 is not permitted'`.  
   **Output so far:**
   ```
   3.3333333333333335
   Division by 0 is not permitted
   ```

4. **Executing `print(inner(10, 3))`**  
   - **Error!**  
   - `inner(10, 3)` is **not defined in the global scope**.
   - `inner` is **only defined inside `decor`**, and it is not directly accessible.
   - This will cause a **NameError**:  
     ```
     NameError: name 'inner' is not defined
     ```

---

### **Final Output Before the Error:**
```
3.3333333333333335
Division by 0 is not permitted
```
Then, a **NameError** occurs.

---

### **Fixing the Error:**
If you want to call `inner(10, 3)`, you **must call `div(10, 3)`** instead because `div` now refers to `inner`:
```python
print(div(10, 3))  # Correct way to call inner
```
or store `inner` in another variable:
```python
new_div = decor(div)
print(new_div(10, 3))  # This will work
```
-----------------------------------------------------------------------------------------------------------------------
You can modify the `decor` function so that it **checks for specific inputs** `(9, 2)` and `(2, 9)` and always returns `4.5` for those cases. Otherwise, it will perform normal division.

Here’s the modified code:

```python
def decor(fun):
    def inner(a, b):
        if (a, b) == (9, 2) or (a, b) == (2, 9):
            return 4.5  # Hardcoded result for these inputs
        return fun(a, b)  # Otherwise, perform normal division
    return inner

@decor
def div(a, b):
    return a / b

print(div(9, 2))  # 4.5
print(div(2, 9))  # 4.5
print(div(10, 2)) # 5.0 (normal behavior)
```

### **How It Works:**
1. **When `div(9, 2)` or `div(2, 9)` is called** → The decorator **forces** the return value to `4.5`.
2. **For any other values** → It **performs normal division**.

### **Expected Output:**
```
4.5
4.5
5.0
```

This approach ensures the function behaves normally except for the specific cases you wanted to modify. 
----------------------------------------------------------------------------------------------------------
Let's analyze the execution of the given Python script step by step:

```python
def decor(fun):
    def inner():
        print(f'Decorating {fun.__name__} function')  # Prints function name being decorated
        fun()  # Calls the original function
        print('Decoration is finished')  # Prints after calling the function
    return inner

@decor  # Applying the decorator to f1
def f1():
    print('Hello')

# End of the function

f1()  # Calling the decorated function
print('Bye')  # Printing 'Bye'
```

---

### **Step-by-step Execution:**

1. **Applying the `@decor` decorator to `f1()`**  
   - The `decor` function is called with `fun = f1`.  
   - It returns `inner`, so now `f1` refers to `inner`.

2. **Executing `f1()`**  
   - Since `f1` now refers to `inner()`, `inner()` executes.
   - `inner()` prints:  
     ```
     Decorating f1 function
     ```
   - `inner()` calls `fun()`, which is the original `f1()`, so `f1()` prints:  
     ```
     Hello
     ```
   - `inner()` prints:  
     ```
     Decoration is finished
     ```

3. **Executing `print('Bye')`**  
   - Prints:  
     ```
     Bye
     ```

---

### **Final Output:**
```
Decorating f1 function
Hello
Decoration is finished
Bye
```

The decorator **adds extra functionality** before and after calling `f1()`. 
---------------------------------------------------------------------------------------------
Let's analyze the execution of the given Python script step by step:

---

### **Understanding the `decor` Function**
```python
def decor(fun):
    print(fun.__name__)  # Prints the function name during decoration
    def inner(*x):  # `inner` can accept any number of arguments
        print(x)  # Prints the tuple of arguments passed
        fun(*x)  # Calls the original function with unpacked arguments
        print('End of decoration')  # Prints after calling the function
    return inner
```
- This decorator prints the function name when it is applied.
- The `inner` function takes any number of arguments (`*x`).
- It prints the arguments, calls the original function, and prints `"End of decoration"`.

---

### **Decorating Functions**
```python
@decor
def f1(x):
    print('f1 function : ', x)
```
- When the script encounters `@decor`, it **immediately calls `decor(f1)`**.
- This prints `"f1"`, then replaces `f1` with `inner`.

Similarly, the following functions are also decorated:
```python
@decor
def f2(x, y):
    print('f2 function : ', x, y)

@decor
def f3(x, y, z):
    print('f3 function : ', x, y, z)

@decor
def f4():
    print('f4 function')
```
- Each function is replaced with `inner`.
- Each function name (`f2`, `f3`, `f4`) is printed **during decoration**.

---

### **Execution Step-by-Step**
#### **During Function Decoration**
At the time of defining functions, the `decor` function runs **once per function**, printing:
```
f1
f2
f3
f4
```

---

#### **Calling the Functions**
##### 1️⃣ `f1(10)`
- `inner(10)` runs because `f1 = inner`.
- Prints:
  ```
  (10,)
  ```
- Calls `f1(10)`, printing:
  ```
  f1 function :  10
  ```
- Prints:
  ```
  End of decoration
  ```

##### 2️⃣ `f2(25, 10.8)`
- `inner(25, 10.8)` runs because `f2 = inner`.
- Prints:
  ```
  (25, 10.8)
  ```
- Calls `f2(25, 10.8)`, printing:
  ```
  f2 function :  25 10.8
  ```
- Prints:
  ```
  End of decoration
  ```

##### 3️⃣ `f3('Hyd', True, 3 + 4j)`
- `inner('Hyd', True, 3 + 4j)` runs because `f3 = inner`.
- Prints:
  ```
  ('Hyd', True, (3+4j))
  ```
- Calls `f3('Hyd', True, 3 + 4j)`, printing:
  ```
  f3 function :  Hyd True (3+4j)
  ```
- Prints:
  ```
  End of decoration
  ```

##### 4️⃣ `f4()`
- `inner()` runs because `f4 = inner`.
- Prints:
  ```
  ()
  ```
- Calls `f4()`, printing:
  ```
  f4 function
  ```
- Prints:
  ```
  End of decoration
  ```

---

### **Final Output**
```
f1
f2
f3
f4
(10,)
f1 function :  10
End of decoration
(25, 10.8)
f2 function :  25 10.8
End of decoration
('Hyd', True, (3+4j))
f3 function :  Hyd True (3+4j)
End of decoration
()
f4 function
End of decoration
```

### **Summary**
- The decorator **prints the function name when applied**.
- Each function is replaced by `inner`, which **prints the arguments, calls the original function, and prints "End of decoration"**.
- This ensures **consistent behavior** across functions with different signatures.

Great use of decorators for handling multiple functions! 
--------------------------------------------------------------------------------------------------------------------------------------
Let's analyze the execution of the given Python script step by step.

---

### **Understanding the Decorators**
#### **1️⃣ `square` Decorator**
```python
def square(fun):
    def inner1():
        x = fun()  # Calls the original function and stores the result
        return x * x  # Returns the square of the result
    return inner1
```
- It **calls the original function**, stores the result in `x`, and **returns `x * x`**.

#### **2️⃣ `double` Decorator**
```python
def double(fun):
    def inner2():
        y = fun()  # Calls the function and stores the result
        return 2 * y  # Returns double the result
    return inner2
```
- It **calls the function**, stores the result in `y`, and **returns `2 * y`**.

---

### **Applying the Decorators**
```python
@double
@square
def num():
    return 10
```
- **First**, `@square` is applied to `num`, replacing `num` with `inner1` from `square`.
- **Then**, `@double` is applied to `inner1`, replacing `num` with `inner2` from `double`.

---

### **Execution Step-by-Step**
#### **1️⃣ `num()` is called**
Since `num` is now `inner2` (from `double`), `inner2()` runs:

```python
def inner2():
    y = fun()  # fun is `inner1`
    return 2 * y
```
- **Calls `inner1()`** because `fun = inner1` (from `square`).

#### **2️⃣ `inner1()` is called**
Since `fun` inside `inner1` is the original `num()`:

```python
def inner1():
    x = fun()  # Calls the original num() function
    return x * x  # Squares the result
```
- Calls `num()`, which returns `10`.
- `x = 10`, so `inner1()` returns `10 * 10 = 100`.

#### **3️⃣ Back to `inner2()`**
- `y = inner1() = 100`
- `inner2()` returns `2 * 100 = 200`.

---

### **Final Output**
```python
print(num())  # 200
```
**Output:**
```
200
```

### **Explanation of the Output**
- `square` **first** squares `10 → 100`
- `double` **then** doubles `100 → 200`

So, the final output is **`200`**. 
------------------------------------------------------------------------------------------------------------
Let's analyze the execution of the given Python script step by step.

---

### **Understanding the Decorators**
Each decorator **wraps** the function output inside an HTML-like tag.

#### **1️⃣ `bold` Decorator**
```python
def bold(fun):
    def inner1():
        return '<b>' + fun() + '</b>'  # Wraps the output in <b> tags
    return inner1
```

#### **2️⃣ `italic` Decorator**
```python
def italic(fun):
    def inner2():
        return '<i>' + fun() + '</i>'  # Wraps the output in <i> tags
    return inner2
```

#### **3️⃣ `underline` Decorator**
```python
def underline(fun):
    def inner3():
        return '<u>' + fun() + '</u>'  # Wraps the output in <u> tags
    return inner3
```

---

### **Applying the Decorators**
```python
@bold
@italic
@underline
def f1():
    return 'Hello World'
```
- **First, `@underline` is applied** → `f1` is replaced with `inner3` from `underline`.
- **Then, `@italic` is applied** → `f1` is replaced with `inner2` from `italic`.
- **Finally, `@bold` is applied** → `f1` is replaced with `inner1` from `bold`.

---

### **Execution Step-by-Step**
#### **1️⃣ Calling `f1()`**
Since `f1` is now `inner1()` (from `bold`), `inner1()` runs:

```python
def inner1():
    return '<b>' + fun() + '</b>'
```
- Calls `fun()`, which is `inner2()`.

#### **2️⃣ `inner2()` is called**
Since `fun` inside `inner2` is `inner3()`:

```python
def inner2():
    return '<i>' + fun() + '</i>'
```
- Calls `fun()`, which is `inner3()`.

#### **3️⃣ `inner3()` is called**
Since `fun` inside `inner3` is the original `f1()`:

```python
def inner3():
    return '<u>' + fun() + '</u>'
```
- Calls `f1()`, which returns `'Hello World'`.

#### **4️⃣ Back to `inner3()`**
- `inner3()` returns:
  ```html
  <u>Hello World</u>
  ```

#### **5️⃣ Back to `inner2()`**
- `inner2()` returns:
  ```html
  <i><u>Hello World</u></i>
  ```

#### **6️⃣ Back to `inner1()`**
- `inner1()` returns:
  ```html
  <b><i><u>Hello World</u></i></b>
  ```

---

### **Final Output**
```python
print(f1())
```
**Output:**
```html
<b><i><u>Hello World</u></i></b>
```

---

### **Explanation of the Output**
- `underline` **first** wraps the text: `<u>Hello World</u>`
- `italic` **then** wraps it: `<i><u>Hello World</u></i>`
- `bold` **finally** wraps it: `<b><i><u>Hello World</u></i></b>`

The output is **a fully formatted HTML string** with bold, italic, and underline tags applied in the correct nested order.

This is a great example of **decorators stacking** to modify a function’s output! 
----------------------------------------------------------------------------------------------------------------------------
Here’s the recursive implementation of the **Greatest Common Divisor (GCD)** function using **Euclidean Algorithm**:

---

### **Recursive GCD Function**
```python
def gcd(m, n):
    if n == 0:  # Base case: if the second number becomes 0, return the first number
        return m
    else:
        return gcd(n, m % n)  # Recursive case: call gcd with (n, remainder of m/n)

# Taking user input
m = int(input('Enter any number: '))
n = int(input('Enter any number: '))

# Calling the gcd function and printing result
print('Gcd:', gcd(m, n))
```

---

### **How It Works (Example Walkthrough)**

#### **Example 1: `gcd(12, 15)`**
1. `gcd(12, 15)` → Calls `gcd(15, 12 % 15)` → `gcd(15, 12)`
2. `gcd(15, 12)` → Calls `gcd(12, 15 % 12)` → `gcd(12, 3)`
3. `gcd(12, 3)` → Calls `gcd(3, 12 % 3)` → `gcd(3, 0)`
4. `gcd(3, 0)` → Returns `3` (Base case)

✅ **Final Answer:** `gcd(12, 15) = 3`

---

#### **Example 2: `gcd(4, 7)`**
1. `gcd(4, 7)` → Calls `gcd(7, 4 % 7)` → `gcd(7, 4)`
2. `gcd(7, 4)` → Calls `gcd(4, 7 % 4)` → `gcd(4, 3)`
3. `gcd(4, 3)` → Calls `gcd(3, 4 % 3)` → `gcd(3, 1)`
4. `gcd(3, 1)` → Calls `gcd(1, 3 % 1)` → `gcd(1, 0)`
5. `gcd(1, 0)` → Returns `1` (Base case)

✅ **Final Answer:** `gcd(4, 7) = 1`

---

### **Key Concept**
- The function **keeps reducing** the numbers by replacing `m` with `n` and `n` with `m % n`.
- When `n` becomes `0`, the function **returns `m`**, which is the GCD.

This method ensures an **efficient solution** with **O(log(min(m, n)))** time complexity.

 **Try running the code and check for different values!**
 -----------------------------------------------------------------------------------------------------------------------
 Here’s the **recursive implementation** of the **Sum of Digits (SOD)** function:  

---

### **Recursive Function for Sum of Digits**
```python
def sod(n):
    if n == 0:  # Base case: if n is 0, return 0
        return 0
    else:
        return (n % 10) + sod(n // 10)  # Recursive case: extract last digit and add to recursive call

# Taking user input
n = int(input('Enter any number: '))

# Calling the function and printing result
print('Sum of the digits:', sod(n))
```

---

### **How It Works (Example Walkthrough)**

#### **Example: `sod(678)`**
1. `sod(678) = 678 % 10 + sod(678 // 10) = 8 + sod(67)`
2. `sod(67) = 67 % 10 + sod(67 // 10) = 7 + sod(6)`
3. `sod(6) = 6 % 10 + sod(6 // 10) = 6 + sod(0)`
4. `sod(0) = 0` (Base case)

✅ **Final Answer:** `8 + 7 + 6 + 0 = 21`

---

### **Function Call Analysis**
- **For `sod(678)`:** It makes **4 function calls** (one for each digit + base case).
- **For an `n`-digit number:** It makes **(n + 1) function calls** (n recursive calls + base case).

---

### **Example Output**
#### **Input:**
```
Enter any number: 9427
```
#### **Recursive Breakdown:**
```
sod(9427) = 7 + sod(942)
sod(942)  = 2 + sod(94)
sod(94)   = 4 + sod(9)
sod(9)    = 9 + sod(0)
sod(0)    = 0  (Base case)
```
#### **Output:**
```
Sum of the digits: 22
```

---

This approach ensures a **clear and efficient** way to calculate the sum of digits using recursion. 
----------------------------------------------------------------------------------------------------------------
Here’s the **recursive implementation** of the Fibonacci series along with the function call breakdown.  

---

### **Recursive Fibonacci Function**
```python
def fib(i):  # 'i' is the term number
    if i == 0:  # Base case: first term is 0
        return 0
    if i == 1:  # Base case: second term is 1
        return 1
    return fib(i - 1) + fib(i - 2)  # Recursive case: sum of previous two terms

# Taking user input for number of terms
n = int(input('How many terms? : '))

# Generating and printing Fibonacci series
print('Fibonacci series:')
for i in range(n):
    print(fib(i), end=' ')
```

---

### **Understanding Fibonacci Formula**
- **Recursive Formula**:
  \[
  F(i) = F(i-1) + F(i-2)
  \]
- **Base Cases**:
  - \( F(0) = 0 \)
  - \( F(1) = 1 \)

---

### **Example Walkthrough: `fib(5)`**
The recursive function calls follow this pattern:

```
fib(5) = fib(4) + fib(3)
fib(4) = fib(3) + fib(2)
fib(3) = fib(2) + fib(1)
fib(2) = fib(1) + fib(0)
fib(1) = 1
fib(0) = 0
```

---

### **Function Call Breakdown**
| Function Call | Number of Calls | Result |
|--------------|---------------|--------|
| `fib(1)` | 1 | `1` |
| `fib(2)` | 1 | `fib(1) + fib(0) = 1 + 0 = 1` |
| `fib(3)` | 2 | `fib(2) + fib(1) = 1 + 1 = 2` |
| `fib(4)` | 3 | `fib(3) + fib(2) = 2 + 1 = 3` |
| `fib(5)` | 5 | `fib(4) + fib(3) = 3 + 2 = 5` |
| `fib(6)` | 8 | `fib(5) + fib(4) = 5 + 3 = 8` |
| `fib(7)` | 13 | `fib(6) + fib(5) = 8 + 5 = 13` |

---

### **Example Output**
#### **Input:**
```
How many terms? : 7
```
#### **Output:**
```
Fibonacci series:
0 1 1 2 3 5 8
```

---

### **Optimized Approach Using Memoization**
Since the recursive approach has **O(2ⁿ) time complexity**, we can optimize it using **memoization**:

```python
def fib_memo(i, memo={}):
    if i in memo:
        return memo[i]
    if i == 0:
        return 0
    if i == 1:
        return 1
    memo[i] = fib_memo(i - 1, memo) + fib_memo(i - 2, memo)
    return memo[i]

n = int(input('How many terms? : '))
print('Fibonacci series:')
for i in range(n):
    print(fib_memo(i), end=' ')
```

This **reduces time complexity** to **O(n)**, making it much faster for large values of `n`. 
------------------------------------------------------------------------------------------------------------------------
Here's the recursive implementation of the **power function** that handles both positive and negative exponents.  

---

### **Recursive Power Function**
```python
def power(a, b):
    # Base case: anything raised to power 0 is 1
    if b == 0:
        return 1
    # If exponent is negative, use reciprocal
    if b < 0:
        return 1 / power(a, -b)
    # Recursive case: multiply base 'a' by the result of 'a' raised to (b-1)
    return a * power(a, b - 1)

# Taking user input
a = float(input('Enter base: '))
b = int(input('Enter power: '))

# Printing result
print(f"{a} ^ {b} = {power(a, b)}")
```

---

### **Understanding Recursive Formula**
1) **For positive exponents**  
   \[
   a^b = a \times a^{b-1}
   \]
   Example:  
   \[
   4.5^3 = 4.5 \times 4.5^2
   \]
   
2) **For negative exponents**  
   \[
   a^{-b} = \frac{1}{a^b}
   \]
   Example:  
   \[
   4.5^{-3} = \frac{1}{4.5^3}
   \]

3) **Base Case:**  
   \[
   a^0 = 1
   \]

---

### **Example Walkthrough: `power(4.5, 3)`**
```
power(4.5, 3) = 4.5 * power(4.5, 2)
power(4.5, 2) = 4.5 * power(4.5, 1)
power(4.5, 1) = 4.5 * power(4.5, 0)
power(4.5, 0) = 1
```
Final result:
\[
4.5^3 = 4.5 \times 4.5 \times 4.5 = 91.125
\]

---

### **Example Outputs**
#### **Input 1:**
```
Enter base: 4.5
Enter power: 3
```
#### **Output 1:**
```
4.5 ^ 3 = 91.125
```

#### **Input 2:**
```
Enter base: 4.5
Enter power: -3
```
#### **Output 2:**
```
4.5 ^ -3 = 0.010973936899862825
```

---

### **Function Call Count**
- For `power(4.5, 3)`, function calls:
  ```
  power(4.5, 3)
  power(4.5, 2)
  power(4.5, 1)
  power(4.5, 0)  # Base case
  ```
  **Total Calls = 4**

- For `power(4.5, -3)`, function calls:
  ```
  power(4.5, -3)
  power(4.5, 3)
  power(4.5, 2)
  power(4.5, 1)
  power(4.5, 0)  # Base case
  ```
  **Total Calls = 5**

---

### **Optimized Approach (Using Fast Exponentiation)**
The above approach has **O(b) time complexity**. To optimize, we can use **exponentiation by squaring**, reducing time complexity to **O(log b)**:

```python
def power_fast(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / power_fast(a, -b)
    half_power = power_fast(a, b // 2)
    if b % 2 == 0:
        return half_power * half_power
    else:
        return a * half_power * half_power
```

This method **reduces function calls significantly**, especially for large values of `b`. 
-------------------------------------------------------------------------------------------------------------------------------------------
Here’s how you can implement a **recursive function to reverse a number** in Python:  

---

### **Recursive Reverse Function**
```python
from math import log10

def rev(n, length=None):
    if n == 0:
        return 0
    if length is None:
        length = int(log10(n))  # Get the number of digits - 1
    return (n % 10) * (10 ** length) + rev(n // 10, length - 1)

# Taking user input
n = int(input('Enter any number: '))
print('Reverse Number:', rev(n))
```

---

### **Explanation**
We break the number into its **last digit** and the **remaining part**, reversing it recursively:
1. **Extract the last digit:** `n % 10`
2. **Multiply it by the appropriate power of 10** (based on length)
3. **Make a recursive call** with the remaining number `n // 10`
4. **Base case:** When `n == 0`, return 0

---

### **Example Execution: `rev(678)`**
```
rev(678, 2) = (8 * 10^2) + rev(67, 1)
rev(67, 1)  = (7 * 10^1) + rev(6, 0)
rev(6, 0)   = (6 * 10^0) + rev(0)
rev(0)      = 0
```
Final result:
\[
678 \to 876
\]

---

### **Output Examples**
#### **Input 1:**
```
Enter any number: 946
```
#### **Output 1:**
```
Reverse Number: 649
```

#### **Input 2:**
```
Enter any number: 12345
```
#### **Output 2:**
```
Reverse Number: 54321
```

---

### **Function Call Count**
For `rev(678)`, the calls are:
```
rev(678) -> rev(67) -> rev(6) -> rev(0)
```
**Total calls = 4**

For an `n`-digit number, **total calls = n + 1**.

This implementation ensures efficient recursion by determining the power of 10 dynamically. 
