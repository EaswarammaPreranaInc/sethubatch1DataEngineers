#programs on generatos
l = [x * x for x in range(5)]
print(l)
print(type(l))

s = {x * x for x in range(5)}
print(s)
print(type(s))

d = {x: x * x for x in range(5)}
print(d)
print(type(d))

g = (x * x for x in range(5))
print(g)
print(type(g))
```

### Breakdown:

1. **List Comprehension (`l`)**:
   ```python
   l = [x * x for x in range(5)]
   ```
   - This creates a **list** where each element is the square of numbers from `0` to `4`.
   - **Output**: `[0, 1, 4, 9, 16]`
   - **Type**: `<class 'list'>`

2. **Set Comprehension (`s`)**:
   ```python
   s = {x * x for x in range(5)}
   ```
   - This creates a **set** containing the squares of numbers from `0` to `4`.
   - **Output**: `{0, 1, 4, 9, 16}` (sets have unique elements and unordered representation)
   - **Type**: `<class 'set'>`

3. **Dictionary Comprehension (`d`)**:
   ```python
   d = {x: x * x for x in range(5)}
   ```
   - This creates a **dictionary** where keys are numbers from `0` to `4`, and values are their squares.
   - **Output**: `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}`
   - **Type**: `<class 'dict'>`

4. **Generator Expression (`g`)**:
   ```python
   g = (x * x for x in range(5))
   ```
   - This creates a **generator**, which is an iterator that generates values on demand.
   - **Output**: `<generator object <genexpr> at some_memory_location>`
   - **Type**: `<class 'generator'>`

### Final Output:
```
[0, 1, 4, 9, 16]
<class 'list'>
{0, 1, 4, 9, 16}
<class 'set'>
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>
<generator object <genexpr> at 0x...>
<class 'generator'>
```
--------------------------------------------------------------------------------------------------------------------------------

def f1():
    return 10
    return 20
    return 30

def f2():
    yield 10
    yield 20
    yield 30

# End of the function
print(f1())
print(f1())
print(f1())
print()

g = f2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
```

---

### **Explanation:**

#### **Function `f1()`**
```python
def f1():
    return 10
    return 20
    return 30
```
- The function **returns 10** and immediately exits.  
- The remaining `return` statements are **unreachable** and never executed.

**Output of `print(f1())` three times:**
```
10
10
10
```
(since `f1()` always returns `10` and exits)

---

#### **Function `f2()` (Generator Function)**
```python
def f2():
    yield 10
    yield 20
    yield 30
```
- A function using `yield` creates a **generator** instead of executing immediately.
- `yield` pauses execution and remembers its state, allowing iteration over the values one by one.

```python
g = f2()
print(next(g))  # First yield → 10
print(next(g))  # Second yield → 20
print(next(g))  # Third yield → 30
print(next(g))  # ERROR (No more values to yield)
```

**Output of `print(next(g))`:**
```
10
20
30
Traceback (most recent call last):
  File "<stdin>", line 16, in <module>
StopIteration
```
(The fourth `next(g)` call raises a `StopIteration` error because the generator is exhausted.)

---

### **Final Output:**
```
10
10
10

10
20
30
Traceback (most recent call last):
  File "<stdin>", line 16, in <module>
StopIteration
```
