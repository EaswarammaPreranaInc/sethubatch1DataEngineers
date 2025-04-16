from itertools import count  # Importing count from itertools to create infinite iterators

# Create a count iterator starting from 0
c = count()

print('While  loop')
# Using a while loop to print numbers from 0 to 9
while True:
    x = next(c)     # Get the next number from the iterator
    if x > 9:       # Stop when x exceeds 9
        break
    print(x)        # Print the current number

print('For  loop')
# Using a for loop with a new count iterator
for x in count():   # Start a fresh count from 0
    if x > 20:      # Stop when x exceeds 20
        break
    print(x)        # Print the current number

# end of for loop
# This line prints a label followed by the first element from a new count iterator
print('Element :  ', end='\t')  # Prints "Element :" and a tab, staying on the same line
print(next(count()))            # Starts a new count (from 0) and prints the first number (0)

# ⚠️ WARNING: This creates a new infinite iterator and tries to print all values using unpacking
# It will cause the program to hang or crash because count() is infinite
c = count()
print(*c)  # ❌ Avoid doing this! It will never stop printing numbers.
```

---

### Safe Version of the Last Line:
To print only the first few numbers safely:

from itertools import islice  # islice allows slicing an infinite iterator

c = count()
print(*islice(c, 10))  # Prints numbers 0 to 9
```
Outputs:
While  loop
0
1
2
3
4
5
6
7
8
9
For  loop
0
1
2
...
20
Element :  	0
0 1 2 3 4 5 6 7 8 9 10 11 12 ...
forever — it never ends because *c tries to unpack an infinite iterator.
-----------------------------------------------------------------------------------------
from itertools import count  # Import the count function from itertools

# Define a function 'disp' that takes an iterator 'cnt' and prints 4 next values from it
def disp(cnt):
    for i in range(4):                  # Loop 4 times
        print(next(cnt), end='\t')     # Print next value from the iterator with a tab
    print()                             # Move to the next line after 4 values

# Create a count iterator starting at 10 with default step 1
a = count(start=10)
disp(a)     # Expected: 10 11 12 13

# Create a count iterator starting at 10 with step 5
b = count(start=10, step=5)
disp(b)     # Expected: 10 15 20 25

# Create a count iterator starting at 10, stepping backward by 2.5
c = count(start=10, step=-2.5)
disp(c)     # Expected: 10.0 7.5 5.0 2.5

# Create a default count iterator starting from 0 with step 1
d = count()
disp(d)     # Expected: 0 1 2 3
```

---

 Output:
10	11	12	13	
10	15	20	25	
10.0	7.5	5.0	2.5	
0	1	2	3
```
-------------------------------------------------------------------------------------------------------------
  Let's walk through your code **step-by-step with detailed comments** and then see the **output**.

---

### ✅ Code with Comments:

```python
from itertools import count  # Import count to create an infinite iterator

cnt = count()  # Infinite counter starting from 0
list = [10, 20, 15, 18]  # A simple list of integers

# z1 is a zip object pairing list items with counter values: (10,0), (20,1), ...
z1 = zip(list, cnt)

print('While  loop')
# Looping through z1 using next() until it's exhausted
while True:
    try:
        print(next(z1))  # Get next pair
    except:
        break  # Stop when zip is exhausted (i.e., when list is fully consumed)

# z2 is another zip of the same list with the same counter (cnt continues from where it left off!)
z2 = zip(list, cnt)
print('for  loop')
for x in z2:
    print(x)

# z3 again zips list with cnt, which continues counting (not reset)
z3 = zip(list, cnt)
print('Next  element :  ', next(z3))  # Fetches the first zipped item
print('*z3 :  ', *z3)  # Unpacks and prints remaining zipped items

# z4 same again
z4 = zip(list, cnt)
print('Next  element  : ', next(z4))  # Another next() call on the zip object
```

---

### ⚠️ Important Note:
`cnt = count()` is a **single iterator**. Every time it is used in zip, it continues from where it left off. It doesn’t reset!

---

### Step-by-Step `cnt` Values:
- `cnt` starts from `0`
- Each zipped object (`z1`, `z2`, etc.) pairs the values from `list` with the **next values from `cnt`**
- `list = [10, 20, 15, 18]` has 4 elements, so each zip will consume 4 values from `cnt`

---

### Let's simulate what happens:

1. `z1 = zip(list, cnt)` — uses `cnt = 0,1,2,3`
   ```
   While  loop
   (10, 0)
   (20, 1)
   (15, 2)
   (18, 3)
   ```

2. `z2 = zip(list, cnt)` — now `cnt = 4,5,6,7`
   ```
   for  loop
   (10, 4)
   (20, 5)
   (15, 6)
   (18, 7)
   ```

3. `z3 = zip(list, cnt)` — now `cnt = 8,9,10,11`
   - `next(z3)` → `(10, 8)`
   - `*z3` → prints remaining:
     ```
     (20, 9)
     (15, 10)
     (18, 11)
     ```

4. `z4 = zip(list, cnt)` — now `cnt = 12,13,14,15`
   - `next(z4)` → `(10, 12)`

---

### ✅ Final Output:

```
While  loop
(10, 0)
(20, 1)
(15, 2)
(18, 3)
for  loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)
Next  element :   (10, 8)
*z3 :   (20, 9) (15, 10) (18, 11)
Next  element  :  (10, 12)
```
----------------------------------------------------------------------------------------
  Let's walk through this updated version of your code step-by-step with **comments**, then show the **final output**.

---

### ✅ Code with Comments:

```python
from itertools import count  # Import count to get an infinite counter

cnt = count()  # Create an infinite iterator starting at 0
list = [10, 20, 15, 18]  # A list with 4 elements

# z1 will pair each value from cnt with a value from list: (0,10), (1,20), ...
z1 = zip(cnt, list)

print('while  loop')
# Iterate over z1 using next() until StopIteration occurs
while True:
    try:
        print(next(z1))  # Print the next zipped item
    except:
        break  # Stop when the zip iterator is exhausted

# z2: zip list with cnt, but cnt continues from where it left off
z2 = zip(list, cnt)
print('for  loop')
for x in z2:
    print(x)

# z3: again zip cnt (continued) with list
z3 = zip(cnt, list)
print(next(z3))  # Print first item from z3
print(*z3)       # Print remaining items using unpacking

# z4: again zip list with cnt (continued)
z4 = zip(list, cnt)
print(next(z4))  # Print the first pair
```

---

### ⚠️ Key Note:

The **`cnt` iterator is shared and never reset**. Each call to `zip(..., cnt)` continues from where `cnt` left off.

---

### Let's trace how `cnt` is consumed:

#### Step-by-step:
- `z1 = zip(cnt, list)` → list has 4 elements, so cnt yields: `0, 1, 2, 3`
  - Output:
    ```
    (0, 10)
    (1, 20)
    (2, 15)
    (3, 18)
    ```

- `z2 = zip(list, cnt)` → list still has 4 elements, cnt continues: `4, 5, 6, 7`
  - Output:
    ```
    (10, 4)
    (20, 5)
    (15, 6)
    (18, 7)
    ```

- `z3 = zip(cnt, list)` → cnt now gives: `8, 9, 10, 11`
  - `next(z3)` → `(8, 10)`
  - `*z3` → prints the rest:
    ```
    (9, 20) (10, 15) (11, 18)
    ```

- `z4 = zip(list, cnt)` → cnt now gives: `12, 13, 14, 15`
  - `next(z4)` → `(10, 12)`

---

### ✅ Final Output:

```
while  loop
(0, 10)
(1, 20)
(2, 15)
(3, 18)
for  loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)
(8, 10)
(9, 20) (10, 15) (11, 18)
(10, 12)
```

---
----------------------------------------------------------------------------------------------
    Let's walk through this Python code step by step with **clear explanations**, and then show the **final output**. The program uses `zip`, `zip_longest`, and `time.sleep()`.

---

### ✅ Code with Comments:

```python
from itertools import zip_longest  # For zipping with fill value for missing elements
import time  # To add delay in output

# Define a function to print elements from a zip/zip_longest iterator
def disp(z):
    while True:
        try:
            print(next(z))       # Print one element at a time
            time.sleep(1)        # Pause for 1 second
        except:
            break                # Stop when iterator is exhausted

list = [10, 20, 30, 40]           # A list of 4 elements

# zip stops at the shortest iterable
z1 = zip(range(7), list)         # range(7) has 7 elements, list has 4 → zip stops at 4
print(type(z1))                  # <class 'zip'>
disp(z1)                         # Will print 4 (index, value) pairs

# zip_longest fills missing list values with None
z2 = zip_longest(range(7), list)  # list shorter than range(7) → fill with None
print(type(z2))                   # <class 'itertools.zip_longest'>
disp(z2)                          # Will print 7 (index, value) pairs, filling missing with None
```

---

### 🔍 What Happens Internally:

- `range(7)` = [0, 1, 2, 3, 4, 5, 6]
- `list` = [10, 20, 30, 40]

#### `zip(range(7), list)`
- Stops at the shortest input → 4 items
```
(0, 10)
(1, 20)
(2, 30)
(3, 40)
```

#### `zip_longest(range(7), list)`
- Continues for all 7 values in range
- Fills missing values from list with `None`:
```
(0, 10)
(1, 20)
(2, 30)
(3, 40)
(4, None)
(5, None)
(6, None)
```

---

### ✅ Final Output (with 1-second pause between each line):

```plaintext
<class 'zip'>
(0, 10)
(1, 20)
(2, 30)
(3, 40)
<class 'itertools.zip_longest'>
(0, 10)
(1, 20)
(2, 30)
(3, 40)
(4, None)
(5, None)
(6, None)
```
-------------------------------------------------------------------------------------------------
You're using `itertools.cycle`, which creates an **infinite loop** that keeps repeating the elements of the list `[10, 20, 30, 40]`.

---

### ✅ Code with Comments:

```python
import time
from itertools import cycle

list = [10, 20, 30, 40]
c = cycle(list)  # Infinite iterator: cycles through [10, 20, 30, 40] endlessly

print(type(c))   # Will print: <class 'itertools.cycle'>

while True:
    print(next(c))  # Prints next item in cycle: 10 → 20 → 30 → 40 → 10 → ...
    time.sleep(1)   # Pauses for 1 second between prints
```

---

### ✅ Output (with 1-second delay between lines):

```
<class 'itertools.cycle'>
10
20
30
40
10
20
30
40
10
20
...
```

🔁 And it **keeps repeating forever**. This is useful when you want to loop over a fixed pattern continuously.

---

### 🛑 Important:
This will **never stop** unless you:
- Manually interrupt it (Ctrl + C in terminal),
- Or modify the code to break after a few elements.

---

### ✅ Example: Print only 10 elements from the cycle (Safe Version):

```python
from itertools import cycle, islice
import time

list = [10, 20, 30, 40]
c = cycle(list)

for x in islice(c, 10):  # Limit to 10 items
    print(x)
    time.sleep(1)
```
-------------------------------------------------------------------------------------------------------
 You're using `itertools.repeat()` to create two repeat objects—one **finite** and one **infinite**. Let's walk through the code with **comments** and then show the **expected output**.

---

### ✅ Code with Comments:

```python
import time
from itertools import repeat

# First repeat object: repeat the value 25 exactly 3 times
r = repeat(25, times=3)
print('1st repeat object')

while True:
    try:
        print(next(r))      # Will print 25 three times
        time.sleep(1)
    except:
        break               # Will break when StopIteration is raised

# Second repeat object: infinite repeat of 'Hyd'
print('2nd repeat object')
r = repeat('Hyd')           # Infinite repeat (no 'times' argument)

while True:
    print(next(r))          # Will print 'Hyd' forever
    time.sleep(1)
```

---

### ✅ Output:

```
1st repeat object
25
25
25
2nd repeat object
Hyd
Hyd
Hyd
Hyd
Hyd
Hyd
... (keeps going forever, one per second)
```

---

### 🛑 Note:
The **second loop is infinite** and will **never stop** unless interrupted (e.g., by pressing `Ctrl + C` or closing the program).

---

### ✅ Safer Version (Optional):

If you want a version that doesn’t run forever:

```python
from itertools import repeat, islice
import time

print('1st repeat object')
for x in repeat(25, times=3):
    print(x)
    time.sleep(1)

print('2nd repeat object')
for x in islice(repeat('Hyd'), 5):  # Only take 5 repetitions
    print(x)
    time.sleep(1)
```
-------------------------------------------------------------------------------------------------------
 You're using `map()` along with `itertools.repeat()` to repeatedly apply the `pow` function to a sequence of values.

Let’s break it down step-by-step and then show the **final output**.

---

### ✅ Code with Comments:

```python
import time
from itertools import repeat

# m is a map object that applies pow(x, 2) for x in range(10)
# range(10) = 0, 1, 2, ..., 9
# repeat(2) = 2, 2, 2, ..., (infinite 2s)
# So m = pow(0,2), pow(1,2), ..., pow(9,2)

m = map(pow, range(10), repeat(2))  # pow(x, 2) → squares of numbers from 0 to 9

while True:
    try:
        print(next(m))        # Prints each result with 1 second delay
        time.sleep(1)
    except:
        break                 # Stops when map is exhausted
```

---

### 🔍 What `map(pow, range(10), repeat(2))` does:

It computes:

```
pow(0, 2) = 0
pow(1, 2) = 1
pow(2, 2) = 4
pow(3, 2) = 9
pow(4, 2) = 16
pow(5, 2) = 25
pow(6, 2) = 36
pow(7, 2) = 49
pow(8, 2) = 64
pow(9, 2) = 81
```

---

### ✅ Final Output (with 1-second delay between each line):

```plaintext
0
1
4
9
16
25
36
49
64
81
```

Then the program stops (since `range(10)` is exhausted).
-------------------------------------------------------------------------------------------------------------------
 You're working with `itertools.combinations` and `itertools.permutations`, which are used to generate all possible **combinations** and **permutations** of a given length from a list.

Let’s walk through your code step by step with comments and show the exact output.

---

### ✅ Code with Comments:

```python
import time

# A display function that prints items from any iterator, one per second
def disp(itr):
    while True:
        try:
            print(next(itr))
            time.sleep(1)
        except:
            break

from itertools import combinations, permutations

list = ['A', 'B', 'C', 'D']

# Get all 3-element combinations of the list
c = combinations(list, 3)
print('Different Combinations')
disp(c)

# Get all 3-element permutations of the list
p = permutations(list, 3)
print('Different Permutations')
disp(p)
```

---

### 🔍 Understanding the Outputs:

#### `combinations(list, 3)`
Gives all unique **groups of 3 elements**, in sorted order, **ignoring order** within the group:

```
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'D')
('B', 'C', 'D')
```

(4 combinations in total from 4 elements taken 3 at a time)

---

#### `permutations(list, 3)`
Gives all possible **arrangements** of 3 elements from the list, **order matters**:

There are `4P3 = 4 × 3 × 2 = 24` permutations:

```
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'B')
('A', 'C', 'D')
('A', 'D', 'B')
('A', 'D', 'C')
('B', 'A', 'C')
('B', 'A', 'D')
('B', 'C', 'A')
('B', 'C', 'D')
('B', 'D', 'A')
('B', 'D', 'C')
('C', 'A', 'B')
('C', 'A', 'D')
('C', 'B', 'A')
('C', 'B', 'D')
('C', 'D', 'A')
('C', 'D', 'B')
('D', 'A', 'B')
('D', 'A', 'C')
('D', 'B', 'A')
('D', 'B', 'C')
('D', 'C', 'A')
('D', 'C', 'B')
```

---

### ✅ Final Output:

```
Different Combinations
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'D')
('B', 'C', 'D')
Different Permutations
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'B')
('A', 'C', 'D')
('A', 'D', 'B')
('A', 'D', 'C')
('B', 'A', 'C')
('B', 'A', 'D')
('B', 'C', 'A')
('B', 'C', 'D')
('B', 'D', 'A')
('B', 'D', 'C')
('C', 'A', 'B')
('C', 'A', 'D')
('C', 'B', 'A')
('C', 'B', 'D')
('C', 'D', 'A')
('C', 'D', 'B')
('D', 'A', 'B')
('D', 'A', 'C')
('D', 'B', 'A')
('D', 'B', 'C')
('D', 'C', 'A')
('D', 'C', 'B')
```

Each line will be printed with a **1-second delay**, thanks to `time.sleep(1)`.
